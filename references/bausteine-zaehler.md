# Zähler
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## 1. Zähler

Dieser Baustein erfasst den Verbrauch oder die Lieferung verschiedener Medien wie Strom, Gas, Wasser und Wärme durch Auslesen physischer Zähler. Die Werte können zusammen mit anderen Zählerbausteinen im Energieflussmonitor verknüpft werden.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Wird nur dieser Eingang verwendet, wird daraus auch der Zählerstand berechnet. Ansonsten wird er nur für den Ausgang (Pf) und die Visualisierung verwendet. | 0...∞ |
| Mr | Meter reading | Eingang für Zähler, die den Zählerstand direkt als Analogwert senden. Für Zähler, die nur Teilmengen senden (z.B. Smart Socket), ist in den Einstellungen des Bausteins die Relativzählung zu aktivieren. | 0...∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Mro | Meter reading offset | Wert wird zum Ausgang (Mr) hinzugefügt. | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Leistung oder Durchfluss | 0...∞ |
| Mr | Meter Reading | Zählerstand | 0...∞ |
| Rd | Reading today | Zählerstand heute | 0...∞ |
| Rld | Reading yesterday | Zählerstand gestern | 0...∞ |
| Rm | Reading this month | Zählerstand dieses Monats | 0...∞ |
| Rlm | Reading last month | Zählerstand letzter Monat | 0...∞ |
| Ry | Reading this year | Zählerstand dieses Jahr | 0...∞ |
| Rly | Reading last year | Zählerstand letztes Jahr | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/zaehler/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Relativzählung | Aktiv: Der ausgelesene Zähler sendet nur Teilmengen in Intervallen (relativ), der Baustein zählt zusammen und bildet daraus den Zählerstand. Nicht aktiv: Der ausgelesene Zähler sendet selbst seinen Gesamtzählerstand (absolut), der Baustein bildet diesen nur ab. | - |
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/zaehler/
- Dokumentation erwähnt: "Zählerstand und Einheiten" — Pf/Mr-Einheiten müssen unabhängig wählbar sein. Bei alleiniger Nutzung von Pf müssen die Einheiten stundenbezogen und größenordnungsmäßig übereinstimmend sein (z.B. Pf=kW, Mr=kWh).
- "Erkennung ungültiger Zählerstände" — Der Baustein erkennt fehlerhafte Datenübertragung und ignoriert sinkende oder auf 0 springende Werte sowie "unrealistisch stark steigende" Werte.

Quelle: https://www.loxone.com/dede/kb/zaehler/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Rw | `ORw` | Ausgang | Reading this week | Zählerstand diese Woche | ≥ 0 |
| Rlw | `ORlw` | Ausgang | Reading last week | Zählerstand letzte Woche | ≥ 0 |

---

## 2. Zähler & Speicher

Dieser Baustein integriert einen Speicher und erfasst dessen Füllstand, Ladung und Entladung durch Auslesen physischer Zählerwerte oder des Speichers selbst.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Wird nur dieser Eingang verwendet, wird daraus auch der Zählerstand berechnet. Ansonsten wird er nur für den Ausgang (Pf) und die Visualisierung verwendet. | ∞ |
| Mrd | Meter reading Discharge | Eingang Entladen für Zähler, die den Zählerstand direkt als Analogwert senden. Für Zähler, die nur Teilmengen senden (z.B. Smart Socket), ist in den Einstellungen des Bausteins die Relativzählung zu aktivieren. | 0...∞ |
| Mrc | Meter reading Charge | Eingang Laden für Zähler, die den Zählerstand direkt als Analogwert senden. Für Zähler, die nur Teilmengen senden (z.B. Smart Socket), ist in den Einstellungen des Bausteins die Relativzählung zu aktivieren. | 0...∞ |
| Slvl | Storage level or state of charge | Speicher- oder Ladestand | ∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/zaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Mrod | Meter reading offset discharge | Zählerstand Offset Entladen | ∞ | 0 |
| Mroc | Meter reading offset charge | Zählerstand Offset Laden | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Positiver Wert: Der Speicher wird entladen. Negativer Wert: Der Speicher wird geladen. | ∞ |
| Mrd | Meter Reading discharge | Zählerstand Entladen | 0...∞ |
| Rdd | Reading today discharge | Zählerstand Entladen heute | 0...∞ |
| Rldd | Reading yesterday discharge | Zählerstand Entladen gestern | 0...∞ |
| Rmd | Reading this month discharge | Zählerstand Entladen dieser Monat | 0...∞ |
| Rlmd | Reading last month discharge | Zählerstand Entladen letzter Monat | 0...∞ |
| Ryd | Reading this year discharge | Zählerstand Entladen dieses Jahr | 0...∞ |
| Rlyd | Reading last year discharge | Zählerstand Entladen letztes Jahr | 0...∞ |
| Mrc | Meter Reading charge | Zählerstand Laden | 0...∞ |
| Rdc | Reading today charge | Zählerstand Laden heute | 0...∞ |
| Rldc | Reading yesterday charge | Zählerstand Laden gestern | 0...∞ |
| Rmc | Reading this month charge | Zählerstand Laden dieser Monat | 0...∞ |
| Rlmc | Reading last month charge | Zählerstand Laden letzter Monat | 0...∞ |
| Ryc | Reading this year charge | Zählerstand Laden dieses Jahr | 0...∞ |
| Rlyc | Reading last year charge | Zählerstand Laden letztes Jahr | 0...∞ |
| Slvl | Storage level or state of charge | Speicher- oder Ladestand | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/zaehler-speicher/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Leistung/Durchfluss Richtung | Gibt an, ob der physikalische Zähler den Lade- oder Entladewert als positiven oder negativen Wert an den Eingang Pf des Bausteins liefert. | - | - |
| Maximaler Speicherstand | Maximaler Speicherstand, der für die Visualisierung verwendet wird | 0...∞ | 100 |
| Relativzählung | Aktiv: Der ausgelesene Zähler sendet nur Teilmengen in Intervallen (relativ), der Baustein zählt zusammen und bildet daraus den Zählerstand. Nicht aktiv: Der ausgelesene Zähler sendet selbst seinen Gesamtzählerstand (absolut), der Baustein bildet diesen nur ab. | - | - |
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/zaehler-speicher/
- Die Dokumentation enthält wichtige Informationen unter "Zählerstand und Einheiten" sowie "Erkennung ungültiger Zählerstände" zu beachten.

Quelle: https://www.loxone.com/dede/kb/zaehler-speicher/

---

## 3. Zähler Bidirektional

Der bidirektionale Zähler erfasst Verbrauch und Lieferung verschiedener Medien wie Strom, Gas, Wasser oder Wärme durch Auslesen eines physischen Zählers. Zusammen mit anderen Zählerbausteinen ermöglicht er eine Gesamtdarstellung im Energieflussmonitor.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Wird nur dieser Eingang verwendet, wird daraus auch der Zählerstand berechnet. Ansonsten wird er nur für den Ausgang (Pf) und die Visualisierung verwendet. | ∞ |
| Mrc | Meter reading Consumption | Verbrauchseingang für Zähler, die den Zählerstand direkt als Analogwert senden. Für Zähler, die nur Teilmengen senden (z.B. Smart Socket), ist in den Einstellungen des Bausteins die Relativzählung zu aktivieren. | 0...∞ |
| Mrd | Meter reading Delivery | Liefereingang für Zähler, die den Zählerstand direkt als Analogwert senden. Für Zähler, die nur Teilmengen senden (z.B. Smart Socket), ist in den Einstellungen des Bausteins die Relativzählung zu aktivieren. | 0...∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/zaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Mroc | Meter reading offset consumption | Wert wird zum Ausgang (Mrc) hinzugefügt. | ∞ | 0 |
| Mrod | Meter reading offset delivery | Wert wird zum Ausgang (Mrd) hinzugefügt. | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/zaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Positiver Wert: Energie wird verbraucht. Negativer Wert: Energie wird geliefert. | ∞ |
| Mrc | Meter Reading consumption | Zählerstand Verbrauch | 0...∞ |
| Rdc | Reading today consumption | Zählerstand Verbrauch heute | 0...∞ |
| Rldc | Reading yesterday consumption | Zählerstand Verbrauch gestern | 0...∞ |
| Rmc | Reading this month consumption | Zählerstand Verbrauch dieses Monats | 0...∞ |
| Rlmc | Reading last month consumption | Zählerstand Verbrauch letzter Monat | 0...∞ |
| Ryc | Reading this year consumption | Zählerstand Verbrauch dieses Jahr | 0...∞ |
| Rlyc | Reading last year consumption | Zählerstand Verbrauch letztes Jahr | 0...∞ |
| Mrd | Meter Reading delivery | Zählerstand Lieferung | 0...∞ |
| Rdd | Reading today delivery | Zählerstand Lieferung heute | 0...∞ |
| Rldd | Reading yesterday delivery | Zählerstand Lieferung gestern | 0...∞ |
| Rmd | Reading this month delivery | Zählerstand Lieferung dieses Monats | 0...∞ |
| Rlmd | Reading last month delivery | Zählerstand Lieferung letzter Monat | 0...∞ |
| Ryd | Reading this year delivery | Zählerstand Lieferung dieses Jahr | 0...∞ |
| Rlyd | Reading last year delivery | Zählerstand Lieferung letztes Jahr | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/zaehler-bidirektional/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Leistung/Durchfluss Richtung | Gibt an, ob die Lieferung oder der Verbrauch als positiver oder negativer Wert vom physischen Zähler an den Pf Eingang des Bausteins übergeben wird. | - |
| Relativzählung | Aktiv: Der ausgelesene Zähler sendet nur Teilmengen in Intervallen (relativ), der Baustein zählt zusammen und bildet daraus den Zählerstand. Nicht aktiv: Der ausgelesene Zähler sendet selbst seinen Gesamtzählerstand (absolut), der Baustein bildet diesen nur ab. | - |
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/zaehler-bidirektional/
- "Zählerstand und Einheiten: Pf/Mr-Einheiten müssen unabhängig wählbar sein. Bei alleiniger Nutzung von Pf müssen die Einheiten stundenbezogen und größenordnungsmäßig übereinstimmend sein (z.B. Pf=kW, Mr=kWh)."
- "Erkennung ungültiger Zählerstände: Der Baustein erkennt fehlerhafte Datenübertragung und ignoriert sinkende oder auf 0 springende Werte sowie "unrealistisch stark steigende" Werte."

Quelle: https://www.loxone.com/dede/kb/zaehler-bidirektional/

---

## 4. Aufwärtszähler

Einfacher Zähler mit Endwert- und Rücksetzfunktion. Der Zähler beginnt erst wieder von vorne, wenn ein Impuls an (Off) erfolgt oder (M) auf 0 gesetzt wird.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/aufwaertszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| C | Count | Impuls erhöht (V) um 1. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/aufwaertszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Daten werden auf SD gespeichert. | 0/1 | 0 |
| L | Limit | Grenzwert | ∞ | 1000 |
| M | 0 = counter loops automatically, 1 = counter stops at limit | 0 = Zähler beginnt automatisch neu, 1 = Zähler stoppt beim Limit | 0/1 | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/aufwaertszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Lr | 1 when (V) = (L) | 1 wenn (V) = (L) | 0/1 |
| V | Counter value | Zählerwert | ∞ |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/aufwaertszaehler/
- Im Originaltext sind keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen vorhanden, die über die bereits genannte Hinweisfunktion hinausgehen.

Quelle: https://www.loxone.com/dede/kb/aufwaertszaehler/

---

## 5. Auf/Abwärts-Zähler

Ein Baustein, der mit jedem Impuls den Zählerwert um 1 erhöht oder verringert und dabei eine Richtungsvorgabe beachtet.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/aufabwaerts-zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| C | Count | Mit jedem Impuls wird der Zähler um 1 erhöht/verringert | 0/1 |
| Dir | Direction | 0 = aufwärts, 1 = abwärts | 0/1 |
| R | Reset | Bei 1 (O) = 0 und (V) = (Sv) | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/aufabwaerts-zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | "Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart" (Speicherung beim Speichern, geplanten Neustart, vor Backup, einmal pro Stunde auf SD) | 0/1 | 0 |
| Sv | Start value | Startwert des Zählerwertes | ∞ | 0 |
| Von | On-value | Ein-Wert | ∞ | 10 |
| Voff | Off-value | Aus-Wert | ∞ | 5 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/aufabwaerts-zaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Schaltet in Abhängigkeit vom Parameter (Von) & (Voff) | 0/1 |
| V | Counter value | Zählerwert | ∞ |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/aufabwaerts-zaehler/
- Keine Warnhinweise, Achtung- oder Hinweis-Boxen im Dokument vorhanden.

Quelle: https://www.loxone.com/dede/kb/aufabwaerts-zaehler/

---

## 6. Impulszähler

Dieser Zähler erfasst Impulse physischer Zähler mit Impulsausgang (S0) zur Messung von Verbrauch oder Lieferung verschiedener Medien wie Strom, Gas, Wasser oder Wärme.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge. | 0/1 |
| F | Frequency | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge, welche als Frequenzzähler verwendet werden. | 0...∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Np | Number of pulses per unit | Impulse pro Einheit | 0...∞ | 1000 |
| Mro | Meter reading offset | Wert wird zum Ausgang (Mr) hinzugefügt. | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Leistung oder Durchflussrate. Wird berechnet aus der Zeit von Impuls zu Impuls und Parameter Np. Impulsabstand <= 10 Sekunden: Aktualisierung und Berechnung durch jeden Impuls. Impulsabstand > 10 Sekunden: Aktualisierung alle 10 Sekunden, Berechnung eines Mittelwerts. | 0...∞ |
| Mr | Meter Reading | Zählerstand | 0...∞ |
| Rd | Reading today | Zählerstand heute | 0...∞ |
| Rld | Reading yesterday | Zählerstand gestern | 0...∞ |
| Rm | Reading this month | Zählerstand dieses Monats | 0...∞ |
| Rlm | Reading last month | Zählerstand letzter Monat | 0...∞ |
| Ry | Reading this year | Zählerstand dieses Jahr | 0...∞ |
| Rly | Reading last year | Zählerstand letztes Jahr | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/impulszaehler/
- Im bereitgestellten Inhalt waren keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen vorhanden.

Quelle: https://www.loxone.com/dede/kb/impulszaehler/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Rw | `ORw` | Ausgang | Reading this week | Zählerstand diese Woche | ≥ 0 |
| Rlw | `ORlw` | Ausgang | Reading last week | Zählerstand letzte Woche | ≥ 0 |

---

## 7. Impulszähler & Speicher

Der Baustein erfasst Impulse eines physischen Zählers (S0) zur Überwachung von Speichern. Er misst Füllstand, Ladung und Entladung und kann mit anderen Zählerbausteinen im Energieflussmonitor verknüpft werden.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Pd | Pulse discharge | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge. | 0/1 |
| Pc | Pulse charge | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge. | 0/1 |
| Fd | Frequency discharge | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge, welche als Frequenzzähler verwendet werden. | 0...∞ |
| Fc | Frequency charge | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge, welche als Frequenzzähler verwendet werden. | 0...∞ |
| Slvl | Storage level or state of charge | Speicher- oder Ladestand | ∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Npd | Number of pulses per unit | Impulse pro Einheit | 0...∞ | 1000 |
| Npc | Number of pulses per unit | Impulse pro Einheit | 0...∞ | 1000 |
| Mrod | Meter reading offset discharge | Zählerstand Offset Entladen | ∞ | 0 |
| Mroc | Meter reading offset charge | Zählerstand Offset Laden | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-speicher/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Pf | Power or flow | Aktuelle Leistung/Durchfluss berechnet mit Eingängen (Pd) und (Fd) wird als positiver Wert ausgegeben. Aktuelle Leistung/Durchfluss berechnet mit Eingängen (Pc) und (Fc) wird als negativer Wert ausgegeben. | ∞ |
| Mrd | Meter Reading discharge | Zählerstand Entladen | 0...∞ |
| Rdd | Reading today discharge | Zählerstand Entladen heute | 0...∞ |
| Rldd | Reading yesterday discharge | Zählerstand Entladen gestern | 0...∞ |
| Rmd | Reading this month discharge | Zählerstand Entladen dieser Monat | 0...∞ |
| Rlmd | Reading last month discharge | Zählerstand Entladen letzter Monat | 0...∞ |
| Ryd | Reading this year discharge | Zählerstand Entladen dieses Jahr | 0...∞ |
| Rlyd | Reading last year discharge | Zählerstand Entladen letztes Jahr | 0...∞ |
| Mrc | Meter Reading charge | Zählerstand Laden | 0...∞ |
| Rdc | Reading today charge | Zählerstand Laden heute | 0...∞ |
| Rldc | Reading yesterday charge | Zählerstand Laden gestern | 0...∞ |
| Rmc | Reading this month charge | Zählerstand Laden dieser Monat | 0...∞ |
| Rlmc | Reading last month charge | Zählerstand Laden letzter Monat | 0...∞ |
| Ryc | Reading this year charge | Zählerstand Laden dieses Jahr | 0...∞ |
| Rlyc | Reading last year charge | Zählerstand Laden letztes Jahr | 0...∞ |
| Slvl | Storage level or state of charge | Speicher- oder Ladestand | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-speicher/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|--------------|--------------|
| Maximaler Speicherstand | Maximaler Speicherstand, der für die Visualisierung verwendet wird | 0...∞ | 100 |
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-speicher/
- Keine explizit gekennzeichneten Warnhinweise, Achtung- oder Hinweisboxen in der Quelle vorhanden.

Quelle: https://www.loxone.com/dede/kb/impulszaehler-speicher/

---

## 8. Impulszähler Bidirektional

Dieser bidirektionale Zähler erfasst Verbrauch und Lieferung verschiedener Medien (Strom, Gas, Wasser, Wärme) über Impulse von physischen Zählern mit S0-Impulsausgang.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Pc | Pulse consumption | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge. | 0/1 |
| Pd | Pulse delivery | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge. | 0/1 |
| Fc | Frequency consumption | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge, welche als Frequenzzähler verwendet werden. | 0...∞ |
| Fd | Frequency delivery | Für Zähler mit Impulsausgang (S0), angeschlossen an digitale Eingänge, welche als Frequenzzähler verwendet werden. | 0...∞ |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Npc | Number of pulses per unit | Impulse pro Einheit | 0...∞ | 1000 |
| Npd | Number of pulses per unit | Impulse pro Einheit | 0...∞ | 1000 |
| Mroc | Meter reading offset consumption | Wert wird zum Ausgang (Mrc) hinzugefügt. | ∞ | 0 |
| Mrod | Meter reading offset delivery | Wert wird zum Ausgang (Mrd) hinzugefügt. | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-bidirektional/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Pf | Power or flow | Aktuelle Leistung/Durchfluss berechnet mit Eingängen (Pc) und (Fc) wird als positiver Wert ausgegeben. Aktuelle Leistung/Durchfluss berechnet mit Eingängen (Pd) und (Fd) wird als negativer Wert ausgegeben. | ∞ |
| Mrc | Meter Reading consumption | Zählerstand Verbrauch | 0...∞ |
| Rdc | Reading today consumption | Zählerstand Verbrauch heute | 0...∞ |
| Rldc | Reading yesterday consumption | Zählerstand Verbrauch gestern | 0...∞ |
| Rmc | Reading this month consumption | Zählerstand Verbrauch dieses Monats | 0...∞ |
| Rlmc | Reading last month consumption | Zählerstand Verbrauch letzter Monat | 0...∞ |
| Ryc | Reading this year consumption | Zählerstand Verbrauch dieses Jahr | 0...∞ |
| Rlyc | Reading last year consumption | Zählerstand Verbrauch letztes Jahr | 0...∞ |
| Mrd | Meter Reading delivery | Zählerstand Lieferung | 0...∞ |
| Rdd | Reading today delivery | Zählerstand Lieferung heute | 0...∞ |
| Rldd | Reading yesterday delivery | Zählerstand Lieferung gestern | 0...∞ |
| Rmd | Reading this month delivery | Zählerstand Lieferung dieses Monats | 0...∞ |
| Rlmd | Reading last month delivery | Zählerstand Lieferung letzter Monat | 0...∞ |
| Ryd | Reading this year delivery | Zählerstand Lieferung dieses Jahr | 0...∞ |
| Rlyd | Reading last year delivery | Zählerstand Lieferung letztes Jahr | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-bidirektional/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/impulszaehler-bidirektional/
- Im Dokument finden sich keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen.

Quelle: https://www.loxone.com/dede/kb/impulszaehler-bidirektional/

---

## 9. Festwertzähler

Der Festwertzähler berechnet Zählerstand aus der Einschaltdauer für Verbraucher oder Erzeuger mit konstanter Leistung bzw. konstantem Durchfluss, ohne physischen Zähler installieren zu müssen.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/festwertzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | State | Wenn 1, wird der Wert des Parameters (Pf) am Ausgang (Pf) ausgegeben, und der Zähler läuft. | 0/1 |
| R | Reset | Impuls: Zählerausgänge werden zurückgesetzt. Ein: Baustein ist gesperrt. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/festwertzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Mro | Meter reading offset | Wert wird zum Ausgang (Mr) hinzugefügt. | ∞ | 0 |
| Pf | Power rating or nominal flow | Nennleistung od. Durchfluss | 0...∞ | 1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/festwertzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pf | Power or flow | Leistung oder Durchfluss | ∞ |
| Mr | Meter Reading | Zählerstand | 0...∞ |
| Rd | Reading today | Zählerstand heute | 0...∞ |
| Rld | Reading yesterday | Zählerstand gestern | 0...∞ |
| Rm | Reading this month | Zählerstand dieses Monats | 0...∞ |
| Rlm | Reading last month | Zählerstand letzter Monat | 0...∞ |
| Ry | Reading this year | Zählerstand dieses Jahr | 0...∞ |
| Rly | Reading last year | Zählerstand letztes Jahr | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/festwertzaehler/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/festwertzaehler/
- Keine Warnhinweise, Achtung-Boxen oder Hinweis-Boxen im Dokument vorhanden.

Quelle: https://www.loxone.com/dede/kb/festwertzaehler/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Rw | `ORw` | Ausgang | Reading this week | Zählerstand diese Woche | ≥ 0 |
| Rlw | `ORlw` | Ausgang | Reading last week | Zählerstand letzte Woche | ≥ 0 |

---

## 10. Betriebszeitzähler

Der Betriebszeitzähler implementiert eine Gesamtbetriebszeitmessung und Wartungsintervalle. "Solange der Eingang (En) eingeschaltet ist, wird die Zeit gemessen."

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/betriebszeitzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| En | Enable | Die Zähler laufen, wenn Ein. | 0/1 |
| Rmc | Reset maintenance counter | Setzt den Wartungszähler auf den Parameter Mi zurück. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/betriebszeitzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Tu | Time unit | 0=Sekunden 1=Minuten 2=Stunden 3=Tage Bezieht sich nur auf die analogen Ausgänge, nicht auf die Visualisierung! | 0...3 | 0 |
| Mi | Maintenance interval | Baustein: Wert wird in Sekunden angegeben Eigenschaftsfenster: 1d12:00:00.000 (Tage, Stunden, Minuten, Sekunden, Ms) 0 = Ausgang (Me) wird nicht verwendet. | ∞ | 0 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/betriebszeitzaehler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Me | Maintenance interval exceeded | Wartungsintervall überschritten | 0/1 |
| To | Total operating time | Gesamtbetriebszeit | ∞ |
| Lst | Last start time | Letzte Startzeit | ∞ |
| Rtm | Remaining time maintenance | Verbleibende Zeit bis zum Erreichen des Wartungsintervalls. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

### Fallstricke
[BELEGT] https://www.loxone.com/dede/kb/betriebszeitzaehler/
- Im Quelltext sind keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen vorhanden.

Quelle: https://www.loxone.com/dede/kb/betriebszeitzaehler/

---

## Zusammenfassung

Alle 10 Bausteine aus der Kategorie "Zähler" wurden vollständig dokumentiert:
1. Zähler [BELEGT]
2. Zähler & Speicher [BELEGT]
3. Zähler Bidirektional [BELEGT]
4. Aufwärtszähler [BELEGT]
5. Auf/Abwärts-Zähler [BELEGT]
6. Impulszähler [BELEGT]
7. Impulszähler & Speicher [BELEGT]
8. Impulszähler Bidirektional [BELEGT]
9. Festwertzähler [BELEGT]
10. Betriebszeitzähler [BELEGT]

Stand: 30.07.2026
