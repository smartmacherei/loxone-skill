# Loxone Config skill for Claude — Smartmacherei

Verified knowledge about Loxone Config projects for Claude Code / Claude Desktop skills:
file format, function blocks with their inputs/outputs/parameters, connectors,
Auto-Konfiguration, XML editing rules and the traps you otherwise learn by trial and error.
Content is in German (the language of the official Loxone documentation it was verified against).

Status: Loxone Config 17.1.7.27 · ControlList version 273

Additional project evidence (2026-09-09): ControlList 274, ConfigVersion `17020828`.
The [project audit](references/demo-project-audit.md) adds a sanitized structural
inventory of 223 XML types, including 31 page-block types absent from the existing
XML templates, and the observed native MCP plugin structure. These are project
observations, not factory defaults or a live compatibility test.

## Install

Copy this folder to your Claude skills directory so that `SKILL.md` sits at:

- Windows: `%USERPROFILE%\.claude\skills\loxone-config\SKILL.md`
- macOS / Linux: `~/.claude/skills/loxone-config/SKILL.md`

Restart Claude Code (or reload skills). The skill triggers automatically when you work with
`.Loxone` files or ask what a Loxone block can do — or invoke it with `/loxone-config`.

## Updates

New versions are announced to subscribers of the "Loxone skill" topic:
https://smartmacherei.at/en/downloads

## Licence

Free to use and modify. No warranty. Block documentation is paraphrased from the public
Loxone documentation; Loxone is a trademark of Loxone Electronics GmbH, which is not affiliated
with this skill.

---

Smartmacherei e.U. · Ing. Thomas Basting · Gnadlingerweg 11, 4650 Edt bei Lambach, Austria
office@smartmacherei.at · https://smartmacherei.at
