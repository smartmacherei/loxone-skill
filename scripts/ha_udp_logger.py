#!/usr/bin/env python3
r"""Klemmen eines Loxone-Programms per Logger-Objekt (UDP) in Echtzeit nach aussen melden.

Verifiziert 05.09.2026 am Miniserver Gen 2, FW 17.1.6.30 (Demo-Koffer):
  * Der Miniserver wertet <LoggerMailer> NUR an Objekten vom Typ OutputRefLM aus - also an der
    Logger-Referenz, die Config beim Ziehen eines Loggers auf eine Seite anlegt. Eine
    <LoggerMailer RefLogger=...>-Zeile direkt an einer Klemme oder an einem Funktionsbaustein
    wird ignoriert (77 Klemmen + 1 Baustein getestet, null Meldungen).
  * Deshalb legt dieses Skript eine eigene Programmseite an und stellt je Klemme ein
    OutputRefLM darauf, dessen Eingang AI direkt vom Wert-Konnektor der Klemme gespeist wird
    (Q bei digitalen, AQ bei analogen Eingaengen; bei Ausgaengen vom Konnektor, der den Ausgang
    speist). Meldungstext: "<uuid>;<v>".
  * Ein Logger mit Adresse /dev/udp/<ip>/<port> sendet bei jeder Aenderung sofort ein UDP-Paket
    "<JJJJ-MM-TT hh:mm:ss>;<Logger-Titel>;<Meldungstext>\r\n" (Quellport = Zielport) und schreibt
    NICHT auf die SD-Karte. Broadcast-Adressen funktionieren.

Aufruf (Programm zuerst aus dem Miniserver ziehen - nie aus einer alten lokalen Datei):
    py -3 ha_udp_logger.py sps_0272_<ts>.zip --target 192.168.0.223:55555 -o sps_new.zip
    py -3 ha_udp_logger.py --from-miniserver 192.168.0.186 --user admin --password-env LOX_PW \
        --target 192.168.0.223:55555 -o sps_new.zip [--upload] [--restart]
    py -3 ha_udp_logger.py Projekt.Loxone --target 192.168.0.223:55555 -o Projekt_udp.Loxone

--upload legt die Datei per FTP als /prog/sps_new.zip ab, --restart ruft dev/sps/restart; genau
das tut auch Loxone Config beim "In Miniserver speichern" (siehe references/miniserver-dateizugriff.md).
Danach in Config "Aus Miniserver laden", sonst ueberschreibt der naechste Config-Upload alles wieder.
Keine Fremdbibliothek noetig; mit installiertem Paket `lz4` wird echt komprimiert, sonst als
LZ4-Literalblock geschrieben (gueltig, nur groesser).
"""
import argparse
import base64
import datetime
import ftplib
import io
import os
import re
import struct
import sys
import urllib.request
import zipfile
import zlib
import xml.etree.ElementTree as ET

MAGIC = 0xAABBCCEE
# Klemmentypen wie in der HA-Integration (topology._READ_TERMINALS)
TERMINAL_TYPES = ("DigitalIn", "VoltageIn", "Actor", "Online", "TreeSensor", "TreeAsensor", "TreeActor",
                  "TreeAactor", "LoxAIRsensor", "LoxAIRAsensor", "LoxAIRactor", "LoxAIRAactor")
ANALOG_OUT_TYPES = ("TreeAactor", "LoxAIRAactor")
DOC_SUFFIX_RE = re.compile(r'<C Type="Document" [^>]*?U="[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-([0-9a-f]{16})"')


# ---------------------------------------------------------------- LoxCC
def lz4_decompress(src: bytes, dst_size: int) -> bytes:
    out = bytearray()
    i, n = 0, len(src)
    while i < n:
        token = src[i]
        i += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[i]
                i += 1
                lit += b
                if b != 255:
                    break
        out += src[i:i + lit]
        i += lit
        if len(out) >= dst_size or i >= n:
            break
        off = src[i] | (src[i + 1] << 8)
        i += 2
        if off == 0:
            break
        mlen = (token & 15) + 4
        if (token & 15) == 15:
            while True:
                b = src[i]
                i += 1
                mlen += b
                if b != 255:
                    break
        start = len(out) - off
        for j in range(mlen):
            out.append(out[start + j])
    return bytes(out)


def lz4_compress(data: bytes) -> bytes:
    try:
        import lz4.block  # type: ignore
        return lz4.block.compress(data, mode="high_compression", store_size=False)
    except ImportError:
        pass
    # Literalblock: eine Sequenz, nur Literale (gueltiges LZ4-Blockformat, keine Kompression)
    n = len(data)
    out = bytearray([0xF0 if n >= 15 else n << 4])
    if n >= 15:
        rem = n - 15
        while rem >= 255:
            out.append(255)
            rem -= 255
        out.append(rem)
    return bytes(out) + data


def loxcc_decode(data: bytes) -> bytes:
    magic, comp, uncomp, crc = struct.unpack("<4I", data[:16])
    if magic != MAGIC:
        raise SystemExit("keine LoxCC-Datei")
    xml = lz4_decompress(data[16:], uncomp)
    if zlib.crc32(xml) & 0xFFFFFFFF != crc:
        print("WARNUNG: CRC32 des entpackten XML stimmt nicht", file=sys.stderr)
    return xml


def loxcc_encode(xml: bytes) -> bytes:
    comp = lz4_compress(xml)
    return struct.pack("<4I", MAGIC, len(comp), len(xml), zlib.crc32(xml) & 0xFFFFFFFF) + comp


# ---------------------------------------------------------------- Miniserver
class Miniserver:
    def __init__(self, host, user, password):
        self.base = "http://%s" % host
        self.host, self.user, self.password = host, user, password
        self.auth = "Basic " + base64.b64encode(("%s:%s" % (user, password)).encode()).decode()

    def get(self, path, timeout=30):
        req = urllib.request.Request(self.base + path, headers={"Authorization": self.auth})
        return urllib.request.urlopen(req, timeout=timeout).read()

    def newest_program(self):
        best, key = None, (-1, -1)
        for line in self.get("/dev/fslist/prog").decode().splitlines():
            m = re.search(r"(sps_\d+_(\d+)\.(LoxCC|zip))\s*$", line.strip())
            if m:
                k = (int(m.group(2)), 1 if m.group(3) == "LoxCC" else 0)
                if k > key:
                    key, best = k, m.group(1)
        if not best:
            raise SystemExit("kein sps_* in /prog")
        return best, self.get("/dev/fsget/prog/" + best, timeout=120)

    def ftp_put(self, name, data):
        try:
            ftp = ftplib.FTP_TLS(self.host, timeout=60)
            ftp.login(self.user, self.password)
            ftp.prot_p()
        except Exception:
            ftp = ftplib.FTP(self.host, timeout=60)
            ftp.login(self.user, self.password)
        ftp.cwd("/prog")
        res = ftp.storbinary("STOR " + name, io.BytesIO(data))
        ftp.quit()
        return res


# ---------------------------------------------------------------- XML-Helfer (textbasiert, kein Roundtrip)
def element_end(t: str, start: int) -> int:
    """Index hinter dem schliessenden Tag des <C>-Elements, das bei start beginnt."""
    tag_end = t.index(">", start)
    if t[tag_end - 1] == "/":
        return tag_end + 1
    depth, pos = 1, tag_end + 1
    pat = re.compile(r"<C\s|<C>|</C>")
    while depth:
        m = pat.search(t, pos)
        if not m:
            raise ValueError("unbalanced <C>")
        if m.group(0) == "</C>":
            depth -= 1
            pos = m.end()
        else:
            te = t.index(">", m.end())
            if t[te - 1] != "/":
                depth += 1
            pos = te + 1
    return pos


def find_c(t: str, type_: str, title=None):
    out = []
    for m in re.finditer(r'<C Type="%s"[ />]' % re.escape(type_), t):
        tag = t[m.start():t.index(">", m.start()) + 1]
        if title is None or 'Title="%s"' % xml_attr(title) in tag:
            out.append((m.start(), element_end(t, m.start())))
    return out


def xml_attr(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def loxone_epoch_now():
    now = datetime.datetime.now().replace(microsecond=0)
    utc = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
    return now.strftime("%Y-%m-%d %H:%M:%S"), int((utc - datetime.datetime(2009, 1, 1)).total_seconds())


# ---------------------------------------------------------------- Kern
def collect_terminals(xml: bytes, include_visu: bool, try_input_connector: bool):
    """Liste (uuid, title, type, source_connector_uuid, analog) fuer alle meldbaren Klemmen."""
    root = ET.fromstring(xml)
    out, skipped = [], []
    for el in root.iter("C"):
        ty = el.get("Type")
        if ty not in TERMINAL_TYPES:
            continue
        u, title = el.get("U"), el.get("Title") or el.get("IName") or el.get("U")
        iod, disp = el.find("IoData"), el.find("Display")
        unit = disp.get("Unit", "") if disp is not None else ""
        if not unit or "<v.i>" in unit:
            skipped.append((title, ty, "ungueltige/unbelegte Klemme"))
            continue
        if not include_visu and iod is not None and iod.get("Visu") == "true":
            skipped.append((title, ty, "Visu - pusht der WebSocket ohnehin"))
            continue
        cos = {co.get("K"): co for co in el.findall("Co")}
        src, analog = None, False
        if "AQ" in cos:
            src, analog = cos["AQ"].get("U"), True
        elif "Q" in cos:
            src = cos["Q"].get("U")
        elif "I" in cos:
            ins = cos["I"].findall("In")
            analog = ty in ANALOG_OUT_TYPES
            if ins:
                src = ins[0].get("Input")   # was den Ausgang speist
            elif try_input_connector:
                src = cos["I"].get("U")
        if not src:
            skipped.append((title, ty, "Ausgang ohne Quelle - nichts zu melden"))
            continue
        out.append((u, title, ty, src, analog))
    return out, skipped


def build(xml: bytes, target: str, page_title: str, include_visu: bool, bc, bc_uuids: set,
          try_input_connector: bool, replace: bool):
    t = xml.decode("utf-8")
    nl = "\r\n" if "\r\n" in t else "\n"
    suffix = DOC_SUFFIX_RE.search(t).group(1)
    date_str, date_s = loxone_epoch_now()
    used = set(re.findall(r'U="([0-9a-f-]{35})"', t))

    counter = [0]

    def uuid(kind="ffff", tail=None):
        """Objekt-UUIDs enden auf das 16-stellige Dokument-Suffix (ffff + 12 hex), Konnektor-UUIDs
        auf ein objekt-eigenes Suffix (00ff/01ff + 12 hex). Loxone-UUIDs sind 8-4-4-16 = 35 Zeichen."""
        counter[0] += 1
        last = suffix if tail is None else kind + tail
        u = "%08x-%04x-%04x-%s" % (date_s, counter[0] >> 16, counter[0] & 0xFFFF, last)
        if u in used:
            raise SystemExit("UUID-Kollision %s" % u)
        used.add(u)
        return u

    # vorhandene Seite/Logger gleichen Namens entfernen (Idempotenz)
    for ty, title in (("Page", page_title), ("Logger", page_title), ("Logger", page_title + " BC")):
        for s, e in reversed(find_c(t, ty, title)):
            if not replace:
                raise SystemExit("'%s' (%s) existiert schon - mit --replace ueberschreiben" % (title, ty))
            ls = t.rfind(nl, 0, s)
            t = t[:ls] + t[e:]

    terminals, skipped = collect_terminals(t.encode("utf-8"), include_visu, try_input_connector)
    if not terminals:
        raise SystemExit("keine meldbaren Klemmen gefunden")

    # Logger-Objekte in die Mitteilungen
    cap = find_c(t, "LoggerOutCaption")
    if not cap:
        raise SystemExit("LoggerOutCaption fehlt")
    cs, _ = cap[0]
    open_end = t.index(">", cs) + 1
    indent = t[t.rfind(nl, 0, cs) + len(nl):cs]
    ip, port = target.split(":")
    u_log = uuid()
    loggers = '%s%s\t<C Type="Logger" V="175" U="%s" Title="%s" WF="16384" Address="/dev/udp/%s/%s" MailSubjText=""/>' % (
        nl, indent, u_log, xml_attr(page_title), ip, port)
    u_bc = None
    if bc:
        bip, bport = bc.split(":")
        u_bc = uuid()
        loggers += '%s%s\t<C Type="Logger" V="175" U="%s" Title="%s BC" WF="16384" Address="/dev/udp/%s/%s" MailSubjText=""/>' % (
            nl, indent, u_bc, xml_attr(page_title), bip, bport)
    t = t[:open_end] + loggers + t[open_end:]

    # Seite mit OutputRefLM je Klemme (Seite ist Kind von <C Type="Program">)
    prog = find_c(t, "Program")
    if not prog:
        raise SystemExit('<C Type="Program"> fehlt')
    ps, pe = prog[0]
    pindent = t[t.rfind(nl, 0, ps) + len(nl):ps] + "\t"
    ind1, ind2, ind3 = pindent + "\t", pindent + "\t\t", pindent + "\t\t\t"
    page = ['%s<C Type="Page" V="175" U="%s" Title="%s" WF="16384">' % (pindent, uuid(), xml_attr(page_title))]
    cols = 4
    for i, (u, title, ty, src, analog) in enumerate(terminals):
        ref = u_bc if (u_bc and u.lower() in bc_uuids) else u_log
        px = 1344 + (i % cols) * 2688
        py = 576 + (i // cols) * 384
        tail = "%012x" % (int(date_s) * 4096 + i)
        page += [
            '%s<C Type="OutputRefLM" V="175" U="%s" Title="%s" Px="%d" Py="%d" Px2="%d" Py2="%d" Cl="0,0,0" Nio="2" Ref="%s" WF="147456"%s>'
            % (ind1, uuid(), xml_attr(title), px, py, px + 2112, py + 192, ref, ' Analog="true"' if analog else ""),
            '%s<Co K="AI" Nc="1" U="%s">' % (ind2, uuid("00ff", tail)),
            '%s<In Input="%s"/>' % (ind3, src),
            "%s</Co>" % ind2,
            '%s<Co K="AQ" U="%s"/>' % (ind2, uuid("01ff", tail)),
            '%s<LoggerMailer RefLogger="%s" On="%s;&lt;v&gt;" Off="%s;&lt;v&gt;" MinimumTime="0"/>' % (ind2, ref, u, u),
            "%s</C>" % ind1,
        ]
    page.append("%s</C>" % pindent)
    close_start = t.rfind(nl, 0, pe) + len(nl)
    t = t[:close_start] + nl.join(page) + nl + t[close_start:]

    # Document: Datum und Objektzahl (NumO = Anzahl der <C>-Elemente, sonst weist Config die Datei ab)
    numo = len(re.findall(r"<C ", t))
    t, n1 = re.subn(r'(<C Type="Document" [^>]*?) Date="[^"]*"', r'\1 Date="%s"' % date_str, t, count=1)
    t, n2 = re.subn(r'(<C Type="Document" [^>]*?) DateS="\d+"', r'\1 DateS="%d"' % date_s, t, count=1)
    t, n3 = re.subn(r'(<C Type="Document" [^>]*?) NumO="\d+"', r'\1 NumO="%d"' % numo, t, count=1)
    if not (n1 and n2 and n3):
        raise SystemExit("Document-Attribute Date/DateS/NumO nicht gefunden")
    return t.encode("utf-8"), terminals, skipped, date_str, u_log


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", help="sps_*.zip | *.LoxCC | *.xml | *.Loxone (oder --from-miniserver)")
    ap.add_argument("--from-miniserver", metavar="HOST", help="neuestes Programm per HTTP aus /prog holen")
    ap.add_argument("--user", default="admin")
    ap.add_argument("--password-env", default="LOX_PW", help="Umgebungsvariable mit dem Miniserver-Passwort")
    ap.add_argument("--target", required=True, help="UDP-Ziel ip:port, z.B. 192.168.0.223:55555")
    ap.add_argument("--broadcast", metavar="IP:PORT", help="zweiter Logger mit Broadcast-Ziel (Test/Vergleich)")
    ap.add_argument("--broadcast-uuids", default="", help="Klemmen-UUIDs (Komma), die an den Broadcast-Logger gehen")
    ap.add_argument("--title", default="HA UDP", help="Titel von Seite und Logger")
    ap.add_argument("--include-visu", action="store_true", help="auch Klemmen mit Visu-Haekchen melden")
    ap.add_argument("--try-input-connector", action="store_true",
                    help="Experiment: unverdrahtete Ausgaenge ueber ihren I-Konnektor")
    ap.add_argument("--replace", action="store_true", help="vorhandene Seite/Logger gleichen Titels ersetzen")
    ap.add_argument("-o", "--out", required=True, help="Ziel: .zip (fuer den Miniserver), .Loxone oder .xml")
    ap.add_argument("--upload", action="store_true", help="Ergebnis-ZIP per FTP als /prog/sps_new.zip ablegen")
    ap.add_argument("--restart", action="store_true",
                    help="danach dev/sps/restart (laedt sps_new.zip) - unterbricht die Anlage kurz!")
    args = ap.parse_args()

    ms = None
    if args.from_miniserver:
        pw = os.environ.get(args.password_env)
        if not pw:
            raise SystemExit("Passwort in %s setzen" % args.password_env)
        ms = Miniserver(args.from_miniserver, args.user, pw)
        name, raw = ms.newest_program()
        print("Miniserver-Programm:", name, len(raw), "Bytes")
    else:
        if not args.source:
            raise SystemExit("Quelle oder --from-miniserver angeben")
        name, raw = args.source, open(args.source, "rb").read()

    zin, member = None, None
    if name.lower().endswith(".zip"):
        zin = zipfile.ZipFile(io.BytesIO(raw))
        member = next(n for n in zin.namelist() if n.lower().startswith("sps") and n.lower().endswith(".loxcc"))
        xml = loxcc_decode(zin.read(member))
    elif name.lower().endswith(".loxcc"):
        xml = loxcc_decode(raw)
    else:
        xml = raw[3:] if raw.startswith(b"\xef\xbb\xbf") else raw

    bc_uuids = {u.strip().lower() for u in args.broadcast_uuids.split(",") if u.strip()}
    out_xml, terminals, skipped, date_str, u_log = build(
        xml, args.target, args.title, args.include_visu, args.broadcast, bc_uuids, args.try_input_connector, args.replace)
    print("%d Klemmen gemeldet, %d uebersprungen; Logger %s; Programmdatum %s" % (len(terminals), len(skipped), u_log, date_str))
    for title, ty, why in skipped:
        print("  - %-32s %-14s %s" % (title, ty, why))

    out = args.out
    if out.lower().endswith(".zip"):
        if zin is None:
            raise SystemExit("ZIP-Ausgabe braucht ein ZIP-Programm als Quelle (LoxAPP3.json, permissions.bin ...)")
        buf = io.BytesIO()
        now = datetime.datetime.now().timetuple()[:6]
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = zin.read(info.filename)
                if info.filename == member:
                    data = loxcc_encode(out_xml)
                elif info.filename == "LoxAPP3.json":
                    data = re.sub(rb'("lastModified"\s*:\s*")[^"]*"', lambda m: m.group(1) + date_str.encode() + b'"', data)
                zi = zipfile.ZipInfo(info.filename, date_time=now)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zout.writestr(zi, data)
        data = buf.getvalue()
        open(out, "wb").write(data)
        print("->", out, len(data), "Bytes")
        if args.upload:
            if ms is None:
                raise SystemExit("--upload braucht --from-miniserver")
            print("FTP:", ms.ftp_put("sps_new.zip", data))
            if args.restart:
                print("restart:", ms.get("/jdev/sps/restart").decode().strip())
    else:
        bom = b"\xef\xbb\xbf" if out.lower().endswith(".loxone") else b""
        open(out, "wb").write(bom + out_xml)
        print("->", out)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
