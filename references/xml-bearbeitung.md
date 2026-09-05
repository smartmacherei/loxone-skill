# Loxone Config — XML-Referenz für direkte Projektbearbeitung

**Zweck:** `.Loxone`-Projektdateien direkt per Skript bearbeiten, wenn die GUI zu langsam ist oder
die Auto-Konfiguration nicht greift (z. B. bei KNX/DALI-Bestand).

**Erarbeitet:** 30.07.2026 · Loxone Config 17.1.7.27 · Bestandsprojekt (KNX + DALI + Extensions)
Alles hier ist **verifiziert** — entweder aus Loxone's eigenen Dateien oder durch einen Testlauf,
bei dem Loxone Config die erzeugte Datei geladen, migriert und zurückgeschrieben hat.

---

## 1. Dateiformat

`.Loxone` ist **reines XML**, kein Container:

| Eigenschaft | Wert |
|---|---|
| Encoding | UTF-8 **mit BOM** (`EF BB BF`) |
| Zeilenende | **CRLF** |
| Einrückung | **Tabs** |
| Selbstschließende Tags | `<X/>` — **ohne** Leerzeichen vor dem Slash |
| Wurzel | `<ControlList Version="273" LxAV="86" NextObj="…" …>` |

### PowerShell-Rezept zum verlustfreien Zurückschreiben
`XmlWriter` schreibt `<X />` statt `<X/>`. Nur am Zeilenende normalisieren — sonst identisch:

```powershell
$set = New-Object System.Xml.XmlWriterSettings
$set.Indent = $true; $set.IndentChars = "`t"; $set.NewLineChars = "`r`n"
$set.Encoding = New-Object System.Text.UTF8Encoding($true)
$ms = New-Object System.IO.MemoryStream
$w = [System.Xml.XmlWriter]::Create($ms, $set); $doc.Save($w); $w.Close()
$txt = [System.Text.Encoding]::UTF8.GetString($ms.ToArray())
if ($txt.Length -gt 0 -and [int]$txt[0] -eq 0xFEFF) { $txt = $txt.Substring(1) }
$txt = [regex]::Replace($txt, ' />(\r?\n)', '/>$1')
[System.IO.File]::WriteAllText($path, $txt, (New-Object System.Text.UTF8Encoding($true)))
```

### 🛑 Korrektur (verifiziert 05.08.2026): rohe Zeilenumbrüche in Attributen

> Die frühere Fassung dieses Abschnitts behauptete, .NET schreibe Zeilenumbrüche in Attributen
> „korrekt als `&#xA;`". **Das ist falsch** — der Schaden entsteht schon beim *Einlesen*.

Loxone Config schreibt mehrzeilige Attributwerte mit **rohen CRLF** — verifiziert am
`Code`-Attribut des Programm-Bausteins (`<C Type="Code16">`). Im gesamten Projektfile kommt
`&#xA;` **kein einziges Mal** vor.

Der XML-Standard verlangt für Attributwerte *Attribute-Value Normalization*: jeder Zeilenumbruch
wird beim Parsen durch ein **Leerzeichen** ersetzt. `XmlDocument` hält sich daran. Ein Round-Trip
mit dem Rezept oben macht deshalb aus

```
int n;⏎while(TRUE) {⏎  n = getinputevent();⏎  sleep(100);⏎}
```

eine einzige Zeile — **ohne Fehler, ohne Warnung**, bei unveränderter Objekt- und
Verbindungszahl. Enthält der Text `//`-Kommentare, ist danach der Rest auskommentiert.

**Gegenmittel — vor dem Parsen maskieren:**

```powershell
function Protect-AttrNewlines([string]$text) {
    # Attributwerte sind durch " begrenzt; ein rohes " kann darin nicht vorkommen (waere &quot;)
    # TABs werden BEWUSST NICHT maskiert - siehe Warnung unten.
    $sb = New-Object System.Text.StringBuilder
    $inAttr = $false
    for ($i = 0; $i -lt $text.Length; $i++) {
        $ch = $text[$i]
        if ($ch -eq '"')               { $inAttr = -not $inAttr; [void]$sb.Append($ch); continue }
        if ($inAttr -and $ch -eq "`r") { continue }
        if ($inAttr -and $ch -eq "`n") { [void]$sb.Append('&#xA;'); continue }
        [void]$sb.Append($ch)
    }
    return $sb.ToString()
}

$safe = Protect-AttrNewlines ([System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8))
[xml]$doc = New-Object System.Xml.XmlDocument
$doc.LoadXml($safe)
```

### 🛑 Numerische Zeichenreferenzen zerstören semikolongetrennte Attribute

**[VERIFIZIERT 05.08.2026]** — an `SEQ/@CFG` der Ablaufsteuerung, echter Schaden im Projekt.

Mehrere Loxone-Attribute sind **Listen mit `;` als Trenner**: `SEQ/@CFG` (Sequenzzeilen),
`VNAME`, `CNAME`, `uuidSeqencing`. Loxones Parser löst darin die **benannten** Entities
`&gt;` `&lt;` `&amp;` korrekt auf — **numerische Zeichenreferenzen wie `&#x9;` aber nicht.**
Das `;` darin bleibt stehen und wirkt als Trenner.

Folge: aus jeder eingerückten Sequenzzeile werden zwei — eine Fehlerzeile `&#x9` und der Rest.
Der Editor markiert sie rot („Zeilen müssen mit einem gültigen Befehl beginnen").

Deshalb schreibt **Config Tabulatoren im Attribut roh** (Byte `0x09`) und escaped sie nicht.
`System.Xml.XmlWriter` macht das Gegenteil: es schreibt jeden TAB als `&#x9;`. Nachgemessen:

```powershell
$d.SelectSingleNode("//C").SetAttribute("A", "zeile1`tzeile2")
# -> im File steht:  A="zeile1&#x9;zeile2"
```

**Regeln:**
1. In `Protect-AttrNewlines` **keine** TABs maskieren. Ein roher TAB wird vom Parser zu einem
   Leerzeichen normalisiert — kosmetisch, aber ungefährlich.
2. Beim **Schreiben** von `CFG`/`VNAME`/`CNAME` **niemals TAB oder Zeilenumbruch** in den Wert
   legen. Einrückung ausschließlich mit **Leerzeichen** — die escaped XmlWriter nicht.
3. `<` und `>` sind unkritisch: XmlWriter schreibt `&lt;`/`&gt;`, Config löst beide auf.
4. Nach jedem Schreiben gegenprüfen: Feldzahl `($cfg -split ';').Count` vor und nach dem
   Roundtrip vergleichen.

Testergebnis: ohne Schutz 4 von 4 Umbrüchen verloren, mit Schutz alle 4 erhalten und der String
**identisch** zum Original. Beim Speichern schreibt .NET sie dann als `&#xA;`.

**Schnelltest, ob ein Projekt betroffen ist** — zählt rohe Umbrüche innerhalb von Attributwerten:

```powershell
$raw = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$inAttr = $false; $n = 0
foreach ($c in $raw.ToCharArray()) {
    if ($c -eq '"') { $inAttr = -not $inAttr; continue }
    if ($inAttr -and $c -eq "`n") { $n++ }
}
"rohe Zeilenumbrueche in Attributwerten: $n"
```

Bekannt betroffen: `Code16/@Code` (PicoC-Programm) und mit hoher Wahrscheinlichkeit
`SequenceController/<SEQ>/@CFG` (Sequenztext — noch **nicht** verifiziert). Notiztexte
(`Text/@Text`) enthielten in den geprüften Projekten keine rohen Umbrüche.

**Noch offen:** ob Loxone Config `&#xA;` im `Code`-Attribut beim Einlesen wieder als Umbruch
darstellt. Bis das geprüft ist: Projekte mit PicoC-Code **nicht** per `XmlDocument` patchen —
gezielte Textersetzung nehmen, oder den Code vor dem Patch herauskopieren und danach in Config
wieder einfügen.

**Verwandter Altschaden:** Steht im XML-Rohtext die Folge `&amp;#xA;`, enthält der Wert die
fünf sichtbaren Zeichen `&#xA;` statt eines Umbruchs — die Narbe eines Skripts, das auf dem
*Wert* statt auf dem *serialisierten XML* ersetzt hat. In der App steht dann wörtlich `&#xA;`
mitten im Text.

Details zu beiden Programmier-Bausteinen: [programmier-bausteine.md](programmier-bausteine.md).

> **PowerShell 5.1:** Skriptdateien mit Umlauten **müssen** mit BOM gespeichert werden, sonst
> werden `ä/ö/ü` als ANSI fehlinterpretiert und Kategorie-Namen wie „Fühler" matchen nicht.

### 🛑 UUID-Präfix vor jedem Build gegen das Projekt prüfen

Skriptgenerierte Objekte bekommen üblicherweise ein eigenes Präfix (`21b00033-0001-0033-…`).
**Frühere Builds haben ihre Präfixe aber schon verbraucht.** Ein wiederverwendetes Präfix erzeugt
doppelte UUIDs — Config verwirft dann still eines der beiden Objekte.

```powershell
# alle belegten Präfixe auflisten
[regex]::Matches($raw,'U="([0-9a-f]{4})') | % { $_.Groups[1].Value } | Sort-Object -Unique
# gewähltes Präfix gegenprüfen (muss 0 sein)
([regex]::Matches($raw,'23b0')).Count
```

Nach dem Build gegenprüfen: `//C[@U]` + `//Co[@U]` einsammeln und auf Dubletten testen, dazu
`IName` der virtuellen Ein-/Ausgänge (`VQ*`, `VI*`) — auch die müssen eindeutig sein.
Verifiziert 07.08.2026: Präfix `22d0` war bereits vergeben, Kollision fiel erst im Nachtest auf.

### 🛑 Niemals bearbeiten, solange Loxone Config die Datei offen hat
Loxone Config hält das Projekt **im Speicher** und schreibt beim Speichern den kompletten Stand
zurück. Änderungen, die zwischenzeitlich per Skript auf die Datei geschrieben wurden, sind dann
**spurlos weg** — ohne Warnung, ohne Konflikt-Dialog.

**Verifiziert am 30.07.2026:** Zwei Korrekturen (Konnektor-Umhängung und Kategorie-Wechsel) wurden
um 14:00 per Skript geschrieben; um 14:26 speicherte der Anwender aus Config — beide Änderungen
waren danach auf dem alten Stand.

**Arbeitsablauf:** Config schließen → Skript laufen lassen → Config öffnen → prüfen → speichern.
Nie parallel.

---

## 2. Grundstruktur

```xml
<C Type="…" V="175" U="<uuid>" Title="…" Px="…" Py="…" Px2="…" Py2="…" Nio="<Konnektorzahl>">
  <Co K="<Konnektorname>" Def="<Standardwert>" Nc="1" U="<uuid>">
    <In Input="<uuid des Quell-Konnektors>"/>
  </Co>
  <IoData Visu="true" Cr="<Kategorie-UUID>" Pr="<Raum-UUID>" Ugr="…" Ugx="…"/>
</C>
```

* **`Nio`** = Anzahl der `Co`-Elemente. Muss stimmen.
* **`U`-Schema:** Objekt-UUIDs enden auf das **Dokument-Suffix** (z. B. `ffff949738c6754e`),
  Konnektor-UUIDs auf ein **objekt-eigenes Suffix**. Muss projektweit eindeutig sein.
  **Loxone-UUIDs haben 35 Zeichen (8-4-4-16), nicht 36** — `{36}`-Regexe und UUID-Bibliotheken
  finden nichts. Das erste Feld ist die Anlegezeit in Sekunden seit 2009-01-01 00:00 UTC (derselbe
  Zähler wie `Document/@DateS`), die beiden mittleren sind Laufnummern. Für skripterzeugte Objekte
  reicht: aktuelle Loxone-Sekunde als erstes Feld, Zähler, Dokument-Suffix — und gegen alle
  vorhandenen `U="…"` prüfen (verifiziert 05.09.2026, `scripts/ha_udp_logger.py`).
* **Verbindungen** laufen ausschließlich über `<In Input="…"/>` mit der **Konnektor**-UUID der Quelle.
* **`IoData`** fehlt bei reinen Logikbausteinen (z. B. `2Point`) — die haben dann weder Raum noch Kategorie.
* Verbindungen gelten **innerhalb einer Programmseite**. Seitenübergreifend braucht es
  `InputRef` / `OutputRef`-Objekte.

### Attribute an `IoData` und `Display` — was die App daraus macht

*Verifiziert 03.08.2026 am Bestandsprojekt, gegen die laufende Anlage abgeglichen.*

| Ort | Attribut | Wirkung |
|---|---|---|
| `IoData` | **`UseInFav="true"`** | **Favoriten-Häkchen.** Das Objekt erscheint zusätzlich in der Favoritenliste der App. Kein Einfluss auf Funktion oder Verdrahtung — zum Entfernen genügt das Attribut. |
| `IoData` | `Visu="true"` | in der Visualisierung sichtbar |
| `IoData` | `Cr` / `Pr` | Kategorie- bzw. Raum-UUID |
| `IoData` | `Rating` | Sortier-/Gewichtungswert der Visu (beobachtet: `1` an Zentralbausteinen, `4` an Präsenzbausteinen) |
| `Display` | **`IxText`** | Textsatz der Zustandsanzeige. **Fehlt das Attribut, zeigt die App „Ein/Aus"** statt „Offen/Geschlossen" — das ist die häufigste Ursache für optisch zusammengewürfelte Listen. Beobachtet: `2` und `3` = Offen/Geschlossen. |
| `Display` | `IxColor="1"` | färbt den aktiven Zustand rot (Alarmfarbe) |
| `Display` | `StateOnly="true"` | nur Anzeige, nicht bedienbar |

**Namensanzeige in Sammelbausteinen:** Die Fenster- und Türüberwachung zeigt je Sensor
**`Desc` (Beschreibung), nicht `Title`**. Steht dort wie üblich nur „Fensterkontakt" / „Türkontakt",
sind alle konventionellen Kontakte in der App **nicht unterscheidbar** — der Raum in der zweiten
Zeile ist die einzige Unterscheidung. Loxone-Air-Geräte haben kein `Desc` und zeigen ihren `Title`.
→ Bei konventionellen Kontakten `Desc` sprechend setzen (kurz, der Raum steht ohnehin darunter).

### Seitenübergreifende Verbindungen gibt es tatsächlich

Die Regel „Verbindungen gelten innerhalb einer Programmseite" stimmt als *Entwurfsregel*, aber
Config **speichert und verarbeitet** auch Verbindungen über Seitengrenzen hinweg. Im Projekt
Bestandsprojekt: 1326 seiteninterne und **67 seitenübergreifende** Verbindungen, teils aus dem
Originalprojekt des Vorgängers, teils aus der Auto-Konfiguration.
→ Ein Skript, das Verbindungen prüft, darf sie **nicht** als Fehler werten.

### Zwei Dinge, die beide wie „Referenzen" aussehen — nur eines ist ein Objekt

**[VERIFIZIERT 05.08.2026]** — frühere Fassung dieses Abschnitts behauptete, die seitenüber-
greifende Linie sei „in Config unsichtbar". **Falsch.**

| | **Referenzobjekt** | **Verbindungs-Stub** |
|---|---|---|
| XML | echtes `<C Type="InputRef">` / `<C Type="OutputRef">` mit `Ref` und `LinkRefType` | **gar nichts** — nur das normale `<In Input="…"/>` am Zielkonnektor |
| Wofür | **Peripherie**: IOs, KNX-/DALI-/Air-Objekte, Merker, Betriebsarten, Daylight | **Baustein → Baustein** |
| Darstellung | Kästchen mit dem Objektnamen | Kästchenpaar, beschriftet `<Zielkonnektor>: <Zielbaustein>` bzw. `<Quellkonnektor>: <Quellbaustein>` |
| Anlass | immer, wenn ein Peripherieobjekt auf einer Seite gebraucht wird | wenn Quelle und Ziel im Layout **weit auseinander** liegen — auch **auf derselben Seite** |

**Beweis:** Zwei per Skript angelegte Baustein-zu-Baustein-Verbindungen über Seitengrenzen
(`SequenceController.AQ4 → HeatIRoomController2.Window` und `.AQt → SequenceController.AI4`).
Nach dem Öffnen und Speichern durch Config: Objektzahl **2201 → 2201**, Verbindungen
**1411 → 1411**. Config hat für die Stub-Kästchen **kein** Objekt angelegt — sie entstehen beim
Zeichnen. Im selben Projekt wird `PresenceDetector.OutputPresence → HeatIRoomController2.Move`
ebenfalls als Stub gezeichnet, obwohl beide Bausteine **untereinander auf einer Seite** stehen.

### Das Attribut `FLG` am `<In>`-Element steuert die Darstellung

**[VERIFIZIERT 05.08.2026]** — Bestandsprojekt, 1411 Verbindungen.

```xml
<Co K="Move" Nc="1" U="…">
  <In Input="…" FLG="2"/>
</Co>
```

| Wert | Bedeutung | Häufigkeit im Projekt |
|---|---|---|
| *(fehlt)* | normale Linie im Diagramm | 1299 |
| **`FLG="2"`** | **als beschriftete Referenz zeichnen** — Kästchenpaar `<Zielkonnektor>: <Zielbaustein>` | 87 |
| `FLG="1"` | **Geräte-/Objektzuordnung** — Verbindungen aus dem Dialog *Objekte zuordnen*: Loxone-Air-Melder an `DeviceTrigger`, Air-Kontakte an `Alarm.HI3/HI4`, `SmokeAlarm.InputAir*`, API-Konnektoren | 25 |

**`FLG="2"` ist keine Seiten-Eigenschaft:** 74 der 87 liegen auf **derselben** Seite — Config
setzt es, wenn Quelle und Ziel im Layout weit auseinanderstehen. Beispiel aus dem Projekt:
`PresenceDetector.OutputPresence → HeatIRoomController2.Move`, beide Bausteine untereinander auf
einer Seite, trotzdem `FLG="2"`.

**Praxis beim Skripten:**
- Eine Baustein-zu-Baustein-Verbindung per Skript anzulegen ist **zulässig**, auch über
  Seitengrenzen. Man braucht weder Merker noch Referenzobjekt.
- Ohne `FLG` zeichnet Config eine **Linie**, die bei seitenübergreifender Verbindung als
  unbeschriftetes „loses Ende" zum Seitenrand läuft — sieht nach Fehler aus, ist keiner.
- Wer die saubere Darstellung will, setzt **`FLG="2"` selbst**. Config übernimmt das und
  beschriftet das Kästchen beim Zeichnen.
- Config vergibt `FLG="2"` beim eigenen Speichern **nicht zuverlässig nachträglich**: von zwei
  gleichzeitig per Skript angelegten seitenübergreifenden Verbindungen bekam nur eine ein `FLG`.
- **`FLG="1"` niemals selbst setzen oder verändern** — das gehört zur Objektzuordnung des
  jeweiligen Bausteins (Attribut `DEVS`, `iObj`, `Objects`) und nicht zur Zeichnung.

> ⚠️ Beim Suchen im Diagramm: der Stub trägt den **Ziel**konnektor im Text, nicht den eigenen.
> `Dwc: Raumregelung Bad OG` am Ausgang heißt „geht auf den `Dwc`-Eingang der Raumregelung".

### `LinkRefType` am `InputRef`/`OutputRef` — bekannte Werte

Das Attribut sagt Config, **welche Art Peripherieobjekt** die Referenz darstellt. Es ist nicht
ableitbar und darf **nicht geraten** werden. Aus dem Bestandsprojekt erhoben (07.08.2026):

| Wert | Zieltyp | | Wert | Zieltyp |
|---|---|---|---|---|
| 2 | `Online` | | 103 | `Lox1wireAsensor` |
| 21 | `Mode` (Betriebsart) | | 126 | `DaliGroup` |
| 51 | `VoltageIn` | | 127 | `DaliActor` |
| 55 | `DigitalIn` | | 129 | `DaliSwitch` |
| 63 | `Actor` | | 136 | `ApiActor` |
| 66 | `EIBsensor` | | 172–175 | `LoxAIRsensor` / `LoxAIRAsensor` / `LoxAIRactor` / `LoxAIRAactor` |
| 69 | `EIBactor` | | 282 | `Daylight2` |
| 71 | `VirtualIn` | | 287 | `StartPulse` |
| **74** | **`VirtualOutCmd`** | | 307 | `SysVar` |
| 95 | `CallerVirtualIn` | | 320 | `Memory` |

Fehlt ein Typ in dieser Liste: **ein** Objekt in Config von Hand auf eine Seite ziehen, speichern,
Wert auslesen — dann den Rest skripten. Alternativ ganz ohne Referenzobjekt arbeiten und die Logik
direkt auf den `<Co K="I">` des Peripherieobjekts legen (funktioniert, ist nur nicht gezeichnet).

> 🛑 **Eine neu gezogene Ausgangsreferenz ERSETZT eine bestehende Verbindung am Eingang des
> Peripherieobjekts, sie ergänzt sie nicht.** Verifiziert 07.08.2026: `Mode "Schlafen".Q →
> VirtualOutCmd.I` war spurlos weg, nachdem derselbe Befehl per Drag&Drop als Ausgangsreferenz auf
> eine Seite gelegt wurde. Nach jedem manuellen Eingriff in Config die Konnektorenpaare gegen den
> Vorstand diffen (siehe Rebuild-Check).
>
> Ebenso: **`Inv` bleibt am Konnektor stehen, wenn die Quelle wechselt** (Falle 8). Eine Inversion,
> die für ein Betriebsart-Signal gedacht war, dreht danach den Taster aus der Visualisierung um.

### ⚠️ Falle: `InputRef`-Konnektoren
```
AI  <=  Quelle.Q    (Zustand)      ->  Ausgang  AQ   = Zustand
I   <=  Quelle.Qe   (FEHLER)       ->  Ausgang  Q    = FEHLER
```
**`InputRef.Q` ist der Fehlerausgang, nicht der Zustand.** Für Zustände immer **`.AQ`** verwenden.
Loxone macht das intern genauso.

---

## 3. Bausteintypen (XML-Name ↔ GUI-Name)

| XML `Type` | GUI |
|---|---|
| `HeatIRoomController2` | Intelligente Raumregelung |
| `IRoomcontrol` | Intelligente Raumregelung (Altbaustein) |
| `LightController2` | Beleuchtungssteuerung |
| `AutoJalousie` | Automatikbeschattung (früher Automatikjalousie) |
| `PresenceDetector` | Präsenz |
| `HVACController` | Heiz- und Kühlsteuerung |
| `CentralLight` / `CentralShade` / `CentralGate` / `CentralAlarm` / `CentralPresence` | Zentralbausteine |
| `SmokeAlarm` | Brandmeldezentrale |
| `AlarmChain` | Alarmierungskette |
| `2Point` | 2-Punkt-Regler |
| `StairwayLS` | Treppenlichtschalter |
| `EIBsensor` / `EIBactor` | KNX-Gruppenobjekt lesend / schreibend |
| `DaliDevice` / `DaliActor` / `DaliSensor` / `DaliGroup` | DALI |
| `Lox1wireAsensor` | 1-Wire-Fühler |
| `DigitalIn` / `Actor` / `VoltageIn` / `VoltageOut` | Extension-Klemmen |
| `Place` / `Category` / `Page` / `Mode` / `Memory` | Raum / Kategorie / Programmseite / Betriebsart / Merker |
| **`RoofWindow`** | **Dachfenster** (Fenstermotor) — Konnektoren `FullOpen`/`FullClose`/`So`/`Protection`, Ausgänge `OpenOut`/`CloseOut` |
| **`ShadeRoof`** | **Dachfenster Beschattung** (das Rollo davor), `Nio="38"` — `FullUp`/`FullDown`, `OutputUp`/`OutputDown`, `AutoEnable`/`AutoDisable`/`AutoReacivate`. **Hat keinen `Type`-Parameter** (Bausteinart ist bereits festgelegt), dafür `Tilt` = Dachneigung. |
| `WindowsMonitor` | Fenster- und Türüberwachung — `W` = Dwco (Sammeleingang, invertiert), `HI2` = zugeordnete Loxone-Geräte (Liste im Attribut **`iObj`**) |
| `Doorcontroller` | Türsteuerung — **kein** Eingang für Tür-/Fensterkontakte; Kontakte gehören auf die Fenster-/Türüberwachung bzw. die Alarmanlage |

### Virtuelle Ausgänge — Attributnamen

**[VERIFIZIERT 07.08.2026]** — aus dem Stringtable von `LoxoneConfig.exe` 17.1.7.27 gelesen
(die Namen liegen dort als zusammenhängender Block neben `SourceValHigh`/`CmdSep`), gegengeprüft
gegen ein von Config selbst geschriebenes Objekt. **Nicht geraten.**

| GUI-Feld | Attribut | am Objekt |
|---|---|---|
| Adresse | `Address` | `VirtualOut` |
| Befehl bei Initialisierung | `CmdInit` | `VirtualOut` |
| Trennzeichen / Verbindung schließen | `CmdSep` / `CloseAfterSend` | `VirtualOut` |
| Befehl bei EIN / AUS | `CmdOn` / `CmdOff` | `VirtualOutCmd` |
| HTTP-Post-Befehl bei EIN / AUS | `CmdOnPost` / `CmdOffPost` | `VirtualOutCmd` |
| HTTP-Erweiterung bei EIN / AUS | `CmdOnHTTP` / `CmdOffHTTP` | `VirtualOutCmd` |
| HTTP-Methode bei EIN / AUS | `CmdOnMethod` / `CmdOffMethod` | `VirtualOutCmd` |
| als Analogausgang / Wiederholrate / Antwort | `Analog` / `Repeat` / `CmdAnswer` | `VirtualOutCmd` |

Sonderzeichen aus URL und JSON werden **ganz normal XML-escapet** (`&`→`&amp;`, `"`→`&quot;`).
`IName` (`VQ1`, `VQC1`, …) muss projektweit eindeutig sein. Analog dazu am virtuellen Eingang:
`VirtualInHttp` mit `PollingTime`, `VirtualInHttpCmd`, `VirtualInUdp` mit `Port`.

Der Eingang eines `VirtualOutCmd` (`<Co K="I">`) lässt sich **direkt** aus der Logik speisen —
eine Ausgangsreferenz auf einer Seite ist nur die Zeichnung. Das erspart das Raten des
`LinkRefType`. Gleiches Muster wie bei `EIBactor`: `OutputRef.AQ → EIBactor.I`.

**Vorsicht bei `RoofWindow` vs. `ShadeRoof`:** In KNX-Bestandsanlagen heißen die Aktoren gern
`DF Bad auf/zu` (Fenstermotor) und `DF Jal Bad auf/zu` (Rollo). Sitzt versehentlich eine
**Automatikbeschattung** auf den Fenstermotoren, öffnet die Sonnenstandsautomatik bei Sonne das
**Fenster** statt zu beschatten — und der Windalarm reißt es auf (siehe Falle 4).

---

## 4. Intelligente Raumregelung — Konnektor-Mapping

`Type="HeatIRoomController2"`, `V="175"`, **`Nio="57"`**

### Eingänge
| XML `Co K` | Doku-Kürzel | Bedeutung |
|---|---|---|
| `AMode` | Mode | Betriebsart −1…5 |
| `Input` | ϑt | Zieltemperatur (nur Modi 3–5) |
| **`Temp`** | **ϑc** | **Ist-Temperatur** |
| **`Window`** | **Dwc** | **Fenster-/Türkontakt** (0 = zu) |
| `Comfort` | C | Komfort starten |
| `Save` | E | Eco starten |
| `Save2` | Bp | Gebäudeschutz |
| **`Move`** | **P** | **Präsenz** |
| `Reset` | Off | Aus / Sperren |
| `DisMv` | DisP | Präsenzeingang deaktivieren |
| `RtD` | Rtd | auf Vorlagenwerte zurücksetzen |
| **`TempO`** | **ϑo** | **Außentemperatur** — unverbunden lassen, nutzt dann die Systemvariable |
| `InCo2` / `InHumid` | CO2 / H | nur Durchreichung, nicht in der Regelung |
| `inFan` / `inAirDir` | Fan / ADir | Lüfterstufe / Luftrichtung |

### Ausgänge
| XML `Co K` | Doku | Bedeutung |
|---|---|---|
| **`AQh` / `AQc` / `AQhc`** | H / C / HC | **Heizen / Kühlen / kombiniert**, 0…10 |
| `AQh1…3`, `AQc1…3`, `AQhc1…3` | H1–3 … | nur bei konfigurierten Quellen sichtbar |
| **`Qs`** | **Shd** | **Beschattungsanforderung** → Automatikbeschattung |
| `AQs` | Os | aktueller Temperaturmodus |
| `Qe` | Error | Fehler |
| `Qa` | – | (Alarm/aktiv) |
| `AQt` | ϑt | aktuelle Solltemperatur |
| `AQhm` | HCm | 1 = Heizen, −1 = Kühlen, 0 = Aus |
| `AQtm` | Om | Betriebsmodus-ID aus der Schaltuhr |
| `Qb` | Boost | Vorbereitungsphase aktiv |
| `OutputAPI` | API | |

### Parameter
| XML `Co K` | Doku | Bedeutung |
|---|---|---|
| `TComfort` | ϑch | Komforttemperatur Heizen |
| `TComfortC` | ϑcc | Komforttemperatur Kühlen |
| `TComfortHC` | ϑchc | eine gemeinsame Komforttemperatur |
| `TDiff` | ϑd | erlaubte Abweichung Komfort |
| `TSaveL` / `TSaveU` | ϑeh / ϑec | Eco-Offset Heizen / Kühlen |
| `TSave` | ϑe | erlaubte Abweichung Eco |
| **`TShadeHeat` / `TShadeCool`** | **ϑsh / ϑsc** | **Beschattungstemperatur Heiz-/Kühlbetrieb** |
| `TDeepSleep` | ϑfp | Frostschutz |
| `TMax` | ϑhp | Hitzeschutz |
| `TimeMove` | Vs | Ventilschutz (Tage) |
| `TimeC` / `TimeS` / `TimeMv` | Cet / EBpet / Pet | Nachlauf Komfort / Eco / **Präsenz** |
| `THCelvin` / `TCCelvin` | Hs / Cs | Aufheiz-/Abkühlgeschwindigkeit (0 = lernen) |
| **`TPWM`** | **Pwm** | **PWM-Intervall** (leer/0 = automatisch 10–60 min) |
| `TWin` | Ddwc | Verzögerung Fensterkontakt |
| `TExcess` | ϑExc | Temperatur-Offset bei Überschussenergie |

### Attribute
| Attribut | Bedeutung |
|---|---|
| `UUIDTimer` | verweist auf die integrierte Schaltuhr — legt Config selbst an |
| `Objects` | **UUID der Heiz- und Kühlsteuerung**, an der sich der Regler registriert |
| `SourceCap`, `Cap` | Fähigkeits-Bitmasken, setzt Config selbst |
| `PrioH` / `PrioC` | Quellen-Priorität Heizen / Kühlen |
| `ExT` | Erweiterungstyp (2 bei Schlafraum-Vorlage, 3 sonst) |
| `AQDig` | vermutlich „PWM Ausgänge" — **noch nicht bestätigt** |

### Die integrierte Schaltuhr: `<Timer>` — und die stille Falle der leeren Spalte

**[VERIFIZIERT 07.08.2026]** — Bestandsprojekt, 13 Raumregler.

```xml
<Timer M="5" UserModes="2" DefValue="0" N="15"
       Modes="00000000-0000-0003-1500000000000000,00000000-0000-0001-1500000000000000,
              00000000-0000-0004-1500000000000000, … 00000000-0000-000a-1500000000000000">
  <Entry            To="1440"  V="1"/>   <!-- Ix fehlt = Ix 0 -->
  <Entry Ix="1"     To="1440"  V="1"/>
  <Entry Ix="2"     To="360"   V="1"/>
  <Entry Ix="2" From="1200" To="1440" V="1"/>
  …
</Timer>
```

| Attribut | Bedeutung |
|---|---|
| `Modes` | **Reihenfolge der Spalten**, als Komma-Liste von `Mode`-UUIDs. `Ix` in den Einträgen indiziert genau in diese Liste (0-basiert, fehlendes `Ix` = 0). |
| `N` | Anzahl der `<Entry>`-Elemente |
| `UserModes` | Zahl der Spalten **vor** den sieben Wochentagen … außer Heiz-/Kühlperiode, die zählen nicht mit |
| `DefValue` | Wert außerhalb aller Einträge |
| `From` / `To` | Minuten ab Mitternacht; fehlendes `From` = 0, `To="1440"` = 24:00 |
| `V` | Temperaturmodus wie am Ausgang `Os`: **0 = Eco · 1 = Komfort · 2 = Gebäudeschutz** (−1 = Aus, 3/4 = manuell) |

Die System-Betriebsarten haben feste UUIDs `00000000-0000-000X-1500000000000000`:
`1` Feiertag · `2` Urlaub · `3` Freier Tag/Schulferien · `4`–`a` Montag–Sonntag ·
`b` Heizperiode · `c` Kühlperiode. Benutzer-Betriebsarten stehen mit ihrer eigenen UUID drin.

> 🛑 **Eine vorhandene, aber leere Mode-Spalte schaltet den Raum ab, sobald die Betriebsart aktiv
> wird.** Steht eine Betriebsart in `Modes`, hat aber **keinen** `<Entry>`, dann gilt für den
> ganzen Tag `DefValue` — **nicht** der Wochentag. Bei `DefValue="0"` heißt das Eco rund um die
> Uhr, solange die Betriebsart läuft.
> Im Bestandsprojekt hatten zwei Kinderzimmer eine leere Spalte *Freier Tag/Schulferien* (→ neun
> Wochen Eco in den Sommerferien) und der Fitnessraum leere Spalten *Heiz-* **und** *Kühlperiode*
> (→ ganzjährig Eco, die Wochentage kamen nie zum Zug).
> **Prüfroutine:** je Regler `Modes` gegen die vorhandenen `Ix`-Werte halten; jede Spalte ohne
> Eintrag ist ein Befund.

### Betriebszeiten / Kalender — `<C Type="CalendarEntry">`

| Attribut | Bedeutung |
|---|---|
| `CalType` | **welche Betriebsart** der Eintrag aktiviert = die `Mode`-Nummer des Ziel-`<C Type="Mode">` (2 = Freier Tag/Schulferien, 10 = Heizperiode, 11 = Kühlperiode). Fehlt = Feiertag. |
| `Mode` | **Typ des Eintrags**: fehlt = jährlich fixes Datum · `1` = relativ zu Ostern (`EasterOffset`) · `4` = **Zeitraum** `Month/Day` bis `Month2/Day2` |
| `Month`,`Day` / `Month2`,`Day2` | Beginn / Ende |
| `EasterOffset`, `WeekDayInMonth` | Osterbezug bzw. „n-ter Wochentag im Monat" |

> ⚠️ **Kalendereinträge kennen kein Jahr** — es gibt kein `Year`-Attribut, jeder Eintrag
> wiederholt sich jährlich. Für Schulferien (die sich jedes Jahr verschieben) heißt das:
> **ein Zeitraum-Eintrag, jährlich zu pflegen** — nicht zwei Einträge „Start" und „Ende".

---

## 4b. Heiz- und Kühlsteuerung — Konnektor-Mapping

`Type="HVACController"`, `Nio="38"`. Die XML-Namen sind hier **systematisch irreführend** —
verifiziert 03.08.2026 dadurch, dass in einem unangetasteten Baustein *jeder* Wert exakt dem
Doku-Default entspricht:

| XML `Co K` | Doku | Bedeutung | Default |
|---|---|---|---|
| `Temp` | ϑo | Außentemperatur — **unverbunden = Systemvariable „Außentemperatur"**; `Def=-1000` heißt „kein Wert" | −1000 |
| **`Average`** | **`Otm`** | **Außentemperatur-Modus**: 0 = deaktiviert · 1 = Durchschn. 48 h · 2 = Systemvariable „Erw. Durchschn. 48 h" · 3 = Aktuelle Temperatur | **2** |
| **`TempLimitC`** | **`ϑLimH`** | **Heizgrenze** — keine Heizung, wenn verwendete Außentemp. **über** diesem Wert | **18** |
| **`TempLimitH`** | **`ϑLimC`** | **Kühlgrenze** — keine Kühlung, wenn verwendete Außentemp. **unter** diesem Wert | **15** |
| `OnThreshold` | Sot | mittlere Ventilanforderung **aller** Raumregler muss darüber liegen | 30 % |
| `TimeAddional` | Tt2s | Verzögerung bis Stufe 2 | 60 min |
| `TempAdditional` | ϑminS2 | Außentemp., unter der Stufe 2 sofort kommt | −6 °C |
| `TempMin` | ϑminHP | minimale Außentemp. für Wärmepumpenbetrieb | −22 °C |
| `FanDelay` | Fod | Ventilator-Nachlauf | 120 s |
| `TimePulseOn` / `TimePulseOff` | Don / Doff | Taktung Ein / Aus | 750 / 300 s |
| `Mode` | Mode | −1 aus · 0 Automatik · 1 nur Heizen · 2 nur Kühlen | **−2** |
| `CoolAvailable` / `HeatAvailable` | — | Rückmeldung des Erzeugers; **unbeschaltet nimmt der Baustein „verfügbar" an** | – |

> ⚠️ **`TempLimitC` ist die HEIZgrenze, `TempLimitH` die KÜHLgrenze.** Wer nach dem Buchstaben geht,
> verstellt den falschen Wert und wundert sich, dass nichts passiert. Im Config-Dialog stehen die
> deutschen Beschriftungen — **dort einstellen, nicht blind per Skript**.

**Warum die Kühlung nicht anläuft — die Reihenfolge zum Prüfen:**
1. `Mode` — bei −2 (Werksstand) macht der Baustein gar nichts.
2. `Average`/`Otm` — steht es auf 2, ist der Eingang `Temp`/ϑo **wirkungslos**; der Baustein liest
   die Systemvariable „Erwartete durchschnittliche Außentemperatur 48 h". Ein manuell eingespeister
   Testwert wirkt erst bei `Otm = 3`.
3. Kühlgrenze (`TempLimitH`) — darunter keine Kühlung, egal wie hoch die Anforderung ist.
4. `OnThreshold`/Sot — der **Mittelwert über alle** Raumregler muss darüber liegen; ein einzelner
   kühlender Raum reicht nicht.

**Systemvariablen sind nicht beschreibbar.** „Außentemperatur" & Co. kommen vom Loxone-Wetterdienst.
Zum Testen entweder `Otm` auf 0 (Außentemperatur wird ignoriert) oder einen **virtuellen analogen
Eingang** auf ϑo legen **und** `Otm = 3` setzen — danach wieder abklemmen, sonst bleibt die Anlage
auf dem Testwert stehen.

---

## 5. Automatikbeschattung — Konnektor-Mapping

`Type="AutoJalousie"`, `Nio="49"`

| XML `Co K` | Doku | Bedeutung |
|---|---|---|
| `InputTrigger` | Tg | Toggle auf/stopp/zu |
| `InputTriggerUp` / `InputTriggerDown` | Po / Pc | partiell öffnen / schließen |
| `EndUp` / `EndDown` | Co / Cc | vollständig öffnen / schließen |
| `Shade` | So | schließen + Lamellen horizontal |
| **`AutoShade`** | **Sps** | **Sonnenstandsautomatik starten** ← hier kommt `IRC.Qs` rein |
| `EnAutoShade` | DisSp | Sonnenstandsautomatik deaktivieren |
| `ReactAutoShade` | Spr | Automatik neu starten |
| `Safety` | Wa | **Windalarm** |
| `Window` | Dwc | Fenster-/Türkontakt |
| `Stop` | Off | Stopp / Sperren |
| `ManualPosition` / `ManualLamelle` | Pos / Slat | Position / Lamellen |
| `Gesture` | T5 | T5-Bedienung |
| `InputDisable` | DisPc | Peripheriebedienung sperren |
| `OutputUp` / `OutputDown` | Op / Cl | Relais auf / zu |

Wichtige Parameter/Attribute:

| Name | Bedeutung | Default |
|---|---|---|
| `AutMode` | Sonnenstandsautomatik-Modus (0=Helligkeit, **1=Kühlung**) | 1 |
| **`Dir`** | **Himmelsrichtung** (0=N, 90=O, 180=S, 270=W) | **−1 = nicht konfiguriert** |
| `DirTol` / `DirTol2` | Richtungstoleranz Ein-/Austritt | 85° |
| `AutoShadeTime` | Lamellen-Nachführintervall | 120 min |
| `TimeEnd` / `TimeEndDown` | Fahrzeit auf / ab | 75 / 70 s |
| `SRoff` / `SSoff` | Verschiebung Sonnenauf-/untergang | +30 / −30 min |
| `Width` / `Space` | Lamellenbreite / -abstand | 70 / 60 mm |
| **`Sun`** (Attribut) | **„Sonnenschein verwenden"** | `true` bei Autokonfig-Erzeugung |

**Voraussetzungen für die Sonnenstandsautomatik:** GPS-Koordinaten im Projektkopf **und** `Dir` je
Baustein. `Dir` bleibt auch nach der Auto-Konfiguration auf −1 → immer manuell nachziehen.

### Parameternamen: XML ↔ Doku (Beschattung)

Die häufigste Fehlerquelle beim Auswerten per XPath — die KB-Kürzel existieren im XML **nicht**:

| XML `Co K` | Doku | Bedeutung | Default |
|---|---|---|---|
| `Type` | Type | 0 Jalousie/Raffstore · 1 Rollladen/Rollo · 2/4/5 Vorhang · 3 Retrolux · 6 Markise | **0** |
| `TimeEnd` / `TimeEndDown` | Opd / Cld | Fahrzeit auf / ab | 75 / 70 s |
| `SO` | Rd | Rücklaufzeit bis Lamellen horizontal — bei Type 1 die Zielposition für `So` | 0,8 |
| `AutMode` | Spm | Sonnenstandsautomatik-Modus | 1 |
| `AutoShadeEnd` | Spe | Endaktion der Automatik | 1 |
| `Width` / `Space` | Sw / Sd | Lamellenbreite / -abstand | 70 / 60 mm |
| `AutoShadeTime` | Spi | Lamellen-Nachführintervall | 120 min |
| `SRoff` / `SSoff` | Spos / Spoe | Verschiebung Sonnenauf-/untergang | +30 / −30 min |
| `DirTol` / `DirTol2` | Dts / Dte | Richtungstoleranz Ein-/Austritt | 85° |

`Type` wird von der Auto-Konfiguration **nicht** gesetzt und bleibt auf 0 — in einem Bestandsprojekt
sind also alle Rollläden als Raffstore parametriert, bis es jemand korrigiert. Das ändert, was der
Befehl `So` tut (Raffstore: zufahren + Lamellen horizontal · Rollladen: Position laut `SO`/`Rd`).

### Lebenszyklus der Sonnenstandsautomatik — warum sie „immer aus" ist

Der Ausgang `Sp`, den die App als „Sonnenstandsautomatik" anzeigt, ist **kein Dauerzustand**:

1. Er ist nur ein, wenn Eingang **`AutoShade` (Sps) = 1** und `EnAutoShade` (DisSp) = 0 — oder wenn
   der Anwender den Schalter **in der App** setzt (das ist das manuelle Gegenstück zu `Sps`).
2. Kommt `Sps` wie üblich vom Raumregler-Ausgang `Qs`, liegt es nur an, **solange der Raum zu warm
   ist**. Kühler Raum → „keine Sonnenstandsautomatik". Das ist gewollt, kein Fehler.
3. **Jede Handbedienung deaktiviert die Automatik für den Rest des Tages** (KB, Eingang `Sps`).
   Reaktivierung nur über einen Impuls an `ReactAutoShade` (Spr) **gefolgt von** einer steigenden
   Flanke an `Sps` — oder am nächsten Tag zu Beginn der Beschattungszeit.
4. Bei `AutMode` (Spm) **0 oder 1** — Default! — **bleibt die Automatik bei geschlossener
   Beschattung aus**. Ein `Spr`-Impuls auf einen zugefahrenen Behang bewirkt also *nichts*.
   Nur 2 und 3 aktivieren auch bei geschlossener Beschattung.
5. `AutoShadeEnd` (Spe, Default 1 = vollständig öffnen) ist die **einzige** automatische
   Auffahrbewegung, die der Baustein von sich aus macht — und nur, wenn die Automatik regulär bis
   zum Ende der Beschattungszeit lief, nicht nach einem Handeingriff.

**Konsequenz für „morgens soll aufgefahren werden":** Ein `Spr`-Impuls reicht nicht. Es braucht
einen echten Fahrbefehl (`EndUp`/Co bzw. `Shade`/So) — und weil der selbst als Handbedienung zählt,
den `Spr`-Impuls **danach**, mit ein paar Sekunden Verzögerung.

**Zentralbausteine (`CentralShade`, `CentralLight`, …) haben keine eigene Schaltuhr.** Sie reichen
nur Befehle an die Mitglieder in `rec` weiter. Wer eine Tages- oder Ankunftsautomatik will, muss
sie selbst bauen.

---

## 6. Kopplung Heizung ↔ Beschattung

```
IRC.Qs (Shd)  ────►  AutoJalousie.AutoShade (Sps)
```

Auslösung: im **Heizbetrieb** bei ϑc > `TShadeHeat`, im **Kühlbetrieb** bei ϑc > `TShadeCool`,
Hysterese 0,4 K. **Nur wirksam in Mode 0/1/2**, nicht in den Fix-Sollwert-Modi 3–5.

Ist am Raumregler **ausschließlich** `Qs` beschaltet (kein Stellantrieb), setzt sich der Baustein
automatisch auf Mode 2 (nur Kühlen) und wird zum reinen Hitzeschutz-Geber.

---

## 7. Zentralbausteine: Mitglieder-Zuordnung

Zentralbausteine verdrahten ihre Mitglieder **nicht**, sondern führen eine UUID-Liste im Attribut:

| Baustein | Attribut | Inhalt |
|---|---|---|
| `CentralLight`, `CentralShade`, `CentralGate`, `CentralAlarm`, `CentralPresence` | **`rec`** | UUIDs der zugeordneten Raumbausteine |
| `SmokeAlarm` | **`Objects`** | UUIDs aller überwachten Objekte |
| `HeatIRoomController2` | **`Objects`** | UUID der Heiz- und Kühlsteuerung |
| `PresenceDetector` | **`DEVS`** | UUIDs der zugeordneten Melder |
| `WindowsMonitor` | **`iObj`** | UUIDs der zugeordneten Loxone-Geräte (deren Signale liegen zusätzlich am versteckten Eingang `HI2`) |
| `Alarm` | **`Objects`** | gemischt: die zugeordneten Melder **und** die Licht-/Beschattungsbausteine, die im Alarmfall reagieren sollen |

### Alarmanlage: XML-`I1`…`I5` ↔ Doku-Kürzel

Die Melder-Eingänge heißen im XML durchnummeriert und in der Doku sprechend — Reihenfolge
verifiziert 03.08.2026:

| XML | Doku | Bedeutung |
|---|---|---|
| `I1` | P | Präsenz |
| `I2` | Gb | Glasbruch |
| `I3` | Wc | **Fensterkontakte** — 0 = geschlossen, 1 = offen |
| `I4` | Dc | **Türkontakte** — 0 = geschlossen, 1 = offen |
| `I5` | Ot | sonstige Melder (z. B. Sabotage) |

Weil `Wc`/`Dc` **1 = offen** erwarten, die Fenster-/Türüberwachung an `W` (Dwco) aber üblicherweise
**invertiert** betrieben wird, landen dieselben Kontakte an beiden Bausteinen mit *entgegengesetzter*
Auffassung, wenn man nicht aufpasst. Beim Übernehmen aus einem Altprojekt ist die Verdrahtung an
`I3`/`I4` deshalb der verlässlichste Hinweis darauf, welche Polarität der Vorgänger angenommen hat.

→ Beim Anlegen neuer Raumbausteine per XML **muss** die jeweilige `rec`-Liste ergänzt werden,
sonst hängt der Raum nicht an der Zentrale.

---

## 8. Räume & Kategorien

### Raumtyp `PType` am `<C Type="Place">`
*Offiziell nirgends dokumentiert — verifiziert aus Loxone's `FactoryPresets.xml`:*

| `PType` | intern | deutsch |
|---|---|---|
| 1 | `SleepingRoom` | Schlafraum |
| 2 | `LivingRoom` | Aufenthaltsraum |
| 3 | `PassageRoom` | Durchgangsraum |
| 4 | — | Zentral / Technik |
| 5 | — | Außen |

`Sqm` = Raumgröße in m². Geht direkt in die Bedarfsberechnung der Heiz- und Kühlsteuerung ein
(*„(Zieltemperatur − aktuelle Temperatur) × Raumgröße"*) — unbedingt pflegen.

### Kategorie-Verwendung `CatGroup` am `<C Type="Category">`
Beobachtete Werte: Beschattung=1 · Beleuchtung=2 · Temperatur=3 · Audio=4 · Klima=5 ·
**Fühler=6** · Stellantrieb=7 · **Heizung=8** · Melder=9 · Lüftung=10 · Überwachung=12 ·
Alarm=14 · Tor=15 · Wellness=16 · Zutritt=31 · Verbraucher=33 · Elektrofahrzeug=41 ·
Wecker=43 · Wetter=48 · Energie=51 · Einstellungen=52 · Bedienelemente=57

### Die vier Zuordnungsregeln der Auto-Konfiguration
> Stellantriebe = **Heizung** · Temperatur Sensoren = **Fühler** ·
> Jalousien = **Beschattung** · Lampen = **Beleuchtung**

Der erzeugte **Raumregler-Baustein** selbst landet dagegen in Kategorie **Klima**.

Für **Fensterkontakte** und **Präsenzmelder** gibt es keine dokumentierte Regel — die Verbindung
auf `Window` bzw. `Move` ist immer Handarbeit.

---

## 9. Werksvorgaben: `FactoryPresets.xml`

`C:\ProgramData\Loxone\Loxone Config <Version>\Templates\FactoryPresets.xml`

Enthält je Raumtyp die kompletten Baustein-Vorlagen mit allen Defaults und Schaltuhren —
das ist die Quelle, aus der die Auto-Konfiguration schöpft. Details und Wertetabellen in
[autokonfiguration.md](autokonfiguration.md).

Ein daraus entnommener Baustein trägt eine ältere `V`-Nummer (z. B. 124). **Loxone Config migriert
ihn beim Öffnen selbstständig** auf die aktuelle Version (175) und ergänzt fehlende Konnektoren,
Timer und `SpStates`. Verifiziert am 30.07.2026: Nio 40 → 57.

**Bewährtes Vorgehen:** Baustein aus `FactoryPresets.xml` einsetzen → Datei einmal in Loxone Config
öffnen und speichern → danach den migrierten Baustein als Vorlage für alle weiteren Räume nehmen.

---

## 10. Grenzen der Auto-Konfiguration

**Sie erkennt KNX- und DALI-Peripherie nicht als Klima-/Beschattungs-Geräte.** Im Testprojekt waren
die Spalten *Beschattung, Klima, Audio, Peripherie, Präsenz* bei allen 19 KNX-Bestandsräumen
ausgegraut — nur der Raum mit Loxone-Air-Geräten war anwählbar. Verfügbar blieben *Beleuchtung*,
*Wecker* (nur Schlafräume) und *Raum verlassen* (nur Räume mit verdrahtetem Bewegungsmelder).

→ In KNX-Bestandsprojekten ist die Auto-Konfiguration **kein Generator**, sondern nur eine
**Parametrier-Referenz**. Die Bausteine müssen von Hand oder per XML gebaut werden.

Weitere Einschränkungen: Jalousie-Ausgänge werden nie automatisch verbunden („aus Sicherheits-
gründen"), und die Auto-Konfiguration legt **neben** bestehende Seiten neue an — in Bestands-
projekten also nur auf einer Wegwerf-Kopie laufen lassen.

---

## 11. Erzeugte Dateien prüfen

Gilt, sobald ein Skript ein Projekt **erzeugt** statt nur zu patchen — Demoprojekt aus einem
Kundenprojekt, Vorlage aus einem Bestand, Projekt-Teilung. Verifiziert 27.08.2026 an 14
Projektständen desselben Hauses (Config 17.1.7.27).

**Warum überhaupt.** Wohlgeformtes XML, null Verbindungen ins Nichts und aufgelöste
`Ref`/`RefL` reichen **nicht**. Config wies eine so geprüfte Datei mit
„Das aus dem Miniserver geladene Projekt hat einen fehlerhaften Inhalt!" ab. Die Meldung liegt
in `LoxoneConfigres_DEU.dll` neben „Projekt nicht vorhanden" / „Projekt mit fehlerhaftem Inhalt"
und erscheint auch beim gewöhnlichen Datei-Öffnen — sie ist die generische Ablehnung beim Laden,
kein Miniserver-Thema. **Es gibt dazu kein Logfile und keine Detailmeldung.**

### Die harte Prüfung: `Document/@NumO`

**`NumO` ist exakt die Anzahl der `<C>`-Elemente im File.** Das ist die Bedingung, an der eine
erzeugte Datei scheitert. **[VERIFIZIERT 27.08.2026]:** eine abgewiesene Datei trug `NumO="2240"`
bei 183 Objekten; nach dem Korrigieren **nur dieses einen Attributs** öffnete sie.
In 13 von 14 gewachsenen Projektständen stimmt der Wert exakt — der einzige Ausreißer war selbst
skripterzeugt. Also: nach jedem Anlegen oder Löschen von Objekten neu zählen.

```python
doc.set('NumO', str(sum(1 for e in root.walk() if e.name == 'C')))   # inkl. Document selbst
```

### Was Config beim Laden *nicht* stört

Gemessen an derselben Datei, die nach der `NumO`-Korrektur öffnete — sie enthielt all das
gleichzeitig. Nützlich, um nicht in die falsche Richtung zu suchen:

- leeres `<C>` ausgeschrieben als `<C …></C>`
- fehlende `Category/@RGR`, `Place/@RGR`, `SysVar/@source`, `Document/@APPKEY`, `@APPID`,
  `@CrashL`, `LoxLIVE/@Installation`
- komplett fehlende Onboard-Ein-/Ausgänge des Miniservers
- fehlende `EIBline`, fehlende Benutzer- und Berechtigungsgruppen, fehlende Extensions
- Dangling-UUIDs in `SpStates`, `Icon`, `uuidNotifications`, `RefAS`, `VisuUUID` — die hat
  jedes echte Projekt auch

### Trotzdem: Configs Schreibstil nachbilden

Kosmetik, nicht Ursache — aber es kostet nichts und hält spätere Diffs sauber, weil Config beim
nächsten Speichern ohnehin normalisiert.

| Stil-Regel | Messung |
|---|---|
| Leeres `<C>` immer `<C …/>` | `></C>` kommt in 1,5 MB Projektdatei **nullmal** vor |
| Universelle Attribute leeren statt löschen | je Elementtyp über alle Instanzen geschnitten |

`<IoData></IoData>` schreibt Config dagegen ausgeschrieben — die Selbstschließ-Regel gilt nur
für `<C>`. Wer beim Leeren eines Containers die Kinder entfernt, muss das Element also aktiv
wieder auf selbstschließend setzen.

Universell belegte Attribute (Wert leeren, Attribut behalten):
`Document/@APPKEY` · `@APPID` · `@CrashL` · `Category/@RGR` · `Place/@RGR` ·
`SysVar/@source` · `LoxLIVE/@Installation`.
**Nicht** universell und damit gefahrlos löschbar: `Document/@DeviceTelemetry`.

Zeigt ein Attribut auf ein Objekt, das gelöscht wird (`SysVar/@source` auf ein Air-Gerät,
`Category/@RGR` auf eine Berechtigungsgruppe), ist Umhängen besser als Löschen — beim `source`
etwa auf den `WeatherServer`, der ohnehin bleibt.

### Rezept: Konformitätsprüfung gegen den Bestand

Alle vorhandenen Projektstände als Referenzkorpus nehmen, je `(Elementname, @Type)` schneiden,
welche Attribute **immer** gesetzt sind, und die erzeugte Datei dagegen halten:

```python
always, ever = {}, {}
for e in reference_root.walk():                 # über alle Referenzprojekte
    k = (e.name, e.get('Type'))
    names = {n for n, _ in e.attrs}
    ever[k] = ever.get(k, set()) | names
    always[k] = names if k not in always else (always[k] & names)

for e in generated_root.walk():                 # die erzeugte Datei
    k = (e.name, e.get('Type'))
    fehlt  = always.get(k, set()) - {n for n, _ in e.attrs}   # nie löschen
    fremd  = {n for n, _ in e.attrs} - ever.get(k, set())     # gibt es sonst nie
```

Dieselbe Methode findet auch **strukturelle** Abweichungen: je Container die Kinderzahl in
Referenz und Erzeugnis vergleichen. Übrig bleiben dürfen nur Bereiche, die ein Projekt
legitim leer haben kann (Extensions, Intercoms, virtuelle Ein-/Ausgänge, KNX-Geräte, Seiten).

### Onboard-Ein-/Ausgänge des Miniservers

Sie sind **feste Hardware** und stehen im Projekt, ob verdrahtet oder nicht:
`DigitalIn` I1–I8, `VoltageIn` AI1–AI4, `Actor` Q1–Q8, `VoltageOut` AQ1–AQ4.

Config **toleriert** es, wenn sie fehlen (verifiziert, siehe oben) — inhaltlich beschreibt man
damit aber einen Miniserver, den es nicht gibt, und ein neunter `Actor` „Q9" wäre eine Klemme,
die es nicht gibt. Für ein weitergegebenes Projekt deshalb: vorhandene behalten und für den
Demo-Zweck **umbenennen**, statt sie zu löschen und eigene anzulegen. [ABGELEITET]

Werksbeschriftungen zum Zurücksetzen: `Eingang %d #A%d` · `Aktor (Relais) %d #MS%d` ·
`Spannung %d #I%d` (analog ein) · `Spannung %d` (analog aus).

### Was Config beim ersten Speichern zurückholt

**[VERIFIZIERT 27.08.2026]** an den drei erzeugten Demoprojekten, jeweils in Config geöffnet,
Passwort gesetzt, gespeichert. Config hat dabei je **+19 Objekte** ergänzt und Titel überschrieben:

| Config holt zurück | |
|---|---|
| `EIBline` samt `EIBsensorCaption`/`EIBactorCaption` | leer, mit Vorgabeadresse `1.1.250 14/` |
| die 11 `Permission`-Objekte | Standardrechte |
| 3 `SwitchingTimer`, 2 weitere `LoxCaption` | Systeminventar |

→ **Standard-Rahmenobjekte zu löschen ist zwecklos** — Config legt sie beim nächsten Speichern
neu an. Es schadet nur nicht, weil die Neuanlage leer und vorgabebefüllt ist. Wer Kundendaten
entfernen will, muss also die *Inhalte* leeren, nicht die Container.

**Und: Config besitzt die Namen seiner Systemobjekte.** Beim Speichern hat es **alle 95**
Titel von Betriebsmodi, Zeitfunktionen, Systemvariablen, Berechtigungen und Captions wieder in
die Sprache der eigenen Oberfläche geschrieben — eine vorher gemachte Übersetzung ist damit
weg. **Unberührt bleiben selbst angelegte Objekte:** Seiten, Funktionsbausteine, virtuelle
Ein-/Ausgänge, Notizen und Sequenztexte. Für ein fremdsprachiges Demo heißt das: die eigene
Funktion lässt sich benennen wie man will, das Systeminventar nicht.
Ausnahme in beide Richtungen: eine `InputRef` auf ein **Systemobjekt** (z. B. `StartPulse`)
wird mit umbenannt, eine `InputRef` auf einen **projekteigenen** `Mode` nicht.

### Wenn die Datei veröffentlicht wird

Zusätzlich zu den offensichtlichen Feldern (Adresse, Telefon, Mail, `APPKEY` am `Document`;
`Serial` und `IntAddr` am `LoxLIVE`; KNX-`EIBline`; Extensions samt `<Key>`; Benutzer mit
`HP`-Hashes; Push-Geräte; Mailer- und Caller-Empfänger) stecken zwei Kennungen an Stellen,
an die man nicht zuerst denkt:

1. **Die Miniserver-Seriennummer steckt im UUID-Schwanz** der von Config erzeugten Konnektoren
   (`…-ffff504f941162d7`).
2. **Das Projekt selbst hat eine Kennung im UUID-Schwanz** — im Testprojekt `…-ffff949738c6754e`,
   **828-mal** in einer bereits stark reduzierten Datei. Damit teilt ein veröffentlichtes Demo
   Objektidentitäten mit der laufenden Kundenanlage.

Beides lässt sich gefahrlos ersetzen, weil es opake Kennungen sind: **einheitliche
Textersetzung über alle Attributwerte**, dann bleibt jede Referenz stimmig. Danach mit einem
Leak-Scan gegenprüfen, dass die alten Zeichenketten nirgends mehr vorkommen.

Ebenfalls sinnvoll zu entfernen: `LtE` (Bearbeitungszeitstempel des Quellprojekts) und nicht
verwendete `Category`-Objekte — Letztere lassen sich aus den tatsächlich benutzten
`IoData/@Cr`-Werten bestimmen.

Was danach übrig bleiben darf, ist **ein leeres Loxone-Projekt plus die Funktion**: Kategorien
in Benutzung, zwei Räume, die 22 Standard-Betriebsmodi, die Zeitfunktionen, Wetterserver und
Systemvariablen — alles Loxone-Systeminventar, das in jedem Projekt steht. Im Testfall 148–157
Objekte statt 2240.

### Parser-Falle: Elementtext

`<Key>…</Key>` unterhalb einer Air-Extension (Pairing-Key) enthält **Elementtext** statt
Attributen — im Testprojekt die einzigen zwei Stellen im ganzen File. Ein handgeschriebener
Scanner, der nur `<tag attr="…">` kennt, läuft dort auf einen Fehler. Beim Veröffentlichen ist
dieser Key außerdem ein Geheimnis und muss weg.

### Prüfliste vor der Abgabe

1. **`NumO` = Anzahl `<C>`** — die eine Bedingung, an der Config die Datei sonst abweist.
2. Round-Trip: unveränderte Quelle einlesen und schreiben → muss **byte-identisch** sein.
3. XML wohlgeformt (rohe Umbrüche in Attributwerten vorher maskieren, Falle 10).
4. Jede `<In Input>`, `Ref`, `RefL` löst auf.
5. Stil: kein `></C>` · keine universellen Attribute gelöscht.
6. Strukturvergleich der Container gegen die Referenz.
7. **Und dann trotzdem in Config öffnen** — Punkt 1–6 sind notwendig, nicht hinreichend.
   Danach zusätzlich die Objektzahl je Seite gegenprüfen (Falle 7).
