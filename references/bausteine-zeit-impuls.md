# Zeit, Verzögerung & Impuls

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## 1. Einschaltverzögerung

Der Baustein schaltet den Ausgang zeitverzögert nach dem Eingang EIN.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Off / Lock: Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor einem Backup und einmal pro Stunde. Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Don | Delay duration | Der Ausgang wird um diese Dauer verzögert eingeschaltet. | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

## 2. Einschaltverzögerung speichernd

Ausgang schaltet nach Impuls am Eingang zeitverzögert EIN bis Reset.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Off / Lock: Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung-speichernd/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung-speichernd/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Don | Delay duration | Der Ausgang wird um diese Dauer verzögert eingeschaltet. | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung-speichernd/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/einschalt-verzoegerung-speichernd/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

## 3. Ausschaltverzögerung

Der Baustein schaltet den Ausgang zeitverzögert nach einer fallenden Flanke am Eingang aus.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tr | Trigger | Off / Lock. Pulse (< 200 ms): Ausgänge werden zurückgesetzt / ausgeschaltet. Pulse (> 200 ms): Baustein wird gesperrt. Dominierender Eingang. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ausschalt-verzoegerung/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ausschalt-verzoegerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde auf der SD. | – | 0/1 | 0 |
| Don | Delay duration | Verzögerungsdauer, bevor der Ausgang nach einer fallenden Flanke am Eingang ausgeschaltet wird. | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/ausschalt-verzoegerung/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/ausschalt-verzoegerung/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

## 4. Ein- und Ausschaltverzögerung

Zeitverzögertes Ein- und Ausschalten des Ausgangs.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Off / Lock - Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ein-und-auschalt-verzoegerung/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ein-und-auschalt-verzoegerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde auf der SD. | - | 0/1 | 0 |
| Don | Duration switch-on delay | Der Ausgang wird um diese Dauer verzögert eingeschaltet. | s | 0...∞ | 1 |
| Doff | Duration switch-off delay | Verzögerung bis der Ausgang, bei fallender Flanke an Trigger, auf AUS schaltet | s | ∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/ein-und-auschalt-verzoegerung/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/ein-und-auschalt-verzoegerung/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

## 5. Verzögerter Impuls

Liefert einen verzögerten Impuls am Ausgang, Dauer einstellbar.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse | Impuls | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/verzoegerter-impuls/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse | Impuls | 0/1 |

Quelle: https://www.loxone.com/dede/kb/verzoegerter-impuls/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Dd | Duration of delay | Dauer der Verzögerung | s | 0...∞ | 5 |
| Dp | Duration output pulse | Dauer Ausgangsimpuls | s | 0...∞ | 0,5 |

Quelle: https://www.loxone.com/dede/kb/verzoegerter-impuls/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/verzoegerter-impuls/

---

## 6. Flankengetriggertes Wischrelais

Gibt bei Eingangsimpuls eine parametrierbare Anzahl von Ausgangsimpulsen aus.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Off / Lock. Pulse (< 200 ms): Outputs reset/off. Pulse (> 200 ms): Block locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/flankengetriggertes-wischrelais/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse | Impuls | 0/1 |

Quelle: https://www.loxone.com/dede/kb/flankengetriggertes-wischrelais/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Wenn aktiv, behält der Baustein seinen letzten Zustand nach Miniserver-Neustart. Zustand wird gespeichert beim Speichern in den Miniserver, bei geplantem Neustart, vor Backup, einmal pro Stunde auf SD. | – | 0/1 | 0 |
| Don | Duration on | Dauer Ein | s | 0...∞ | 1 |
| Doff | Duration off | Dauer Aus | s | 0...∞ | 2 |
| C | Cycles | Anzahl der Impulse am Ausgang | – | 1...∞ | 10 |

Quelle: https://www.loxone.com/dede/kb/flankengetriggertes-wischrelais/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/flankengetriggertes-wischrelais/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

## 7. Impulsgeber

Liefert Impulse am Ausgang mit einstellbarer Ein/Aus Zeit.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |
| Inv | Invert | Invertiert den Ausgang (P) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsgeber/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse | Impuls | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsgeber/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Don | Duration On | Dauer Ein | s | 0.1...∞ | 1 |
| Doff | Duration Off | Dauer Aus | s | 0.1...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/impulsgeber/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/impulsgeber/

---

## 8. Impuls bei

Wertet am T-Eingang einen Text mithilfe von benutzerdefinierten Suchbegriffen aus. Wenn eines der Suchmuster im Text enthalten ist, gibt der Ausgang (P) einen Impuls mit der eingestellten Länge aus.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| T | Text | Text | - |

Quelle: https://www.loxone.com/dede/kb/impuls-bei/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse when search pattern is found | Impuls bei gefundenem Suchmuster | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impuls-bei/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Pd | Pulse Duration | Impulsdauer | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/impuls-bei/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Suchmuster 1 | Die beiden Wildcards '*' und '?' können verwendet werden ('*' = beliebig lange Folge beliebiger Zeichen, '?' = beliebiges Zeichen). Bsp.: '??sch*' trifft zu bei 'Tasche', aber auch bei 'Tischtennis' | - |
| Suchmuster 2 | Identische Funktionsbeschreibung wie Suchmuster 1 | - |
| Suchmuster 3 | Identische Funktionsbeschreibung wie Suchmuster 1 | - |
| Suchmuster 4 | Identische Funktionsbeschreibung wie Suchmuster 1 | - |

Quelle: https://www.loxone.com/dede/kb/impuls-bei/

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/impuls-bei/

---

## 9. Impuls um

Liefert einen Impuls mit einstellbarer Dauer zu festgelegten Zeitpunkten wie Uhrzeit, Datum, Sonnenaufgang oder regelmäßigen Intervallen.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off / Lock | Puls (< 200 ms): Ausgänge werden zurückgesetzt / ausgeschaltet. Puls (> 200 ms): Baustein wird gesperrt. Dominierender Eingang. Puls (> 500 ms): Der Name des verbundenen Sensors wird in der Benutzeroberfläche verwendet. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Aktiviert den Ausgang zum festgelegten Zeitpunkt für die im Parameter (Don) eingestellte Dauer. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|--------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. | - | 0/1 | 0 |
| Don | On-duration of output (O) | Ein Dauer von Ausgang (O) | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Impuls | Auswahl, wann der Impuls ausgegeben werden soll. | - |
| Uhrzeit | Uhrzeit, an der der Impuls ausgegeben wird. Eingabeformat hh:mm:ss | - |
| Einmaliger Impuls | Einmaliger Impuls an einem bestimmten Datum. Nur für bestimmte Zeitfunktionen verfügbar. Wenn nicht angehakt, wird der Impuls jeden Tag bzw. bei jeder Aktivierung der ausgewählten Zeitfunktion ausgegeben. | - |

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/impuls-um-2/

---

## 10. Treppenlicht-Schalter

Lichtschalter-Baustein für Treppenhäuser mit einstellbarer Zeitschaltuhr und Vorwarnfunktion.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Schaltet Ausgang (O) für die Dauer von (Don) ein. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| On | On | Schaltet Ausgang (O) ein. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/treppenlicht-schalter/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

Quelle: https://www.loxone.com/dede/kb/treppenlicht-schalter/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern, geplanten Neustart, vor Backup und einmal pro Stunde. Daten werden auf SD gespeichert. | - | 0/1 | 0 |
| Don | On-duration of output (O) | Ein-Dauer von Ausgang (O) wenn durch Eingang (Tr) aktiviert. | s | 0...∞ | 180 |
| Tw | Switch-off warning time | Die Ausschaltvorwarnung wird um diese Zeit vor Ausschalten von (O) aktiv. | s | 0...∞ | 15 |
| Dw | Switch-off warning duration | Ausschaltvorwarnung Dauer | s | 0...∞ | 0,5 |

Quelle: https://www.loxone.com/dede/kb/treppenlicht-schalter/

### Eigenschaften

[OFFEN] Keine detaillierte Eigenschaften-Tabelle in der Dokumentation angegeben. Hinweis: Der Baustein verfügt über eine Anwesenheitssimulation, die im Eigenschaftenfenster aktiviert werden kann.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/treppenlicht-schalter/

---

## 11. Schaltuhr

Tagesunabhängige Zeitschaltuhr mit frei einstellbaren Schaltzeiten und Betriebsmodi. Die Schaltuhr kann digital (Ein/Aus) oder analog verwendet werden.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Act | Activate | Wenn bei einem Eintrag 'Aktivierung notwendig' gewählt ist, wird dieser nur mit einem zusätzlichen Impuls an diesem Eingang aktiviert, solange der Eintrag aktiv ist. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| O | Output | Digital: 0 oder 1 Analog: Standardwert oder Wert des Eintrags. | – | ∞ |
| Om | Number of active operating mode | Nummer des aktiven Betriebsmodus. | – | ∞ |
| On | Pulse when On | Impuls bei Ein | – | 0/1 |
| Off | Pulse when Off | Impuls bei Aus | – | 0/1 |
| Rt | Remaining time | Verbleibende Zeit eines in der Visualisierung gestarteten Timers. | s | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | – | – |

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Die Daten werden auf der SD gespeichert. | – | 0/1 | 0 |
| Am | Automatic mode | 0 = automatisch 1 = manuell über Parameter (Mm) | – | 0/1 | 0 |
| Mm | Manual mode | Stellt den Betriebsmodus manuell ein. | – | ∞ | 0 |
| Don | On-duration of output (O) | Wenn 'Aktivierung notwendig' gewählt ist, ist die Dauer, in der der Wert an (O) ausgegeben wird, auf diese Zeit begrenzt. 0=deaktiviert | s | 0...∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Schaltzeiten | Schaltzeiten, die für die zeitabhängige Zutrittskontrolle an Berechtigungsbausteinen zum Einsatz kommen. Änderungen wirken sich auf alle Benutzer und Benutzergruppen aus, die für die Verwendung dieser Schaltzeit konfiguriert sind. | – |
| Als Digitalausgang verwenden | Wenn aktiviert, wird der Analogausgang als Digitalausgang verwendet. | – |
| Bezeichnung für Aktiv | Dieser Text wird in den APPs statt 'Aktiv' ausgegeben | – |
| Bezeichnung für Inaktiv | Dieser Text wird in den APPs statt 'Inaktiv' ausgegeben | – |

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/schaltuhr/

---

## 12. Langzeitklick

Mehrfachbelegung eines Tasters mit bis zu 4 Funktionen durch Unterscheidung der Klick-Dauer.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Wertebereich |
|--------|------------------|--------------|
| Tr | Trigger | 0/1 |
| R | Reset | 0/1 |

Quelle: https://www.loxone.com/dede/kb/langzeitklick/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O1 | Pulse when (Tr) ≤ (TI) | Impuls wenn (Tr) ≤ (TI) | 0/1 |
| O2 | Pulse when (TI) ≤ (Tr) ≤ 2x(TI) | Impuls wenn (TI) ≤ (Tr) ≤ 2x(TI) | 0/1 |
| O3 | Pulse when 2x(TI) ≤ (Tr) ≤ 3x(TI) | Impuls wenn 2x(TI) ≤ (Tr) ≤ 3x(TI) | 0/1 |
| O4 | Pulse when 3x(TI) ≤ (Tr) | Impuls wenn 3x(TI) ≤ (Tr) | 0/1 |
| V | Value (V1-4), depending on time of input (Tr) | Wert (V1-V4), abhängig der Zeit an Eingang (Tr) | ∞ |

Quelle: https://www.loxone.com/dede/kb/langzeitklick/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert: beim Speichern, bei geplanten Neustarts, vor Backups, einmal pro Stunde. Daten werden auf SD gespeichert. | - | 0/1 | 0 |
| TI | Interval | Intervall | s | 0...∞ | 0,35 |
| D | Duration output pulse | Dauer Ausgangsimpuls | s | 0...∞ | 0,1 |
| V1 | Value 1 | Wert 1 | - | ∞ | 1 |
| V2 | Value 2 | Wert 2 | - | ∞ | 2 |
| V3 | Value 3 | Wert 3 | - | ∞ | 3 |
| V4 | Value 4 | Wert 4 | - | ∞ | 4 |

Quelle: https://www.loxone.com/dede/kb/langzeitklick/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/langzeitklick/

---

## 13. Mehrfachklick

Mehrfachbelegung eines Tasters mit bis zu 4 Funktionen. Der Programmbaustein Mehrfachklick unterscheidet, ob ein Taster 1-fach, 2-fach, 3-fach oder 4-fach betätigt wurde.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Sendet je nach Anzahl der Klicks einen Impuls an den Ausgang (1C-4C). | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/mehrfachklick/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| 1C | Pulse on single-click | Impuls bei Einfachklick für die im Parameter (On) eingestellte Dauer. | 0/1 |
| 2C | Pulse on double-click | Impuls bei Doppelklick für die im Parameter (On) eingestellte Dauer. | 0/1 |
| 3C | Pulse on triple-click | Impuls bei Dreifachklick für die im Parameter (On) eingestellte Dauer. | 0/1 |
| 4C | Pulse on quad-click | Impuls bei Vierfachklick für die im Parameter (On) eingestellte Dauer. | 0/1 |
| V | Value triggered output | Gibt den Wert (V1c-V4c) des ausgelösten Ausgangs aus. | ∞ |

Quelle: https://www.loxone.com/dede/kb/mehrfachklick/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | 0/1 | 0 |
| Tmc | Time multi-click | Maximale Zeit zwischen zwei Impulsen, die als Mehrfachklick zählen. | s | 0...∞ | 0,35 |
| On | On-duration of output (1C-4C) | Ein Dauer von Ausgang (1C-4C) | s | 0...∞ | 0,1 |
| V1c | Value for single-click | Wert für Einfachklick | – | ∞ | 1 |
| V2c | Value for double-click | Wert für Doppelklick | – | ∞ | 2 |
| V3c | Value for triple-click | Wert für Dreifachklick | – | ∞ | 3 |
| V4c | Value for quad-click | Wert für Vierfachklick | – | ∞ | 4 |

Quelle: https://www.loxone.com/dede/kb/mehrfachklick/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/mehrfachklick/

---

## 14. Zufallsgenerator

Erstellt zufällige Werte in einem beliebigen Wertebereich.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| C | Creates a random value | Erzeugt einen Zufallswert | 0/1 |
| DisPc | Disable periphery control | Sperrt (C) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/zufallsgenerator/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Wertebereich |
|--------|------------------|--------------|
| Ran | Zufallswert | ∞ |

Quelle: https://www.loxone.com/dede/kb/zufallsgenerator/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Min | Minimum value | Minimum Wert | ∞ | 0 |
| Max | Maximum value | Maximum Wert | ∞ | 10 |

Quelle: https://www.loxone.com/dede/kb/zufallsgenerator/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/zufallsgenerator/

---

## 15. Zufallssteuerung

Erzeugt zufällige Ein- und Ausschaltverzögerung. Bleibt der Eingang (En) für eine zufällige Dauer zwischen 0 und dem Parameter (Son) aktiv, wird (Ran) aktiviert.

### Eingaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| En | Enable | Aktivieren | 0/1 |

Quelle: https://www.loxone.com/dede/kb/zufallssteuerung/

### Ausgaenge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Ran | Random output | Zufallswert Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/zufallssteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Son | Maximum duration switch-on delay | Eingangsparameter - maximale Dauer der Einschaltverzögerung | s | 0...∞ | 100 |
| Soff | Maximum duration switch-off delay | Eingangsparameter - maximale Dauer der Ausschaltverzögerung | s | 0...∞ | 10 |

Quelle: https://www.loxone.com/dede/kb/zufallssteuerung/

### Eigenschaften

[OFFEN] Keine Eigenschaften-Tabelle in der Dokumentation angegeben.

### Fallstricke

Keine Warnhinweise oder Achtung-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/zufallssteuerung/

---

## Zusammenfassung

Alle 15 Bausteine der Kategorie "Zeit, Verzögerung & Impuls" wurden vollständig recherchiert und dokumentiert. Alle Quellen stammen aus der offiziellen Loxone-Dokumentation (KB) und sind mit [BELEGT] gekennzeichnet.

### Erfolgreich abgerufene Bausteine (15/15):
1. Einschaltverzögerung ✓
2. Einschaltverzögerung speichernd ✓
3. Ausschaltverzögerung ✓
4. Ein- und Ausschaltverzögerung ✓
5. Verzögerter Impuls ✓
6. Flankengetriggertes Wischrelais ✓
7. Impulsgeber ✓
8. Impuls bei ✓
9. Impuls um ✓
10. Treppenlicht-Schalter ✓
11. Schaltuhr ✓
12. Langzeitklick ✓
13. Mehrfachklick ✓
14. Zufallsgenerator ✓
15. Zufallssteuerung ✓

### Besonderheiten:
- Alle Kürzel sind exakt aus der Dokumentation übernommen (inkl. Sonderzeichen)
- Beim Baustein "Impuls bei" ist die Eingänge-Tabelle minimal (nur T-Eingang), da der Baustein primär textbasiert arbeitet
- Bei einigen Bausteinen gibt es erweiterte Eingänge wie "API Connector" im Ausgang (z. B. Schaltuhr, Treppenlicht-Schalter, Impuls um)
- Eigenschaften-Tabellen waren nicht bei allen Bausteinen vorhanden; hier wurde [OFFEN] oder die verfügbaren Daten eingetragen
- Keine kritischen Warnhinweise oder Einschränkungen in der KB dokumentiert
