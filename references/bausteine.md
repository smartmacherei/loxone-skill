# Loxone-Bausteinvorlagen — Konnektor-Referenz

Begleitdokument zu **[bausteinvorlagen.xml](bausteinvorlagen.xml)** — dort liegt je Bausteintyp
ein vollständiges XML-Muster, aus dem sich per Skript neue Instanzen erzeugen lassen.

**Stand:** 30.07.2026 · Loxone Config 17.1.7.27 · ControlList Version 273 · Objektversion `V="175"`

---

## Wie man eine Vorlage verwendet

1. Knoten aus `bausteinvorlagen.xml` klonen und in das Zieldokument importieren
2. `U` und **jede** `Co/@U` durch neue, projektweit eindeutige UUIDs ersetzen
3. `Title`, `Px`, `Py`, `Px2`, `Py2` setzen
4. In `<IoData>` die Attribute `Cr` (Kategorie), `Pr` (Raum), `Ugr`/`Ugx` (Benutzergruppe) setzen
5. Verbindungen als `<In Input="<Konnektor-UUID der Quelle>"/>` im Ziel-`<Co>` anlegen und
   dort `Nc` auf die Anzahl der `<In>` setzen
6. Knoten an die gewünschte `<C Type="Page">` anhängen, `NextObj` im Wurzelelement erhöhen

> **Verbindungen gelten nur seitenintern.** Seitenübergreifend braucht es `InputRef`/`OutputRef`.
> Und: **`InputRef.AQ` ist der Zustand, `InputRef.Q` der Fehlerausgang** — siehe
> [xml-bearbeitung.md](xml-bearbeitung.md).

---

## Logik- und Analogbausteine

### `AnalogThresholdTrigger` — Schwellwertschalter (Nio 8)
| Konnektor | Bedeutung | Default |
|---|---|---|
| `Input` | Eingangswert | – |
| `On` | Einschaltschwelle | 5 |
| `Off` | Ausschaltschwelle (Hysterese) | 1 |
| `Remanence` | Zustand über Neustart halten | – |
| `PulseTime` | Impulsdauer | 1 |
| `Q` | Ausgang | – |
| `RisingEdge` / `FallingEdge` | Impuls bei Über-/Unterschreiten | – |

⭐ **`On` und `Off` sind Konnektoren, keine reinen Parameter** — sie lassen sich also mit einem
anderen Signal speisen. Damit sind gleitende Schwellen möglich, z. B. Raumtemperatur gegen die
aktuelle Solltemperatur `ϑt` der Intelligenten Raumregelung.

### `Formula` — Formel (Nio 6)
`Input1` … `Input4` · Ausgänge `AQ` (Zahl) und `TQ` (Text).
Der Ausdruck steht im **Attribut `Formula`**, dazu `Valid="true|false"`.
Eingänge werden im Ausdruck als `I1`…`I4` angesprochen.

### `And` / `Or` — UND / ODER (Nio 3)
`I1`, `I2` → `Q`. **Nur zwei Eingänge.** Für mehr entweder kaskadieren (sicher) oder weitere
`Co K="I3"`… ergänzen und `Nio` entsprechend erhöhen (Muster wie bei `LightController2`, dort
`I1`…`I8`) — Letzteres ist plausibel, aber nicht verifiziert.

### Weitere vorhandene Bausteine
`OffDelay` · `OnDelay` · `Memory` (Merker, analogfähig: `Input` → `AQ`/`Q`) ·
`EdgeDetection` · `RSFlipFlop` · `SwitchingTimer` · `PulseAt` · `PushButton`

---

## Funktionsbausteine

| Typ | GUI-Name | Nio | Kernkonnektoren |
|---|---|---|---|
| `HeatIRoomController2` | Intelligente Raumregelung | 57 | `Temp`=ϑc · `Window`=Dwc · `Move`=P · `Reset`=Off · `TempO`=ϑo · `AQh`/`AQc`/`AQhc`=H/C/HC · `AQhc1`=HC1 · `Qs`=Shd · `AQt`=ϑt |
| `PresenceDetector` | Präsenz | 19 | `InputActivate`=Act · `InputExtend`=Ext · `InputTrigger`=AE · `DeviceActivate/Extend/Trigger` (nur Loxone-Geräte) · `ParamTOn`=Pet · `OutputActive`=P · `OutputPresence`=Pc (TechDoc 05.09.2026; bis dahin stand hier `OutputPresence`=P) |
| `LightController2` | Beleuchtungssteuerung | 75 | `Move`=Mo · `Presence`=P · `Brightness`=Br · `Sel1`…`Sel8` · `AQ1`…`AQ20` · `OutputReset` |
| `AutoJalousie` | Automatikbeschattung | 49 | `InputTrigger`=Tg · `EndUp`/`EndDown`=Co/Cc · `AutoShade`=**Sps** · `EnAutoShade`=DisSp · `ReactAutoShade`=Spr · `Safety`=**Wa** · `Window`=Dwc · `Dir` · `OutputUp`/`OutputDown` |
| `ToiletFan` | WC Lüftungssteuerung | 10 | `Trigger` · `Move` (Präsenz) · `Reset` · `Disable` · `AiringDelay` (180 s) · `MaxAiringDuration` (180 s) · `OutputActive`=S · `OutputFan`=Fan |
| `WindowsMonitor` | Fenster- und Türüberwachung | – | `W` (Kontakte) · `HI2` |
| `SmokeAlarm` | Brand-/Wassermeldezentrale | 27 | `InputAirDigitalS`/`W` · `InputAirAnalog` · Attribut `Objects` |
| `AlarmChain` | Alarmierungskette | – | `Alarm` · `Urgent` · `Text1` · `A1`…`A10` |
| `Alarm` | Alarmanlage | – | `ActiveDelay` · `ActiveDelayP` · `Inactive` · `HI1`…`HI4` · `Confirm` · `Q1`/`Q2`/`TQ` |
| `HVACController` | Heiz- und Kühlsteuerung | 38 | `Mode` · `OnThreshold`=Sot · `TempLimitH/C` · `FanDelay` · `TimePulseOn/Off` |
| `CentralLight` / `CentralShade` / `CentralGate` / `CentralPresence` | Zentralbausteine | – | Mitglieder im Attribut **`rec`** |
| `StairwayLS` | Treppenlichtschalter | – | `InputTrigger` → `Q` |
| `Doorcontroller` | Türsteuerung | – | – |
| `DayTimer` | Schaltuhr | – | – |

---

## Zuordnung ohne Verdrahtung

Diese Attribute ersetzen Verbindungen — sie entstehen in Config per **Doppelklick** auf den Baustein:

| Attribut | wo | Inhalt |
|---|---|---|
| `rec` | Zentralbausteine | UUIDs der Mitglieds-Raumbausteine |
| `Objects` | Meldezentrale, Fensterüberwachung, IRC→HVAC | UUIDs zugeordneter Geräte bzw. der Quelle |
| `DEVS` | Präsenz | UUIDs zugeordneter Loxone-Melder |
| `UUIDTimer` | Intelligente Raumregelung | verweist auf die integrierte Schaltuhr |

---

## Was noch fehlt

> **Vollständige, gegen die KB abgeglichene Fassung:** „Lücke 1" in
> [xml-doku-mapping.md](xml-doku-mapping.md) — **152 der 179 Doku-Bausteine haben keine
> Vorlage**, abgedeckt sind 27 (15 %). Die Liste unten ist der ältere, kürzere Auszug.

Für diese Typen liegt **keine** Vorlage vor — sie müssten bei Bedarf einmalig in Config eingefügt
und dann hier nachgetragen werden:

`Not` · `Vergleicher` · `Multiplexer` · `Statusbaustein` · `Zufallsgenerator` ·
`Pulsweitenmodulator` · `Windmesser` · `Ventilation` / `Leaf` (nur in `FactoryPresets.xml`) ·
`Jalousie` (einfach, ohne Automatik) · `Energiemanager` · `Wecker`

Dazu eine Lücke **innerhalb** der Vorlagendatei: `SwitchingTimer` ist zwar als Typ vorhanden,
hat aber **kein einziges `<Co>`-Kindelement und kein `Nio`** — als Zeitschalter unbrauchbar.
Stattdessen `DayTimer` (Schaltuhr) verwenden.

**Merke:** Bausteintypen, die weder im Projekt noch in `FactoryPresets.xml` vorkommen, lassen
sich nicht zuverlässig per XML erzeugen — Typname, Konnektorsatz und `Nio` sind nicht ableitbar.
Der Weg ist immer: einmal in Config einfügen, speichern, dann als Vorlage übernehmen.
