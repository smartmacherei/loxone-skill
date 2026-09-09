# Projektabgleich: Demo Case, 09.09.2026

## Aussagekraft

`[PROJEKT-BELEGT]`: Read-only-Auswertung eines vom Nutzer bereitgestellten
Loxone-Demoprojekts. Vergleichsbasis ist Skill-Commit `6c86c64` vom 05.09.2026.
Der SHA-256 zur eindeutigen Zuordnung steht im
[strukturellen Inventar](demo-project-inventory.json). Die Originaldatei wird nicht mitgeliefert.

Das Projekt enthält **2.279 C-Objekte und 223 unterschiedliche Type-Werte**.
`Document/@NumO="2279"` stimmt mit der gezählten Objektzahl überein.
Unter den 11 Programmseiten kommen **50 unterschiedliche Bausteintypen** vor
(ohne `Text`, `InputRef`, `OutputRef` und `OutputRefLM`).
223 XML-Typen sind keine 223 Funktionsbausteine: Darunter sind auch Container,
Benutzerverwaltung, Systemwerte, Geräte und einzelne Ein-/Ausgänge.
Das Projekt bildet viele Bereiche ab, belegt aber nicht die Vollständigkeit
aller Loxone-Produkte, Funktionen oder Konfigurationsvarianten.

## Versionsunterschied

| Merkmal | Bisherige Vorlagen | Dieses Projekt |
|---|---|---|
| ConfigVersion | 17.1.7.27 | Rohwert `17020828` (17.2.8.28 nach bisherigem Versionsschema) |
| ControlList/@Version | 273 | 274 |
| Objektversion | überwiegend 175 | je Typ/Variante im Inventar nachsehen |

Die gespeicherte ConfigVersion ist kein Nachweis der laufenden Miniserver-Firmware.
Die alten Vorlagen bleiben als geprüfter Stand erhalten; Header und Objektversionen
nicht pauschal auf den neueren Wert umschreiben.

## Was der Skill hierdurch zusätzlich weiß

1. **31 der 50 Seiten-Bausteintypen fehlen in `bausteinvorlagen.xml`.**
   Für diese liegen jetzt beobachtete Konnektornamen, `Nio`, Objektversionen,
   Attributnamen und Kind-Elemente im Inventar vor. Das ist zusätzliche Strukturinformation;
   vielfach existiert die Funktionsbeschreibung bereits im deutschen Katalog.
2. **19 Typen überschneiden sich mit den bisherigen Vorlagen.** Bei diesen stimmen
   die Mengen der direkten `Co/@K` in allen beobachteten Projektvarianten mit den
   Vorlagen überein. Das bestätigt die Konnektornamen in diesem Projekt, aber nicht
   identische Parameterwerte, Semantik oder Versionskompatibilität.
3. **Gerätecontainer und Kanäle sind getrennte Objekte.** Das Projekt enthält
   58 `LoxAIRDevice`- und 37 `TreeDevice`-Einträge, dazu unter anderem
   `LoxAIRsensor`, `LoxAIRAsensor`, `LoxAIRactor`, `TreeSensor`, `TreeAsensor`
   und `TreeActor`. Gerätezahl und Kanalzahl getrennt auswerten.
   Auch Modbus-, DALI-, KNX-, EnOcean-, RS232-/RS485-, DMX- und weitere
   Schnittstellenstrukturen sind im Inventar enthalten.
4. **Der native MCP-Server ist als Plugin gespeichert**, nicht als eigener
   `C Type="McpServer"`. Details und ein reduziertes Strukturbeispiel stehen
   in [mcp-server.md](mcp-server.md#projektbeleg-vom-09092026).

### Auffällige interne Typnamen

Die Bezeichnungen rechts sind im Projekt beobachtete Objekttitel und damit
Orientierungshilfen, keine unabhängige Bestätigung offizieller Typ-Aliase.

| XML-Typ | Beobachtete Bezeichnung |
|---|---|
| `EFM` | Energieflussmonitor |
| `Heatmixer2` | Vorlauftemperatur Rechner |
| `HvacAC` | Klimaanlagen Zentralsteuerung |
| `AalEmergency` | Notfall Alarm |
| `AalSmartAlarm` | AAL Smart Alarm |
| `PowerUnit` | Power Supply & Backup |
| `TpfController` | Touch Pure Flex Controller |
| `TPDC` | Touch Pure Display Controller / CO2 Tree / CO2 Air |
| `MeterAbsBi` | Zähler Bidirektional |
| `MeterAbsUni` | Zähler |
| `NfcCodeTouch` | NFC Code Touch Tree / Air |

**Konnektornamen exakt übernehmen:** `StepSel` besitzt hier etwa
`InputTrigger 1` bis `InputTrigger 16` **mit Leerzeichen**. `Wallbox` verwendet
unter anderem `allow`, `ocppAuth`, `sessStop`, `outPower` und `OutputAPI`.
Ein Katalogname oder eine TechDoc-Familie ersetzt nicht den konkreten XML-Typ
und Konnektorsatz des Zielprojekts.

## Inventar richtig verwenden

Jeder Type-Eintrag enthält Anzahl, beobachtete Elterntypen, Attributnamen,
Kind-Elementnamen und Varianten mit `version`, `nio` und `connectorKeys`.
Eine Variante wird durch Version, Nio und die geordnete direkte Konnektorliste
unterschieden. Die Attribute/Kind-Elemente sind dagegen die Vereinigungsmenge
über alle Instanzen des Typs, keine Pflichtfelddefinition.

**Das Inventar ist keine importierbare Bausteinvorlage.** Es enthält weder UUIDs
noch Verbindungen, Parameterwerte, Programme oder vollständige Geräteeinstellungen.
Beim Erzeugen eines Bausteins weiter eine vollständige Vorlage aus dem Zielprojekt
oder Loxone Config verwenden; Referenzen und eingebettete Konfigurationen erhalten.
Projektwerte nicht als Werkseinstellungen dokumentieren. Ein `OutputAPI`-Konnektor
oder ein vorhandenes Gerät belegt auch keine Freigabe über MCP.

Reproduzieren (PowerShell, ohne Änderung des Projekts):

```powershell
./scripts/project_inventory.ps1 -ProjectPath '<Projekt.Loxone>' -OutputPath '<Inventar.json>'
```

Der Export verwendet eine Positivliste struktureller Felder. Projekttitel, Pfade,
Adressen, Seriennummern, UUIDs, Zugangsdaten, Pairing-Schlüssel, Programme und
Konnektorwerte werden nicht übernommen. Der Parser dient ausschließlich der Analyse;
wegen der bekannten Zeilenumbruch-Normalisierung niemals sein DOM zurückspeichern.

## Was das Projekt nicht beantwortet

- Live-Erreichbarkeit, OAuth-Anmeldung, tatsächlich angebotene MCP-Tools und Benutzerrechte.
- Konkrete, getestete Einrichtung des MCP-Clients in Codex oder ChatGPT.
- Allgemeine Werkseinstellungen und die Bedeutung bislang undokumentierter Attribute.
- Vollständigkeit des Produktkatalogs und Verhalten aller Bausteine zur Laufzeit.

Für diese Punkte sind weiterhin aktuelle Herstellerdokumentation bzw. gezielte
Tests nötig. Die Projektdatei wurde weder verändert noch in einen Miniserver geladen.

## Seiten-Bausteintypen ohne bisherige XML-Vorlage

Die folgende Tabelle verweist auf die beobachteten Strukturen im JSON-Inventar.

| XML-Typ | Instanzen im gesamten Projekt | Nio / direkte Konnektorzahl je Variante |
|---|---:|---|
| `AalEmergency` | 1 | 13 / 13 |
| `AalSmartAlarm` | 1 | 18 / 18 |
| `AcControl` | 2 | 25 / 25 |
| `AlarmClock` | 2 | 26 / 26 |
| `ClimateControllerUS` | 1 | 32 / 32 |
| `Code16` | 1 | 34 / 34 |
| `Door` | 2 | 28 / 28 |
| `EFM` | 1 | 19 / 19 |
| `Greater` | 1 | 3 / 3 |
| `Heatmixer2` | 1 | 23 / 23 |
| `HvacAC` | 1 | 11 / 11 |
| `Irrigation` | 1 | 26 / 26 |
| `Jalousiemotor` | 3 | 41 / 41 |
| `Leaf` | 2 | 30 / 30 |
| `LongClick` | 1 | 14 / 14 |
| `MailBox` | 1 | 13 / 13 |
| `Media` | 1 | 94 / 94 |
| `MeterAbsBi` | 6 | 26 / 26 |
| `MeterAbsUni` | 2 | 15 / 15 |
| `Monoflop` | 1 | 5 / 5 |
| `NfcCodeTouch` | 2 | 33 / 33 |
| `PButtonT` | 1 | 7 / 7 |
| `PoolController` | 1 | 50 / 50 |
| `PowerUnit` | 1 | 15 / 15 |
| `PulseGen` | 1 | 6 / 6 |
| `Sequencer` | 1 | 16 / 16 |
| `SteakThermo` | 1 | 17 / 17 |
| `StepSel` | 1 | 42 / 42 |
| `TPDC` | 3 | 16 / 16 |
| `TpfController` | 1 | 29 / 29 |
| `Wallbox` | 2 | 56 / 56 |
