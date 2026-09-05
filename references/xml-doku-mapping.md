# XML-Konnektoren ↔ Doku-Kürzel — die fehlende Brücke

Die offizielle Loxone-Knowledge-Base nennt die **internen Konnektornamen (`Co/@K`) nirgends**.
Sie beschreibt Ein-/Ausgänge nur mit den GUI-Kürzeln (`Tg`, `Wa`, `Dwc`, …). Dieses Dokument
verbindet beide Welten für alle **29 Bausteintypen** aus
[bausteinvorlagen.xml](bausteinvorlagen.xml).

**Stand:** 30.07.2026 · Loxone Config 17.1.7.27 · ControlList Version 273 · Objektversion `V="175"`

**Gegen TechDoc geprüft am 05.09.2026** ([techdoc-lxres.md](techdoc-lxres.md), Bericht in
[techdoc-abgleich.md](techdoc-abgleich.md)): 424 Zuordnungen bestätigt, **sechs korrigiert** — sie
tragen unten die Marke `[BELEGT-TECHDOC]`. Neue Zuordnungen nicht mehr hier von Hand erheben, sondern
`py -3 scripts/decode_lxres.py <sys_DEU.zip> --block <LxType>` fragen.

## Legende

| Marke | Bedeutung |
|---|---|
| `[BELEGT]` | wörtlich aus der offiziellen Loxone-KB bzw. aus der bereits verifizierten Zuordnung in [bausteine.md](bausteine.md). Quell-URL steht unter jeder Tabelle. |
| `[ABGELEITET]` | aus Konnektorzahl, Reihenfolge, Namensgleichheit und **`Def`-Standardwerten** geschlossen — **stand so nicht in der Doku** |
| `[OFFEN]` | unbekannt. Nicht geraten. |
| `[COMMUNITY]` | LoxWiki / Loxforum — nicht offiziell |

**Richtung:** `E` = Eingang · `A` = Ausgang · `P` = Parameter (in Config als Eingang gezeichnet,
aber in der Doku als Parameter tabelliert)

> ⚠️ **Bevor du eine `[ABGELEITET]`- oder `[OFFEN]`-Zeile in ein Kundenprojekt verdrahtest:**
> einmal in Loxone Config verdrahten, speichern, XML gegenlesen. Eine falsche Zuordnung
> erzeugt eine falsche Verdrahtung, die niemand sieht.

---

## 1. Logik- und Analogbausteine

### `And` → **Und**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `I1` | `I1` | Eingang 1 | E | [BELEGT] |
| `I2` | `I2` | Eingang 2 | E | [BELEGT] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] — Doku nennt den Ausgang `O`, das XML `Q`; einziger Ausgang, daher eindeutig |

Quelle: https://www.loxone.com/dede/kb/und/

### `Or` → **Oder**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `I1` | `I1` | Eingang 1 | E | [BELEGT] |
| `I2` | `I2` | Eingang 2 | E | [BELEGT] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] — wie bei `And` |

Quelle: https://www.loxone.com/dede/kb/oder/

### `Memory` → **Merker**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Input` | `I` | Eingang | E | [ABGELEITET] — einziger Eingang, Name deckungsgleich |
| `AQ` | – | Analogausgang | A | [OFFEN] — die KB-Seite führt **überhaupt keine Ausgänge** auf ("wahrscheinlich O") |
| `Q` | – | Digitalausgang | A | [OFFEN] — dito; welcher der beiden XML-Ausgänge dem undokumentierten `O` entspricht, ist nicht entscheidbar |

Quelle: https://www.loxone.com/dede/kb/merker/

### `RSFlipFlop` → **RS-Impulsschalter**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputS` | `S` | Set — Impuls schaltet `O` ein | E | [ABGELEITET] |
| `InputTrigger` | `Tg` | Toggle — Impuls schaltet `O` um | E | [ABGELEITET] |
| `InputR` | `R` | Reset — dominierender Eingang | E | [ABGELEITET] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-rs/

> ⚠️ **RS und SR haben identische Konnektorsätze.** `RS-Impulsschalter` (Reset dominiert) und
> `SR-Impulsschalter` (Set dominiert) unterscheiden sich in der Doku nur im Verhalten, nicht in
> den Kürzeln. Einziges Unterscheidungsmerkmal ist der XML-Typname `RSFlipFlop`.
> Für den SR-Baustein liegt **keine** Vorlage vor — Typname unbekannt, **nicht raten**.
> (SR-Doku: https://www.loxone.com/dede/kb/impulsschalter-sr/)

### `EdgeDetection` → **Flankenerkennung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Input` | `I` | Eingang, dessen Flanken erkannt werden | E | [ABGELEITET] |
| `PulseTime` (`Def="300"`) | `Pd` | Impulsdauer (Doku-Default 1 s) | P | [ABGELEITET] |
| `Edge` | `P` | Impuls bei jeder Flanke | A | [ABGELEITET] |
| `RisingEdge` | `On` | Impuls bei steigender Flanke | A | [ABGELEITET] |
| `FallingEdge` | `Off` | Impuls bei fallender Flanke | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/flankenerkennung/

Konnektorzahl 5 = Doku-Zahl 5, Reihenfolge identisch, Bedeutungen eindeutig.

### `AnalogThresholdTrigger` → **Schwellwertschalter**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Input` | `V` | Wert | E | [ABGELEITET] |
| `On` (`Def="5"`) | `Von` | Wert, bei dem `O` **ein**schaltet | P | [ABGELEITET] — Default 5 = Doku-Default 5 |
| `Off` (`Def="1"`) | `Voff` | Wert, bei dem `O` **aus**schaltet | P | [ABGELEITET] — Default 1 = Doku-Default 1 |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `PulseTime` (`Def="1"`) | `Pd` | Impulsdauer | P | [ABGELEITET] — Default 1 = Doku-Default 1 |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |
| `RisingEdge` | `On` | Impuls bei steigender Flanke | A | [ABGELEITET] |
| `FallingEdge` | `Off` | Impuls bei fallender Flanke | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/schwellwert-schalter/

> ⚠️ **Namenskollision, echte Fehlerquelle:** Die XML-Konnektoren `On`/`Off` sind die
> **Schwellwert-Parameter** (`Von`/`Voff`), die Doku-Kürzel `On`/`Off` sind dagegen die
> **Flankenimpuls-Ausgänge** (im XML `RisingEdge`/`FallingEdge`). Wer `On` aus der Doku sucht
> und `Co K="On"` verdrahtet, hängt am Schwellwert statt am Impulsausgang.
> (Siehe auch bausteine.md: `On`/`Off` sind Konnektoren, keine reinen Parameter — gleitende
> Schwellen sind damit möglich.)

### `Formula` → **Formel**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Input1` | `I1` | Wert 1 (in der Formel als `I1`) | P/E | [BELEGT] |
| `Input2` | `I2` | Wert 2 | P/E | [BELEGT] |
| `Input3` | `I3` | Wert 3 | P/E | [BELEGT] |
| `Input4` | `I4` | Wert 4 | P/E | [BELEGT] |
| `AQ` | `R` | Result — Ergebnis | A | [ABGELEITET] |
| `TQ` | `E` | Error — z. B. bei verbotener Rechenoperation | A | [OFFEN] |

Quelle: https://www.loxone.com/dede/kb/formel/

`TQ` ist [OFFEN], weil bausteine.md `TQ` als **Textausgang** beschreibt, die KB den zweiten
Ausgang aber als `E` (Error) führt. Beides kann zutreffen (Fehlertext), verifiziert ist es nicht.
Der Formelausdruck steht im Attribut `Formula`, dazu `Valid="true|false"`.

---

## 2. Zeit- und Impulsbausteine

### `OnDelay` → **Einschaltverzögerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` (`Inv="true"`) | `Tr` | Trigger | E | [ABGELEITET] |
| `Reset` | (`Off`) | Off / Lock — dominierender Eingang | E | [OFFEN] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `Time` (`Def="60"`) | `Don` | Verzögerungsdauer (Doku-Default 1 s) | P | [ABGELEITET] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung/

**Zahlen stimmen nicht überein:** XML 5 Konnektoren, Doku 4 (1 Eingang + 1 Ausgang + 2 Parameter).
Die KB-Tabelle listet nur `Tr`, beschreibt dort aber wörtlich den *Off/Lock*-Text
("Pulse > 200 ms: Block is locked. Dominating input.") — das ist ein Datenfehler der KB-Seite:
die `Off`-Zeile fehlt. `Reset` bleibt deshalb [OFFEN] (starker Kandidat: `Off`).

### `OffDelay` → **Ausschaltverzögerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Tr` | Trigger | E | [ABGELEITET] |
| `Reset` | (`Off`) | Off / Lock — dominierender Eingang | E | [OFFEN] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `Time` (`Def="7200"`) | `Don` | Verzögerung bis Ausschalten (Doku-Default 1 s) | P | [ABGELEITET] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/ausschalt-verzoegerung/

Gleiche Lücke wie bei `OnDelay`: KB listet nur einen Eingang, XML hat zwei.

### `PulseAt` → **Impuls um**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputDisable` | `Off` | Off / Lock — dominierender Eingang | E | [ABGELEITET] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `Time` (`Def="1"`) | `Don` | Ein-Dauer von Ausgang `O` | P | [ABGELEITET] — Default 1 = Doku-Default 1 |
| `Q` | `O` | Ausgang zum festgelegten Zeitpunkt | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

**Abgrenzung:** Nicht „Impuls **bei**" (Textmustersuche, https://www.loxone.com/dede/kb/impuls-bei/) —
der hat `T`/`P`/`Pd` = 3 Konnektoren und keinen API-Ausgang. `PulseAt` hat 5 und passt exakt auf
„Impuls **um**" (1 E + 2 P + 2 A). Der englische Typname ist hier irreführend.

### `StairwayLS` → **Treppenlicht-Schalter**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Tr` | Schaltet `O` für die Dauer `Don` ein | E | [BELEGT] (bausteine.md: `InputTrigger` → `Q`) |
| `On` | `On` | Schaltet `O` ein | E | [ABGELEITET] — Namensgleichheit |
| `Reset` | `Off` | Off / Lock — dominierender Eingang | E | [ABGELEITET] |
| `InputDisable` | `DisPc` | Deaktiviert alle Eingänge (Kindersicherung) | E | [ABGELEITET] |
| `TimeHigh` (`Def="300"`) | `Don` | Ein-Dauer von `O` (Doku-Default 180 s) | P | [ABGELEITET] |
| `TimeWarn` | (`Tw`) | Vorwarnzeit vor Ausschalten | P | [OFFEN] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `WarnTime` | (`Dw`) | Dauer der Ausschaltvorwarnung | P | [OFFEN] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/treppenlicht-schalter/

`TimeWarn` und `WarnTime` sind **Fast-Anagramme** und beide unbelegt (`Def` fehlt ⇒ 0).
Die Reihenfolge legt `TimeWarn`=`Tw` (Vorwarnzeit) und `WarnTime`=`Dw` (Vorwarn-Dauer) nahe —
das ist aber nicht beweisbar, und eine Verwechslung dreht Vorwarnzeit und Vorwarn-Dauer
gegeneinander. Deshalb [OFFEN]. Konnektorzahl passt (10 = 4 E + 2 A + 4 P).

### `DayTimer` → **Schaltuhr**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Act` | Activate — aktiviert Einträge mit „Aktivierung notwendig" | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierender Eingang | E | [ABGELEITET] |
| `RtD` | `Rtd` | Reset to default | E | [ABGELEITET] — Namensgleichheit |
| `PulseTime` | `Don` | Ein-Dauer von `O` bei „Aktivierung notwendig" | P | [ABGELEITET] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `Manual` | `Am` | Automatic mode (0 = automatisch, 1 = manuell über `Mm`) | P | [ABGELEITET] |
| `Mode` | `Mm` | Manual mode — Betriebsmodus manuell setzen | P | [ABGELEITET] |
| `AQ` | `O` | Ausgang (digital 0/1 oder analog) | A | [ABGELEITET] |
| `Qon` | `On` | Impuls bei Ein | A | [ABGELEITET] |
| `Qoff` | `Off` | Impuls bei Aus | A | [ABGELEITET] |
| `AQm` | `Om` | Nummer des aktiven Betriebsmodus | A | [ABGELEITET] |
| `AQmt` | `Rt` | Verbleibende Zeit eines gestarteten Timers | A | [OFFEN] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

Konnektorzahl 13 = Doku 13 (3 E + 6 A + 4 P). `AQmt` ist nur durch **Ausschluss** auf `Rt`
gefallen (alle anderen sind vergeben) — der Name legt eher „mode time" als „remaining time"
nahe, deshalb [OFFEN].

> ℹ️ Die Zuordnung `DayTimer` = Schaltuhr wird zusätzlich dadurch gestützt, dass der
> Miniserver in `LoxAPP3.json` denselben Steuerungstyp `Daytimer` für die Schaltuhr führt.
> [COMMUNITY] https://www.loxwiki.eu/ (Loxone-Web-API-Struktur) — nicht Teil der KB.

---

## 3. Bedienung

### `PushButton` → **Schalter** (nicht „Taster"!)

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Tg` | Toggle — schaltet `O` ein/aus | E | [ABGELEITET] |
| `On` | `On` | Schaltet `O` ein | E | [ABGELEITET] — Namensgleichheit |
| `Reset` | `Off` | Off / Lock — dominierender Eingang | E | [ABGELEITET] |
| `InputDisable` | `DisPc` | Deaktiviert alle Eingänge | E | [ABGELEITET] |
| `Remanence` (`Inv="true"`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `Q` | `O` | Ausgang | A | [ABGELEITET] |
| `Qon` | `On` | Impuls, wenn `O` eingeschaltet wird | A | [ABGELEITET] |
| `Qoff` | `Off` | Impuls, wenn `O` ausgeschaltet wird | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/schalter/

> ⚠️ **Der Typname lügt.** `PushButton` klingt nach „Taster", aber der **Taster**
> (https://www.loxone.com/dede/kb/taster/) hat nur 7 Konnektoren (`Tr`, `Off`, `DisPc`, `O`,
> `API`, `Rem`, `Don`) und einen Zeit-Parameter `Don`. Der **Tastschalter**
> (https://www.loxone.com/dede/kb/tastschalter/) hat zwar 9, aber **kein** `Rem` und dafür `Don`.
> `PushButton` hat 9 Konnektoren mit `Remanence` und **ohne** Zeitparameter — das ist
> eindeutig der bistabile **Schalter**.

---

## 4. Beleuchtung

### `LightController2` → **Lichtsteuerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `I1` … `I8` | `Lc1-8` | Lichtkreis 1–8 (Langklick = Dimmen) | E | [ABGELEITET] |
| `InputTriggerUp` | `M+` | Nächste Stimmung | E | [ABGELEITET] |
| `InputTriggerDown` | `M-` | Vorherige Stimmung | E | [ABGELEITET] |
| `Select` | `Mood` | Stimmung per ID auswählen (0…99) | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierender Eingang | E | [ABGELEITET] |
| `Sel1` … `Sel8` | `T5/1-8` | T5-Steuerung 1–8 | E | [ABGELEITET] |
| `EnMove` | `DisP` | Deaktiviert `P` und `Mo` | E | [ABGELEITET] ⚠️ Semantik invertiert |
| `Move` | `Mo` | Motion / Bewegung | E | [BELEGT] |
| `On` | `On` | All on (Stimmung ID 99) | E | [ABGELEITET] |
| `Alarm` | `Alarm` | Alarm — Ausgänge blinken | E | [ABGELEITET] |
| `AlarmClock` | `Buzzer` | Weckerstimmung (ID 98) | E | [ABGELEITET] |
| `Brightness` | `Br` | Aktuelle Helligkeit (lux) | E | [BELEGT] |
| `InputDisable` | `DisPc` | Deaktiviert Peripherie-Eingänge | E | [ABGELEITET] |
| `Presence` | `P` | Präsenz | E | [BELEGT] |
| `RtD` | `Rtd` | Reset to default | E | [ABGELEITET] |
| `MasterBr` | `MBr` | Master Brightness | E | [ABGELEITET] |
| `BrightnessLimit` (`30`) | `Brt` | Helligkeitsschwelle (lux) | P | [ABGELEITET] · Default 30 = 30 |
| `Remanence` (`Inv`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `MoveOn` (`900`) | `Moet` | Motion extend time | P | [ABGELEITET] · 900 = 900 |
| `MoveIgnore` (`300`) | `Pto` | Presence automatic timeout | P | [ABGELEITET] · 300 = 300 |
| `Step` (`2`) | `Sts` | Schrittweite Helligkeit (%) | P | [ABGELEITET] · 2 = 2 |
| `Steptime` (`0.2`) | `Str` | Schrittrate Helligkeit (s) | P | [ABGELEITET] · 0,2 = 0,2 |
| `Min` | `MinBr` | Minimale Helligkeit (%) | P | [ABGELEITET] · 0 = 0 |
| `Max` (`100`) | `MaxBr` | Maximale Helligkeit (%) | P | [ABGELEITET] · 100 = 100 |
| `Wrap` | `Dm` | Dim mode | P | [ABGELEITET] · 0 = 0 |
| `NoLast` | `Lv` | Last value output Lc1-4 | P | [ABGELEITET] ⚠️ Semantik invertiert |
| `MoveScene` | `Pm` | Presence mood (Stimmungs-ID) | P | [ABGELEITET] · 0 = 0 |
| `MaxP` (`0.35`) | `Tdc` | Time double-click | P | [ABGELEITET] · 0,35 = 0,35 |
| `MoveTimeout` (`3600`) | `Met` | Manual operation extend time | P | [ABGELEITET] · 3600 = 3600 |
| `RGBalt` | `Ao` | Alternative operation Lc1-4 | P | [ABGELEITET] · 0 = 0 |
| `SceneMixTime` (`1`) | `Mmd` | Mixing moods duration | P | [ABGELEITET] · 1 = 1 |
| `FadingTime` (`1`) | `Ft` | Fading time | P | [ABGELEITET] · 1 = 1 |
| `AlarmClockPeriod` (`3`) | `Fbu` | Fading time buzzer (min) | P | [ABGELEITET] · 3 = 3 |
| `DayMinTemp` (`2700`) | `MinCt` | Minimale Farbtemperatur (K) | P | [ABGELEITET] · 2700 = 2700 |
| `DayMaxTemp` (`6500`) | `MaxCt` | Maximale Farbtemperatur (K) | P | [ABGELEITET] · 6500 = 6500 |
| `AlarmPeriod` (`4`) | `Afi` | Alarm flashing interval (s) | P | [ABGELEITET] · 4 = 4 |
| `AlarmBrightness` (`50`) | `MaxAbr` | Maximum alarm brightness (%) | P | [ABGELEITET] · 50 = 50 |
| `AQ1` … `AQ18` | `Lc1-18` | Lichtkreis-Ausgang 1–18 | A | [ABGELEITET] |
| `AQ19`, `AQ20` | – | – | A | [OFFEN] — die KB kennt nur `Lc1-18`, das XML hat 20 |
| `Scene` | `M` | Current mood (ID; 0 Aus, 98 Buzzer, 99 alles an, -1/-3) | A | [ABGELEITET] |
| `OutputReset` | `2C` | Impuls bei Doppel-/Dreifachklick oder `Off` | A | [ABGELEITET] |
| `OutputResetAll` | `3C` | Impuls bei Dreifachklick | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/lichtsteuerung/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

**Warum das trotz „[ABGELEITET]" belastbar ist:** alle 21 Parameter stimmen im
`Def`-Standardwert **exakt** mit den KB-Defaults überein (30/900/300/2/0,2/100/0,35/3600/1/1/3/2700/6500/4/50).
Eingangszahl 30 = Doku 30, Parameterzahl 21 = Doku 21. Nur die Ausgänge weichen ab (20 statt 18 `Lc`).

⚠️ `EnMove` ↔ `DisP` und `NoLast` ↔ `Lv`: XML-Name und Doku-Kürzel bezeichnen dieselbe
Funktion mit **umgekehrtem Vorzeichen**. Wert 1 heißt bei `DisP` „Präsenz aus".

### `CentralLight` → **Licht Zentral**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `I1` … `I4` | – | – | E | [OFFEN] — die KB-Seite „Licht Zentral" führt **keine** `Lc`-Eingänge; Analogie zur Lichtsteuerung (`Lc1-4`) ist plausibel, aber unbelegt |
| `InputTriggerUp` | `M+` | Nächste Stimmung | E | [ABGELEITET] |
| `InputTriggerDown` | `M-` | Vorherige Stimmung | E | [ABGELEITET] |
| `Select` | `Mood` | Stimmung per ID | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock | E | [ABGELEITET] |
| `Sel1` … `Sel8` | `T5/1-8` | T5-Steuerung 1–8 | E | [ABGELEITET] |
| `EnMove` | `DisP` | Deaktiviert `P`/`Mo` der Mitglieder | E | [ABGELEITET] ⚠️ invertiert |
| `On` | `On` | All on | E | [ABGELEITET] |
| `Alarm` | `Alarm` | Alarm | E | [ABGELEITET] |
| `AlarmClock` | `Buzzer` | Weckerstimmung | E | [ABGELEITET] |
| `InputDisable` | `DisPc` | Peripherie sperren | E | [ABGELEITET] |
| `RtD` | `Rtd` | Reset to default | E | [ABGELEITET] |
| `OutActive` | `Na` | Anzahl der aktiven Leuchten | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/licht-zentral/

Mitglieder stehen im Attribut **`rec`** (Doppelklick in Config), nicht als Verdrahtung.
Konnektorzahl 24 = 18 dokumentierte Eingänge + 2 Ausgänge + 4 undokumentierte `I1`–`I4`.
**Merke:** Zentralbefehle umgehen den `DisPc` der Mitglieder.

---

## 5. Beschattung und Fenster

### `AutoJalousie` → **Automatikbeschattung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Tg` | Toggle (Öffnen/Stopp/Schließen) | E | [BELEGT] |
| `InputTriggerUp` | `Po` | Partial open (Drücken & Halten) | E | [ABGELEITET] |
| `InputTriggerDown` | `Pc` | Partial close (Drücken & Halten) | E | [ABGELEITET] |
| `EndUp` | `Co` | Complete open | E | [BELEGT] |
| `EndDown` | `Cc` | Complete close | E | [BELEGT] |
| `Shade` | `So` | Slightly open | E | [ABGELEITET] |
| `AutoShade` | `Sps` | Sonnenstandsautomatik Start | E | [BELEGT] |
| `EnAutoShade` | `DisSp` | Sonnenstandsautomatik deaktivieren | E | [BELEGT] ⚠️ invertierter Name |
| `ReactAutoShade` | `Spr` | Sonnenstandsautomatik Neustart | E | [BELEGT] |
| `Safety` | `Wa` | **Windalarm** | E | [BELEGT] |
| `Window` | `Dwc` | **Tür-/Fensterkontakt** (0 zu, 1 offen) | E | [BELEGT] |
| `Stop` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `ManualPosition` | `Pos` | Position der Beschattung (%) | E | [ABGELEITET] |
| `ManualLamelle` | `Slat` | Lamellenposition (%) | E | [ABGELEITET] |
| `Gesture` | `T5` | T5-Steuerung (Taste 1 auf, Taste 4 zu) | E | [ABGELEITET] |
| `InputDisable` | `DisPc` | Deaktiviert `Tg, Po, Pc, Co, Cc, So, T5` | E | [ABGELEITET] |
| `Type` (`Def="6"`) | `Type` | Beschattungstyp 0…6 (hier 6 = Markise) | P | [ABGELEITET] |
| `Dir` (`270`) | `Dir` | Himmelsrichtung (0 N, 90 O, 180 S, 270 W, -1 aus) | P | [BELEGT] |
| `TimeEnd` (`75`) | `Opd` | Dauer Öffnen (s) | P | [ABGELEITET] · 75 = 75 |
| `TimeEndDown` (`70`) | `Cld` | Dauer Schließen (s) | P | [ABGELEITET] · 70 = 70 |
| `SO` | – | – | P | [OFFEN] — kein Gegenstück auf der KB-Seite (Kandidat: `Sop` „Slightly open position" aus der *integrierten* Variante) |
| `WP` | `Wap` | Windalarm-Position (0 offen, 1 zu) | P | [ABGELEITET] · 0 = 0 |
| `AutoShadeEnd` (`1`) | `Spe` | Aktion bei Automatik-Ende (0…3) | P | [ABGELEITET] · 1 = 1 |
| `AutMode` (`1`) | `Spm` | Automatikmodus (Helligkeit/Kühlung) | P | [ABGELEITET] · 1 = 1 |
| `MinPulse` (`3`) | `Tlc` | Langklickdauer an `Po`/`Pc` (s) | P | [ABGELEITET] · 3 = 3 |
| `DblClk` (`0.3`) | `Tdc` | Doppelklickdauer (s) | P | [ABGELEITET] · 0,3 = 0,3 |
| `DirTol` (`85`) | `Dts` | Richtungstoleranz Sonneneintritt (°) | P | [ABGELEITET] · 85 = 85 |
| `DirTol2` (`85`) | `Dte` | Richtungstoleranz Sonnenaustritt (°) | P | [ABGELEITET] · 85 = 85 |
| `AutoShadeTime` (`120`) | `Spi` | Nachstellintervall Lamellen (min) | P | [ABGELEITET] · 120 = 120 |
| `SRoff` (`30`) | `Spos` | Startversatz zum Sonnenaufgang (min) | P | [ABGELEITET] · 30 = 30 |
| `SSoff` (`-30`) | `Spoe` | Endversatz zum Sonnenuntergang (min) | P | [ABGELEITET] · -30 = -30 |
| `Width` (`70`) | `Sw` | Lamellenbreite (mm) | P | [ABGELEITET] · 70 = 70 |
| `Space` (`60`) | `Sd` | Lamellenabstand (mm) | P | [ABGELEITET] · 60 = 60 |
| `Rdd` | `Rdd` | Reference Drive Down | P | [ABGELEITET] · Namensgleichheit, 0 = 0 |
| `TimeBlock` (`0.5`) | `Mld` | Motorverriegelung bei Richtungswechsel (s) | P | [ABGELEITET] · 0,5 = 0,5 |
| `TurnOffset` (`0.15`) | `Bldo` | Totzeit bei Bewegung in **Gegen**richtung (s) | P | [ABGELEITET] · 0,15 = 0,15 |
| `Deadtime` | `Bld` | Totzeit bei Bewegung in **gleiche** Richtung (s) | P | [ABGELEITET] · 0 = 0 |
| `MinMove` (`0.4`) | `minTd` | Mindestfahrzeit bei Impuls (s) | P | [ABGELEITET] · 0,4 = 0,4 |
| `Back` (`0.8`) | `Rd` | Rücklaufzeit bis Lamellen horizontal (s) | P | [ABGELEITET] · 0,8 = 0,8 |
| `OutputUp` | `Op` | Open | A | [BELEGT] |
| `OutputDown` | `Cl` | Close | A | [BELEGT] |
| `OutputPos` | `Pos` | Position der Beschattung (0,0 offen … 1,0 zu) | A | [ABGELEITET] |
| `OutputLPos` | `Slat` | Lamellenposition (0,0 waagrecht … 1,0 senkrecht) | A | [ABGELEITET] |
| `OutputAutoShade` | `Sp` | Sonnenstandsautomatik aktiv | A | [ABGELEITET] |
| `OutputSafety` | `Wds` | Wind- bzw. Fenster-/Türkontakt-Zustand | A | [ABGELEITET] |
| `OutputLock` | `Off` | Aktiv, wenn Eingang `Off` = 1 | A | [ABGELEITET] |
| `OutputCombined` | `AQpp` | Befehlsausgang (Befehl·10⁶ + Pos·10³ + Lamelle) | A | [ABGELEITET] |
| `TargetPos` | `TPos` | Zielposition (z. B. Hunter Douglas) | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/automatikjalousie/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

**Belastbarkeit:** 16 Eingänge = 16 Doku-Eingänge in **identischer Reihenfolge**;
10 Ausgänge = 10 Doku-Ausgänge in identischer Reihenfolge; 23 XML-Parameter gegen 22 Doku-Parameter,
davon **20 über exakt gleiche `Def`-Standardwerte** verankert. Übrig bleibt genau `SO` → [OFFEN].
Die Eingangsreihenfolge wird zusätzlich durch `CentralShade` bestätigt (identische Kette ohne `Window`).

> ⚠️ **`Safety` ist NICHT der Sicherheitskontakt einer Tür**, sondern der **Windalarm** (`Wa`).
> **`Window` ist der Fensterkontakt** (`Dwc`) und fährt die Beschattung *auf* und sperrt.
> Wer die beiden vertauscht, baut eine Anlage, die bei Sturm auffährt.

### `CentralShade` → **Automatikbeschattung Zentral**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputTrigger` | `Tg` | Toggle | E | [ABGELEITET] |
| `InputTriggerUp` | `Po` | Partial open | E | [ABGELEITET] |
| `InputTriggerDown` | `Pc` | Partial close | E | [ABGELEITET] |
| `EndUp` | `Co` | Complete open (Stoppen nicht möglich) | E | [ABGELEITET] |
| `EndDown` | `Cc` | Complete close (Stoppen nicht möglich) | E | [ABGELEITET] |
| `Shade` | `So` | Slightly open | E | [ABGELEITET] |
| `AutoShade` | `Sps` | Sonnenstandsautomatik Start | E | [ABGELEITET] |
| `EnAutoShade` | `DisSp` | Sonnenstandsautomatik deaktivieren | E | [ABGELEITET] ⚠️ invertiert |
| `ReactAutoShade` | `Spr` | Sonnenstandsautomatik Neustart | E | [ABGELEITET] |
| `Safety` | `Wa` | Windalarm | E | [ABGELEITET] |
| `Stop` | `Off` | Off / Lock | E | [ABGELEITET] |
| `ManualPosition` | `Pos` | Position (%) | E | [ABGELEITET] |
| `ManualLamelle` | `Slat` | Lamellenposition (%) | E | [ABGELEITET] |
| `Gesture` | `T5` | T5-Steuerung | E | [ABGELEITET] |
| `InputDisable` | `DisPc` | Peripherie sperren | E | [ABGELEITET] |
| `OutOpen` | `No` | Anzahl der geöffneten Beschattungen | A | [ABGELEITET] |
| `OutClose` | `Nc` | Anzahl der geschlossenen Beschattungen | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/beschattung-zentral/

18 = 15 Doku-Eingänge + 3 Doku-Ausgänge, Reihenfolge identisch. Der Zentralbaustein hat
**kein `Window`/`Dwc`** — genau die Differenz zur `AutoJalousie`. Mitglieder im Attribut `rec`.

### `WindowsMonitor` → **Fenster- und Türüberwachung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Wh` | `Hpos` | Griffposition (1 zu, 2 gekippt, 3 offen, 4/5 gesichert, 0 offline) | E | [ABGELEITET] |
| `W` (`Inv="true"`) | `Dwco` | Kontakt „offen" (0 zu, 1 offen) | E | [ABGELEITET] — KB: „wird normalerweise invertiert verwendet", XML hat `Inv="true"` |
| `Wt` (`Inv="true"`) | `Dwct` | Kontakt „gekippt" | E | [ABGELEITET] — dito |
| `Wl` | `Dwcs` | Kontakt „gesichert/verriegelt" | E | [ABGELEITET] |
| `HI1` | – | – | E | [OFFEN] |
| `HI2` | – | – | E | [OFFEN] — in bausteine.md als vorhanden vermerkt, ohne Bedeutung |
| `HI3` | – | – | E | [OFFEN] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `AQo` | `Open` | Anzahl offene Fenster/Türen | A | [ABGELEITET] |
| `AQt` | `Tilt` | Anzahl gekippte | A | [ABGELEITET] |
| `AQc` | `Closed` | Anzahl geschlossene | A | [ABGELEITET] |
| `AQof` | `Offline` | Anzahl Sensoren offline | A | [ABGELEITET] |
| `AQl` | `Secured` | Anzahl verriegelte | A | [ABGELEITET] |
| `AQu` | `Unlocked` | Anzahl nicht verriegelte | A | [ABGELEITET] |
| `TQ` | `Txlt` | Name des zuletzt ausgelösten Sensors | A | [ABGELEITET] |
| `TQo` | `Txu` | Namen der offenen/gekippten/unversperrten | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

14 der 17 Konnektoren decken die Doku vollständig ab (4 E + 9 A + 1 P), Reihenfolge identisch.
Die drei `HI*` sind undokumentiert. Zugeordnete Geräte stehen im Attribut **`Objects`**.

---

## 6. Klima und Heizung

### `HeatIRoomController2` → **Intelligente Raumregelung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `AMode` | `Mode` | Betriebsart -1…5 | E | [ABGELEITET] |
| `Input` | `ϑt` | Zieltemperatur (Modus „fixer Sollwert") | E | [ABGELEITET] |
| `Temp` | `ϑc` | Aktuelle Raumtemperatur | E | [BELEGT] |
| `Window` | `Dwc` | Tür-/Fensterkontakt | E | [BELEGT] |
| `Comfort` | `C` | Startet Komfort (steigende Flanke) | E | [ABGELEITET] |
| `Save` | `E` | Startet Eco | E | [ABGELEITET] |
| `Save2` | `Bp` | Startet Gebäudeschutz | E | [ABGELEITET] |
| `Move` | `P` | Präsenz (verlängert Komfort) | E | [BELEGT] |
| `Reset` | `Off` | Off / Lock | E | [BELEGT] |
| `DisMv` | `DisP` | Deaktiviert Eingang `P` | E | [ABGELEITET] |
| `RtD` | `Rtd` | Reset to default | E | [ABGELEITET] |
| `TempO` | `ϑo` | Außentemperatur | E | [BELEGT] |
| `InCo2` | `CO2` | CO₂-Gehalt (ppm) | E | [ABGELEITET] |
| `InHumid` | `H` | Relative Luftfeuchtigkeit (%) | E | [ABGELEITET] |
| `inFan` (`2`) | `Fan` | Lüfterstufe 0–7 | E | [ABGELEITET] |
| `inAirDir` (`1`) | `ADir` | Luftrichtung 1–8 | E | [ABGELEITET] |
| `TComfort` (`22.5`) | `ϑch` | Komforttemperatur Heizen | P | [ABGELEITET] · 22,5 = 22,5 |
| `TComfortC` (`24.5`) | `ϑcc` | Komforttemperatur Kühlen | P | [ABGELEITET] · 24,5 = 24,5 |
| `TComfortHC` (`22`) | `ϑchc` | Komforttemperatur Heizen+Kühlen | P | [ABGELEITET] · 22 = 22 |
| `TDiff` (`1.5`) | `ϑd` | Erlaubte Abweichung Komfort | P | [ABGELEITET] · 1,5 = 1,5 |
| `TShadeHeat` (`27.5`) | `ϑsh` | Beschattungsanforderung Heizbetrieb | P | [ABGELEITET] · 27,5 = 27,5 |
| `TShadeCool` (`23.5`) | `ϑsc` | Beschattungsanforderung Kühlbetrieb | P | [ABGELEITET] · 23,5 = 23,5 |
| `TSaveL` (`3`) | `ϑeh` | Eco Heizen (relativ zu `ϑch`) | P | [ABGELEITET] · 3 = 3 |
| `TSaveU` (`3`) | `ϑec` | Eco Kühlen (relativ zu `ϑcc`) | P | [ABGELEITET] · 3 = 3 |
| `TSave` (`2`) | `ϑe` | Eco Heizen+Kühlen | P | [ABGELEITET] · 2 = 2 |
| `TDeepSleep` (`5`) | `ϑfp` | Frostschutztemperatur | P | [ABGELEITET] · 5 = 5 |
| `TMax` (`28`) | `ϑhp` | Hitzeschutztemperatur | P | [ABGELEITET] · 28 = 28 |
| `TimeMove` (`14`) | `Vs` | Max. Ventilstillstand (Tage) | P | [ABGELEITET] · 14 = 14 |
| `TimeC` (`3600`) | `Cet` | Komfort-Verlängerung nach `C` (s) | P | [ABGELEITET] · 3600 = 3600 |
| `TimeS` (`3600`) | `EBpet` | Eco-/Gebäudeschutz-Verlängerung (s) | P | [ABGELEITET] · 3600 = 3600 |
| `TimeMv` (`1800`) | `Pet` | Komfort-Verlängerung nach `P` (s) | P | [ABGELEITET] · 1800 = 1800 |
| `THCelvin` (`120`) | `Hs` | Aufheizgeschwindigkeit (min/°C) | P | [ABGELEITET] · 120 = 120 |
| `TCCelvin` (`60`) | `Cs` | Abkühlgeschwindigkeit (min/°C) | P | [ABGELEITET] · 60 = 60 |
| `TPWM` | `Pwm` | PWM-Intervall (min; 0 = automatisch) | P | [ABGELEITET] · 0 = 0 |
| `TWin` (`300`) | `Ddwc` | Verzögerung Gebäudeschutz nach Fensteröffnung (s) | P | [ABGELEITET] · 300 = 300 |
| `TExcess` (`1`) | `ϑExc` | Sollwertversatz bei Heiz-/Kühlüberschuss | P | [ABGELEITET] · 1 = 1 |
| `AQh` | `H` | Heizen | A | [BELEGT] |
| `AQc` | `C` | Kühlen | A | [BELEGT] |
| `AQhc` | `HC` | Heizen/Kühlen kombiniert | A | [BELEGT] |
| `AQh1` / `AQc1` / `AQhc1` | `H1` / `C1` / `HC1` | Quelle 1 | A | [BELEGT] (`AQhc1`=`HC1`) |
| `AQh2` / `AQc2` / `AQhc2` | `H2` / `C2` / `HC2` | Quelle 2 | A | [ABGELEITET] |
| `AQh3` / `AQc3` / `AQhc3` | `H3` / `C3` / `HC3` | Quelle 3 | A | [ABGELEITET] |
| `Qs` | `Shd` | Beschattungsanforderung | A | [BELEGT] |
| `AQs` | `HCm` | Heiz-/Kühlmodus ("Heating / Cooling mode") | A | [BELEGT-TECHDOC] — vorher [OFFEN] |
| `Qe` | `Error` | Fehler vorhanden | A | [ABGELEITET] |
| `Qa` | – | – | A | [OFFEN] — Kandidat `TxErr`, aber `TxErr` ist ein **Text**ausgang, `Qa` sieht digital aus |
| `AQt` | `ϑt` | Zieltemperatur | A | [BELEGT] |
| `AQhm` | `Om` | Aktueller Betriebsmodus ("Current operating mode") | A | [BELEGT-TECHDOC] ⚠️ **vorher `HCm`** |
| `AQtm` | `Os` | Aktueller Temperaturmodus (-1…4) | A | [ABGELEITET] |
| `Qb` | `Boost` | Boost aktiv | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/intelligente-raumregelung/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

**Belastbarkeit:** 16 Eingänge = 16 Doku-Eingänge (Reihenfolge bis auf `RtD` identisch — `RtD`
steht im XML an Position 11, in der Doku als `Rtd` an Position 16; Namensgleichheit macht das
eindeutig). Alle **20 Parameter über identische `Def`-Standardwerte** verankert.
Bei den 21 Ausgängen bricht die Reihenfolgeannahme im Bereich Position 14–20:
`Qb`↔`Boost` und `AQtm`↔`Os` passen dem Namen nach, der Position nach aber nicht.
Deshalb bleiben `AQs` und `Qa` [OFFEN] — und damit auch die Doku-Ausgänge **`Om`** und
**`TxErr`** ohne gesicherten XML-Partner.

Zusatzattribute: **`Objects`** (Quelle/HVAC-Zuordnung) · **`UUIDTimer`** (integrierte Schaltuhr).

### `HVACController` → **Heiz- und Kühlsteuerung** (nicht „HVAC Controller"!)

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Temp` | `ϑo` | Außentemperatur | E | [ABGELEITET] |
| `TempAvg` | – | – | E | [OFFEN] |
| `Boost` | `B` | Boost — aktiviert Stufe 2 sofort | E | [ABGELEITET] |
| `Stop` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Error` | – | – | E | [OFFEN] |
| `SecHeat` | `Ah` | Additional heating — Zusatzheizung anfordern | E | [ABGELEITET] |
| `Fan` | `F` | Ventilator-Ausgang aktivieren | E | [ABGELEITET] |
| `FilterAck` | `Cfc` | Filterwechsel bestätigen | E | [ABGELEITET] |
| `CoolAvailable` | `Ec` | Excess cooling — günstige Kühlenergie vorhanden | E | [ABGELEITET] |
| `HeatAvailable` | `Eh` | Excess heating | E | [ABGELEITET] |
| `ManualHeat` | `Mh` | Manueller Heizbetrieb | E | [ABGELEITET] |
| `ServiceMode` | – | – | E | [OFFEN] |
| `Mode` (`-2`) | `Mode` | -1 aus, 0 automatisch, 1 nur Heizen, 2 nur Kühlen | P | [ABGELEITET] · -2 = -2 |
| `OnThreshold` (`30`) | `Sot` | Einschaltschwelle mittlere Ventilöffnung (%) | P | [BELEGT] |
| `Average` (`2`) | `Otm` | Outdoor Temperature Mode 0…3 | P | [ABGELEITET] · 2 = 2 |
| `TempLimitC` (`18`) | – | – | P | [OFFEN] ⚠️ siehe Warnung |
| `TempLimitH` (`15`) | – | – | P | [OFFEN] ⚠️ siehe Warnung |
| `TimePump` | `MinHr` | Mindestlaufzeit vor Moduswechsel (min) | P | [ABGELEITET] · 0 = 0 |
| `FanDelay` (`120`) | `Fod` | Ventilator-Nachlaufzeit (s) | P | [BELEGT] · 120 = 120 |
| `TimePulseOn` (`750`) | `Don` | Ein-Impuls-Dauer für `MaxTp` (s) | P | [BELEGT] · 750 = 750 |
| `TimePulseOff` (`300`) | `Doff` | Aus-Impuls-Dauer (s) | P | [BELEGT] · 300 = 300 |
| `PulseThreshold` | `MaxTp` | Max. Ventilöffnung für Taktung (%) | P | [ABGELEITET] · 0 = 0 |
| `TimeFilter` | `Dfc` | Tage bis Filterwechsel | P | [ABGELEITET] · 0 = 0 |
| `TimeAddional` (`60`) | `Tt2s` | Verzögerung bis Stufe 2 (min) | P | [ABGELEITET] · 60 = 60 · *(XML-Tippfehler „Addional")* |
| `TempAdditional` (`-6`) | `ϑminS2` | Außentemperatur, ab der Stufe 2 sofort startet | P | [ABGELEITET] · -6 = -6 |
| `TempMin` (`-22`) | `ϑminHP` | Min. Außentemperatur Wärmepumpenbetrieb | P | [ABGELEITET] · -22 = -22 |
| `ValveDelay` | `Vd` | Umschaltventil-Laufzeit (s) | P | [ABGELEITET] · 0 = 0 |
| `OutHeat1` | `H` | Heizen Stufe 1 | A | [ABGELEITET] |
| `OutHeat2` | `H2` | Heizen Stufe 2 | A | [ABGELEITET] |
| `OutCool1` | `C` | Kühlen Stufe 1 | A | [ABGELEITET] |
| `OutCool2` | `C2` | Kühlen Stufe 2 | A | [ABGELEITET] |
| `OutSecHeat` | `Ah` | Zusatzheizung | A | [ABGELEITET] |
| `OutValve` | `Sv` | Umschaltventil (0 Heizen, 1 Kühlen) | A | [ABGELEITET] |
| `OutFan` | `F` | Ventilator | A | [ABGELEITET] |
| `OutFilter` | `Fc` | Filterwechsel fällig | A | [ABGELEITET] |
| `OutAverageTemp` | `ϑoa` | Durchschnittliche Außentemperatur 48 h | A | [ABGELEITET] |
| `OutError` | – | – | A | [OFFEN] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/klima-controller/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

**Warum „Heiz- und Kühlsteuerung" und nicht „HVAC Controller"?** Der XML-Typ hat
`FilterAck`/`OutFilter`/`TimeFilter`, `SecHeat`/`OutSecHeat`, `OutValve`/`ValveDelay` und
`OutAverageTemp`. Genau diese Funktionen (`Cfc`, `Fc`, `Dfc`, `Ah`, `Sv`, `Vd`, `ϑoa`) gibt es
**nur** auf der Seite *klima-controller*. Die Seite *hvac-controller* (`W/W1`, `Y`, `O/B`, `G`,
`Hmd`, `Emh`) hat keine davon. Parameterzahl 15 = 15, davon 12 über `Def`-Werte verankert.

> ⚠️ **`TempLimitC` / `TempLimitH` sind [OFFEN] — bewusst.** Die `Def`-Werte sind 18 bzw. 15.
> Die KB vergibt 18 an **`ϑLimH`** („keine Heizung, wenn Außentemp > 18") und 15 an **`ϑLimC`**
> („keine Kühlung, wenn Außentemp < 15"). Die XML-Namen sind also gegenüber den Doku-Kürzeln
> **vertauscht** — entweder weil der XML-Name die *freigegebene Betriebsart* meint
> („ab 18 °C nur noch Cooling") oder weil eines von beidem schlicht falsch benannt ist.
> Die HVAC-Controller-Seite bestätigt dasselbe Zahlenpaar in derselben Richtung
> (`mioϑc` = 15, `maoϑh` = 18). Eine Vertauschung sperrt im Kundenprojekt die Heizung im
> Winter. **Nicht raten — in Config nachsehen.**

---

## 7. Lüftung

### `ToiletFan` → **WC-Lüftungssteuerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Trigger` | `Tg` | Toggle — Sitzung starten/beenden | E | [BELEGT] |
| `Move` | `P` | Presence — startet Sitzung | E | [BELEGT] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [BELEGT] |
| `Disable` | `DisPc` | Deaktiviert alle Eingänge | E | [BELEGT] |
| `AiringDelay` (`Def="30"`) | `Fsd` | Fan start delay (s) | P | [ABGELEITET] · 30 = 30 |
| `MaxAiringDuration` (`180`) | `FPet` | Fan / Movement extend time (s) | P | [ABGELEITET] · 180 = 180 |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `OutputActive` | `S` | Session status — ein solange Sitzung aktiv | A | [BELEGT] |
| `OutputFan` | `Fan` | Lüfteransteuerung | A | [BELEGT] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/wc-lueftungssteuerung/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

Vollständige 10-zu-10-Deckung (4 E + 3 A + 3 P), Reihenfolge identisch.
*Korrektur zu bausteine.md:* der `Def`-Wert von `AiringDelay` in der Vorlage ist **30 s**
(nicht 180 s) — deckungsgleich mit dem KB-Default von `Fsd`.

---

## 8. Sicherheit und Alarm

### `Alarm` → **Alarmanlage**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `I1` | `P` | Alarmeingang Präsenzerkennung | E | [ABGELEITET] |
| `I2` | `Gb` | Glasbruch | E | [ABGELEITET] |
| `I3` | `Wc` | Fensterkontakte | E | [ABGELEITET] |
| `I4` | `Dc` | Türkontakte | E | [ABGELEITET] |
| `I5` (`Inv="true"`) | `Ot` | Sonstige Melder | E | [ABGELEITET] |
| `ActiveOO` | `Tg` | Toggle scharf/unscharf, mit Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `ActiveOOP` | `Tgnp` | Toggle scharf/unscharf, ohne Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `Active` | `A` | Scharfschalten, mit Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `ActiveP` | `Anp` | Scharfschalten, ohne Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `ActiveDelay` | `Ad` | Verzögert scharfschalten, mit Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `ActiveDelayP` | `Adnp` | Verzögert scharfschalten, ohne Präsenzerkennung | E | [BELEGT-TECHDOC] — vorher [OFFEN], Reihenfolge-Vermutung bestätigt |
| `Inactive` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Confirm` | `Ca` | Confirm alarm — Alarm bestätigen, Anlage bleibt scharf | E | [BELEGT] |
| `InputDisable` | `DisPc` | Sperrt `Tg, Tgnp, A, Anp, Ad, Adnp` | E | [ABGELEITET] |
| `DisMv` | – | – | E | [OFFEN] |
| `HI1` … `HI4` | – | – | E | [OFFEN] — in bausteine.md gelistet, in der KB nicht vorhanden |
| `Delay` (`600`) | `Ard` | Arming delay (s) | P | [ABGELEITET] · 600 = 600 |
| `MaxDurOut` (`900`) | `MaxA` | Maximale Alarmdauer (s) | P | [ABGELEITET] · 900 = 900 |
| `Remanence` (`Inv`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `IInit` (`Inv`) | `Aoc` | Arm open contact (offene Kontakte beim Scharfschalten) | P | [ABGELEITET] |
| `AutoConfirm` | `Sac` | Stillen Alarm bei `MaxA` quittieren | P | [ABGELEITET] |
| `TM` | `Atm` | Alarm test mode | P | [ABGELEITET] |
| `TQ1` | `Sad` | Verzögerung **stiller** Alarm (s) | P | [ABGELEITET] · 0 = 0 |
| `TQ2` (`20`) | `Aad` | Verzögerung **akustischer** Alarm | P | [ABGELEITET] · 20 = 20 |
| `TQ3` (`40`) | `Vad` | Verzögerung **optischer** Alarm | P | [ABGELEITET] · 40 = 40 |
| `TQ4` (`90`) | `Iad` | Verzögerung **interner** Alarm | P | [ABGELEITET] · 90 = 90 |
| `TQ5` (`150`) | `Ead` | Verzögerung **externer** Alarm | P | [ABGELEITET] · 150 = 150 |
| `TQ6` (`300`) | `Rad` | Verzögerung **ferner** Alarm | P | [ABGELEITET] · 300 = 300 |
| `TI` | `Eip` | Verlängerung der Alarmeingangs-Impulse (s) | P | [ABGELEITET] · 0 = 0 |
| `WI2` (`900`) | `Spt` | Zeitfenster zweiter Präsenzmelder (s) | P | [ABGELEITET] · 900 = 900 |
| `Q` | `S` | Status (0 unscharf, 1 scharf mit BM, 2 scharf ohne BM) | A | [ABGELEITET] |
| `Q1` | `Sa` | Stiller Alarm | A | [ABGELEITET] |
| `Q2` | `Aa` | Akustischer Alarm | A | [ABGELEITET] |
| `Q3` | `Va` | Optischer Alarm | A | [ABGELEITET] |
| `Q4` | `Ia` | Interner Alarm | A | [ABGELEITET] |
| `Q5` | `Ea` | Externer Alarm | A | [ABGELEITET] |
| `Q6` | `Ra` | Ferner Alarm | A | [ABGELEITET] |
| `AQ` | `N` | Anzahl aktiver Melder | A | [ABGELEITET] |
| `QT` | `At` | Alarmtest (nur wenn `Atm`=1) | A | [ABGELEITET] |
| `AQr` | `Rtad` | Restzeit Aktivierungsverzögerung (s) | A | [ABGELEITET] |
| `TQ` | `Ca` | Ursache des letzten Alarms (Text) | A | [ABGELEITET] |
| `OutTime` | `Ta` | Datum/Uhrzeit des letzten Alarms | A | [ABGELEITET] |
| `Qo` | `WDs` | Fenster/Tür offen | A | [ABGELEITET] |
| `TTS` | `WDot` | Namen offener Fenster/Türen (Text, TTS-tauglich) | A | [ABGELEITET] — die KB nennt den TTS-Einsatz wörtlich |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/alarmanlage/

Die Kette `TQ1`…`TQ6` (Verzögerungen) und `Q1`…`Q6` (Ausgänge) stützen sich gegenseitig:
sechs Alarmstufen in identischer Reihenfolge **still → akustisch → optisch → intern → extern → fern**,
Defaults 0/20/40/90/150/300 = KB-Defaults. Parameterzahl 14 = 14, Ausgangszahl 15 = 15.

> ⚠️ **Die sechs Scharfschalt-Eingänge bleiben [OFFEN] — das ist Absicht.**
> Die Doku hat drei Paare: mit Präsenzerkennung (`Tg`, `A`, `Ad`) und ohne (`Tgnp`, `Anp`, `Adnp`).
> Das XML hat ebenfalls drei Paare, unterschieden durch das Suffix **`P`**.
> - Nach **Reihenfolge** wäre `ActiveOO`=`Tg` (mit Präsenz) und `ActiveOOP`=`Tgnp` (ohne).
> - Nach **Name** würde `P` für „Präsenz" stehen — dann genau umgekehrt.
>
> Beides ist gleich plausibel. Eine falsche Zuordnung schaltet die Anlage im
> Kundenprojekt mit statt ohne Bewegungsmelder scharf — Fehlalarm oder blinde Anlage.
> **Einmal in Config verdrahten und im XML gegenlesen.**

### `AlarmChain` → **Alarmierungskette**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Alarm` | `A` | Ein = Alarm Start, Aus = Alarm Ende | E | [BELEGT] |
| `Urgent` | `Au` | Urgent alarm — aktiviert alle Ausgänge, dominiert `A` | E | [BELEGT] |
| `InEmgService` | `AEs` | Notalarm starten | E | [ABGELEITET] |
| `Text1` | `T1` | Alarmtext 1 (Platzhalter `<vt1>`) | E | [BELEGT] |
| `Text2` | `T2` | Alarmtext 2 | E | [ABGELEITET] |
| `Text3` | `T3` | Alarmtext 3 | E | [ABGELEITET] |
| `Confirm` | `Ca` | Setzt alle Alarmausgänge zurück | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Time` (`60`) | `Rt` | Reaction time bis zur nächsten Stufe (s) | P | [ABGELEITET] · 60 = 60 |
| `MaxRuns` (`4`) | `MaxR` | Maximale Wiederholungen (0 = unbegrenzt) | P | [ABGELEITET] · 4 = 4 |
| `Level1` … `Level10` | `A1` … `A10` | Textausgabe Stufe 1–10 | A | [BELEGT] |
| `OutEmgService` | `AEs` | Alarmtext Notfalldienst | A | [ABGELEITET] |
| `ActiveLevel` | `As` | Aktuelle Stufe (-1 = alle aktiv) | A | [ABGELEITET] |
| `LastStart` | `Ton` | Zeitpunkt des letzten Alarmstarts | A | [ABGELEITET] |
| `LastStop` | `Toff` | Zeitpunkt des letzten Alarmstopps | A | [ABGELEITET] |
| `ConfirmCause` | `Cc` | Grund der Bestätigung | A | [ABGELEITET] |
| `ConfirmTime` | `Tc` | Zeit der Bestätigung | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

Vollständige 26-zu-26-Deckung (8 E + 16 A + 2 P) in identischer Reihenfolge.
**Kein API-Ausgang** — einziger Funktionsbaustein der Sammlung ohne `OutputAPI`.
`AEs` existiert als Eingang **und** Ausgang; im XML sauber getrennt (`InEmgService`/`OutEmgService`).

### `SmokeAlarm` → **Brand- und Wassermeldezentrale**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Confirm` | `Ca` | Alarm bestätigen | E | [ABGELEITET] |
| `Mute` | `Cs` | Alarmsignale bestätigen (deaktiviert `Pas`/`Mas`) | E | [ABGELEITET] |
| `InputAlarm` | `S` | Externe **Rauch**melder ("Smoke detector") | E | [BELEGT-TECHDOC] — vorher [OFFEN] mit Kandidat `F` |
| `InputAlarmW` | `W` | Externe **Wasser**melder | E | [BELEGT-TECHDOC] |
| `InputAlarmS` | `F` | AFCI / Brandschutzschalter | E | [BELEGT-TECHDOC] ⚠️ **vorher `S`** — das `S` im XML-Namen steht nicht für Smoke |
| `InputTemp` | `T` | Externe Temperatursensoren | E | [ABGELEITET] |
| `InputAirDigitalS` | – | – | E | [OFFEN] — in bausteine.md gelistet, in der KB nicht vorhanden |
| `InputAirDigitalW` | – | – | E | [OFFEN] |
| `InputAirAnalog` | – | – | E | [OFFEN] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `AlarmDelay` (`120`) | `Mad` | Hauptalarm-Verzögerung nach Voralarm (s) | P | [ABGELEITET] · 120 = 120 |
| `MaxTemp` (`43`) | `Maxϑ` | Temperaturschwelle für Alarm (°) | P | [ABGELEITET] · 43 = 43 |
| `MaxDuration` (`300`) | `MaxA` | Maximale Alarmdauer (s) | P | [ABGELEITET] · 300 = 300 |
| `Remanence` (`Inv`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `Autoconfirm` | `Pac` | Voralarm bei `MaxA` automatisch bestätigen | P | [ABGELEITET] |
| `Servicemode` | `Sm` | Servicemodus (0 aus, 1 dauerhaft, >1 für diese Zeit) | P | [ABGELEITET] |
| `OutActive` | – | – | A | [OFFEN] |
| `OutAlarm1` | `Pa` | Voralarm | A | [ABGELEITET] |
| `OutAlarm2` | `Ma` | Hauptalarm | A | [ABGELEITET] |
| `OutSilent` | (`Pas`) | Voralarm-Signal? | A | [OFFEN] — „Silent" ≠ „Pre-alarm signal" |
| `OutHorn` | `Mas` | Hauptalarm-Signal (Sirene) | A | [ABGELEITET] |
| `OutNumAlarms` | `N` | Anzahl aktiver Melder | A | [ABGELEITET] |
| `OutAlarmTest` | `At` | Alarmtest | A | [ABGELEITET] |
| `OutText` | `Ca` | Ursache des letzten Alarms (Text) | A | [ABGELEITET] |
| `OutTime` | `Ta` | Datum/Uhrzeit des letzten Alarms | A | [ABGELEITET] |
| `OutHornSpd` | – | – | A | [OFFEN] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

**Zahlen passen nicht:** XML 27, Doku 22 (7 E + 9 A + 6 P). Die 6 Parameter decken sich exakt
(4 über `Def`-Werte). Bei den Eingängen sind `S`/`W` im XML **gegenüber der Doku vertauscht**
(XML: …W vor …S) — die Namen `InputAlarmS`/`InputAlarmW` sind aber selbsterklärend.
Zugeordnete Geräte stehen im Attribut **`Objects`**.

### `PresenceDetector` → **Präsenz**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputActivate` | `Act` | Activate — Präsenz bei steigender Flanke | E | [BELEGT] |
| `InputExtend` | `Ext` | Extend — verlängert aktive Präsenz | E | [BELEGT] |
| `InputTrigger` | `AE` | Activate / Extend — jede Änderung aktiviert/verlängert | E | [BELEGT] |
| `InputReset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `DeviceActivate` | – | – | E | [BELEGT] als „nur Loxone-Geräte", Doku-Kürzel [OFFEN] |
| `DeviceExtend` | – | – | E | [BELEGT] als „nur Loxone-Geräte", Doku-Kürzel [OFFEN] |
| `DeviceTrigger` | – | – | E | [BELEGT] als „nur Loxone-Geräte", Doku-Kürzel [OFFEN] |
| `ControlInput` | – | – | E | [OFFEN] |
| `ParamTOn` (`900`) | `Pet` | Presence extend time (s) | P | [BELEGT] · 900 = 900 |
| `ParamTWarn` (`15`) | `Tw` | Abschaltwarnzeit (s) | P | [ABGELEITET] · 15 = 15 |
| `OutputPresence` | `Pc` | Presence combined (für Präsenz-/Bewegungseingänge) | A | [BELEGT-TECHDOC] ⚠️ **bis 05.09.2026 stand hier `P`** — TechDoc: `OutputPresence` = "Presence combined" |
| `OutputActive` | `P` | Präsenz | A | [BELEGT-TECHDOC] ⚠️ vorher `Pc` per Ausschlussverfahren |
| `OutputOn` | `Pon` | Impuls bei Präsenzstart | A | [ABGELEITET] |
| `OutputOff` | `Poff` | Impuls bei Präsenzende | A | [ABGELEITET] |
| `OutputOnTime` | `Pd` | Dauer der aktuellen Präsenzphase (s) | A | [ABGELEITET] |
| `OutputWarn` | `Warn` | Warnimpuls vor Präsenzende | A | [ABGELEITET] |
| `OutputDevOnTime` | – | – | A | [OFFEN] |
| `OutputDevActiveTime` | – | – | A | [OFFEN] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/praesenz/ · verifizierte Teilzuordnung: [bausteine.md](bausteine.md)

XML 19, Doku 13 (4 E + 7 A + 2 P). Die sechs Zusatz-Konnektoren betreffen alle die
**Loxone-Melder-Anbindung** (`Device*`, `OutputDev*`) — in der KB nicht beschrieben.
Zugeordnete Melder stehen im Attribut **`DEVS`**.

⚠️ **Korrigiert 05.09.2026 nach TechDoc:** `OutputPresence`=`Pc`, `OutputActive`=`P`. Die alte
Zuordnung (`OutputPresence`=`P`) stammte aus bausteine.md und war eine Namensanalogie, kein Config-Befund.
Wer in einem Bestandsprojekt an `OutputPresence` hängt, hat den *kombinierten* Ausgang. Alter Text:
`OutputActive`↔`Pc` folgte nur aus dem Ausschlussverfahren: bausteine.md legte
`OutputPresence`=`P` fest, damit blieb für die verbleibenden sechs XML-Ausgänge nur noch `Pc`
übrig. Die Doku-Reihenfolge (`Pc` **vor** `P`) spricht dagegen.

---

## 9. Tore und Türen

### `Doorcontroller` → **Türsteuerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `TriggerFan` | `Bell` | Activate bell — Klingel aktivieren | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Timeout` (`Def="60"`) | `maxB` | Maximale Klingeldauer (s) | P | [ABGELEITET] · 60 = 60 |
| `Qb` | `Bell` | Ausgang Türklingel | A | [ABGELEITET] |
| `Q1` | `O1` | Custom output 1 (z. B. Türöffner) | A | [ABGELEITET] |
| `Q2` | `O2` | Custom output 2 (z. B. Licht außen) | A | [ABGELEITET] |
| `Q3` | `O3` | Custom output 3 (z. B. Licht innen) | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/tuersteuerung/

Vollständige 8-zu-8-Deckung. Der Konnektorname **`TriggerFan` ist eine Altlast** und hat mit
einem Lüfter nichts zu tun — es ist der Klingeleingang. Zugeordnete Intercom in den Eigenschaften.

### `CentralGate` → **Tor Zentral**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `Trigger` | `Tg` | Toggle (Öffnen/Stopp/Schließen) | E | [ABGELEITET] |
| `Open` | `Co` | Complete open (Stoppen nicht möglich) | E | [ABGELEITET] |
| `Close` | `Cc` | Complete close (Stoppen nicht möglich) | E | [ABGELEITET] |
| `T5` | `T5` | T5-Steuerung (Taste 1 auf, Taste 4 zu) | E | [ABGELEITET] — Namensgleichheit |
| `InputStop` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `InputPo` | `Po` | Partially Open — Teilöffnungsposition | E | [ABGELEITET] — Namensgleichheit |
| `InputDisable` | `DisPc` | Sperrt `Tg, Co, Cc, T5` | E | [ABGELEITET] |
| `OutOpenGate` | `No` | Anzahl der offenen Tore | A | [ABGELEITET] |
| `OutCloseGate` | `Nc` | Anzahl der geschlossenen Tore | A | [ABGELEITET] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/tor-zentral/

Vollständige 10-zu-10-Deckung (7 E + 3 A). Mitglieder im Attribut **`rec`**.

---

## 10. Ohne Zuordnung

### `CentralPresence` → **Präsenz Zentral** — Doku existiert nicht

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `InputReset` | – | – | E | [OFFEN] |
| `ParamTAbsence` (`Def="48"`) | – | – | P | [OFFEN] |
| `OutputActive` | – | – | A | [OFFEN] |
| `OutputPOn` | – | – | A | [OFFEN] |
| `OutputPOff` | – | – | A | [OFFEN] |
| `OutputOnTime` | – | – | A | [OFFEN] |
| `OutputPAbsent` | – | – | A | [OFFEN] |
| `OutputAPI` | – | – | A | [OFFEN] |

Quelle: **keine.** Der Baustein „Präsenz Zentral" ist mit Config 17 neu und hat
(Stand 30.07.2026) **keine KB-Seite**. Siehe [zentralfunktionen.md](zentralfunktionen.md).

Die Konnektorstruktur ähnelt der von `PresenceDetector` (`OutputActive`, `OutputPOn`,
`OutputPOff`, `OutputOnTime`) plus `OutputPAbsent` und `ParamTAbsence`. Eine Ableitung
über diese Ähnlichkeit wäre reine Analogie und wird hier **nicht** vorgenommen.

### `SwitchingTimer` — keine Konnektoren, keine Zuordnung

Die Vorlage hat **kein `Nio`-Attribut und kein einziges `<Co>`-Kindelement**. Geprüft:

```xml
<C Type="SwitchingTimer" V="175" U="…" Title="…" Cl="0,0,0" WF="16384" M="3" N="7"
   Modes="00000000-0000-0004-…,…,00000000-0000-000a-…" FIX="1">
  <Entry To="1440" V="1" /><Entry To="1440" Ix="1" V="1" /> … <Entry To="1440" Ix="6" V="1" />
</C>
```

Statt Konnektoren enthält der Knoten **`<Entry>`-Elemente** (Schaltzeiten je Betriebsmodus,
`To="1440"` = bis 24:00, `Ix` = Modus-Index 0…6) sowie `Modes` (7 Betriebsmodus-UUIDs) und
`FIX="1"`.

**Deutung [ABGELEITET]:** Das ist **nicht** der eigenständige Schaltuhr-Baustein
(der ist `DayTimer`), sondern das **eingebettete Schaltzeiten-Objekt**, auf das andere
Bausteine per `UUIDTimer` verweisen — bei der Intelligenten Raumregelung, der Lichtsteuerung
und den Berechtigungsbausteinen. Ein solches Objekt hat definitionsgemäß keine Ein-/Ausgänge
und deshalb auch keine Kürzeltabelle in der KB.

**Bekannte Lücke der Vorlagendatei:** Wer `SwitchingTimer` als eigenständigen Zeitschalter
verwenden will, findet in `bausteinvorlagen.xml` keine brauchbare Vorlage. Für einen
freistehenden Zeitplan `DayTimer` nehmen.

---

## 11. Programmier-Bausteine

Beide tragen ihre Logik als **Text in einem Attribut**, nicht als Verdrahtung. Ausführliche
Behandlung samt Befehls- und PicoC-Referenz, Entwurfsleitfaden und der Zeilenumbruch-Falle:
[programmier-bausteine.md](programmier-bausteine.md).

Verifiziert 05.08.2026 an `Bestandsprojekt V5.Loxone` (Config 17.1.7.27).

### `SequenceController` → **Ablaufsteuerung**

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `AI1` … `AI8` | `AI1-8` | Eingänge 1–8 (umbenennbar über `CNAME`) | E | [ABGELEITET] |
| `Trigger1` … `Trigger8` | `S1-8` | Sequenz 1–8 aktivieren | E | [ABGELEITET] |
| `ATrigger` | `S` | Sequenz per Nummer wählen (0…8) | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Remanence` (`Inv`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `Param` | – | – | E/P | **[OFFEN]** |
| `AQ1` … `AQ8` | `AQ1-8` | Ausgänge 1–8 | A | [ABGELEITET] |
| `OutputCurrSequence` | `S` | aktuell aktive Sequenz | A | [ABGELEITET] |
| `OutputCurrLine` | `L` | aktuelle Programmzeile | A | [ABGELEITET] |
| `TQ` | `TQ` | Textausgang | A | [BELEGT] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Quelle: https://www.loxone.com/dede/kb/ablaufsteuerung/

XML 32 Konnektoren, Doku 31. Die **Ausgangsseite ist 1:1 in gleicher Reihenfolge**; auf der
Eingangsseite bleibt `Param` übrig. ⚠️ Die Doku vergibt `S` **doppelt** (Eingang „Sequenz
auswählen" und Ausgang „aktuell aktive Sequenz") — im XML `ATrigger` bzw. `OutputCurrSequence`.

Nicht-Konnektor-Attribute: `STEP` = Intervall [ms] (KB 20…1000, Default 500) ·
`VNAME` = 5 Variablennamen, semikolongetrennt · `CNAME` = 31 semikolongetrennte
Konnektor-Klartextnamen (alle außer `OutputAPI`) · **`<SEQ NAM="…" CFG="…"/>` je Sequenz**,
`CFG` trägt den Programmtext.

### `Code16` → **Programm** (PicoC)

| XML-Konnektor (Co/@K) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `TI1` … `TI3` | `T1-3` | Texteingang 1–3 | E | [ABGELEITET] |
| `AI1` … `AI13` | `I1-13` | Eingang 1–13 | E | [ABGELEITET] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `TQ1` … `TQ3` | `Txt1-3` | Textausgang 1–3 (max. 4096 Byte) | A | [ABGELEITET] |
| `AQ1` … `AQ13` | `O1-13` | Ausgang 1–13 | A | [ABGELEITET] |
| `TeQ` | `Etxt` | Fehlertext | A | [ABGELEITET] |

Quelle: https://www.loxone.com/enus/kb/program/

**Vollständige 1:1-Deckung:** 17 E + 17 A = 34 = `Nio`, Doku ebenso. Kein `IoData` — der
Baustein hat weder Raum noch Kategorie („Nicht zugeordnet" ist der Normalzustand).

Nicht-Konnektor-Attribute: `Code` = PicoC-Quelltext · `Task` = laufende Nummer
(KB: max. 8 Programm-Bausteine) [ABGELEITET].

> 🛑 **Zwei Fallen, beide verifiziert:**
> 1. **`Code` ist doppelt vergeben.** Am `<C Type="Document">` ist `Code` die **Postleitzahl**.
>    Textsuche nach `Code="` erwischt zuerst die PLZ — immer über den Typ `Code16` gehen.
> 2. **`Code` enthält rohe CRLF.** Ein `XmlDocument`-Roundtrip macht daraus Leerzeichen und
>    zerstört das Programm lautlos. Rezept dagegen in
>    [programmier-bausteine.md](programmier-bausteine.md) Abschnitt 4 und
>    [xml-bearbeitung.md](xml-bearbeitung.md).

### PicoC-Indexierung — Doku-Kürzel ≠ Funktionsargument

`getinput(0)` liest **I1**, `setoutput(0, v)` schreibt **O1**, `getinputtext(0)` liest **T1**.
Text- und Analogkanäle haben **getrennte** Indexräume. [ABGELEITET]

---

## Lücke 1 — Doku-Bausteine **ohne** XML-Vorlage (152 von 179)

Aktualisierte Fassung des Abschnitts „Was noch fehlt" aus [bausteine.md](bausteine.md).
Für diese Typen ist **Typname, Konnektorsatz und `Nio` nicht ableitbar**. Weg: einmal in
Config einfügen, speichern, als Vorlage übernehmen.

**Abgedeckt sind 27 von 179 Doku-Bausteinen** (15 %) — siehe Tabellen oben.

**Logik, Vergleich & Speicher (17 von 22 offen)**
Nicht · Exklusiv ODER · Gleich · Ungleich · Größer oder gleich · Kleiner oder gleich ·
Analogkomparator · Analogspeicher · **SR-Impulsschalter** · Monoflop · Schieberegister ·
Status · Virtueller Status · Status Monitor · Binärdecoder · Binärdekoder · Binärkodierer
*(abgedeckt: Und, Oder, Merker, RS-Impulsschalter, Flankenerkennung — 5; offen: 17)*

**Analog & Mathematik (21 von 23 offen)**
Addierer · Addierer 4 · Subtrahierer · Multiplizierer · Dividierer · Modulo · Ganzzahl ·
Skalierer · MinMax · MinMax seit Reset · Analog MinMax-Begrenzer · Mittelwert ·
Gleitender Mittelwert · Analogwahlschalter · Analogwahlschalter 4-fach ·
Analogwertvalidierung · Analogwertüberwachung · Differenzschwellwertschalter ·
Rampensteuerung · Pulsweitenmodulator · Stepper
*(abgedeckt: Formel, Schwellwertschalter)*

**Zeit, Verzögerung & Impuls (11 von 15 offen)**
Einschaltverzögerung speichernd · Ein- und Ausschaltverzögerung · Verzögerter Impuls ·
Flankengetriggertes Wischrelais · Impulsgeber · Impuls bei · Langzeitklick · Mehrfachklick ·
Zufallsgenerator · Zufallssteuerung
*(abgedeckt: Einschaltverzögerung, Ausschaltverzögerung, Impuls um, Treppenlicht-Schalter, Schaltuhr — 5; offen: 10)*

**Bedienung, Taster & Oberfläche (15 von 16 offen)**
Taster · Tastschalter · 2 Tasten · 2 Auswahltasten · Auswahltaste · Radiotasten ·
Radiotasten 16 Eingänge · Komfortschalter · Touch Pure Flex Controller · Touch & Grill Baustein ·
App · Tablet · Webpage · Miniserver Shortcut · EIB-Taster
*(abgedeckt: Schalter)*

**Beleuchtung (6 von 8 offen)**
Hotel Lichtsteuerung · Dimmer · EIB Dimmer · RGB Lichtszene · Konstantlichtregler · Szene
*(abgedeckt: Lichtsteuerung, Licht Zentral)*

**Beschattung & Fenster (7 von 10 offen)**
Automatikbeschattung Integriert · Dachfenster Beschattung · EIB Beschattung · Fenster ·
Fenster Zentral · Composite-Fensterkontakt · Windmesser
*(abgedeckt: Automatikbeschattung, Automatikbeschattung Zentral, Fenster- und Türüberwachung)*

**Klima, Heizung & Regler (10 von 12 offen)**
HVAC Controller · Heizkurve · Heizungsmischer · Vorlauftemperatur Rechner · Taupunktrechner ·
Solarregelung · 2-Punkt-Regler · 3-Punkt-Regler · PI-Regler · PID-Regler
*(abgedeckt: Intelligente Raumregelung, Heiz- und Kühlsteuerung)*

**Lüftung & Klimaanlage (8 von 9 offen)**
Raumlüftungssteuerung · Leaf Lüfter · Internorm Lüfter · Fan Coil Steuerung ·
Fan Coil Frischluft Steuerung · Fan Coil Zentralsteuerung · Klimaanlagensteuerung ·
Klimaanlagen Zentralsteuerung
*(abgedeckt: WC-Lüftungssteuerung)*

**Sicherheit, Alarm & Präsenz (9 von 13 offen)**
Alarmanlage Zentral (`CentralAlarm` — Typname bekannt, **Vorlage fehlt**) · AAL Smart Alarm ·
Notfall Alarm · SIA DC-09 · Berechtigung · Berechtigung NFC Code Touch · Sprechanlage ·
Post- und Paketkasten · Trust
*(abgedeckt: Alarmanlage, Alarmierungskette, Brand- und Wassermeldezentrale, Präsenz)*

**Tore, Türen & Sonderanwendungen (7 von 9 offen)**
Tor · Bewässerung · Poolsteuerung · Saunasteuerung · Saunasteuerung mit Verdampfer ·
Wecker · Automatik-Regel
*(abgedeckt: Türsteuerung, Tor Zentral)*

**Zähler (10 von 10 offen — komplett)**
Zähler · Zähler & Speicher · Zähler Bidirektional · Aufwärtszähler · Auf/Abwärts-Zähler ·
Impulszähler · Impulszähler & Speicher · Impulszähler Bidirektional · Festwertzähler ·
Betriebszeitzähler

**Energie & Lastmanagement (11 von 11 offen — komplett)**
Energiemanager · Energiemanager Gen. 1 · Energiemonitor · Energieflussmonitor · Lastmanager ·
Wallbox · Wallbox Gen. 1 · Wallbox Manager · PV Produktionsvorhersage · Spotpreis-Optimierer ·
Power Supply & Backup

**Multimedia & Kommunikation (11 von 11 offen — komplett)**
Audio Player · Audio Player Gruppe fix · Audio Zentral · Music Server Zone · Mediensteuerung ·
Mail Generator · Call Generator · Text Generator · Benachrichtigung · IR Steuerung ·
Befehlserkennung

**System, Ablauf & Schnittstellen (10 von 10 offen — komplett)**
Ablaufsteuerung · Sequenzer · Programm · Ping · Netzwerk Interkommunikation · BACnet ·
Home Connect · Event Database Connector · Session Database Connector · Multiplikator Projekt

> **Merke:** Bausteintypen, die weder im Projekt noch in `FactoryPresets.xml` vorkommen, lassen
> sich nicht zuverlässig per XML erzeugen. Der Weg ist immer: einmal in Config einfügen,
> speichern, dann als Vorlage übernehmen.

---

## Lücke 2 — XML-Typen **ohne** Doku-Seite

| XML-Typ | Vermutete GUI-Bezeichnung | Warum keine Zuordnung |
|---|---|---|
| `CentralPresence` | Präsenz Zentral | Neu mit Config 17, **keine KB-Seite vorhanden** — alle 8 Konnektoren [OFFEN] |
| `SwitchingTimer` | (eingebettetes Schaltzeiten-Objekt) | Kein `Nio`, keine `<Co>`; kein Baustein mit Ein-/Ausgängen, daher kein KB-Pendant |

Alle übrigen 27 XML-Typen sind einer deutschen KB-Seite zugeordnet.

**Namensfallen** — XML-Typname ≠ GUI-Name:

| XML-Typ | Naheliegende, aber **falsche** Lesart | Tatsächlich |
|---|---|---|
| `PushButton` | Taster | **Schalter** (bistabil, mit `Rem`, ohne `Don`) |
| `PulseAt` | Impuls **bei** (Textmuster) | **Impuls um** (Zeitpunkt) |
| `HVACController` | HVAC Controller | **Heiz- und Kühlsteuerung** |
| `DayTimer` | Tagesschaltuhr | **Schaltuhr** |
| `AutoJalousie` | Jalousie | **Automatikbeschattung** (die einfache „Jalousie" hat keine Vorlage) |
| `Doorcontroller` · `TriggerFan` | Lüftersteuerung | **Türsteuerung**, `TriggerFan` = Klingeleingang |
| `SmokeAlarm` | Rauchmelder | **Brand- und Wassermeldezentrale** |
| `WindowsMonitor` | Fensterbaustein | **Fenster- und Türüberwachung** (der Baustein „Fenster" fehlt) |

---

## Lücke 3 — bekannte Mängel der Vorlagendatei

1. **`SwitchingTimer` ohne Konnektoren** (siehe oben) — als Zeitschalter unbrauchbar,
   `DayTimer` verwenden.
2. **`And`/`Or` nur zweikanalig.** Für mehr Eingänge kaskadieren (sicher) oder weitere
   `Co K="I3"`… ergänzen und `Nio` erhöhen — Letzteres ist plausibel (Muster wie
   `LightController2` mit `I1`…`I8`), aber **nicht verifiziert**.
3. **`Def`-Werte sind Instanzwerte, keine Werksdefaults.** Die Vorlagen stammen aus einem
   realen Projekt. Wo `Def` vom KB-Standardwert abweicht (z. B. `StairwayLS/TimeHigh` 300
   statt 180, `EdgeDetection/PulseTime` 300 statt 1, `AutoJalousie/Type` 6 statt 0), ist der
   KB-Wert der Werksdefault. **Beim Klonen bewusst setzen.**
4. **`AutoJalousie/Type="6"` (Markise).** Lamellen-abhängige Parameter (`Sw`, `Sd`, `Spm`,
   `Spi`) sind bei diesem Typ in Config unsichtbar — im XML aber vorhanden.
5. **Alarmanlage Zentral (`CentralAlarm`)**: Typname aus zentralfunktionen.md bekannt,
   aber **keine Vorlage** in `bausteinvorlagen.xml`.

---

## Methodik — wie diese Zuordnungen entstanden sind, und wo sie tragen

### Die vier Beweismittel, nach Stärke geordnet

1. **`Def`-Standardwerte (stärkstes Indiz).**
   Ein Parameterblock wie die Intelligente Raumregelung hat 20 Parameter mit 20 verschiedenen
   Zahlen (22,5 / 24,5 / 22 / 1,5 / 27,5 / 23,5 / 3 / 3 / 2 / 5 / 28 / 14 / 3600 / 3600 / 1800 /
   120 / 60 / 0 / 300 / 1). Wenn alle 20 XML-`Def`-Werte exakt auf die 20 KB-Standardwerte
   passen, ist das keine Reihenfolgeannahme mehr, sondern eine Wertetabelle mit
   praktisch eindeutiger Lösung. Genauso bei `LightController2` (21/21), `AutoJalousie` (20/22),
   `Alarm` (0/20/40/90/150/300) und `HVACController` (12/15).
   **Hier trägt die Ableitung.**

2. **Konnektorzahl-Gleichheit.**
   Wo XML-Konnektorzahl = Summe (Doku-Eingänge + Ausgänge + Parameter) gilt, ist die Menge
   geschlossen — jede Zuordnung schließt eine andere aus. Das ist bei 12 Typen der Fall:
   `And`, `Or`, `EdgeDetection`, `AnalogThresholdTrigger`, `PulseAt`, `StairwayLS`, `DayTimer`,
   `PushButton`, `CentralShade`, `CentralGate`, `Doorcontroller`, `ToiletFan`, `AlarmChain`.
   Ergibt die Restzuordnung genau einen Kandidaten, wird das als [ABGELEITET] gewertet
   (z. B. `PresenceDetector/OutputActive` → `Pc`).

3. **Reihenfolge (starkes, aber nicht beweiskräftiges Indiz).**
   Die `Co/@K`-Reihenfolge folgt in aller Regel dem Muster
   **Eingänge → Parameter → Ausgänge**, wobei innerhalb jeder Gruppe die KB-Tabellenreihenfolge
   gilt. Bestätigt bei `AutoJalousie` (16 E in exakter Doku-Reihenfolge, 10 A in exakter
   Doku-Reihenfolge), `LightController2` (30 E), `Alarm` (5 + 9 E, 15 A), `WindowsMonitor`,
   `CentralShade`, `AlarmChain`.
   **Achtung:** die KB tabelliert *Eingänge, Ausgänge, Parameter*, das XML sortiert
   *Eingänge, Parameter, Ausgänge* — die Parameter-Gruppe muss also umgesetzt werden.
   **Wo die Reihenfolge NICHT trägt:**
   - `HeatIRoomController2`: `RtD` steht im XML an Position 11, in der Doku an Position 16.
   - `HeatIRoomController2`, Ausgänge 14–20: Position und Name widersprechen sich
     (`Qb`/`Boost`, `AQtm`/`Os`) → `AQs`, `Qa` bleiben [OFFEN].
   - `AutoJalousie`, Parameter: XML-Reihenfolge weicht komplett von der Doku-Reihenfolge ab —
     hier haben nur die `Def`-Werte entschieden.
   - `StairwayLS`, `PushButton`, `DayTimer`, `CentralGate`, `SmokeAlarm`: Ein-/Ausgänge
     paarweise vertauscht gegenüber der Doku.
   Deshalb wurde Reihenfolge **nie allein** als Beleg verwendet.

4. **Namensähnlichkeit (schwächstes Indiz).**
   Trägt bei exakter Gleichheit (`Rdd`↔`Rdd`, `T5`↔`T5`, `RtD`↔`Rtd`, `InputPo`↔`Po`,
   `Type`↔`Type`, `Dir`↔`Dir`, `Mode`↔`Mode`).
   Trägt **nicht** bei Fast-Anagrammen (`TimeWarn` / `WarnTime`) und bei
   invertierter Semantik (`EnAutoShade`↔`DisSp`, `EnMove`↔`DisP`, `NoLast`↔`Lv`,
   `Safety`↔`Wa`). In beiden Fällen wurde entweder [OFFEN] gesetzt oder ein
   ⚠️-Hinweis in die Zeile geschrieben.

### Was bewusst NICHT gemacht wurde

- **Kein Raten bei Sicherheitsfunktionen.** Die sechs Scharfschalt-Eingänge der Alarmanlage
  (`ActiveOO`/`ActiveOOP`/`Active`/`ActiveP`/`ActiveDelay`/`ActiveDelayP`) und die beiden
  Temperaturlimits der Heiz-/Kühlsteuerung (`TempLimitC`/`TempLimitH`) sind [OFFEN], obwohl
  jeweils eine plausible Lesart existiert. Die Folgekosten einer Fehlzuordnung
  (Anlage scharf ohne Bewegungsmelder / Heizung im Winter gesperrt) rechtfertigen die Lücke.
- **Keine Analogieschlüsse zwischen Bausteinen.** `CentralPresence` hätte sich aus
  `PresenceDetector` „ableiten" lassen — das wäre eine Erfindung mit Doku-Anstrich.
- **Keine Übernahme aus der KB-Seite einer *anderen* Variante.** `AutoJalousie/SO` bleibt
  [OFFEN], obwohl die Seite „Automatikbeschattung **Integriert**" ein passendes `Sop` kennt.
  Das ist ein anderer Baustein.

### Zählwerk

| | Anzahl |
|---|---|
| XML-Bausteintypen gesamt | 29 |
| davon mit mindestens einer `[BELEGT]`-Zuordnung (aus bausteine.md / KB-Wortlaut) | 7 |
| davon vollständig oder überwiegend `[ABGELEITET]` | 20 |
| davon vollständig `[OFFEN]` | 2 (`CentralPresence`, `SwitchingTimer`) |
| Doku-Bausteine gesamt | 179 |
| Doku-Bausteine mit XML-Vorlage | 27 |
| Doku-Bausteine ohne XML-Vorlage | 152 |

### Nächster Schritt zur Verifikation

Die [OFFEN]-Zeilen lassen sich in einer einzigen Config-Sitzung schließen:
Baustein einfügen → **jeden** Ein-/Ausgang mit einem eindeutig benannten Merker verdrahten →
speichern → im XML nachsehen, welcher `Co/@K` welche `<In Input="…"/>` bekommen hat.
Ergebnisse hierher zurückschreiben und den Status von [OFFEN] auf [BELEGT] heben.
