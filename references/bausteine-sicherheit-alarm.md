# Sicherheit, Alarm & Präsenz
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

### Alarmanlage

Zentrale Alarmanlage zur Verwaltung von Fenster-, Tür-, Glas- und Präsenzsensoren mit Alarmstufen (stil, akustisch, optisch, intern, extern, fern).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Presence | Alarmeingang für Präsenzerkennung. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Gb | Glass breakage | Alarmeingang für Glasbrucherkennung. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Wc | Window contacts | Alarmeingang für Fensterkontakte (0 = geschlossen, 1 = offen). Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Dc | Door contacts | Alarmeingang für Türkontakte (0 = geschlossen, 1 = offen). Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Ot | Other | Alarmeingang für zusätzliche Sensoren und Melder. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Tg | Toggle with presence detection | Schaltet zwischen scharf/unscharf um. Präsenzmelder werden zum Auslösen eines Alarms verwendet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Tgnp | Toggle without presence detection | Schaltet zwischen scharf/unscharf um. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. | 0/1 |
| A | Arm with presence detection | Schaltet die Alarmanlage scharf. Präsenzmelder werden zum Auslösen eines Alarms verwendet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Anp | Arm without presence detection | Schaltet die Alarmanlage scharf. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Ad | Arm delayed with presence detection | Schaltet das Alarmsystem mit einer Verzögerung (Ard) scharf. Präsenzmelder werden zum Auslösen eines Alarms verwendet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Adnp | Arm delayed without presence detection | Schaltet das Alarmsystem mit einer Verzögerung (Ard) scharf. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Ca | Confirm alarm | Bestätigt den aktuellen Alarm und setzt alle Alarmausgänge zurück. Die Alarmanlage bleibt scharf. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tg), (Tgnp), (A), (Anp), (Ad), (Adnp) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| S | Status | 0 = Entschärft; 1 = Aktiviert mit Bewegungsmeldern; 2 = Aktiviert ohne Bewegungsmelder | - | 0...2 |
| Sa | Silent alarm | Stiller Alarm | - | 0/1 |
| Aa | Audible alarm | Akustischer Alarm | - | 0/1 |
| Va | Visual alarm | Optischer Alarm | - | 0/1 |
| Ia | Internal alarm | Interner Alarm | - | 0/1 |
| Ea | External alarm | Externer Alarm | - | 0/1 |
| Ra | Remote alarm | Ferner Alarm | - | 0/1 |
| N | Number of active sensors | Anzahl aktive Melder | - | ∞ |
| At | Alarm test | Wird nur verwendet wenn der Parameter Atm = 1 ist. | - | 0/1 |
| Rtad | Remaining time arming delay | Restzeit Aktivierungsverzögerung | s | 0...∞ |
| Ca | Cause of alarm | Meldet die Ursache des letzten Alarms. | - | - |
| Ta | Time and date of alarm | Meldet Datum und Uhrzeit des letzten Alarms. | - | - |
| WDs | Window / door state | Ein, wenn Fenster oder Türen geöffnet sind. Wenn der Parameter (Aoc) 1 ist: Offene Fenster/Türen werden ignoriert und die Eingänge (Wc & Dc) beim Scharfschalten auf 0 gesetzt. | - | 0/1 |
| WDot | Text output for open windows / doors | Gibt die Namen der Fenster und Türen aus, die während der Scharfschaltung geöffnet waren. (Der Ausgang kann mit einem TTS-Eingang verbunden werden.) | - | - |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde – Bei Aktivierung/Deaktivierung einer Alarmanlage (max. alle 10s) Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Ard | Arming delay | Verzögerung Aktivierung | s | 0...∞ | 600 |
| Sad | Silent alarm delay | Verzögerung stiller Alarm | s | 0...∞ | 0 |
| Aad | Audible alarm delay | Verzögerung akustischer Alarm | s | 0...∞ | 20 |
| Vad | Visual alarm delay | Verzögerung optischer Alarm | s | 0...∞ | 40 |
| Iad | Internal alarm delay | Verzögerung interner Alarm | s | 0...∞ | 90 |
| Ead | External alarm delay | Verzögerung externer Alarm | s | 0...∞ | 150 |
| Rad | Remote alarm delay | Verzögerung ferner Alarm | s | 0...∞ | 300 |
| Eip | Extension of alarm input pulses | Definiert die Mindestdauer, wie lange Alarmeingangsimpulse aktiv bleiben. Wird zur Berechnung der Anzahl aktiver Sensoren am Ausgang (N) verwendet. 0 = Jeder Impuls erhöht den Wert am Ausgang (N) nur so lange, wie er aktiv ist. | s | 0...∞ | 0 |
| Spt | Second presence sensor time window | Definiert das Zeitfenster, innerhalb dessen ein zweiter Präsenzmelder auslösen muss, damit der Alarm aktiviert wird. Wenn nur ein Präsenzmelder verwendet wird, hat dieser Parameter keine Wirkung und der Alarm wird sofort ausgelöst. 0 = Funktion wird nicht verwendet | s | 0...∞ | 900 |
| Atm | Alarm test mode | 1 = Nur der Ausgang (At) wird ausgelöst, wenn der Alarm aktiv ist. | - | 0/1 | 0 |
| MaxA | Maximum alarm duration | Der Alarm wird am Ende der eingestellten Dauer auf einen stillen Alarm zurückgesetzt. 0 = Keine Begrenzungsdauer Die maximale Alarmdauer sollte länger sein als die längste Alarmverzögerung, sonst werden bestimmte Alarmstufen nie aktiviert! | s | 0...∞ | 900 |
| Sac | Silent alarm confirmation | 1 = Der stille Alarm wird quittiert, wenn die maximale Alarmdauer (MaxA) erreicht ist. | - | 0/1 | 0 |
| Aoc | Arm open contact | 0 = Der Alarm wird ausgelöst, wenn ein Fenster oder eine Tür während des Scharfschaltens geöffnet ist. 1 = Der Alarm wird nur ausgelöst, wenn sich der Zustand (Offen/Geschlossen) einer Tür oder eines Fensters ändert, während die Anlage scharfgestellt ist. | - | 0/1 | 0 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmanlage/

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|--------------|---------|--------------|--------------|
| Unterdrückung Ausgänge | Unterdrückung aller nicht verbundenen Ausgänge Aa-Ra. Der stille Alarm kann nicht unterdrückt werden! | - | - | - |
| Wartezeit nach Start | Verzögerung der Aktivierung nach Neustart des Programms. Ein Wert unter 10 kann zu Fehlalarmen bei Neustart des Miniservers führen! Dies betrifft nur eine aktivierte Alarmanlage mit Remanenz! | s | 0...3600 | - |
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | - | 2...100 | - |
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge. | - | - | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmanlage/

- "Wenn die Alarmanlage scharf gestellt wird, während der Präsenzmelder noch Anwesenheit erkennt, wird die aktive Bewegung sofort den Alarm auslösen. Daher ist es entscheidend, das System mit einer Verzögerung zu aktivieren, um Fehlalarme zu vermeiden."
- "Die maximale Alarmdauer sollte länger sein als die längste Alarmverzögerung, sonst werden bestimmte Alarmstufen nie aktiviert!"
- "Ein Wert unter 10 [Wartezeit nach Start] kann zu Fehlalarmen bei Neustart des Miniservers führen!"

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| DisP | `DisMv` | Eingang | Disable motion sensor input I1 | Bewegungsmeldereingang I1 deaktivieren | – |

---

### Alarmanlage Zentral

Zentrale Steuerung mehrerer Alarmanlagen-Bausteine (Gruppenschaltung).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarm-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle with presence detection | Schaltet zwischen scharf/unscharf um. Präsenzmelder werden zum Auslösen eines Alarms verwendet. | 0/1 |
| Tgnp | Toggle without presence detection | Schaltet zwischen scharf/unscharf um. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. | 0/1 |
| A | Arm with presence detection | Schaltet die Alarmanlage scharf. Präsenzmelder werden zum Auslösen eines Alarms verwendet. | 0/1 |
| Anp | Arm without presence detection | Schaltet die Alarmanlage scharf. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. | 0/1 |
| Ad | Arm delayed with presence detection | Schaltet das Alarmsystem mit einer Verzögerung (Ard) scharf. Präsenzmelder werden zum Auslösen eines Alarms verwendet. | 0/1 |
| Adnp | Arm delayed without presence detection | Schaltet das Alarmsystem mit einer Verzögerung (Ard) scharf. Präsenzmelder werden nicht zum Auslösen eines Alarms verwendet. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Ca | Confirm alarm | Bestätigt den aktuellen Alarm und setzt alle Alarmausgänge zurück. Die Alarmanlage bleibt scharf. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tg), (Tgnp), (A), (Anp), (Ad), (Adnp) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarm-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |
| Na | Active Armed Alarms | Anzahl der aktiven scharf geschalteten Alarme | ∞ |

#### Parameter [OFFEN]
Quelle: https://www.loxone.com/dede/kb/alarm-zentral/

Diese Baustein hat in der Dokumentation keine explizite Parameter-Tabelle.

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarm-zentral/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Auswahl | Alle ausgewählten Alarmanlagen Bausteine können gemeinsam gesteuert werden. | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarm-zentral/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert.

---

### Alarmierungskette

Eskalierendes Alarmierungssystem mit Stufen 1-10, mit konfigurierbaren Reaktionszeiten und Notruf-Integration.

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| A | Alarm | Ein: Alarm Start, Aus: Alarm Ende | 0/1 |
| Au | Urgent alarm | Ein: Aktiviert Alarm an allen Ausgängen (A1-10), Aus: Deaktiviert Alarm an allen Ausgängen (A1-10). Wenn (A) und (Au) Ein sind, ist (Au) dominierend. | 0/1 |
| AEs | Alarm emergency service | Ein: Notalarm beginnt, Aus: Notalarm endet, wenn (A) und (Au) Aus sind. | 0/1 |
| T1-3 | Alarm texts 1-3 | Kann im Alarmtext an den Ausgängen (A1-10) verwendet werden. | - |
| Ca | Confirm alarm | Impuls: Setzt alle Alarmausgänge zurück. Ein = Alarmausgänge sind gesperrt. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| A1-10 | Alarm chain stage 1-10 | Textausgabe für Stufe 1-10 der Alarmierungskette. Wird übersprungen, wenn nicht angeschlossen. | - |
| AEs | Alarm text emergency services | Ein, wenn die Alarmierungskette ihre maximale Wiederholung (MaxR) erreicht hat oder wenn der Eingang (AEs) aktiviert ist. | - |
| As | Current alarm stage | Nummer der aktuellen Stufe der Alarmierungskette (A1-10) -1 = Alle Alarmstufen aktiv | -1...10 |
| Ton | Time of last alarm start | Zeitpunkt des letzten Alarmstarts | - |
| Toff | Time of last alarm stop | Zeitpunkt des letzten Alarmstopps | - |
| Cc | Cause of confirmation | Grund der Bestätigung | - |
| Tc | Time of confirmation | Zeit der Bestätigung | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rt | Reaction time | Zeit, bevor die nächste Stufe aktiviert wird. Wenn der Eingang (Au) aktiviert ist, bezieht sich dieser Parameter auf die Dauer, bevor die Ausgänge wieder aktiviert werden. 0 = Alle Alarmausgänge werden gleichzeitig und nur einmal aktiviert. | s | 0...∞ | 60 |
| MaxR | Maximum repetitions | Die maximale Anzahl der Wiederholungen der Alarmierungskette. 0 = Unbegrenzte Wiederholungen | - | 0...∞ | 4 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Notfalldienst Alarmtext | Wird am Ausgang (AEs) ausgegeben, wenn dieser aktiv ist. Ist dieser Text leer wird der normale Alarmtext verwendet. Folgende Kürzel können verwendet werden: <vn>: Name des Bausteins <vt1> - <vt3>: Text an den Eingängen (T1-3) <vton>: Startzeit der Alarmierung beim Aktivieren von (A) oder (Au) <vcn>: Name des Kunden aus den Projekteinstellungen <vca>: Adresse des Kunden aus den Projekteinstellungen | - |
| Alarmtext | Wird an den Ausgängen (A1-10) ausgegeben, wenn diese aktiv sind. Folgende Kürzel können verwendet werden: <vn>: Name des Bausteins <vt1> - <vt3>: Text an den Eingängen (T1-3) <v1> - <v3>: Wert ohne Nachkommastellen an den Eingängen (T1-3) <v1.2> - <v3.2>: Wert mit 2 Nachkommastellen an den Eingängen (T1-3) <vton>: Startzeit der Alarmierung beim Aktivieren von (A) oder (Au) <vcn>: Name des Kunden aus den Projekteinstellungen <vca>: Adresse des Kunden aus den Projekteinstellungen <vtes>: Zeit in Sekunden bis zum Schalten des Ausgangs (AEs) | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/alarmierungskette/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert.

---

### Brand- und Wassermeldezentrale

Brandschutz und Wasserschaden-Erfassung mit Rauch-, Wasser- und Temperaturmeldern sowie Brandschutzschalter (AFCI).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Ca | Confirm alarm | Alarm bestätigen | 0/1 |
| Cs | Confirm alarm signals | Deaktiviert die Ausgänge (Pas) und (Mas). Die Ausgänge (Pa) und (Ma) bleiben aktiv. Zugeordnete Audio Player oder Lichtsteuerungen werden ebenfalls abgeschaltet. | 0/1 |
| S | Smoke detector | Alarmeingang für externe Rauchmelder. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| W | Water detector | Alarmeingang für externe Wassermelder. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| F | AFCI | Eingang für Brandschutzschalter. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| T | Temperature input | Anschluss für externe Temperatursensoren. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pa | Pre-alarm | Voralarm | 0/1 |
| Ma | Main alarm | Hauptalarm | 0/1 |
| Pas | Pre-alarm signal | Voralarm Signal | 0/1 |
| Mas | Main alarm signal | Hauptalarm Signal | 0/1 |
| N | Number of active sensors | Anzahl aktive Melder | ∞ |
| At | Alarm test | Alarmtest | 0/1 |
| Ca | Cause of alarm | Meldet die Ursache des letzten Alarms. | - |
| Ta | Time and date of alarm | Meldet Datum und Uhrzeit des letzten Alarms. | - |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|--------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde – Bei Aktivierung/Deaktivierung einer Alarmanlage (max. alle 10s) Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Mad | Main alarm delay | Verzögerung des Hauptalarms nach Aktivieren des Voralarms. | s | 0...∞ | 120 |
| Maxϑ | Maximum temperature | Wenn der Eingang (T) diesen Wert erreicht oder überschreitet, wird der Alarm aktiviert. | ° | ∞ | 43 |
| MaxA | Maximum alarm duration | Der Hauptalarm wird nach Ablauf der eingestellten Zeit automatisch bestätigt. Wenn (Pac) = 1, wird auch der Voralarm automatisch bestätigt. 0 = kein Zeitlimit | s | 0...∞ | 300 |
| Pac | Pre-alarm confirmation | 1 = Voralarm wird automatisch bestätigt, wenn (MaxA) erreicht ist. 0 = Voralarm bleibt aktiv, wenn (MaxA) erreicht ist. | - | 0/1 | 0 |
| Sm | Service mode | Aktiviert den Servicemodus und unterdrückt den Alarm, nur (At) wird im Falle eines Alarms aktiviert. 0 = Servicemodus aus, 1 = Servicemodus dauerhaft eingeschaltet, >1 = Servicemodus für diese Zeit eingeschaltet. | s | 0...∞ | 0 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 2...100 | - |
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge. | - | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/brand-wasser-meldezentrale/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert (technische Informationen sind in Tabellen und Abschnitten enthalten).

---

### AAL Smart Alarm

Intelligente Sturz- und Notfallerfassung mit raumgerichteter Bewegungserkennung (Durchgangsraum, Aufenthaltsraum, Schlafzimmer).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/aal-smart-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| A | Activate alarm | Löst den Alarm aus. Schließen Sie hier einen Notrufknopf oder eine andere Alarmlogik an. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Mvt | Movement transit room | Bewegung Durchgangsraum | 0/1 |
| Mvc | Movement common room | Bewegung Aufenthaltsraum | 0/1 |
| Mvb | Movement bedroom | Bewegung Schlafzimmer | 0/1 |
| Ca | Confirm alarm | Alarm bestätigen | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Dis | Disable | Intelligente Erkennung von Notsituationen ist deaktiviert, wenn 1. Kann verwendet werden, wenn das Haus verlassen wird. Ein manueller Alarm über den Eingang (A) ist weiterhin möglich. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/aal-smart-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| A1-2 | Alarm level 1-2 | Stufe 1 wird sofort bei Alarmauslösung aktiv, Stufe 2 nach der am Parameter D eingestellten Zeit. | 0/1 |
| Ca | Cause of alarm | Alarmursache | – |
| Ta | Time and date of alarm | Alarmzeit und Datum | – |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | – |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/aal-smart-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Tt | Time transit room | Wird innerhalb dieser Zeit nach der letzten Bewegung in einem Durchgangsraum keine weitere Bewegung festgestellt, wird der Alarm ausgelöst. | min | 1...∞ | 15 |
| Tc | Time common room | Wird innerhalb dieser Zeit nach der letzten Bewegung in einem Aufenthaltsraum keine weitere Bewegung festgestellt, wird der Alarm ausgelöst. | min | 1...∞ | 60 |
| Tb | Time bedroom | Wird innerhalb dieser Zeit nach der letzten Bewegung in einem Schlafraum keine weitere Bewegung festgestellt, wird der Alarm ausgelöst. | min | 1...∞ | 420 |
| D | Alarm level 2 delay | Verzögerung Alarmstufe 2 | s | 0...∞ | 60 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/aal-smart-alarm/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 2...100 | 20 |
| Konfiguration | Konfigurieren Sie hier Geräte zur automatischen Verwendung als Melder im Baustein (z.B. Bewegungsmelder Tree). Bewegungsmelder ohne zugeordneten Raum oder mit einem Raum der Typen Sonstige und Zentral werden in der intelligenten Erkennung von Notfallsituationen ignoriert und im Dialog grau markiert. | – | – |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/aal-smart-alarm/

- "WICHTIG: Für eine zuverlässige Erkennung sind zugeordnete Präsenz/Bewegungsmelder in jedem Raum, sowie die Verwendung des Eingangs (Dis) erforderlich."

---

### Notfall Alarm

Notfallknopf mit konfigurierbarer Druckdauer und Quittungsmechanismus (Halten & Loslassen).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/notfall-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle push & hold | Wenn der Eingang länger als der Parameter (Ta) aktiv ist, wird ein Alarm ausgelöst. Wenn der Eingang länger als der Parameter (Tc) aktiv ist, während ein Alarm aktiv ist, wird der Alarm quittiert. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| A | Activate alarm | Löst den Alarm aus. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Ca | Confirm alarm | Alarm bestätigen. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/notfall-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| A | Alarm | | 0/1 |
| Aon | Pulse on alarm start | Impuls bei Alarmstart | 0/1 |
| Aoff | Pulse on alarm end | Impuls bei Alarmende | 0/1 |
| Ca | Cause of alarm | Gibt den Namen bzw. Ort des auslösenden Tasters bzw. den Namen des App-Benutzers aus. | - |
| Cc | Cause of confirmation | Gibt den Namen bzw. Ort des quittierenden Tasters bzw. den Namen des App-Benutzers aus. | - |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/notfall-alarm/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Ta | Push & hold time alarm | Für Eingang (Tg). | s | 1...10 | 4 |
| Tc | Push & hold time confirmation | Für Eingang (Tg). | s | 1...10 | 2 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/notfall-alarm/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 2...100 | 20 |
| Konfiguration | Konfigurieren Sie hier Geräte zur Verwendung als Notfallknopf. Normale Taster (z.B. Touch Tree) lösen einen Alarm aus, wenn sie für die Dauer 'Ta' gedrückt werden. Ein erneuter Impuls für die Dauer 'Tc' quittiert den Alarm wieder. | - | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/notfall-alarm/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert.

---

### SIA DC-09

SIA DC-09 Protokoll-Sender für externe Leitstellen und Notfalldienste (Fernübertragung von Alarmen).

#### Eingänge [OFFEN]
Quelle: https://www.loxone.com/dede/kb/sia-dc-09/

Diese Baustein hat keine Eingänge in der Dokumentation.

#### Ausgänge [OFFEN]
Quelle: https://www.loxone.com/dede/kb/sia-dc-09/

Diese Baustein hat keine Ausgänge in der Dokumentation.

#### Parameter [OFFEN]
Quelle: https://www.loxone.com/dede/kb/sia-dc-09/

Diese Baustein hat keine klassische Parameter-Tabelle.

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sia-dc-09/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|---|---|---|---|
| Server address | IP-Adresse:Port bzw. sia.example.com:Port | - | - |
| Backup server address | IP-Adresse:Port bzw. sia.example.com:Port; wenn angegeben wird dieser Server verwendet wenn der Hauptserver nicht erreichbar ist | - | - |
| Polling [s] | Überprüfung [s] der Serveradresse (0 = keine Überprüfung, max. 86400 Sekunden) | 0...86400 | - |
| Backup polling [s] | Überprüfung [s] der Backup Serveradresse (0 = keine Überprüfung, max. 86400 Sekunden) | 0...86400 | - |
| Server timeout [s] | Timeout [s] für die Antwort vom Server (1 bis 10 Sekunden) | 1...10 | - |
| Protocol | IP Protokoll; zur Zeit wird nur TCP unterstützt | - | - |
| Data format | Protokoll (vom Server erwartet) | - | - |
| Encryption Key | Schlüssel mit 0, 32, 48 bzw. 64 Zeichen (erlaubte Zeichen: 0-9,A-F); wenn kein Schlüssel angegeben ist dann wird unverschlüsselt gesendet | - | - |
| Account Number | Konto am Server (3-16 Zeichen, erlaubte Zeichen: 0-9,A-F) | - | - |
| Account prefix | Prefix zu Konto (1-6 Zeichen, erlaubte Zeichen: 0-9,A-F); Verwenden Sie 0 wenn keine vorgegeben ist | - | - |
| Receiver number | optionale Empfängernummer (0-6 Zeichen, erlaubte Zeichen: 0-9, A-F) | - | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sia-dc-09/

- "Für SIA DC-09 ist der aktuelle Miniserver notwendig, der Miniserver Gen. 1 wird nicht unterstützt!"

---

### Präsenz

Allgemeiner Präsenzbaustein zur Erkennung von Anwesenheit mit konfigurierbarer Nachlaufzeit und Abschaltwarnung.

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/praesenz/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Act | Activate | Aktiviert Präsenz bei steigender Flanke. Bei fallender Flanke startet der Nachlauftimer (Pet). Dauer-Ein und jede fallende Flanke verlängert die Präsenz. Bei Verwendung der Desktop-App zur Präsenzerkennung sendet die App alle (Pet)/2 Sekunden einen (Act) Impuls. | 0/1 |
| Ext | Extend | Solange der Eingang aktiv ist, wird bereits aktive Präsenz verlängert. Bei fallender Flanke startet die Zeit (Pet) zur Verlängerung der Präsenz. | 0/1 |
| AE | Activate / Extend | Jede Änderung am Eingang aktiviert oder verlängert die Präsenz. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/praesenz/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Pc | Presence combined | Kombinierter Präsenzausgang. Kann an allen Präsenz- und Bewegungseingängen anderer Bausteine verwendet werden. | - | ∞ |
| P | Presence | Präsenz | - | 0/1 |
| Pon | Pulse on presence start | Impuls bei Präsenzstart | - | 0/1 |
| Poff | Pulse on presence end | Impuls bei Präsenzende | - | 0/1 |
| Pd | Current presence duration | Dauer der aktuellen Präsenzphase. | s | ∞ |
| Warn | Switch-off warning | Warnungsimpuls vor Präsenz-Ende. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/praesenz/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Pet | Presence extend time | Beginnt mit der fallenden Flanke von Eingang (Act) und Eingang (Ext) und verlängert die Präsenz um die eingestellte Zeit. Erfolgt innerhalb von 30 Sekunden eine Reaktivierung, wird diese Zeit für den aktuellen Präsenzzeitraum verdoppelt. Loxone Präsenzmelder übernehmen diese Verlängerungszeit. Das Gerät und der Baustein verlängern die Präsenz um (Pet) Sekunden, nachdem zuletzt eine Anwesenheit vom Gerät erkannt wurde. | s | 2...∞ | 900 |
| Tw | Switch-off warning time | Zeit der Abschaltwarnung vor dem Ende der Präsenz. Mindestens 2 Sekunden oder 0 zum Deaktivieren. Der Wert muss mindestens 2 Sekunden niedriger als "Pet" sein. | s | 0...∞ | 15 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/praesenz/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge. | - | - |
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 1...50 | 50 |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/praesenz/

- "In einer ruhigen Situation kann es vorkommen, dass trotz Anwesenheit einer Person keine Präsenz mehr erkannt wird."
- "Wenn ein Präsenzmelder im Präsenzbaustein verknüpft wird, übernimmt er automatisch die Einstellung des Parameters Pet (Präsenz-Timeout) vom Block."
- "Der 'P'-Eingang des Präsenzmelders bleibt für die gesamte Dauer von 'Pet' aktiv, selbst wenn der Präsenz-Baustein selbst ausgeschaltet wird."

---

### Berechtigung

Zutrittskontrolle mit externer Authentifizierungs-ID (z.B. Fingerabdruck) via 1-Wire Geräte (Intercom, 1-Wire Extension).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Sel | Select access controller | Impuls um den Baustein bei Berechtigung auszuwählen. (bei Verwendung mehrerer Bausteine) | 0/1 |
| Eid | External Authentication ID | Diese externe Authentifizierungs-ID kann z. B. durch einen Fingerabdruck über einen virtuellen Eingang bereitgestellt werden. Diese ID muss bei der Benutzerauthentifizierung vorhanden sein. | – |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Permission given | Aktiviert den Ausgang für die in Parameter (Pd) eingestellte Dauer bei erteilter Berechtigung. | 0/1 |
| Txt | Providing the last authorisation details | Letzte Berechtigungsdetails. Text ist verfügbar, solange Ausgang (P) Ein ist. | – |
| Pd | Permission denied | Aktiviert den Ausgang für die in Parameter (Pd) eingestellte Dauer bei abgelehnter Berechtigung. | 0/1 |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Dsel | Duration Access Controller selected | Wenn (Dsel) = 0 ist, wird die Authentifizierungsprüfung sofort durchgeführt, (Sel) wird nicht verwendet. | ∞ | 0 |
| Pd | Pulse duration | Impulsdauer der Ausgänge (P), (Pd). | ∞ | 3 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Zugeordnetes Gerät | Folgende Geräte werden unterstützt: Loxone Intercom, 1-Wire Extension, Geräte mit 1-Wire Schnittstelle | – |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert.

---

### Berechtigung NFC Code Touch

NFC/RFID Zutrittskontroller für NFC Code Touch Geräte (Air, Tree, Nano) mit LED-Kontrolle und konfigurierbarem Authentifizierungsmodus (Zwei-Faktor, NFC, Code, OCPP).

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung-nfc-code-touch/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off / Lock | Impuls: Ausgänge werden zurückgesetzt / ausgeschaltet. Ein: Baustein ist gesperrt. Dominierender Eingang. Authentifizierung nicht mehr möglich, Gerät blinkt rot. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | 0/1 |
| Lr | Turns status LEDs red | Status LEDs Rot einschalten | 0/1 |
| Lg | Turns status LEDs green | Status LEDs Grün einschalten | 0/1 |
| Lb | Turns status LEDs blue | Status LEDs Blau einschalten | 0/1 |
| Lw | Turns status LEDs white | Status LEDs Weiß einschalten | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung-nfc-code-touch/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O1-6 | Output 1-6 | Aktiviert Ausgang (Output 1-6) für die Dauer von (Don), bei erfolgreicher Authentifizierung. | 0/1 |
| Cla | Cause of last authorization | Liefert Datum & Uhrzeit, Benutzer und Ausgabe der letzten Berechtigung. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. Datenschutzbestimmungen beachten! | – |
| Ula | User of last authorization | Gibt die NFC-Code-Touch-ID des Benutzers an, falls vorhanden (ansonsten Benutzername), NFC-Tag oder Zugangscode-Name. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. | – |
| Nlo | Name or number of last output | Gibt Bezeichnung bzw. Nummer des letzten Ausgangs an. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. | – |
| Tla | Time and date of last authorization | Gibt Datum und Uhrzeit der letzten Berechtigung an. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. | – |
| Ad | Authentication denied | Aktiviert den Ausgang für die Dauer von (Don), bei abgelehnter Authentifizierung. | 0/1 |
| As | Authentication successful | Aktiviert den Ausgang für die Dauer von (Don), bei erfolgreicher Authentifizierung. | 0/1 |
| Nco | Number of current output | Nummer des aktuellen Ausgangs. -1 = Abgelehnt | -1...∞ |
| Bell | Doorbell output | Klingelausgang | 0/1 |
| Bsel | Doorbell pre-select | Eine Zahl, die vor dem Klingeln eingegeben wurde, wird hier angezeigt. -1 wird ausgegeben, wenn keine Vorwahl getätigt wurde. | -1...9999 |
| Unla | Username of last authorization | Liefert den Benutzernamen des letzten berechtigten Benutzers. Trust Benutzer werden mit dem Hostnamen des Trust-Teilnehmers ergänzt. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. | – |
| Uidla | User-Id of last authorization | Liefert die User-ID des letzten berechtigten Benutzers. Trust Benutzer werden mit dem Hostnamen des Trust-Teilnehmers ergänzt. Der Text ist verfügbar bis die nächste Nachricht ihn ablöst. | – |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | – |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung-nfc-code-touch/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Bbl | Activate bell button light | Lässt die Klingeltaste des Gerätes grün leuchten, wenn 1. Nicht verfügbar bei batteriebetriebenen Geräten. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | – | 0/1 | 0 |
| Bbr | Button brightness | Helligkeit der Tastenbeleuchtung einstellen. Nicht verfügbar bei batteriebetriebenen Geräten. | % | 0...100 | 50 |
| Don | On-duration of outputs (O1-6), (Ad) and (As). | Einschaltdauer der Ausgänge (O1-6), (Ad) und (As). | s | 0...∞ | 3 |
| Blan | Activate button light at night | Schaltet automatisch die Tastenbeleuchtung bei Nacht (Tageslicht 30min) ein, wenn 1. Nur verfügbar bei NFC Code Touch Gen.1 Geräten. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | – | 0/1 | 0 |
| Bl | Activate button light | Schaltet die Tastenbeleuchtung dauerhaft ein, wenn 1. Nicht verfügbar bei batteriebetriebenen Geräten. | – | 0/1 | 0 |
| Au | Authentication | Auswahl der Authentifizierungsmethode. 0 = Zwei-Faktor-Authentifizierung; 1 = Code oder NFC; 2 = NFC; 3 = Code; 4 = OCPP oder NFC. Standard= 1, oder wenn der Wert außerhalb des gültigen Bereichs liegt. Zwei-Faktor-Authentifizierung erfordert sowohl einen Zugangscode als auch einen NFC-Tag innerhalb von 30 Sekunden, in beliebiger Reihenfolge. Tags und Codes von verschiedenen Benutzern können kombiniert werden, solange beide gültig sind. Nicht verfügbar bei batteriebetriebenen NFC Code Touch Air Gen. 1 Geräten. | – | 0...4 | 1 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung-nfc-code-touch/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Zugeordnetes Gerät | Der Benutzer muss sich auf dem ausgewählten Gerät identifizieren. Folgende Geräte können ausgewählt werden: NFC Code Touch Air, NFC Code Touch Tree, NFC Code Touch for Nano | – | – |
| Zugangsberechtigung bearbeiten | Hier klicken, um Zugangsberechtigungen von benutzernunabhängigen NFC-Tags/Zugangscodes zu bearbeiten | – | – |
| Zusätzliche Vorwahlen erlauben | Wenn aktiviert können zusätzlich Vorwahlen von 7 bis 9999 verwendet werden. Aktivierte Vorwahlen größer 6 werden am Bausteinausgang (Nco) ausgegeben. Mit dieser Option muss immer vor jedem Zugangscode eine Vorwahl getätigt werden! | – | – |
| NFC bestätigt Eingabe | Beim Auflegen eines NFC-Tags wird die Vorwahl automatisch bestätigt. Bei Zwei-Faktor-Authentifizierung kann so auch der Code bestätigt werden. | – | – |
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 0...100 | – |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/berechtigung-nfc-code-touch/

- "Statuslicht-Eingänge können nicht mit batteriebetriebenen Geräten verwendet werden!"
- "Bei Batteriebetrieb muss ein NFC Code Touch Air vor dem Einlernvorgang z.b. durch Tastendruck aufgeweckt werden."
- "Verwenden Sie nur verschlüsselte NFC/RFID Tags für den Zutritt zu einem Gebäude oder sensiblen Bereichen. Dies sind Tags mit MIFARE DESFire Chip, wie die Loxone Tags oder Keyfobs."
- "Zusätzlich ist für die Benutzer auch das Recht für den Baustein Berechtigung NFC Code Touch notwendig, damit diese Zutritt erhalten."
- "Für Zutrittscodes gelten dieselben Regeln wie für Kennwörter: Möglichst lang, möglichst schwer zu erraten."
- "Zur Verwendung dieser Eingänge wird der Baustein Berechtigung NFC Code Touch nicht benötigt. Diese Variante wird nicht für die Zutrittssteuerung zu einem Gebäude empfohlen."

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| PUDel | `PUDel` | Ausgang | Pulse by user deletion | Impuls bei Benutzerlöschung | – |

---

### Sprechanlage

Intercom-Integration für Türklingel, Videoübertragung, Text-zu-Sprache (TTS) und maßgeschneiderte Ausgänge.

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sprechanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bell | Activate bell | Aktiviert den Ausgang (Bell) und die zugewiesenen Audio Player. Aktiviert den Ausgang (Mute), wenn der Eingang (Mute) 1 ist. Dieser Eingang ist nicht sichtbar, wenn die Intercom von einem anderen Trust-Mitglied stammt. | 0/1 |
| Mute | Mute bell | Deaktiviert den Ausgang (Bell) und die zugewiesenen Audio Player, wenn 1. | 0/1 |
| TTS | Text to speech | Texteingang zum Abspielen einer Sprachnachricht über die Lautsprecher der Intercom. Dieser Eingang ist nicht sichtbar, wenn die Intercom von einem anderen Trust-Mitglied stammt. | - |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sprechanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bell | Bell | Ausgang zur Ansteuerung einer Türklingel. | 0/1 |
| Mute | Bell muted | Ausgang zur Ansteuerung einer Alternative, wird aktiviert, wenn die Türklingel stummgeschaltet ist und geklingelt wird. | 0/1 |
| O1 | Custom output 1 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| O2 | Custom output 2 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| O3 | Custom output 3 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

#### Parameter [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sprechanlage/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| maxB | Maximum bell duration | Die Ausgänge (Bell) und (Mute) bleiben für die eingestellte Dauer aktiv. Das Klingelsignal wird von den zugewiesenen Audio Playern nur einmal abgespielt, auch wenn Besucher mehrmals klingeln. Das Annehmen oder Ablehnen des Anrufs deaktiviert die Ausgänge (Bell) und (Mute) sofort. Wenn auf 0 gesetzt, bleibt die Türklingel aktiv, bis sie in der Visualisierung beantwortet wird. | s | 0...∞ | 60 |
| Bbr | Button brightness | Stellt die Helligkeit der Tastenbeleuchtung der Intercom ein. Dieser Eingang ist nicht sichtbar, wenn die Intercom von einem anderen Trust-Mitglied stammt. | % | 0...100 | 20 |
| Bbl | Activate bell button light | Aktiviert die Intercom Tastenbeleuchtung, wenn 1. Dieser Eingang ist nicht sichtbar, wenn die Intercom von einem anderen Trust-Mitglied stammt. | - | 0/1 | 0 |
| Qon | ON duration of custom outputs (O1-3) | Ein Dauer der Ausgänge (O1-O3) | s | 0...∞ | 3 |

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sprechanlage/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Audio Player zur Klingel Ausgabe | Verknüpfen Sie die Sprechanlage mit Ihren Audio Playern, um einen Klingelton abzuspielen, wenn die Klingel betätigt wird. | - |
| Mit Nachricht antworten | Ermöglicht das Eingeben von Texten, die nach Aufruf in der Visualisierung als Sprachnachricht an der Intercom abgespielt werden. | - |
| O1: Visualisierung Funktion 1 | Bezeichnung Funktion 1 z.B. Türöffner | - |
| O2: Visualisierung Funktion 2 | Bezeichnung Funktion 2 z.B. Licht aussen | - |
| O3: Visualisierung Funktion 3 | Bezeichnung Funktion 3 z.B. Licht innen | - |
| O1: Visualisierungssymbol 1 | Gibt das Symbol an, das in der Visualisierung (App und Webinterface) angezeigt wird. | - |
| O2: Visualisierungssymbol 2 | Gibt das Symbol an, das in der Visualisierung (App und Webinterface) angezeigt wird. | - |
| O3: Visualisierungssymbol 3 | Gibt das Symbol an, das in der Visualisierung (App und Webinterface) angezeigt wird. | - |
| Video beim Klingeln anzeigen | Standardmäßig zeigt die App ein Standbild an, wenn an der Türklingel geklingelt wird, das den Moment festhält, in dem die Klingeltaste gedrückt wurde. Aktivieren Sie diese Option, um stattdessen den Live-Feed anzuzeigen. Bitte beachten Sie, dass die Intercom nur 3 gleichzeitig aktive Live-Feeds unterstützt. | - |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/sprechanlage/

- "These notifications may be restricted on some iOS devices if the 'Private Relay' service is active. If this is the case, the notification will not display an image."
- "Unter iOS 15 kann es beim Aufbau einer Videoverbindung zum Abbruch der Verbindung mit dem Miniserver kommen."
- "Video and audio connection are not supported in the web interface of the Miniserver Gen. 1. The LOXONE Apps, on the other hand, do fully support the Miniserver Gen. 1."
- "Für die TTS Funktion ist eine Internetverbindung notwendig. Es werden Texte mit jeweils bis zu 300 Zeichen (mit Leerzeichen) unterstützt."

---

### Post- und Paketkasten

Paketsafe Air Integration zur Verfolgung von Paketablage und Posteingang mit Benachrichtigungen.

#### Eingänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/post-und-paketkasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| DisN | Disable Notifications | Benachrichtigungen deaktivieren | 0/1 |
| P | Package received | Paket zugestellt. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| M | Mail received | Post zugestellt. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| Cp | Confirm package | Paket bestätigen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| Cm | Confirm mail | Post bestätigen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |

#### Ausgänge [BELEGT]
Quelle: https://www.loxone.com/dede/kb/post-und-paketkasten/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Package present | EIN, wenn sich ein Paket in der Paketablage befindet. | 0/1 |
| M | Mail present | EIN, wenn sich Post im Briefkasten befindet. | 0/1 |
| Pon | Pulse on package received | Impuls bei Paket zugestellt | 0/1 |
| Poff | Pulse on package confirmed | Impuls bei Paket bestätigt | 0/1 |
| Mon | Pulse on mail received | Impuls bei Post zugestellt | 0/1 |
| Moff | Pulse on mail confirmed | Impuls bei Post bestätigt | 0/1 |
| Txle | Text of last event | Liefert Datum, Uhrzeit und Beschreibung des letzten Ereignisses. | – |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | – |

#### Parameter [OFFEN]
Quelle: https://www.loxone.com/dede/kb/post-und-paketkasten/

Diese Baustein hat keine Einträge in einer Parameter-Tabelle.

#### Eigenschaften [BELEGT]
Quelle: https://www.loxone.com/dede/kb/post-und-paketkasten/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 2...100 | 20 |
| Zugeordnetes Paketsafe Air Gerät | Das Paketsafe Air Gerät, welches mit diesem Baustein verknüpft ist. | – | – |

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/post-und-paketkasten/

Keine expliziten Warnhinweise oder Fallstricke dokumentiert.

---

### Trust

Trust-Infrastruktur für zentrale Benutzerverwaltung und verteilte Systeme (Multi-Miniserver-Netzwerk).

#### Eingänge [OFFEN]
Quelle: https://www.loxone.com/dede/kb/trust/

Diese Baustein/Komponente hat keine klassische Eingänge-Tabelle in der Dokumentation.

#### Ausgänge [OFFEN]
Quelle: https://www.loxone.com/dede/kb/trust/

Diese Baustein/Komponente hat keine klassische Ausgänge-Tabelle in der Dokumentation.

#### Parameter [OFFEN]
Quelle: https://www.loxone.com/dede/kb/trust/

Diese Baustein/Komponente hat keine klassische Parameter-Tabelle in der Dokumentation.

#### Eigenschaften [OFFEN]
Quelle: https://www.loxone.com/dede/kb/trust/

Diese Baustein/Komponente hat keine klassische Eigenschaften-Tabelle in der Dokumentation.

#### Fallstricke [BELEGT]
Quelle: https://www.loxone.com/dede/kb/trust/

- "Für Trusts ist der aktuelle Miniserver notwendig, der Miniserver Gen. 1 wird nicht unterstützt!"
- "Falls der externe Zugang manuell eingerichtet wurde, ist es zwingend erforderlich, einen HTTPS-Port zu verwenden und auch eine Portweiterleitung auf diesen Port einzurichten."
- "Die Zeit, bis ein Trust Teilnehmer aus allen Trusts abgemeldet wird, hängt von dem in den Einstellungen dieses Teilnehmers konfigurierten Verbindungstimeout ab."

---

## Zusammenfassung

| Baustein | Eingänge | Ausgänge | Parameter | Eigenschaften | Status |
|----------|----------|----------|-----------|---------------|--------|
| Alarmanlage | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Alarmanlage Zentral | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | Teilweise |
| Alarmierungskette | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Brand- und Wassermeldezentrale | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| AAL Smart Alarm | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Notfall Alarm | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| SIA DC-09 | [OFFEN] | [OFFEN] | [OFFEN] | [BELEGT] | Teilweise |
| Präsenz | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Berechtigung | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Berechtigung NFC Code Touch | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Sprechanlage | [BELEGT] | [BELEGT] | [BELEGT] | [BELEGT] | Vollständig |
| Post- und Paketkasten | [BELEGT] | [BELEGT] | [OFFEN] | [BELEGT] | Teilweise |
| Trust | [OFFEN] | [OFFEN] | [OFFEN] | [OFFEN] | Keine Tabellen |

## Sonderzeichen-Dokumentation

Folgende Sonderzeichen wurden exakt wie im Original übernommen:
- **ϑ** (griechisches Theta) im Parameter "Maxϑ" (Brand- und Wassermeldezentrale)

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Präsenz Zentral (`CentralPresence`)

Mit diesem Baustein können Präsenzbausteine gemeinsam gesteuert werden. Öffnen Sie mit einem Doppelklick auf den Baustein den Dialog zum Auswählen der verknüpften Bausteine.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Off | `InputReset` | Off / Lock | Impuls (< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| P | `OutputActive` | Presence | Präsenz | – |
| Pon | `OutputPOn` | Pulse on presence start | Impuls bei Präsenzstart | – |
| Poff | `OutputPOff` | Pulse on presence end | Impuls bei Präsenzende | – |
| Pd | `OutputOnTime` | Current presence duration | Dauer der aktuellen Präsenzphase. | ∞ s |
| Absent | `OutputPAbsent` | Pulse on absent | Impuls, wenn "P" länger als die in Parameter "Ta" angegebene Zeit inaktiv ist. | – |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Ta | `ParamTAbsence` | Duration of inactivity before absence | Die Dauer der Inaktivität, nach der das Gebäude als unbesetzt gilt. Sobald diese Zeit ohne neue Aktivität verstrichen ist, gibt der Ausgang "Absent" einen Impuls aus. | ≥ 0 h | – |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 546

---

### Visualisierungs-Präsenz (`Presence`)

Dieser Baustein kann in Verbindung mit der Loxone Desktop-App als Computer-Präsenzmelder verwendet werden.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Tr | `InputTrigger` | Trigger | Trigger | – |
| R | `Reset` | Reset | Reset | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Q | `Q` | – | Digitaler Ausgang | – |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| T | `Time` | Delay duration | Dauer Verzögerung | ≥ 10 s | 900 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 376 · KB: https://www.loxone.com/help/Presence

---

### Präsenzmelder (veraltet) (`PresenceController`)

Präsenzmelder (veraltet)

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Mo | `Mv` | Presence or motion sensor input | Digitaler Eingang für externe Präsenz- oder Bewegungsmelder | – |
| Idw | `W` | Door and window contact | Digitaler Eingang für Tür- und Fensterkontakte | – |
| Ic | `C` | User defined | Digitaler Eingang Benutzerspezifisch | – |
| Lon | `Li` | Lights on | Analoger Eingang aktuelle Lichtszene | ∞ |
| Mu | `Mu` | Music | Digitaler Eingang Impuls Musik | – |
| P | `P` | Power | Analoger Eingang für aktuelle Leistung [kW] | ∞ |
| CO2 | `CO2` | CO2 | Analoger Eingang für aktuellen CO2 Wert [ppm] | ∞ |
| T5 | `Gesture` | Pulse combined button input | Impuls Kombinierter Tasteneingang | ∞ |
| R | `Reset` | Reset | Reset | – |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Q | `PA` | – | Digitaler Ausgang Präsenz erkannt | – |
| AQ | `AQ` | – | Anzahl aktiver Eingänge | ∞ |
| TQ | `TQ` | – | Textausgang letzter Melder | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| T | `TVi` | Duration by which presence is extended when enabled through UI | Dauer [s] Verlängerung nach fallender Flanke bei Aktivierung über die Visualisierung | ∞ | 60 |
| TMv | `TMv` | Duration by which pulses from motion sensors are extended in seconds | Dauer [s] Verlängerung nach fallender Flanke des Eingangs Präsenz | ∞ | 60 |
| TW | `TW` | Input pulse extension door/window contact | Dauer [s] Verlängerung nach fallender oder steigender Flanke des Eingangs Tür- oder Fensterkontakte | ∞ | 60 |
| TC | `TC` | Duration by which pulses on the user defined input are extended in seconds | Dauer [s] Verlängerung nach fallender Flanke des Eingangs für den benutzerdefinierten Eingang | ∞ | 60 |
| TL | `TL` | Duration by which signal on the lighting input is extended in seconds | Dauer [s] Verlängerung nach erster steigender Flanke des Eingangs für Licht | ∞ | 60 |
| TM | `TM` | Duration by which signal on the music input is extended in seconds | Dauer [s] Verlängerung nach erster steigender Flanke des Eingangs für Musik | ∞ | 60 |
| TP | `TP` | Duration by which signal on the power input is extended in seconds | Dauer [s] Verlängerung des analogen Eingangs Leistung, falls dieser unter den Schwellwert fällt | ∞ | 60 |
| TCO | `TCO` | Parameter - Duration by which signal on the CO2 input is extended in seconds | Dauer [s] Verlängerung des analogen Eingangs CO2, falls dieser unter den Schwellwert fällt | ∞ | 60 |
| TT | `TT` | Extension duration of the T5 input | Verlängerung des Eingangsimpulses nach erster steigender Flanke für T5 | ∞ | 60 |
| Sp | `dP` | Power Threshold | Schwelle Leistung [kW], ab welcher der Eingang P berücksichtigt wird | ∞ | 0,1 |
| Dc | `dC` | CO2 threshold | Schwelle CO2 [ppm], ab welcher der Eingang CO2 berücksichtigt wird | ∞ | 500 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 477

---
