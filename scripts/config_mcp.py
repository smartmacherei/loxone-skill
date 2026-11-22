#!/usr/bin/env python3
"""Minimal client for the Loxone Config 17.3 "Config MCP" (Streamable HTTP, JSON-RPC).

Talks to the server directly, no MCP registration needed. Keeps the session id in a
state file next to this script per URL.

  py -3 config_mcp.py --url http://127.0.0.1:57707/mcp list
  py -3 config_mcp.py --url ... skill                      # agent skill (index)
  py -3 config_mcp.py --url ... skill skill://loxone-config-agent/references/wiring.md
  py -3 config_mcp.py --url ... query script.js            # code_query (read only)
  py -3 config_mcp.py --url ... run script.js [timeout_ms] # code_run (one undo step)
  py -3 config_mcp.py --url ... tool save_project '{"path": "C:\\\\x.Loxone"}'
"""
import argparse, hashlib, json, os, sys, tempfile, urllib.request


def _state(url):
    h = hashlib.sha1(url.encode()).hexdigest()[:10]
    return os.path.join(tempfile.gettempdir(), f"config_mcp_{h}.json")


def _post(url, obj, sid=None):
    h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if sid:
        h["Mcp-Session-Id"] = sid
    req = urllib.request.Request(url, data=json.dumps(obj).encode(), headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=600) as r:
        nsid, ct, body = r.headers.get("Mcp-Session-Id"), r.headers.get("Content-Type", ""), r.read().decode("utf-8", "replace")
    if "event-stream" in ct:
        msgs = [json.loads(l[5:]) for l in body.splitlines() if l.startswith("data:") and l[5:].strip()]
        hit = [m for m in msgs if m.get("id") == obj.get("id")]
        return nsid, (hit or msgs or [None])[-1]
    return nsid, (json.loads(body) if body.strip() else None)


class Client:
    def __init__(self, url):
        self.url, self.sf = url, _state(url)
        st = json.load(open(self.sf)) if os.path.exists(self.sf) else {}
        self.sid, self.n = st.get("sid"), st.get("n", 1)

    def _save(self):
        json.dump({"sid": self.sid, "n": self.n}, open(self.sf, "w"))

    def _init(self):
        self.sid, _ = _post(self.url, {"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
            "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "config_mcp.py", "version": "1"}}})
        _post(self.url, {"jsonrpc": "2.0", "method": "notifications/initialized"}, self.sid)
        self._save()

    def call(self, method, params=None, retry=True):
        if not self.sid:
            self._init()
        self.n += 1
        self._save()
        try:
            _, b = _post(self.url, {"jsonrpc": "2.0", "id": self.n, "method": method, "params": params or {}}, self.sid)
        except urllib.error.HTTPError as e:   # stale session after Config restart
            if retry and e.code in (400, 404):
                self.sid = None
                return self.call(method, params, False)
            raise
        return b

    def tool(self, name, **args):
        b = self.call("tools/call", {"name": name, "arguments": args})
        if not b or "result" not in b:
            return json.dumps(b, ensure_ascii=False)
        res = b["result"]
        out = [c.get("text") if c.get("type") == "text" else json.dumps(c) for c in res.get("content", [])]
        return ("[ERROR] " if res.get("isError") else "") + "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=os.environ.get("CONFIG_MCP_URL", "http://127.0.0.1:57707/mcp"))
    ap.add_argument("cmd", choices=["list", "skill", "query", "run", "tool"])
    ap.add_argument("args", nargs="*")
    a = ap.parse_args()
    c = Client(a.url)
    if a.cmd == "list":
        for t in c.call("tools/list")["result"]["tools"]:
            print(f"## {t['name']}\n  {t.get('description', '')[:300]}")
    elif a.cmd == "skill":
        print(c.tool("skill_read", **({"uri": a.args[0]} if a.args else {})))
    elif a.cmd in ("query", "run"):
        code = open(a.args[0], encoding="utf-8").read()
        to = int(a.args[1]) if len(a.args) > 1 else 60000
        print(c.tool("code_query" if a.cmd == "query" else "code_run", code=code, timeout_ms=to))
    else:
        print(c.tool(a.args[0], **(json.loads(a.args[1]) if len(a.args) > 1 else {})))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
