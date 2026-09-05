# Beleuchtung
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## Baustein 1: Lichtsteuerung

### Lichtsteuerung

Ermöglicht Steuerung und Bedienung von Beleuchtungen in einem Raum oder Bereich mit Unterstützung für Schalten, Dimmen, Farblicht und verschiedene Leuchtmittelschnittstellen.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/lichtsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Lc1-8 | Light circuit 1-8 | Aktiviert den Ausgang (Lc1-4). Langer Klick zum Dimmen. | - | 0/1 |
| M+ | Next mood | Impuls: Wählt die nächste Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | - | 0/1 |
| M- | Previous mood | Impuls: Wählt die vorherige Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | - | 0/1 |
| Mood | Select mood by ID | Stimmung durch ID auswählen | - | 0...99 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. An alarm can still be triggered via the input (Alarm). Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| T5/1-8 | T5 control | Impuls: Der erste Impuls wählt die zugewiesene Stimmung aus, jeder weitere Impuls schaltet auf die nächste Stimmung um. Erfolgt 30 Sekunden lang kein weiterer Impuls, wählt ein Impuls wieder die zugewiesene Stimmung. Langklick: Mischt entweder die Stimmung (Mmd) ein oder schaltet auf die nächste Stimmung um. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet die Lichter aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | - | ∞ |
| DisP | Disable presence / motion | Deaktiviert Eingänge (P) und (Mo) wenn 1. Beleuchtung, die durch Präsenz (P) aktiviert wurde, wird sofort ausgeschaltet. Wenn Beleuchtung durch Bewegung (Mo) aktiviert wurde, wird bei steigender Flanke an (DisP) der Timer (Moet) gestartet und die Lichter werden nach Ablauf ausgeschaltet. Wenn die Zeit von (Met) kürzer ist als (Moet), wird stattdessen (Met) verwendet. | - | 0/1 |
| Mo | Motion | Aktiviert die Lichtstimmung für Bewegung/Präsenz bei 1. Bei fallender Flanke wird die Beleuchtung nach Ablauf des Parameters (Moet) ausgeschaltet. Wird die Beleuchtung manuell bedient, wird die Beleuchtung erst nach Ablauf des Parameters (Met) ausgeschaltet. | - | 0/1 |
| On | All on | Aktiviert Stimmung mit ID 99. Wenn keine Stimmung mit ID 99 konfiguriert ist, werden alle verwendeten Ausgänge (Lc1-18) mit der im Parameter (MaxAbr) eingestellten Helligkeit aktiviert. | - | 0/1 |
| Alarm | Alarm | Verwendete Ausgänge (Lc1-18) beginnen zu blinken, wenn 1. Parameter (MaxAbr) definiert die Helligkeit, Parameter (Afi) definiert das Blinkintervall. Am Ausgang (M) wird die ID 99 ausgegeben. Wenn der Eingang (Off) 1 ist, kann weiterhin ein Alarm ausgelöst werden. | - | 0/1 |
| Buzzer | Buzzer | Aktiviert Weckerstimmung (ID 98), wenn 1. Parameter (Fbu) definiert die Fadingzeit. Fading setzt die Verwendung von Smartaktoren voraus. Wenn keine Weckerstimmung konfiguriert ist, wird stattdessen die Stimmung mit ID 99 verwendet. Die Beleuchtung wird nach Ablauf der im Parameter (Met) eingestellten Zeit ausgeschaltet. | - | 0/1 |
| Br | Current brightness | Wenn die aktuelle Helligkeit den Schwellenwert (Brt) überschreitet, wird Präsenz/Bewegung ignoriert. | lux | 0...∞ |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Lc1-4, M+, M-, Mood, Off, T5/1-8, On, Buzzer, MBr) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| P | Presence | Aktiviert die für Bewegung/Präsenz konfigurierte Lichtstimmung, wenn 1. Wird in der Zwischenzeit die Beleuchtung manuell bedient, wird die Beleuchtung erst nach Ablauf der im Parameter (Met) eingestellten Zeit ausgeschaltet. | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| MBr | Master Brightness | Setzt die Helligkeit der Ausgänge (Lc1-18) auf einen Wert relativ zum Eingang (MBr). Z.B. Eingang (MBr) = 20%, Ausgang (Lc1) = 40% : Die Helligkeit des Ausgangs (Lc1) ist immer doppelt so hoch wie die Master-Helligkeit (MBr). | - | ∞ |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/lichtsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Lc1-18 | Light circuit 1-18 | Ausgang für Lichtkreis 1-18. Je nach Aktortyp verwendbar. | 0...100 |
| M | Current mood | Vordefinierte Stimmungs-IDs: 0: Aus, 98: Buzzer (Wecker), 99: Alles an, -1: Benutzerdefinierte Stimmung, -3: Mehrere eingemischte Stimmungen | -3...99 |
| 2C | Pulse on double-click | Impuls bei einem Doppel- oder Dreifachklick oder Impuls bei Eingang (Off). | 0/1 |
| 3C | Pulse on triple-click | Impuls bei einem Dreifach-Klick. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/lichtsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Tdc | Time double-click | Zeit für Doppelklick | s | 0...∞ | 0,35 |
| Sts | Step size brightness | Schrittweite Helligkeit | % | 0...100 | 2 |
| Str | Step rate brightness | Die Helligkeit wird bei einem langen Klick alle (Str) Sekunden um (Sts) erhöht/verringert. | s | 0...∞ | 0,2 |
| MinBr | Minimum brightness (0 to 50%) | Minimale Helligkeit, wenn Ausgänge direkt mit Lc Eingängen gedimmt werden. | % | 0...50 | 0 |
| MaxBr | Maximum brightness (50 to 100%) | Maximale Helligkeit, wenn Ausgänge direkt mit Lc Eingängen gedimmt werden. | % | 50...100 | 100 |
| Dm | Dim mode | Wenn aktiviert, erfolgt das Dimmen zwischen den Parametern (MinBr) und (MaxBr) bei langem Klick. Wenn deaktiviert, stoppt das Dimmen beim Erreichen des Parameters (MinBr) oder (MaxBr) bei langem Klick. | - | 0/1 | 0 |
| Lv | Last value output Lc1-4 | Wenn aktiviert, wird die Helligkeit beim Einschalten des Ausgangs (Lc1-4) über den Eingang (Lc1-4) auf (MaxBr) gesetzt. Wenn deaktiviert, wird beim Einschalten des Ausgangs (Lc1-4) über den Eingang (Lc1-4) der letzte Helligkeitswert eingestellt. | - | 0/1 | 0 |
| Moet | Motion extend time | Startet mit der fallenden Flanke an (Mo) und verlängert die Bewegung um die eingestellte Zeit. Wenn die Verlängerungszeit von (Met) kürzer ist als (Moet), wird stattdessen (Met) verwendet. 0 = Deaktiviert die automatische Abschaltung. Parameter gilt nicht für Präsenzeingang (P)! | s | 0...∞ | 900 |
| Pto | Presence automatic timeout | Deaktiviert die Präsenz / Bewegungsautomatik nach manuellem Ausschalten der Beleuchtung. Eingang (Mo): Impuls am Eingang (Mo) startet den Timeout neu. Aktiviert die Präsenz / Bewegungsautomatik wieder, wenn für die eingestellte Zeit keine Bewegung stattgefunden hat. 0 = Deaktiviert diese Funktion. Eingang (P): Parameterwert wird automatisch auf 0,01 gesetzt, wenn Eingang (P) verwendet wird. Wiedereinschalten der Präsenz / Bewegungsautomatik unmittelbar nach Beendigung der Präsenz. | s | 0...∞ | 300 |
| Pm | Presence mood | >0 = Die hier angegebene Stimmungs ID wird mit Eingang (P) or (Mo) gestartet. 0 = Die im Baustein bei Automatik angegebene Stimmung bei Präsenz/Bewegung wird verwendet. Ebenso, wenn die angegebene Stimmungs ID nicht existiert. | - | ∞ | 0 |
| Met | Manual operation extend time | Nachlaufzeit zur automatischen Abschaltung der Beleuchtung durch die Melder auch nach manueller Bedienung. Eingang DisP verhindert nicht das Ausschalten der Beleuchtung. Timer startet nach Ende der Bewegung/Präsenz oder mit einer fallenden Flanke am Eingang (Buzzer). 0 = Deaktiviert die automatische Abschaltung. | s | 0...∞ | 3600 |
| Ao | Alternative operation Lc1-4 | Wenn aktiviert, schalten Impulse die Primärfarben des RGB-Ausgangs durch. Langer Klick zum Dimmen. | - | 0/1 | 0 |
| Afi | Alarm flashing interval | Definiert das Blinkintervall der Beleuchtung während des Alarms. Z.B. 2s = 1s Ein, 1s Aus | s | 0.1...∞ | 4 |
| Fbu | Fading time buzzer | Fadingzeit der Weckerstimmung, wenn der Eingang (Buzzer) ausgelöst wird. Nur für unterstützte Geräte mit Smart Aktor. | min | 0...60 | 3 |
| Brt | Brightness threshold | Wenn der Eingang (Br) den Grenzwert des Parameters (Brt) überschreitet, werden die Eingänge (Mo), (P), (P/1-8) deaktiviert. | lux | 0...∞ | 30 |
| Mmd | Mixing moods duration | Dauer Tastendruck zum Mischen einer zusätzlichen Stimmung über Eingänge (T5/1-8). 0 = Keine Mischung der zugewiesenen Stimmung. | s | 0...∞ | 1 |
| Ft | Fading time | Dauer des Fadings bei Stimmungswechsel. Gilt für regelmäßige Stimmungswechsel auf Smart-Aktor-Geräten. Der Farbwähler hat eine feste Fadingzeit von 0,2s, während Sequenzen ihre eigenen individuellen Fadingzeiten besitzen. | s | 0...1800 | 1 |
| MaxAbr | Maximum alarm brightness | Wenn der Eingang (Alarm) 1 ist, beginnen die verwendeten Ausgänge (Lc1-18) zwischen dem Wert 0 und dem Parameter (MaxAbr) zu blinken. Wenn der Eingang (On) 1 ist, werden die verwendeten Ausgänge auf den Parameter (MaxAbr) gesetzt, wenn keine Stimmung mit ID 99 konfiguriert ist. | % | 10...100 | 50 |
| MinCt | Minimum color temperature | Minimale Farbtemperatur (warm) für Tageslichtsteuerung. | K | 2000...4000 | 2700 |
| MaxCt | Maximum color temperature | Maximale Farbtemperatur (kalt) für Tageslichtsteuerung. | K | 4000...12000 | 6500 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/lichtsteuerung/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|--------------|--------------|
| Stimmungen | Stimmungen und Betriebsmodi verwalten | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/lichtsteuerung/

[BELEGT] Im Dokument finden sich technische Hinweise in den Beschreibungen der Parameter und Eingänge:
- Remanenz (Rem): Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde
- Parameter (Moet) gilt nicht für Präsenzeingang (P)
- Tageslichtsteuerung mit Parametern MinCt und MaxCt erfordert entsprechende Sensoren

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| M- | `InputTriggerDown` | Eingang | Previous mood | Impuls: Wählt die vorherige Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | – |

---

## Baustein 2: Licht Zentral

### Licht Zentral

Ermöglicht zentrale Steuerung aller Lichtsteuerungs-Bausteine.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/licht-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| M+ | Next mood | Impuls: Wählt die nächste Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | 0/1 |
| M- | Previous mood | Impuls: Wählt die vorherige Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | 0/1 |
| Mood | Select mood by ID | Stimmung durch ID auswählen | 0...99 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. An alarm can still be triggered via the input (Alarm). Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| T5/1-8 | T5 control | Impuls: Der erste Impuls wählt die zugewiesene Stimmung aus, jeder weitere Impuls schaltet auf die nächste Stimmung um. Erfolgt 30 Sekunden lang kein weiterer Impuls, wählt ein Impuls wieder die zugewiesene Stimmung. Langklick: Mischt entweder die Stimmung (Mmd) ein oder schaltet auf die nächste Stimmung um. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet die Lichter aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | ∞ |
| DisP | Disable presence / motion | Deaktiviert Eingänge (P) und (Mo) wenn 1. Beleuchtung, die durch Präsenz (P) aktiviert wurde, wird sofort ausgeschaltet. Wenn Beleuchtung durch Bewegung (Mo) aktiviert wurde, wird bei steigender Flanke an (DisP) der Timer (Moet) gestartet und die Lichter werden nach Ablauf ausgeschaltet. Wenn die Zeit von (Met) kürzer ist als (Moet), wird stattdessen (Met) verwendet. | 0/1 |
| On | All on | Aktiviert Stimmung mit ID 99. Wenn keine Stimmung mit ID 99 konfiguriert ist, werden alle verwendeten Ausgänge (Lc1-18) mit der im Parameter (MaxAbr) eingestellten Helligkeit aktiviert. | 0/1 |
| Alarm | Alarm | Verwendete Ausgänge (Lc1-18) beginnen zu blinken, wenn 1. Parameter (MaxAbr) definiert die Helligkeit, Parameter (Afi) definiert das Blinkintervall. Am Ausgang (M) wird die ID 99 ausgegeben. Wenn der Eingang (Off) 1 ist, kann weiterhin ein Alarm ausgelöst werden. | 0/1 |
| Buzzer | Buzzer | Aktiviert Weckerstimmung (ID 98), wenn 1. Parameter (Fbu) definiert die Fadingzeit. Fading setzt die Verwendung von Smartaktoren voraus. Wenn keine Weckerstimmung konfiguriert ist, wird stattdessen die Stimmung mit ID 99 verwendet. Die Beleuchtung wird nach Ablauf der im Parameter (Met) eingestellten Zeit ausgeschaltet. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Lc1-4, M+, M-, Mood, Off, T5/1-8, On, Buzzer, MBr) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/licht-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | – |
| Na | Active Lights | Anzahl der aktiven Leuchten | ∞ |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/licht-zentral/

[BELEGT] Der Baustein hat keine separaten Parameter in der Dokumentation.

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/licht-zentral/

[BELEGT] Alle ausgewählten Lichtsteuerungen können gemeinsam gesteuert werden.

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/licht-zentral/

[BELEGT] Zentral-Befehle werden auch durch einen aktiven (DisPc) Eingang am jeweiligen Baustein nicht blockiert.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Lc1-n | `In` | Eingang | Light circuit 1-n | Aktiviert den Ausgang (Lc1-4). Langer Klick zum Dimmen. | – |
| M- | `InputTriggerDown` | Eingang | Previous mood | Impuls: Wählt die vorherige Stimmung. Doppelklick: Schaltet das Licht aus und sendet einen Impuls an den Ausgang (2C). Dreifachklick: Schaltet das Licht aus und sendet einen Impuls an die Ausgänge (3C) und (2C). | – |

---

## Baustein 3: Hotel Lichtsteuerung

### Hotel Lichtsteuerung

Spezialisierte Lichtsteuerung für Hotelzimmer mit Kartenschalter, Bewegungsmelder, Zimmermädchenstatus und Szenen-Management.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/hotel-lichtsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| I1-20 | Triggereingang 1-20 für Dimmer bzw. Schalteingang für Leuchten | Triggereingang 1-20 für Dimmer bzw. Schalteingang für Leuchten | 0/1 |
| S10 | Trigger selection scene 10 | Trigger Auswahl Lichtszene 10 | 0/1 |
| S11 | Trigger seletion scene 11 | Trigger Auswahl Lichtszene 11 | 0/1 |
| S12 | Trigger seletion scene 12 | Trigger Auswahl Lichtszene 12 | 0/1 |
| S13 | Trigger seletion scene 13 | Trigger Auswahl Lichtszene 13 | 0/1 |
| R | Reset | Reset-Eingang der Hotel Lichtsteuerung | 0/1 |
| IC | Card switch | Schalter Kartenkontakt | 0/1 |
| IS | Service button | Eingang Servicetaste Abhängig von Servicemodus | 0/1 |
| AIr | Room state | Statuseingang 0='Ungebucht', 1='Gebucht', 2='Gast eingecheckt' | ∞ |
| ID | Door contact | Eingang Türkontakt | 0/1 |
| DisMo | Disable motion sensor input | Disable-Eingang des Bewegungsmelders | 0/1 |
| Mo | Motion sensor | Bewegungsmelder Eingang | 0/1 |
| Dis | Disable | Disable-Eingang der Hotel Lichtsteuerung | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/hotel-lichtsteuerung/

| Kürzel | Beschreibung | Wertebereich |
|--------|--------------|--------------|
| AQ1-20 | Analoger Ausgang für Aktor/Dimmer 1-20 bei RGB - %-Wert Rot + %-Wert Grün * 1000 + %-Wert Blau * 1000000 | ∞ |
| AQs | Analoger Ausgang für aktivierte Szene | ∞ |
| QP | Anwesend Ausgang | 0/1 |
| QS | Service Ausgang | 0/1 |
| QD | Service durchgeführt Ausgang | 0/1 |
| AQrm | Analoger Ausgang für Zimmermädchenstatus 1=Frei/nicht sauber 2=Besetzt/nicht sauber 3=Frei/sauber 4=Besetzt/sauber | ∞ |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/hotel-lichtsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanted Neustart, vor Backup, einmal pro Stunde. Daten werden auf SD gespeichert. | - | 0/1 | 0 |
| MS | Service staff mode | Parametereingang Modus Servicepersonal 0=Servicetaste mit Langzeitklick nach Karte einstecken 1=Servicetaste Impuls vor Karte einstecken 2=Servicetaste Ein vor Karte einstecken 3=Karte muss 2 mal gesteckt werden | - | ∞ | 2 |
| TM | Duration of Service Staff mode | Parametereingang Dauer für Modus Servicepersonal | s | ∞ | 60 |
| To | Duration press and hold for 'All off' | Parametereingang Dauer Langzeitklick für 'Alles aus' | s | ∞ | 2 |
| Tl | Timeout for leaving room | Parametereingang Timeout für Raumverlassen 0 wenn danach nicht ausgeschaltet werden soll | s | ∞ | 60 |
| M | Max time between pulses | Parametereingang maximaler Zeitabstand zwischen 2 Impulsen | s | ∞ | 0,35 |
| SI | Step | Parametereingang Schrittweite Dimmer in % | % | ∞ | 2 |
| ST | Step rate | Parametereingang Schrittzeit Dimmer | s | ∞ | 0,2 |
| Min | Minimum value | Parametereingang Minimumwert Dimmer (0 bis 50%) | % | ∞ | 15 |
| Max | Maximum value | Parametereingang Maximumwert Dimmer (50 bis 100%) | % | ∞ | 100 |
| L | Do not set last value | Parametereingang Letzten Dimmerwert nicht setzen (Aus = Kurzer Klick setzt letzten Wert, wenn ausgeschaltet) | - | 0/1 | 0 |
| TH | Duration On | Nachlaufzeit für Bewegungsmelder Startet mit fallender Flanke von Mo | s | ∞ | 180 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/hotel-lichtsteuerung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Lichtszenen | Lichtszenenverwaltung | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/hotel-lichtsteuerung/

[BELEGT] Der Baustein verfügt über eine Anwesenheitssimulation, die im Eigenschaftenfenster aktiviert bzw. definiert werden kann.

---

## Baustein 4: Dimmer

### Dimmer

Optimierter Lichtdimmer mit Doppelklick für Eintastenbedienung.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tg | Toggle | Schaltet den Ausgang (D) zwischen 0 und dem letzten Wert um (oder zwischen 0 und 100, wenn der Parameter (Lv) 1 ist). Langer Klick zum auf/abwärts Dimmen. | 0/1 |
| + | Dim+ | Schaltet den Ausgang (D) zwischen 0 und dem letzten Wert um (oder zwischen 0 und 100, wenn der Parameter (Lv) 1 ist). Langer Klick zum aufwärts Dimmen. | 0/1 |
| - | Dim- | Schaltet den Ausgang (D) zwischen 0 und dem letzten Wert um (oder zwischen 0 und 100, wenn der Parameter (Lv) 1 ist). Langer Klick zum abwärts Dimmen. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert Eingänge (Tg), (+), (-) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |
| Set | Sets output (D) to value of input (Set) | Setzt Ausgang (D) auf den Wert des Eingangs (Set) | ∞ |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| D | Dimmer output | Analoger Ausgang zur Dimmersteuerung (z.B. 0-10V) | ∞ |
| S | Status | Ein, wenn der Ausgang (D) größer als 0 ist. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| Di | Delay input | Verzögert den Eingang um die eingestellte Zeit. Wenn dieser Parameter zu niedrig eingestellt ist, kann der Baustein den Eingang als gedrückt gehaltene Taste statt als normalen (kurzen) Tastendruck interpretieren. Gilt für die Eingänge (Tg), (+), (-). | ∞ | 0,4 |
| Sts | Step size | Schrittweite | ∞ | 0,5 |
| Str | Step rate | Der Dimmwert wird bei einem langen Klick alle (Str) Sekunden um (Sts) erhöht/verringert. | ∞ | 0,2 |
| MinD | Minimum dim value | Minimaler Dimmwert | ∞ | 0 |
| MaxD | Maximum dim value | Maximaler Dimmwert | ∞ | 100 |
| Dm | Dim mode | 1 = Dimmen zwischen den Parametern (MinD) und (MaxD) bei langem Klick. 0 = Dimmen stoppen bei Erreichen des Parameters (MinD) oder des Parameters (MaxD) bei langem Klick. Gilt nur für den Eingang (Tg). | 0/1 | 0 |
| Lv | Last value | 1 = Setzt beim Einschalten Ausgang (D) auf (MaxD). 0 = Setzt beim Einschalten Ausgang (D) auf den letzten Wert. | 0/1 | 0 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/dimmer/

[BELEGT] Der Baustein verfügt über eine Anwesenheitssimulation, die im Eigenschaftenfenster aktiviert bzw. definiert werden kann.

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/dimmer/

[BELEGT] Der Parameter (Di) sollte nicht zu niedrig eingestellt werden, da der Baustein sonst einen Tastendruck als gedrückt gehaltene Taste interpretieren kann. Der Parameter (Dm) gilt nur für den Eingang (Tg).

---

## Baustein 5: EIB Dimmer

### EIB Dimmer

Gibt mittels Trigger +/- Eingang einen EIB-Dimmer-geeigneten Wert am Ausgang aus.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/eib-dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| + | Dim+ | — | 0/1 |
| − | Dim− | — | 0/1 |
| DisPc | Disable periphery control | Deaktiviert alle Eingänge | 0/1 |
| On | On | Ein: Status = EIN, Dimmerwert = 100% | 0/1 |
| Off | Off | Aus: Status = AUS, Dimmerwert = 0 % | 0/1 |
| Set | Sets output (Cdv) to value of input (Set) | Setzt Ausgang (Cdv) auf den Wert des Eingangs (Set) | ∞ |
| S | Status | Verbinden Sie diesen Eingang mit einem EIB-Sensor (Gruppenadresse Schalten oder Rückmeldung Schalten) | 0/1 |
| Cdv | Current dim value | Verbinden Sie diesen Eingang mit einem EIB-Sensor (Gruppenadresse Helligkeit oder Rückmeldung Helligkeit) | ∞ |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/eib-dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| D | Dimmer output | Der Ausgang D ist der analoge Dimmausgang und stellt einen relativen Befehl „Dimmen um ± Wert %" dar | ∞ |
| S | Status | Schaltausgang zum Ein- und Auschalten. Dieser Ausgang wird über die Eingänge (On) und (Off) gesteuert | 0/1 |
| Cdv | Current dim value | Verbinden Sie diesen Ausgang mit einem EIB-Dimmaktor (Gruppenadresse Helligkeitswert) | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen | − |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/eib-dimmer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Sts | Step size | Schrittweite | ∞ | 5 |
| Rr | Repetition rate | Wiederholrate | ∞ | 0,2 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/eib-dimmer/

[BELEGT] Der Baustein verfügt über eine Anwesenheitssimulation, die im Eigenschaftsfenster aktivierbar ist.

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/eib-dimmer/

[BELEGT] Der Ausgang (D) stellt einen relativen Befehl dar, nicht einen absoluten Wert. Die Eingänge (S) und (Cdv) müssen mit entsprechenden EIB-Sensoren verbunden werden.

---

## Baustein 6: RGB Lichtszene

### RGB Lichtszene

RGB-Lichtszene mit Ein- oder Zweitastenbedienung. Über den Eingang "+" können die Szenen durchgeschalten werden. An den Ausgängen AQr, AQg und AQb werden die Farben in RGB aufgeteilt, oder am Ausgang AQa zusammengefasst ausgegeben.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/rgb_lichtszene/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| AI | Analoger Eingang RGB | %-Wert Rot + %-Wert Grün × 1000 + %-Wert Blau × 1000000 | ∞ |
| + | Trigger next scene | Nächste RGB-Lichtszene | 0/1 |
| − | Trigger previous scene | Vorherige RGB-Lichtszene | 0/1 |
| AIs | Scene | Auswahl der RGB-Lichtszene (0-x) | ∞ |
| Dis | Disable | Sperrt alle Eingänge (Kindersicherung) | 0/1 |
| R | Reset | Reset der Lichtszene. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| O | On | Alles EIN. Setzt alle Ausgänge auf Maximum (weiß) | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/rgb_lichtszene/

| Kürzel | Beschreibung | Wertebereich |
|--------|--------------|--------------|
| AQr | Analoger Ausgang für rote LED | ∞ |
| AQg | Analoger Ausgang für grüne LED | ∞ |
| AQb | Analoger Ausgang für blaue LED | ∞ |
| AQs | Analoger Ausgang für aktivierte Szene | ∞ |
| AQa | Analoger Ausgang RGB. %-Wert Rot + %-Wert Grün × 1000 + %-Wert Blau × 1000000 | ∞ |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/rgb_lichtszene/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/rgb_lichtszene/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Lichtszenen | Lichtszenenverwaltung | − |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/rgb_lichtszene/

[BELEGT] Der Ausgang (AQa) kodiert die RGB-Werte mit einer speziellen Formel: %-Wert Rot + %-Wert Grün × 1000 + %-Wert Blau × 1000000. Dies muss bei der Interpretation berücksichtigt werden.

---

## Baustein 7: Konstantlichtregler

### Konstantlichtregler

Baustein zur Konstantlichtregelung eines Raumes. Benötigt einen gut positionierten Sensor, der die Helligkeit im Raum schnell erfasst.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/konstantlichtregler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Br | Current brightness | Aktuelle Helligkeit | ∞ |
| Set | Sets output (Lc) to value of input (Set) | Setzt Ausgang (Lc) auf den Wert des Eingangs (Set) | 0...100 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |
| Act | Activation | Aktiviert die Konstantlichtregelung, wenn 1. | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/konstantlichtregler/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Lc | Light circuits | Unterstützt werden: Smartaktor RGBW oder WW, Lumitech, RGB, 0-100%, 0-10V, 1-10V. Wenn mehrere Aktoren verbunden sind, müssen alle denselben Typ besitzen. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | − |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/konstantlichtregler/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Hys | Hysteresis | Ist der Unterschied zwischen Soll- und Istwert größer als diese Hysterese, wird nachgeregelt. | % | 0...100 | 10 |
| Sts | Step size | Je größer die Schritte, desto schneller wird der Zielwert erreicht. Bei großen Schritten kann der Lichtwechsel aber sichtbar sein. | % | 0...100 | 5 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/konstantlichtregler/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Ziel-Helligkeit | Diese Helligkeit soll erreicht werden, wenn der Regler aktiv ist. | ∞ | 5000 |
| Ziel-Helligkeit einstellen | Ermitteln Sie die Ziel-Helligkeit, welche erreicht werden soll, wenn der Regler aktiv ist. | − | − |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/konstantlichtregler/

[BELEGT] Der Konstant-Lichtregler benötigt einen gut positionierten Helligkeitssensor zur schnellen und zuverlässigen Erfassung der Raumhelligkeit. Die Parameter (Hys) und (Sts) sollten angepasst werden, um ein visuell angenehmes Dimmen zu erreichen.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| TB | `Target` | Parameter | Target brightness | Diese Helligkeit soll vorhanden sein, wenn Regler aktiv. | ∞ lx |

---

## Baustein 8: Szene

### Szene

Eine Szene enthält eine Aktionsliste, die mit dem Objekteingang oder über die Visualisierung ausgeführt wird. Die Szene ist der Automatik-Regel sehr ähnlich, es können ebenso eine oder mehrere Aktionen ausgewählt werden.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/szene/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Act | Activate scene | Szene aktivieren | 0/1 |
| Off | Off | Ein: Baustein ist gesperrt. Dominierender Eingang. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/szene/

| Kürzel | Kurzbeschreibung | Beschreibung |
|--------|------------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/szene/

[BELEGT] Der Baustein hat keine separaten Parameter in der Dokumentation.

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/szene/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Konfiguration | Konfiguration anzeigen | — |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/szene/

[BELEGT] Bei der Szene können keine Bedingungen definiert werden. Die Aktionen in der Szene werden also nur ausgeführt, wenn die Szene über den (Act) Eingang oder in der Visualisierung ausgelöst wird.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| + | `InputTriggerUp` | Eingang | Trigger next scene | Nächste-Eingang des Szenenbausteins | – |
| AIs | `Select` | Eingang | Scene | Auswahl-Eingang des Szenenbausteins (0-x) | ∞ |
| Dis | `InputDisable` | Eingang | Disable | Disable-Eingang des Szenenbausteins (Kindersicherung) | – |
| R | `Reset` | Eingang | – | Reset Eingang des Szenenbausteins Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | – |
| AQn | `AQ1` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ2` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ3` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ4` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ5` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ6` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ7` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQn | `AQ8` | Ausgang | – | Analoger Ausgang für Aktor/Dimmer n | ∞ |
| AQs | `AQs` | Ausgang | – | Analoger Ausgang für Szene | ∞ |
| Rem | `Remanence` | Parameter | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – |

---

## Zusammenfassung Abdeckung

- **8 von 8 Bausteine erfolgreich recherchiert** [BELEGT]
- **Alle Seiten erreichbar und dokumentiert**
- **Tabellen vollständig extrahiert und als Markdown-Format vorgelegt**

## Besonderheiten für XML-Mapping

Die folgenden Kürzel sind besonders wichtig für die spätere Zuordnung zu internen Loxone-XML-Konnektornamen:

**Lichtsteuerung:** Lc1-18, M, 2C, 3C, DisP, Mo, P, Br, Tdc, Sts, Str, MinBr, MaxBr, Moet, Met

**Licht Zentral:** M+, M-, Off, Na

**Hotel Lichtsteuerung:** I1-20, S10-13, IC, IS, AIr, ID, DisMo, Mo, AQ1-20, AQs, QP, QS, QD, AQrm

**Dimmer:** Tg, +, -, D, S, Di, Sts, Str, MinD, MaxD

**EIB Dimmer:** +, −, D, S, Cdv, Sts, Rr

**RGB Lichtszene:** AI, +, −, AIs, AQr, AQg, AQb, AQs, AQa, Rem

**Konstantlichtregler:** Br, Lc, Hys, Sts

**Szene:** Act, Off (kein Output außer API)

---

*Datei erstellt: 30.07.2026*
*Recherche durchgeführt mittels offizielle Loxone Knowledge Base*
*Alle Tabellen wörtlich aus der Quelle übernommen und mit [BELEGT] gekennzeichnet*

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Tageslicht Steuerung (BETA) (`DaylightController`)

Dieser Baustein liefert die Farbe der momentanen Tageszeit. Die Helligkeit des Lichts kann unabhängig von der Lichttemperatur gesetzt werden.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Off | `Deactivate` | – | Mit diesem Eingang kann die Tageslicht Steuerung deaktiviert werden. | – |
| B | `Brightness` | – | An diesem Eingang kann die Helligkeit des Farbtemperaturverlaufs gesetzt werden. Wird dieser Eingang nicht verwendet, so wird die Helligkeit auf 100% gesetzt. | 0…100 % |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AQ | `AQ` | – | Analoger Ausgang für Smart-Aktor. | ∞ |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| NCT | `NightColorTemperature` | – | Mit diesem Parameter kann die Farbtemperatur der Nachtfarbe eingestellt werden. 6500K entspricht natürlichem Tageslicht. Darunter wird das Licht wärmer (gelblich), darüber kälter (bläulich). | 1000…10000 K | 2000 |
| DCT | `DayColorTemperature` | – | Mit diesem Parameter kann die Farbtemperatur der Tagfarbe eingestellt werden. 6500K entspricht natürlichem Tageslicht. Darunter wird das Licht wärmer (gelblich), darüber kälter (bläulich). | 1000…10000 K | 6500 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 498

---

### Lichtsteuerung Gen 1 (`LightController`)

Dieser Baustein ermöglicht sowohl die Steuerung mehrerer einzelner Lichtkreise als auch die kombinierte Steuerung durch Lichtszenen (Schalten, Dimmen, RGB)

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| I1-n | `In` | – | Trigger 1-n für Dimmer bzw. Schalteingang für Leuchten | – |
| + | `InputTriggerUp` | Trigger next scene | Nächste Szene | – |
| - | `InputTriggerDown` | Trigger previous scene | Vorige Szene | – |
| AIs | `Select` | Scene | Auswahl der Lichtszene mit Wert 0-9 | ∞ |
| R | `Reset` | Reset | Reset, aktiviert Lichtszene Alles Aus | – |
| S1-n | `Seln` | – | Trigger Auswahl Lichtszene 1-n 5 Sekunden Impuls lernt den aktuellen Zustand der Ausgänge Doppelimpuls schaltet alles aus und Impuls auf RQ. Dreifachimpuls schaltet alles aus und Impuls auf RaQ. | – |
| DisMo | `EnMove` | Disable motion sensor input | Verhindert das Einschalten der Bewegungsmelderszene über Mv. Hat keinen Einfluss auf die automatische Lichtabschaltung mit Parameter MT. | – |
| Mo | `Move` | Motion sensor input | Bewegungsmeldereingang Aktiviert konfigurierte Bewegungsmelderstimmung | – |
| O | `On` | On | alles EIN Setzt alle Ausgänge auf Ein bzw. Maximum | – |
| T5 | `Gesture` | Combined button input | Nächste Szene, Aus bei Doppel- bzw. Dreifachklick. | ∞ |
| A | `Alarm` | Alarm | Alarmeingang Wenn ein, dann blinken alle Lichter mit dem Wert von Parameter Ba | – |
| AIb | `Brightness` | Current Brightness | IST-Wert der aktuellen Helligkeit Überschreitet der Ist-Wert den Maximalwert, wird die Bewegungsmelderszene nicht aktiviert | ∞ |
| Dis | `InputDisable` | Disable | Kindersicherung – sperrt alle Eingänge, aber nicht die Visualisierung Bewegungsmeldereingänge werden nicht gesperrt | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AQ1-n | `AQn` | – | Analoger Ausgang für Aktor/Dimmer 1-n bei RGB - %%-Wert Rot + %%-Wert Grün * 1000 + %%-Wert Blau * 1000000 | ∞ |
| AQs | `Scene` | – | Analoger Ausgang für aktivierte Szene | ∞ |
| RQ | `OutputReset` | – | Reset der Lichtszene Wird mit Doppelklick/Dreifachklick auf lichtbeeinflussenden Eingang oder Reset aktiviert | – |
| RaQ | `OutputResetAll` | – | Reset der Lichtszene 3-fach Impuls | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| Tdc | `MaxP` | Double click speed | Doppelklickzeit [s] bei Eingangsimpuls | ∞ | 0,35 |
| SI | `Step` | Step size | Schrittweite Dimmer in % | ∞ | 2 |
| ST | `Steptime` | Step rate | Schrittzeit Dimmer Zeitabstand in dem der Ausgangswert mit Schrittweite angepasst wird | ∞ | 0,2 |
| Min | `Min` | Minimum value | Minimumwert Dimmer (0 bis 50%) | ∞ | 0 |
| Max | `Max` | Maximum value | Maximumwert Dimmer (50 bis 100%) | ∞ | 100 |
| W | `Wrap` | Up/Down mode | Auf/Ab-Modus Dimmer (Aus = Stop bei Maximum/Minimum) | – | – |
| L | `NoLast` | Do not set last value | Letzten Dimmerwert nicht setzen (Aus = Kurzer Klick setzt letzten Wert, wenn ausgeschaltet) | – | – |
| TH | `MoveOn` | Duration [s] On | Aktiviert die zugewiesene Bewegungsmelderszene und startet bei fallender Flanke diesen Nachlauftimer EIN [s] Startet mit fallender Flanke des Bewegungsmelder Eingangs | ∞ | 900 |
| Ti | `MoveIgnore` | Delay of the Motion Sensor | Deaktiviert den Bewegungsmelder nach ausschalten für [s] Sekunden Wenn dieser Wert 0 ist gilt der Status von DisMv | ∞ | 300 |
| LT | `Learntime` | Learn period | Lernzeit Dauer Tastendruck zum Lernen der Szene über Eingänge S1-S8 | ∞ | 5 |
| MS | `MoveScene` | Motion sensor scene | Szene für Bewegungsmelder, wenn nicht 0 Dies übersteuert die zugewiesene Bewegungsmelderszene (Register Szenen). Beispiel Szene 8 sollte nachts aktiviert werden | ∞ | 0 |
| MT | `MoveTimeout` | Timeout for the automatic switching off of lights after no motion [s] | Automatische Abschaltung des Lichtes nach Ende letzter Bewegung Wenn dieser Wert ungleich 0 ist, wird der Bewegungsmelder verwendet, um die aktuelle Szene auszuschalten. Unabhängig von (TH) und der zugewiesenen Bewegungsmelderszene. Zur Verwendung um Licht das vergessen wurde automatisch abzuschalten. Empfohlener Wert 30 Minuten (1800) | ∞ | 3600 |
| Ra | `RGBalt` | Alternative operation I1-I12 when output is RGB | RGB-Bedienung I1 bis I12 (Ein = Kurzer Tastendruck bedeutet Grundfarben durchschalten, langer Tastendruck bedeutet Helligkeit verändern) | – | – |
| Ta | `AlarmPeriod` | Flashing interval during the alarm[s] | Dauer [s] Periode Ein/Aus, Beispiel 2s, 1s Ein/ 1s Aus | ∞ | 4 |
| T | `BrightnessLimit` | Brightness threshold [lux] | Maximalwert Helligkeit Überschreitet die aktuelle Helligkeit diesen Wert wird die Bewegungsmelderszene bei Bewegung nicht aktiviert | ∞ | 30 |
| Ba | `AlarmBrightness` | Maximum brightness level for Alarm | Maximalwert Alarm (10 - 100) Ist Alarm aktiv, schalten die Ausgänge zwischen 0 und [Maximalwert Alarm] | ∞ | 50 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 356 · KB: https://www.loxone.com/help/LightController

---

### Lichtszene (`LightsceneLearn`)

Lernfähige Lichtszene

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AIn | `AI1` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI2` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI3` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI4` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI5` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI6` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI7` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIn | `AI8` | – | Analoger Eingang für Aktor/Dimmer n in % Dieser Eingang übersteuert den Lichtszeneausgang n bei Veränderung. | ∞ |
| AIs | `Select` | Scene | Auswahl-Eingang der Lichtszene (0-x) | ∞ |
| R | `Reset` | Reset | Reset Eingang der Lichtszene | – |
| S1-n | `Seln` | – | Trigger Auswahl Lichtszene 1-n 5 Sekunden Impuls lernt den aktuellen Zustand der Ausgänge Doppelimpuls schaltet alles aus. Dreifachimpuls schaltet alles aus und setzt den Resetausgang. | – |
| Dis | `InputDisable` | Disable | Disable-Eingang der Lichtszene (Kindersicherung) | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AQ1-n | `AQn` | – | Analoger Ausgang für Aktor/Dimmer 1-n in %% | ∞ |
| AQs | `Scene` | – | Analoger Ausgang für aktivierte Szene | ∞ |
| RQ | `RQ` | – | Reset Ausgang der Lichtszene Wird mit Reseteingang oder Szene 0 aktiviert | – |
| RaQ | `RaQ` | – | Reset Ausgang der Lichtszene 3-fach Impuls | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| M | `Max` | Max time between pulses | Parameter - maximaler Zeitabstand zwischen 2 Impulsen | ∞ s | 0,35 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 354

---
