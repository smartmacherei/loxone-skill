#!/usr/bin/env python3
r"""LxRes / LoxCC entpacken (Loxone Config TechDoc, Miniserver-Meldungstabelle, sps*.LoxCC).

Format: 16-Byte-Header (<4I: Magic 0xAABBCCEE, komprimierte Groesse, entpackte Groesse,
Pruefsumme) + LZ4-Block. Keine Fremdbibliothek noetig.

    py -3 decode_lxres.py tdc_DEU.LxRes                 -> tdc_DEU.LxRes.xml daneben
    py -3 decode_lxres.py tdc_DEU.LxRes --block AutoJalousie   -> Konnektortabelle als Markdown
    py -3 decode_lxres.py tdc_DEU.LxRes --list          -> alle LxTypes mit Namen

Fundort (Config 17.1.7.27):
    C:\ProgramData\Loxone\Loxone Config <Ver>\SDcard\sys\sys_DEU.zip  (DEU.LxRes, tdc_DEU.LxRes)
    ...\sys_ENG.zip  (ENG.LxRes, tdc_ENG.LxRes)
"""
import argparse
import struct
import sys
import zipfile
import xml.etree.ElementTree as ET

MAGIC = 0xAABBCCEE


def lz4_block(src: bytes, dst_size: int) -> bytes:
    out = bytearray()
    i, n = 0, len(src)
    while i < n:
        token = src[i]; i += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[i]; i += 1; lit += b
                if b != 255:
                    break
        out += src[i:i + lit]; i += lit
        if len(out) >= dst_size or i >= n:
            break
        offset = src[i] | (src[i + 1] << 8); i += 2
        if offset == 0:
            break
        mlen = (token & 0x0F) + 4
        if (token & 0x0F) == 15:
            while True:
                b = src[i]; i += 1; mlen += b
                if b != 255:
                    break
        start = len(out) - offset
        for j in range(mlen):
            out.append(out[start + j])
    return bytes(out)


def decode(data: bytes) -> bytes:
    magic, _comp, uncomp, _chk = struct.unpack("<4I", data[:16])
    if magic != MAGIC:
        raise SystemExit(f"keine LoxCC/LxRes-Datei (Magic 0x{magic:08x})")
    xml = lz4_block(data[16:], uncomp)
    if len(xml) != uncomp:
        print(f"WARNUNG: {len(xml)} statt {uncomp} Bytes entpackt", file=sys.stderr)
    return xml


def load(path: str, member: str | None) -> bytes:
    if path.lower().endswith(".zip"):
        with zipfile.ZipFile(path) as z:
            name = member or next(n for n in z.namelist() if n.lower().startswith("tdc_"))
            return z.read(name)
    return open(path, "rb").read()


def io_table(fb: ET.Element, templates: dict[str, ET.Element]) -> str:
    rows = ["| Gruppe | Id | XML-Name | Doku-Kürzel | Einheit | Min | Max | Default | Kurzbeschreibung |",
            "|---|---|---|---|---|---|---|---|---|"]
    for grp in fb.findall("IOGroup"):
        for io in grp.findall("IO"):
            a = dict(io.attrib)
            tpl = templates.get(a.get("TemplateId", ""))
            if tpl is not None:  # Template liefert die fehlenden Felder
                a = {**tpl.attrib, **a}
            rows.append("| {} | {} | `{}` | {} | {} | {} | {} | {} | {} |".format(
                grp.get("Type"), a.get("Id", ""), a.get("Name", "?"), a.get("ShortName", ""),
                a.get("Unit", ""), a.get("Min", ""), a.get("Max", ""), a.get("Default", ""),
                (a.get("ShortDescription") or "").replace("|", "/")))
    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help=".LxRes, .LoxCC oder sys_*.zip")
    ap.add_argument("-m", "--member", help="Dateiname im ZIP (Default: tdc_*)")
    ap.add_argument("-o", "--out", help="Ziel-XML (Default: <file>.xml)")
    ap.add_argument("--list", action="store_true", help="alle Bausteine mit LxType auflisten")
    ap.add_argument("--block", help="Konnektortabelle eines Bausteins (LxType oder Name)")
    args = ap.parse_args()

    xml = decode(load(args.file, args.member))
    if not (args.list or args.block):
        out = args.out or args.file + ".xml"
        open(out, "wb").write(xml)
        print(f"{len(xml)} Bytes -> {out}")
        return

    root = ET.fromstring(xml.decode("utf-8-sig"))
    templates = {io.get("TemplateId"): io for t in root.findall("Templates") for io in t}
    blocks = root.findall("FunctionBlock")
    if args.list:
        for fb in sorted(blocks, key=lambda f: f.get("LxType") or "~"):
            print(f"{fb.get('LxType') or '-':32} {fb.get('ControlType'):>5}  {fb.get('Name')}")
        return
    hits = [f for f in blocks if args.block in (f.get("LxType"), f.get("Name"))]
    if not hits:
        raise SystemExit(f"Baustein {args.block!r} nicht gefunden (--list zeigt alle)")
    for fb in hits:
        print(f"## {fb.get('Name')}  (LxType `{fb.get('LxType')}`, ControlType {fb.get('ControlType')})\n")
        print(io_table(fb, templates), "\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
