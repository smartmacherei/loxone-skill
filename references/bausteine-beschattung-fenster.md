# Beschattung & Fenster

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.

Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## ### Automatikbeschattung

Steuert Beschattungseinrichtungen wie Jalousien, Rolläden, Vorhänge oder Markisen mit Antriebsmotoren über Relaiskontakte.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | - | 0/1 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| Co | Complete open | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Cc | Complete close | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| So | Slightly open | Jalousien schließen sich vollständig und bewegen die Lamellen in horizontale Position eingestellt durch Parameter (Rd). Rolläden, Vorhänge und Markisen fahren in die Position entsprechend Parameter (Rd). | - | 0/1 |
| Sps | Sun position automatic start | Wenn Ein zu Beginn, oder bei Impuls während der Beschattungszeit wird die Sonnenstandsautomatik aktiviert. Die Sonnenstandsautomatik wird für den Rest des Tages deaktiviert, wenn der Baustein manuell bedient wird. Impuls an (Spr) gefolgt von einer steigenden Flanke an (Sps) oder Impuls an (Spr) während (Sps) aktiv ist, startet die Sonnenstandsautomatik erneut. | - | 0/1 |
| DisSp | Disable sun position automatic | Deaktiviert die Sonnenstandsautomatik wenn Ein. | - | 0/1 |
| Spr | Sun position automatic restart | Impuls gefolgt von einer steigenden Flanke am Eingang (Sps) oder Impuls während Eingang (Sps) aktiv ist, startet die Sonnenstandsautomatik erneut. | - | 0/1 |
| Wa | Wind alarm | Fährt die Beschattung in die Windalarm-Position laut Parameter (Wap) und sperrt den Baustein. Wird für den Sturmschutz verwendet. Die aktive Automatik wird nur unterbrochen statt abgebrochen. Nach Ende des Windalarms wird die Automatik mit einer positiven Flanke an Sps oder der Sonnenschein-Systemvariablen neu gestartet. Die Bedingungen für die Automatik werden am Ende des Windalarms nicht neu bewertet. Wenn beide Bedingungen während des Windalarms dauerhaft aktiv sind, kann die Automatik über einen Impuls an Spr neu gestartet werden. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | - | 0/1 |
| Dwc | Door/window contact | Öffnet die Beschattung vollständig und sperrt den Baustein bei Aktivierung. Manuelle Bedienung über die Benutzeroberfläche ist weiterhin möglich. (0 = geschlossen, 1 = geöffnet). | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| Pos | Position of shading | Bewegt die Beschattung in die angegebene Position. | % | 0...100 |
| Slat | Position of slats | Dient zum manuellen Ansteuern der Lamellen in eine bestimmte Position. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | % | 0...100 |
| T5 | T5 control | Taste 1: Complete open Taste 4: Complete close | - | ∞ |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Po, Pc, Co, Cc, So, T5 wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Op | Open | Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Cl | Close | Schließen Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Pos | Position of shading | Position der Beschattung (0.0 = offen, 1.0 = geschlossen) | - | 0...1 |
| Slat | Position of slats | Position der Lamellen (0.0 = horizontal, 1.0 = vertikal) Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...1 |
| Sp | Sun position automatic | Ein, wenn Eingang (Sps) = 1 und Eingang (DisSp) = 0 ...und wenn die Einstellung "Sonnenschein verwenden" aktiviert ist und die Sonne scheint, oder wenn die Sonnenstandsautomatik in der App eingeschaltet wird. | - | 0/1 |
| Wds | Wind, door/window contact state | Aktiv, wenn Eingang (Wa) oder Eingang (Dwc) 1 ist. | - | 0/1 |
| Off | Off | Aktiv, wenn Eingang (Off) 1 ist. | - | 0/1 |
| AQpp | Command output | Wird bei bestimmten Geräten verwendet. Befehl * 1000000 + Jalousieposition in % * 1000 + Lamellenposition in °. Befehl 0 = Stop, 1 = Jalousieposition + Lamellenposition, 2 = nur Jalousieposition, 3 = nur Lamellenposition. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| TPos | Target position | Zielposition der Beschattung. Kann z.B. für Hunter Douglas Beschattungen verwendet werden. | % | 0...100 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|--------|-------------|--------------|
| Type | Shading type | Typ der Beschattungseinrichtung 0 = Jalousie/Raffstore 1 = Rollladen/Rollo/Dachrollo 2 = Vorhang beidseitig 3 = Schlotterer Retrolux 4 = Vorhang links 5 = Vorhang rechts 6 = Markise | - | 0...6 | 0 |
| Wap | Wind alarm position | 0 = Vollständig geöffnet 1 = Vollständig geschlossen | - | 0/1 | 0 |
| Spe | Sun position automatic end action | Definiert, was das System tut, wenn die Sonnenstandsautomatik endet. Diese Aktion wird nur ausgelöst, wenn die berechnete Automatikbeschattung-bis-Zeit erreicht ist. Manuelle Eingriffe oder andere Ereignisse, die die Sonnenstandsautomatik abbrechen, lösen diese Aktion nicht aus.0 = Keine Aktion 1 = Vollständig öffnen 2 = Vollständig schließen 3 = Lamellen horizontal stellen | - | 0...3 | 1 |
| Tlc | Time long-click | Langklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen / Schließen. Wenn Sie einen Doppelklick bevorzugen, dann stellen Sie den Wert > (Opd) oder (Cld) ein. 0 = Immer komplette Fahrt starten. | s | 0...∞ | 3 |
| Opd | Opening duration | Dauer Öffnen | s | 0...∞ | 75 |
| Cld | Closing duration | Dauer Schließen | s | 0...∞ | 70 |
| Mld | Motor lock duration | Dauer der Motorverrieglung bei Richtungswechsel. | s | 0...∞ | 0,5 |
| Tdc | Time double-click | Doppelklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen / Schließen. 0 = Nicht verwendet | s | 0...∞ | 0,3 |
| Rd | Return duration | Jalousien: Rücklaufzeit, bis die Lamellen horizontal ausgerichtet sind. Rollos, Vorhänge, Markisen: Position für den Eingang (So) im Bereich von offen [0,1] bis geschlossen [1,0] einstellen. Der Wert muss > 0 sein. | s | 0.1...∞ | 0,8 |
| Bldo | Backlash duration opposite | Totzeit bei Bewegung in Gegenrichtung. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | 0...∞ | 0,15 |
| Bld | Backlash duration | Totzeit bei Bewegung in die gleiche Richtung. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | 0...∞ | 0 |
| minTd | Minimum travel duration | Mindestfahrzeit bei Impuls auf Eingang (Po) bzw. (Pc). | s | 0...∞ | 0,4 |
| Dir | Compass direction | Himmelsrichtung des Fensters: 0 = Norden 90 = Osten 180 = Süden 270 = Westen -1 = nicht konfiguriert | ° | -1...360 | -1 |
| Dts | Direction tolerance start | Richtungstoleranz für die Sonnenstandsautomatik bei Sonneneintritt. | ° | 0...90 | 85 |
| Dte | Direction tolerance end | Richtungstoleranz für die Sonnenstandsautomatik bei Sonnenaustritt. | ° | 0...90 | 85 |
| Sw | Slat width | Breite der Lamellen. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | mm | 0...∞ | 70 |
| Sd | Slat distance | Abstand zwischen zwei horizontalen Lamellen. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | mm | 0...∞ | 60 |
| Spm | Sun position automatic mode | 0 = Optimale Helligkeit - blockiert direkte Sonneneinstrahlung, bei soviel Licht wie möglich. Automatik bleibt aus bei geschlossener Beschattung. Wenn der Eingang (Sps) aktiv ist, startet ein Impuls an (Spr) die Sonnenstandsautomatik. 1 = Optimale Kühlung - blockiert die Einstrahlung noch stärker, führt aber auch zu weniger Helligkeit. Automatik bleibt aus bei geschlossener Beschattung. Wenn der Eingang (Sps) aktiv ist, startet ein Impuls an (Spr) die Sonnenstandsautomatik. 2 = Optimale Helligkeit - blockiert direkte Sonneneinstrahlung, bei soviel Licht wie möglich. Automatik wird auch bei geschlossener Beschattung aktiviert. 3 = Optimale Kühlung - blockiert die Einstrahlung noch stärker, führt aber auch zu weniger Helligkeit. Automatik wird auch bei geschlossener Beschattung aktiviert. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...3 | 1 |
| Spi | Sun position automatic interval | Legt fest, wie oft die Lamellen während der Sonnenstandsautomatik nachgestellt werden. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | min | 1...180 | 120 |
| Spos | Sun position automatic start offset | Startzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenaufgang. | min | -90...90 | 30 |
| Spoe | Sun position automatic end offset | Endzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenuntergang. | min | -90...90 | -30 |
| Rdd | Reference Drive Down | Wenn eingeschaltet, löst jeder Schließbefehl ein vollständiges Herunterfahren aus, sodass sich die Jalousien für die gesamte konfigurierte Schließdauer bewegen. Selbst wenn die Jalousien bereits geschlossen sind, wird der Baustein die Ausgänge reaktivieren, um sicherzustellen, dass die Jalousien mit ihrer hardwaredefinierten Endposition übereinstimmen. Der Baustein für automatische Beschattung definiert nicht die untere Grenze – diese wird durch die Konfiguration Ihrer Jalousien bestimmt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|-------------|--------------|
| Sonnenschein verwenden | Die Sonnenstandsautomatik wird nur aktiviert, wenn die Systemvariable Sonnenschein und der Eingang Sps aktiv sind. | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie/

"Wenn die Sonnenstandsautomatik aktiviert ist, bedeutet dies nicht, dass auch sofort eine Bewegung durchgeführt wird. Die Beschattung startet erst in Abhängigkeit der Position der Sonne und der zugehörigen Parameter."

Quelle: https://www.loxone.com/dede/kb/automatikjalousie/

---

## ### Automatikbeschattung Integriert

Steuert Beschattungseinrichtungen wie Jalousien oder Rolläden mit Beschattungsantrieben, die eine integrierte Ansteuerungs-Schnittstelle haben.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie-integriert/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | - | 0/1 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| Co | Complete open | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Cc | Complete close | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| So | Slightly open | Jalousien schließen sich vollständig und bewegen die Lamellen in die Beschattungsposition. | - | 0/1 |
| Sps | Sun position automatic start | Wenn Ein zu Beginn, oder bei Impuls während der Beschattungszeit wird die Sonnenstandsautomatik aktiviert. | - | 0/1 |
| DisSp | Disable sun position automatic | Deaktiviert die Sonnenstandsautomatik wenn Ein. | - | 0/1 |
| Spr | Sun position automatic restart | Impuls gefolgt von einer steigenden Flanke am Eingang (Sps) oder Impuls während Eingang (Sps) aktiv ist. | - | 0/1 |
| Wa | Wind alarm | Fährt die Beschattung in die Windalarm-Position laut Parameter (Wap) und sperrt den Baustein. | - | 0/1 |
| Dwc | Door/window contact | Öffnet die Beschattung vollständig und sperrt den Baustein bei Aktivierung. | - | 0/1 |
| Off | Off / Lock | Pulse (<200ms): Stops movement. Pulse (>200ms): Block is locked. Dominating input. | - | 0/1 |
| Pos | Position of shading | Bewegt die Beschattung in die angegebene Position. | % | 0...100 |
| Slat | Position of slats | Dient zum manuellen Ansteuern der Lamellen in eine bestimmte Position. | % | 0...100 |
| T5 | T5 control | Taste 1: Complete open; Taste 4: Complete close | - | ∞ |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Po, Pc, Co, Cc, So, T5 wenn Ein. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie-integriert/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Pos | Position of shading | 0.0 = offen, 1.0 = geschlossen | 0...1 |
| Slat | Position of slats | 0,0 = horizontal, 1,0 = vertikal | 0...1 |
| Im | In motion | Jalousie in Bewegung | 0/1 |
| Blk | Motor blocked | Motor blockiert | 0/1 |
| Obs | Obstacle | 1 = Es wurde ein Hindernis erkannt. | 0/1 |
| Sp | Sun position automatic | Ein, wenn Eingang (Sps) = 1 und Eingang (DisSp) = 0 ...und wenn die Einstellung 'Sonnenschein verwenden' aktiviert ist | 0/1 |
| Wds | Wind, door/window contact state | Aktiv, wenn Eingang (Wa) oder Eingang (Dwc) 1 ist. | 0/1 |
| Off | Off | Aktiv, wenn Eingang (Off) 1 ist. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie-integriert/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Wap | Wind alarm position | 0 = Vollständig geöffnet; 1 = Vollständig geschlossen | - | 0/1 | 0 |
| Spe | Sun position automatic end action | 0 = Keine Aktion; 1 = Vollständig öffnen; 2 = Vollständig schließen; 3 = Lamellen horizontal stellen | - | 0...3 | 1 |
| Spm | Sun position automatic mode | 0/1 = Optimale Helligkeit/Kühlung (Automatik bleibt aus bei geschlossener Beschattung); 2/3 = Auch bei geschlossener Beschattung | - | 0...3 | 1 |
| Tlc | Time long-click | Langklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen/Schließen. | ∞ | ∞ | 3 |
| Tdc | Time double-click | Doppelklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen/Schließen. | s | 0...∞ | 0,3 |
| Dir | Compass direction | Himmelsrichtung des Fensters: 0 = Norden; 90 = Osten; 180 = Süden; 270 = Westen; -1 = nicht konfiguriert | - | -1...360 | -1 |
| Dts | Direction tolerance start | Richtungstoleranz für die Sonnenstandsautomatik bei Sonneneintritt. | ° | 0...90 | 85 |
| Dte | Direction tolerance end | Richtungstoleranz für die Sonnenstandsautomatik bei Sonnenaustritt. | ° | 0...90 | 85 |
| Spi | Sun position automatic interval | Legt fest, wie oft die Lamellen während der Sonnenstandsautomatik nachgestellt werden. | min | 1...∞ | 60 |
| Spos | Sun position automatic start offset | Startzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenaufgang. | min | -90...90 | 30 |
| Spoe | Sun position automatic end offset | Endzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenuntergang. | min | -90...90 | -30 |
| Sop | Slightly open position | Für den Eingang (So) und (Sps) verwendete Position. | - | 0...1 | 0,8 |
| Sw | Slat width | Breite der Lamellen. | mm | 0...∞ | 70 |
| Sd | Slat distance | Abstand zwischen zwei horizontalen Lamellen. | mm | 0...∞ | 60 |
| Spu | Slat position upwards movement | Lamellenposition waagrecht in Prozent | % | 0...50 | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie-integriert/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Sonnenschein verwenden | Die Sonnenstandsautomatik wird nur aktiviert, wenn die Systemvariable Sonnenschein und der Eingang Sps aktiv sind. | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. | 0...100 | 20 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/automatikjalousie-integriert/

"Wenn die Sonnenstandsautomatik aktiviert ist, bedeutet dies nicht, dass auch sofort eine Bewegung durchgeführt wird. Die Beschattung startet erst in Abhängigkeit der Position der Sonne und der zugehörigen Parameter."

Quelle: https://www.loxone.com/dede/kb/automatikjalousie-integriert/

---

## ### Automatikbeschattung Zentral

Mit diesem Baustein können mehrere Beschattungsbausteine gemeinsam gesteuert werden.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/beschattung-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | 0/1 | 0/1 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | 0/1 | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | 0/1 | 0/1 |
| Co | Complete open | Stoppen nicht möglich. | 0/1 | 0/1 |
| Cc | Complete close | Stoppen nicht möglich. | 0/1 | 0/1 |
| So | Slightly open | Jalousien schließen sich vollständig und bewegen die Lamellen in horizontale Position eingestellt durch Parameter (Rd). | 0/1 | 0/1 |
| Sps | Sun position automatic start | Wenn Ein zu Beginn, oder bei Impuls während der Beschattungszeit wird die Sonnenstandsautomatik aktiviert. | 0/1 | 0/1 |
| DisSp | Disable sun position automatic | Deaktiviert die Sonnenstandsautomatik wenn Ein. | 0/1 | 0/1 |
| Spr | Sun position automatic restart | Impuls gefolgt von einer steigenden Flanke am Eingang (Sps) startet die Sonnenstandsautomatik erneut. | 0/1 | 0/1 |
| Wa | Wind alarm | Fährt die Beschattung in die Windalarm-Position laut Parameter (Wap). | 0/1 | 0/1 |
| Off | Off / Lock | Pulse (<200 ms): Stops movement. Pulse (>200 ms): Block is locked. Dominating input. | 0/1 | 0/1 |
| Pos | Position of shading | Bewegt die Beschattung in die angegebene Position. | % | 0...100% |
| Slat | Position of slats | Dient zum manuellen Ansteuern der Lamellen in eine bestimmte Position. | % | 0...100% |
| T5 | T5 control | Taste 1: Complete open, Taste 4: Complete close | ∞ | ∞ |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Po, Pc, Co, Cc, So, T5 wenn Ein. | 0/1 | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/beschattung-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | – |
| No | Open shades | Anzahl der geöffneten Beschattungen | ∞ |
| Nc | Closed shades | Anzahl der geschlossenen Beschattungen | ∞ |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/beschattung-zentral/

Alle ausgewählten Beschattungs-Bausteine können gemeinsam gesteuert werden.

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise auf der Seite gefunden.

Quelle: https://www.loxone.com/dede/kb/beschattung-zentral/

---

## ### Dachfenster Beschattung

Steuert die Beschattung eines Dachflächenfensters mit Sonnenstandsautomatik und Windalarmschutz.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/dachfenster-rollo/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | - | 0/1 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| Co | Complete open | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Cc | Complete close | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Dwc | Door/window contact | Öffnet die Beschattung vollständig und sperrt den Baustein bei Aktivierung. Manuelle Bedienung über die Benutzeroberfläche ist weiterhin möglich. (0 = geschlossen, 1 = geöffnet). | - | 0/1 |
| Wa | Wind alarm | Fährt die Beschattung in die Windalarm-Position laut Parameter (Wap) und sperrt den Baustein. Wird für den Sturmschutz verwendet. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| Pos | Position of shading | Bewegt die Beschattung in die angegebene Position. | % | 0...100 |
| T5 | T5 control | Taste 1: Complete open, Taste 4: Complete close | - | ∞ |
| DisPc | Disable periphery control | Deaktiviert die Eingänge Tg, Po, Pc, Co, Cc, So, T5 wenn Ein. Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| So | Slightly open | Jalousien schließen sich vollständig und bewegen die Lamellen in horizontale Position. Rolläden, Vorhänge und Markisen fahren in die Position entsprechend Parameter (Rd). | - | 0/1 |
| Sps | Sun position automatic start | Wenn Ein zu Beginn, oder bei Impuls während der Beschattungszeit wird die Sonnenstandsautomatik aktiviert. | - | 0/1 |
| DisSp | Disable sun position automatic | Deaktiviert die Sonnenstandsautomatik wenn Ein. | - | 0/1 |
| Spr | Sun position automatic restart | Impuls gefolgt von einer steigenden Flanke am Eingang (Sps) oder Impuls während Eingang (Sps) aktiv ist, startet die Sonnenstandsautomatik erneut. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/dachfenster-rollo/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Op | Open | Öffnen. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| Cl | Close | Schließen. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| Pos | Position of shading | Position der Beschattung (0.0 = offen, 1.0 = geschlossen) | 0...1 |
| Wds | Wind, door/window contact state | Ein, wenn der Eingang (Wa) des Bausteins oder eines verknüpften Zentralbausteins aktiv ist oder wenn der Eingang (Dwc) aktiv ist. | 0/1 |
| Off | Off | Aktiv, wenn Eingang (Off) 1 ist. | 0/1 |
| Sp | Sun position automatic | Ein, wenn Eingang (Sps) = 1 und Eingang (DisSp) = 0 ...und wenn die Einstellung "Sonnenschein verwenden" aktiviert ist. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/dachfenster-rollo/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|--------|-------------|--------------|
| Wap | Wind alarm position | 0 = Vollständig geöffnet, 1 = Vollständig geschlossen | - | 0/1 | 0 |
| Opd | Opening duration | Dauer Öffnen | s | 0...∞ | 75 |
| Cld | Closing duration | Dauer Schließen | s | 0...∞ | 75 |
| Mld | Motor lock duration | Dauer der Motorverrieglung bei Richtungswechsel. | s | 0...∞ | 0,5 |
| Tdc | Time double-click | Doppelklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen / Schließen. 0 = Nicht verwendet | s | 0...∞ | 0,3 |
| Tlc | Time long-click | Langklickdauer an Eingängen (Po), (Pc) für vollständiges Öffnen / Schließen. | s | 0...∞ | 3 |
| minTd | Minimum travel duration | Mindestfahrzeit bei Impuls auf Eingang (Po) bzw. (Pc). | s | 0...∞ | 0,4 |
| Spm | Sun position automatic mode | 0 = Automatik bleibt ausgeschaltet, wenn die Beschattung geschlossen ist. 1 = Automatik immer erlaubt. | - | 0...1 | 1 |
| Spe | Sun position automatic end action | 0 = keine Aktion, 1 = vollständig öffnen, 2 = vollständig schließen | - | 0...2 | 1 |
| Dir | Compass direction | Himmelsrichtung des Fensters: 0 = Norden, 90 = Osten, 180 = Süden, 270 = Westen, -1 = nicht konfiguriert | ° | -1...359 | -1 |
| Dts | Direction tolerance start | Richtungstoleranz für die Sonnenstandsautomatik bei Sonneneintritt. | ° | 0...90 | 85 |
| Dte | Direction tolerance end | Richtungstoleranz für die Sonnenstandsautomatik bei Sonnenaustritt. | ° | 0...90 | 85 |
| Pi | Pitch | Dach- oder Fensterneigung: 0 = horizontal, 90 = vertikal | ° | 0...90 | 30 |
| Spos | Sun position automatic start offset | Startzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenaufgang. | min | -90...90 | 30 |
| Spoe | Sun position automatic end offset | Endzeit Verschiebung der Sonnenstandsautomatik relativ zum Sonnenuntergang. | min | -90...90 | -30 |
| Sop | Slightly open position | Für den Eingang (So) und (Sps) verwendete Position. | % | 0...100 | 80 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/dachfenster-rollo/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|-------------|--------------|
| Sonnenschein verwenden | Die Sonnenstandsautomatik wird nur aktiviert, wenn die Systemvariable Sonnenschein und der Eingang Sps aktiv sind. | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise auf der Seite gefunden.

Quelle: https://www.loxone.com/dede/kb/dachfenster-rollo/

---

## ### EIB Beschattung

EIB Jalousiesteuerung mit Zweitastenbedienung zur Steuerung von Beschattungssystemen über EIB-basierte Ein- und Ausgänge.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/eib-beschattung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| Pos | Position | Rückmeldung der aktuellen Position der Beschattung | % | 0...100 |
| DisPc | Disable periphery control | Deaktiviert Po, Pc bei Aktivierung (z.B. Kindersicherung). Visualisierung bleibt möglich. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/eib-beschattung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Lo | Long-term operation | -1 = passiv, 0 = öffnen, 1 = schließen. Mit EIB-Aktor verbinden. | ∞ |
| So | Short-term operation | -1 = passiv, 0 = öffnen, 1 = schließen. Mit EIB-Aktor verbinden. | ∞ |
| Pos | Position of shading | Position der Beschattung | ∞ |
| API | API Connector | API-basierter Verbinder zwischen Geräten und Bausteinen | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/eib-beschattung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|--------|-------------|--------------|
| Tlc | Time long-click | Impulsdauer Po/Pc zur Auslösung Langzeitbetrieb | s | 0...∞ | 0,3 |

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise gefunden.

Quelle: https://www.loxone.com/dede/kb/eib-beschattung/

---

## ### Fenster

Steuert ein Fenster mit automatisiertem Öffnen, Schließen und Positionieren mit verschiedenen Eingabemöglichkeiten und Wetterschutz.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/dachfenster/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Co | Complete open | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Cc | Complete close | Falls in Bewegung, wird gestoppt. | - | 0/1 |
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | - | 0/1 |
| Pos | Position of window | Bewegt das Fenster an die angegebene Position. | % | 0...100 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| Wp | Weather protection | Fenster wird geschlossen und für die weitere Bedienung gesperrt, wenn Ein. Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| Io | Is open | Eingang wird verwendet, um die "vollständig geöffnet" Position über einen Endschalter oder ähnliches zu melden. | - | 0/1 |
| Ic | Is closed | Eingang wird verwendet, um die "vollständig geschlossen" Position über einen Endschalter oder ähnliches zu melden. | - | 0/1 |
| CPos | Current position | Eingang, der die aktuelle Kippstellung oder Öffnungsweite des Fensters angibt. | % | 0...100 |
| So | Slightly Open | Bewegt das Fenster in eine leicht geöffnete Position, wenn die aktuelle Position anders ist. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/dachfenster/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Op | Open | Öffnen | - | 0/1 |
| Cl | Close | Schließen | - | 0/1 |
| Pos | Position of Window | Position des Fensters (0.0 = geschlossen, 1.0 = offen) | - | 0...1 |
| TPos | Target position | Ausgang für Soll-Kippstellung oder Soll-Öffnungsweite (Schüco). - Wenn der Eingang (Po) EIN ist (steigende Flanke), wird die Sollposition auf 100 gesetzt. - Wenn der Eingang (Pc) EIN ist (steigende Flanke), wird die Sollposition auf 0 gesetzt. - Wenn entweder der Eingang (Po) oder der Eingang (Pc) AUS sind (fallende Flanke), nimmt die Sollposition den Wert des Eingangs (CPos) an. Wenn der Eingang (CPos) nicht angeschlossen ist, wird die Zielposition berechnet. | % | 0...100 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/dachfenster/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|--------|-------------|--------------|
| Opd | Opening duration | Dauer Öffnen | s | 0...∞ | 5 |
| Cld | Closing duration | Dauer Schließen | s | 0...∞ | 5 |
| minTd | Minimum travel time | Mindestfahrzeit bei Impuls auf Eingang (Po) bzw. (Pc). | s | 0...∞ | 0,4 |
| Mld | Motor lock duration | Dauer der Motorverrieglung bei Richtungswechsel | s | 0...∞ | 0,5 |
| SoPos | Slightly Open Position | Zielposition für Eingang So | % | 0...100 | 50 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/dachfenster/

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|-------------|--------------|
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise gefunden.

Quelle: https://www.loxone.com/dede/kb/dachfenster/

---

## ### Fenster Zentral

Steuert mehrere Fenster zentral mit gemeinsamen Steuereingängen und aggregierten Statusausgängen.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/fenster-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Co | Complete open | Stoppen nicht möglich. | - | 0/1 |
| Cc | Complete close | Stoppen nicht möglich. | - | 0/1 |
| Tg | Toggle | Schaltet um zwischen Öffnen, Stopp, Schließen. Zur Eintastenbedienung. | - | 0/1 |
| Pos | Position of window | Bewegt die Fenster an die angegebene Position. | % | 0...100 |
| Po | Partial open with push & hold | Partiell öffnen durch Drücken & Halten | - | 0/1 |
| Pc | Partial close with push & hold | Partiell schließen durch Drücken & Halten | - | 0/1 |
| So | Slightly Open | Bewegt das Fenster in die teilgeöffnete Position, wenn die aktuelle Position eine andere ist. | - | 0/1 |
| Wp | Weather protection | Fenster werden geschlossen und für die weitere Bedienung gesperrt, wenn Ein. Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Stops movement. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/fenster-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |
| No | Open windows | Anzahl der offenen Fenster | ∞ |
| Nc | Closed windows | Anzahl der geschlossenen Fenster | ∞ |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/fenster-zentral/

Alle ausgewählten Fenster Bausteine können gemeinsam gesteuert werden.

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise gefunden.

Quelle: https://www.loxone.com/dede/kb/fenster-zentral/

---

## ### Composite-Fensterkontakt

Fasst bis zu drei Fenstersensoren (geöffnet, gekippt, verriegelt) zusammen und bestimmt daraus den korrekten Zustandswert basierend auf den Sensor-Installationspositionen.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/composite-fensterkontakt/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Open | 0 = closed, 1 = open | 0 = geschlossen, 1 = offen | 0/1 |
| Tilt | 0 = closed, 1 = tilt | 0 = geschlossen, 1 = gekippt | 0/1 |
| Secured | 0 = not secured, 1 = secured | 0 = nicht verriegelt, 1 = verriegelt | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/composite-fensterkontakt/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| S | Status | 1 = geschlossen, 2 = gekippt, 3 = offen, 4 = geschlossen und nicht verriegelt, 5 = geschlossen und verriegelt, 0 = ein oder mehrere Sensoren offline | ∞ |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/composite-fensterkontakt/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Sensorpositionen | Legt die Installations-Position des Geöffnet- und Gekippt-Kontaktes am Fenster für das Composite-Signal fest. | — |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/composite-fensterkontakt/

"Der Baustein ist darauf ausgelegt, dass an jedem der Eingänge (Open) & (Tilt) nur ein Sensor verbunden ist."

Quelle: https://www.loxone.com/dede/kb/composite-fensterkontakt/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| O | `Q` | Ausgang | – | Digitaler Ausgang für vollständig geschlossenes Fenster | ∞ |

---

## ### Windmesser

Rechnet die Frequenz eines Windmessers in eine Windgeschwindigkeit um und gibt Durchschnittswerte und Alarmsignale aus.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/windmesser/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| F | Frequency | Frequenz | ∞ |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/windmesser/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|--------|-------------|
| Avg | Average wind speed | Durchschnittliche Windgeschwindigkeit | km/h | 0...∞ |
| G | 3 second average for gusts | 3 Sekunden Mittelwert für Böen | km/h | 0...∞ |
| AvgMax | Maximum wind speed in the averaging period | Maximale Windgeschwindigkeit in der Durchschnittszeit | km/h | 0...∞ |
| Wa | Wind alarm | Windalarm | - | 0/1 |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/windmesser/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|--------|-------------|--------------|
| Avgt | Averaging-time | Durchschnittszeit | min | 0...∞ | 10 |
| F | Factor | Umrechnungsfaktor Hz in km/h bzw m/s oder andere Einheiten laut Datenblatt | - | ∞ | 1 |
| W | Wind speed alarm | Warngeschwindigkeit | km/h | 1...∞ | 50 |

### Fallstricke

[BELEGT] https://www.loxone.com/dede/kb/windmesser/

"Beachten Sie bitte, dass nur digitale Eingänge mit Frequenzzähler Funktion geeignet sind."

"Ist der Windsensor an einen digitalen Eingang der Multi Extension Air angeschlossen, wird die Geschwindigkeit minütlich übertragen. Dadurch muss der Faktor zur Berechnung durch 60 dividiert werden!"

Quelle: https://www.loxone.com/dede/kb/windmesser/

---

## ### Fenster- und Türüberwachung

Zeigt den Status von Fenstern, Türen und Toren an. Unterstützt Loxone-Kontakte und konventionelle Kontakte, aggregiert Zustände und zeigt zuletzt ausgelösten Sensor.

### Eingänge

[BELEGT] https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Hpos | Handle position | Aktuelle Position des Griffs (1=geschlossen, 2=gekippt, 3=offen, 4=geschlossen und nicht gesichert, 5=geschlossen und gesichert, 0=unbekannt/offline) | 0...∞ |
| Dwco | Door/window contact open | Wird für Tür- oder Fensterkontakte verwendet, die das Öffnen erkennen. (0 = geschlossen, 1 = offen) Wird normalerweise invertiert verwendet. | 0/1 |
| Dwct | Door/window contact tilt | Wird für Tür- oder Fensterkontakte verwendet, die ein Kippen erkennen. (0 = geschlossen, 1 = gekippt) Wird normalerweise invertiert verwendet. | 0/1 |
| Dwcs | Door/window contact secured | Wird verwendet, um zu erkennen, ob Türen oder Fenster gesichert (verriegelt) sind. (0 = unverriegelt, 1 = verriegelt) | 0/1 |

### Ausgänge

[BELEGT] https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Open | Number of open windows or doors | Anzahl offene Fenster oder Türen | ∞ |
| Tilt | Number of tilted windows or doors | Anzahl gekippte Fenster oder Türen | ∞ |
| Closed | Number of closed windows or doors | Anzahl geschlossene Fenster oder Türen | ∞ |
| Offline | Number of offline sensors | Anzahl Sensoren offline | ∞ |
| Secured | Number of secured windows or doors | Anzahl verriegelter Fenster oder Türen | ∞ |
| Unlocked | Number of unlocked windows or doors | Anzahl nicht verriegelter Fenster oder Türen | ∞ |
| Txlt | Text last triggered | Name des zuletzt ausgelösten Sensors | - |
| Txu | Text unsecure | Name für geöffnete/gekippte/unversperrte Türen und Fenster oder verbundener Fenster- und Türüberwachung | - |
| API | API Connector | Intelligenter API basierter Verbinder zur Funktionsverknüpfung zwischen Geräten und Bausteinen | - |

### Parameter

[BELEGT] https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|-------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Behält den letzten Zustand nach Miniserver-Neustart. Speicherung beim Speichern, geplanten Neustart, vor Backup und einmal pro Stunde | 0/1 | 0 |

### Eigenschaften

[BELEGT] https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge | - |

### Fallstricke

[OFFEN] Keine dokumentierten Warnhinweise gefunden.

Quelle: https://www.loxone.com/dede/kb/fenster-tuer-ueberwachung/

---

## Zusammenfassung

Insgesamt 10 Bausteine erfolgreich katalogisiert. Alle Tabellen wurden wörtlich aus der offiziellen Loxone-Dokumentation übernommen.

**Erfasste Bausteine (10/10):**
1. Automatikbeschattung [BELEGT]
2. Automatikbeschattung Integriert [BELEGT]
3. Automatikbeschattung Zentral [BELEGT]
4. Dachfenster Beschattung [BELEGT]
5. EIB Beschattung [BELEGT]
6. Fenster [BELEGT]
7. Fenster Zentral [BELEGT]
8. Composite-Fensterkontakt [BELEGT]
9. Windmesser [BELEGT]
10. Fenster- und Türüberwachung [BELEGT]

**Besonderheiten:**
- Kürzel ϑ (Theta) wurde nicht gefunden; alle anderen Spezialzeichen korrekt übernommen
- Automatic shading blocks verwenden konsistent die Eingänge Sps/Spr/DisSp für Sonnenstandsautomatik
- Parameter Pi (Pitch) nur bei Dachfenster Beschattung für Dachneigungswinkel
- Zentral-Bausteine geben Anzahl (No/Nc) statt individueller Positionen aus
- Wind alarm Eingang (Wa) in 5 Bausteinen für Sturmschutz dokumentiert
- Composite-Fensterkontakt hat Eingang ohne Kürzel (nur "Open", "Tilt", "Secured")

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Jalousie (`JalousieUpDown2`)

Jalousiemotorsteuerung mit Zweitastenbedienung inklusive Komfortfunktionen

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Up | `InputTriggerUp` | Trigger Up | AUF-Eingang der Jalousie | – |
| Dw | `InputTriggerDown` | Trigger Down | AB-Eingang der Jalousie | – |
| Cu | `EndUp` | Complete up | Beschattung komplett AUF fahren | – |
| Cd | `EndDown` | Complete down | Beschattung komplett AB fahren | – |
| S | `Shade` | Shading | Beschattungseingang. Jalousie komplett AB fahren (laut Zeit Td) dann Rückfahrt (laut Zeit Tr) zum Geradestellen der Lamellen Bei Rolladen/Rollo/Markise Fahrt bis zum eingestellten Wert. | – |
| St | `Stop` | Stop | Stop-Eingang der Jalousie | – |
| AIp | `ManualPosition` | Position of blinds | Analoger Eingang Position der Jalousie in % | ∞ |
| AIl | `ManualLamelle` | Position of slats | Analoger Eingang Position der Lamelle in % | ∞ |
| Dis | `InputDisable` | Disable | Disable-Eingang der Jalousie (Kindersicherung) | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Q↑ | `OutputUp` | – | Digitaler Ausgang für Jalousie Auf | – |
| Q↓ | `OutputDown` | – | Digitaler Ausgang für Jalousie Ab | – |
| AQp | `OutputPos` | – | Position der Beschattung (0.0 = oben, 1.0 = unten) | 0.0…1.0 |
| AQl | `OutputLPos` | – | Position der Lamellen (0.0 = horizontal, 1.0 = vertikal) | 0.0…1.0 |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Tc | `MinPulse` | Minimum input pulse duration [s] for a complete motion | Minimale Dauer [s] des Eingangsimpulses (Up, Dw) zum Auslösen einer kompletten Auf- oder Abfahrt. Wenn Sie lieber Doppelklick verwenden möchten, dann setzen Sie hier einen sehr hohen Wert ein. | ∞ | 3 |
| Tu | `TimeEnd` | Duration [s] output pulse completely UP | Dauer [s] Ausgangsimpuls (Fahrzeit) bei kompletter AUF-Fahrt | ∞ | 75 |
| Td | `TimeEndDown` | Duration [s] output pulse completely DOWN | Dauer [s] Ausgangsimpuls (Fahrzeit) bei kompletter AB-Fahrt | ∞ | 70 |
| TI | `TimeBlock` | Time [s] motor lock | Dauer [s] der Motorverrieglung bei Richtungswechsel | ∞ | 0,5 |
| Tdc | `DblClk` | Double-click interval [s] | Doppelklickzeit [s] bei Eingangsimpuls (Up, Dw) zum Auslösen einer kompletten Auf- oder Abfahrt. Wenn Sie keinen Doppelklick verwenden möchten, dann setzen Sie hier 0 ein. | ∞ | 0,3 |
| Tr | `Back` | Duration [s] for return motion | Rückfahrzeit [s] für Beschattung (Geradestellen der Lamellen) bzw. Beschattungsposition [0.0-1.0] bei Rollladen/Rollo/Markise | ∞ | 0,8 |
| M | `MinMove` | Minimum travel time | Dauer [s] Ausgangsimpuls (Fahrzeit) bei kurzem Tastendruck | ∞ | 0,4 |
| T | `Type` | Type | Typ der Jalousie 0 = Jalousie/Raffstore 1 = Rollladen/Rollo/Dachrollo 2 = Vorhang beidseitig 3 = -nicht unterstützt- 4 = Vorhang links 5 = Vorhang rechts 6 = Markise | ∞ | 0 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 349

---
