# Bedienung, Taster & Oberfläche
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## ### Taster

Kurzpulsiger oder gedruckter Eingang schaltet einen Ausgang für eine einstellbare Dauer ein. Weitere Impulse verlängern die Aktivität.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Schaltet den Ausgang (O) für die in Parameter (Don) eingestellte Dauer ein. Ein weiterer Impuls verlängert die Einschaltdauer. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert Eingänge (Tr), (Off) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ein für die in Parameter (Don) eingestellte Dauer. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | 0/1 | 0 |
| Don | On-duration of output (O) | 0 = Ausgang (O) bleibt aktiv, solange die Taste gedrückt wird. | s | 0...∞ | 0,3 |

### Eigenschaften [OFFEN]
Keine Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine zusätzlichen Warnhinweise, Achtung-Boxen oder Hinweis-Boxen im Originaldokument.

---

## ### Tastschalter

Schalter mit Flankenerkennung, erzeugt kurze Impulse bei steigender und fallender Flanke des Triggers.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tastschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Impuls schaltet den Ausgang (O) für die in Parameter (Don) eingestellte Dauer ein. | 0/1 |
| Off | Off | Schaltet den Ausgang (O) aus. Permanent 1 = Sperrt den Baustein. | 0/1 |
| On | On | Schaltet Ausgang (O) ein. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tr), (Off), (On), wenn Ein. (z.B. Kindersicherung, Reinigung) | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tastschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Impuls bei jeder Flanke am Eingang (Tr) für die in Parameter (Don) eingestellte Dauer. | 0/1 |
| Off | Falling edge input (Tr) | Impuls bei fallender Flanke am Eingang (Tr) für Parameter (Don). | 0/1 |
| On | Rising edge input (Tr) | Impuls bei steigender Flanke am Eingang (Tr) für Parameter (Don). | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | \- |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tastschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Don | On-duration of outputs (O), (Off), (On) | Einschaltdauer der Ausgänge (O), (Aus), (Ein) | s | 0...∞ | 0,02 |

### Eigenschaften [OFFEN]
Keine Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Rem | `Remanence` | Parameter | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – |

---

## ### Schalter

Bistabiler Schalter mit Ein-/Aus-Steuereingängen und Toggle-Funktionalität. Speichert seinen Zustand nach Neustart.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/schalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Schaltet Ausgang (O) ein / aus. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| On | Switches output (O) on. | Schaltet Ausgang (O) ein. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/schalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |
| Off | Pulse when output (O) is switched off. | Impuls, wenn Ausgang (O) ausgeschaltet wird. | 0/1 |
| On | Pulse when output (O) is switched on. | Impuls, wenn Ausgang (O) eingeschaltet wird. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/schalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

### Eigenschaften [OFFEN]
Keine Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## ### 2 Tasten

Zwei separate Ein-/Aus-Steuereingänge für einen Ausgang. Ähnlich zwei separaten Tastschaltern, ohne Toggle.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-tasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Son | Switch on | Schaltet Ausgang (O) ein. | 0/1 |
| Soff | Switch off | Schaltet Ausgang (O) aus. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-tasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | \- |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-tasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

### Eigenschaften [OFFEN]
Keine Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine explizit gekennzeichneten Warn-, Achtungs- oder Hinweis-Boxen dokumentiert.

---

## ### 2 Auswahltasten

Werteselektor mit Plus/Minus-Eingängen und direktem Wert-Zugang. Minimal 1, maximal 10 Schritte voreingestellt.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-auswahltasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| + | Value+ | Erhöht den Wert am Ausgang (O) um die Schrittweite (Sts). | 0/1 |
| − | Value− | Verringert den Wert am Ausgang (O) um die Schrittweite (Sts). | 0/1 |
| V | Set value | Setzt einen bestimmten Wert an Ausgang (O). | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Output (O) is reset to the default value (Vdef). Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-auswahltasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | − |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/2-auswahltasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | − | 0/1 | 0 |
| Vmin | Minimum value | Minimum Wert | − | ∞ | 1 |
| Vmax | Maximum value | Maximum Wert | − | ∞ | 10 |
| Sts | Step size | Schrittweite | − | ∞ | 1 |
| Rr | Repetition rate | Ein langer Klick auf (+) / (−) erhöht / verringert den Wert am Ausgang (O) alle (Rr) Sekunden. | s | 0...∞ | 0,2 |
| Vdef | Default value | Standardwert, wenn der Eingang (Off) ausgelöst wird. | − | ∞ | 1 |

### Eigenschaften [OFFEN]
Keine Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine zusätzlichen Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## ### Auswahltaste

Werteselektor mit Plus-Eingang und direktem Wert-Zugang. Werte zirkulieren nach oben (von Vmax zu Vmin).

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/auswahltaste/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| + | Value+ | Erhöht den Wert am Ausgang (O) um die Schrittweite (Sts). Nachdem (Vmax) erreicht ist, wird wieder bei (Vmin) begonnen. | 0/1 |
| Val | Set value | Setzt einen bestimmten Wert an Ausgang (O). | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Output (O) is reset to the default value (Vdef). Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/auswahltaste/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/auswahltaste/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Vmin | Minimum value | Minimum Wert | - | ∞ | 1 |
| Vmax | Maximum value | Maximum Wert | - | ∞ | 10 |
| Sts | Step size | Schrittweite | - | ∞ | 1 |
| Rr | Repetition rate | Langer Klick auf (+) erhöht den Wert am Ausgang (O) alle (Rr) Sekunden. | s | 0...∞ | 0,2 |
| Vdef | Default value | Standardwert, wenn der Eingang (Off) ausgelöst wird. | - | ∞ | 1 |

### Eigenschaften [OFFEN]
Keine separaten "Eigenschaften"-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## ### Radiotasten

8-fache Radiobutton-Gruppe. Nur ein Ausgang kann zur Zeit aktiv sein. Auswahl erfolgt über separate Eingänge oder zyklisch.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| I1-8 | Input 1-8 | Schaltet den jeweiligen Ausgang 1-8 auf Ein | 0/1 |
| + | Next output | Nächster Ausgang | 0/1 |
| - | Previous output | Vorheriger Ausgang | 0/1 |
| Sel | Select output | Schaltet auf einen bestimmten Ausgang | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| O1-8 | Output 1-8 | Ausgang 1-8 | 0/1 |
| N | Number of active output | Nummer des aktiven Ausgangs | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| Max | Max. outputs | Maximale Anzahl der wählbaren Ausgänge. Beispiel: Max=4 -> nur die Ausgänge 1-4 können über Bausteineingänge aktiviert werden. In der Visualisierung können unabhängig von dieser Einstellung alle beschrifteten Ausgänge aktiviert werden. | 1...8 | 8 |
| Sk0 | Skip 0 | 'Alles-Aus' (0) wird beim Durchschalten mit +/- übersprungen, wenn Ein. Gilt nur für Objekteingänge, nicht für die Tasten in der Visualisierung. | 0/1 | 0 |

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Ausgänge bearbeiten | Bezeichnungen der Ausgänge bearbeiten | - |

### Fallstricke [BELEGT]
Keine separaten Warn-, Achtungs- oder Hinweis-Boxen im Dokument vorhanden.

---

## ### Radiotasten 16 Eingänge

16-fache Radiobutton-Gruppe. Nur ein Ausgang kann zur Zeit aktiv sein. Auswahl über 16 separate Eingänge oder zyklisch.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten-16-eingaenge/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I1-16 | Input 1-16 | Schaltet den jeweiligen Ausgang 1-16 auf Ein. | 0/1 |
| + | Next output | Nächster Ausgang | 0/1 |
| − | Previous output | Vorheriger Ausgang | 0/1 |
| Sel | Select output | Schaltet auf einen bestimmten Ausgang. | 0...16 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten-16-eingaenge/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O1-16 | Output 1-16 | Ausgang 1-16 | 0/1 |
| N | Number of active output | Nummer des aktiven Ausgangs | 0...16 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | − |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten-16-eingaenge/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| Max | Max. outputs | Maximale Anzahl der wählbaren Ausgänge. Beispiel: Max=4 -> nur die Ausgänge 1-4 können über Bausteineingänge aktiviert werden. In der Visualisierung können unabhängig von dieser Einstellung alle beschrifteten Ausgänge aktiviert werden. | 1...16 | 16 |
| Sk0 | Skip 0 | 'Alles-Aus' (0) wird beim Durchschalten mit +/- übersprungen, wenn Ein. Gilt nur für Objekteingänge, nicht für die Tasten in der Visualisierung. | 0/1 | 0 |

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/radiotasten-16-eingaenge/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Ausgänge bearbeiten | Bezeichnungen der Ausgänge bearbeiten | − |

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen im Dokument vorhanden.

---

## ### Komfortschalter

Schalter mit zeitgesteuerten Impulsen und automatischer Ausschaltvorwarnung. Toggle und Langklick für Dauerbetrieb.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/komfortschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Impuls am Eingang schaltet Ausgang (O) für die in Parameter (Don) eingestellte Dauer ein. Ein weiterer Impuls schaltet den Ausgang (O) wieder aus. Langer Klick = Schaltet den Ausgang (O) dauerhaft ein. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| On | On | Schaltet den Ausgang (O) ein. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/komfortschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | – |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/komfortschalter/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | 0/1 | 0 |
| Don | On-duration of output (O) on pulse | Ein-Dauer von Ausgang (O) bei Impuls | s | 0...∞ | 180 |
| Tlc | Time long-click for continious-on | Definiert die Dauer eines langen Klicks, um den Ausgang (O) über den Eingang (Tr) dauerhaft einzuschalten. | s | 0...∞ | 0,5 |
| Tw | Switch-off warning time | Die Ausschaltvorwarnung wird um diese Zeit vor Ausschalten von (O) aktiv. | s | 0...∞ | 15 |
| Dw | Switch-off warning duration | Ausschaltvorwarnung Dauer | s | 0...∞ | 0,5 |

### Eigenschaften [OFFEN]
Keine separaten Eigenschaften-Tabelle im Dokument vorhanden. Anwesenheitssimulation erwähnt als aktivierbar über Eigenschaftenfenster.

### Fallstricke [BELEGT]
Keine separaten Warn-, Achtung- oder Hinweis-Boxen dokumentiert. Anwesenheitssimulation ist über Eigenschaftenfenster aktivierbar.

---

## ### Touch Pure Flex Controller

Schnittstelle zwischen Touchscreen und Miniserver. Helligkeitssteuerung basierend auf Präsenz und Raumhelligkeit.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-pure-flex-controller/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| P | Presence | Präsenz ist aktiv. Aktiviert das Display. | - | 0/1 |
| DnD | Do not Disturb | Display und Hintergrundbeleuchtung bleiben ausgeschaltet, wenn sich das Gerät im Ruhezustand befindet. | - | 0/1 |
| LbT | Light by Touch | Wenn aktiviert, schaltet die erste Berührung das Display ein, führt aber keinen Befehl aus. | - | 0/1 |
| L | Lighting active | Der Raum wird durch künstliche Beleuchtung erhellt. Dieser Eingang wird nicht verwendet, wenn ein Lichtsteuerungs Baustein über den API-Connector verbunden ist. | - | 0/1 |
| Br | Room brightness | Aktuelle Raumhelligkeit. Dieser Eingang wird nicht verwendet, wenn ein Lichtsteuerungs Baustein über den API-Connector verbunden ist. | lux | ∞ |
| Set | Set Brightness | Individuelle Displayhelligkeit. Der Wert bleibt aktiv, bis Änderungen in der Präsenz, Raumhelligkeit oder künstlichen Beleuchtung erkannt werden. | % | ∞ |
| Off | Off | Sperrt den Baustein. Dominierender Eingang. | - | 0/1 |
| Don | Display On | Aktiviert das Display. Es wird die Displayhelligkeit 'BrD' verwendet. Der Eingang wird von 'DnD' übersteuert. | - | 0/1 |
| Bl | Backlight On | Aktiviert die Hintergrundbeleuchtung. Ist die aktuelle Helligkeit 'CBrB' = 0, wird die Standardhelligkeit 'BrDef' verwendet. Der Eingang wird von 'DnD' übersteuert. | - | 0/1 |
| Txt | Display Text | Benutzerdefinierten Display-Text festlegen. Es wird die Displayhelligkeit 'BrD' verwendet. Der Eingang wird von 'DnD' übersteuert. | - | - |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-pure-flex-controller/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| BrDP | Dark and Presence Brightness | Helligkeit für Räume mit Präsenz, ohne Tageslicht oder künstliche Beleuchtung. | % | 0...100 | 30 |
| BrDnP | Dark and no Presence Brightness | Helligkeit für Räume ohne Präsenz, ohne Tageslicht oder künstliche Beleuchtung. | % | 0...100 | 0 |
| BrLP | Lighting and Presence Brightness | Helligkeit für Räume mit Präsenz und künstlicher Beleuchtung, wenn die aktuelle Raumhelligkeit unter dem Schwellwert 'Brt' liegt. | % | 0...100 | 50 |
| BrLnP | Lighting and no Presence Brightness | Helligkeit für Räume ohne Präsenz und mit künstlicher Beleuchtung, wenn die aktuelle Raumhelligkeit unter dem Schwellwert 'Brt' liegt. | % | 0...100 | 0 |
| BrBP | Bright and Presence Brightness | Helligkeit für Räume mit Präsenz und einer Raumhelligkeit über dem Schwellwert 'Brt'. | % | 0...100 | 80 |
| BrBnP | Bright and no Presence Brightness | Helligkeit für Räume ohne Präsenz und einer Raumhelligkeit über dem Schwellwert 'Brt'. | % | 0...100 | 0 |
| BrDef | Default Brightness | Standardhelligkeit, die als Fallback für die Hintergrundbeleuchtung 'CBrB' oder die Displayhelligkeit 'BrD' verwendet wird, wenn die berechnete Helligkeit 'CBrB' den Wert 0 hat. | % | 0...100 | 70 |
| Brt | Brightness threshold | Wenn die Helligkeit des Raumes den Höchstwert überschreitet, werden die Tageslichteinstellungen aktiviert. Dieser Parameter wird nicht verwendet, wenn ein Lichtsteuerungs-Baustein über den API-Connector angeschlossen ist. | lux | 0...∞ | 30 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-pure-flex-controller/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| CBrB | Current Brightness Backlight | Aktuelle Hintergrundbeleuchtungshelligkeit für verbundene Geräte. Wenn die Hintergrundbeleuchtung (Bl) aktiv ist, wird 'BrDef' als Fallback verwendet, wenn der Wert 0 ist. | - | ∞ |
| P | Presence | Präsenz ist aktiv. | - | 0/1 |
| L | Lighting Active | Beleuchtung ist aktiv. | - | 0/1 |
| B | Bright | Aktiv, wenn die Raumhelligkeit über dem Schwellenwert liegt. | - | 0/1 |
| Br | Room brightness | Aktuelle Raumhelligkeit. | lux | ∞ |
| BrD | Brightness Display & status LEDs | Helligkeit für das Display, wenn es aktiv ist, sowie für die Status-LEDs, wenn eine LED aktiv ist. Die Helligkeit entspricht 'CBrB'. Ist 'CBrB' = 0, wird 'BrDef' verwendet. Dadurch bleiben Display und LEDs auch dann sichtbar, wenn die Hintergrundbeleuchtung inaktiv ist. | - | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-pure-flex-controller/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Voreingestellte Helligkeit | Stellt den Helligkeitswert auf einen empfohlenen Wert ein, der auf der Farbe des Touch Pure Flex basiert. | - |

### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-pure-flex-controller/

"Wenn die Helligkeit über einen Bausteinparameter auf 0 % gesetzt ist und der Eingang (LbT) aktiv ist, wird bei Berührung des Displays die in den Geräteeigenschaften festgelegte Helligkeit verwendet."

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Dl | `indaylight` | Eingang | Daylight active | Der Raum wird durch Sonnenlicht beleuchtet und alle anderen Lichter werden ausgeschaltet. Dieser Eingang wird nicht verwendet, wenn ein Lichtsteuerungs Baustein über den API-Connector verbunden ist. | – |
| Dis | `indis` | Eingang | Disable periphery control | Deaktiviert alle Eingänge, wenn eingeschaltet (z. B. Kindersicherung, Reinigung). | – |

---

## ### Touch & Grill Baustein

Steuerschnittstelle für Touch & Grill Air Thermometer mit Alarm-Verwaltung, Sensortemperaturausgängen und Timer.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-and-grill-baustein/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Ca | Confirm alarm | Alarm bestätigen | 0/1 |
| Afb | Activate function block | Aktiviert die Steuerung dieses Bausteins durch seinen zugehörigen Touch & Grill. | 0/1 |
| DisT | Disable touch controls | Dient als Schutz vor unabsichtlicher Tastenbetätigung, z. B. bei der Reinigung oder beim Transport. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-and-grill-baustein/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|--------|--------------|
| Ay | Alarm yellow sensor | Aktiv, wenn der Alarm durch den gelben Sensor ausgelöst wird. | \- | 0/1 |
| Ag | Alarm green sensor | Aktiv, wenn der Alarm durch den grünen Sensor ausgelöst wird. | \- | 0/1 |
| At | Alarm timer | Aktiv, wenn der Alarm am Ende des Timers ausgelöst wird. | \- | 0/1 |
| ϑcy | Current temperature yellow sensor | Aktuelle Temperatur gelber Sensor | ° | \-28...300 |
| ϑcg | Current temperature green sensor | Aktuelle Temperatur grüner Sensor | ° | \-28...300 |
| ϑty | Target temperature yellow sensor | Zieltemperatur gelber Sensor | ° | 10...300 |
| ϑtg | Target temperature green sensor | Zieltemperatur grüner Sensor | ° | 10...300 |
| Rt | Remaining time | Verbleibende Laufzeit eines aktiven Timers. | s | 0...5999 |
| Fb | Function block state | Ausgang ist aktiv, solange dieser Baustein vom entsprechenden Touch & Grill gesteuert wird. | \- | 0/1 |
| Atx | Alarm Text | Text des letzten ausgelösten Alarms. | \- | \- |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | \- | \- |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-and-grill-baustein/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|--------|--------------|--------------|
| Dm | Maximum alarm duration (s) | Nach Ablauf dieser Zeit werden alle bestehenden Alarme automatisch quittiert. | s | 1...∞ | 3600 |
| B | Display-Brightness | Die Helligkeit des Displays des zugeordneten Touch & Grill Air Geräts. | % | 0...100 | 100 |

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/touch-and-grill-baustein/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 2...100 | 20 |
| Zugeordnetes Touch & Grill Air | Touch & Grill Air, welches mit diesem Baustein verknüpft ist | \- | \- |

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## ### App

Baustein für App-Aufrufe direkt aus der Loxone App heraus.

### Eingänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Ausgänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Parameter [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/app/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| URL | URL für den App-Aufruf z.B.: spotify:// | - |
| Symbol | Symbol für mobile Anwendung | - |
| Symbolfarbe | Farbe des Symbols in der Visualisierung | - |

### Fallstricke [OFFEN]
Keine Warnhinweise oder Hinweis-Boxen dokumentiert.

---

## ### Tablet

Tablet-Schnittstelle mit Display-Helligkeitssteuerung, Präsenz-Eingängen und Batterie-Überwachung.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tablet/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Ds | Default screen | Eingang wird verwendet, um die festgelegte Standardansicht auf dem Tablet zu aktivieren. | 0/1 |
| P | Presence | Solange der Eingang aktiv ist, bleibt der Bildschirm eingeschaltet und der Bildschirmschoner ausgeschaltet, auch wenn das Tablet inaktiv ist und keine Benutzerinteraktion stattfindet. | 0/1 |
| Dnd | Do not disturb | Alle Benachrichtigungen werden stumm geschaltet. Dimmt das Display vollständig oder auf den über den Parameter (SBr) angegebenen Wert, je nach Bildschirmschoner-Einstellungen, solange keine Benutzerinteraktion erfolgt. Übersteuert den Eingang (P). | 0/1 |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tablet/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| DBr | Display brightness | Legt die Bildschirmhelligkeit fest. | % | 0...100 | 80 |
| SBr | Screensaver brightness | Legt die Bildschirmhelligkeit bei eingeschaltetem Bildschirmschoner fest. | % | 0...100 | 10 |
| Lm | Light mode | Legt das visuelle Design der App fest. Wenn aktiviert, ist der Light-Modus aktiv. | – | 0/1 | 0 |
| Hs | Header style | Legt das Erscheinungsbild und das Layout des Kopfbereichs fest. | – | 0/1 | 0 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/tablet/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| DBr | Current display brightness | Aktuelle Bildschirmhelligkeit | % | 0...100 |
| Cac | Charging active | Ein während des Aufladens | – | 0/1 |
| Blvl | Battery level | Aktueller Batteriestand | % | 0...100 |
| Ui | User interaction | Ein, solange das Tablet in Gebrauch ist. Schaltet ab nach Ende der Nachlaufzeit Benutzerinteraktion. | – | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | – | – |

### Eigenschaften [OFFEN]
Keine separaten Eigenschaften-Tabelle dokumentiert.

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## ### Webpage

Konfiguriert eine benutzerdefinierte Webseite in der Loxone-Visualisierung.

### Eingänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Ausgänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Parameter [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/webpage/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| URL (intern low res) | URL für Webpage, z.B.: http://192.168.1.7:80/test.html | – |
| URL (intern high res) | URL für Webpage, z.B.: http://192.168.1.7:80/testhd.html | – |
| URL (extern low res) | URL für Webpage, z.B.: http://www.mypage.com/test.html | – |
| URL (extern high res) | URL für Webpage, z.B.: http://www.mypage.com/testhd.html | – |
| Symbol | Gibt das Symbol an, das in der Visualisierung angezeigt wird | – |
| Symbolfarbe | Farbe des Symbols in der Visualisierung | – |

### Fallstricke [OFFEN]
Keine separaten Warnhinweise oder Achtung-Boxen dokumentiert.

---

## ### Miniserver Shortcut

Trust Miniserver-Verknüpfung in der Loxone-Visualisierung.

### Eingänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Ausgänge [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Parameter [OFFEN]
Tabelle nicht im Dokument vorhanden.

### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/miniserver-shortcut/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Verknüpfe einen Trust Miniserver | Verknüpfen Sie einen Trust Teilnehmer, anstatt die Adresse und Seriennummer manuell einzugeben. | \- |
| Verknüpfter Trust Miniserver | Wählen Sie einen bereits beigetretenen Trust Teilnehmer aus. | \- |
| Miniserver Seriennummer | — | — |
| Miniserver lokale Adresse | — | — |
| Miniserver externe Adresse | — | — |

### Fallstricke [OFFEN]
Keine separaten Warnhinweise oder Hinweis-Boxen dokumentiert.

---

## ### EIB-Taster

KNX/EIB-Schnittstelle für Taster-Funktionen mit Zustandsabfrage und Direktzugriff.

### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/eib-taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Schaltet zwischen Ein und Aus um. | 0/1 |
| Off | Off | Schaltet den Ausgang (O) aus. Permanent 1 = Sperrt den Baustein. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| On | On | Schaltet den Ausgang (O) ein. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tg), (Aus), (Ein) wenn Ein (z.B. Kindersicherung, Reinigung) | 0/1 |
| S | State | Dieser Eingang kann den Zustand eines EIB-Aktors an den Ausgang weiterleiten, ohne eine Aktion am Ausgang auszulösen. | 0/1 |

### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/eib-taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Verbinden Sie diesen Ausgang mit einem EIB-Schaltaktor (Gruppenadresse Schalten) | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/eib-taster/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanntem Neustart, vor Backup und einmal pro Stunde. Daten auf SD gespeichert. | 0/1 | 0 |

### Eigenschaften [OFFEN]
Keine separaten Eigenschaften-Tabelle im Dokument vorhanden.

### Fallstricke [BELEGT]
Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

---

## Zusammenfassung Completion-Status

| Baustein | Eingänge | Ausgänge | Parameter | Eigenschaften | Fallstricke | Status |
|----------|----------|----------|-----------|---------------|------------|--------|
| Taster | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Tastschalter | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Schalter | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| 2 Tasten | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| 2 Auswahltasten | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Auswahltaste | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Radiotasten | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | ✓ |
| Radiotasten 16 Eingänge | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | ✓ |
| Komfortschalter | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Touch Pure Flex Controller | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | ✓ |
| Touch & Grill Baustein | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | ✓ |
| App | [OFFEN] | [OFFEN] | [OFFEN] | [BELEGT] | [OFFEN] | ⚠ |
| Tablet | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |
| Webpage | [OFFEN] | [OFFEN] | [OFFEN] | [BELEGT] | [OFFEN] | ⚠ |
| Miniserver Shortcut | [OFFEN] | [OFFEN] | [OFFEN] | [BELEGT] | [OFFEN] | ⚠ |
| EIB-Taster | [BELEGT] | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | ✓ |

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Device Tablet (`Device Tablet`)

Managed Tablets can be further integrated with this function block.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Ds | `Ds` | Default screen | Input can be used to launch the specified Default Screen on the Tablet by triggering this input. | – |
| P | `P` | Presence | As long as the input is active the display will stay on and the Screensaver stays off, even if the tablet is idle and there is no user interaction. | – |
| Dnd | `Dnd` | Do not disturb | All notifications will be silenced. Fully dims the display or dims to the value specified via parameter SBr, depending on the screensaver settings, as long as there is no user interaction. Overrides input (P). | – |
| Off | `Off` | Off | Turns off the device. | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| DBr | `ODBr` | Current display brightness | – | 0…100 % |
| Ui | `OUi` | User interaction | Stays ON as long as the tablet is in use. Goes Off after the user interaction overrun duration has ended. | 0…100 |
| API | `API` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| DBr | `DBr` | Display brightness | Controls the brightness of the display. Higher values make the screen brighter; lower values make it dimmer. | 0…100 % | – |
| SBr | `SBr` | Screensaver brightness | Controls the brightness of the display when the Screensaver is on. Higher values make the screen brighter; lower values make it dimmer. | 0…100 % | – |
| V | `V` | Volume | Adjusts the output volume of the device. Increasing this value makes the sound louder; decreasing it makes it quieter. | 0…100 % | – |
| Va | `Va` | Volume alarm sounds | The volume of the device when alarm is active. Higher values make alarms louder; lower values make them quieter. | 0…100 % | – |
| Vbell | `Vbell` | Volume doorbell | The volume of the device when doorbell is triggered. Higher values make the doorbell louder; lower values make it quieter. | 0…100 % | – |
| Lm | `Lm` | Light mode | Specifies the visual theme of the App. When enabled, light mode is active. | – | – |
| Hs | `Hs` | Header style | Specifies the appearance and layout of the header section. | – | – |
| ABr | `ABr` | Adaptive brightness | Specifies whether the display brightness automatically adjusts. | – | – |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 545 · KB: https://www.loxone.com/help/ManagedTabletBlock

---

### Touch Pure Display Controller (`TPDC`)

Configure and Control Touch Pure Display Devices

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| P | `P` | Presence | When connected and presence ends, the display automatically switches to Eco mode. | – |
| On | `On` | On | Activates the display and ends Rest Mode. Rest Mode is not activated as long as this input is active. Is overriden by the Eco input. | – |
| DnD | `DnD` | Do not Disturb | Activates Do Not Disturb mode. Bell notifications are suppressed. Alerts remain active (e.g. alarm system). | – |
| Nm | `Nm` | Night Mode | Activates Night Mode on the display. Reduces brightness and adjusts colors for comfortable viewing in dark environments without causing glare. | – |
| DisPc | `Dis` | Disable periphery control | Disables all inputs when On. (e.g. Child lock, cleaning) | – |
| Eco | `Eco` | Eco | Activates Eco mode. Turns off non-essential functions to save power. The display can be woken up by touch interaction. | – |
| Bell | `Bell` | Bell | Triggers a bell notification on the display. Has no effect when Do Not Disturb is active. | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| TQ | `TQ` | Last interaction | Text output for the last accepted interaction on a Touch Pure Display. | – |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| ABr | `ABr` | Automatic Brightness | Activates automatic brightness control. When active, the device adjusts brightness automatically. BrGain shifts the base brightness up or down. | – | – |
| BrMan | `BrMan` | Manual Brightness | Set the brightness of the Display. | 0…100 % | 60 |
| VolDef | `VolDef` | Default Speaker Volume | Default volume for the built-in speakers. | 0…100 % | 80 |
| BrDelta | `BrDelta` | Rest Mode Brightness Delta | Dims or brightens the display when Rest Mode activates. Negative values dim, positive values brighten the current brightness level. Does not apply when Rest Mode is set to Eco. | -5…5 Steps | -2 |
| BrGain | `BrGain` | Brightness Gain | Shifts the automatic brightness regulation curve up or down. Negative values dim, positive values brighten the automatic brightness level. Only used when Automatic Brightness is enabled. | -5…5 Steps | 0 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 544

---
