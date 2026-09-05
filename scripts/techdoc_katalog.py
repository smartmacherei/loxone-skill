#!/usr/bin/env python3
r"""Katalog (references/bausteine-*.md) aus der TechDoc ergaenzen.

    py -3 scripts/techdoc_katalog.py <sys_DEU.zip|tdc_DEU.LxRes> [--skill DIR] [--apply]

A) Bausteine mit LxType in der TechDoc, aber ohne Katalogseite: je Baustein ein Abschnitt
   "### <Name> (`<LxType>`)" mit Eingaengen/Ausgaengen/Parametern [BELEGT-TECHDOC] am Ende der
   thematisch passenden Datei, unter "## Aus der TechDoc ergänzt". Eintraege ohne Konnektoren
   (Extensions, Geraete, Dialoge) landen als Tabelle in bausteine-geraete-erweiterungen.md.
B) Fuer vorhandene Katalogseiten: Konnektoren, die nur die TechDoc kennt (Standard-Kuerzel wie
   Off, Tr, Rem, O), als Tabelle "**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]" am Ende
   des Bausteinabschnitts.

Ohne --apply nur Bericht. Mit --apply idempotent: vorhandene TechDoc-Abschnitte und -Tabellen
werden ersetzt. Danach scripts/techdoc_abgleich.py erneut laufen lassen.
"""
import argparse
import datetime
import glob
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from decode_lxres import decode, load  # noqa: E402
import techdoc_abgleich as A  # noqa: E402

MARK_SECTION = "## Aus der TechDoc ergänzt"
MARK_TABLE = "**Weitere Konnektoren laut TechDoc**"
DEVICES_FILE = "bausteine-geraete-erweiterungen.md"
DIRNAME = {"E": "Eingang", "A": "Ausgang", "P": "Parameter"}
SECTION_TITLE = {"E": "Eingänge", "A": "Ausgänge", "P": "Parameter"}

# LxType -> Katalogdatei (nur fuer Bausteine ohne Seite; alles andere -> DEVICES_FILE)
TARGET = {
    "FlipFlop": "bausteine-logik-basis.md", "Greater": "bausteine-logik-basis.md", "Less": "bausteine-logik-basis.md",
    "StepSel": "bausteine-logik-basis.md", "Equal": "bausteine-logik-basis.md", "NotEqual": "bausteine-logik-basis.md",
    "HeatCentral": "bausteine-klima-heizung.md", "IRoomcontrol": "bausteine-klima-heizung.md",
    "Roomcontrol": "bausteine-klima-heizung.md", "Heatmixer": "bausteine-klima-heizung.md",
    "Fan": "bausteine-lueftung-klimaanlage.md",
    "CentralPresence": "bausteine-sicherheit-alarm.md", "Presence": "bausteine-sicherheit-alarm.md",
    "PresenceController": "bausteine-sicherheit-alarm.md",
    "LightController": "bausteine-beleuchtung.md", "LightsceneLearn": "bausteine-beleuchtung.md",
    "DaylightController": "bausteine-beleuchtung.md", "AutomaticScene": "bausteine-beleuchtung.md",
    "JalousieUpDown2": "bausteine-beschattung-fenster.md",
    "Energy": "bausteine-energie.md", "Power": "bausteine-energie.md", "Wallbox": "bausteine-energie.md",
    "Device Tablet": "bausteine-bedienung-taster.md", "TPDC": "bausteine-bedienung-taster.md",
    "Weed": "bausteine-tore-tueren-spezial.md",
    "Code16": "bausteine-system-schnittstellen.md", "Code8": "bausteine-system-schnittstellen.md",
    "Code4": "bausteine-system-schnittstellen.md",
}


# ---------------------------------------------------------------- TechDoc
def techdoc_full(path):
    root = ET.fromstring(decode(load(path, None)).decode("utf-8-sig"))
    tpl = {io.get("TemplateId"): io for t in root.findall("Templates") for io in t}
    blocks = {}
    for fb in root.findall("FunctionBlock"):
        lx = fb.get("LxType")
        if not lx:
            continue
        groups = []
        for g in fb.findall("IOGroup"):
            d = A.DIR.get(g.get("Type"))
            ios = []
            for io in g.findall("IO"):
                a = {**tpl.get(io.get("TemplateId", ""), ET.Element("x")).attrib, **io.attrib}
                if a.get("Name"):
                    ios.append(a)
            if d and ios:
                groups.append((d, ios))
        blocks[lx] = {"name": fb.get("Name", ""), "ct": fb.get("ControlType", ""), "short": fb.get("ShortDescription", ""),
                      "desc": fb.get("Description", ""), "link": fb.get("ShortLink", ""), "groups": groups,
                      "io": {d: {a["Name"]: a.get("ShortName", "") for a in ios} for d, ios in groups}}
        for d in "EAP":
            blocks[lx]["io"].setdefault(d, {})
    return blocks


def clean(s: str) -> str:
    s = (s or "").replace("$$BR$$", " ").replace("<br>", " ").replace("<BR>", " ")
    s = re.sub(r"</?(?:b|i|u|p|strong|em)>", "", s)     # HTML-Auszeichnung aus der TechDoc
    s = re.sub(r"\$\$LINK::([^@$]+)@@([^$]+)\$\$", r"\2 (\1)", s)
    s = s.replace("%d-%e", "1-n").replace("%d", "n").replace("%e", "n")
    s = re.sub(r"<([^<>\s]+)>", r"`<\1>`", s)          # <v>, <v.1> ... als Code
    s = s.replace("|", "\\|")
    return re.sub(r"\s+", " ", s).strip()


def kz_display(s: str) -> str:
    return (s or "").replace("%d-%e", "1-n").replace("%d", "n").replace("%e", "n")


def value_range(a: dict) -> str:
    lo, hi, unit = a.get("Min", ""), a.get("Max", ""), a.get("Unit", "")
    if lo == "" and hi == "":
        rng = "∞" if a.get("Unit") or a.get("Default") else ""
    elif lo != "" and hi != "":
        rng = f"{lo}…{hi}"
    elif lo != "":
        rng = f"≥ {lo}"
    else:
        rng = f"≤ {hi}"
    if unit:
        rng = (rng + " " + unit).strip()
    return rng or "–"


def io_table(ios, with_default: bool) -> str:
    head = "| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |" + (" Standard |" if with_default else "")
    sep = "|---|---|---|---|---|" + ("---|" if with_default else "")
    rows = [head, sep]
    for a in ios:
        row = "| {} | `{}` | {} | {} | {} |".format(kz_display(a.get("ShortName", "")) or "–", kz_display(a["Name"]),
                                                    clean(a.get("ShortDescription", "")) or "–",
                                                    clean(a.get("Description", "")) or "–", value_range(a))
        if with_default:
            row += " {} |".format(a.get("Default", "–") or "–")
        rows.append(row)
    return "\n".join(rows)


def block_markdown(lx: str, b: dict, version: str) -> str:
    out = [f"### {b['name']} (`{lx}`)", ""]
    desc = clean(b["desc"]) or clean(b["short"])
    if desc:
        out += [desc, ""]
    groups = dict(b["groups"])
    for d in "EAP":
        out.append(f"**{SECTION_TITLE[d]}** [BELEGT-TECHDOC]")
        if d in groups:
            out.append(io_table(groups[d], with_default=(d == "P")))
        else:
            out.append("[nicht vorhanden]")
        out.append("")
    out += ["**Eigenschaften** [OFFEN]", "Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.", "",
            "**Fallstricke** [OFFEN]", "Keine dokumentiert.", ""]
    src = f"Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config {version}), ControlType {b['ct']}"
    if b["link"]:
        src += f" · KB: https://{b['link']}"
    out += [src, "", "---", ""]
    return "\n".join(out)


def devices_table(items, version: str) -> str:
    out = ["| Name | LxType | ControlType | Beschreibung | KB |", "|---|---|---|---|---|"]
    for lx, b in items:
        link = f"https://{b['link']}" if b["link"] else "–"
        out.append("| {} | `{}` | {} | {} | {} |".format(b["name"], lx, b["ct"], clean(b["desc"]) or clean(b["short"]) or "–", link))
    return "\n".join(out)


# ---------------------------------------------------------------- Katalog-Text bearbeiten
def strip_generated(text: str) -> str:
    """Frueher erzeugte Abschnitte/Tabellen entfernen (Idempotenz)."""
    i = text.find("\n" + MARK_SECTION)
    if i >= 0:
        j = text.rfind("\n---", 0, i)
        text = text[: j if j >= 0 and i - j < 8 else i].rstrip() + "\n"
    lines, out, skip = text.splitlines(), [], False
    for l in lines:
        if l.startswith(MARK_TABLE):
            skip = True
            if out and out[-1] == "":
                out.pop()
            continue
        if skip:
            if l.strip() == "":
                skip = False
            continue
        out.append(l)
    return "\n".join(out) + "\n"


def canon(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower().replace("∆", "d").replace("δ", "d").replace("ϑ", "t")
    return s.strip()


def only_techdoc(cat_block: dict, td_block: dict):
    """TechDoc-Konnektoren, deren Kuerzel im Katalog fehlt: Liste (dir, io-dict)."""
    out = []
    for d, ios in td_block["groups"]:
        alts = set()
        for k in cat_block.get(d, set()):
            for x in A.kz_alts(k):
                x = canon(x)
                alts.add(x)
                alts.add(re.sub(r"\d+$", "", x))
        templ = {}
        for a in ios:
            k = canon(A.kz_td(a.get("ShortName", "")))
            if not k or "%" in k or k in alts or re.sub(r"\d+$", "", k) in alts:
                continue
            if "%" in (a.get("ShortName", "") + a.get("Name", "")):
                # nummerierte Vorlage (AQ%d): einmal listen, Anzahl zaehlen
                key = (d, a.get("ShortName", ""), a.get("Name", ""))
                if key in templ:
                    templ[key]["_count"] += 1
                    continue
                a = dict(a, _count=1)
                templ[key] = a
            out.append((d, a))
    for d, a in out:
        n = a.get("_count")
        if n and n > 1:
            a["ShortName"] = re.sub(r"%d(-%e)?", "1-%d" % n, a.get("ShortName", ""))
            a["Name"] = re.sub(r"%d(-%e)?", "1-%d" % n, a.get("Name", ""))
    return out


def find_block_span(lines, title: str):
    """(start, end) des Bausteinabschnitts 'title' in lines; end = Zeile vor naechster Ueberschrift <= Ebene oder '---'."""
    for i, l in enumerate(lines):
        m = re.match(r"^(#{2,4})\s+(.+?)\s*$", l)
        if m and re.sub(r"^[#\s]+", "", m.group(2)).strip() == title:
            lvl = len(m.group(1))
            for j in range(i + 1, len(lines)):
                m2 = re.match(r"^(#{2,4})\s+", lines[j])
                if lines[j].strip() == "---" or (m2 and len(m2.group(1)) <= lvl):
                    return i, j
            return i, len(lines)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("techdoc")
    ap.add_argument("--skill", default=os.path.join(os.path.dirname(__file__), ".."))
    ap.add_argument("--apply", action="store_true", help="Dateien schreiben (sonst nur Bericht)")
    ap.add_argument("--version", default=None, help="Config-Version fuer die Quellenangabe (Default: aus dem Pfad)")
    args = ap.parse_args()
    version = args.version or (re.search(r"Loxone Config ([\d.]+)", args.techdoc) or [None, "?"])[1]
    today = datetime.date.today().strftime("%d.%m.%Y")

    td = techdoc_full(args.techdoc)
    refs = os.path.join(args.skill, "references")
    files = sorted(glob.glob(os.path.join(refs, "bausteine-*.md")))
    texts = {os.path.basename(p): strip_generated(Path(p).read_text(encoding="utf-8")) for p in files}
    # Katalog aus dem bereinigten Text lesen (Tempdateien vermeiden: parse_catalog will Pfade)
    tmpdir = os.path.join(args.skill, ".techdoc_tmp")
    os.makedirs(tmpdir, exist_ok=True)
    for name, t in texts.items():
        Path(tmpdir, name).write_text(t, encoding="utf-8")
    catalog = A.parse_catalog(sorted(glob.glob(os.path.join(tmpdir, "bausteine-*.md"))))
    for p in glob.glob(os.path.join(tmpdir, "*")):
        os.remove(p)
    os.rmdir(tmpdir)

    matched, _fuzzy, by_name = A.match_blocks(catalog, td)
    used = set(matched.values())
    covered = {A.norm(td[lx]["name"]) for lx in used}
    missing = [lx for lx in sorted(td) if lx not in used and A.norm(td[lx]["name"]) not in covered]

    # ---- A: fehlende Bausteine
    additions = {}
    devices = []
    for lx in missing:
        b = td[lx]
        if not b["groups"]:
            devices.append((lx, b))
            continue
        additions.setdefault(TARGET.get(lx, DEVICES_FILE), []).append(lx)
    report = ["# techdoc_katalog: Bericht", f"TechDoc {version}, {len(td)} Bausteine; Katalog {len(catalog)} Seiten, {len(matched)} zugeordnet.", ""]
    for fname, lxs in sorted(additions.items()):
        report.append(f"A) {fname}: +{len(lxs)} Bausteine: " + ", ".join(f"`{x}`" for x in lxs))
    report.append(f"A) {DEVICES_FILE}: {len(devices)} Einträge ohne Konnektoren (Tabelle)")

    # ---- B: weitere Konnektoren
    extra = {}
    for name, lx in sorted(matched.items()):
        rows = only_techdoc(catalog[name], td[lx])
        if rows:
            extra[name] = (catalog[name]["file"], lx, rows)
    report.append("")
    report.append(f"B) {len(extra)} Katalogseiten bekommen eine Tabelle 'Weitere Konnektoren laut TechDoc':")
    for name, (fname, lx, rows) in extra.items():
        report.append(f"   - {name} (`{lx}`, {fname}): " + ", ".join(f"{d}:{kz_display(a.get('ShortName',''))}" for d, a in rows))

    if not args.apply:
        sys.stdout.reconfigure(encoding="utf-8")
        print("\n".join(report))
        print("\n(kein --apply: nichts geschrieben)")
        return

    # B einfuegen (von unten nach oben je Datei, damit Zeilennummern stimmen)
    for fname in texts:
        lines = texts[fname].splitlines()
        todo = [(name, lx, rows) for name, (f, lx, rows) in extra.items() if f == fname]
        spans = []
        for name, lx, rows in todo:
            span = find_block_span(lines, name)
            if span:
                spans.append((span, name, lx, rows))
            else:
                report.append(f"   ! Abschnitt '{name}' in {fname} nicht gefunden - Tabelle nicht eingefuegt")
        for (s, e), name, lx, rows in sorted(spans, key=lambda x: -x[0][1]):
            tbl = [MARK_TABLE + " [BELEGT-TECHDOC]",
                   "| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |", "|---|---|---|---|---|---|"]
            for d, a in rows:
                tbl.append("| {} | `{}` | {} | {} | {} | {} |".format(
                    kz_display(a.get("ShortName", "")) or "–", kz_display(a["Name"]), DIRNAME[d],
                    clean(a.get("ShortDescription", "")) or "–", clean(a.get("Description", "")) or "–", value_range(a)))
            # vor die Abschlusszeile (---/naechste Ueberschrift), mit Leerzeile davor und danach
            k = e
            while k > s and lines[k - 1].strip() == "":
                k -= 1
            lines[k:k] = [""] + tbl + ([""] if k >= len(lines) or lines[k].strip() != "" else [])
        texts[fname] = "\n".join(lines).rstrip("\n") + "\n"

    # A anhaengen
    intro = (f"Stand {today}, Loxone Config {version}. Diese Bausteine haben keine eigene Seite in der KB-Kategorie "
             "„Funktionsbausteine\"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des "
             "Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und "
             "Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, "
             "sondern das Skript nach einem Config-Update erneut laufen lassen.")
    for fname, lxs in additions.items():
        body = "\n".join(block_markdown(lx, td[lx], version) for lx in lxs)
        texts.setdefault(fname, "")
        texts[fname] = texts[fname].rstrip("\n") + "\n\n---\n\n" + MARK_SECTION + "\n\n" + intro + "\n\n" + body
    dev_text = texts.get(DEVICES_FILE)
    if dev_text is None or not dev_text.strip():
        dev_text = ("# Geräte, Extensions und Systemobjekte — aus der TechDoc\n"
                    "Teil des Loxone-Baustein-Katalogs. Quelle: maschinenlesbare Bausteindoku des Config-Pakets "
                    "([techdoc-lxres.md](techdoc-lxres.md)). Erzeugt von `scripts/techdoc_katalog.py`.\n")
    dev_text = dev_text.rstrip("\n") + "\n\n---\n\n" + MARK_SECTION + "\n\n" + intro + "\n\n"
    if additions.get(DEVICES_FILE):
        pass  # Bausteine mit Konnektoren stehen schon oben im additions-Block
    dev_text += ("### Einträge ohne Konnektoren\n\nExtensions, Geräte und Systemobjekte: die TechDoc kennt zu ihnen Name und "
                 "Beschreibung, aber keine Ein-/Ausgänge (ihre Klemmen entstehen erst mit dem Gerät im Projekt).\n\n"
                 + devices_table(devices, version) + "\n")
    texts[DEVICES_FILE] = dev_text

    for fname, t in texts.items():
        Path(refs, fname).write_text(t, encoding="utf-8", newline="\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(report))
    print(f"\n{len(texts)} Dateien geschrieben.")


if __name__ == "__main__":
    main()
