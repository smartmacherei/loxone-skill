# Tore, Türen & Sonderanwendungen

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.

Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## Türsteuerung

Steuert Türklingel und Türöffner mit bis zu 3 benutzerdefinierten Ausgängen. Ermöglicht die Integration von Intercoms und Audioplayern für Klingel- und Sprechfunktionen.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bell | Activate bell | Aktiviert den Ausgang (Klingel) und die zugewiesenen Audioplayer. Wenn eine Loxone Intercom verwendet wird, ist es nicht notwendig, diesen Eingang anzuschließen. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/tuersteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bell | Bell | Ausgang zur Ansteuerung einer Türklingel. | 0/1 |
| O1 | Custom output 1 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| O2 | Custom output 2 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| O3 | Custom output 3 | Ausgang wird in den Einstellungen benannt und über die Visualisierung angesteuert. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

Quelle: https://www.loxone.com/dede/kb/tuersteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| maxB | Maximum bell duration | Der Ausgang (Bell) bleibt für die eingestellte Dauer aktiv. Das Annehmen oder Ablehnen des Anrufs deaktiviert den Ausgang (Bell) sofort. Wenn auf 0 gesetzt, bleibt die Türklingel aktiv, bis sie in der Visualisierung beantwortet wird. | s | 0...∞ | 60 |

Quelle: https://www.loxone.com/dede/kb/tuersteuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Zugeordnete Intercom | Hier kann die Türsteuerung einer Intercom zugeordnet werden. (Intercom wird als Peripherieobjekt eingefügt) | - |
| O1: Visualisierung Funktion 1 | Bezeichnung Funktion 1 z.B. Türöffner | - |
| O2: Visualisierung Funktion 2 | Bezeichnung Funktion 2 z.B. Licht aussen | - |
| O3: Visualisierung Funktion 3 | Bezeichnung Funktion 3 z.B. Licht innen | - |
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge. | - |
| Beim Klingeln Videostream anzeigen | Zeigt in der Visualisierung den Videostream anstelle eines Standbildes, wenn jemand klingelt. Deaktivieren Sie diese Option, wenn die Sprechanlage kein Videostreaming an mehrere Visualisierungen gleichzeitig zulässt. | - |

Quelle: https://www.loxone.com/dede/kb/tuersteuerung/

### Fallstricke

[BELEGT] Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen in der Dokumentation vorhanden.

---

## Praxis: IP-Kamera als „benutzerdefinierte Intercom" einbinden

Loxone hat **keinen eigenen Kamera-Gerätetyp**. Eine IP-Kamera wird als *benutzerdefinierte
Intercom* (`<C Type="IntercomDevice">`, Peripherie → Intercom) angelegt; die Türsteuerung ist
optional und dient nur der Darstellung auf einer Programmierseite.

### 🛑 Die Zugangsdaten gehören in die URL — nicht in die Felder daneben

**[VERIFIZIERT 07.08.2026]** Am Intercom-Objekt gibt es beides:

| GUI-Feld | XML-Attribut | wofür |
|---|---|---|
| URL Videostream (intern) | `IntVideoUrl` | Bildquelle im Heimnetz |
| URL Videostream (extern) | `ExtVideoUrl` | Bildquelle von außen |
| Benutzername Kamera | `VideoUser` | generische Kamera-Anmeldung (Basic-Auth-Pfad) |
| Kennwort Kamera | `VideoPwd` | dito |

**Loxone setzt `VideoUser`/`VideoPwd` *nicht* in die URL ein.** Beide Wege existieren
nebeneinander, und welcher funktioniert, entscheidet die **Kamera**:

- Kameras mit HTTP-Basic-Auth auf dem Bild-Pfad → die beiden Felder genügen.
- **Kameras, die die Anmeldung als Query-Parameter erwarten — darunter Reolink — brauchen sie
  in der URL.** `[BELEGT]` Reolink-Support und der Loxone-Library-Eintrag *Reolink IP CAM* nennen
  beide dieselbe Form:
  ```
  http://<IP>/cgi-bin/api.cgi?cmd=Snap&channel=0&user=<Benutzer>&password=<Kennwort>
  ```
  optional `&rs=<Zufallsstring>` gegen Caching und `&width=640&height=480` für den Substream.
  `[BELEGT]` Voraussetzung: **HTTP- oder HTTPS-Port an der Kamera freigeschaltet** — bei
  aktueller Reolink-Firmware ab Werk **aus** (nur der proprietäre Port 9000 ist offen).

`[COMMUNITY]` Im LoxWiki (Adatis-Intercom) steht, die beiden Felder seien „von Loxone
erforderlich, werden aber nicht von der Intercom benötigt" — sie also auszufüllen schadet
nicht, auch wenn die Kamera sie ignoriert.

### `VideoPwd` steht verschlüsselt in der Projektdatei

**[VERIFIZIERT 07.08.2026]** Config schreibt in `VideoPwd` **32 Hex-Zeichen**, nicht das Klartext-
Passwort — und bei gleichem Passwort an vier Kameras **vier verschiedene** Werte (Schlüssel hängt
also am Objekt). Folgen:

- Das Feld lässt sich **nicht per Skript befüllen** — es muss in Config eingetippt werden.
- **Was in der URL steht, ist dagegen Klartext.** Wer die Anmeldung als Query-Parameter braucht,
  hat das Kamerapasswort im Klartext in der Config und in jedem HTTP-Abruf im Netz.
  → Dann für die **Bildabfrage** ein Konto mit möglichst wenig Rechten anlegen. Reolink kennt nur
  *Administrator* und *Benutzer*; **Live-Bild kann auch der Benutzer**, PTZ nur der Administrator.
  Also: Snapshot-URL mit dem Benutzer-Konto, nur die PTZ-Befehle mit Administrator.

### PTZ / Patrouille über virtuelle Ausgänge (Reolink)

Zwei verschiedene Dinge heißen „Patrouille":

| | Wirkung | Befehl |
|---|---|---|
| Patrouille abschalten | dauerhaft, überlebt den Kamera-Neustart | `SetPtzPatrol`, `enable: 0` |
| laufende Fahrt stoppen | hält die Bewegung *jetzt* an | `PtzCtrl`, `op: "StopPatrol"` |

Für „nachts ist Ruhe" braucht es **beide** — sonst dreht die Kamera nach dem Abschalten noch die
angefangene Runde zu Ende. Umsetzung: ein `VirtualOut` (Adresse `http://<IP>`) mit **zwei**
`VirtualOutCmd`, Attribute siehe [xml-bearbeitung.md](xml-bearbeitung.md).

### ⚠️ Türsteuerung als Kamera-Kachel: zwei Fallen

1. **Beim Ziehen eines Peripherie-Ausgangs auf eine Seite übernimmt die neue Ausgangsreferenz den
   Eingang — eine dort bereits bestehende Verbindung wird ersetzt, nicht ergänzt.** Verifiziert
   07.08.2026: `Mode "Schlafen".Q → VirtualOutCmd.I` war weg, nachdem der Befehl als
   Ausgangsreferenz auf die Seite gezogen wurde. Danach immer die Konnektorenpaare gegenprüfen.
2. **`Inv` bleibt am Konnektor stehen, auch wenn die Quelle wechselt** (Falle 8). Eine Inversion,
   die für ein Betriebsart-Signal gedacht war, dreht danach den Taster aus der Visualisierung um.
3. Die Ausgänge `O1`–`O3` der Türsteuerung werden „über die Visualisierung angesteuert"
   `[BELEGT]`; ob sie halten oder nur pulsen, sagt die KB **nicht** `[OFFEN]`. Beim
   Schwesterbaustein *Sprechanlage* gibt es dafür den Parameter `Qon` („Ein Dauer der Ausgänge
   O1-O3", Default **3 s**) — dort sind es also Impulse. Für einen Dauerzustand (Patrouille
   ein/aus) deshalb einen **Schalter** dazwischensetzen, nicht direkt verdrahten.

---

## Tor

Steuert Garagentore, Schwenktore und Sektionaltore mit Endschaltern, Präsenzsensoren und Warnleuchte. Unterstützt Teillöffnung und verhindert Öffnung/Schließung über externe Sensoren.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | 0/1 |
| Co | Complete open | Falls in Bewegung, wird gestoppt. | 0/1 |
| Cc | Complete close | Falls in Bewegung, wird gestoppt. | 0/1 |
| T5 | T5 control | Taste 1: Complete open Taste 4: Complete close | ∞ |
| Io | Is open | Eingang wird verwendet, um die "vollständig geöffnet" Position über einen Endschalter oder ähnliches zu melden. | 0/1 |
| Ic | Is closed | Eingang wird verwendet, um die "vollständig geschlossen" Position über einen Endschalter oder ähnliches zu melden. | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Spo | Sensor prevent opening | Wenn aktiv, wird das Öffnen verhindert, aber das Schließen ist weiterhin möglich. Dient zum Anschluss einer Lichtschranke oder ähnlichem. | 0/1 |
| Spc | Sensor prevent closing | Wenn aktiv, wird das Schließen verhindert, aber das Öffnen ist weiterhin möglich. Dient zum Anschluss einer Lichtschranke oder ähnlichem. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Co, Cc, T5 wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |
| Po | Partially Open | Fährt das Tor in die teilgeöffnete Position, wenn die aktuelle Position eine andere ist. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/tor/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Pulse to Open/Stop/Close | Impuls für öffnen/stop/schließen Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| Op | Open | Öffnen | 0/1 |
| Cl | Close | Schließen | 0/1 |
| Im | In motion | In Bewegung | 0/1 |
| Pos | Position | 0.0 = geschlossen, 1.0 = offen | 0...1 |
| Wl | Warning light | Aktiviert eine blinkende Warnleuchte, wenn sich das Tor bewegt. Die Ein/Aus Zeit wird über die Parameter (Wlon) and (Wloff) definiert. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

Quelle: https://www.loxone.com/dede/kb/tor/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Opd | Opening Duration | Dauer Öffnen | s | 0...∞ | 60 |
| Cld | Closing Duration | Dauer Schließen | s | 0...∞ | 60 |
| Pd | Pulse duration | Impulsdauer der Ausgänge Tg, Op, Cl. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | 0...∞ | 0,5 |
| Ppd | Pulse pause duration | Pausendauer zwischen zwei aufeinander folgenden Impulsen der Ausgänge Tg, Op, Cl. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | 0...∞ | 0,5 |
| Mld | Motor lock duration | Dauer der Motorverrieglung bei Richtungswechsel. | s | 0...∞ | 0,5 |
| Wlon | Warning light on duration | Warnlicht Ein Dauer | s | 0...∞ | 1 |
| Wloff | Warning light off duration | Warnlicht Aus Dauer | s | 0...∞ | 1 |
| Type | Type | Animationstyp 0=Garagentor 1=Schwenktor mit einem Flügel links 2=Schwenktor mit einem Flügel rechts 3=Schwenktor mit zwei Flügel 4=Seitensektionaltor links 5=Seitensektionaltor rechts | - | 0...5 | 0 |
| PoPos | Partially Open Position | Zielposition für Eingang Po. 0,2 = 20 % offen | - | 0...1 | 0,2 |

Quelle: https://www.loxone.com/dede/kb/tor/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anschlussart Antrieb | Legt das Verhalten der Ausgänge (Tg), (Op), (Cl) fest Direkt = digitale Ausgänge nachf. Steuerung = impulsgesteuerte Ausgänge | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

Quelle: https://www.loxone.com/dede/kb/tor/

### Fallstricke

[BELEGT] Im bereitgestellten Dokumentationstext sind keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen enthalten.

---

## Tor Zentral

Zentralisiert die Steuerung mehrerer Tor-Bausteine. Ermöglicht gleichzeitige Kontrolle aller verbundenen Tore und meldet aktuelle Zustände (offen/geschlossen/Anzahl).

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | 0/1 |
| Co | Complete open | Stoppen nicht möglich. | 0/1 |
| Cc | Complete close | Stoppen nicht möglich. | 0/1 |
| T5 | T5 control | Taste 1: Complete open Taste 4: Complete close | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Co, Cc, T5 wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | 0/1 |
| Po | Partially Open | Fährt das Tor in die teilgeöffnete Position, wenn die aktuelle Position eine andere ist. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/tor-zentral/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |
| No | Open gates | Anzahl der offenen Tore | ∞ |
| Nc | Closed gates | Anzahl der geschlossenen Tore | ∞ |

Quelle: https://www.loxone.com/dede/kb/tor-zentral/

### Parameter

[BELEGT] Im Dokument sind keine separaten Tabellen für Parameter vorhanden.

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Alle ausgewählten Tor-Bausteine können gemeinsam gesteuert werden. | Alle ausgewählten Tor-Bausteine können gemeinsam gesteuert werden. | - |

Quelle: https://www.loxone.com/dede/kb/tor-zentral/

### Fallstricke

[BELEGT] Warnung-, Achtung- oder Hinweis-Boxen sind nicht enthalten.

---

## Bewässerung

Steuert automatische Bewässerungsanlagen mit bis zu 8 Ventilen und Pumpe. Berücksichtigt Niederschlagsvorhersage und Regensensoren zur intelligenten Wassernutzung.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Act | Activation | Aktiviert die Bewässerung. Gestartet wird diese nur, wenn es nicht ausreichend lange geregnet hat, und keine ausreichende Regenmenge zu erwarten ist. | - | 0/1 |
| Sel | Select valve | Aktiviert das Ventil (V1-8). 0 - deaktiviert alle Ventile 9 - aktiviert alle Ventile | - | 0...9 |
| Raf | Rain forecast | Eingang für die zu erwartende Niederschlagsmenge in den nächsten Stunden | l/m² | 0...∞ |
| Ra | Rain | Eingang für einen Regensensor oder eine vergleichbare Information. Wird verwendet um die Regendauer zu ermitteln. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/bewaesserung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pump | Ausgang zur Ansteuerung einer Pumpe | 0/1 |
| V1-8 | Valve 1-8 | Ausgang zur Ansteuerung eines Ventils | 0/1 |
| Av | Active valve | Aktuell aktives Ventil 0 - Alle Aus 9 - Alle Ein | 0...9 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

Quelle: https://www.loxone.com/dede/kb/bewaesserung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| MaxR | Maximum precipitation in the next set hours | Ist die Niederschlags Vorhersage (Raf) größer als dieser Wert, wird die Bewässerung über den Eingang (Act) nicht mehr aktiviert. | l/m² | 0...∞ | 2 |
| MaxRa | Maximum rain duration in the last 24 hours | Hat es in Summe in den letzten 24 Stunden länger als diese Zeit geregnet, wird die Bewässerung über den Eingang (Act) nicht mehr aktiviert. | s | 0...∞ | 1800 |
| Tv1-8 | Valve Time 1-8 | Dauer wie lange das Ventil aktiv ist, bis das nächste aktiviert wird. | s | 0...∞ | 600 |

Quelle: https://www.loxone.com/dede/kb/bewaesserung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|
| Konfiguration | Konfiguration der Bewässerungs Zonen | - | - |
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen | 1...50 | 50 |

Quelle: https://www.loxone.com/dede/kb/bewaesserung/

### Fallstricke

[BELEGT] Keine derartigen Boxen wurden im bereitgestellten Text gefunden.

---

## Poolsteuerung

Vollständige Poolverwaltung mit Temperaturregelung, Filterzyklus, Gegenstromanlage und Zentralabdeckung. Unterstützt Heiz- und Kühlmodi mit Eco-Funktion und Servicemodus für manuelle Ventilkontrolle.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Om | Set operating mode | 1 = Automatisch, 2 = Service | - | 0...2 |
| ϑm | Set temperature mode | 0 = Aus, 1 = Automatik: Heizen/Kühlen mit Sollwert-Regulierung (Eco berücksichtigt), 2 = Automatik Heizen, 3 = Automatik Kühlen, 4 = Manuell Heizen, 5 = Manuell Kühlen | - | 0...5 |
| Eco | Eco | Ausgang (H) und Ausgang (C) ausgeschaltet, wenn 1 | - | 0/1 |
| ϑt | Target temperature | Zieltemperatur | ° | ∞ |
| ϑc | Current temperature | Aktuelle Temperatur | ° | ∞ |
| Wlvl | Water level | Wasserstand | cm | 0...∞ |
| Cpos | Cover position | Position der Abdeckung (0.0 = offen, 1.0 = geschlossen) | - | 0...1 |
| Sm | Swimming machine | Digitaler oder analoger Eingang je nach Ausgang (Wm) | - | ∞ |
| I1 | Custom input 1 | Wert wird in der Visualisierung angezeigt | - | ∞ |
| I2 | Custom input 2 | Wert wird in der Visualisierung angezeigt | - | ∞ |
| Fi | Activate Filter cycle | Filterzyklus aktivieren (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Bw | Activate Backwash & rinse cycle | Rückspül & Klarspülzyklus aktivieren (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Ci | Activate Circulation cycle | Zirkulier Zyklus aktivieren (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Dr | Activate Drain cycle | Entleer Zyklus aktivieren (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Vp | Set valve position | Auswahl Ventilposition, nur im Servicemodus: 0=Filtern, 1=Rückspülen, 2=Klarspülen, 3=Zirkulieren, 4=Geschlossen, 5=Entleeren (nur bei bestimmten Konfigurationen sichtbar) | - | ∞ |
| Fp | Filtration pump | Manuelle Steuerung Filterpumpe, nur Servicemodus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Dv | Drain valve | Manuelle Steuerung Abflussventil, nur Servicemodus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Error | Error Input | Als Fehlereingang verwendbar; Impuls sperrt Ventil bis Reset über (Off) oder Quittierung via Visualisierung | - | 0/1 |
| Off | Off / Lock | Puls <200ms: Reset auf Initialzustand; Puls >200ms: Sperrt Funktionsbaustein; Puls >500ms: Sensorname in UI | - | 0/1 |
| DisPc | Disable periphery control | Deaktiviert Eingänge (Om), (ϑm), (ϑt), (Fi), (Bw), (Ci), (Dr), (Vp), (Fp), (Dv) wenn Ein; Bedienung via Visualisierung möglich | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/poolsteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| H | Heating demand | Aktiviert nur wenn Filterpumpe aktiv und angeschlossen; bei "Automatik" Heizbedarf startet Zirkulieren-Zyklus wenn kein Zyklus aktiv | - | 0/1 |
| C | Cooling demand | Aktiviert nur wenn Filterpumpe aktiv und angeschlossen; bei "Automatik" Kühlbedarf startet Zirkulieren-Zyklus wenn kein Zyklus aktiv | - | 0/1 |
| Om | Current operating mode | 0 = Außer Betrieb, 1 = Automatik, 2 = Service | - | 0...2 |
| ϑm | Current temperature control mode | 0 = Aus, 1 = Automatik Heizen/Kühlen (Eco berücksichtigt), 2 = Automatik Heizen, 3 = Automatik Kühlen, 4 = Manuell Heizen, 5 = Manuell Kühlen | - | 0...5 |
| Cϑm | Cycle started via (ϑm) | Ein, wenn aktiver Zyklus von Temperatur Regelung gestartet wurde | - | 0/1 |
| ϑt | Current target temperature | Aktuelle Zieltemperatur | ° | ∞ |
| Wlvl | Current water level | Aktueller Füllstand | cm | ∞ |
| Op | Open pool cover | Sendet Impuls wenn Taste in Visualisierung gedrückt wird | - | 0/1 |
| Cl | Close pool cover | Sendet Impuls wenn Taste in Visualisierung gedrückt wird | - | 0/1 |
| Wm | Water machine | Ausgang für Gegenstromanlage (analog/digital abhängig von Beschaltung) | - | ∞ |
| Fi | Filtration cycle state | Status Filterzyklus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Bw | Backwash cycle state | Status Rückspülzyklus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Ci | Circulation cycle state | Status Zirkulierzyklus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Dr | Draining cycle state | Status Entleerzyklus (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Rtc | Remaining duration of the active cycle | Restzeit des aktiven Zyklus (nur bei bestimmten Konfigurationen sichtbar) | s | ∞ |
| Fpet | Filtration pump extend time | Anzeige ob Filterpumpe aufgrund Parameter (Fpet) noch läuft (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Vpos | Current valve position | -1 = in Bewegung/unbekannt, 0 = Filtern, 1 = Rückspülen, 2 = Klarspülen, 3 = Zirkulieren, 4 = Geschlossen, 5 = Entleeren, 6 = Entlasten (nur bei bestimmten Konfigurationen sichtbar) | - | ∞ |
| Fp | Filtration pump | Ausgang zur Ansteuerung Filterpumpe (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Dv | Drain valve | Ausgang zur Ansteuerung Abflussventil (nur bei bestimmten Konfigurationen sichtbar) | - | 0/1 |
| Error | Error code | Aktiviert durch Eingang (Error); aktiv bis Reset via (Off) oder Quittierung via Visualisierung | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder; verknüpft Funktionen zwischen Geräten/Bausteinen | - | - |

Quelle: https://www.loxone.com/dede/kb/poolsteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| ϑh | Hysteresis temperature | Im "Automatik" Modus wird zu Mitternacht entschieden, ob geheizt/gekühlt wird; <Solltemp-Hysterese=heizen, >Solltemp+Hysterese=kühlen | - | ∞ | 0,5 |
| Fpet | Filtration pump extend time | Nachlaufzeit Filterpumpe nach Zyklus mit freigegebener Heizung/Kühlung; hält Wasser in Bewegung gegen Wärmestau (nur bei bestimmten Konfigurationen sichtbar) | s | 0...1800 | 0 |
| Fid | Filtration cycle duration | Dauer Filterzyklus (nur bei bestimmten Konfigurationen sichtbar) | s | 0...∞ | 18000 |
| Bwd | Backwash cycle duration | Dauer Rückspülzyklus (nur bei bestimmten Konfigurationen sichtbar) | s | 20...600 | 120 |
| Rid | Rinsing cycle duration | Dauer Klarspülzyklus (nur bei bestimmten Konfigurationen sichtbar) | s | 20...300 | 30 |
| Cid | Circulation cycle duration | Dauer Zirkulierzyklus (nur bei bestimmten Konfigurationen sichtbar) | s | 0...∞ | 43200 |
| Drd | Draining cycle duration | Dauer Entleerzyklus (nur bei bestimmten Konfigurationen sichtbar) | s | 0...∞ | 3600 |

Quelle: https://www.loxone.com/dede/kb/poolsteuerung/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Aquastar Air | Referenz zum Aquastar Air des Pools; zuordenbare Geräte: Aquastar Air | - |

Quelle: https://www.loxone.com/dede/kb/poolsteuerung/

### Fallstricke

[BELEGT]

**Automatik-Betrieb:** "Verwendet die in der Schaltuhr eingestellten Zyklen. Wenn ein manueller Zyklus gestartet wird, hat dieser Vorrang. Manuelle Änderungen der Ventilposition, Pumpe und Abflussventils werden ignoriert."

**Servicemodus-Warnung:** "In diesem Modus sind gegenseitige Verriegelungen und Sicherheitsfeatures deaktiviert. Es sollte vermieden werden, dass die Pumpe aktiv ist, während das Ventil in Bewegung ist."

---

## Saunasteuerung

Regelt Saunaheizung mit bis zu 3 Phasen, Lüfter, Sanduhr und Sicherheitsabschaltung. Unterscheidet Heiz-, Trocknung- und Lüftungsphase mit Temperatursensor und optionalem Banksensor.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Tg | Toggle | Schaltet zwischen Sauna Ein, Heizen, Trocknen, Lüften und Sauna Aus um. | - | 0/1 |
| ϑt | Target temperature | Min: 30°C Max: 120°C | ° | ∞ |
| ϑc | Current temperature | Aktuelle Temperatur | ° | ∞ |
| Fan | Toggle fan | Schaltet den Lüfter ein/aus. Der Lüfter kann nur eingeschaltet werden, wenn die Sauna eingeschaltet ist. | - | 0/1 |
| St | Activate sand timer | Aktiviert die Sanduhr für die im Parameter (Std) eingestellte Dauer. Jeder weitere Impuls am Eingang startet den Timer neu. | - | 0/1 |
| Dc | Door contact | Der Türzustand wird nur zur Anzeige in der Visualisierung verwendet! 0 = geöffnet, 1 = geschlossen. | - | 0/1 |
| ϑb | Current temperature bench | Falls angeschlossen, wird die Banktemperatur als aktuelle Temperatur verwendet. | ° | ∞ |
| P | Presence | Wird für die Sicherheitsabschaltung verwendet. Wenn keine Präsenz festgestellt wird, schaltet sich die Sauna automatisch nach der im Parameter (Ssdt) eingestellten Dauer ab. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tg), (Fan), (St) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| On | On | Sauna aktivieren | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| So | Sauna output (0-10V) | Analoger Ausgang 0-10V für die Saunasteuerung. | V | 0...10 |
| L1-3 | Sauna phase output (1-3) | Phasenausgang (L1-3) für die Saunasteuerung. | - | 0/1 |
| On | Sauna state | An, solange Sauna und Trocknungsphase aktiv sind. | - | 0/1 |
| Fan | Fan | Ausgang zur Ansteuerung des Lüfters. | - | 0/1 |
| Stt | Sand timer remaining time | Sanduhr Restzeit | s | 0...∞ |
| Dry | Drying state | Ein, solange das Trocknen und Lüften aktiv ist. | - | 0/1 |
| Ssd | Safety shutdown | Impuls, wenn die aktuelle Temperatur den im Parameter (Ssdϑ) eingestellten Wert überschreitet. | - | 0/1 |
| ϑt | Target temperature | Gibt die Zieltemperatur aus. | ° | 30...120 |
| Stoff | Sand timer end | Impuls, wenn die Sanduhr abgelaufen ist. | - | 0/1 |
| St | Sand timer state | Ein wenn die Sanduhr aktiv ist. | - | 0/1 |
| Ready | Sauna ready | Impuls, wenn die Zieltemperatur erreicht ist. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| ϑd | Temperature deviation | Abweichung der aktuellen Temperatur (ϑc) von der Sitztemperatur (wenn die aktuelle Banktemperatur (ϑb) nicht verwendet wird). | ° | ∞ | 0 |
| Dryϑ | Drying phase target temperature | Die Temperatur, die erforderlich ist, um den Lüfter in der Trocknungsphase zu starten. | ° | ∞ | 70 |
| Dryd | Drying phase duration | Lüftungsdauer nach Erreichen der Temperatur der Trocknungsphase (Dryϑ). | s | 0...∞ | 1800 |
| Std | Sand timer duration | Sanduhr Dauer | s | 0...∞ | 900 |
| Ssdϑ | Safety shutdown temperature | Bei Überschreitung werden alle Ausgänge ausgeschaltet, mit Ausnahme des Ausgangs (Ssd). | ° | ∞ | 139 |
| Ssdt | Safety shutdown time | Die Sauna wird zur eingestellten Zeit automatisch ausgeschaltet. Wenn der Eingang (P) verwendet wird, beginnt die Zeit zu laufen, wenn keine Anwesenheit mehr festgestellt wird. | s | 0...∞ | 7200 |
| PWMp | PWM period | Legt die PWM-Periode für die Phasenausgänge (L1-3) fest. | s | 0...∞ | 180 |
| G | Gain | Verstärkung für den Regler des PWM modulierten Ausgangs. Bei Verringerung des Werts reagiert die Temperaturregelung langsamer, bei Erhöhung schneller. Falls notwendig, ändern Sie den Wert in kleinen Schritten, um die Regelung an die Sauna anzupassen. | - | 0...∞ | 1 |
| Pm | Phase mode | Anzahl der verwendeten Phasen: Aus = 3 Phasen Ein = 1 Phase Parameter wird nur angezeigt, wenn die Phasenausgänge (L2) und (L3) verwendet werden. | - | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung/

### Eigenschaften

[OFFEN] Keine spezialisierten Eigenschaften in der Dokumentation dokumentiert.

### Fallstricke

[BELEGT]

**Sicherheit:** "Aus Sicherheitsgründen besitzt der Baustein keine Remanenz. Daher ist dieser nach einem Miniserver Neustart stets ausgeschaltet."

**Anwendungshinweis:** "Beachten sie dabei die Sicherheitsvorschriften und Gesetzesbestimmungen des jeweiligen Landes."

---

## Saunasteuerung mit Verdampfer

Erweiterte Saunasteuerung mit automatischen Modi (Finnisch, Kräuter, Dampfbad, Warmluft) und Feuchtereglung über Verdampfer. Kombiniert Temperatur- und Feuchtemanagement für verschiedene Sauntypen.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Mode | Select sauna mode | 0 = Aus / Manuell, 1 = Finnisch manuell, 2 = Feuchte manuell, 3 = Finnische Sauna, 4 = Kräutersauna, 5 = Softdampfbad, 6 = Warmluftbad | - | 0...6 |
| Fim | Finnish manual | Wechselt in diesen Modus. (Temperatur: manuell, Feuchte: Aus) | - | 0/1 |
| Hum | Humidity manual | Wechselt in diesen Modus. (Temperatur: manuell, Feuchte: manuell) | - | 0/1 |
| Fin | Finnish sauna | Wechselt in diesen Modus. (Temperatur: 80°C, Feuchte: Aus) | - | 0/1 |
| Her | Herbal sauna | Wechselt in diesen Modus. (Temperatur: 45°C, Feuchte: 50%) | - | 0/1 |
| Sof | Soft Steam bath | Wechselt in diesen Modus. (Temperatur: 50°C, Feuchte: 50%) | - | 0/1 |
| Hot | Hot-air bath | Wechselt in diesen Modus. (Temperatur: 45°C, Feuchte: 45%) | - | 0/1 |
| Tg | Toggle | Schaltet zwischen Sauna Ein, Heizen, Trocknen, Lüften und Sauna Aus um. | - | 0/1 |
| ϑt | Target temperature | Min: 30°C, Max: 110°C (Finnisch manuell), Max: 70°C (Feuchte manuell) | ° | ∞ |
| ϑc | Current temperature | Aktuelle Temperatur | ° | ∞ |
| Ht | Target humidity | Zielfeuchte | % | 15...65 |
| Hc | Current humidity | Aktuelle Feuchte | % | 0...100 |
| Fan | Toggle fan | Schaltet den Lüfter ein/aus. Der Lüfter kann nur eingeschaltet werden, wenn die Sauna eingeschaltet ist. | - | 0/1 |
| St | Activate sand timer | Aktiviert die Sanduhr für die im Parameter (Std) eingestellte Dauer. Jeder weitere Impuls am Eingang startet den Timer neu. | - | 0/1 |
| Dc | Door contact | Der Türzustand wird nur zur Anzeige in der Visualisierung verwendet! 0 = geöffnet, 1 = geschlossen. | - | 0/1 |
| ϑb | Current temperature bench | Falls angeschlossen, wird die Banktemperatur als aktuelle Temperatur verwendet. | ° | ∞ |
| P | Presence | Wird für die Sicherheitsabschaltung verwendet. Wenn keine Präsenz festgestellt wird, schaltet sich die Sauna automatisch nach der im Parameter (Ssdt) eingestellten Dauer ab. | - | 0/1 |
| Ws | Water shortage | Bei niedrigem Wasservorrat wird der Verdampfer abgeschaltet. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Tg), (Fan), (St) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| On | On | Sauna aktivieren | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung-mit-verdampfer/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| So | Sauna output (0-10V) | Analoger Ausgang 0-10V für die Saunasteuerung. | - | ∞ |
| L1-3 | Sauna phase output (1-3) | Phasenausgang (L1-3) für die Saunasteuerung. | - | 0/1 |
| Ev | Evaporator output (0-10V) | Analoger Ausgang 0-10V für Verdampfersteuerung. | - | ∞ |
| Evd | Evaporator digital output | Digitaler Ausgang für Verdampfersteuerung. | - | 0/1 |
| On | Sauna state | An, solange Sauna und Trocknungsphase aktiv sind. | - | 0/1 |
| Fan | Fan | Ausgang zur Ansteuerung des Lüfters. | - | 0/1 |
| Stt | Sand timer remaining time | Sanduhr Restzeit | s | 0...∞ |
| Dry | Drying phase | Nachtrocknungsphase | - | 0/1 |
| Mode | Current sauna mode | 0 = Aus / Manuell, 1 = Finnisch manuell, 2 = Feuchte manuell, 3 = Finnische Sauna, 4 = Kräutersauna, 5 = Softdampfbad, 6 = Warmluftbad | - | ∞ |
| Ssd | Safety shutdown | Impuls, wenn die aktuelle Temperatur den im Parameter (Ssdϑ) eingestellten Wert überschreitet. | - | 0/1 |
| ϑt | Target temperature | Gibt die Zieltemperatur aus. | ° | ∞ |
| Ht | Target humidity | Gibt die Zielfeuchtigkeit aus. | % | 15...65 |
| Stoff | Sand timer end | Impuls, wenn die Sanduhr abgelaufen ist. | - | 0/1 |
| St | Sand timer state | Ein wenn die Sanduhr aktiv ist. | - | 0/1 |
| Ready | Sauna ready | Impuls, wenn die Zieltemperatur erreicht ist. | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung-mit-verdampfer/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| ϑd | Temperature deviation | Abweichung der aktuellen Temperatur (ϑc) von der Sitztemperatur (wenn die aktuelle Banktemperatur (ϑb) nicht verwendet wird). | ° | ∞ | 0 |
| Dryϑ | Drying phase temperature | Die Temperatur, die erforderlich ist, um den Lüfter in der Trocknungsphase zu starten. | ° | ∞ | 70 |
| Dryd | Drying phase duration | Lüftungsdauer nach Erreichen der Temperatur der Trocknungsphase (Dryϑ). | s | 0...∞ | 1800 |
| Std | Sand timer duration | Sanduhr Dauer | s | 0...∞ | 600 |
| Ssdϑ | Safety shutdown temperature | Bei Überschreitung werden alle Ausgänge ausgeschaltet, mit Ausnahme des Ausgangs (Ssd). | ° | ∞ | 139 |
| Ssdt | Safety shutdown time | Die Sauna wird zur eingestellten Zeit automatisch ausgeschaltet. Wenn der Eingang (P) verwendet wird, beginnt die Zeit zu laufen, wenn keine Anwesenheit mehr festgestellt wird. | s | 0...∞ | 7200 |
| PWMp | PWM period | Legt die PWM-Periode für die Phasenausgänge (L1-3) fest. | s | 0...∞ | 180 |
| G | Gain | Verstärkung für den Regler des PWM modulierten Ausgangs. Bei Verringerung des Werts reagiert die Temperaturregelung langsamer, bei Erhöhung schneller. Falls notwendig, ändern Sie den Wert in kleinen Schritten, um die Regelung an die Sauna anzupassen. | - | 0...∞ | 1 |
| Pm | Phase mode | Anzahl der verwendeten Phasen: 0 = 3 Phasen, 1 = 1 Phase, 2 = 2 Phasen im Verdampfermodus oder 3 Phasen im Modus ohne Verdampfer. Parameter wird nur angezeigt, wenn die Phasenausgänge (L2) und (L3) verwendet werden. | - | 0...2 | 2 |

Quelle: https://www.loxone.com/dede/kb/saunasteuerung-mit-verdampfer/

### Eigenschaften

[OFFEN] Keine spezialisierten Eigenschaften in der Dokumentation dokumentiert.

### Fallstricke

[BELEGT]

**Sicherheit - Keine Remanenz:** "Aus Sicherheitsgründen besitzt der Baustein keine Remanenz. Daher ist dieser nach einem Miniserver Neustart stets ausgeschaltet."

---

## Wecker

Alarm-Management mit konfigurierbaren Weckzeiten, Schlummerfunktion und optionalen Voralarm. Unterstützt Sanduhr, Bildschirmhelligkeit und Alarm-Sounds für Touch Nightlight Displays.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Ca | Confirm alarm | Alarm bestätigen | - | 0/1 |
| S | Start snooze timer | Ein Impuls setzt den Ausgang (Buzzer) auf 0 und startet den Snooze-Timer für die Dauer des Parameters (Sd). Ein weiterer Impuls während eines aktiven Snooze-Timers startet den Timer neu. | - | 0/1 |
| DisA | Disable alarm entries | Deaktiviert alle Alarmeinträge wenn Ein. | - | 0/1 |
| Tg | Toggle | Aktiviert/deaktiviert den Alarmeintrag 'Standardalarm'. Ein Impuls während eines aktiven Alarms beendet den Alarm. | - | 0/1 |
| Set | Set alarm time for default alarm | Definiert durch Minuten nach Mitternacht (z. B. 360 min = 06:00 Uhr) | min | 0...1439 |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/wecker/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Aon | Pulse on alarm start | Impuls bei Alarmstart | - | 0/1 |
| Aoff | Pulse on alarm end | Impuls bei Alarmende | - | 0/1 |
| Buzzer | Buzzer | Ein, wenn der Alarmton aktiv ist. Aus während der Schlummerzeit. | - | 0/1 |
| A | Alarm | Ein bei aktivem Alarm. | - | 0/1 |
| Pa | Pre-alarm | Gibt einen Impuls vor dem Alarm aus. Startzeit wird über Parameter (Pat) eingestellt. | - | - |
| Rst | Remaining snooze time | Verbleibende Schlummerzeit | s | 0...∞ |
| Da | Default alarm state | Ein, wenn der Alarmeintrag "Standardalarm" aktiviert ist. | - | 0/1 |
| Tna | Time of next alarm | Gibt Datum und Uhrzeit des nächsten Alarms aus. | - | - |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/wecker/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| MaxA | Maximum alarm duration | Beendet den Alarm nach der eingestellten Zeit. Wenn die Einstellung "Bestätigung benötigt" aktiviert ist, beginnt der Snooze-Timer nach Ablauf der Alarmdauer. | s | 0...∞ | 120 |
| Pat | Pre-alarm time | Legt fest, wie lange vor dem Alarm der Voralarm (Pa) gestartet wird. | s | 0...∞ | 180 |
| Sd | Snooze duration | Schlummerdauer bis zum erneuten Start des Alarms. | s | 60...1800 | 300 |
| Bri | Touch Nightlight display brightness inactive | Touch Nightlight Displayhelligkeit inaktiv. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | % | 0...100 | 0 |
| Bra | Touch Nightlight display brightness active | Touch Nightlight Displayhelligkeit aktiv. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | % | 0...100 | 50 |
| As | Alarm sound (Touch Nightlight) | (1: Tiefer 4-fach Piep, 2: Hoher 4-fach Piep, 3: Tiefer 2-fach Piep, 4: Hoher 2-fach Piep, 5: Sirene). Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 1...5 | 1 |
| Asv | Alarm sound volume (Touch Nightlight) | Lautstärke Weckalarm (Touch Nightlight). Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | % | 5...100 | 100 |
| Asf | Alarm sound fade-in (Touch Nightlight) | 1 = Lautstärke des Alarmtons steigt während 60 Sekunden langsam an. 0 = keine ansteigende Lautstärke. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/wecker/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Weckereigenschaften | Bearbeiten der Weckzeiten. | - |
| Bestätigung benötigt | Nach Ablauf des Alarms startet der Schlummertimer immer automatisch, bis eine Bestätigung erfolgt. | - |

Quelle: https://www.loxone.com/dede/kb/wecker/

### Fallstricke

[BELEGT] Im bereitgestellten Dokumenttext sind keine separaten Warn-, Achtungs- oder Hinweisboxen vorhanden. Die Dokumentation beschränkt sich auf tabellarische Darstellungen und eine kurze Erläuterung zur Konfiguration der Weckzeiten.

---

## Automatik-Regel

Aktiviert/deaktiviert automatische Regeln und löst konfigurierte Aktionslisten aus. Ermöglicht bedingte Automatisierungen mit optionalen App-Benachrichtigungen.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tg | Toggle | Automatik-Regel aktivieren / deaktivieren | 0/1 |
| Off | Disable automatic rule | Automatik-Regel deaktivieren | 0/1 |
| On | Enable automatic rule | Automatik-Regel aktivieren | 0/1 |

Quelle: https://www.loxone.com/dede/kb/automatik-regel/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| E | Enabled | Aktiviert | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

Quelle: https://www.loxone.com/dede/kb/automatik-regel/

### Parameter

[BELEGT] Im Dokument sind keine Parameter dokumentiert.

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Konfiguration | Konfiguration anzeigen | – |
| Benachrichtigung beim Ausführen | Benachrichtigung in der App anzeigen, wenn Aktionsliste ausgeführt wird. | – |

Quelle: https://www.loxone.com/dede/kb/automatik-regel/

### Fallstricke

[BELEGT] Im Dokument sind **keine Warnhinweise, Achtung-Boxen oder Hinweis-Boxen** vorhanden, die wörtlich wiedergegeben werden könnten.

---

## Zusammenfassung

| Baustein | Status | URL |
|----------|--------|-----|
| Türsteuerung | [BELEGT] | https://www.loxone.com/dede/kb/tuersteuerung/ |
| Tor | [BELEGT] | https://www.loxone.com/dede/kb/tor/ |
| Tor Zentral | [BELEGT] | https://www.loxone.com/dede/kb/tor-zentral/ |
| Bewässerung | [BELEGT] | https://www.loxone.com/dede/kb/bewaesserung/ |
| Poolsteuerung | [BELEGT] | https://www.loxone.com/dede/kb/poolsteuerung/ |
| Saunasteuerung | [BELEGT] | https://www.loxone.com/dede/kb/saunasteuerung/ |
| Saunasteuerung mit Verdampfer | [BELEGT] | https://www.loxone.com/dede/kb/saunasteuerung-mit-verdampfer/ |
| Wecker | [BELEGT] | https://www.loxone.com/dede/kb/wecker/ |
| Automatik-Regel | [BELEGT] | https://www.loxone.com/dede/kb/automatik-regel/ |
