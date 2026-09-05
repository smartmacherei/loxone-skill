# Lüftung & Klimaanlage

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## 1. Raumlüftungssteuerung

Steuert Wohnungslüftungsgeräte mit oder ohne Wärmetauscher. Kombiniert automatische Luftfeuchte-, CO2- und Temperaturregelung mit manuellen Betriebsmodi (Boost, Abluft, Schlafmodus) und Frostschutz.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Hi | Humidity indoor | Wenn eine intelligente Raumregelung mit der Raumlüftungssteuerung verbunden ist und die Luftfeuchtigkeit am Eingang (H) angeschlossen ist, verwendet das System den Luftfeuchtigkeitswert der intelligenten Raumregelung und ignoriert den Wert am Eingang (Hi) der Raumlüftungssteuerung. | % | 0...100 |
| CO2 | CO2 indoor | Wenn eine intelligente Raumregelung mit der Raumlüftungssteuerung verbunden und CO2 an den Eingang angeschlossen ist, verwendet das System den CO2-Wert von der intelligenten Raumregelung und ignoriert den Wert am Eingang (CO2) der Raumlüftungssteuerung. | ppm | 0...∞ |
| Sat | Supply air temperature | Wird für Temperaturunterstützung in Kombination mit der Intelligenten Raumregelung und Frostschutz verwendet. Ist dieser Eingang nicht verbunden wird der Wert der Systemvariable "Außentemperatur" verwendet. Ist auch diese nicht verfügbar, sind Temperaturunterstützung und Frostschutz nicht möglich. | ° | ∞ |
| Dwc | Door/window contact | 1 = Offen, 0 = Geschlossen Wenn ein Fenster geöffnet ist, wird die Lüftung deaktiviert. Sobald das Fenster geschlossen ist, wird der Betrieb auf der Grundlage der zuvor aktiven Lüftung fortgesetzt. | - | 0/1 |
| P | Presence | Präsenz | - | 0/1 |
| Off | Off | 1 = Steuerung wird gestoppt und gesperrt | - | 0/1 |
| Sm | Sleep mode | Schaltet die Lüftung für die unter Parameter (Smt) eingestellte Zeit aus. Anschließend wird wieder mit Lüftung begonnen. | - | 0/1 |
| B | Boost | Beendet die Regelung und setzt die Ausgänge (F), (Fea) und (Fsa) auf 100 Prozent. Der Wärmetauscher wird weiterhin automatisch gesteuert. | - | 0/1 |
| Ex | Exhaust air | Beendet die Regelung und setzt die Ausgänge (F) und (Fea) auf 100 Prozent. Der Wärmetauscher wird weiterhin automatisch gesteuert. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/raumlueftungssteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| F | Fan | Kombinierter Zu- und Abluftlüfter. | % | 0...100 |
| Fea | Fan exhaust air | Dedizierter Abluftlüfter. | % | 0...100 |
| Fsa | Fan supply air | Dedizierter Zuluftlüfter. | % | 0...100 |
| He | Heat exchanger | Der Ausgang (He) ist standardmäßig immer Ein, kann manuell ausgeschaltet werden. Bei Heiz-/Kühlanforderung vom Intelligenten Raumregler wird (He), abhängig von der Systemvariable (Außentemperatur) oder Eingang (Sat), aus- bzw. wieder eingeschaltet. | - | 0/1 |
| S | Status | 0: Grundlüftung 1: Erhöhte Luftfeuchtigkeit 2: Temperaturunterstützung 3: Schlechte Luftqualität (CO2) 4: Manuell gestoppt 5: Fenster/Tür geöffnet 6: Manuell Turbo 7: Manuell App 8: Manuell Abluft 9: Schlafmodus 10: Frostschutz | - | 0...10 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/raumlueftungssteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Hmax | Maximum humidity | Der Baustein versucht, (Hi) unter dem eingestellten Wert zu halten. | % | 0...100 | 60 |
| CO2max | Maximum CO2 (air pollution) | Der Baustein versucht, (CO2) unter dem eingestellten Wert zu halten. | ppm | 0...∞ | 1000 |
| Pet | Presence extend time | Beginnt mit der fallenden Flanke des Eingangs (P). Verlängert die Anwesenheit um die angegebene Zeit. | s | 0...∞ | 1800 |
| Smt | Sleep mode timeout | Beginnt mit der fallenden Flanke des Eingangs (Sm). Hält das Gerät für die angegebene Zeit ausgeschaltet. | s | 0...∞ | 7200 |
| Iva | Intensive ventilation absence | Wert für den Lüfter, wenn die Anwesenheit ausgeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 100 |
| Bva | Basic ventilation absence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit ausgeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 10 |
| Ivp | Intensive ventilation presence | Wert für den Lüfter, wenn die Anwesenheit eingeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 0 |
| Bvp | Basic ventilation presence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit eingeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 20 |
| Fpt | Frost protection temperature | Wenn die Außentemperatur unter diesem Wert liegt, wird die Belüftung unterbrochen, um Schäden zu vermeiden. ACHTUNG: Wird keine Außentemperatur gemessen, ist diese Sicherheitsfunktion nicht funktionsfähig! | - | ∞ | -1 |

Quelle: https://www.loxone.com/dede/kb/raumlueftungssteuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|--------------|---------|--------------|--------------|
| Energiekosten | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - | - | - |
| Abluft-/Zuluftbetrieb erlaubt | Legt fest, ob Lüfter einen Unterdruck im Raum erzeugen darf. Falls aktiv, besitzt der Lüfter-Programmbaustein einen zusätzlichen Eingang, mit dem der Abluft-Modus gestartet werden kann. ACHTUNG: Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen! | - | - | - |
| Maximaler Luftaustausch | Geben Sie den maximalen Luftaustausch an, den das Lüftungsgerät für den aktuellen Raum leisten kann. Sie finden Angaben dazu im Datenblatt des Geräteherstellers. Diese Angabe wird für die optimale Einstellung des Reglers verwendet. | m³/h | ∞ | 40 |

Quelle: https://www.loxone.com/dede/kb/raumlueftungssteuerung/

### Fallstricke [BELEGT]

- **Parameter Fpt (Frostschutz):** "Wird keine Außentemperatur gemessen, ist diese Sicherheitsfunktion nicht funktionsfähig!"
- **Eigenschaft Abluft-/Zuluftbetrieb:** "Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen!"

---

## 2. WC-Lüftungssteuerung

Spezialisierte Steuerung für Badezimmer-/WC-Lüftungsgeräte. Startet automatisch bei Anwesenheit oder Steuersignal und läuft für eine konfigurierbare Nachlaufzeit.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Sitzung starten/beenden. | 0/1 |
| P | Presence | Startet Sitzung wenn 1. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/wc-lueftungssteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Session status | Ein solange die Sitzung aktiv ist. | 0/1 |
| Fan | Fan | Ausgang zur Ansteuerung des Lüfters. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/wc-lueftungssteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|--------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Fsd | Fan start delay | Verzögerung bis zum Einschalten des Lüfters nach Beginn der Sitzung. | s | 0...∞ | 30 |
| FPet | Fan / Movement extend time | 1. Die Zeit beginnt mit der fallenden Flanke am Ausgang (S) und verlängert den Ausgang (Fan) um die eingestellte Zeit. 2. Bei Verwendung des Eingangs (P) startet die Zeit mit fallender Flanke an Eingang (P) und verlängert die Ausgänge (S) und (Fan) um die eingestellte Zeit. | s | 0...∞ | 180 |

Quelle: https://www.loxone.com/dede/kb/wc-lueftungssteuerung/

### Eigenschaften [OFFEN]

Keine Eigenschaften in der Dokumentation aufgeführt.

### Fallstricke [BELEGT]

Keine expliziten Warnhinweise oder Achtung-Boxen dokumentiert.

---

## 3. Leaf Lüfter

Dezentrales Lüftungsgerät mit Wärmerückgewinnung für Einzelräume. Regelt Feuchtigkeit, CO2 und Temperatur automatisch, mit Filterüberwachung und synchronisierter Paar-Steuerung (A/B-Lüfter).

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Hi | Humidity indoor | Feuchtigkeit innen | % | 0...100 |
| CO2 | CO2 indoor | CO2 innen | ppm | 0...∞ |
| Sat | Supply air temperature | Gibt die Temperatur der einströmenden Luft an. Wird für die Temperaturunterstützung verwendet. Ist dieser Eingang nicht verbunden wird der Wert der Systemvariable "Aussentemperatur" verwendet. Ist auch diese nicht verfügbar, ist die Temperaturunterstützung deaktiviert. | ° | ∞ |
| Dwc | Door/window contact | EIN: Fenster offen, AUS: Fenster geschlossen. Bei geöffnetem Fenster ist die Lüftung deaktiviert. | - | 0/1 |
| P | Presence | Präsenz | - | 0/1 |
| Off | Off | Stoppt den Lüfter und schließt die Lüftungsklappe, solange EIN. | - | 0/1 |
| Sm | Sleep mode | Schaltet die Lüftung für die unter Parameter (Smt) eingestellte Zeit aus. Anschließend wird wieder mit Lüftung begonnen. | - | 0/1 |
| B | Boost | Beendet die Regelung und setzt den Ausgang auf 100 Prozent. | - | 0/1 |
| Ex | Exhaust air | Stoppt die Regelung und stellt die Abluft auf 100 Prozent. ACHTUNG: Dieser Eingang kann nur verwendet werden, wenn die Bausteineigenschaft "Abluft-/Zuluftbetrieb erlaubt" aktiviert ist. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Cfc | Confirm Filter Change | Filterwechsel bestätigen | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/leaf-luefter/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Status | Gibt an, warum der Lüfter aktiv ist. Dieser Ausgang ist rein informativ. 0: Grundlüftung 1: erhöhte Luftfeuchte 2: Temperaturunterstützung 3: schlechte Luftqualität (CO2) 4: Manuell gestoppt 5: Fenster geöffnet 6: Manuell Turbo 7: Manuell App 8: Manuell Abluft 9: Einschlafmodus. | 0...9 |
| Fc | Filter change | Zeigt an, ob Luftfilter gewechselt werden müssen. | 0/1 |
| Error | Error | 0=Kein Fehler, 1=Offline, 2=Stuck, 3=Blendenfehler. | 0...3 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/leaf-luefter/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Hmax | Maximum humidity | Der Baustein versucht, (Hi) unter dem eingestellten Wert zu halten. | % | 0...100 | 60 |
| CO2max | Maximum CO2 (air pollution) | Der Baustein versucht, (CO2) unter dem eingestellten Wert zu halten. | ppm | 0...∞ | 1000 |
| Pet | Presence extend time | Beginnt mit der fallenden Flanke des Eingangs (P). Verlängert die Anwesenheit um die angegebene Zeit. | s | 0...∞ | 1800 |
| Smt | Sleep mode timeout | Beginnt mit der fallenden Flanke des Eingangs (Sm). Hält das Gerät für die angegebene Zeit ausgeschaltet. | s | 0...∞ | 7200 |
| Iva | Intensive ventilation absence | Wert für den Lüfter, wenn die Anwesenheit ausgeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 100 |
| Bva | Basic ventilation absence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit ausgeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 10 |
| Ivp | Intensive ventilation presence | Wert für den Lüfter, wenn die Anwesenheit eingeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 30 |
| Bvp | Basic ventilation presence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit eingeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 20 |

Quelle: https://www.loxone.com/dede/kb/leaf-luefter/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Energiekosten | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |
| Abluft-/Zuluftbetrieb erlaubt | Legt fest, ob Lüfter einen Unterdruck im Raum erzeugen darf. Falls aktiv, besitzt der Lüfter-Programmbaustein einen zusätzlichen Eingang, mit dem der Abluft-Modus gestartet werden kann. ACHTUNG: Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen! | - |
| Lüftungsrichtung (ohne Wärmetauscher) | Legt die Lüftungsrichtung fest, wenn bei einem Leaf-Paar die Wärmetauscher ausgeschalten sind. Sind die Wärmetauscher aktiv, gibt es keine vorherrschende Lüftungsrichtung, da die Richtung des Luftstroms regelmäßig umgekehrt wird. | - |
| Zugeordneter Lüfter A 1 | Leaf-Lüfter sind zeitlich synchronisiert. Während Lüfter A für Zuluft sorgt, bläst Lüfter B aus, und umgekehrt. Sorgen Sie dafür, dass sich in Ihrer Konfiguration immer gleich viele Lüfter von Typ A wie von Typ B befinden! ACHTUNG: ein Ungleichgewicht in der Verteilung auf Typ A und B kann zu einem Unter-/Überdruck im Raum führen! | - |
| Zugeordneter Lüfter B 1 | Leaf-Lüfter sind zeitlich synchronisiert. Während Lüfter A für Zuluft sorgt, bläst Lüfter B aus, und umgekehrt. Sorgen Sie dafür, dass sich in Ihrer Konfiguration immer gleich viele Lüfter von Typ A wie von Typ B befinden! ACHTUNG: ein Ungleichgewicht in der Verteilung auf Typ A und B kann zu einem Unter-/Überdruck im Raum führen! | - |

Quelle: https://www.loxone.com/dede/kb/leaf-luefter/

### Fallstricke [BELEGT]

- **Eingang Ex (Exhaust air):** "ACHTUNG: Dieser Eingang kann nur verwendet werden, wenn die Bausteineigenschaft 'Abluft-/Zuluftbetrieb erlaubt' aktiviert ist."
- **Eigenschaft Abluft-/Zuluftbetrieb erlaubt:** "ACHTUNG: Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen!"
- **Eigenschaften Zugeordneter Lüfter A 1 und B 1:** "ACHTUNG: ein Ungleichgewicht in der Verteilung auf Typ A und B kann zu einem Unter-/Überdruck im Raum führen!"

---

## 4. Internorm Lüfter

Steuerung für Internorm i-Tec Fenster-Lüftungsgeräte. Regelt Feuchtigkeit, CO2 und Temperatur mit Frostschutz und optionalem Abluft-Modus.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Hi | Humidity indoor | Feuchtigkeit innen | % | 0...100 |
| CO2 | CO2 indoor | CO2 innen | ppm | 0...∞ |
| Sat | Supply air temperature | Wird für Temperaturunterstützung in Kombination mit der Intelligenten Raumregelung und Frostschutz verwendet. Ist dieser Eingang nicht verbunden wird der Wert der Systemvariable "Außentemperatur" verwendet. Ist auch diese nicht verfügbar, sind Temperaturunterstützung und Frostschutz nicht möglich. | ° | ∞ |
| Dwc | Door/window contact | 1 = Offen, 0 = Geschlossen | - | 0/1 |
| P | Presence | Präsenz | - | 0/1 |
| Off | Off | 1 = Steuerung wird gestoppt und gesperrt | - | 0/1 |
| Sm | Sleep mode | Digitaler Eingang Einschlafmodus: Schaltet die Lüftung für die unter Parameter (Smt) eingestellte Zeit aus. Anschließend wird wieder mit Lüftung begonnen. | - | 0/1 |
| B | Boost | Beendet die Regelung und setzt den Ausgang auf 100 Prozent. | - | 0/1 |
| Ex | Exhaust air | Beendet die Regelung und bläst mit 100 Prozent Lüftungsstärke aus. ACHTUNG: Dieser Eingang kann nur verwendet werden, wenn die Bausteineigenschaft "Abluft-/Zuluftbetrieb erlaubt" aktiviert ist. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/internorm-luefter/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Status | Aktueller Status: Gibt an, warum der Lüfter aktiv ist. Dieser Ausgang ist rein informativ. 0: Grundlüftung, 1: erhöhte Luftfeuchte, 2: Temperaturunterstützung, 3: schlechte Luftqualität (CO2), 4: Manuell gestoppt, 5: Fenster geöffnet, 6: Manuell Turbo, 7: Manuell App, 8: Manuell Abluft, 9: Einschlafmodus, 10: Frostschutz. | 0...10 |
| Fc | Filter change | Digitaler Ausgang Filterwechsel: Zeigt an, ob Luftfilter gewechselt werden müssen. | 0/1 |
| Error | Error | Analoger Fehlerausgang: Zeigt an, ob ein Fehler vorliegt: 0=Kein Fehler, 1=Offline, 2=Klappen geschlossen, 100-115=Internorm Fehlercode. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/internorm-luefter/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Hmax | Maximum humidity | Der Baustein versucht, (Hi) unter dem eingestellten Wert zu halten. | % | 0...100 | 60 |
| CO2max | Maximum CO2 (air pollution) | Der Baustein versucht, (CO2) unter dem eingestellten Wert zu halten. | ppm | 0...∞ | 1000 |
| Pet | Presence extend time | Beginnt mit der fallenden Flanke des Eingangs (P). Verlängert die Anwesenheit um die angegebene Zeit. | s | 0...∞ | 1800 |
| Smt | Sleep mode timeout | Beginnt mit der fallenden Flanke des Eingangs (Sm). Hält das Gerät für die angegebene Zeit ausgeschaltet. | s | 0...∞ | 7200 |
| Iva | Intensive ventilation absence | Wert für den Lüfter, wenn die Anwesenheit ausgeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 100 |
| Bva | Basic ventilation absence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit ausgeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 10 |
| Ivp | Intensive ventilation presence | Wert für den Lüfter, wenn die Anwesenheit eingeschaltet ist und (Hi) größer ist als der Parameter (Hmax). Die Intensivlüftung wird gestoppt, wenn (Hi) kleiner ist als (Hmax - 3%). In den Modi „Temperaturunterstützung" und „Schlechte Luftqualität (CO2)" wird dieser Wert als Maximum verwendet. | % | 0...100 | 30 |
| Bvp | Basic ventilation presence | Wert für den Lüfter im Automatikmodus, wenn Anwesenheit eingeschaltet ist. Im Temperaturmodus wird dieser Wert als Mindestwert verwendet. | % | 0...100 | 22 |

Quelle: https://www.loxone.com/dede/kb/internorm-luefter/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Energiekosten | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |
| Abluft-/Zuluftbetrieb erlaubt | Legt fest, ob Lüfter einen Unterdruck im Raum erzeugen darf. Falls aktiv, besitzt der Lüfter-Programmbaustein einen zusätzlichen Eingang, mit dem der Abluft-Modus gestartet werden kann. ACHTUNG: Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen! | - |
| Lüftungsrichtung (ohne Wärmetauscher) | Legt die Lüftungsrichtung fest, wenn bei einem Internorm Lüfter der Wärmetauscher ausgeschalten ist. Ist der Wärmetauscher aktiv, gibt es keine vorherrschende Lüftungsrichtung, da Zuluft und Abluft simultan laufen. | - |
| Zugeordneter Lüfter | Lüfter der mit diesem Baustein verknüpft ist. Geräte die zugeordnet werden können: Internorm I-Tec Lüfter | - |

Quelle: https://www.loxone.com/dede/kb/internorm-luefter/

### Fallstricke [BELEGT]

- **Eingang Ex (Exhaust air):** "ACHTUNG: Dieser Eingang kann nur verwendet werden, wenn die Bausteineigenschaft "Abluft-/Zuluftbetrieb erlaubt" aktiviert ist."
- **Eigenschaft Abluft-/Zuluftbetrieb:** "ACHTUNG: Falls sich Raumluftabhängige Feuerstellen im Einflussbereich des Lüfters befinden, kann ein Unterdruck Rauchqualm in den Wohnraum ziehen!"

---

## 5. Fan Coil Steuerung

Steuert Ventilatorkonvektor (Fan Coil) Geräte für Raum-Heiz-/Kühlbetrieb. Regelt Lüftergeschwindigkeit und Ventile basierend auf Solltemperatur, Luftfeuchte und manuellen Modi (Silent, Boost, Pause).

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| ϑc | Current Room Temperature | Der Wert wird von der verknüpften Intelligenten Raumregelung bereitgestellt. Wird der Eingang ebenfalls verwendet, gilt die zuletzt erfolgte Änderung. | ° | ∞ |
| ϑt | Target Room Temperature | Der Wert wird von der verknüpften Intelligenten Raumregelung bereitgestellt. Wird der Eingang ebenfalls verwendet, gilt die zuletzt erfolgte Änderung. | ° | ∞ |
| Ha | Heating Available | Bestätigung, dass an dieser Einheit Heizenergie verfügbar ist. Kann einzeln verwendet werden (z. B. Wärmepumpe "bereit", Kessel freigegeben) oder in Kombination mit einer Fan Coil Zentralsteuerung, um lokal zu prüfen, dass Warmwasser die Einheit erreicht hat (Laufzeitschutz). TRUE / nicht verbunden: Heizung darf bei Bedarf laufen. FALSE: Heizausgang wird abgeschaltet, verhindert, dass kalte Luft in den Raum geblasen wird. Wenn der Zentralsteuerung zugeordnet: UND-verknüpft mit den Informationen der Zentralsteuerung. | - | 0/1 |
| Ca | Cooling Available | Bestätigung, dass an dieser Einheit Kälteenergie verfügbar ist. Kann einzeln verwendet werden (z. B. Kaltwasseranlage "bereit") oder in Kombination mit einer Fan Coil Zentralsteuerung, um lokal zu prüfen, dass Kaltwasser die Einheit erreicht hat (Laufzeitschutz). TRUE / nicht verbunden: Kühlung darf bei Bedarf laufen. FALSE: Kühlausgang wird abgeschaltet, verhindert, dass warme Luft in den Raum geblasen wird. Wenn der Zentralsteuerung zugeordnet: UND-verknüpft mit den Informationen der Zentralsteuerung. | - | 0/1 |
| Dwc | Door and Window Contact | 0=Geschlossen 1=Offen | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Turns Fan and Valves Off. Pulse (> 200 ms): All outputs are switched off, timers are reset and block is locked. Dominating input. | - | 0/1 |
| Sm | Silent Mode | Wenn aktiviert, wird die maximale Lüftergeschwindigkeit gemäß der Einstellung "Lüftergeschwindigkeit im Leisemodus" festgelegt. Wird die Funktion wieder deaktiviert, wird die Lüftergeschwindigkeit neu berechnet. | - | 0/1 |
| Bm | Boost Mode | Setzt die Lüftergeschwindigkeit auf maximal. | - | 0/1 |
| Pt | Pause Timer | Pausiert das Gerät für die im Parameter (Ptd) eingestellte Dauer. | - | 0/1 |
| Fan | Fan Speed | Lüftergeschwindigkeit in Prozent der maximalen Leistung. -1 für Auto. -1 wenn nicht verbunden. | % | -1...100 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-steuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| H | Heating Output | Heizausgang | - | 0...10 |
| C | Cooling Output | Kühlausgang | - | 0...10 |
| HC | Combined Heating/Cooling Output | Kombinierter Heiz-/Kühlausgang | - | 0...10 |
| Fan | Fan Speed Analogue | Lüftergeschwindigkeit analog | - | 0...100 |
| FanS | Fan Speed Step | Aktuelle Stufe, berechnet mit der Einstellung "Lüfterstufen". | - | 0...∞ |
| ϑc | Current Room Temperature | Aktuelle Raumtemperatur | ° | ∞ |
| ϑt | Target Room Temperature | Zielraumtemperatur | ° | ∞ |
| Mode | Current Mode | 0 = Aus 1 = Auto 2 = Heizen 3 = Kühlen 4 = Belüftung | - | 0...4 |
| S | Status | An wenn entweder Ventil offen oder Lüfter aktiv ist. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/fan-coil-steuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Fmax | Maximum Fan Speed in Auto Mode | Maximale Lüftergeschwindigkeit im Automatikmodus | % | 0...100 | 80 |
| Mode | Mode | 0 = Aus 1 = Auto 2 = Heizen 3 = Kühlen 4 = Belüftung Wird durch IRC festgelegt, wenn auf Automatik gestellt und von IRC gesteuert | - | 0...4 | 1 |
| Ptd | Pause Timer Duration | Startet mit steigender Flanke am Eingang (Pt). Hält das Gerät für die angegebene Dauer an. | s | 0...∞ | 7200 |
| FϑKP | Proportional Gain (Fan) | Proportionaler Verstärkungsfaktor für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 50 |
| FϑKI | Integral Gain (Fan) | Integrierter Verstärkungsfaktor für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 0.01 |
| FϑSt | Sample Time (Fan) | Abtastintervall für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | s | 0...∞ | 60 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-steuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|--------------|---------|--------------|--------------|
| Lüfterstufen | Zur Abbildung diskreter Stufen. Beispiel: 4 Stufen → 25 % der Gesamtleistung pro Stufe. Wenn es auf 0 gesetzt wird, wird der Ausgang 'Fan Speed Step' (FanS) deaktiviert. | - | 0...100 | 3 |
| Lüftergeschwindigkeit im Leisemodus | Maximale Lüftergeschwindigkeit im Leisemodus | % | 0...100 | 10 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-steuerung/

### Fallstricke [BELEGT]

- **Regelanpassung:** "Um störende Sprünge in der Regelung zu vermeiden, erfolgt die Anpassung der Luftmenge einmal pro Minute mit einer maximalen Änderung von 20 %. Eine Änderung von 100 % auf 0 % dauert somit 5 Minuten."

---

## 6. Fan Coil Frischluft Steuerung

Ventilatorkonvektor mit Frischluftregelung. Kombiniert Temperatur- und Feuchte-/CO2-basierte Luftmengen-Regelung für optimalen Luftqualität und Komfort.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| ϑc | Current Room Temperature | Der Wert wird von der verknüpften Intelligenten Raumregelung bereitgestellt. Wird der Eingang ebenfalls verwendet, gilt die zuletzt erfolgte Änderung. | ° | ∞ |
| ϑt | Target Room Temperature | Der Wert wird von der verknüpften Intelligenten Raumregelung bereitgestellt. Wird der Eingang ebenfalls verwendet, gilt die zuletzt erfolgte Änderung. | ° | ∞ |
| Ha | Heating Available | Bestätigung, dass an dieser Einheit Heizenergie verfügbar ist. Kann einzeln verwendet werden (z. B. Wärmepumpe "bereit", Kessel freigegeben) oder in Kombination mit einer Fan Coil Zentralsteuerung, um lokal zu prüfen, dass Warmwasser die Einheit erreicht hat (Laufzeitschutz). TRUE / nicht verbunden: Heizung darf bei Bedarf laufen. FALSE: Heizausgang wird abgeschaltet, verhindert, dass kalte Luft in den Raum geblasen wird. Wenn der Zentralsteuerung zugeordnet: UND-verknüpft mit den Informationen der Zentralsteuerung. | - | 0/1 |
| Ca | Cooling Available | Bestätigung, dass an dieser Einheit Kälteenergie verfügbar ist. Kann einzeln verwendet werden (z. B. Kaltwasseranlage "bereit") oder in Kombination mit einer Fan Coil Zentralsteuerung, um lokal zu prüfen, dass Kaltwasser die Einheit erreicht hat (Laufzeitschutz). TRUE / nicht verbunden: Kühlung darf bei Bedarf laufen. FALSE: Kühlausgang wird abgeschaltet, verhindert, dass warme Luft in den Raum geblasen wird. Wenn der Zentralsteuerung zugeordnet: UND-verknüpft mit den Informationen der Zentralsteuerung. | - | 0/1 |
| CO2 | Current Room CO2 | Der Wert wird von der verknüpften Intelligenten Raumregelung bereitgestellt. Wird der Eingang ebenfalls verwendet, gilt die zuletzt erfolgte Änderung. | ppm | 0...∞ |
| Dwc | Door and Window Contact | 0=Geschlossen  1=Offen | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Turns Fan and Valves Off. Pulse (> 200 ms): All outputs are switched off, timers are reset and block is locked. Dominating input. | - | 0/1 |
| Sm | Silent Mode | Wenn aktiviert, wird die maximale Lüftergeschwindigkeit gemäß der Einstellung "Lüftergeschwindigkeit im Leisemodus" festgelegt. Wird die Funktion wieder deaktiviert, wird die Lüftergeschwindigkeit neu berechnet. | - | 0/1 |
| Bm | Boost Mode | Setzt die Lüftergeschwindigkeit auf maximal. | - | 0/1 |
| Pt | Pause Timer | Pausiert das Gerät für die im Parameter (Ptd) eingestellte Dauer. | - | 0/1 |
| Fan | Fan Speed | Lüftergeschwindigkeit in Prozent der maximalen Leistung. -1 für Auto. -1 wenn nicht verbunden. | % | -1...100 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-frischluft-steuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| H | Heating Output | Heizausgang | - | 0...10 |
| C | Cooling Output | Kühlausgang | - | 0...10 |
| HC | Combined Heating/Cooling Output | Kombinierter Heiz-/Kühlausgang | - | 0...10 |
| Fan | Fan Speed Analogue | Lüftergeschwindigkeit analog | - | 0...100 |
| FanS | Fan Speed Step | Aktuelle Stufe, berechnet mit der Einstellung "Lüfterstufen". | - | 0...∞ |
| ϑc | Current Room Temperature | Aktuelle Raumtemperatur | ° | ∞ |
| ϑt | Target Room Temperature | Zielraumtemperatur | ° | ∞ |
| Mode | Current Mode | 0 = Aus  1 = Auto  2 = Heizen  3 = Kühlen  4 = Belüftung | - | 0...4 |
| S | Status | An wenn entweder Ventil offen oder Lüfter aktiv ist. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/fan-coil-frischluft-steuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| CO2t | Target CO2 | CO2-Grenzwert für die Luftqualität. Wird dieser Grenzwert überschritten, gilt die Luftqualität als schlecht und die Logik ändert sich gemäß der unten stehenden Tabelle. | ppm | 0...∞ | 600 |
| Fmax | Maximum Fan Speed in Auto Mode | Maximale Lüftergeschwindigkeit im Automatikmodus | % | 0...100 | 80 |
| Mode | Mode | 0 = Aus  2 = Heizen  3 = Kühlen  4 = Belüftung  Wird durch IRC festgelegt, wenn auf Automatik gestellt und von IRC gesteuert | - | 0...4 | 1 |
| Ptd | Pause Timer Duration | Startet mit steigender Flanke am Eingang (Pt). Hält das Gerät für die angegebene Dauer an. | s | 0...∞ | 7200 |
| FϑKP | Proportional Gain (Fan Temp) | Proportionaler Verstärkungsfaktor für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 50 |
| FϑKI | Integral Gain (Fan Temp) | Integrierter Verstärkungsfaktor für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 0.01 |
| FϑSt | Sample Time (Fan Temp) | Abtastintervall für den Lüfterausgang basierend auf der Temperatur. Wird für den PI-Regler verwendet. | s | 0...∞ | 60 |
| Fco2KP | Proportional Gain (Fan CO2) | Proportionaler Verstärkungsfaktor für den Lüfterausgang basierend auf der Luftqualität (CO2). Wird für den PI-Regler verwendet. | - | 0...∞ | 50 |
| Fco2KI | Integral Gain (Fan CO2) | Integrierter Verstärkungsfaktor für den Lüfterausgang basierend auf der Luftqualität (CO2). Wird für den PI-Regler verwendet. | - | 0...∞ | 0.01 |
| Fco2St | Sample Time (Fan CO2) | Abtastintervall für den Lüfterausgang basierend auf der Luftqualität (CO2). Wird für den PI-Regler verwendet. | s | 0...∞ | 60 |
| VKP | Proportional Gain (Valve) | Proportionaler Verstärkungsfaktor für Ventilausgänge basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 50 |
| VKI | Integral Gain (Valve) | Integrierter Verstärkungsfaktor für Ventilausgänge basierend auf der Temperatur. Wird für den PI-Regler verwendet. | - | 0...∞ | 0.01 |
| VSt | Sample Time (Valve) | Abtastintervall für Ventilausgänge basierend auf der Temperatur. Wird für den PI-Regler verwendet. | s | 0...∞ | 60 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-frischluft-steuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|--------------|---------|--------------|--------------|
| Lüfterstufen | Zur Abbildung diskreter Stufen. Beispiel: 4 Stufen → 25 % der Gesamtleistung pro Stufe. Wenn es auf 0 gesetzt wird, wird der Ausgang 'Fan Speed Step' (FanS) deaktiviert. | - | 0...100 | 3 |
| Lüftergeschwindigkeit im Leisemodus | Maximale Lüftergeschwindigkeit im Leisemodus | % | 0...100 | 10 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-frischluft-steuerung/

### Fallstricke [BELEGT]

- **Regelanpassung:** "Um störende Sprünge in der Regelung zu vermeiden, erfolgt die Anpassung der Luftmenge einmal pro Minute mit einer maximalen Änderung von 20 %."

---

## 7. Fan Coil Zentralsteuerung

Zentrale Steuerung für mehrere Fan Coil Geräte. Verwaltet Heiz-/Kühlmodus, Energieverfügbarkeit und Außentemperatur-basierte Betriebsart-Umschaltung mit Ventil-Verzögerung.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| ϑo | Outdoor Temperature | Ist dieser Eingang nicht verbunden, wird der Wert der Systemvariable "Außentemperatur" verwendet. Ist dieser nicht verfügbar, wird 0° zur Berechnung verwendet und der Wert -1000 an diesem Eingang angezeigt. | ° | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | - | 0/1 |
| Eh | Excess heating | Überschuss oder günstige Heizenergie verfügbar. Im Heizmodus überheizt der Block oder erlaubt einen vorzeitigen Heizstart. | - | 0/1 |
| Ec | Excess cooling | Überschuss oder günstige Kühlenergie verfügbar. Im Kühlmodus überükhlt der Block oder erlaubt einen vorzeitigen Kühlstart. | - | 0/1 |
| Hac | Heating Active | Bestätigung durch die gesteuerte Quelle, dass tatsächlich Wärme geliefert wird (Kessel in Betrieb, Mischventil geöffnet, Rücklauftemperatur erreicht), nachdem der (H)-Ausgang aktiviert wurde. FALSE: Die Heizungsausgänge aller zugewiesenen Steuerungen bleiben geschlossen, bis TRUE – keine kalte Luft. TRUE / nicht angeschlossen: Zugewiesene Steuerungen können die Heizung entsprechend ihrem Bedarf betreiben. Hat keinen Einfluss auf den eigenen (H)-Ausgang der Zentralsteuerung. | - | 0/1 |
| Cac | Cooling Active | Bestätigung durch die gesteuerte Quelle, dass tatsächlich gekühlt wird (Kältemaschine läuft, Mischventil geöffnet, Rücklauftemperatur erreicht), nachdem dies über den (C)-Ausgang aktiviert wurde. FALSE: Die Kühlausgänge aller zugewiesenen Steuerungen bleiben geschlossen, bis TRUE – keine warme Luft. TRUE / nicht angeschlossen: Zugewiesene Steuerungen können je nach Bedarf den Kühlbetrieb ausführen. Hat keinen Einfluss auf den eigenen (C)-Ausgang der Zentralsteuerung. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-zentralsteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| H | Heating | Gerät ist im Heizmodus. | - | 0/1 |
| C | Cooling | Gerät ist im Kühlmodus. | - | 0/1 |
| ϑoa | Average Outdoor Temperature | Zeigt die durchschnittliche Außentemperatur der letzten 48 Stunden an. Der berechnete Wert ist verfügbar, sobald die ersten 24 Stunden vergangen sind. Bis dahin wird der Wert -1000 angezeigt. | ° | ∞ |
| AvMode | Available Mode [0-3] | Zurzeit verfügbare Modi basierend auf dem Otm oder Mode Parameter 0 = Keine 1 = Nur Heizen 2 = Nur Kühlen 3 = Heizen oder Kühlen | - | 0...3 |
| Sv | Switching Valve | 0 = Heizen 1 = Kühlen Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/fan-coil-zentralsteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Mode | Mode | 0 = Gerät abgeschaltet. 1 = Automatischer Wechsel je nach Anforderung der Fan Coil Steuerung. 2 = Nur Heizen bei ausreichendem Bedarf. 3 = Nur Kühlen bei ausreichendem Bedarf. | - | 0...3 | 1 |
| SotH | Switch on threshold for Heating | Einschaltschwelle fürs Heizen | % | 0...100 | 30 |
| SotC | Switch on threshold for Cooling | Einschaltschwelle fürs Kühlen | % | 0...100 | 30 |
| MinHrt | Minimum Heating Runtime | Definiert die minimale Dauer, für die der Ausgang aktiv bleiben muss sobald eingeschaltet. | min | 0...∞ | 0 |
| MinCrt | Minimum Cooling Runtime | Definiert die minimale Dauer, für die der Ausgang aktiv bleiben muss sobald eingeschaltet. | min | 0...∞ | 0 |
| Otm | Outdoor Temperature Mode | 0 = Deaktiviert (ϑLimH and ϑLimC werden nicht verwendet) 1 = Durchschnittliche Außentemperatur der letzten 48h 2 = Wert der Systemvariablen 'Erwartete durchschnittliche Außentemperatur 48h' 3 = Aktuelle Außentemperatur Wenn aktiviert, wird die durchschnittliche Außentemperatur der letzten 48h, der nächsten 48h oder die aktuelle Temperatur verwendet, um den Heiz-/Kühlmodus gemäß (ϑLimH) und (ϑLimC) auszuwählen. Wenn der Wert nicht verfügbar ist, hat dieser Parameter keine Auswirkung. | - | 0...3 | 2 |
| ϑLimH | Temperature Limit Heating | Wenn die verwendete Außentemperatur (Parameter Otm) über (ϑLimH) liegt, wird trotz Anforderung nicht in den Heizbetrieb gewechselt. | ° | ∞ | 18 |
| ϑLimC | Temperature Limit Cooling | Wenn die verwendete Außentemperatur (Parameter Otm) unter (ϑLimC) liegt, wird trotz Anforderung nicht in den Kühlbetrieb gewechselt. | ° | ∞ | 15 |
| Vd | Valve Delay | Dauer des Umschaltens zwischen Heizen und Kühlen. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | 0...∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/fan-coil-zentralsteuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Rohrsystem | Rohrsystem des Ventilatorkonvektors auswählen | - |
| Zuordnungen | Klimaanlagensteuerungs Bausteine hinzufügen oder entfernen | - |
| Energiekosten(Heizen) | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |
| Energiekosten(Kühlen) | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |

Quelle: https://www.loxone.com/dede/kb/fan-coil-zentralsteuerung/

### Fallstricke [BELEGT]

Keine expliziten Warnhinweise oder Achtung-Boxen dokumentiert.

---

## 8. Klimaanlagensteuerung

Steuert Split-Klimageräte (kabellose Kommunikation). Regelt Betriebsmodi (Auto, Heizen, Kühlen, Trocknen, Ventilator), Zieltemperatur, Lüftergeschwindigkeit und Luftstromrichtung mit Pause- und Energiespar-Funktionen.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Tg | Toggles between On and Off | Schaltet zwischen Ein und Aus um | - | 0/1 |
| On | Set to On | Einschalten | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): AC unit and Status output are switched off. Pulse (> 200 ms): AC unit is switched off, Block is locked, all outputs are reset while input is on. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| ϑt | Target Temperature | Zieltemperatur | ° | ∞ |
| ϑc | Current Temperature | Wenn dieser Eingang verbunden ist, wird er zur Temperaturregelung verwendet. Die Klimaanlagensteuerung passt ihr Verhalten entsprechend der gemessenen Raumtemperatur an. Ist der Eingang nicht verbunden, übernimmt die Inneneinheit die Regelung selbstständig. Bei Steuerung durch eine intelligente Raumregelung wird die Raumtemperatur vom Raumregler vorgegeben. | - | ∞ |
| Mode | Mode 1-5 | 1 = Auto, 2 = Heizen, 3 = Kühlen, 4 = Trocknen, 5 = Ventilator. Die verfügbaren Modi können in den Modus-Einstellungen des Bausteins festgelegt werden. | - | 1...5 |
| Fan | Fan speed 0-7 | 0 = Aus, 1 = Auto, 2 = Leise, 3 = Sehr Niedrig, 4 = Niedrig, 5 = Mittel, 6 = Hoch, 7 = Sehr Hoch. Die verfügbaren Lüftergeschwindigkeiten können in den Lüftergeschwindigkeits-Einstellungen des Bausteins festgelegt werden. | - | 0...7 |
| ADir | Airflow direction up/down 1-8 | 1 = Auto, 2-6 = Position 1-5, 7 = Pendeln, 8 = Kein Pendeln. Die verfügbaren Luftstromrichtungen können in den Luftstromrichtungs-Einstellungen des Bausteins festgelegt werden. Die vertikale Lamellenverstellung wird von keinem AC Control-Typ unterstützt. Diese Einschränkung ist in erster Linie auf Einschränkungen bei den Schnittstellen zurückzuführen, die für die Kommunikation mit den Klimageräten verwendet werden. Während einige Modelle diese Funktion theoretisch unterstützen könnten, wurde sie nicht implementiert, um die Konsistenz der Steuerungen über alle Typen hinweg zu erhalten. | - | 1...8 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Dwc | Door / window contact | 0 = geschlossen, 1 = offen. Wenn das Gerät eingeschaltet ist, wird es so lange pausiert, wie eine oder mehrere Türen/Fenster offen sind. | - | 0/1 |
| Pt | Pause timer | Pausiert das Gerät für die im Parameter (Ptd) eingestellte Dauer. | - | 0/1 |
| Ls | Load shedding | Wenn aktiviert, pausiert das Gerät das Laden, um Netzleistungsspitzen oder ähnliche Probleme zu verhindern, und bleibt so lange pausiert, wie die Lastabwurf aktiv ist. | - | 0/1 |
| Sm | Silent Mode | Wenn aktiviert, wird die Lüftergeschwindigkeit gemäß der Einstellung 'Lüftergeschwindigkeit im Leisemodus' gesetzt. Bei Deaktivierung wird sie auf den zuletzt über den Eingang oder die App definierten Wert zurückgesetzt. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ac-control/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Status | Device-Status | 0 = Aus, 1 = An | 0/1 |
| Mode | Current Mode 1-5 | Aktueller Modus 1-5 | 1...5 |
| Fan | Fan speed 0-7 | Lüftergeschwindigkeit 0-7 | 0...7 |
| Adir | Airflow direction up/down 1-7 | Luftstromrichtung nach oben/unten 1-7 | 1...7 |
| ϑt | Target temperature | Zieltemperatur | ∞ |
| ϑc | Current temperature | Aktuelle Temperatur | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/ac-control/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Ptd | Pause timer duration | Beginnt mit der fallenden Flanke des Eingangs (Pt). Hält das Gerät für die angegebene Dauer pausiert. | s | 0...∞ | 7200 |
| Hys | Hysteresis | Hysterese für das Ein- und Ausschalten. Diese Einstellung gilt nur, wenn die Zieltemperatur vom Intelligenten Raumcontroller verwaltet wird (automatisch aktiviert). | ° | 0...∞ | 0.5 |
| O | Target Offset | Offset der Zieltemperatur bezogen auf die empfangene Zieltemperatur. Diese Einstellung gilt nur, wenn die Zieltemperatur von der Intelligenten Raumregelung verwaltet wird (automatisch aktiviert) und sich der Regler im Modus Eco oder Eco2 (Gebäudeschutz) befindet. | ° | 0...∞ | 1 |
| minT | Minimum Target Temperature | Niedrigste einstellbare Zieltemperatur in der App | ° | ∞ | 1 |
| maxT | Maximum Target Temperature | Höchste Zieltemperatur, die in der App eingestellt werden kann | ° | ∞ | 40 |

Quelle: https://www.loxone.com/dede/kb/ac-control/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|--------------|--------------|
| Modus Bezeichnungen | Verwendung und Bezeichnung der Modi konfigurieren | - | - |
| Luftstromrichtung Bezeichnungen | Verwendung und Bezeichnung der Luftstromrichtungen konfigurieren | - | - |
| Lüftergeschwindigkeit Bezeichnungen | Verwendung und Bezeichnung der Lüftergeschwindigkeiten konfigurieren | - | - |
| Lüftergeschwindigkeit im Leisemodus | Lüftergeschwindigkeit, die beim Aktivieren des Leisemodus gesetzt wird | - | - |
| Standard-Luftstrom | Luftstromrichtung, die eingestellt wird, wenn die Klimaanlage ausgeschaltet ist | - | - |
| Standard-Lüftergeschwindigkeit | Lüftergeschwindigkeit, die eingestellt wird, wenn die Klimaanlage ausgeschaltet ist | - | - |
| Standard-Zieltemperaturmodus | Gibt an, ob das System die zuletzt angewendete Standard-Zieltemperatur oder einen manuell definierten Festwert verwendet. | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

Quelle: https://www.loxone.com/dede/kb/ac-control/

### Fallstricke [BELEGT]

Keine expliziten Warnhinweise oder Achtung-Boxen in der Dokumentation vorhanden.

---

## 9. Klimaanlagen Zentralsteuerung

Zentrale Steuerung für mehrere Split-Klimageräte. Verwaltet Heiz-/Kühlmodus, Energieverfügbarkeit und Außentemperatur-basierte Freigabe für intelligente Raumregler.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| ϑo | Outdoor Temperature | Ist dieser Eingang nicht verbunden, wird der Wert der Systemvariable "Außentemperatur" verwendet. Ist diese nicht verfügbar, wird der Wert -1000 angezeigt. | ° | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| Ec | Excess cooling | Überschüssige oder günstige Kühlenergie vorhanden. Im Kühlbetrieb wird Intelligenten Raumreglern überkühlen bzw. vorzeitiger Kühlbeginn erlaubt. | - | 0/1 |
| Eh | Excess heating | Überschüssige oder günstige Heizenergie vorhanden. Im Heizbetrieb wird Intelligenten Raumreglern überheizen bzw. vorzeitiger Heizbeginn erlaubt. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/klimaanlagen-zentralsteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| H | Heating | Gerät ist im Heizmodus | 0/1 |
| C | Cooling | Gerät ist im Kühlmodus | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/klimaanlagen-zentralsteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Mode | Mode | 0 = Gerät abgeschaltet. 1 = Automatischer Wechsel je nach Anforderung der Intelligenten Raumregler. 2 = Nur Heizen bei genügend Anforderung. 3 = Nur Kühlen bei genügend Anforderung. | - | 0...3 | -1 |
| ϑLimH | Temperature Limit Heating | Wenn die verwendete Außentemperatur (Parameter Otm) über (ϑLimH) liegt, wird trotz Anforderung nicht in den Heizbetrieb gewechselt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | ° | ∞ | 18 |
| ϑLimC | Temperature Limit Cooling | Wenn die verwendete Außentemperatur (Parameter Otm) unter (ϑLimC) liegt, wird trotz Anforderung nicht in den Kühlbetrieb gewechselt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | ° | ∞ | 15 |
| Otm | Outdoor Temperature Mode | 0 = Deaktiviert (ϑLimH and ϑLimC werden nicht verwendet) 1 = Durchschnittliche Außentemperatur der letzten 48h 2 = Wert der Systemvariablen 'Erwartete durchschnittliche Außentemperatur 48h' 3 = Aktuelle Außentemperatur Wenn aktiviert, wird die durchschnittliche Außentemperatur der letzten 48h, der nächsten 48h oder die aktuelle Temperatur verwendet, um den Heiz-/Kühlmodus gemäß (ϑLimH) und (ϑLimC) auszuwählen. Wenn der Wert nicht verfügbar ist, hat dieser Parameter keine Auswirkung. | - | 0...3 | 2 |

Quelle: https://www.loxone.com/dede/kb/klimaanlagen-zentralsteuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Zuordnungen | Klimaanlagensteuerungs Bausteine hinzufügen oder entfernen | - |
| Energiekosten(Heizen) | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |
| Energiekosten(Kühlen) | Kosten für Energiebereitstellung. Objekte mit der konfiguration 'teuer' werden von den Raumregelungen nur angefordert, wenn keine höher priorisierten Quellen verfügbar sind. | - |

Quelle: https://www.loxone.com/dede/kb/klimaanlagen-zentralsteuerung/

### Fallstricke [BELEGT]

Keine expliziten Warnhinweise oder Achtung-Boxen dokumentiert.

---

## Zusammenfassung

**Kategorie:** Lüftung & Klimaanlage  
**Bausteine erfasst:** 9 von 9  
**Bausteine fehlgeschlagen:** Keine  

Alle 9 Bausteine wurden vollständig recherchiert und dokumentiert. Alle Tabellen (Eingänge, Ausgänge, Parameter, Eigenschaften) wurden wörtlich aus der offiziellen Loxone-Dokumentation übernommen und entsprechend mit [BELEGT] gekennzeichnet. Fallstricke und Warnhinweise wurden vollständig erfasst. Spezielle Kürzel mit Sonderzeichen (wie ϑ) wurden exakt beibehalten.

**Stand:** 30.07.2026
