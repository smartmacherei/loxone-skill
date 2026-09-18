#!/usr/bin/env python3
"""Crawlt library.loxone.com und erzeugt references/library-katalog.json.

Die API ist lesend ohne Anmeldung erreichbar (POST, multipart/form-data).
Doku und Format: references/library-loxone-com.md

  py -3 scripts/library_crawl.py                 # Katalog neu erzeugen
  py -3 scripts/library_crawl.py --keep-tpl DIR  # Vorlagen zusätzlich ablegen

Die 701 Vorlagen sind zusammen unter 1 MB — das Ablegen kostet nichts, ist für den
Katalog aber nicht nötig.
"""
import argparse
import collections
import io
import json
import os
import re
import sys
import time
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

API = "https://api.library.loxone.com"
HDR = {"Origin": "https://library.loxone.com", "User-Agent": "Mozilla/5.0"}

# templateType -> Wurzelelement, verifiziert an 701 Vorlagen (18.09.2026)
TEMPLATE_TYPES = {
    "1": "VirtualInUdp", "2": "VirtualInHttp", "3": "VirtualOut", "4": "RC",
    "5": "Comm (RS232)", "6": "Comm (RS485)", "7": "Modbus", "20": "template (MP-Bus)",
}
CMD_TAGS = r"<(?:VirtualOutCmd|VirtualInHttpCmd|VirtualInUdpCmd|ModbusCmd|CommCmd|RCkey)\b"


def post(path, fields):
    b = "----b%d" % int(time.time() * 1000)
    body = b""
    for k, v in fields.items():
        body += ("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                 % (b, k, v)).encode()
    body += ("--%s--\r\n" % b).encode()
    h = dict(HDR)
    h["Content-Type"] = "multipart/form-data; boundary=%s" % b
    req = urllib.request.Request(API + path, data=body, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=60) as r:
        return r.read()


def safe_name(slug):
    """Vier Slugs enthalten ':' (z.B. pulse-eight-neo:4-1211). Unter Windows landet
    alles nach dem Doppelpunkt sonst in einem Alternate Data Stream - die Datei ist
    dann 0 Bytes gross und die vier ueberschreiben sich gegenseitig."""
    return re.sub(r'[<>:"/\\|?*]', "_", slug)


def scan_template(slug, keep_dir=None):
    """Laedt das Config-Beispiel und liest templateType, Wurzelelement, Befehlszahl."""
    try:
        raw = get("%s/downloader/config/%s" % (API, slug))
    except Exception:
        return {}
    if raw[:2] != b"PK":
        return {}
    if keep_dir:
        open(os.path.join(keep_dir, safe_name(slug) + ".LxAddon"), "wb").write(raw)
    try:
        z = zipfile.ZipFile(io.BytesIO(raw))
    except Exception:
        return {}
    for n in z.namelist():
        if not n.lower().endswith(".xml"):
            continue
        x = z.read(n).decode("utf-8-sig", "replace")
        tt = re.search(r'templateType="([^"]*)"', x)
        root = re.search(r"<([A-Za-z][A-Za-z0-9]*)[\s>]", x.split("?>", 1)[-1])
        return {"tt": tt.group(1) if tt else None,
                "root": root.group(1) if root else None,
                "ncmd": len(re.findall(CMD_TAGS, x))}
    return {}


def build(keep_dir=None):
    print("Liste laden ...", flush=True)
    src = post("/loadFilteredPlugins", {"filter": "{}", "orderby": "p.plugin_displayname",
                                        "order": "ASC", "limit": "0,5000"})
    print("  %d Einträge" % len(src), flush=True)

    # Kategorien kommen nicht in der Liste mit - je Kategorie ein gefilterter Aufruf.
    print("Kategorien zuordnen ...", flush=True)
    cat_of = collections.defaultdict(list)
    for cid, c in post("/loadCategories", {}).items():
        try:
            r = post("/loadFilteredPlugins", {"filter": json.dumps({"categories": [cid]}),
                                              "orderby": "p.id", "order": "ASC",
                                              "limit": "0,5000"})
        except Exception:
            continue
        for v in r.values():
            cat_of[v["id"]].append(c["value"])

    def one(item):
        key, v = item
        pid = key.split("-")[-1]
        e = {"n": v.get("name"), "slug": v.get("id"),
             "brand": (v.get("brands") or {}).get("value"),
             "tech": (v.get("technologies") or {}).get("value"),
             "cat": sorted(cat_of.get(v.get("id"), [])),
             "by": (v.get("creator") or {}).get("value"),
             "dl": 0, "cert": bool(v.get("certified")),
             "short": (v.get("short_description") or "")[:150]}
        try:  # plugin_id ist die ZAHL aus dem Listenschluessel, nicht der Slug
            d = post("/loadPluginDetail", {"plugin": pid, "plugin_id": pid, "lang": "de"})
            if isinstance(d, dict):
                e["dl"] = int(d.get("downloads") or 0)
        except Exception:
            pass
        e.update({k: v2 for k, v2 in scan_template(e["slug"], keep_dir).items() if v2 is not None})
        return e

    print("Details und Vorlagen holen ...", flush=True)
    out = []
    items = list(src.items())
    with ThreadPoolExecutor(max_workers=6) as ex:
        for i, e in enumerate(ex.map(one, items), 1):
            out.append(e)
            if i % 100 == 0:
                print("  %d/%d" % (i, len(items)), flush=True)

    out.sort(key=lambda e: (-e["dl"], (e["n"] or "").lower()))
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest = os.path.join(here, "references", "library-katalog.json")
    json.dump(out, open(dest, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

    tpl = sum(1 for e in out if "tt" in e)
    print("\n%s\n  %d Einträge, %d mit Vorlage, %d zertifiziert, %d Downloads"
          % (dest, len(out), tpl, sum(1 for e in out if e["cert"]),
             sum(e["dl"] for e in out)))
    for k, v in collections.Counter(e.get("tt") for e in out if "tt" in e).most_common():
        print("  templateType %-3s %-20s %4d" % (k, TEMPLATE_TYPES.get(k, "?"), v))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--keep-tpl", metavar="DIR", help="Vorlagen als .LxAddon hier ablegen")
    a = p.parse_args()
    if a.keep_tpl:
        os.makedirs(a.keep_tpl, exist_ok=True)
    build(a.keep_tpl)
