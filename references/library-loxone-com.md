# Loxone Library — Fremdgeräte-Integrationen

Was Loxone selbst an Integrationen bereitstellt, in welcher Form, und wie man an alles
maschinell herankommt. **Vollständig gecrawlt am 18.09.2026: 735 Einträge.**

Der Katalog liegt als Datei daneben: [library-katalog.json](library-katalog.json)
(735 Einträge, nach Downloads sortiert). Erneuern mit
`py -3 scripts/library_crawl.py` — das Skript ist im Skill.

---

## 1. Was die Library ist — und was nicht

`library.loxone.com` ist Loxones Sammelstelle für **Gerätevorlagen**: fertige
Konfigurationsobjekte, die man in Loxone Config importiert. Sie ersetzt das frühere
Vorgehen, Registerlisten von Hand abzutippen.

**Sie ist kein Treiber-Store.** Eine Vorlage ist eine XML-Datei mit vorausgefüllten
Modbus-Registern, virtuellen Ausgängen oder IR-Codes — mehr nicht. Nach dem Import steht
sie im Projekt wie handgetippt, und niemand pflegt sie nach.

| Kennzahl (18.09.2026) | Wert |
|---|---|
| Einträge gesamt | **735** |
| davon mit herunterladbarer Vorlage | **701** |
| davon von Loxone selbst | 139 |
| Ersteller gesamt | 269 |
| Marken | 391 |
| **Zertifiziert (WWLX)** | **33** — also 4,5 % |
| Downloads gesamt | 499.727 (Momentaufnahme, steigt laufend) |
| Befehle/Register in allen Vorlagen | 19.638 |

**Die 4,5 % sind die eigentliche Aussage.** Alles andere ist von Dritten eingestellt und
von Loxone nur freigeschaltet, nicht geprüft. Vor produktivem Einsatz gilt dasselbe wie
bei `community-praxiswissen.md`: Quelle und Alter ansehen.

### Verteilung nach Technologie

| Technologie | Einträge | Vorlagentyp im XML |
|---|---|---|
| **Modbus** | 448 | `<Modbus>` + `<ModbusCmd>` |
| **Network** (virtuelle E/A) | 191 | `<VirtualOut>`, `<VirtualInHttp>`, `<VirtualInUdp>` |
| RS232 | 26 | `<Comm>` + `<CommCmd>` |
| IR | 25 | `<RC>` + `<RCkey>` + `<IRdata>` |
| MP-Bus | 13 | `<template>` mit `<C Type="BelimoDevice">` |
| Air | 13 | *keine Vorlage* — nativ in Config |
| RS485 | 11 | `<Comm>` + `<CommCmd>` |
| Other | 7 | gemischt |
| Air & Tree | 1 | *keine Vorlage* |

Nach Kategorie dominieren **Climate (275)** und **Energy (241)**, danach Controls (127),
Sensor (101), Other (93), Multimedia (86), Inverter (78), Wallbox (61),
Battery storage (55), Wellness (34), Security (31), Shading (21), Access (20),
Weather (19), Lighting (13), Irrigation (4). Mehrfachzuordnung ist die Regel.

---

## 2. Das `.LxAddon`-Format

**[VERIFIZIERT 18.09.2026]** an allen 701 heruntergeladenen Vorlagen.

Eine `.LxAddon`-Datei ist ein **ZIP** mit genau zwei Dateien:

| Datei | Inhalt |
|---|---|
| `<name>.xml` | die eigentliche Vorlage |
| `desc.json` | Metadaten: `type`, `name`, `uuid`, `version`, `id`, `file`, `templateType` |

Die XML trägt als **zweites** Element ein `<Info>` mit zwei Attributen:

```xml
<VirtualOut Title="Sonos" Address="http://192.168.1.232:1400" CloseAfterSend="true" CmdSep="">
	<Info templateType="3" minVersion="12031214"/>
	<VirtualOutCmd Title="Play" .../>
</VirtualOut>
```

### `templateType` → Wurzelelement

Die Zuordnung ist eindeutig (Häufigkeit aus 701 Vorlagen):

| `templateType` | Wurzelelement | Anzahl | Technologie |
|---|---|---|---|
| `1` | `VirtualInUdp` | 5 | Network |
| `2` | `VirtualInHttp` | 79 | Network |
| `3` | `VirtualOut` | 97 | Network |
| `4` | `RC` | 25 | IR |
| `5` | `Comm` | 27 | **RS232** |
| `6` | `Comm` | 11 | **RS485** |
| `7` | `Modbus` | 444 | Modbus |
| `20` | `template` | 13 | MP-Bus |

`5` und `6` teilen sich dasselbe Wurzelelement `Comm` und unterscheiden sich **nur** im
`templateType`. Wer eine Vorlage per Skript erzeugt, muss den richtigen Wert setzen —
aus dem XML allein ist die Schnittstelle nicht ablesbar.

**Windows-Falle beim Speichern der Vorlagen:** Vier Slugs enthalten einen Doppelpunkt
(`pulse-eight-neo:4-1211`, `:6a-1212`, `:8a-1213`, `:x-1214`). Wer sie unverändert als
Dateinamen benutzt, schreibt unter NTFS in einen **Alternate Data Stream** — die vier
überschreiben sich gegenseitig und hinterlassen eine 0-Byte-Datei `pulse-eight`, ohne
Fehlermeldung. `library_crawl.py` ersetzt solche Zeichen (`safe_name`).

### `minVersion`

Gepackte Config-Version im selben Format wie `Document/@ConfigVersion`: je zwei Stellen
für Haupt-, Neben-, Build- und Patchnummer. `12031214` = Config **12.3.12.14**,
`16000610` = **16.0.6.10**. Die häufigsten Werte liegen bei Config 12 und 16 — viele
Vorlagen sind also mehrere Jahre alt.

### MP-Bus: die einzigen Vorlagen mit echten `<C>`-Objekten

Die 13 MP-Bus-Vorlagen (12× Belimo, 1× FIRVENA) enthalten als einzige richtige
`<C>`-Objekte: `<C Type="BelimoDevice">`, `<C Type="Online">` und Kanäle mit den
numerischen Typen `1`, `2` und `4`.

> **Das macht die Library trotzdem nicht zur Quelle für Baustein-Vorlagen.** Die
> numerischen Typen sind MP-Bus-Kanäle, keine Funktionsbausteine. Für Bausteintypen
> bleibt es bei Falle 3 in SKILL.md: Projekt → `FactoryPresets.xml` → einmal in Config
> einfügen.

### Vorlage in Config importieren

**[COMMUNITY]** Doppelklick auf die `.LxAddon`-Datei, oder in Config im Gerätebaum
über das Auswahlmenü **„Vorlage importieren…"**. Config legt das Gerät samt allen
Befehlen an. Gespeicherte Vorlagen landen als `.xml` im Templates-Ordner der jeweiligen
Kategorie. Aus Config heraus erreichbar über **„Loxone Library online durchsuchen…"**.
Quelle: [Loxone KB Vorlagen](https://www.loxone.com/dede/kb/templates/) ·
[LoxWiki](https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696312/Templates+in+Loxone+Config+einbinden)

**Nach dem Import unbedingt die Adresse anpassen.** Die Vorlagen tragen die IP des
Einreichers — die Sonos-Vorlage z. B. `http://192.168.1.232:1400`.

---

## 3. Die API — alles ohne Anmeldung lesbar

**[VERIFIZIERT 18.09.2026]** Basis `https://api.library.loxone.com`, alle Aufrufe
**POST** mit `multipart/form-data`, Header `Origin: https://library.loxone.com`.
Lesende Endpunkte brauchen **keine Anmeldung**.

| Endpunkt | Felder | Liefert |
|---|---|---|
| `/loadFilteredPlugins` | `filter` (JSON), `orderby`, `order`, `limit` (`"0,2000"`) | die Liste. `filter={}` + großes `limit` = **alles** |
| `/loadPluginDetail` | `plugin`, `plugin_id` (**numerisch**), `lang` | Volltext, `downloads`, `products`, `devices` |
| `/loadPluginVersions` | `plugin`, `plugin_id` | Versionshistorie mit Changelog und Datum |
| `/loadCategories` | – | die 16 Kategorien |
| `/loadBrands` | – | alle Marken |
| `/loadFilters` | – | Technologien/Kategorien **mit Trefferzahl** |
| `/downloader/config/<slug>` | **GET** | die `.LxAddon`-Datei |

**Zwei Stolpersteine:**

- `plugin_id` ist die **Zahl** aus dem Listen-Schlüssel (`plugin-28` → `28`), nicht der
  Slug. Mit dem Slug antwortet die API mit einer rohen MySQL-Fehlermeldung.
- `/loadFilteredPlugins` liefert **keine** Kategorien (das Feld ist immer `[]`). Die
  Zuordnung bekommt man nur über `loadPluginDetail` je Eintrag — oder in 16 Aufrufen
  über `filter={"categories":["<id>"]}`.

Der Detail-URL im Browser ist `library.loxone.com/detail/<slug>/overview`, wobei der
Slug auf die numerische Id endet: `sonos-speakers-28`.

---

## 4. Die 34 Einträge ohne Vorlage

Sie sind kein Fehler, sondern zeigen an: **hier gibt es nichts zu importieren.** Bei 32
von 34 liegt das daran, dass die Anbindung anderswo passiert — als Loxone-Add-on, als
Air-Gerät oder als Extension. (Zwei Modbus-Einträge von Dritten sind schlicht
unvollständig eingestellt.)

| Gruppe | Einträge |
|---|---|
| **Air-Geräte** | AC Control Air für Daikin P1P2/S21, Gree, LG, Mitsubishi Electric, Mitsubishi Heavy, Panasonic, Sinclair, Toshiba · AQUASTAR Air Pool · Geiger Shading Motors · Molto Luce Volare Air · Paulmann Plug & Shine · Leaf 1 (Air & Tree) |
| **Extensions** | Fröling · Internorm · Schüco · Honeywell MB Secure/PRO |
| **Add-on / Dienst** | Apple HomeKit · Home Connect · Husqvarna · Miele@home · Hunter Douglas PowerView Gen. 3 · Fronius · EEBUS · Tesla Powerwall · sonnenBatterie 10 · KEBA KeContact · BMW i Wallbox Pro · Vaillant · iRoom iDock · Smart filter pump E.Pro |

### Gegenprobe in der lokalen Config

Die Behauptung „ist nativ" hält nur teilweise. **[VERIFIZIERT 18.09.2026]** gegen
Config 17.2.8.28: `Internorm` und `Schüco` stehen in TechDoc **und** `Treesort.xml`
(sie sind Extensions), `KEBA`, `Hunter Douglas` und `Fronius` nur in der TechDoc.
**`HomeKit`, `Miele`, `Powerwall`, `EEBUS`, `Vaillant`, `Husqvarna`, `Home Connect`
kommen in der TechDoc gar nicht vor** — sie sind Add-ons bzw. laufen über die
Loxone-App/Cloud, nicht über einen Config-Bausteintyp.

---

## 5. Die Add-ons in Config selbst

**[VERIFIZIERT 18.09.2026]** aus `C:\ProgramData\Loxone\Loxone Config 17.2.8.28\addons.json`
(Stand `20260826`, signiert). Das ist die **lokale, autoritative Liste** der Integrationen,
die Config als Add-on anbieten kann — 21 Stück, **alle mit `needGen2: true`**:

| Titel | `id` | Beschreibung laut Datei |
|---|---|---|
| Amazon Alexa | `Alexa` | Amazon Alexa Integration |
| Apple HomeKit | `HomeKit` | Apple HomeKit Integration |
| BMW | `BMW` | BMW vehicle integration |
| EEBUS Gerät | `EEBUS` | Anbindung von EEBUS Geräten |
| EXO | `Exo` | Loxone Exosphere Integration |
| FIAS PMS Integration | `FIAS` | FIAS PMS Integration |
| Fronius | `Fronius` | Fronius integration |
| Gardena | `Gardena` | Gardena Smart System |
| Home Connect | `HomeConnect` | Integration von Home Connect Geräten |
| Honeywell | `Honeywell` | Honeywell |
| Hunter Douglas PowerView Hub | `HunterDouglas` | Hunter Douglas PowerView Hub Anbindung |
| Husqvarna | `Husqvarna` | Husqvarna Mower |
| **Matter** | `Matter` | Matter Integration |
| **McpServer** | `McpServer` | Loxone MCP server plugin |
| **Mqtt** | `Mqtt` | MQTT client integration |
| OCPP | `ocpp` | Open Charge Point Integration for Loxone Wallboxes |
| SegwayNavimow | `SegwayNavimow` | SegwayNavimow integration |

Dazu **vier Einträge ohne Titel und Beschreibung**: `Ikarus`, `Vesta`, `Minotaurus`,
`Hephaistos`. Codenamen, in der Datei ausgeliefert, in der Oberfläche nicht benannt —
vermutlich noch nicht freigeschaltet. **[ABGELEITET]**

**Was daraus folgt:** MQTT, Matter und der MCP-Server sind keine Bausteine, sondern
Add-ons — und damit **Gen 2 vorausgesetzt**. Das deckt sich mit
[mcp-server.md](mcp-server.md). **Sonos steht nicht in dieser Liste** und auch in keiner
anderen Datei der Installation außer `ForbiddenPasswords.txt`
(→ [sonos-integration.md](sonos-integration.md)).

---

## 6. Die meistgenutzten Integrationen

Downloads als grober Reifegrad-Hinweis — mehr Nutzer heißt, dass Fehler eher aufgefallen sind.

| Downloads | Integration | Marke | Technologie |
|---:|---|---|---|
| 19.168 | **Sonos** | Sonos | Network |
| 13.412 | HUAWEI SUN2000 Inverter & LUNA2000 battery | Huawei | Modbus |
| 12.762 | Eastron SDM630 Series | Eastron | Modbus |
| 9.785 | LOXONE Modbus Electricity Meter (3 Phase) | LOXONE | Modbus |
| 8.979 | SolarEdge Inverter | SolarEdge | Modbus |
| 8.122 | Fronius GEN24 | Fronius | Modbus |
| 6.358 | Fronius – Modbus TCP | Fronius | Modbus |
| 5.763 | Samsung TV | Samsung | Network |
| 5.647 | Huawei Sun + Luna2000 + DTSU666-H | Huawei | Modbus |
| 5.281 | Fronius smart meter 63A | Fronius | Network |
| 5.237 | GoodWe inverter ET series | Goodwe | Modbus |
| 5.041 | SMA Sunny Tripower | SMA | Modbus |
| 4.909 | Shelly Pro 3EM | Shelly | Modbus |
| 4.909 | Solax X3 Hybrid G2 | Solax | Modbus |
| 4.248 | **Nuki Smart Lock** (zertifiziert) | NUKI | Network |
| 3.971 | iDM Heating & Cooling | iDM | Modbus |
| 3.567 | Kostal Modbus-TCP and Battery | Kostal | Modbus |
| 3.548 | **Tedee Smart Lock** (zertifiziert) | tedee | Network |
| 3.015 | Spot Price aWATTar (Price absolute) | LOXONE | Network |
| 2.835 | Sony Bravia TV Simple IP Control | Sony | Network |

**Sonos ist die meistheruntergeladene Integration der gesamten Library** — mit deutlichem
Abstand, und das bei einer Vorlage, die zuletzt 2021 angefasst wurde. Der Rest der
Spitzengruppe ist fast vollständig PV und Zähler.

### Die 8 zertifizierten mit Downloads

Von den 33 zertifizierten Einträgen haben nur acht überhaupt Downloads — die übrigen 25
sind die Add-on-/Air-/Extension-Einträge aus Abschnitt 4, die nichts zum Herunterladen haben.

| Downloads | Integration | Technologie |
|---:|---|---|
| 4.248 | Nuki Smart Lock Integration | Network |
| 3.548 | Tedee Smart Lock Integration | Network |
| 793 | Wattsonic – Schmachtl Sun Energy Box | Modbus |
| 737 | Heidelberg Wallbox Energy Control | Modbus |
| 588 | connecdoor.controller | RS485 |
| 235 | cunnect.keyless | Network |
| 180 | Alnor HRU | Modbus |
| 104 | Alnor HRU-P | Modbus |

---

## 7. Wie man den Katalog benutzt

[library-katalog.json](library-katalog.json) — ein JSON-Array, nach Downloads absteigend.
Felder je Eintrag:

| Feld | Bedeutung |
|---|---|
| `n` | Name |
| `slug` | Id für URL und Download (`.../downloader/config/<slug>`) |
| `brand` · `by` | Marke · Ersteller |
| `tech` | Network · Modbus · RS232 · RS485 · IR · MP-Bus · Air · Other |
| `cat` | Kategorien (Liste) |
| `dl` | Downloads |
| `cert` | zertifiziert (WWLX) |
| `short` | Kurzbeschreibung |
| `tt` · `root` · `ncmd` | `templateType` · XML-Wurzelelement · Anzahl Befehle/Register — **fehlen, wenn es keine Vorlage gibt** |

Typische Fragen:

```bash
# Gibt es für Gerät X etwas?
py -3 -c "import json;[print(e['dl'],e['n'],e['slug']) for e in json.load(open('references/library-katalog.json',encoding='utf-8')) if 'daikin' in (e['n'] or '').lower()]"

# Vorlage holen
curl -L -o X.LxAddon https://api.library.loxone.com/downloader/config/<slug>
```

**Vor dem Empfehlen einer Vorlage immer prüfen:** `cert`, `dl` und `by`. Ein Eintrag mit
`cert=false`, `dl` unter 50 und einem Privatnamen als `by` ist ein Vorschlag, kein Produkt.

---

## Quellen

Lokal verifiziert: `C:\ProgramData\Loxone\Loxone Config 17.2.8.28\addons.json`,
`SDcard/sys/sys_DEU.zip`, `SDcard/sys/Treesort.xml`.

Gecrawlt am 18.09.2026 über `api.library.loxone.com` (735 Einträge, 701 Vorlagen
heruntergeladen und ausgewertet) — `scripts/library_crawl.py`.

[Loxone KB: Vorlagen](https://www.loxone.com/dede/kb/templates/) ·
[LoxWiki: Templates in Loxone Config einbinden](https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696312/Templates+in+Loxone+Config+einbinden) ·
[library.loxone.com](https://library.loxone.com/)
