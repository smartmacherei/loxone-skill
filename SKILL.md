---
name: loxone-config
description: Use when working with Loxone Config projects or .Loxone files - reading, analysing or script-editing project XML, wiring function blocks (Intelligente Raumregelung, Automatikbeschattung, Präsenz, Lichtsteuerung, WC Lüftungssteuerung, Zentralbausteine), retrofitting KNX/DALI installations, running or evaluating the Auto-Konfiguration, or answering what a Loxone block can do.
---

# Loxone Config

Verifiziertes Wissen über Loxone-Config-Projekte: Dateiformat, Bausteine, Konnektoren und die
Fallen, die man sonst durch Ausprobieren lernt. **Nicht raten — hier nachsehen.**

Stand: Loxone Config 17.1.7.27 · ControlList Version 273 · Objektversion `V="175"`

## Wann dieser Skill

- `.Loxone`-Dateien lesen, analysieren oder per Skript bearbeiten
- Funktionsbausteine verdrahten oder ihre Ein-/Ausgänge nachschlagen
- KNX-/DALI-Bestandsanlagen auf Loxone-Bausteine umbauen
- Auto-Konfiguration einsetzen oder ihr Ergebnis bewerten
- Fragen wie „was kann Baustein X laut Doku"
- MCP-Server einrichten oder einen KI-Assistenten an den Miniserver anbinden
- Das Programm direkt aus dem Miniserver lesen oder zurückschreiben

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
| [references/xml-bearbeitung.md](references/xml-bearbeitung.md) | Dateiformat, verlustfreies Schreiben, PowerShell-Rezept, Fallstricke |
| [references/bausteine.md](references/bausteine.md) | Vorlagen-Handhabung, die sieben verifizierten Konnektor-Zuordnungen |
| [references/xml-doku-mapping.md](references/xml-doku-mapping.md) | **Interner XML-Konnektorname ↔ Doku-Kürzel** für alle 29 Vorlagentypen, plus die drei Lücken-Listen |
| [references/autokonfiguration.md](references/autokonfiguration.md) | Was die Auto-Konfiguration je Raumtyp anlegt, alle Vorgabewerte |
| [references/zentralfunktionen.md](references/zentralfunktionen.md) | Die 20 Komfortfunktionen, Zentralbausteine, Klimasteuerung, Sturm-/Frostschutz |
| [references/programmier-bausteine.md](references/programmier-bausteine.md) | **Ablaufsteuerung + Programm (PicoC)** — wann welches Werkzeug, XML-Aufbau, Befehls- und PicoC-Funktionsreferenz, Zeilenumbruch-Falle |
| [references/mcp-server.md](references/mcp-server.md) | **MCP-Server auf dem Miniserver** (ab Config 17.1.6, nur Gen 2) — Einrichtung in der Netzwerkperipherie, OAuth statt Basic-Auth, Claude-Anbindung, Community-Bridges als Fallback |
| [references/miniserver-dateizugriff.md](references/miniserver-dateizugriff.md) | **Programm im Miniserver lesen und schreiben** — HTTP kann nur lesen, FTP schreibt; LoxCC-Format samt CRC32; was der WebSocket pusht und was nicht |
| [references/techdoc-lxres.md](references/techdoc-lxres.md) | **Offizielle Bausteindoku als XML aus dem Config-Paket** — 220 typisierte Bausteine mit XML-Konnektorname, Doku-Kürzel, Einheit, Bereich, Vorgabe; Decoder `scripts/decode_lxres.py`, Abgleich `scripts/techdoc_abgleich.py` → [techdoc-abgleich.md](references/techdoc-abgleich.md); kommt mit jedem Config-Update mit |

### Baustein-Katalog — alle 179 Bausteine der offiziellen KB

Je Baustein: Eingänge, Ausgänge, Parameter, Eigenschaften wörtlich, dazu dokumentierte
Fallstricke und Quell-URL. Quelle: `loxone.com/dede/kb-cat/config-functionblock/`, Stand 30.07.2026.

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

### Praxis

| Datei | Inhalt |
|---|---|
| [references/anwendungsbeispiele.md](references/anwendungsbeispiele.md) | 25 Anwendungsbeispiele + 11 Config Challenges, je mit Verdrahtungsidee |
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
