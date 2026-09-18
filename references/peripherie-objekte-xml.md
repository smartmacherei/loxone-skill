# Peripherie-Objekte im XML — Modbus, RS232/485, HTTP-/UDP-Eingang, IR

Die Attributsätze der Peripherieobjekte, **empirisch erhoben aus 701 Vorlagen der Loxone
Library** (18.09.2026, Config 17.2.8.28). Insgesamt 176.850 ausgewertete Attributvorkommen.

`VirtualOut` / `VirtualOutCmd` steht in [xml-bearbeitung.md](xml-bearbeitung.md) —
diese Datei ergänzt die übrigen Objekttypen. Woher die Vorlagen kommen und wie man weitere
holt: [library-loxone-com.md](library-loxone-com.md).

> **Was diese Datei ist und was nicht.** Die Attribute sind **beobachtet**, nicht aus einer
> Loxone-Spezifikation abgeschrieben — es gibt keine. Ein Attribut, das hier fehlt, kann
> trotzdem existieren; es kam in 701 Vorlagen nur nicht vor. Kennzeichnung durchgehend
> `[PROJEKT-BELEGT]`, sofern nicht anders vermerkt.

---

## 1. Modbus — 444 Vorlagen, 14.794 Befehle

### `<Modbus>` — das Gerät

| Attribut | Vorkommen | Beobachtete Werte |
|---|---|---|
| `Title` | 444 | Gerätename |
| `Comment` | 444 | meist leer |
| **`Channel`** | 444 | **Modbus-Adresse des Geräts.** `1` (297×), `2`, `3`, `10`, bis `255` |
| `Baudrate` | 257 | `9600` (151×), `19200` (76×), `38400`, `115200`, `57600`, `0` |
| `Parity` | 98 | `1` (95×), `0` |
| `Stopbits` | 64 | `1` (60×), `0` |
| `HintText` | 189 | Hinweistext, meist leer |
| `Usage` · `DevInfo` · `Manu` · `ProductCode` · `ProductVersion` | je 3 | in fast allen Vorlagen leer |

`Baudrate`/`Parity`/`Stopbits` fehlen bei **Modbus TCP** — sie gelten nur für RTU.
Fehlt `Baudrate`, ist die Vorlage für TCP gedacht.

### `<ModbusCmd>` — der einzelne Sensor/Aktor

Das mit Abstand häufigste Objekt der ganzen Library: **150.298 Attributvorkommen**.

| Attribut | Vorkommen | Bedeutung |
|---|---|---|
| **`ModbusCmd`** | 14.792 | **Funktionscode** — siehe Tabelle unten |
| **`ModbusAddress`** | 14.600 | Registeradresse |
| **`ModbusDataType`** | 6.564 | Datentyp + Flags — siehe unten. **Fehlt = Vorgabe** |
| `ModbusPollingCycle` | 10.664 | Abfragezyklus in s: `60` (3079×), `5` (2751×), `10`, `30`, `300`, `15` |
| `Analog` | 13.047 | `true` (11.433×) / `false` |
| `Sensor` | 13.047 | `true` = lesen (9606×) / `false` = schreiben (3441×) |
| `SourceValLow` / `SourceValHigh` | 723 / 11.001 | Quellbereich der Skalierung |
| `DestValLow` / `DestValHigh` | 765 / 11.000 | Zielbereich der Skalierung |
| `RepeatRate` | 1.380 | Wiederholrate beim Schreiben: `3600` (643×), `0`, `60` |
| `Unit` | 13.047 | Anzeigeformat, z. B. `<v.1>°C`, `<v>`, `<v.1>%` |
| `HintText` | 7.912 | Hinweis, oft die Registerbelegung: `0=OFF\r\n1=ON` |
| `ST` | 253 | `0` (247×), sonst `17`, `18`, `19` — **[OFFEN]** |
| `Documentation` | 170 | Freitext |

**Skalierung:** `SourceValLow/High` → `DestValLow/High` bildet den Rohwert auf den
Loxone-Wert ab. Der mit Abstand häufigste Fall ist `SourceValHigh=10` oder `100` auf
`DestValHigh=10`/`100`/`1` — also schlicht ein Faktor 1/10 oder 1/100 für Register, die
Zehntel oder Hundertstel liefern.

### `ModbusCmd` — die Funktionscodes

Alle acht beobachteten Werte, mit der Standard-Modbus-Bedeutung:

| Wert | Vorkommen | Modbus-Funktion |
|---:|---:|---|
| `3` | 5.518 | Read Holding Registers |
| `4` | 3.973 | Read Input Registers |
| `6` | 2.964 | Write Single Register |
| `16` | 863 | Write Multiple Registers |
| `5` | 619 | Write Single Coil |
| `1` | 561 | Read Coils |
| `2` | 283 | Read Discrete Inputs |
| `15` | 11 | Write Multiple Coils |

### `ModbusDataType` — Bitfeld aus Basistyp und Flags

**[VERIFIZIERT 18.09.2026]** an **allen 6.854 Vorkommen — jedes einzelne zerlegt sich
restlos**, kein Ausreißer:

```
ModbusDataType = Basistyp + Flags
```

| Basistyp | Bedeutung |
|---:|---|
| `0` | uint16 |
| `1` | int16 |
| `2` | uint32 |
| `3` | int32 |
| `4` | float32 |
| `6` | uint64 |
| `7` | int64 |
| `8` | double |

| Flag | Bedeutung |
|---:|---|
| `+32` | Registerreihenfolge tauschen (Word Swap) **[COMMUNITY]** |
| `+64` | **[OFFEN]** — kommt in 1.096 Fällen vor, auch auf 16-Bit-Typen. Loxone benennt es nirgends |
| `+128` | Byte-Reihenfolge tauschen (Byte Swap) **[COMMUNITY]** |

Beobachtete Kombinationen, absteigend: `1` (int16, 2508×) · `36` (float32 +32, 873×) ·
`32` (uint16 +32, 714×) · `34` (uint32 +32, 522×) · `100` (float32 +32+64, 457×) ·
`4` (float32, 312×) · `33` · `98` · `99` · `35` · `2` · `0` · `162` (uint32 +32+128) …

Die Basistypen stammen aus einer Forumsquelle
([loxforum](https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/400905-modbus-datentypen-in-template)),
**decken sich aber exakt mit den Daten**: es treten nur die acht dokumentierten Basiswerte
auf, `5` fehlt sowohl in der Quelle als auch in den Vorlagen. Dieselbe Quelle nennt
zusätzlich ein Flag `+16`, das in **keiner einzigen** der 701 Vorlagen vorkommt — und
nennt `+64` nicht, das sehr wohl vorkommt. Im Zweifel den Daten glauben.

---

## 2. RS232 / RS485 — `<Comm>` und `<CommCmd>`

38 Vorlagen (27× RS232 mit `templateType="5"`, 11× RS485 mit `templateType="6"`).

### `<Comm>` — die Schnittstelle

| Attribut | Vorkommen | Beobachtete Werte |
|---|---|---|
| `Baudrate` | 38 | `9600` (19×), `57600`, `115200`, `19200` |
| `Databits` | 38 | **immer `8`** |
| **`RS485`** | 13 | `true` (11×) / `false` — unterscheidet die beiden Bustypen im XML |
| `CycleUserProt` | 21 | `-1` (16×), sonst Zyklus in s |
| `Parity` | 3 | `0` / `1` |
| `Stopbits` | 2 | `0` |
| `EndChar` | 4 | `0`, `266`, `259` |
| `ChecksumType` | 4 | `0`, `4`, `5` |
| `UserProt` · `DataUserProt` | 1 / 2 | `1` bzw. `ASCII` |

Beachte: `RS485="true"` steht nur an 13 von 38 Objekten. **Verlässlich ist die
Unterscheidung nur über `templateType`** im `<Info>`-Element (5 = RS232, 6 = RS485).

### `<CommCmd>` — der Befehl (9.849 Attributvorkommen)

| Attribut | Bedeutung |
|---|---|
| `CmdOn` / `CmdOff` | zu sendende Zeichenfolge |
| `Analog` | Analog- statt Digitalbefehl |
| `Sensor` | lesen statt schreiben |
| `Text` | Textbefehl |
| `Signed` | Werteinterpretation mit Vorzeichen |
| `SourceValLow/High` · `DestValLow/High` | Skalierung, wie bei Modbus |
| `Unit` | Anzeigeformat |
| `ID` | Befehlskennung |
| `Title` · `Comment` · `HintText` | Beschriftung |

---

## 3. Virtueller HTTP-Eingang — `<VirtualInHttp>` / `<VirtualInHttpCmd>`

79 Vorlagen, 12.848 Attributvorkommen. Das ist der **Polling**-Weg: Der Miniserver holt
zyklisch eine URL und zerlegt die Antwort.

### `<VirtualInHttp>`

| Attribut | Vorkommen | Werte |
|---|---|---|
| `Address` | 79 | die abzufragende URL, z. B. `http://<ip_adress>/v1/data` |
| **`PollingTime`** | 79 | Sekunden: `10` (52×), `60` (7×), `120`, `3600` |

**10 Sekunden ist der De-facto-Standard.** Wer kürzer pollt, sollte wissen warum — jeder
Zyklus ist eine HTTP-Anfrage aus dem Miniserver heraus.

### `<VirtualInHttpCmd>` und `<VirtualInUdpCmd>`

Beide haben **denselben** Attributsatz, `VirtualInUdpCmd` zusätzlich `Address`:

| Attribut | Bedeutung |
|---|---|
| **`Check`** | **die Befehlserkennung** — das eigentliche Werkzeug |
| `Analog` | Analog- statt Digitalwert |
| `Signed` | Vorzeichenbehaftete Interpretation |
| `SourceValLow/High` · `DestValLow/High` | Skalierung |
| `DefVal` · `MinVal` · `MaxVal` | Vorgabe- und Grenzwerte |
| `Unit` | Anzeigeformat |
| `Title` · `Comment` · `HintText` | Beschriftung |

**`Check` in der Praxis.** Fast alle Vorlagen zerlegen JSON, und zwar mit demselben
Muster: zum Schlüssel springen, dann den Wert lesen.

```
\i"active_power_w":\i\v      →  liest den Zahlenwert hinter "active_power_w"
\i"P_Grid" : \i\v            →  Leerzeichen im JSON gehören mit in die Suchmaske
"cW":\v                      →  ohne Sprungmarke, wenn der Schlüssel eindeutig ist
```

`\i…\i` = springe zu diesem Text, `\v` = hier steht der Wert. Die vollständige Syntax
steht beim Baustein *Befehlserkennung* in
[bausteine-multimedia-kommunikation.md](bausteine-multimedia-kommunikation.md).

> **Falle:** Im XML ist der Wert **doppelt maskiert** — ein Anführungszeichen erscheint als
> `&quot;`, der Backslash bleibt stehen. Wer `Check` per Skript schreibt, muss die
> XML-Maskierung setzen, aber die Backslashes der Befehlserkennung **nicht** escapen.

### `<VirtualInUdp>`

Nur 5 Vorlagen. Attribute: `Address` (Absender, oft leer = beliebig) und **`Port`** —
beobachtet `7090`, `1234`, `32100`, `50222`. Kein `PollingTime`: UDP ist Push, das Gerät
schickt von sich aus.

---

## 4. IR — `<RC>`, `<RCkey>`, `<IRdata>`

25 Vorlagen. `<RC>` (die Fernbedienung) und `<RCkey>` (die Taste) tragen **nur `Title` und
`Comment`** — die eigentlichen Signaldaten stehen in den Kindelementen `<IRdata>`,
`<IRdataToggle>` (21 Vorlagen), `<RawPeriod>` und `<Period>`.

Das heißt: **IR-Vorlagen sind per Skript nicht sinnvoll zu erzeugen.** Die Nutzdaten sind
gemessene Pulsfolgen; ohne Originalfernbedienung oder fertige Vorlage gibt es nichts
abzuleiten. Hier lohnt der Blick in den Katalog besonders.

---

## 5. MP-Bus — `<template>` mit `<C>`-Objekten

13 Vorlagen (12× Belimo, 1× FIRVENA), `templateType="20"`. Als **einzige** Vorlagenart
enthalten sie echte `<C>`-Objekte: `<C Type="BelimoDevice">`, `<C Type="Online">` und
Kanäle mit den numerischen Typen `1`, `2` und `4`.

Die zugehörigen Fehlercodes (MP-Bus-Timeout, Parity, Adressierung, Gerätestörungen)
dokumentiert Loxone in `IOs_StatVal_Error.pdf` →
[techdoc-dokumente.md](techdoc-dokumente.md).

---

## 6. Wenn man eine Vorlage per Skript baut

Die Mindestbestandteile, aus allen 701 Vorlagen gleich:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Modbus Title="Gerät" Comment="" Channel="1" Baudrate="9600" Parity="1" Stopbits="1">
	<Info templateType="7" minVersion="12031214"/>
	<ModbusCmd Title="Vorlauftemperatur" Comment="" ModbusCmd="3" ModbusAddress="1"
	           ModbusDataType="1" ModbusPollingCycle="60" Analog="true" Sensor="true"
	           SourceValHigh="10" DestValHigh="1" Unit="&lt;v.1&gt;°C" HintText=""/>
</Modbus>
```

Verpacken als ZIP mit `desc.json` daneben ergibt eine `.LxAddon` →
[library-loxone-com.md](library-loxone-com.md) 2.

**Drei Dinge, die schiefgehen:**

1. **`templateType` passend zum Wurzelelement setzen.** Aus dem XML allein ist bei
   `<Comm>` nicht ableitbar, ob RS232 (`5`) oder RS485 (`6`) gemeint ist.
2. **`minVersion` nicht zu hoch setzen.** Gepacktes Config-Versionsformat
   (`12031214` = 12.3.12.14). Zu hoch = die Vorlage lässt sich nicht importieren.
3. **`Unit` enthält XML-Entities.** `&lt;v.1&gt;°C` ist der Normalfall, nicht `<v.1>°C`.

---

## Quellen

Erhoben am 18.09.2026 aus 701 `.LxAddon`-Vorlagen der Loxone Library
(`scripts/library_crawl.py --keep-tpl`), gegen Loxone Config 17.2.8.28.
Modbus-Basisdatentypen zusätzlich abgeglichen mit
[loxforum: MODBUS Datentypen in Template](https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/400905-modbus-datentypen-in-template).
