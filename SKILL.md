---
name: loxone-config
description: Use when working with Loxone Config projects or .Loxone files - reading, analysing or script-editing project XML, wiring function blocks (Intelligente Raumregelung, Automatikbeschattung, Präsenz, Lichtsteuerung, WC Lüftungssteuerung, Zentralbausteine), retrofitting KNX/DALI installations, running or evaluating the Auto-Konfiguration, integrating third-party devices (Loxone Library templates and .LxAddon files, Modbus/virtual output/IR/RS232 templates, Sonos and other audio, LoxBerry or Home Assistant bridges), or answering what a Loxone block can do.
---

# Loxone Config

Verifiziertes Wissen über Loxone-Config-Projekte: Dateiformat, Bausteine, Konnektoren und die
Fallen, die man sonst durch Ausprobieren lernt. **Nicht raten — hier nachsehen.**

Stand: Loxone Config 17.1.7.27 · ControlList Version 273 · Objektversion `V="175"`

Zusätzlicher Projektabgleich vom 09.09.2026: ConfigVersion `17020828`, ControlList 274.
[Projektbefunde und Strukturinventar](references/demo-project-audit.md) ergänzen den
älteren Vorlagenstand; keine pauschale Migration oder Live-Verifikation.

## Wann dieser Skill

- `.Loxone`-Dateien lesen, analysieren oder per Skript bearbeiten
- Funktionsbausteine verdrahten oder ihre Ein-/Ausgänge nachschlagen
- KNX-/DALI-Bestandsanlagen auf Loxone-Bausteine umbauen
- Auto-Konfiguration einsetzen oder ihr Ergebnis bewerten
- Fragen wie „was kann Baustein X laut Doku"
- MCP-Server einrichten oder einen KI-Assistenten an den Miniserver anbinden
- Das Programm direkt aus dem Miniserver lesen oder zurückschreiben
- Fremd-Audio (Sonos, Multiroom) an Loxone anbinden — Music Server, Audioserver,
  virtuelle Ausgänge, LoxBerry- oder Home-Assistant-Brücke
- Ein Fremdgerät (Wechselrichter, Zähler, Wallbox, Wärmepumpe, TV …) einbinden:
  **zuerst in der Loxone Library nachsehen**, statt Modbus-Register abzutippen

## Die elf Fallen

Jede davon hat schon einmal Schaden angerichtet oder Arbeit vernichtet.

**1. Niemals bearbeiten, solange Loxone Config die Datei offen hat.**
Config hält das Projekt im Speicher und schreibt beim Speichern den kompletten Stand zurück.
Skript-Änderungen dazwischen sind danach **spurlos weg** — ohne Warnung, ohne Konflikt-Dialog.
Ablauf: Config schließen → Skript → Config öffnen → prüfen → speichern.

**2. `InputRef.AQ` ist der Zustand, `InputRef.Q` der Fehlerausgang.**
```
AI  <=  Quelle.Q    (Zustand)   ->  AQ  = Zustand      <- diesen verwenden
I   <=  Quelle.Qe   (FEHLER)    ->  Q   = Fehler
```
Ausnahme: Referenzen auf einen `Memory` nutzen `.Q` (dort liegt nur ein Signal an).
Im Zweifel prüfen, welchen Konnektor bestehende, funktionierende Verbindungen im Projekt nutzen.

**3. Bausteintypen ohne Vorlage lassen sich nicht erzeugen.**
Typname, Konnektorsatz und `Nio` sind nicht ableitbar. Quellen für Vorlagen, in dieser Reihenfolge:
das Projekt selbst → `C:\ProgramData\Loxone\Loxone Config <Ver>\Templates\FactoryPresets.xml`
(enthält nur Raum-Bausteine) → sonst: **einmal in Config einfügen lassen**, dann als Muster nutzen.
**Konnektornamen** (nicht den Satz, nicht `Nio`) liefert seit 05.09.2026 die TechDoc aus dem
Config-Paket — [techdoc-lxres.md](references/techdoc-lxres.md).
Aus FactoryPresets entnommene Bausteine tragen eine ältere `V`-Nummer — **Config migriert sie beim
Öffnen selbst** (verifiziert: Nio 40 → 57 bei der Raumregelung).

**4. `Wap` (Windalarm-Position) steht standardmäßig auf 0 = ganz ÖFFNEN.**
Für Rollläden und Raffstores richtig (hochgefahren = windsicher). Für **Fenstermotoren tödlich** —
sie reißen im Sturm auf. Dort `Wap = 1`. Bei Markisen vor Ort verifizieren.
Der Eingang `Wa` fährt in die `Wap`-Position **und sperrt den Baustein selbst** — keine zusätzliche
Verriegelungslogik nötig.

**5. Config normalisiert beim Speichern.** Bei DALI wandert die Kategorie vom `DaliDevice`-Container
auf den `DaliActor`. Das sieht nach Datenverlust aus, ist aber korrekt. **Vor dem „Reparieren"
prüfen, wo der Wert wirklich hingehört.**

**6. PWM sitzt an zwei Orten.** Die Einstellung „PWM Ausgänge" in den Baustein-Eigenschaften wirkt
nur auf `H`/`C`/`HC`. Für die **Quellenausgänge** `H1-3`/`C1-3`/`HC1-3` muss PWM im Dialog
„Quellen konfigurieren" je Quelle aktiviert werden.

**7. Ein Apostroph in einer Notiz kann ein ganzes Objekt verschlucken.**
Bekannt war: `'` im `Text`-Attribut eines `<C Type="Text">` bricht den Text beim nächsten
Config-Öffnen ab und verschachtelt den Seitenbaum — dabei geht *nichts* verloren, alles ist nur
falsch einsortiert. **Verifiziert 03.08.2026: es gibt eine zweite, stillere Schadensform.** Dabei
verschwindet ein Objekt derselben Seite komplett, während der `Text`-Baustein dessen `Ref`/`RefL`
erbt. Ein `Text` mit einem `Ref`-Attribut ist der Verräter — das gibt es sonst nie. Im Projekt
Bestandsprojekt fiel so eine Ausgangsreferenz auf einen KNX-Aktor aus; ein Dachfenster-Rollo konnte
über zwei Versionen hinweg nicht zufahren, ohne dass es auffiel.
→ Keine Apostrophe in Notizen. **Nach jedem Config-Speichern die Objektzahl je Seite gegen den
Vorstand vergleichen** — Verschachtelung fällt sofort auf, ein gefressenes Objekt nicht.
Weitere Verräter: Notiztexte, die mitten im Satz enden; Konnektoren, deren Geschwister an
baugleichen Bausteinen alle verdrahtet sind.

**8. `Inv` sitzt am Konnektor, nicht an der einzelnen Verbindung.**
`<Co K="W" Inv="true" Nc="16">` invertiert **alle 16** Verbindungen dieses Eingangs. Sammeleingänge
— Fenster-/Türüberwachung `W`, Raumregler `Window`, Alarm-Zonen — vertragen deshalb nur Kontakte
**gleicher Polarität**. Weicht einer ab, hilft kein Umschalten des Sammeleingangs; der abweichende
Kontakt muss vorher invertiert werden, z. B. mit `Inv="true"` am `AI` seiner Eingangsreferenz
(dieses Muster ist in Bestandsprojekten an `OutputRef.AI` gut zu sehen).

**9. Doku-Kürzel ≠ XML-Konnektorname.**
Die KB nennt die Beschattungsparameter `Opd`, `Cld`, `Rd`, `Spm`, `Spe`, `Sw`, `Sd`; im XML heißen
sie `TimeEnd`, `TimeEndDown`, `SO`, `AutMode`, `AutoShadeEnd`, `Width`, `Space`. Wer per XPath nach
den Doku-Kürzeln sucht, findet **nichts** und schließt daraus fälschlich „steht überall auf
Default". Immer über [xml-doku-mapping.md](references/xml-doku-mapping.md) gehen.

**10. Ein `XmlDocument`-Roundtrip zerstört PicoC-Programme lautlos.**
Loxone Config schreibt mehrzeilige Attributwerte mit **rohen CRLF** (verifiziert am
`Code`-Attribut des Programm-Bausteins `<C Type="Code16">`; `&#xA;` kommt im ganzen File nie vor).
Der XML-Standard schreibt *Attribute-Value Normalization* vor — jeder Umbruch wird beim **Parsen**
zu einem Leerzeichen. Aus einem PicoC-Programm wird eine Zeile, und ab dem ersten `//` ist der
Rest auskommentiert. Objekt- und Verbindungszahl bleiben dabei gleich, **alle üblichen Prüfsummen
schlagen nicht an**.
→ Vor dem Parsen rohe Umbrüche in Attributwerten zu `&#xA;` maskieren (Rezept in
[xml-bearbeitung.md](references/xml-bearbeitung.md)) — oder Projekte mit PicoC-Code gar nicht
per `XmlDocument` patchen. Betrifft vermutlich auch `SequenceController/<SEQ>/@CFG`.

**11. `Document/@NumO` muss stimmen, sonst weist Config die Datei beim Öffnen ab.**
`NumO` ist **exakt die Anzahl der `<C>`-Elemente** im File. Stimmt sie nicht, kommt
**„Das aus dem Miniserver geladene Projekt hat einen fehlerhaften Inhalt!"** — auch beim
gewöhnlichen Datei-Öffnen. Die Meldung ist die generische Ablehnung beim Laden und hat mit dem
Miniserver nichts zu tun (Stringtabelle `LoxoneConfigres_DEU.dll`, neben „Projekt nicht
vorhanden"). **Kein Logfile, keine Detailmeldung** — man sucht sonst blind.
**[VERIFIZIERT 27.08.2026]** an erzeugten Demoprojekten: abgewiesen mit `NumO="2240"` bei 183
Objekten, und **allein das Korrigieren von `NumO` machte dieselbe Datei wieder öffenbar.**
In 13 von 14 gewachsenen Projektständen stimmt der Wert exakt; der einzige Ausreißer war selbst
skripterzeugt. Wer per Skript Objekte anlegt oder löscht, muss `NumO` neu setzen.

**Was dieselbe Prüfung ausdrücklich *nicht* beanstandet hat** — damit man nicht in die falsche
Richtung sucht. Das alles lag in der geöffneten Datei gleichzeitig vor:
leeres `<C>` ausgeschrieben als `<C …></C>` · fehlende `Category/@RGR`, `Place/@RGR`,
`SysVar/@source`, `Document/@APPKEY`, `@APPID`, `@CrashL`, `LoxLIVE/@Installation` ·
komplett fehlende Onboard-Ein-/Ausgänge · fehlende `EIBline` · fehlende Benutzergruppen ·
Dangling `SpStates`/`Icon`-UUIDs (die hat auch jedes echte Projekt).
Configs Schreibstil trotzdem nachzubilden ist sinnvoll (Config schreibt `></C>` **nie**, und die
genannten Attribute an *jeder* Instanz) — aber es ist Kosmetik, nicht die Ursache.

Referenzintegrität allein ist ebenfalls kein Nachweis: die abgewiesene Datei war wohlgeformt und
hatte null Verbindungen ins Nichts. Rezept zum Messen solcher Invarianten gegen den vorhandenen
Projektbestand in [xml-bearbeitung.md](references/xml-bearbeitung.md), Abschnitt
„Erzeugte Dateien prüfen".

**Nebenbefund zum Parser:** `<Key>…</Key>` (Air-Pairing-Key einer Extension) trägt **Elementtext**
statt Attributen. Ein Scanner, der nur Attribute kennt, bricht dort ab.

## Referenzen

### Grundlagen

| Datei | Inhalt |
|---|---|
| [references/demo-project-audit.md](references/demo-project-audit.md) | **Projektbeleg vom 09.09.2026:** 2.279 Objekte, 223 XML-Typen, 31 zusätzliche Seiten-Bausteintypen gegenüber den XML-Vorlagen; strukturelles JSON-Inventar, konkrete MCP-Plugin-Struktur, Versionsgrenzen |
| [references/xml-bearbeitung.md](references/xml-bearbeitung.md) | Dateiformat, verlustfreies Schreiben, PowerShell-Rezept, Fallstricke |
| [references/bausteine.md](references/bausteine.md) | Vorlagen-Handhabung, die sieben verifizierten Konnektor-Zuordnungen |
| [references/xml-doku-mapping.md](references/xml-doku-mapping.md) | **Interner XML-Konnektorname ↔ Doku-Kürzel** für alle 29 Vorlagentypen, plus die drei Lücken-Listen |
| [references/autokonfiguration.md](references/autokonfiguration.md) | Was die Auto-Konfiguration je Raumtyp anlegt, alle Vorgabewerte |
| [references/zentralfunktionen.md](references/zentralfunktionen.md) | Die 20 Komfortfunktionen, Zentralbausteine, Klimasteuerung, Sturm-/Frostschutz |
| [references/programmier-bausteine.md](references/programmier-bausteine.md) | **Ablaufsteuerung + Programm (PicoC)** — wann welches Werkzeug, XML-Aufbau, Befehls- und PicoC-Funktionsreferenz, Zeilenumbruch-Falle |
| [references/mcp-server.md](references/mcp-server.md) | **MCP-Server auf dem Miniserver** (ab Config 17.1.6, nur Gen 2) — Einrichtung in der Netzwerkperipherie, OAuth statt Basic-Auth, Claude-Anbindung, Community-Bridges als Fallback |
| [references/miniserver-dateizugriff.md](references/miniserver-dateizugriff.md) | **Programm im Miniserver lesen und schreiben** — HTTP kann nur lesen, FTP schreibt; LoxCC-Format samt CRC32; **Upload wie Config: `/prog/sps_new.zip` + `dev/sps/restart`** (verifiziert); was der WebSocket pusht und was nicht; **Klemmen per Logger-UDP in Echtzeit melden** (`OutputRefLM`, Skript `scripts/ha_udp_logger.py`) |
| [references/gateway-client.md](references/gateway-client.md) | **Gateway/Client (Konzentrator, „Master/Client")** — Archiv mit `sps.Loxone` + `spsN.LoxCC` je Miniserver, `Gateway`/`SLAVE`/`GatewayClient`-Objekte, `Program.Ref` → `LoxLIVE`; **fremde Eingänge werden im Teilprogramm zum Merker mit derselben UUID, fremde Ausgänge bleiben hängende Referenzen**; Gateway-Strukturdatei enthält alle Clients, `msInfo.gatewayType`; Folgen für Logger-/Upload-Skripte, Prüfrezept |
| [references/peripherie-objekte-xml.md](references/peripherie-objekte-xml.md) | **Modbus, RS232/485, HTTP-/UDP-Eingang, IR und MP-Bus im XML** — Attributsätze aus 701 Library-Vorlagen erhoben (176.850 Attributvorkommen). Modbus-Funktionscodes, das **`ModbusDataType`-Bitfeld** (an allen 6.854 Vorkommen restlos zerlegt), `Check`-Muster für JSON, was beim Vorlagenbau schiefgeht. Ergänzt `xml-bearbeitung.md`, das nur `VirtualOut` abdeckt |
| [references/techdoc-dokumente.md](references/techdoc-dokumente.md) | **Loxones eigene PDFs aus `TechDoc/TechDoc_Common.zip`** (121 MB, liegt in jeder Installation): die **API-Kommandos** (SET/MENU/VALUESELECT/ECHO …), **Ports und Domains** komplett, **wann Air-Geräte offline gehen** (24 h / 52 h / bis zu 24 h zurück), die **Audio-Gruppierungs-API** `audio/cfg/dgroup`, App-URL-Schemata, Kameraanforderungen für Intercoms, Belimo-Fehlercodes |
| [references/techdoc-lxres.md](references/techdoc-lxres.md) | **Offizielle Bausteindoku als XML aus dem Config-Paket** — 220 typisierte Bausteine mit XML-Konnektorname, Doku-Kürzel, Einheit, Bereich, Vorgabe; Decoder `scripts/decode_lxres.py`, Abgleich `scripts/techdoc_abgleich.py` → [techdoc-abgleich.md](references/techdoc-abgleich.md); kommt mit jedem Config-Update mit |

### Baustein-Katalog — alle 179 Bausteine der offiziellen KB + 20 aus der TechDoc

Je Baustein: Eingänge, Ausgänge, Parameter, Eigenschaften wörtlich, dazu dokumentierte
Fallstricke und Quell-URL. Quelle: `loxone.com/dede/kb-cat/config-functionblock/`, Stand 30.07.2026.
**Seit 05.09.2026 ergänzt aus der TechDoc** ([techdoc-lxres.md](references/techdoc-lxres.md)):
20 Bausteine ohne KB-Seite (Gen-1-Varianten, BETA-Bausteine, Vergleicher, Stufenauswahl …) als
eigene Abschnitte `### Name (\`LxType\`)` am Ende der passenden Datei, 34 vorhandene Seiten um
die Tabelle **„Weitere Konnektoren laut TechDoc"** (Standard-Kürzel wie `Off`, `Rem`, `Rw`, die
die KB-Seiten weglassen) und eine Tabelle der 26 Geräte-/Extension-Einträge ohne Konnektoren.
Erzeugt und aktualisiert mit `py -3 scripts/techdoc_katalog.py <sys_DEU.zip> --apply`, geprüft mit
`scripts/techdoc_abgleich.py` — nach jedem Config-Update beide laufen lassen.

| Datei | Bausteine | Schwerpunkt |
|---|---|---|
| [bausteine-logik-basis.md](references/bausteine-logik-basis.md) | 22 | Und/Oder/Nicht, Vergleicher, Merker, Impulsschalter, Status |
| [bausteine-analog-mathematik.md](references/bausteine-analog-mathematik.md) | 23 | Rechenbausteine, Formel, Skalierer, Schwellwert, PWM, Stepper |
| [bausteine-bedienung-taster.md](references/bausteine-bedienung-taster.md) | 16 | Taster, Schalter, Radiotasten, Touch Pure Flex, App/Tablet |
| [bausteine-zeit-impuls.md](references/bausteine-zeit-impuls.md) | 15 | Verzögerungen, Impulsgeber, Schaltuhr, Treppenlicht, Klicks |
| [bausteine-sicherheit-alarm.md](references/bausteine-sicherheit-alarm.md) | 13 | Alarmanlage, Meldezentrale, Präsenz, Berechtigung, Sprechanlage |
| [bausteine-klima-heizung.md](references/bausteine-klima-heizung.md) | 12 | IRR, Heiz-/Kühlsteuerung, Heizkurve, PI/PID, 2-/3-Punkt |
| [bausteine-energie.md](references/bausteine-energie.md) | 11 | Energiemanager, Lastmanager, Wallbox, PV-Vorhersage, Spotpreis |
| [bausteine-multimedia-kommunikation.md](references/bausteine-multimedia-kommunikation.md) | 11 | Audio, Music Server, Mail/Call/Text Generator, Benachrichtigung |
| [bausteine-beschattung-fenster.md](references/bausteine-beschattung-fenster.md) | 10 | Automatikbeschattung (3 Varianten), Fenster, Windmesser |
| [bausteine-zaehler.md](references/bausteine-zaehler.md) | 10 | Zähler, Impulszähler, Festwert-, Betriebszeitzähler |
| [bausteine-system-schnittstellen.md](references/bausteine-system-schnittstellen.md) | 10 | Ablaufsteuerung, Programm-Baustein, Ping, BACnet, Connectors |
| [bausteine-lueftung-klimaanlage.md](references/bausteine-lueftung-klimaanlage.md) | 9 | Raum-/WC-Lüftung, Fan Coil, Klimaanlage, Leaf/Internorm |
| [bausteine-tore-tueren-spezial.md](references/bausteine-tore-tueren-spezial.md) | 9 | Türsteuerung, Tor, Bewässerung, Pool, Sauna, Wecker |
| [bausteine-beleuchtung.md](references/bausteine-beleuchtung.md) | 8 | Lichtsteuerung, Dimmer, RGB-Lichtszene, Konstantlicht, Szene |
| [bausteine-geraete-erweiterungen.md](references/bausteine-geraete-erweiterungen.md) | 26 | **TechDoc:** Miniserver, Extensions (DI/AI/AO/Dimmer/KNX/EnOcean/1-Wire/RS232/RS485/DMX/M-Bus/Schüco), Audioserver, Datenbank, Wetterserver, Tracker, Notiz — nur Name, Beschreibung, KB-Link |

### Praxis

| Datei | Inhalt |
|---|---|
| [references/anwendungsbeispiele.md](references/anwendungsbeispiele.md) | 25 Anwendungsbeispiele + 11 Config Challenges, je mit Verdrahtungsidee |
| [references/library-loxone-com.md](references/library-loxone-com.md) | **Loxone Library — alle 735 Fremdgeräte-Integrationen**, vollständig gecrawlt. Das `.LxAddon`-Format samt `templateType`-Tabelle, die offene JSON-API zum Selbst-Abfragen, die 21 Add-ons aus `addons.json` (alle **nur Gen 2**), und warum nur 33 Einträge zertifiziert sind. Daten: [library-katalog.json](references/library-katalog.json), erneuern mit `scripts/library_crawl.py` |
| [references/sonos-integration.md](references/sonos-integration.md) | **Sonos an Loxone** — in Config ist nichts eingebaut (an 17.2.8.28 nachgewiesen), aber Loxone veröffentlicht eine Library-Vorlage: 19 SOAP-Befehle, **die meistgeladene Integration überhaupt**. Die vier Wege: Music-Server-Emulation (nativer Baustein), HTTP-Bridge, Home Assistant, UPnP/SOAP. Dazu `Media` als gerätefreie Alternative und die Sonos-Einstellung, die alles stilllegt |
| [references/tutorials.md](references/tutorials.md) | Video-Tutorials und Config-Allgemein-Artikel, nach Baustein sortiert |
| [references/community-praxiswissen.md](references/community-praxiswissen.md) | ⚠️ **LoxWiki / Loxforum** — Bugs, Workarounds, Grenzen. Nicht offiziell. |

### Wie die Referenzen zu lesen sind

Jede Aussage im Katalog ist gekennzeichnet. Die Kennzeichnung ist Teil der Information:

| Kürzel | Bedeutung |
|---|---|
| `[BELEGT]` | wörtlich aus der offiziellen Loxone-KB, Quell-URL steht dabei |
| `[BELEGT-TECHDOC]` | aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](references/techdoc-lxres.md)) — Loxones eigene Daten, gleichwertig zu `[BELEGT]` |
| `[ABGELEITET]` | geschlossen, **nirgends so nachzulesen** — vor sicherheitsrelevantem Einsatz prüfen |
| `[OFFEN]` | unbekannt, bewusst nicht geraten |
| `[PROJEKT-BELEGT]` | direkt in einer konkreten Projektdatei beobachtet; keine Aussage über Werkseinstellungen, Vollständigkeit oder Laufzeitverhalten |
| `[COMMUNITY]` | LoxWiki / Loxforum, nicht offiziell — Config-Version und Alter beachten |

`[BELEGT]` gibt es nur für die offizielle KB. Die gesamte Datei `community-praxiswissen.md`
ist `[COMMUNITY]`, auch wo eine Aussage plausibel klingt.

Maschinenlesbare Bausteindoku (alle Bausteine, offiziell): `C:\ProgramData\Loxone\Loxone Config <Ver>\SDcard\sys\sys_DEU.zip`
→ [techdoc-lxres.md](references/techdoc-lxres.md). Maschinenlesbare Bausteinvorlagen (falls vorhanden):
`X:\Dokumente\Kunden\_Wissen\Loxone\Bausteinvorlagen.xml`

## Schnellzugriff

| Frage | Antwort |
|---|---|
| Heizung ↔ Beschattung koppeln | `IRC.Qs` (Shd) → `AutoJalousie.AutoShade` (Sps) |
| Stellantrieb heizt **und** kühlt, Quelle konfiguriert | `AQhc1` (HC1), nicht `AQhc` |
| Konventioneller Melder an den Präsenzbaustein | `InputActivate` — `DeviceActivate` ist nur für Loxone-Geräte |
| Melder an die Lichtsteuerung | `Move` (Mo, mit eigenem Nachlauf) oder `Presence` (P, ohne) |
| Zentralbaustein-Mitglieder | Attribut `rec` (UUID-Liste), **nicht** verdrahtet |
| Betriebsart aus der Logik schalten | `<C Type="Mode">` hat `I` **und** `Q` — beide verdrahtbar |
| Schulferien/Feiertag wirken im Raum | Spalte in `<Timer Modes="…">` des Reglers **plus** `CalendarEntry`. **Spalte ohne `<Entry>` = ganztags `DefValue`**, nicht Wochentag |
| Virtueller Ausgang per Skript | `Address` · `CmdOn/Off`, `CmdOnPost/CmdOffPost`, `CmdOnHTTP/CmdOffHTTP` — [xml-bearbeitung.md](references/xml-bearbeitung.md) |
| IP-Kamera einbinden | benutzerdefinierte Intercom. **Zugangsdaten je nach Kamera in die URL, nicht in „Benutzername/Kennwort Kamera"** — [bausteine-tore-tueren-spezial.md](references/bausteine-tore-tueren-spezial.md) |
| Peripherie-Ausgang auf eine Seite gezogen | die neue Ausgangsreferenz **ersetzt** eine bestehende Verbindung am Eingang. Danach Konnektorenpaare gegenprüfen |
| Raumregler an die Heiz-/Kühlsteuerung | Attribut `Objects` am Raumregler |
| Raumtyp `PType` | 1 Schlafraum · 2 Aufenthaltsraum · 3 Durchgangsraum |
| Sonnenstandsautomatik läuft nicht | `Dir` = −1, GPS fehlt, oder „Sonnenschein" nicht aktiv |
| Kästchen `Dwc: Raumregelung …` im Diagramm | **Verbindungs-Stub**, kein Objekt. Config zeichnet weit entfernte Baustein-Verbindungen so — auch auf derselben Seite. Der Text nennt den **Ziel**konnektor. Ein Referenzobjekt (`InputRef`/`OutputRef`) gibt es nur für Peripherie. |
| Konnektor eines Bausteins gesucht | `py -3 scripts/decode_lxres.py <sys_DEU.zip> --block <LxType>` — [techdoc-lxres.md](references/techdoc-lxres.md); für die 29 verifizierten Vorlagen zusätzlich [xml-doku-mapping.md](references/xml-doku-mapping.md). Nicht raten |
| Doku-Kürzel → deutscher Klartext | der jeweilige `bausteine-*.md`-Katalog, Tabellen wörtlich |
| Gatterlogik, Ablaufsteuerung oder PicoC? | *Bedingungen* → Gatter · *Abläufe* → Ablaufsteuerung · *Fremdformate* → PicoC. [programmier-bausteine.md](references/programmier-bausteine.md) |
| PicoC: welcher Index ist Eingang I1? | `getinput(0)`. 0-basiert, Text- und Analogkanäle getrennt |
| Sequenztext / Programmcode im XML | `SequenceController` → `<SEQ CFG="…">` · `Code16` → Attribut `Code` |
| Klemme **ohne Visu** in Echtzeit nach außen (HA, MQTT-Bridge …) | Logger-Objekt `Address="/dev/udp/<ip>/<port>"` **plus** je Klemme ein `OutputRefLM` auf einer Seite, `AI` vom `Q`/`AQ` der Klemme. **`LoggerMailer` direkt an der Klemme tut nichts.** 12–20 ms Latenz, Broadcast erlaubt — `py -3 scripts/ha_udp_logger.py`, [miniserver-dateizugriff.md](references/miniserver-dateizugriff.md) 4a |
| Programm ohne Config in den Miniserver | FTP `STOR /prog/sps_new.zip`, dann `GET /jdev/sps/restart` — genau Configs Weg. Vorher `sps_*.zip` aus `/prog` ziehen, `NumO` und `Date`/`DateS` setzen — [miniserver-dateizugriff.md](references/miniserver-dateizugriff.md) 5 |
| Gateway/Client: welche Datei gehört zu welchem Miniserver? | `sps0.LoxCC` = Gateway, `spsN.LoxCC` = Client mit `SLAVE Type="N"` bzw. `GatewayClient ProgType="N"`; `Program Ref="<LoxLIVE-U>"`; `sps.Loxone` = Gesamtprojekt, das Config lädt — [gateway-client.md](references/gateway-client.md) |
| Fremder Ein-/Ausgang auf einer Seite eines anderen Miniservers | Eingang → im Teilprogramm ein `Memory` **mit derselben UUID** (`Tp` 0 digital / 1 analog); Ausgang → `OutputRef` mit `Ref` auf eine UUID, die im Teil nicht existiert. **Keine Markierung im XML**, Besitzer nur über den `LoxLIVE`-Vorfahren — [gateway-client.md](references/gateway-client.md) 4 |
| Logger-UDP oder Upload im Gateway/Client-Verbund | Logger ins Programm des **besitzenden** Miniservers, `sps.Loxone` mitändern, Absender = Client-IP, Heartbeat je Miniserver; FTP-Verteilung an Clients **unbelegt** — nur im Testaufbau — [gateway-client.md](references/gateway-client.md) 6 |
| Gibt es für Gerät X eine Loxone-Vorlage? | Erst in [library-katalog.json](references/library-katalog.json) nachsehen (735 Einträge), **nicht** raten und nicht von Hand Register abtippen. Download: `curl -L -o X.LxAddon https://api.library.loxone.com/downloader/config/<slug>` — [library-loxone-com.md](references/library-loxone-com.md) |
| Modbus-Register per Skript anlegen | `<ModbusCmd>`: `ModbusCmd` = **Funktionscode** (3/4 lesen, 6/16 schreiben, 1/2 Coils lesen, 5/15 schreiben), `ModbusDataType` = **Basistyp 0–8 plus Flags +32/+64/+128** — [peripherie-objekte-xml.md](references/peripherie-objekte-xml.md) |
| JSON aus einem HTTP-Eingang holen | `VirtualInHttp` mit `PollingTime` (Standard 10 s), je Wert ein `VirtualInHttpCmd` mit `Check="\i&quot;schlüssel&quot;:\i\v"`. **Im XML doppelt maskiert** — [peripherie-objekte-xml.md](references/peripherie-objekte-xml.md) 3 |
| Air-Gerät ist offline | Timeout **24 h** netzgespeist, **52 h** batteriebetrieben; Remote Air nie. Das Gerät verlängert seine Wiederholabstände **bis auf 24 h** — Miniserver-Neustart hilft nicht, das Gerät muss aufgeweckt werden — [techdoc-dokumente.md](references/techdoc-dokumente.md) 3 |
| Was kann der API-Konnektor? | `SET` · `SETT5` · `MENU` · `VALUESELECT` · `TIMESELECT` · `WAIT` · `GETINPUT` · `GETOUTPUT` · `ECHO`, Verkettung mit `=…&…`. **Kein Nesting.** Meist nur Touch Pure Flex — [techdoc-dokumente.md](references/techdoc-dokumente.md) 1 |
| Welche Ports muss die Firewall durchlassen? | Miniserver-Suche **UDP 7070–7071**, Gateway/Client **UDP 7070–7077 mit Broadcast**, Audioserver→Miniserver **TCP 7095**, Audio-Steuerung **TCP 7091**, PTP **UDP 319/320**. Remote Connect nutzt **zufällige Ports 20000–65000** — [techdoc-dokumente.md](references/techdoc-dokumente.md) 2 |
| Multiroom-Audio läuft auseinander | PTPv2 prüfen: UDP 319/320, Multicast 224.0.1.129. **IGMP-Snooping und Energiesparmodi der Switches stören** (Loxone wörtlich) — [techdoc-dokumente.md](references/techdoc-dokumente.md) 2 |
| Audiozonen aus der Logik gruppieren | `VirtualOut` auf `http://<audioserver>:7091/` (**Schrägstrich am Ende ist Pflicht**), dann `audio/cfg/dgroup/create/<Master>,<Player>,…` bzw. `/delete/<Master>`. Der Befehl beschreibt den **Sollzustand** — [techdoc-dokumente.md](references/techdoc-dokumente.md) 4 |
| Kamera als Intercom geht nicht | Nur **Basic/Digest-Auth**, nur `multipart/x-mixed-replace` oder `image/jpeg`, max. **5 MB** je Bild. **RTSP/H.264 ist ausgeschlossen** — [techdoc-dokumente.md](references/techdoc-dokumente.md) 6 |
| Vorlage gefunden — ist sie brauchbar? | `cert` (nur 33 von 735 sind zertifiziert), `dl` und `by` prüfen. **Nach dem Import immer die Adresse ändern** — jede Vorlage trägt die IP des Einreichers |
| Was integriert Loxone selbst nativ? | Die 21 Add-ons in `<Config>\addons.json` (Alexa, HomeKit, Matter, MQTT, McpServer, EEBUS, OCPP, Gardena, Fronius, BMW …) — **alle mit `needGen2: true`**. Sonos ist **nicht** dabei — [library-loxone-com.md](references/library-loxone-com.md) 5 |
| Sonos an Loxone | **In Config ist nichts eingebaut** — „Sonos" kommt in der ganzen Installation nur in `ForbiddenPasswords.txt` vor. Schnell: Loxones Library-Vorlage `sonos-speakers-28` importieren (19 SOAP-Befehle, kein Rückkanal). Vollwertig: Software emuliert einen Music Server auf Port 7091, Config legt ihn als „Loxone Music Server" an → native `MediaClient`-Zonen — [sonos-integration.md](references/sonos-integration.md) |
| Fremd-Audio/AV ohne Loxone-Audiogerät in die Visu | Baustein **Medien-Steuerung** (`Media`, ControlType 462) — der einzige Audio-Baustein, der **kein** Gerät voraussetzt. Ein/Aus, Lautstärke, Kanal, Betriebsart. Titel/Cover/Favoritenliste kann nur die Music Server Zone — [sonos-integration.md](references/sonos-integration.md) 8 |
| Werte per BACnet freigeben | **Nichts ist automatisch sichtbar.** Je Wert ein Objekt unter `BACnetDevice` → `ActorCaption` (`BACnetActor` = `binary-input`, Miniserver-Ausgang) bzw. `SensorCaption` (`BACnetSensor` = `binary-output`, schreibbar). `subscribeCOV` pusht in 2–3 ms. XML-Vorlage und Messwerte: [bausteine-system-schnittstellen.md](references/bausteine-system-schnittstellen.md) BACnet; Prüfen ohne YABE: `py -3 scripts/bacnet_probe.py <ip>` |

**XML-Typname ≠ GUI-Name.** Diese sechs führen zuverlässig in die Irre:
`PushButton` ist der **Schalter** (nicht der Taster) · `PulseAt` ist **Impuls um** (Zeitpunkt,
nicht „Impuls bei") · `DayTimer` ist die **Schaltuhr** · `SmokeAlarm` ist die
**Brand- und Wassermeldezentrale** · `WindowsMonitor` ist die **Fenster- und Türüberwachung**
(der Baustein „Fenster" hat gar keine Vorlage) · `AutoJalousie` ist die **Automatikbeschattung**
(die einfache „Jalousie" hat keine Vorlage) · **`Code16` ist der Baustein „Programm"** (PicoC),
`SequenceController` die **Ablaufsteuerung**. Ebenso trügerisch: `AutoJalousie.EnAutoShade`
trägt das Doku-Kürzel **`DisSp`** — der XML-Name sagt „enable", die Doku „disable".
Und `Code` ist **doppelt vergeben**: am `<C Type="Document">` ist es die **Postleitzahl**,
am `Code16` der Programmtext.

**Die Audio-Typen sind durchgehend irreführend benannt** (verifiziert an Config 17.2.8.28):
`MediaClient` ist die **Music Server Zone** · `MusicPlayer` der **Audio Player** ·
`Media` die **Medien-Steuerung** (ein generischer AV-Baustein, *kein* Audioserver-Baustein) ·
`CentralMusic` **Audio Zentral** · `MPGroup` die **Audio Player Gruppe fix**.
Auf der Geräteseite: `MultiMediaServer` ist das **Music-Server-Gerät** mit `MusicZone`-Kindern,
`AudioServer` der **Audioserver** mit `AudioOut`/`AudioGroup`, `MusicExt` die
**Stereo Extension**. In der Visu-/API-Ebene heißt `MediaClient` dann `AudioZone` und
`MusicPlayer` `AudioZoneV2` — die „V2" gehört zum **Audio Player**, nicht zur Zone.

## Grenzen der Auto-Konfiguration

**Sie erkennt KNX- und DALI-Peripherie nicht als Klima-/Beschattungsgeräte.** In Bestandsprojekten
sind die Spalten *Beschattung, Klima, Audio, Peripherie, Präsenz* für alle KNX-Räume ausgegraut —
verfügbar bleiben *Beleuchtung*, *Wecker* (nur Schlafräume) und *Raum verlassen* (nur mit Melder).

Dort ist sie **kein Generator, sondern eine Parametrier-Referenz**: die Werte, die sie setzen würde,
stehen in `FactoryPresets.xml` und sind auch dort gültig, wo sie nicht läuft.

Sie legt außerdem **neben** bestehende Seiten neue an — in Bestandsprojekten nur auf einer
Wegwerf-Kopie laufen lassen.

## Häufige Fehler

| Fehler | Folge |
|---|---|
| Bausteintyp geraten | Config öffnet die Datei nicht mehr oder verwirft den Baustein still |
| `Dir` geschätzt statt gemessen | Beschattung fährt zur falschen Tageszeit; ein sichtbares −1 ist ehrlicher |
| PowerShell: `$doc` und `$DOC` | PowerShell ist case-insensitiv — dieselbe Variable |
| PowerShell: `C 0x106` an eine Funktion **ohne** `[int]`-Parametertyp | der Hex-Literal kommt als Text an, `-f '{0:x5}'` schreibt `0x106` statt `00106` → **unbrauchbare UUIDs**. Parameter immer `[int]` deklarieren |
| `.ps1` mit Umlauten ohne BOM | PS 5.1 liest als ANSI, „Fühler" matcht nicht mehr |
| `Write-Output` in einer Funktion | verschmutzt den Rückgabewert; `Write-Host` verwenden |
