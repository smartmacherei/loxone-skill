# Config MCP (Loxone Config 17.3): Projekt in der laufenden Config bearbeiten und simulieren

**Verifiziert 22.11.2026** an Loxone Config **17.3.11.12** (Server „LOXONE Config“ 1.0.1), Kundenprojekt
(Gateway/Client, 47 Lichtsteuerungen umgebaut). Quelle der Funktion: offizieller Changelog 17.3.11.12
(<https://www.loxone.com/enen/support/changelog-config/>).

## Zwei verschiedene MCP-Server — nicht verwechseln

| | Miniserver-MCP ([mcp-server.md](mcp-server.md)) | **Config MCP (neu in 17.3)** |
|---|---|---|
| Läuft | auf dem Miniserver (Gen 2, Add-on) | **lokal in LoxoneConfig.exe** |
| Kann | Zustände lesen, Befehle senden | **Bausteine anlegen, verdrahten, parametrieren, löschen, Seiten ausrichten, speichern, simulieren** |
| Konfiguration ändern | nein | ja, jede Änderung läuft durch Config und ist per Undo rücknehmbar |
| Voraussetzung | Miniserver erreichbar | Config läuft **mit geöffnetem Projekt**, kein Miniserver nötig |

Einschalten: Titelleiste von Config → **Config MCP** → aktivieren, Port wählen. Config installiert und startet
den Server selbst. Endpunkt: `http://127.0.0.1:<port>/mcp` (Streamable HTTP, JSON-RPC). Eine reine
Kommandozeilen-/Headless-Simulation ohne laufende Config gibt es laut Release Notes **nicht**. CLI-Schalter von
LoxoneConfig.exe: nur `/Language=`, `/auto`, `/NewInstance` (bzw. `--language`, `--auto`, `--new-instance`).

## Ansprechen ohne MCP-Registrierung

Der Server muss nicht in Claude Code eingetragen werden. `scripts/config_mcp.py` spricht ihn direkt an
(initialize → `Mcp-Session-Id` merken → `tools/call`):

```powershell
py -3 'scripts\config_mcp.py' --url http://127.0.0.1:57707/mcp list
py -3 'scripts\config_mcp.py' --url http://127.0.0.1:57707/mcp query skript.js
```

Werkzeuge: `code_query` (nur lesen), `code_run` (lesen + ändern), `sdk_describe`, `skill_read`, `get_doc`,
`get_doc_resource`, `get_block_resource`, `save_project`, `undo`, `redo`.
**Zuerst `skill_read` ohne Argument lesen** — Config liefert einen eigenen, ausführlichen Agenten-Skill samt
9 Referenzen (`skill://loxone-config-agent/references/*.md`: block-configuration, wiring, page-layout,
simulation, errors-and-actions, inserting-objects, periphery, block-pictures, loxone-standard). Die SDK-Methoden
(`cfg.*`, snake_case) liefert `sdk_describe`.

## Was sich in der Praxis bewährt hat

- **Ein `code_run` = genau ein Undo-Schritt.** Je Baustein ein Skript; bricht es mittendrin ab, mit einem `undo`
  alles zurück (verifiziert: Teiländerung vollständig zurückgenommen).
- **Vor dem ersten Schreiben prüfen, welche Datei offen ist** (`cfg.get_project().project.filePath`). Auf eine
  Arbeitskopie umlenken mit `save_project({path})` — der Pfad wird danach der Projektpfad, die Ausgangsdatei
  bleibt bytegleich (SHA256 geprüft).
- **Drei Speicherorte für Werte:** Eigenschaftenfeld (`get/set_block_property`, Id oder Kürzel), Konnektor-Default
  (`set_default`, nur ohne Eigenschaftsfeld dauerhaft), Dialogdaten (`get/set_block_data`, z. B. Stimmungen).
  Bei Rechenbausteinen (`Mult`, `Sub` …) stehen `Input1`/`Input2` unter `connectors.parameters`, Ausgang `AQ`;
  V2 hat ein Eigenschaftsfeld (Id 401) → mit `set_block_property` schreiben.
- **Prüfung:** `cfg.validate_project()` → Regeln wie `UNCONFIGURED_CONTROL`, `MISSING_CONNECTIONS`,
  `CONVERTABLE_OBJ` („n Objekt(e) konvertierbar“ — zeigt Gen-1-Bausteine, für die Config selbst einen Konverter
  hat; im geprüften Kundenprojekt die 19 `IRoomcontrol`). Kein headless-Konverter für `IRoomcontrol` in `get_actions`.
- **Ausrichten:** `cfg.arrange_page({page_uuid})` = „Bausteine ausrichten“ (F11). Bewegt **keine Notizen**
  (`Text`) — die bleiben stehen und überlagern danach Bausteine. Überlauf → Fortsetzungsseite (`overflowPages`).
- **Simulation:** `sim_step`/`sim_run`/`sim_set_time`/`sim_set_value`. Zeit für Zeitglieder mit
  `sim_set_time` vorstellen (ISO mit Millisekunden: `toISOString().slice(0,23)`). Verbundene Eingänge sind nicht
  treibbar (`CONNECTOR_DRIVEN`) → Quelle treiben (VirtualIn, Merker, Referenz, auch Hardware-`DigitalIn` direkt).
  Datentyp beachten: digitale Objekte `true/false`, analoge Zahl — ein VirtualIn mit `Analog="false"` kann
  trotzdem eine Zahl verlangen, im Zweifel beides versuchen.

## Fallen (alle in der Simulation nachgewiesen)

1. **Mehrere Quellen an einem analogen Eingang werden UND-verknüpft**, nicht ODER. Zwei Taster an `Mult.Input1`:
   nur beide gleichzeitig → Ergebnis. Vor einen Analogeingang ein `Or` setzen. (Digitaleingänge: ODER wie üblich.)
2. **`LightController2` T5/1–8 (`Sel1`–`Sel8`) reagiert nur auf den T5-Code 4** (Mitteltaste Touch). Digital 1,
   2, 8, 16, 32 → keine Reaktion. Eine Logik-/Tasterquelle, die bei Gen 1 an `Sel n` „Szene n wählen“ auslöste,
   braucht einen Umsetzer `Mult ×4`. Eine Strukturprüfung (Verbindung vorhanden, Werte gleich) findet das nicht.
3. `Mood` (`Select`) ist pegelgesteuert: Wert 0 = „Aus“. Als Ersatz für einen Szenenimpuls ungeeignet.
4. `get_block` zeigt Parameter mit Eigenschaftsfeld teils als 0 — immer über `get_block_properties` nachlesen.

Lichtsteuerungs-Migration Gen 1 → `LightController2` im Detail: [migrationserkenntnisse.md](migrationserkenntnisse.md),
Abschnitt „Lichtsteuerung Gen 1 → LightController2“.
