# System, Ablauf & Schnittstellen

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## Ablaufsteuerung

Baustein zur sequenziellen Ausführung von Programmzeilen mit konfigurierbarem Intervall. Ermöglicht Steuerung mehrerer Sequenzen parallel mit individuellen Ausgängen pro Sequenz.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/ablaufsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| S1-8 | Activate sequence 1-8 | Aktiviert Sequenz 1-8 | 0/1 |
| AI1-8 | Inputs 1-8 | Eingänge 1-8 | ∞ |
| S | Select sequence | Sequenz auswählen | 0...8 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/ablaufsteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| AQ1-8 | Outputs 1-8 | Ausgänge 1-8 | ∞ |
| S | Current active sequence | Aktuell aktive Sequenz | ∞ |
| L | Current program line | Aktuelle Programmzeile | ∞ |
| TQ | Text output | Der Ausgang kann von Sequenzen verwendet werden. | — |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | — |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/ablaufsteuerung/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|---|---|---|---|
| Konfiguration | Programmcode Editor | — | — |
| Intervall [ms] | Intervall von Zeile zu Zeile in Millisekunden. Beeinflusst die Ausführungsgeschwindigkeit von Sequenzen. Niedrige Werte erhöhen die Ausführungsgeschwindigkeit, können aber auch die CPU-Last erhöhen. | 20...1000 | 500 |

### Hinweise

[BELEGT] https://www.loxone.com/dede/kb/ablaufsteuerung/

"Variablen und benutzerdefinierte Eingangsnamen dürfen nur alphanumerische Zeichen und Unterstriche enthalten."

Quelle: https://www.loxone.com/dede/kb/ablaufsteuerung/

---

## Sequenzer

Schaltet nacheinander vordefinierte Ausgänge ein. Trigger (Tr) schaltet zum nächsten Ausgang, Position (P) wählt direkt einen Ausgang aus. Optionale Remanenz speichert letzten Zustand.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/sequenzer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tr | Trigger | Schaltet den nächsten Ausgang ein. | 0/1 |
| P | Position | Wählt einen bestimmten Ausgang aus | 0...8 |
| R | Reset | Wenn 1 (O) = (Dv) | 0/1 |
| DisPc | Disable | Deaktiviert Eingänge (Tr) und (P) wenn Ein. (Kindersicherung) | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/sequenzer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| O1-8 | Output 1-8 | Ausgang 1-8 | 0/1 |
| Sel | Selected output | Gewählter Ausgang | 0...8 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/sequenzer/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| Max | Maximum number of used outputs | Maximale Anzahl verwendeter Ausgänge | 0...8 | 8 |
| Dv | Default value | Ausgang der bei (R) gesetzt werden soll (0 = alles aus) | 0...8 | 1 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/sequenzer/

Keine dokumentierten Warnhinweise, Achtung- oder Hinweis-Boxen vorhanden.

Quelle: https://www.loxone.com/dede/kb/sequenzer/

---

## Programm (Baustein)

Ermöglicht die Realisierung komplexer Funktionen und Abläufe in der Scriptsprache Pico C. Richtet sich an Entwickler mit guten C-Programmierkenntnissen.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/script-programming/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| T1-3 | Text input 1-3 | Texteingang 1-3 | - |
| I1-13 | Input 1-13 | Eingang 1-13 | ∞ |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/script-programming/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Txt1-3 | Text output 1-3 | Maximale Länge für die Textausgabe: 4096 Bytes | - |
| O1-13 | Output 1-13 | Ausgang 1-13 | ∞ |
| Etxt | Error text | Fehlertext | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/script-programming/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/script-programming/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Programmcode | Programmcode Editor | - |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/script-programming/

"Es sind daher gute Programmierkenntnisse in der Sprache C erforderlich."

"Beachten Sie, dass der Miniserver bei Erkennen eines Fehlers im Programm gegebenenfalls einen Neustart zur Sicherstellung der Datenkonsistenz durchführen kann."

"Da dieser Baustein für Entwickler gedacht ist, wird kein Support angeboten."

"Es werden maximal 8 Programm-Bausteine unterstützt."

Quelle: https://www.loxone.com/dede/kb/script-programming/

---

## Ping

Überwacht die Erreichbarkeit eines Ziels per Ping-Protokoll. Online-Ausgang bleibt aktiv, solange das Ziel erreichbar ist. Konfigurierbare Ping-Intervalle und Timeout-Parameter.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/ping/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/ping/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Online | Online | Ausgang ist aktiviert solange Ziel erreichbar ist | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/ping/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Pi | Ping interval | Zeit zwischen erfolgreichen Pings | s | 0...∞ | 10 |
| Td | Timeout duration | Zeit zwischen fehlgeschlagenen Pings | s | 0...∞ | 30 |
| N | Number of unsuccessful pings | Anzahl Timeout bevor Ausgang ausgeschaltet wird | - | 0...∞ | 5 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/ping/

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|-------------|---------|--------------|--------------|
| Ping-Adresse | Adresse zum Überprüfen, ob die Internetverbindung besteht. Z.B.: 8.8.8.8 | - | - | - |
| Wartezeit nach Start | Verzögerung der ersten Abfrage nach Neustart des Programms. | s | 0...3600 | - |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/ping/

Keine zusätzlichen Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/ping/

---

## Netzwerk Interkommunikation

Ermöglicht Kommunikation zwischen mehreren Miniservern über UDP. Jeder Server bekommt eine eindeutige ID und Kanäle mit Sender/Empfänger-Paaren. Verschlüsselt bei Bedarf.

### Eingänge

[OFFEN] Keine Eingänge-Tabelle in der Dokumentation vorhanden.

### Ausgänge

[OFFEN] Keine Ausgänge-Tabelle in der Dokumentation vorhanden.

### Parameter

[OFFEN] Keine Parameter-Tabelle in der Dokumentation vorhanden.

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/netzwerk-interkommunikation/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|---|---|---|---|
| Eigene ID | ID, mit welcher der eigene Miniserver von anderen Gegenstellen eindeutig identifiziert werden kann. Maximale Länge: 8 Zeichen | - | - |
| Port | UDP Port auf welchem Pakete empfangen werden. Stellen Sie diesen Port auch auf dem Sender-Miniserver in den Eigenschaften der Gegenstelle ein. | 1000...65535 | 61263 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/netzwerk-interkommunikation/

"Die **Übertragungskapazität** der Netzwerk Interkommunikation ist auf 35 Nachrichten pro Sekunde gemittelt über einen Zeitraum von 2 Minuten beschränkt."

"Für verschlüsselte Kommunikation zwischen Miniservern über das Internet benötigen beide Seiten Portweiterleitungen."

"Bei mehreren Kanälen mit gleichen Sendern/Empfängern ist für jeden Kanal ein unterschiedliches Kennwort erforderlich."

Quelle: https://www.loxone.com/dede/kb/netzwerk-interkommunikation/

---

## BACnet

BACnet-Server auf aktuellen Miniserver-Generationen. Ermöglicht Kommunikation mit externen BACnet-Systemen. Mindestversion: Miniserver Gen. 2 oder höher (Gen. 1 nicht unterstützt).

### Eingänge

[OFFEN] Keine Eingänge-Tabelle in der Dokumentation vorhanden.

### Ausgänge

[OFFEN] Keine Ausgänge-Tabelle in der Dokumentation vorhanden.

### Parameter

[OFFEN] Keine Parameter-Tabelle in der Dokumentation vorhanden.

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/bacnet/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|---|---|---|---|
| Port | TCP Port, mit dem dieser BACnet Server erreichbar ist | 1...65535 | 47808 |
| Passwort | Passwort, das für den BACnet-Befehl 'Reinitialize Device' verwendet wird. Ist kein Passwort vorhanden, wird der Befehl nicht zugelassen. | - | - |
| Instanznummer | BACnet-Instanznummer, die der Miniserver im BACnet-Netzwerk verwendet. | ∞ | 0 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/bacnet/

"Für BACnet ist der aktuelle Miniserver notwendig, der Miniserver Gen. 1 wird nicht unterstützt!"

Quelle: https://www.loxone.com/dede/kb/bacnet/

---

## Home Connect

Integration von Home Connect-Hausgeräten (Bosch/Siemens/Neff). Benötigt aktiven Home Connect Account, aktive Internetverbindung und Miniserver Gen. 2+. Frequentes Schalten der Aktoren vermeiden.

### Eingänge

[OFFEN] Keine Standard-Eingänge-Tabelle in der Dokumentation vorhanden.

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/home-connect/

| Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|
| Onlinestatus Home Connect | Gibt an, ob das Gerät für den Miniserver erreichbar ist. | 0/1 |

### Parameter

[OFFEN] Keine dedizierte Parameter-Tabelle in der Dokumentation vorhanden.

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/home-connect/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Dienst überwachen | Wenn angehakt, werden Sie über Systemstatus benachrichtigt, wenn dieser Dienst offline ist. | - |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/home-connect/

"Vermeiden Sie Programmierungen, die Aktoren frequentiert beschalten."

"Zur Verwendung ist ein Home Connect Account erforderlich! Der Miniserver Gen. 1 wird nicht unterstützt. Die Home Connect Geräte und der Miniserver müssen über eine aktive Internetverbindung verfügen."

"Detaillierte Listen unterstützter Funktionen und Geräte finden sich in einem separaten PDF-Dokument."

Quelle: https://www.loxone.com/dede/kb/home-connect/

---

## Event Database Connector

Schreibt Ereignisse in Datenbank-Tabellen. Jeder Trigger (ETr) speichert die konfigurierten Spalten und Custom Inputs (CI1-16). Mit User-ID können Benutzerfelder referenziert werden.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/event-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| ETr | Trigger | Ein Impuls am Eingang löst einen Schreibvorgang in der Datenbank aus | 0/1 |
| Uid | User-ID | User-ID. Wenn vor dem Auslösen festgelegt, können die Benutzerfelder des entsprechenden Benutzers verwendet werden | – |
| CI1-CI16 | Custom input 1-16 | Zusätzliche benutzerdefinierte Eingänge 1-16 | – |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/event-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung |
|--------|------------------|-------------|
| Log | Log output | Logausgang bei jedem Schreibvorgang in die Datenbank |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/event-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Td | Trigger Delay | Verzögert das Schreiben in die Datenbank nach dem Auslösen, um sicherzugehen, dass alle Eingänge gesetzt sind | ms | ∞ | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/event-database-connector/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Spalteninhalt | Bearbeiten Sie den Inhalt der Spalte. Geben Sie die Daten an, die in die Datenbankspalten geschrieben werden sollen | – |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/event-database-connector/

Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/event-database-connector/

---

## Session Database Connector

Erfasst Start/Ende von Sessions (z.B. Anwesenheit) in Datenbank. Session-Aktivitäten und User-IDs können zusammen mit Custom Inputs gespeichert werden. Trigger Delay sichert konsistente Datenerfassung.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/session-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| SStart | Session start | Ein Impuls am Eingang löst den Beginn einer Session aus und schreibt in die Datenbank, falls konfiguriert. | 0/1 |
| SEnd | Session end | Ein Impuls am Eingang löst das Ende einer Session aus und schreibt in die Datenbank, falls konfiguriert. | 0/1 |
| Uid | User-ID | User-ID. Wenn vor dem Auslösen festgelegt, können die Benutzerfelder des entsprechenden Benutzers verwendet werden. | - |
| CI1-CI16 | Custom input 1-16 | Zusätzliche benutzerdefinierte Eingänge 1-16 | - |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/session-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Log | Log output | Logausgang bei jedem Schreibvorgang in die Datenbank | - |
| Sa | Session active | Aktiv, wenn eine Sitzung gerade läuft | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/session-database-connector/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Td | Trigger Delay | Verzögert das Schreiben in die Datenbank nach dem Auslösen, um sicherzugehen, dass alle Eingänge gesetzt sind | ms | ∞ | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/session-database-connector/

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Spalteninhalt | Bearbeiten Sie den Inhalt der Spalte. Geben Sie die Daten an, die in die Datenbankspalten geschrieben werden sollen. | - |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/session-database-connector/

Keine separaten Warnhinweise, Achtung-Boxen oder Hinweis-Boxen dokumentiert.

Quelle: https://www.loxone.com/dede/kb/session-database-connector/

---

## Multiplikator Projekt

Infrastruktur zur Verteilung identischer Programmierungen auf mehrere Miniserver (z.B. für Hotelzimmer oder Wohnungen). Trust-Verwaltung und unabhängige Konfigurationsmöglichkeiten pro Server.

### Eingänge

[OFFEN] Nicht anwendbar - Multiplikator Projekt ist keine Konfigurationskomponente mit Eingängen/Ausgängen.

### Ausgänge

[OFFEN] Nicht anwendbar - Multiplikator Projekt ist keine Konfigurationskomponente mit Eingängen/Ausgängen.

### Parameter

[OFFEN] Nicht anwendbar - Multiplikator Projekt ist keine Konfigurationskomponente mit Parametern.

### Eigenschaften

[OFFEN] Keine Tabelle in der Dokumentation vorhanden. Dokumentation beschreibt konzeptionell vier Hauptabschnitte: Einrichtung, Grundprogrammierung, unabhängige Programmierung einzelner Miniserver und Trust-Verwaltung.

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/multiplikator-projekt/

"Aktueller Miniserver / Go / Compact erforderlich, von Miniserver Gen. 1 Varianten nicht unterstützt!"

"In einem Multiplikator-Projekt können nur gleiche Miniserver Varianten verwendet werden."

"Der Multiplikator kann nicht für Gateway-/Client-Konfigurationen verwendet werden."

Quelle: https://www.loxone.com/dede/kb/multiplikator-projekt/

---

## Zusammenfassung Datenqualität

- **Bausteine mit vollständigen Tabellen (Eingänge, Ausgänge, Parameter, Eigenschaften):** Ablaufsteuerung, Sequenzer, Programm, Ping, Event Database Connector, Session Database Connector
- **Bausteine mit unvollständigen Tabellen:** Netzwerk Interkommunikation, BACnet, Home Connect (keine Standard-Eingänge; Netzwerk Interkommunikation und BACnet haben keine Eingänge/Ausgänge-Tabellen)
- **Nicht-Konfigurationskomponente:** Multiplikator Projekt (keine Tabellen; konzeptionelle Dokumentation nur)

Alle Tabellen wurden direkt von der offiziellen Loxone-Dokumentation [BELEGT] oder als [OFFEN] gekennzeichnet, wenn nicht verfügbar.
