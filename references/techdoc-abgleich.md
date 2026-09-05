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

198 Katalogseiten, 191 einem TechDoc-LxType zugeordnet (3 davon über Namensähnlichkeit), 7 ohne Treffer.
**167 Bausteine stimmen in allen Kürzeln überein.** Abweichungen:

Unscharfe Namenstreffer: 2. Zähler & Speicher → Zähler für Speicher; 7. Impulszähler & Speicher → Impulszähler für Speicher; Binärdecoder → Binärdekoder

| Baustein | LxType | Kürzel nur im Katalog | Kürzel nur in TechDoc |
|---|---|---|---|
| 10. Spotpreis-Optimierer | `SpotOpt` | E:+0 to +23, E:+n to +n | E:%02d:00 to :00 |
| 3. HVAC Controller | `ClimateControllerUS` | A:O/B, A:W/W1, P:Δϑ | A:o/b, A:w/w1, P:∆ϑ |
| 6. Wallbox | `CarChargerDevice` | E:Cac, E:Cp, E:Ec, E:Ecp, E:Lm1-5, E:Ls, E:Mr, E:Off, E:Pm1-5, E:Pmm, E:R, E:Sm1-5, E:Uid, E:Vc, A:API, A:Ca, A:Cac, A:Ccc, A:Cclc, A:Cd, A:Clc, A:Cld, A:Clm, A:Cly, A:Cm, A:Cp, A:Cw, A:Cy, A:Lcl, A:Ls, A:M, A:Mr, A:Se, A:Ss, A:Tp, A:Uid, A:Vc, P:Cfp, P:Mro, P:Muv | – |
| Ablaufsteuerung | `SequenceController` | P:Intervall [ms], P:Konfiguration, P:Kurzbeschreibung | – |
| Audio Player | `MusicPlayer` | E:V-, A:V- | A:v |
| Audio Player Gruppe fix | `MPGroup` | E:V- | – |
| Audio Zentral | `CentralMusic` | E:AIs, E:Repeat, E:S+, E:Shuffle, E:Sleep, E:Stop, E:TTS, E:TgZ, E:V-, E:Zoff, E:Zon | – |
| Binärdecoder | `BinDecoder` | A:Bit 0-31 | A:bit  |
| Binärdekoder | `BinDecoder` | A:Bit 0-31 | A:bit  |
| Binärkodierer | `BinEncoder` | E:Bit 0-31 | E:bit  |
| Event Database Connector | `DbConE` | E:CI1-CI16 | E:ci1, E:ci10, E:ci11, E:ci12, E:ci13, E:ci14, E:ci15, E:ci16, E:ci2, E:ci3, E:ci4, E:ci5, E:ci6, E:ci7, E:ci8, E:ci9 |
| Größer (`Greater`) | `Greater` | P:V1-n | P:v |
| Kleiner (`Less`) | `Less` | P:V1-n | P:v |
| Licht Zentral | `CentralLight` | E:Lc1-n, E:M-, A:API | E:lc, E:m |
| Lichtsteuerung | `LightController2` | E:M- | E:m |
| Lichtsteuerung Gen 1 (`LightController`) | `LightController` | E:I1-n, E:S1-n, A:AQ1-n | E:i, E:s, A:aq |
| Lichtszene (`LightsceneLearn`) | `LightsceneLearn` | E:AIn, E:S1-n, A:AQ1-n | E:ai, E:s, A:aq |
| Mediensteuerung | `Media` | E:Ch-, E:V- | – |
| Music Server Zone | `MediaClient` | E:Song-, E:V-, P:Vt | E:song, E:v |
| Programm (Baustein) | `Code1` | E:I1-13, E:T1-3, A:Etxt, A:O1-13, A:Txt1-3 | – |
| Session Database Connector | `DbConS` | E:CI1-CI16 | E:ci1, E:ci10, E:ci11, E:ci12, E:ci13, E:ci14, E:ci15, E:ci16, E:ci2, E:ci3, E:ci4, E:ci5, E:ci6, E:ci7, E:ci8, E:ci9 |
| Stufenauswahl (`StepSel`) | `StepSel` | E:I1-n, A:O1-n | E:i, A:o |
| Szene | `Lightscene` | E:Act, E:Off, A:AQn | A:aq |
| Tastschalter | `PButtonT` | E:On, A:Off, A:On | – |

## C. Lücken

### Katalogseiten ohne TechDoc-Treffer

- BACnet (bausteine-system-schnittstellen.md) → kein Vorschlag
- Home Connect (bausteine-system-schnittstellen.md) → kein Vorschlag
- Merker (bausteine-logik-basis.md) → `AlarmClock` (Wecker), `LoxLIVE` (Miniserver)
- Multiplikator Projekt (bausteine-system-schnittstellen.md) → kein Vorschlag
- Netzwerk Interkommunikation (bausteine-system-schnittstellen.md) → kein Vorschlag
- SIA DC-09 (bausteine-sicherheit-alarm.md) → kein Vorschlag
- Trust (bausteine-sicherheit-alarm.md) → kein Vorschlag

26 Einträge ohne Konnektoren stehen als Tabelle in bausteine-geraete-erweiterungen.md.

### TechDoc-LxTypes ohne Katalogseite (0)

