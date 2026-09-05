# TechDoc-Abgleich (generiert von scripts/techdoc_abgleich.py)

## A. xml-doku-mapping.md gegen TechDoc

431 Zuordnungen bestätigt, **0 abweichend**, 2 XML-Namen ohne TechDoc-Konnektor. Nur Abweichungen gelistet.

| LxType | XML-Konnektor | Kürzel Skill | Kürzel TechDoc | Befund |
|---|---|---|---|---|
| `Memory` | – | – | – | LxType nicht in TechDoc |
| `CentralLight` | `OutputAPI` | `API` | – | nicht in TechDoc (Eigenschaft statt Konnektor?) |
| `AutoJalousie` | `WP` | `Wap` | – | nicht in TechDoc (Eigenschaft statt Konnektor?) |
| `SwitchingTimer` | – | – | – | LxType nicht in TechDoc |

## B. Katalog (bausteine-*.md) gegen TechDoc

121 Katalogseiten, 117 einem TechDoc-LxType zugeordnet (2 davon über Namensähnlichkeit), 4 ohne Treffer.
**52 Bausteine stimmen in allen Kürzeln überein.** Abweichungen:

Unscharfe Namenstreffer: 2. Zähler & Speicher → Zähler für Speicher; 7. Impulszähler & Speicher → Impulszähler für Speicher

| Baustein | LxType | Kürzel nur im Katalog | Kürzel nur in TechDoc |
|---|---|---|---|
| 1. Addierer | `Add` | – | A:o, P:v |
| 1. Einschaltverzögerung | `OnDelay` | – | E:off, E:tr, A:o |
| 1. Raumlüftungssteuerung | `Ventilation` | – | P:hmin |
| 1. Zähler | `MeterAbsUni` | – | A:rlw, A:rw |
| 10. MinMax | `Minmax` | – | E:off, A:max, A:min, P:v |
| 10. Spotpreis-Optimierer | `SpotOpt` | E:+0 to +23 | E:%02d:00 to :00 |
| 10. Treppenlicht-Schalter | `StairwayLS` | – | E:dispc, E:off, E:on, E:tr, A:api, A:o |
| 11. MinMax seit Reset | `TimeMinmax` | – | E:r, E:v, A:max, A:min, P:rem |
| 11. Power Supply & Backup (Baustein) | `PowerUnit` | – | A:rst |
| 11. Schaltuhr | `DayTimer` | – | E:act, E:off, E:rtd, A:api, A:o, A:off, A:om, A:on, A:rt |
| 12. Analog MinMax-Begrenzer | `AMinmax` | – | E:v, A:v, P:max, P:min |
| 12. Langzeitklick | `LongClick` | – | E:r, E:tr, A:o1, A:o2, A:o3, A:o4, A:v |
| 13. Mehrfachklick | `MultiClick` | – | E:off, E:tr, A:1c, A:2c, A:3c, A:4c, A:v |
| 13. Mittelwert | `Average` | – | A:avg, P:v |
| 14. Gleitender Mittelwert | `Avg` | – | E:r, E:v, A:avg, P:c, P:n, P:rem |
| 14. Zufallsgenerator | `Rand` | – | E:c, E:dispc, A:ran |
| 15. Analogwahlschalter | `AnalogMultiplexer2` | – | E:off, E:v1, E:v2, A:v, P:sel |
| 15. Zufallssteuerung | `RandomGen` | – | E:en, A:ran |
| 16. Analogwahlschalter 4-fach | `AnalogMultiplexer` | – | E:off, E:v, A:v, P:sel |
| 17. Analogwertvalidierung | `Validator` | – | E:en, E:v, A:e, A:v, P:d, P:max, P:min, P:tmc |
| 18. Analogwertüberwachung | `AnalogWatchdog` | – | E:off, E:v, A:te, P:rem, P:tl, P:tu |
| 19. Schwellwertschalter | `AnalogThresholdTrigger` | – | E:v, A:o, A:off, A:on, P:pd, P:rem, P:voff, P:von |
| 2. Addierer 4 | `Add4` | – | A:o, P:v |
| 2. Einschaltverzögerung speichernd | `RetOnDelay` | – | E:off, E:tr, A:o |
| 20. Differenzschwellwertschalter | `AnalogDiffTrigger` | – | E:v, A:t, A:teoff, A:teon, P:d, P:rem, P:t |
| 21. Rampensteuerung | `Ramp` | – | E:off, E:s, E:st, A:v, P:l1, P:l2, P:rem, P:sts, P:sv |
| 22. Pulsweitenmodulator | `PWM` | – | E:off, E:v, A:pwm, P:p |
| 23. Stepper | `AnalogStepper` | – | E:off, E:s, A:v, P:dir, P:m, P:rem, P:sts |
| 3. Ausschaltverzögerung | `OffDelay` | – | E:off, E:tr, A:o |
| 3. Energiemonitor | `Fronius` | – | E:errtx |
| 3. Subtrahierer | `Sub` | – | A:o, P:v |
| 4. Ein- und Ausschaltverzögerung | `OnOffDelay` | – | E:off, E:tr, A:o |
| 4. Energieflussmonitor | `EFM` | – | A:sc, A:yt |
| 4. Internorm Lüfter | `VentInternorm` | – | P:hmin |
| 4. Multiplizierer | `Mult` | – | A:o, P:v |
| 5. Dividierer | `Div` | – | A:o, P:v1, P:v2 |
| 5. Verzögerter Impuls | `OnPulseDelay` | – | E:off, E:p, A:p |
| 6. Flankengetriggertes Wischrelais | `EdgeWipingRelay` | – | E:off, E:tr, A:p |
| 6. Impulszähler | `MeterPUni` | – | A:rlw, A:rw |
| 6. Modulo | `Mod` | – | A:dec, A:int, P:v |
| 6. Wallbox | `CarChargerDevice` | E:Cac, E:Cp, E:Ec, E:Ecp, E:Lm1-5, E:Ls, E:Mr, E:Off, E:Pm1-5, E:Pmm, E:R, E:Sm1-5, E:Uid, E:Vc, A:API, A:Ca, A:Cac, A:Ccc, A:Cclc, A:Cd, A:Clc, A:Cld, A:Clm, A:Cly, A:Cm, A:Cp, A:Cw, A:Cy, A:Lcl, A:Ls, A:M, A:Mr, A:Se, A:Ss, A:Tp, A:Uid, A:Vc, P:Cfp, P:Mro, P:Muv | – |
| 7. Ganzzahl | `Int` | – | A:r, P:ro, P:v |
| 7. Impulsgeber | `PulseGen` | – | E:inv, E:off, A:p |
| 8. Formel | `Formula` | – | A:e, A:r, P:i |
| 8. Impuls bei | `PulseBy` | – | E:t, A:p |
| 9. Festwertzähler | `MeterDig` | – | A:rlw, A:rw |
| 9. Impuls um | `PulseAt` | – | E:off, A:api, A:o |
| 9. Klimaanlagen Zentralsteuerung | `HvacAC` | – | E:cm, A:m, P:dm |
| 9. Skalierer | `AnalogScaler` | – | E:v, A:sv, P:sv1, P:sv2, P:v1, P:v2 |
| Ablaufsteuerung | `SequenceController` | P:Intervall [ms], P:Konfiguration, P:Kurzbeschreibung | – |
| Automatik-Regel | `AutopilotRule` | – | E:i, A:a |
| Baustein 1: Lichtsteuerung | `LightController2` | – | E:alarm, E:br, E:buzzer, E:disp, E:dispc, E:lc, E:m, E:m+, E:mbr, E:mo, E:mood, E:off, E:on, E:p, E:rtd, E:t5/, A:2c, A:3c, A:api, A:lc, A:m, P:afi, P:ao, P:brt, P:dm, P:fbu, P:ft, P:lv, P:maxabr, P:maxbr, P:maxct, P:met, P:minbr, P:minct, P:mmd, P:moet, P:pm, P:pto, P:rem, P:str, P:sts, P:tdc |
| Baustein 2: Licht Zentral | `CentralLight` | – | E:alarm, E:buzzer, E:disp, E:dispc, E:lc, E:m, E:m+, E:mood, E:off, E:on, E:rtd, E:t5/, A:na |
| Baustein 3: Hotel Lichtsteuerung | `LightControllerH` | – | E:air, E:dis, E:dismo, E:i, E:ic, E:id, E:is, E:mo, E:r, E:s10, E:s11, E:s12, E:s13, A:aq, A:aqrm, A:aqs, A:qd, A:qp, A:qs, P:l, P:m, P:max, P:min, P:ms, P:rem, P:si, P:st, P:th, P:tl, P:tm, P:to |
| Baustein 4: Dimmer | `PushDimmer` | – | E:+, E:dispc, E:off, E:set, E:tg, A:api, A:d, A:s, P:di, P:dm, P:lv, P:maxd, P:mind, P:rem, P:str, P:sts |
| Baustein 5: EIB Dimmer | `EibDimmer` | – | E:+, E:cdv, E:dispc, E:off, E:on, E:s, E:set, A:api, A:cdv, A:d, A:s, P:rr, P:sts |
| Baustein 6: RGB Lichtszene | `LightsceneRGB` | – | E:+, E:ai, E:ais, E:dis, E:o, E:r, A:aqa, A:aqb, A:aqg, A:aqr, A:aqs, P:rem |
| Baustein 7: Konstantlichtregler | `BrightnessControl` | – | E:act, E:br, E:off, E:set, A:api, A:lc, P:hys, P:sts, P:tb |
| Baustein 8: Szene | `Lightscene` | – | E:+, E:ais, E:dis, E:r, A:api, A:aq, A:aqs, P:rem |
| Composite-Fensterkontakt | `JoinWindowSensor` | – | A:o |
| Event Database Connector | `DbConE` | E:CI1-CI16 | E:ci1, E:ci10, E:ci11, E:ci12, E:ci13, E:ci14, E:ci15, E:ci16, E:ci2, E:ci3, E:ci4, E:ci5, E:ci6, E:ci7, E:ci8, E:ci9 |
| Programm (Baustein) | `Code1` | E:I1-13, E:T1-3, A:Etxt, A:O1-13, A:Txt1-3 | E:ai, A:aq, A:teq |
| Session Database Connector | `DbConS` | E:CI1-CI16 | E:ci1, E:ci10, E:ci11, E:ci12, E:ci13, E:ci14, E:ci15, E:ci16, E:ci2, E:ci3, E:ci4, E:ci5, E:ci6, E:ci7, E:ci8, E:ci9 |
| Tastschalter | `PButtonT` | E:On, A:Off, A:On | P:rem |
| Touch Pure Flex Controller | `TpfController` | – | E:dis, E:dl |

## C. Lücken

### Katalogseiten ohne TechDoc-Treffer

- BACnet (bausteine-system-schnittstellen.md) → kein Vorschlag
- Home Connect (bausteine-system-schnittstellen.md) → kein Vorschlag
- Multiplikator Projekt (bausteine-system-schnittstellen.md) → kein Vorschlag
- Netzwerk Interkommunikation (bausteine-system-schnittstellen.md) → kein Vorschlag

### TechDoc-LxTypes ohne Katalogseite (104)

- `2Point` — 2-Punkt-Regler
- `3Point` — 3-Punkt-Regler
- `AMemory` — Analogspeicher
- `AalEmergency` — Notfall Alarm
- `AalSmartAlarm` — AAL Smart Alarm
- `Access` — Berechtigung
- `Alarm` — Alarmanlage
- `AlarmChain` — Alarmierungskette
- `AnalogComparator` — Analogkomparator
- `And` — UND
- `AudioServer` — Audioserver
- `AutomaticScene` — Szene
- `BinDecoder` — Binärdekoder
- `BinEncoder` — Binärkodierer
- `CallGen` — Call Generator
- `CentralAlarm` — Alarmanlage Zentral
- `CentralMusic` — Audio Zentral
- `CentralPresence` — Präsenz Zentral
- `ClimateControllerUS` — HVAC Controller
- `CmdRecognition` — Befehlserkennung
- `Code16` — Programm
- `Code4` — Programm
- `Code8` — Programm
- `Comm1wire` — 1-Wire Extension
- `Comm232` — RS232 Extension
- `Comm485` — RS485 Extension
- `CommDMX` — DMX Extension
- `DaylightController` — Tageslicht Steuerung (BETA)
- `DbConT` — Datenbank
- `Device Tablet` — Device Tablet
- `Devicemonitor` — DeviceMonitor
- `DewPoint` — Taupunktrechner
- `EdgeDetection` — Flankenerkennung
- `Energy` — Verbrauchszähler
- `Equal` — Gleich
- `Fan` — Lüftersteuerung (veraltet)
- `FlipFlop` — RS Selbsthalteschalter
- `Greater` — Größer
- `GreaterEqual` — Größer oder gleich
- `HVACController` — Heiz- und Kühlsteuerung
- `HeatCentral` — Zentralheizung (BETA)
- `HeatIRoomController2` — Intelligente Raumregelung
- `Heatcurve` — Heizkurve
- `Heatmixer` — Heizungsmischer
- `Heatmixer2` — Vorlauftemperatur Rechner
- `IRcontroller` — IR Steuerung
- `IRoomcontrol` — Intelligente Raumregelung Gen 1
- `Intercom` — Sprechanlage
- `IntercomDevice` — Gegensprechanlage
- `JalousieUpDown2` — Jalousie
- `Less` — Kleiner
- `LessEqual` — Kleiner oder gleich
- `LightController` — Lichtsteuerung Gen 1
- `LightsceneLearn` — Lichtszene
- `LoxAin` — AI Extension Gen. 1
- `LoxAout` — AO Extension
- `LoxDIMM` — Dimmer Extension
- `LoxDigin` — DI Extension
- `LoxKnx` — KNX Extension
- `LoxLIVE` — Miniserver
- `LoxMORE` — Extension
- `LoxOCEAN` — EnOcean Extension
- `MBusExtension` — M-Bus Extension
- `MPGroup` — Audio Player Gruppe fix
- `MailBox` — Post- und Paketkasten
- `MailGen` — Mail Generator
- `Media` — Medien-Steuerung
- `MediaClient` — Music Server Zone
- `MessageCenter` — Systemstatus
- `ModbusServer` — Modbusserver
- `Monoflop` — Monoflop
- `MusicPlayer` — Audio Player
- `NfcCodeTouch` — Berechtigung NFC Code Touch
- `Not` — NICHT
- `NotEqual` — Ungleich
- `Or` — ODER
- `PI` — PI-Regler
- `PID` — PID-Regler
- `Plugin` — Plugin (In Development)
- `Power` — Power
- `Presence` — Visualisierungs-Präsenz
- `PresenceController` — Präsenzmelder (veraltet)
- `PresenceDetector` — Präsenz
- `RSFlipFlop` — RS-Impulsschalter
- `Roomcontrol` — Raumregelung
- `SRFlipFlop` — SR-Impulsschalter
- `SchuecoExtension` — Schüco Extension
- `Shift` — Schieberegister
- `SmokeAlarm` — Brand- und Wassermeldezentrale
- `Solarpumpcontrol` — Solarregelung
- `SonnenBatteryDevice` — Sonnen Batteriespeicher
- `State` — Status
- `StateV` — Virtueller Status
- `StatusMonitor` — Status Monitor
- `StepSel` — Stufenauswahl
- `SystemScheme` — Anlagenschema
- `TPDC` — Touch Pure Display Controller
- `Text` — Notiz
- `TextGenerator` — Text Generator
- `Tracker` — Tracker
- `Wallbox` — Wallbox
- `WeatherServer` — Wetterserver
- `Weed` — Viking iMow
- `Xor` — Exklusiv ODER
