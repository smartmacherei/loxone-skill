#!/usr/bin/env python3
r"""Abgleich: TechDoc (Config-Paket) gegen den Skill-Katalog und die XML-Doku-Zuordnung.

    py -3 scripts/techdoc_abgleich.py <sys_DEU.zip|tdc_DEU.LxRes> [--skill <Skill-Ordner>] [-o report.md]

Prueft
  A) references/xml-doku-mapping.md   - je Zeile: gibt es den XML-Konnektor in TechDoc, stimmt das Kuerzel?
  B) references/bausteine-*.md         - je Baustein (Name): Kuerzelmengen E/A/P gegen TechDoc
  C) Luecken in beide Richtungen       - TechDoc-LxTypes ohne Katalogseite, Katalogseiten ohne TechDoc-Treffer
Nach jedem Config-Update erneut laufen lassen; Ergebnis nach references/techdoc-abgleich.md.
"""
import argparse
import difflib
import glob
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from decode_lxres import decode, load  # noqa: E402

DIR = {"Input": "E", "Output": "A", "Parameter": "P"}
# Katalogname (KB-Seite) -> TechDoc-Name (DEU), wo beide auseinanderlaufen
ALIAS: dict[str, str] = {
    "Tastschalter": "Taster",
    "Touch & Grill Baustein": "Touch & Grill",
    "Saunasteuerung mit Verdampfer": "Saunasteuerung Verdampfer",
    "Sequenzer": "Sequencer",
    "Programm (Baustein)": "Programm",
    "Zähler & Speicher": "Zähler für Speicher",
    "Impulszähler & Speicher": "Impulszähler für Speicher",
}
# Katalog-Ueberschriften, die keine Bausteine sind
SKIP = re.compile(r"^(Zusammenfassung|Notizen|Besonderheiten|Sonderzeichen|Praxis:|Logische Bausteine|Statusbausteine|"
                  r"Speicher und Zeitbausteine|Flanken- und Zeitbausteine|Vergleichsbausteine|Impulsschalter$|Binär-Kodierung$)")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").strip().lower()
    s = re.sub(r"^(?:\d+\.|baustein \d+:)\s*", "", s)   # "1. Addierer", "Baustein 3: ..."
    s = re.sub(r"\s*\(baustein\)$", "", s)
    return re.sub(r"[\s\-–/&]+", "", s)


def kz_alts(raw: str) -> set[str]:
    """Skill-Kuerzel -> vergleichbare Grundformen. (Off)->{off}; Lc1-8->{lc1-8, lc}; A oder Anp->{a, anp}."""
    raw = re.sub(r"[`*()]", "", raw or "").strip()
    out = set()
    for alt in re.split(r"\s+oder\s+|\s*/\s*(?=[A-Za-z])", raw):
        alt = alt.strip()
        if not alt or alt in ("–", "-", "—", "−"):
            continue
        out.add(alt.lower())
        m = re.match(r"^(.*?[A-Za-z/])\s*\d+\s*(?:[-–…]\s*[A-Za-z]*\d+)?$", alt)
        if m:
            out.add(m.group(1).lower())
    return out


def kz_td(raw: str) -> str:
    """TechDoc-Kuerzel -> Grundform: Lc%d-%e -> lc, T5/%d-%e -> t5/, H%d-%e -> h."""
    return re.sub(r"%d-%e|%d|%e", "", raw or "").rstrip("-").lower()


def techdoc(path: str):
    root = ET.fromstring(decode(load(path, None)).decode("utf-8-sig"))
    tpl = {io.get("TemplateId"): io for t in root.findall("Templates") for io in t}
    blocks = {}
    for fb in root.findall("FunctionBlock"):
        if not fb.get("LxType"):
            continue
        ios = {"E": {}, "A": {}, "P": {}}
        for g in fb.findall("IOGroup"):
            d = DIR.get(g.get("Type"))
            for io in g.findall("IO"):
                a = {**tpl.get(io.get("TemplateId", ""), ET.Element("x")).attrib, **io.attrib}
                if a.get("Name"):
                    ios[d][a["Name"]] = a.get("ShortName", "")
        blocks[fb.get("LxType")] = {"name": fb.get("Name", ""), "io": ios}
    return blocks


def parse_mapping(path: str):
    out, cur = {}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"### `([A-Za-z0-9_]+)`", line)
        if m:
            cur = m.group(1)
            out[cur] = []
            continue
        if cur and line.startswith("| `"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            xml = re.sub(r"`", "", cells[0]).split(" ")[0].split("(")[0]
            kz = re.sub(r"`", "", cells[1]).strip()
            if kz in ("–", "-", "—", ""):
                continue
            out[cur].append((xml, kz, cells[3], cells[4]))
    return out


def parse_catalog(paths):
    out = {}
    for p in paths:
        block, sec = None, None
        for line in Path(p).read_text(encoding="utf-8").splitlines():
            m = re.match(r"^## #{0,3}\s*(.+?)\s*$", line)
            if m:
                block, sec = m.group(1), None
                if SKIP.match(block):
                    block = None
                    continue
                out[block] = {"E": set(), "A": set(), "P": set(), "file": os.path.basename(p)}
                continue
            m = re.match(r"^### (Eingänge|Ausgänge|Parameter)", line)
            if m and block:
                sec = {"Eingänge": "E", "Ausgänge": "A", "Parameter": "P"}[m.group(1)]
                continue
            if line.startswith("### "):
                sec = None
            if block and sec and line.startswith("| ") and not line.startswith("| Kürzel") and not line.startswith("|--"):
                kz = line.strip().strip("|").split("|")[0].strip().strip("`")
                if kz and kz not in ("-", "–", "−"):
                    out[block][sec].add(kz)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("techdoc")
    ap.add_argument("--skill", default=os.path.join(os.path.dirname(__file__), ".."))
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    td = techdoc(args.techdoc)
    by_name = {}
    for lx, v in td.items():
        by_name.setdefault(norm(v["name"]), lx)
    refs = os.path.join(args.skill, "references")
    mapping = parse_mapping(os.path.join(refs, "xml-doku-mapping.md"))
    catalog = parse_catalog(sorted(glob.glob(os.path.join(refs, "bausteine-*.md"))))
    L = ["# TechDoc-Abgleich (generiert von scripts/techdoc_abgleich.py)", ""]

    # ---- A
    A = []
    ok = bad = missing = 0
    for lx, rows in mapping.items():
        b = td.get(lx)
        if not b:
            A.append(f"| `{lx}` | – | – | – | LxType nicht in TechDoc |")
            continue
        allio = {n: s for d in "EAP" for n, s in b["io"][d].items()}
        for xml, kz, rich, status in rows:
            hit = allio.get(xml)
            if hit is None:
                hit = allio.get(re.sub(r"\d+$", "%d", xml))
            if hit is None:
                missing += 1
                A.append(f"| `{lx}` | `{xml}` | `{kz}` | – | nicht in TechDoc (Eigenschaft statt Konnektor?) |")
            elif kz_td(hit) in kz_alts(kz) or hit.lower() in kz_alts(kz):
                ok += 1
            else:
                bad += 1
                A.append(f"| `{lx}` | `{xml}` | `{kz}` | `{hit}` | **weicht ab** ({status}) |")
    L += ["## A. xml-doku-mapping.md gegen TechDoc", "",
          f"{ok} Zuordnungen bestätigt, **{bad} abweichend**, {missing} XML-Namen ohne TechDoc-Konnektor. Nur Abweichungen gelistet.", "",
          "| LxType | XML-Konnektor | Kürzel Skill | Kürzel TechDoc | Befund |", "|---|---|---|---|---|"] + A

    # ---- B
    matched, unmatched, fuzzy = {}, [], {}
    for name in catalog:
        lx = by_name.get(norm(ALIAS.get(name, name)))
        if not lx:
            cand = difflib.get_close_matches(norm(name), list(by_name), n=1, cutoff=0.9)
            if cand:
                lx = by_name[cand[0]]
                fuzzy[name] = td[lx]["name"]
        if lx:
            matched[name] = lx
        else:
            unmatched.append(name)
    B, clean = [], 0
    for name, lx in sorted(matched.items()):
        c, t = catalog[name], td[lx]["io"]
        only_c, only_t = [], []
        for d in "EAP":
            tk = {kz_td(s) for s in t[d].values() if s}
            ck = {k: kz_alts(k) for k in c[d]}
            ck_all = set().union(*ck.values()) if ck else set()
            only_c += [f"{d}:{k}" for k, alts in sorted(ck.items()) if alts and not (alts & tk)]
            only_t += [f"{d}:{k}" for k in sorted(tk - ck_all) if k]
        if only_c or only_t:
            B.append(f"| {name} | `{lx}` | {', '.join(only_c) or '–'} | {', '.join(only_t) or '–'} |")
        else:
            clean += 1
    L += ["", "## B. Katalog (bausteine-*.md) gegen TechDoc", "",
          f"{len(catalog)} Katalogseiten, {len(matched)} einem TechDoc-LxType zugeordnet ({len(fuzzy)} davon über Namensähnlichkeit), {len(unmatched)} ohne Treffer.",
          f"**{clean} Bausteine stimmen in allen Kürzeln überein.** Abweichungen:", ""]
    if fuzzy:
        L += ["Unscharfe Namenstreffer: " + "; ".join(f"{k} → {v}" for k, v in sorted(fuzzy.items())), ""]
    L += ["| Baustein | LxType | Kürzel nur im Katalog | Kürzel nur in TechDoc |", "|---|---|---|---|"] + B

    # ---- C
    L += ["", "## C. Lücken", "", "### Katalogseiten ohne TechDoc-Treffer", ""]
    for n in sorted(unmatched):
        sug = difflib.get_close_matches(norm(n), list(by_name), n=2, cutoff=0.6)
        L.append(f"- {n} ({catalog[n]['file']}) → " + (", ".join(f"`{by_name[x]}` ({td[by_name[x]]['name']})" for x in sug) or "kein Vorschlag"))
    used = set(matched.values())
    rest = [lx for lx in sorted(td) if lx not in used]
    L += ["", f"### TechDoc-LxTypes ohne Katalogseite ({len(rest)})", ""]
    L += [f"- `{lx}` — {td[lx]['name']}" for lx in rest]
    text = "\n".join(L) + "\n"
    if args.out:
        open(args.out, "w", encoding="utf-8", newline="\n").write(text)
        print("->", args.out)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
