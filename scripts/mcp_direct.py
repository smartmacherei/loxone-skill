#!/usr/bin/env python3
"""Loxone-MCP-Server direkt ueber die LAN-IP ansprechen, ohne DNS und ohne MCP-Client.

Wozu: Hinter einer Fritz!Box loest der Name <ip>.<serial>.dyndns.loxonecloud.com wegen des
DNS-Rebind-Schutzes nicht auf, `claude mcp add` und der Browser kommen dann nicht hin. Dieses Skript
verbindet per TLS zur IP (SNI und Zertifikatspruefung gegen den Namen). Fuer den Login laeuft ein
Loopback-Proxy; das Passwort tippt der Benutzer im Browser, es wird weder gespeichert noch geloggt.

    py -3 mcp_direct.py <ip> login
    py -3 mcp_direct.py <ip> tools
    py -3 mcp_direct.py <ip> call control_find "{\"query\":\"Licht\"}"

Client, Token und Sitzung liegen unter %LOCALAPPDATA%\\lxmcp\\<ip>\\ (nicht im Skill-Ordner).
Einzeln und mit Abstand aufrufen, der Miniserver sperrt bei schnellen Anfragen bis zu 5 Minuten.
"""
import base64, hashlib, http.client, http.server, json, os, re, secrets, socket, ssl, sys, threading, time, urllib.parse, webbrowser

PORT = 41678
LOCAL = f"http://127.0.0.1:{PORT}"
REDIRECT = f"{LOCAL}/callback"
CTX = ssl.create_default_context()
IP = HOST = STATE = None


def discover_host(ip):
    """Der Name steht im WWW-Authenticate des 401, das Zertifikat der IP passt nicht dazu."""
    ctx = ssl._create_unverified_context()
    c = http.client.HTTPSConnection(ip, 443, context=ctx, timeout=20)
    c.request("GET", "/mcp")
    r = c.getresponse()
    r.read()
    m = re.search(r'resource_metadata="https://([^/"]+)/', r.getheader("WWW-Authenticate") or "")
    c.close()
    if not m:
        sys.exit(f"Kein MCP-Server auf {ip}: HTTP {r.status} (401 = laeuft, 404 = nicht da)")
    return m.group(1)


class Conn(http.client.HTTPSConnection):
    def connect(self):
        self.sock = CTX.wrap_socket(socket.create_connection((IP, 443), 20), server_hostname=HOST)


def req(method, path, body=None, headers=None):
    c = Conn(HOST, 443, context=CTX, timeout=60)
    c.request(method, path, body=body, headers=headers or {})
    r = c.getresponse()
    data = r.read()
    hdrs = r.getheaders()
    c.close()
    return r.status, hdrs, data


def path(name):
    return os.path.join(STATE, name)


def client_id():
    if not os.path.exists(path("client.json")):
        body = json.dumps({"client_name": "Claude Code Smartmacherei", "redirect_uris": [REDIRECT],
                           "grant_types": ["authorization_code", "refresh_token"], "response_types": ["code"],
                           "token_endpoint_auth_method": "none"})
        s, _, d = req("POST", "/mcp/oauth/register", body, {"Content-Type": "application/json"})
        if s not in (200, 201):
            sys.exit(f"register {s}: {d[:200]!r}")
        open(path("client.json"), "wb").write(d)
    return json.load(open(path("client.json"), encoding="utf-8"))["client_id"]


def login():
    cid = client_id()
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    done = threading.Event()
    result = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def page(self, code, text):
            b = text.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def forward(self, method):
            n = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(n) if n else None
            hdrs = {k: v for k, v in self.headers.items()
                    if k.lower() not in ("host", "accept-encoding", "connection", "content-length")}
            hdrs["Host"] = HOST
            for k in ("Origin", "Referer"):
                if k in hdrs:
                    hdrs[k] = hdrs[k].replace(LOCAL, f"https://{HOST}")
            status, rh, data = req(method, self.path, body, hdrs)
            ctype = dict((k.lower(), v) for k, v in rh).get("content-type", "")
            if "text/html" in ctype:
                # nur Navigationsziele umbiegen: das versteckte Feld "resource" muss unveraendert
                # bleiben, sonst antwortet der Server mit invalid_target
                data = re.sub(rb"""(action|href|src)=(["'])https://""" + re.escape(HOST.encode()),
                              lambda m: m.group(1) + b"=" + m.group(2) + LOCAL.encode(), data)
            self.send_response(status)
            for k, v in rh:
                kl = k.lower()
                if kl in ("content-length", "connection", "transfer-encoding", "content-security-policy",
                          "strict-transport-security"):
                    continue
                if kl == "location":
                    v = v.replace(f"https://{HOST}", LOCAL)
                if kl == "set-cookie":
                    v = v.replace("; Secure", "").replace("; secure", "")
                self.send_header(k, v)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            u = urllib.parse.urlparse(self.path)
            if u.path == "/":
                q = urllib.parse.urlencode({
                    "response_type": "code", "client_id": cid, "redirect_uri": REDIRECT,
                    "code_challenge": challenge, "code_challenge_method": "S256", "state": state,
                    "resource": f"https://{HOST}/mcp"})
                self.send_response(302)
                self.send_header("Location", f"/mcp/oauth/authorize?{q}")
                self.send_header("Content-Length", "0")
                self.end_headers()
            elif u.path == "/callback":
                q = urllib.parse.parse_qs(u.query)
                if q.get("state", [""])[0] != state or "code" not in q:
                    result["error"] = q.get("error", ["state/code fehlt"])[0]
                    self.page(400, "<h2>Anmeldung fehlgeschlagen</h2><p>%s</p>" % result["error"])
                else:
                    form = urllib.parse.urlencode({
                        "grant_type": "authorization_code", "code": q["code"][0], "redirect_uri": REDIRECT,
                        "client_id": cid, "code_verifier": verifier, "resource": f"https://{HOST}/mcp"})
                    s, _, d = req("POST", "/mcp/oauth/token", form,
                                  {"Content-Type": "application/x-www-form-urlencoded"})
                    if s == 200:
                        open(path("token.json"), "wb").write(d)
                        result["ok"] = True
                        self.page(200, "<h2>Anmeldung erfolgreich</h2><p>Dieses Fenster kann geschlossen werden.</p>")
                    else:
                        result["error"] = f"token {s}: {d[:200]!r}"
                        self.page(500, "<h2>Token-Abruf fehlgeschlagen</h2>")
                done.set()
            else:
                self.forward("GET")

        def do_POST(self):
            self.forward("POST")

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f"Login-Seite: {LOCAL}/", flush=True)
    webbrowser.open(f"{LOCAL}/")
    finished = done.wait(900)
    srv.shutdown()
    if not finished:
        sys.exit("Zeitueberschreitung: keine Anmeldung innerhalb 15 min")
    if not result.get("ok"):
        sys.exit(f"Fehler: {result.get('error')}")
    print("Token gespeichert", flush=True)


def refresh():
    t = json.load(open(path("token.json"), encoding="utf-8"))
    form = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": t["refresh_token"],
                                   "client_id": client_id(), "resource": f"https://{HOST}/mcp"})
    s, _, d = req("POST", "/mcp/oauth/token", form, {"Content-Type": "application/x-www-form-urlencoded"})
    if s != 200:
        sys.exit(f"refresh {s}: {d[:200]!r} - neu anmelden mit: login")
    open(path("token.json"), "wb").write(d)


def rpc(method, params=None, notify=False, retry=True):
    msg = {"jsonrpc": "2.0", "method": method}
    if params is not None:
        msg["params"] = params
    if not notify:
        msg["id"] = int(time.time() * 1000) % 1000000
    h = {"Authorization": "Bearer " + json.load(open(path("token.json"), encoding="utf-8"))["access_token"],
         "Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if os.path.exists(path("session.txt")):
        h["Mcp-Session-Id"] = open(path("session.txt")).read().strip()
    s, raw, d = req("POST", "/mcp", json.dumps(msg), h)
    rh = dict((k.lower(), v) for k, v in raw)
    if s == 401 and retry:
        refresh()
        return rpc(method, params, notify, False)
    if s == 429:
        sys.exit(f"429 rate_limited, retry-after {rh.get('retry-after')}")
    if s in (400, 404) and method != "initialize" and retry and os.path.exists(path("session.txt")):
        os.remove(path("session.txt"))
        init()
        return rpc(method, params, notify, False)
    if "mcp-session-id" in rh:
        open(path("session.txt"), "w").write(rh["mcp-session-id"])
    if notify:
        return None
    text = d.decode("utf-8", "replace")
    if "text/event-stream" in rh.get("content-type", ""):
        lines = [l[5:].strip() for l in text.splitlines() if l.startswith("data:")]
        text = lines[-1] if lines else ""
    if s >= 400 or not text:
        sys.exit(f"HTTP {s}: {text[:500]}")
    return json.loads(text)


def init():
    r = rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                           "clientInfo": {"name": "smartmacherei-mcp-direct", "version": "1"}})
    rpc("notifications/initialized", notify=True)
    return r


def main():
    global IP, HOST, STATE
    if len(sys.argv) < 3 or sys.argv[2] not in ("login", "tools", "call"):
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    IP = sys.argv[1]
    STATE = os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), "lxmcp", IP)
    os.makedirs(STATE, exist_ok=True)
    if os.path.exists(path("host.txt")):
        HOST = open(path("host.txt")).read().strip()
    else:
        HOST = discover_host(IP)
        open(path("host.txt"), "w").write(HOST)
    if sys.argv[2] == "login":
        return login()
    if not os.path.exists(path("token.json")):
        sys.exit("Kein Token: zuerst login")
    if not os.path.exists(path("session.txt")):
        init()
        time.sleep(1)
    if sys.argv[2] == "tools":
        print(json.dumps(rpc("tools/list"), ensure_ascii=False, indent=1))
    else:
        args = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
        print(json.dumps(rpc("tools/call", {"name": sys.argv[3], "arguments": args}), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
