# Was die Loxone-Autokonfiguration je Raum und Kategorie anlegt

**Quelle:** nicht die Web-Doku, sondern **Loxone's eigene Werksvorlagen**, die mit Loxone Config
mitgeliefert werden:
`C:\ProgramData\Loxone\Loxone Config 17.1.7.27\Templates\FactoryPresets.xml`

Das ist die Datei, aus der die Autokonfiguration die Bausteine mit ihren Vorgabewerten erzeugt.
Damit ist auch die offene Frage aus der Web-Doku beantwortet: **das XML-Attribut `PType` am Raum
ist der Raumtyp.**

| `PType` | Raumtyp (Loxone-intern) | deutsche Bezeichnung |
|---|---|---|
| **1** | `SleepingRoom` | Schlafraum |
| **2** | `LivingRoom` | Aufenthaltsraum |
| **3** | `PassageRoom` | Durchgangsraum |
| 4 | (keine Vorlage) | Zentral / Technik |
| 5 | (keine Vorlage) | Außen |

---

## 1. Welche Bausteine je Raum erzeugt werden

Pro Raum enthält die Werksvorlage genau diese Bausteine:

| Baustein | XML-Typ | wofür |
|---|---|---|
| Beleuchtungssteuerung | `LightController2` | Kategorie **Beleuchtung** |
| Automatikbeschattung | `AutoJalousie` | Kategorie **Beschattung** |
| Intelligente Raumregelung | `HeatIRoomController2` | Kategorien **Heizung** (Stellantrieb) + **Fühler** (Temperatur) |
| Intelligente Raumregelung (alt) | `IRoomcontrol` | Altbaustein, nur noch für Bestand |
| Präsenz | `PresenceDetector` | Bewegungs-/Präsenzmelder |
| Raumklima / Lüftung | `Ventilation`, `Leaf`, `VentInternorm` | Loxone-Lüftungsgeräte |
| Musik | `MediaClient` | Kategorie **Audio** |

---

## 2. Intelligente Raumregelung — Vorgabewerte je Raumtyp

`HeatIRoomController2`, Nio=40, 43 Konnektoren

| Parameter | Bedeutung (Doku-Kürzel) | Schlafraum | Aufenthaltsraum | Durchgangsraum |
|---|---|---|---|---|
| `TComfort` | **Komforttemperatur Heizen** (ϑch) | **18,0 °C** | **22,5 °C** | **20,0 °C** |
| `TComfortC` | Komforttemperatur Kühlen (ϑcc) | **22,0 °C** | **24,5 °C** | **22,0 °C** |
| `TDiff` | erlaubte Abweichung Komfort (ϑd) | 1,5 K | 1,5 K | 1,5 K |
| `TSaveL` | Eco-Offset Heizen (ϑeh) | **2,5 K** | **3,0 K** | **2,5 K** |
| `TSaveU` | Eco-Offset Kühlen (ϑec) | **2,5 K** | **3,0 K** | **2,5 K** |
| `TShadeHeat` | **Beschattung im Heizbetrieb** (ϑsh) | **20,0 °C** | **27,5 °C** | **24,5 °C** |
| `TShadeCool` | **Beschattung im Kühlbetrieb** (ϑsc) | **19,0 °C** | **23,5 °C** | **21,0 °C** |
| `TDeepSleep` | Frostschutz (ϑfp) | 5 °C | 5 °C | 5 °C |
| `TMax` | Hitzeschutz (ϑhp) | 28 °C | 28 °C | 28 °C |
| `TimeMove` | Ventilschutz (Vs) | 14 d | 14 d | 14 d |
| `TimeC` | Komfort-Nachlauf (Cet) | 3600 s | 3600 s | 3600 s |
| `TimeS` | Eco-/Gebäudeschutz-Nachlauf (EBpet) | 3600 s | 3600 s | 3600 s |
| `TimeMv` | **Präsenz-Nachlauf** (Pet) | 1800 s | 1800 s | 1800 s |
| `THCelvin` | Aufheizgeschwindigkeit (Hs) | 120 min/K | 120 | 120 |
| `TCCelvin` | Abkühlgeschwindigkeit (Cs) | 60 min/K | 60 | 60 |
| `ExT` | (Quellen-/Erweiterungstyp) | 2 | 3 | 3 |

### Integrierte Schaltuhr (Komfortzeiten)

* **Schlafraum** — 15 Einträge: Mo–Fr **00:00–06:00** und **20:00–24:00**, Sa/So **00:00–10:00** und **20:00–24:00**
  → Komfort nachts, Eco tagsüber.
* **Aufenthaltsraum / Durchgangsraum** — 8 Einträge: Mo–Fr und So **06:00–22:00**, Fr/Sa **06:00–24:00**
  → Komfort tagsüber, Eco nachts.

⚠️ Die Schaltuhrzeiten sind laut Doku **Zielerreichungszeiten**, keine Startzeiten — der Baustein
heizt selbstlernend vor.

---

## 3. Beleuchtungssteuerung — Vorgabewerte je Raumtyp

`LightController2`, Nio=64

| Parameter | Bedeutung | Schlafraum | Aufenthaltsraum | Durchgangsraum |
|---|---|---|---|---|
| `MoveOn` | **Nachlaufzeit Bewegungsmelder** | **300 s** | **900 s** | **120 s** |
| `MoveIgnore` | Bewegung ignorieren nach manuellem Aus | 300 s | 300 s | 300 s |
| `MoveTimeout` | max. Dauer Bewegungslicht | 3600 s | 3600 s | 3600 s |
| `BrightnessLimit` | Helligkeitsschwelle | 30 lx | 30 lx | 30 lx |
| `FadingTime` | Überblendzeit | 1 s | 1 s | 1 s |
| `MaxP` | max. Leistung (Anteil) | 0,35 | 0,35 | 0,35 |
| `Step` / `Steptime` | Dimmschritt | 2 % / 0,2 s | 2 % / 0,2 s | 2 % / 0,2 s |
| `AlarmPeriod` / `AlarmClockPeriod` | Alarm-/Weckperiode | 4 / 3 | 4 / 3 | 4 / 3 |

Angelegte Lichtstimmungen: **„Bewegung"**, **„Viel Licht"** (beide als Bewegungsstimmung) und **„Aus"**.

Das ist genau der Unterschied, den die Loxone-Doku textlich beschreibt: im Durchgangsraum
**kürzere** Bewegungsmelderzeiten (120 s), im Aufenthaltsraum **längere** (900 s).

---

## 4. Präsenz-Baustein — Vorgabewerte je Raumtyp

`PresenceDetector`, Nio=17

| Parameter | Bedeutung | Schlafraum | Aufenthaltsraum | Durchgangsraum |
|---|---|---|---|---|
| `ParamTOn` | Präsenz-Nachlauf (Pet) | **300 s** | **900 s** | **120 s** |
| `ParamTWarn` | Abschaltwarnung (Tw) | 15 s | 15 s | 15 s |

Zusätzlich pro Raumtyp identisch die Präsenz-/Bewegungs-Defaults
`PSD As=-2 Ae=1380 Amin=1 Amax=4 Dmin=30 Dmax=180 O=1 V=20`.

---

## 5. Automatikbeschattung — Vorgabewerte

`AutoJalousie`, Nio=45 — **bei allen drei Raumtypen identisch**:

| Parameter | Bedeutung | Wert |
|---|---|---|
| `AutMode` | Sonnenstandsautomatik-Modus (Spm) | **1 = Optimale Kühlung** |
| `Dir` | Himmelsrichtung | **−1 = nicht konfiguriert** ⚠️ muss von Hand gesetzt werden |
| `DirTol` / `DirTol2` | Richtungstoleranz Ein-/Austritt | 85° / 85° |
| `AutoShadeTime` | Nachführintervall Lamellen | 120 min |
| `AutoShadeEnd` | Aktion bei Automatik-Ende | 1 = vollständig öffnen |
| `SRoff` / `SSoff` | Start-/Endverschiebung Sonnenauf-/untergang | +30 / −30 min |
| `Width` / `Space` | Lamellenbreite / -abstand | 70 / 60 mm |
| `TimeEnd` / `TimeEndDown` | Fahrzeit auf / ab | 75 s / 70 s ⚠️ muss je Behang gemessen werden |
| `MinPulse` / `MinMove` / `Back` | Impuls-/Bewegungsparameter | 3 s / 0,4 / 0,8 |
| `Type` | Behangtyp | 0 |

---

## 6. Musik (MediaClient)

Nio=54 — einziger Unterschied je Raumtyp ist wieder `MoveOn`: **300 / 900 / 120 s**.
Lautstärken: Default 25, Max 100, Alarm 75, Klingel 50, TTS 40, Schritt 3.

---

## 6a. Der Autokonfigurations-Dialog (aus dem Testlauf 30.07.2026)

### Schritt 1 — „Grundfunktionen", je Raum anwählbar
Spalten: **Beleuchtung · Beschattung · Klima · Audio · Wecker · Raum verlassen · Peripherie · Präsenz**

Was in diesem Projekt tatsächlich anwählbar war:

| Funktion | anwählbar bei | Regel |
|---|---|---|
| Beleuchtung | allen 20 Räumen | DALI/KNX-Licht wird erkannt |
| **Beschattung** | **nur Testraum** | KNX-Jalousieaktoren werden **nicht** erkannt |
| **Klima** | **nur Testraum** | KNX-Heizventile + 1-Wire-Fühler werden **nicht** erkannt |
| **Audio / Peripherie / Präsenz** | **nur Testraum** | – |
| Wecker | Kinderzimmer 1–3, Schlafzimmer | genau die 4 Räume mit `PType=1` (Schlafraum) |
| Raum verlassen | Bad OG, Bad UG, Diele, Schrankraum, Stiegenhaus, WC | genau die 6 Räume mit **verdrahtetem Bewegungsmelder** |

→ **„Raum verlassen" ist eine Raum-Funktion, keine Zentralfunktion.** Sie erzeugt den Merker
„Raum verlassen &lt;Raumname&gt;" aus `LightController2.OutputReset`, der auf `IRC.Reset` und
`AutoJalousie.ReactAutoShade` geht.

### Schritt 2 — „Komfortfunktionen" (zentral), 20 Stück
AAL Smart Alarm · Alarmanlage · Anwesenheitssimulation · Bewässerung · Brandmeldezentrale ·
Energieflussmonitor · Fensterüberwachung · **Frostsicherung (Beschattung)** · Gute Nacht ·
Haus im Tiefschlaf und Party · **Haus verlassen** · **Heiz- und Kühlsteuerung** · HVAC Control ·
Notfall Alarm · Panik · Stromausfall (nicht verfügbar) · **Sturmschutz (Beschattung)** ·
Vorlauftemperatur Rechner · Wassermeldezentrale · Zentralfunktionen

→ **„Haus verlassen"** erzeugt zentral den Merker „Raumregler Reset", der auf `IRC.Reset` aller
Raumregler geht.
→ **„Zentralfunktionen"** erzeugt CentralLight / CentralShade / CentralGate / CentralAlarm /
**CentralPresence**. Diese merken sich ihre Mitglieder im XML-Attribut **`rec`** (UUID-Liste),
nicht per Verdrahtung.
→ **„Heiz- und Kühlsteuerung"** erzeugt den `HVACController` auf einer eigenen Seite
„Zentral Klima"; jeder Raumregler registriert sich per Attribut `Objects=<HVAC-UUID>`.

### Was der Testlauf sonst noch zeigte
* Der Raumregler landet in Kategorie **Klima** (nicht Heizung).
* `Qs` (Shd) → `AutoShade` (Sps) — **bestätigt**, genau wie in der Doku beschrieben.
* Der neue Beschattungsbaustein bekommt **`Sun="true"`** („Sonnenschein verwenden").
* `Dir` (Himmelsrichtung) bleibt **−1** — muss immer von Hand gesetzt werden (erzeugt To-do).
* Jalousie-Ausgänge (`Op`/`Cl`) bleiben unverbunden — „aus Sicherheitsgründen", wie dokumentiert.
* Präsenz läuft über einen **`PresenceDetector`**-Baustein (Kategorie *Melder*), dessen
  `OutputPresence` **gleichzeitig** auf `LightController2.Presence` und `IRC.Move` geht.

---

## 7. Konsequenz für dieses Projekt

Die Autokonfiguration **verwendet KNX-Komponenten nicht** — bestätigt aus der Praxis. Für ein
KNX/DALI-Bestandsprojekt ist sie damit **kein Generator**, aber sehr wohl die
**Referenz für die Parametrierung**: die Werte oben sind exakt das, was Loxone selbst setzen würde.

Für die 10 regelbaren Räume ergibt sich daraus:

| Raum | PType | Raumtyp | ϑch Heizen | ϑsh Beschattung |
|---|---|---|---|---|
| Schlafzimmer | 1 | Schlafraum | 18,0 °C | 20,0 °C |
| Kinderzimmer 1 | 1 | Schlafraum | 18,0 °C | 20,0 °C |
| Kinderzimmer 2 | 1 | Schlafraum | 18,0 °C | 20,0 °C |
| Kinderzimmer 3 | 1 | Schlafraum | 18,0 °C | 20,0 °C |
| Bad EG | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |
| Bad UG | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |
| Fitnessraum | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |
| Gäste | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |
| Saunaraum | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |
| Sommerküche | 2 | Aufenthaltsraum | 22,5 °C | 27,5 °C |

⚠️ **Bäder** würde ich abweichend höher fahren als die 22,5 °C des Standard-Aufenthaltsraums —
das ist eine bewusste Abweichung von der Loxone-Vorgabe, keine Vorgabe.

⚠️ **Fitnessraum** eher niedriger als 22,5 °C.
