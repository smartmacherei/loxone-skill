# Loxone Zentral- und Komfortfunktionen — Referenz

**Stand:** 30.07.2026 · Loxone Config 17.1.7.27
Quellen: offizielle Loxone-KB (URLs je Abschnitt) + verifizierter Autokonfig-Testlauf.

> **Grundbefund:** Loxone dokumentiert die **Bausteine**, aber **nicht die Autokonfigurations-Rezepte.**
> Die Seite [Auto-Konfiguration](https://www.loxone.com/dede/kb/auto-konfiguration/) listet die
> 20 Dialogeinträge nicht auf und sagt nicht, welche Bausteine je Funktion entstehen.
> **6 der 20 Einträge haben überhaupt keinen eigenen Baustein** — das sind reine Verdrahtungs-,
> Merker- und Betriebsmodus-Rezepte.

---

## 1. Die 20 Komfortfunktionen → Doku

| Funktion im Dialog | Baustein? | Doku |
|---|---|---|
| AAL Smart Alarm | ✅ | `/dede/kb/aal-smart-alarm/` |
| Alarmanlage | ✅ `CentralAlarm` | `/dede/kb/alarmanlage/`, `/dede/kb/alarm-zentral/` |
| **Anwesenheitssimulation** | ❌ Rezept | nur Video-Seite, keine Textdoku |
| Bewässerung | ✅ | `/dede/kb/bewaesserung/` |
| Brandmeldezentrale | ✅ `SmokeAlarm` | `/dede/kb/brand-wasser-meldezentrale/` |
| Energieflussmonitor | ✅ | `/dede/kb/energieflussmonitor/` |
| Fensterüberwachung | ✅ | `/dede/kb/fenster-tuer-ueberwachung/` |
| **Frostsicherung (Beschattung)** | ❌ Rezept | Verhalten in `/dede/kb/sicherheit/` |
| **Gute Nacht** | ❌ Rezept | keine KB-Seite |
| **Haus im Tiefschlaf und Party** | ❌ Betriebsmodi | `/dede/kb/betriebsmodi/` |
| **Haus verlassen** | ❌ Rezept | nur Blog `/dede/blog/haus-verlassen/` |
| Heiz- und Kühlsteuerung | ✅ `HVACController` | `/dede/kb/klima-controller/` |
| HVAC Control | ✅ **anderer Baustein!** | `/dede/kb/hvac-controller/` |
| Notfall Alarm | ✅ | `/dede/kb/notfall-alarm/` |
| **Panik** | ❌ Rezept | keine KB-Seite (→ Notfall Alarm) |
| **Stromausfall** | ❌ Rezept | keine KB-Seite |
| **Sturmschutz (Beschattung)** | ❌ Rezept | `Wa`-Eingang + `/dede/kb/windmesser/` |
| Vorlauftemperatur Rechner | ✅ | `/dede/kb/intelligente-temperatursteuerung/` |
| Wassermeldezentrale | ✅ `SmokeAlarm` | = Brandmeldezentrale, zweite Instanz |
| Zentralfunktionen | ✅ `Central*` | `/dede/kb/kategoriebezogenen-zentralbausteine/` |

---

## 2. ⚠️ Die zwei wichtigsten Regeln

### 2.1 Zuordnung ist immer ein Dialog, nie ein Draht
> *„Über einen **Doppelklick** auf den Baustein öffnet sich der Dialog wo Sie die jeweiligen
> Bausteine zuordnen können."*

Das erzeugt die XML-Attribute `rec` (Zentralbausteine), `Objects` (Meldezentrale, Fenster-
überwachung, AAL, IRC→HVAC) bzw. `DEVS` (Präsenz). **Es gibt keine Verbindungslinie zwischen
Zentral- und Raumbaustein.**

### 2.2 Die Dialoge listen nur Loxone-Air/Tree-Geräte
Genau deshalb erkennt die Autokonfiguration KNX-Peripherie nicht. Für KNX gilt durchgängig:
**Geräte auf die Eingänge verdrahten** statt im Dialog wählen.

| Baustein | KNX-Geräte hierhin verdrahten |
|---|---|
| Brand-/Wassermeldezentrale | `S` (Rauch), `W` (Wasser), `T` (Temperatur), `F` (Brandschutzschalter) |
| Fenster-/Türüberwachung | `Dwco` (offen), `Dwct` (gekippt), `Hpos` (Griffposition) |
| Alarmanlage | `P` (Präsenz), `Gb` (Glasbruch), `Wc` (Fenster), `Dc` (Tür), `Ot` |
| Präsenz | `Act`, `Ext`, `AE` |

**Preis dafür:** die namentliche Meldung („Rauchmelder Küche") in `Ca` / `Txu` geht verloren.
Mehrere Melder brauchen einen ODER-Baustein davor, wodurch `N` (Anzahl aktiver Melder) unbrauchbar wird.

---

## 3. Heiz- und Kühlsteuerung (`HVACController`)

`/dede/kb/klima-controller/` — **nicht** zu verwechseln mit „HVAC Control" (§3.4).

> *„Dieser Baustein steuert eine Heiz- und/oder Kühlquelle. Abhängig von den Anforderungen der
> zugewiesenen Intelligenten Raumregler wird entschieden, ob der Heiz- oder Kühlmodus aktiv ist."*

### Eingänge
| Kürzel | Bedeutung |
|---|---|
| `ϑo` | Außentemperatur — unverbunden ⇒ Systemvariable |
| `B` | Boost — aktiviert Stufe 2 sofort |
| `Ah` | Zusatzheizung |
| `F` | Ventilator |
| `Mh` | Manuell Heizen — **ignoriert alle Raumregler-Anforderungen** |
| `Eh` / `Ec` | Überschuss Heizen / Kühlen ⇒ erlaubt Raumreglern Über­heizen/-kühlen (`ϑExc`) |
| `Cfc` | Filterwechsel bestätigen |
| `Off` | <200 ms Reset, >200 ms Sperre (dominierend) |

### Ausgänge
`H` / `H2` (Stufe 2) · `C` / `C2` · `Ah` · **`Sv` Umschaltventil (Heizen=0, Kühlen=1)** ·
`F` Ventilator · `Fc` Filterwechsel · `ϑoa` Ø-Außentemperatur der letzten 48 h · `API`

### Parameter
| Kürzel | Bedeutung | Standard |
|---|---|---|
| `Mode` | −1 aus · 0 automatisch · 1 nur Heizen · 2 nur Kühlen | **−2** ⚠️ außerhalb des dokumentierten Bereichs — explizit setzen! |
| `Sot` | **Einschaltschwelle**: mittlere Ventilöffnung aller Raumregler muss diese überschreiten | 30 % |
| `MinHr` | Mindestlaufzeit vor Moduswechsel | 0 min |
| `Vd` | Umschaltventil-Laufzeit | 0 s |
| `Fod` | Ventilator-Nachlauf | 120 s |
| `Don` / `Doff` | Taktung Ein / Aus | 750 / 300 s |
| `MaxTp` | Taktungs-Schwelle | 0 % |
| `Tt2s` | Verzögerung bis Stufe 2 | 60 min |
| `ϑminS2` | unter dieser Außentemp. Stufe 2 sofort | −6 ° |
| `ϑminHP` | Min.-Außentemp. für Wärmepumpenbetrieb | −22 ° |
| `Otm` | Außentemp.-Modus: 0 aus · 1 Ø 48 h · 2 Systemvariable | 2 |
| `ϑLimH` | **darüber kein Heizbetrieb** | 18 ° |
| `ϑLimC` | **darunter kein Kühlbetrieb** | 15 ° |

### 3.1 ⚠️ Wie sich Raumregler registrieren — und was das mit den Ausgängen macht

Bidirektional über Dialoge, **nicht** über Drähte:

1. Am **IRC**: Eigenschaft **„Quellen konfigurieren"** → bis zu **3 Quellen** verlinken.
2. Je Quelle: Heizen/Kühlen ja-nein, PWM-Unterstützung, **Priorität**, „günstig".
3. **Danach erscheinen am IRC neue Ausgänge `H1–H3` / `C1–C3` / `HC1–HC3`** — einer je Quelle.
   Diese liefern Stellwerte *nur*, wenn die Quelle im passenden Modus ist.
4. Am **HVACController**: Eigenschaft **„Raumregler zuordnen"** (Gegenrichtung).

> **Für den KNX-Nachbau heißt das:** Sobald eine Quelle konfiguriert ist, gehört der KNX-Ventil-
> aktor an **`AQh1`** (H1) statt an `AQh` (H). Ohne konfigurierte Quelle bleibt `AQh` richtig.
> **Vor dem Rollout im Baustein prüfen, welcher Ausgang tatsächlich angeboten wird.**

**Bedarfsrechnung:** Gesamtbedarf in **Gradquadratmetern**
`(Solltemperatur − Isttemperatur) × Raumgröße` → deshalb `Sqm` je Raum pflegen.
Belegte Räume werden priorisiert.

### 3.2 Abgrenzung der drei Klima-Zentralbausteine

| | **Heiz-/Kühlsteuerung** | **HVAC Controller** | **Vorlauftemperatur Rechner** |
|---|---|---|---|
| Zweck | steuert Heiz-/Kühlquelle | „in erster Linie für **nordamerikanische** HVAC-Systeme" | berechnet Vorlauf-Soll aus Außentemp., Heizkurve, Raumbedarf |
| Ausgänge | H/H2/C/C2/Ah/Sv/F | W/W1/W2, Y (Kompressor), E (Emergency Heat), O/B (Reversing Valve), G | `AQf` Vorlauf-Soll, `AQb` Puffer-Soll, `Qp` Pumpe, `AQr` Bedarf °m² |
| Anlage | Kessel/WP + Umschaltventil, Fußboden | Split/Rooftop/Furnace, 24 V | Mischerkreis |

⚠️ Sind Vorlauftemperatur-Rechner **und** Heiz-/Kühlsteuerung im Projekt, **gewinnt `Sot`** der
Heiz-/Kühlsteuerung über `Str` des Rechners.

**Vorlauftemperatur Rechner — Kernparameter:** `Min`/`Max` 5/40 · `S` Kurvensteigung **0.5** ·
`N` Parallelverschiebung 0 · `Str` Pumpenschwelle 35 % · `G` Gewichtung 1 · `I` Anhebung 2 ·
`B` Puffer-Offset 5 · `Ps` Pumpen-Zwangslauf (Tage).

---

## 4. Sturmschutz & Frostsicherung — es gibt keine Bausteine

Beide Dialogeinträge erzeugen **Verdrahtungslogik** auf die Beschattungsbausteine.

**Verhalten laut `/dede/kb/sicherheit/`:**
> **Sturmschutz:** *„Erfasst die Wetterstation eine Windgeschwindigkeit ab der die Beschattung
> Schaden nehmen könnte, so wird der Sturzschutz aktiv."* → Sicherheitsposition + Sperre.
> **Frostsicherung:** *„Fällt die Außentemperatur **unter 1 °C** und es wird ein **Niederschlag**
> erkannt"* → alle Beschattungen **sofort gestoppt** und gesperrt. Aufhebung ab **10 °C**.

### Der entscheidende Unterschied
| | Ziel-Eingang | Warum |
|---|---|---|
| **Sturmschutz** | **`Wa`** | fährt in Position `Wap` **und** sperrt |
| **Frostsicherung** | **`Off`** (>200 ms) | *stoppt* — der Panzer könnte festgefroren sein, er darf **nicht fahren** |

### `Wa` im Detail
> *„Fährt die Beschattung in die Windalarm-Position laut Parameter (Wap) und sperrt den Baustein."*
> Aktive Automatik wird **pausiert, nicht abgebrochen**. Nach Alarmende Neustart nur über positive
> Flanke an `Sps` oder Impuls auf `Spr` — *„die Bedingungen werden am Ende des Windalarms **nicht
> neu ausgewertet**."*

⚠️ **`Wap` Standard = 0 = ganz offen.** Für Raffstore/Jalousie/Markise richtig (hochfahren/einfahren),
für Rollläden ggf. 1. **Je Behangtyp prüfen.**

### Rezept für KNX
```
Sturmschutz:
  KNX-Windgeschw. → Schwellwertschalter (Ein 50 km/h, Aus 35 km/h) → Wa
Frostsicherung:
  KNX-Außentemp. → Schwellwert (Ein <1 °C, Aus >10 °C) ─┐
  KNX-Niederschlag ─────────────────────────────────── UND → Off (>200 ms)
```
`Wa` existiert **auch am `CentralShade`** — ein Draht dorthin reicht, wenn alle Behänge Mitglied sind.

**Windmesser-Baustein** (`/dede/kb/windmesser/`) nur bei **Frequenz**-Signal nötig
(Parameter `W` Alarmschwelle 50 km/h, `Avgt` 10 min). Liefert KNX bereits km/h ⇒ Schwellwertschalter.

### Benötigte Systemvariablen
**Sonnenschein** (für „Sonnenschein verwenden") · **Windgeschwindigkeit** · **Außentemperatur** ·
**Niederschlag**

---

## 5. Zentralbausteine

| Baustein | XML | Doku |
|---|---|---|
| Licht Zentral | `CentralLight` | `/dede/kb/licht-zentral/` |
| Automatikbeschattung Zentral | `CentralShade` | `/dede/kb/beschattung-zentral/` |
| Audio Zentral | – | `/dede/kb/audio-zentral/` |
| Tor Zentral | `CentralGate` | `/dede/kb/tor-zentral/` |
| Alarmanlage Zentral | `CentralAlarm` | `/dede/kb/alarm-zentral/` |
| Fenster Zentral | – | `/dede/kb/fenster-zentral/` |
| **Präsenz Zentral** | `CentralPresence` | ❌ **keine Doku** (neu mit Config 17) |

> Zentral abgesetzte Befehle **umgehen den `DisPc`-Eingang** der Mitglieder.

**Licht Zentral — wichtige Ein-/Ausgänge:** `M+`/`M-` (Stimmung vor/zurück; **Doppelklick → `2C`,
Dreifachklick → `3C`**) · `Mood` (ID 0–99) · `On` (= Stimmung 99) · `Alarm` (blinkt, **funktioniert
trotz `Off`**) · `Off` · `DisP` · Ausgang `Na` (Anzahl aktiver Leuchten).
Die `2C`/`3C`-Ausgänge sind die Standard-Trigger für „Gute Nacht" und „Haus verlassen".

**Fenster Zentral:** Eingang **`Wp` (Wetterschutz)** — *„Fenster werden geschlossen und für die
weitere Bedienung gesperrt"* — das Fenster-Pendant zu `Wa`.

### `CentralPresence` — keine Doku
Nur die Blog-Ankündigung zu Config 17: *„allows you to keep track of current occupancy throughout
the entire building. When no one is present, the system can automatically trigger actions – such as
switching the heating mode or arming the alarm system."*
`ParamTAbsence=48` ist **nicht dokumentiert**; 48 taucht bei Loxone konsistent als **Stunden**-Größe
auf ⇒ vermutlich „nach 48 h ohne Präsenz gilt längere Abwesenheit" (→ Tiefschlaf-Modus).
**Im Baustein-Tooltip verifizieren.**

**Ersatz ohne den Baustein:** ODER über alle `P`-Ausgänge der Präsenzbausteine →
Ausschaltverzögerung → Merker „Abwesend".

---

## 6. Haus verlassen / Gute Nacht — die Rezepte

**Haus verlassen** (nur Blog dokumentiert): Dreifachklick im **Durchgangsraum**.

| Gewerk | Ziel | Eingang |
|---|---|---|
| Licht | `CentralLight` | `Off` (Impuls) |
| Beschattung | `CentralShade` | `Sps` (Impuls) — *„wieder in den Automatikmodus"* |
| Heizung | alle IRC | **`E`** (Eco) — *„senkt dementsprechend die Temperatur"* |
| Musik | Audio Zentral | `Off` |
| Alarm | `CentralAlarm` | **`Ad`** (verzögert scharf, `Ard` = 600 s) |

**Gute Nacht:** Dreifachklick im **Schlafraum**. Licht + Musik aus, Alarm scharf, Raumregelung
bleibt im Nacht-/Eco-Profil (nicht Gebäudeschutz), auslösender Raum ausgenommen.
Gästezimmer lassen sich von Zentralfunktionen ausnehmen (`/dede/kb/zentralfunktion-gaestezimmer/`).

**Haus im Tiefschlaf / Party:** reine **Betriebsmodi** aus dem Peripheriebaum, per
„Ausgangsreferenz einfügen" in die Logik. *„Auto-Configuration uses predefined modes and connects
them accordingly."* → Tiefschlaf aktiviert am IRC den Gebäudeschutz (`Bp`).

---

## 7. Brand-/Wassermeldezentrale (`SmokeAlarm`)

Ein Bausteintyp, zwei Instanzen (Brand über `S`/`T`/`F`, Wasser über `W`).

**Eingänge:** `S` Rauchmelder · `W` Wassermelder · `T` Temperatursensor · `F` Brandschutzschalter ·
`Ca` bestätigen · `Cs` Signale bestätigen (Alarm bleibt) · `Off`
**Ausgänge:** `Pa`/`Ma` Vor-/Hauptalarm · `Pas`/`Mas` Signale (Sirenen) · `N` Anzahl aktiver Melder ·
`Ca` Ursache · `Ta` Zeitpunkt · `At` Test · `API`

| Parameter | Bedeutung | Standard |
|---|---|---|
| `Mad` | Verzögerung Hauptalarm nach Voralarm | 120 s |
| `Maxϑ` | Maximaltemperatur → Alarm | 43 ° |
| `MaxA` | max. Alarmdauer, danach Auto-Bestätigung | 300 s |
| `Sm` | Servicemodus | 0 s |

**Unscharf ≠ Quittieren:** Quittieren bestätigt den Alarm **ohne** unscharf zu schalten — jeder
Melder kann sofort neu auslösen.

### Alarmierungskette (`AlarmChain`)
10-stufige Eskalation. `A` Alarm · `Au` **dringend** (alle Stufen sofort, dominiert `A`) ·
`AEs` Notfalldienst · `T1-3` Texte · `Ca` bestätigen.
Ausgänge `A1-10` (**unverbundene Stufen werden übersprungen**), `As` aktuelle Stufe (−1 = alle).
Parameter: `Rt` Reaktionszeit **60 s** (0 = alle gleichzeitig), `MaxR` Wiederholungen **4** (0 = unbegrenzt).
Textplatzhalter: `<vn>` Bausteinname · `<vt1-3>` Eingangstexte · `<vton>` Startzeit · `<vcn>`/`<vca>` Kunde.

**Typische Verdrahtung:** `SmokeAlarm.Ma` → `AlarmChain.A`, `SmokeAlarm.Ca` → `AlarmChain.T1`,
`A1` → Push, `A2` → Mail, `A3` → Caller.

---

## 8. Alarmanlage — gestaffelte Alarmstufen

**Alarm-Eingänge:** `P` Präsenz · `Gb` Glasbruch · `Wc` Fenster · `Dc` Tür · `Ot` sonstige
**Scharfschalten:** `Tg`/`Tgnp` Toggle · `A`/`Anp` sofort · `Ad`/`Adnp` verzögert (`np` = ohne Präsenzerkennung)

| Parameter | Standard | | Parameter | Standard |
|---|---|---|---|---|
| `Ard` Einschaltverzögerung | **600 s** | | `Iad` interner Alarm | 90 s |
| `Sad` stiller Alarm | 0 s | | `Ead` externer Alarm | 150 s |
| `Aad` akustisch | 20 s | | `Rad` Fernalarm | 300 s |
| `Vad` optisch | 40 s | | `MaxA` max. Alarmdauer | 900 s |
| `Spt` 2. Melder-Fenster | 900 s | | `Aoc` Fenster offen beim Scharfschalten | 0 |

⚠️ **`MaxA` muss größer sein als die längste Verzögerung**, sonst werden späte Stufen nie aktiv.
⚠️ Bei scharfer Anlage setzt Loxone **Tree-Präsenzmelder automatisch auf kürzeste Nachlaufzeit** —
bei **KNX-Meldern passiert das nicht**, dort im Melder selbst parametrieren.
⚠️ „Wartezeit nach Start" < 10 s kann bei Miniserver-Neustart **Fehlalarme** auslösen.

---

## 9. Weitere Bausteine — kompakt

**Fenster-/Türüberwachung:** `Hpos` (1 zu · 2 gekippt · 3 offen · 4 zu unversperrt · 5 zu versperrt ·
0 offline), `Dwco`/`Dwct`/`Dwcs`. Ausgänge `Open`/`Tilt`/`Closed`/`Offline`/`Secured` (Zähler),
`Txlt` letzter Auslöser, `Txu` Namen aller unsicheren. **Öffner-Kontakte brauchen Eingangsinvertierung.**

**AAL Smart Alarm** (Ambient Assisted Living): Alarm bei ausbleibender Bewegung.
`Tt` Durchgangsraum **15 min** · `Tc` Aufenthaltsraum **60 min** · `Tb` Schlafraum **420 min** ·
`D` Verzögerung Stufe 2 **60 s**. ⚠️ **Raumtypen „Sonstige"/„Zentral" werden ignoriert.**

**Notfall Alarm** (= vermutlich „Panik"): `Tg` Push&Hold, `Ta` Halten für Alarm **4 s**,
`Tc` Halten für Bestätigung **2 s**. Button Air löst **sofort** aus. Loxone Touch: mittlere Taste (I3).

**Bewässerung:** bis **8 Zonen**. `MaxR` max. Regenvorhersage **2 l/m²** · `MaxRa` max. Regendauer
24 h **1800 s** · `Tv1-8` Ventil-Laufzeit **600 s**. `Sel` 0 = alle aus, 9 = alle ein.

**Energieflussmonitor:** bis **6 Objekte** in Sternform. `Pre`/`Pri` Export-/Importpreis 0,2 ·
`CO2` 0,42 kg/kWh. Zähler per **Drag & Drop**, aufeinander ziehen ⇒ Unterverteiler,
nicht gemessene Verbraucher erscheinen als „**Rest**".

**Anwesenheitssimulation:** kein Baustein. Nachbau über **Zufallssteuerung**
(`Son` 100 s, `Soff` 10 s) oder Zufallsgenerator + Schaltuhr auf `CentralLight`.
Wird laut Doku im Betriebsmodus „Haus im Tiefschlaf" aktiviert.

---

## 10. Reihenfolge für den Nachbau

1. **Betriebsmodi zuerst** — Haus verlassen / Gute Nacht / Tiefschlaf / Party hängen alle daran.
2. **Raumbausteine** (IRC, Lichtsteuerung, Beschattung, Präsenz) je Raum.
3. **Zentralbausteine** anlegen, dann per Doppelklick Mitglieder anhaken.
4. **Quellen am IRC konfigurieren** → prüfen, ob der Ventilaktor an `H` oder `H1` gehört.
5. **Beschattung scharf schalten — in dieser Reihenfolge:**
   1. `Dir` (Himmelsrichtung) und Fahrzeiten je Behang setzen — sonst wirkungslos
   2. Sturmschutz (`Wa`) und Frostsicherung (`Off`) verdrahten und **testen**
   3. `Wap` je Behangtyp prüfen (Default 0 = auffahren)
   4. **erst dann** `Sps` freigeben
6. Alle **To-Dos** abarbeiten.
