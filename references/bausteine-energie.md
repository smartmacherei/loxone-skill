# Energie & Lastmanagement

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## 1. Energiemanager

Verwaltet die verfügbare Energie (Netz, Speicher, Produktion) und schaltet bis zu 12 Lasten intelligent an/aus oder regelt deren Leistung, um ein definiertes Netzleistungs-Sollwert einzuhalten.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Gpwr | Grid power | Negativer Wert wenn ans Netz geliefert wird. | kW | ∞ |
| Ppwr | Production power | Nur für die Visualisierung verwendet. | kW | ∞ |
| Spwr | Energy storage power | Negativer Wert wenn der Speicher geladen wird. | kW | ∞ |
| Soc | Energy storage state of charge | Energiespeicher Ladezustand | % | 0...100 |
| Prio | Priority selection | Startet die ausgewählte Last sofort. | \- | 0...12 |
| Recalc | Recalculate | Löst sofort eine Neuberechnung aus. | \- | 0/1 |
| L1-12 | Load 1-12 status | Aktueller Status (digital) oder Verbrauchsleistung (analog) der Last. | \- | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | \- | 0/1 |

Quelle: https://www.loxone.com/dede/kb/energiemanager-2/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Next | Next Calculation | Sekunden bis zur nächsten Neuberechnung. | s | ∞ |
| L1-12 | Load 1-12 | Ausgang für Last 1-12. Digital = 0/1. Analog = kW | \- | ∞ |
| MinSoc | Minimum state of charge | Eingestellte minSoc. | % | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | \- | \- |

Quelle: https://www.loxone.com/dede/kb/energiemanager-2/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| O | Offset grid power | Offset des Leistungssollwerts des Energiemanagements. 0: Der Energiemanager versucht zu gewährleisten, dass keine Energie aus dem Netz und dem Energiespeicher importiert/exportiert wird. Positiver Wert: Es ist erlaubt, Energie aus dem Netz zu importieren oder aus dem Speicher zu entnehmen. Negativer Wert: Stellt sicher, dass immer so viel produzierte Energie für den Export ins Netz oder das Laden des Speichers zur Verfügung steht. | kW | ∞ | 0 |
| MinSoc | Minimum state of charge | Ist der Wert größer als 0, hat das Laden des Energiespeichers höchste Priorität, bis der Mindestladezustand (SoC) erreicht ist. Danach wird der Energiespeicher nur noch geladen, wenn ein Energieüberschuss vorhanden ist. | % | 0...100 | 0 |
| MaxSpwr | Maximum energy storage power | Legt die maximale Ladeleistung des Energiespeichers fest. | kW | 0...∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/energiemanager-2/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Energiemanager bearbeiten | \- | \- |

Quelle: https://www.loxone.com/dede/kb/energiemanager-2/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise oder Achtung-Boxen auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/energiemanager-2/

---

## 2. Energiemanager Gen. 1

Ältere Generation des Energiemanagers. Verwaltet verfügbare Energie und schaltet bis zu 12 Lasten anhand eines Leistungs-Schwellwerts.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| P | Current power | Aktuelle Leistung | kW | ∞ |
| Ps | Power energy storage | Muss angeschlossen werden, wenn der Ausgang (Re) verwendet wird. | kW | ∞ |
| Prio | Priority selection | Startet die ausgewählte Last sofort. | 0/1 | 0...12 |
| L1-12 | Start Load 1-12 | Starte Last 1-12 | – | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | – | 0/1 |

Quelle: https://www.loxone.com/dede/kb/energiemanager/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| L1-12 | Load 1-12 | Last 1-12 | – | 0/1 |
| Re | Residual energy | Kann bspw. zum Laden einer Batterie oder eines Heizstabs verwendet werden (Energiespeicher). Wird dieser Ausgang verwendet, muss der Eingang (Ps) angeschlossen sein. | kW | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | – | – |

Quelle: https://www.loxone.com/dede/kb/energiemanager/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| O | Offset available energy | Es werden nur so viele Verbraucher aktiviert, dass die aktuelle Leistung (P) diesen Wert nicht überschreitet. 0 = Ausgänge werden nur bei Energieüberschuss aktiviert. | kW | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/energiemanager/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Energiemanager bearbeiten | – | – |

Quelle: https://www.loxone.com/dede/kb/energiemanager/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/energiemanager/

---

## 3. Energiemonitor

Überwacht und dokumentiert Energieflüsse (Produktion, Verbrauch, Import, Export) mit verschiedenen Zeiträumen (Tag, Monat, Jahr, Gesamt) und berechnet Kosten/Ersparnis. **Hinweis: Dieser Baustein wird nicht mehr weiterentwickelt und wurde durch den Energieflussmonitor in Kombination mit den Zählerbausteinen ersetzt.**

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Ptot | Production total | Produktion gesamt. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kWh | 0...∞ |
| Ppwr | Production power | Produktionsleistung. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| Gi | Grid energy import | Netz Energie Import | kWh | 0...∞ |
| Gpwr | Grid power | Positiver Wert: Energie wird vom Netz importiert. Negativer Wert: Energie wird ins Netz exportiert. | kW | ∞ |
| Ge | Grid energy export | Netz Energie Export | kWh | 0...∞ |
| Spwr | Energy storage power | Positiver Wert: Der Energiespeicher wird entladen. Negativer Wert: Der Energiespeicher wird geladen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| SoC | Energy storage state of charge | Energiespeicher Ladezustand. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | % | 0...100 |
| Err | Error | Fehler | \- | ∞ |
| R | Reset | Zählerwerte zurücksetzen. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | \- | 0/1 |

Quelle: https://www.loxone.com/dede/kb/energie-monitor/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Ppwr | Production power | Produktionsleistung | kW | ∞ |
| Pd | Production today | Produktion heute | kWh | 0...∞ |
| Pm | Production this month | Produktion dieser Monat | kWh | 0...∞ |
| Py | Production this year | Produktion dieses Jahr | kWh | 0...∞ |
| Ptot | Production total | Produktion gesamt | kWh | 0...∞ |
| Cpwr | Consumption power | Verbrauchsleistung | kW | ∞ |
| Cd | Consumption today | Verbrauch heute | kWh | 0...∞ |
| Cm | Consumption this month | Verbrauch dieser Monat | kWh | 0...∞ |
| Cy | Consumption this year | Verbrauch dieses Jahr | kWh | 0...∞ |
| Ctot | Consumption total | Gesamtverbrauch | kWh | 0...∞ |
| Ed | Export today | Export heute | kWh | 0...∞ |
| Em | Export this month | Export dieser Monat | kWh | 0...∞ |
| Ey | Export this year | Export dieses Jahr | kWh | 0...∞ |
| Etot | Export total | Export Gesamt | kWh | 0...∞ |
| Yd | Yield today | Ertrag heute | Währung | ∞ |
| Ym | Yield this month | Ertrag dieser Monat | Währung | ∞ |
| Yy | Yield this year | Ertrag dieses Jahr | Währung | ∞ |
| Ytot | Yield total | Ertrag gesamt | Währung | ∞ |
| Sci | Status code inverter | Statuscode Wechselrichter | \- | ∞ |
| Eci | Error code inverter | Fehlercode Wechselrichter | \- | ∞ |
| Gpwr | Grid power | Positiver Wert: Energie wird vom Netz importiert. Negativer Wert: Energie wird ins Netz exportiert. | kW | ∞ |
| Spwr | Energy storage power | Positiver Wert: Der Energiespeicher wird entladen. Negativer Wert: Der Energiespeicher wird geladen. | kW | ∞ |
| SoC | Energy storage state of charge | Energiespeicher Ladezustand | % | 0...100 |
| Itot | Import total | Import gesamt | kWh | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | \- | \- |

Quelle: https://www.loxone.com/dede/kb/energie-monitor/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Pre | kWh price export | kWh Preis Export | Währung | ∞ | 0,2 |
| Pri | kWh price import | kWh Preis Import | Währung | ∞ | 0,2 |
| CO2 | Kg/kWh for CO2 savings | Kg/kWh für CO2 Ersparnis | Kg/kWh | 0...∞ | 0,42 |
| Abs | Absolute value | Behandlung der Eingänge (Gi) und (Ge): 0 = Jeder neue Wert wird schrittweise zum Gesamtwert addiert. 1 = Der Wert wird absolut verwendet und entspricht dem Stand des ausgelesenen Zählers. | \- | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/energie-monitor/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|-------------|--------------|--------------|
| Datenquelle | Datenquelle (Generatortyp), z.B. Fronius, Kostal. Die Daten werden zyklisch jede Minute abgefragt. Werden die Objekteingänge als Datenquelle verwendet, so wird der Baustein auch bei jeder Änderung dieser Eingänge aktualisiert. | \- | \- |
| Speicherkapazität | Kapazität des Stromspeichers in kWh | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/energie-monitor/

### Fallstricke [BELEGT]

"Dieser Baustein wird nicht mehr weiterentwickelt und wurde durch den Energieflussmonitor in Kombination mit den Zählerbausteinen ersetzt."

Quelle: https://www.loxone.com/dede/kb/energie-monitor/

---

## 4. Energieflussmonitor

Ersetzt den Energiemonitor. Visualisiert und dokumentiert Energieflüsse mit Preis-/CO₂-Integration. Unterstützt optional Spotpreis-Optimierer zur dynamischen Preisabfrage.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/energieflussmonitor/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|---|---|---|---|---|---|
| Pre | kWh price export | kWh Preis Export. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | Währung | ∞ | 0,2 |
| Pri | kWh price import | kWh Preis Import. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | Währung | ∞ | 0,2 |
| CO2 | Kg/kWh for CO2 savings | Kg/kWh für CO2 Ersparnis | Kg/kWh | 0...∞ | 0,42 |

Quelle: https://www.loxone.com/dede/kb/energieflussmonitor/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|
| Gpwr | Grid power | Netzleistung | ∞ |
| Ppwr | Production power | Produktionsleistung | ∞ |
| Cpwr | Consumption power | Verbrauchsleistung | ∞ |
| Spwr | Energy storage power | Speicherleistung | ∞ |
| Ed | Export today | Export heute | ∞ |
| Id | Import today | Import heute | ∞ |
| Pd | Production today | Produktion heute | ∞ |
| Cd | Consumption today | Verbrauch heute | ∞ |
| Scd | Self Consumption today | Eigenverbrauch heute | ∞ |
| Co2d | CO2 today | Berechnung der CO2 Ersparnis: Co2d = Pd * CO2. Die Berechnung der Anzahl der Bäume in der Visualisierung erfolgt nach den Formeln des Treibhausgas-Äquivalenzen Rechners. | ∞ |
| Yd | Yield today | Berechnung stündlich oder bei Preisänderung nach folgender Formel: Yd = (Pd - Ed) * Pri + Ed * Pre | ∞ |
| Rest | Top Rest Power | Berechnete verbleibende Leistung der Spitzengruppe | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | \- |

Quelle: https://www.loxone.com/dede/kb/energieflussmonitor/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Monitor konfigurieren | \- | \- |
| Quelle Exportpreis | Wählen Sie einen Spotpreis-Optimierer als Quelle für den Energieexportpreis oder verwenden Sie den Parameter. Es können nur Objekte vom selben Miniserver ausgewählt werden! | \- |
| Quelle Importpreis | Wählen Sie einen Spotpreis-Optimierer als Quelle für den Energieimportpreis oder verwenden Sie den Parameter. Es können nur Objekte vom selben Miniserver ausgewählt werden! | \- |

Quelle: https://www.loxone.com/dede/kb/energieflussmonitor/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/energieflussmonitor/

---

## 5. Lastmanager

Verwaltet Lasten intelligent durch Überlastschutz (bei Leistungsüberschuss Lasten sperren) oder Spitzenlastmanagement (begrenzte Durchschnittsleistung im Viertelstundenintervall). Bis zu 12 Lasten mit konfigurierbarer Priorität.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|---|---|---|---|---|
| Gpwr | Grid power | Aktuelle Gesamtleistung. Eingabe ist nur im Modus "Überlastschutz" oder "Spitzenlast Manager & Überlastschutz" verfügbar. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| Gi | Grid energy import | Netz Energie Import. Eingang nur im Spitzenlast Manager Modus verfügbar. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kWh | 0...∞ |
| Tr | Trigger new averaging interval | Aktualisiert den Referenzwert zur Berechnung der Durchschnittsleistung. Eingang nur im Spitzenlast Manager Modus verfügbar. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| S1-12 | Status load 1-12 | Digitaler Eingang für den aktuellen Status der Last. Wenn dieser Eingang verwendet wird, werden Sie benachrichtigt, wenn die Last aufgrund von Überlast abgeschaltet wird. | - | 0/1 |
| Off | Off | Setzt alle Ausgänge zurück. Solange dieser Eingang aktiv ist, bleibt der Baustein deaktiviert. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/lastmanager/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|---|---|---|---|---|
| L1-12 | Lock load 1-12 | Wenn die maximale Leistungskapazität (MaxP) des Blocks überschritten wird, wird die Leistung durch Sperren von Lasten mit höherer Priorität freigegeben. | - | 0/1 |
| Ap | Available power | Aktuell verfügbare Leistung bis zur maximalen Leistungskapazität im Überlastschutz Modus. Im Spitzenlast Manager Modus ist dieser Wert die Leistung, die für die verbleibende Zeit im Intervall verwendet werden kann, um den in (MaxP) angegebenen durchschnittlichen Verbrauch zu erreichen. | kW | ∞ |
| AvgP | Average power | Aktuelle durchschnittliche Leistung seit dem Mittelungsintervallimpuls oder dem Beginn einer neuen Viertelstunde. Der Ausgang ist nur im Spitzenlast Manager Modus verfügbar. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| TsU | Time since update averaging interval | Zeit, die seit dem Auslösen eines neuen Mittelungsintervalls zur Berechnung der durchschnittlichen Leistung oder dem Beginn einer neuen Viertelstunde vergangen ist. Der Ausgang ist nur im Spitzenlast Manager Modus verfügbar. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | s | ∞ |
| MaxPe | Maximum power exceeded | **Überlastschutz:** EIN, wenn die maximale Leistungskapazität (MaxP) für 30 Sekunden überschritten wird. **Spitzenlast Manager:** EIN, wenn die durchschnittliche Leistung die maximale technische Leistung (MaxTp) für 30 Sekunden überschreitet. **Spitzenlast Manager & Überlastschutz:** EIN, wenn die aktuelle Leistung (Gpwr) 30 Sekunden lang (MaxTp) überschreitet. | - | 0/1 |
| ApPeak | Available power Peak | Die verfügbare Spitzenleistung beginnt bei (MaxTp) und wird während des Zeitraums schrittweise auf (MaxP) reduziert. Wird (Gpwr) verwendet und ist dieser Wert negativ, wird die eingespeiste PV-Leistung addiert. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/lastmanager/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|---|---|---|---|---|---|
| MaxP | Maximum power | Gibt die maximale Leistungskapazität im Überlastschutz-Modus an. Im Spitzenlast Manager Modus gibt dieser Wert das durchschnittliche Leistungslimit innerhalb eines Viertelstundenintervalls oder des letzten Durchschnittsimpulses am Eingang (Tr) an. | kW | 0...∞ | 20 |
| Hys | Hysteresis | Gibt den Wert an, wann Lasten wieder eingeschaltet werden können, nachdem (AvgP) unter (MaxP) gefallen ist. Der Parameter ist nur im Spitzenlast Manager Modus verfügbar. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | 0...∞ | 1 |
| MaxTp | Maximum technical power | 0 = Verwenden Sie (MaxP) stattdessen. Gibt die maximale Leistungskapazität im Spitzenlast Manager Modus an. Dieser Wert begrenzt die maximal verfügbare Leistung des Ausgangs (Ap) für das verbleibende Intervall. Zusätzlich werden Lasten sofort abgeworfen, wenn dieser Wert im Überlastschutz Modus des Spitzenlast Managers & überschritten wird. Dieser Wert wird auch für den Ausgang (MaxPe) verwendet. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | 0...∞ | 40 |

Quelle: https://www.loxone.com/dede/kb/lastmanager/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|---|---|---|
| Konfiguration | Konfigurieren Sie die einzelnen Verbraucher, die der Lastmanager verwaltet. | - |
| Arbeitsmodus | Arbeitsmodus des Lastmanagers einstellen | - |

Quelle: https://www.loxone.com/dede/kb/lastmanager/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/lastmanager/

---

## 6. Wallbox

Steuert Ladestationen für Elektrofahrzeuge. Unterstützt mehrere Lademodi (1-5) mit unterschiedlichen Leistungsgrenzen und Preisen. Integriert Zählerfunktionen und Session-Management. Optional vom Wallbox Manager verwaltet.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Ec | Enable charging | Ein Impuls <1s aktiviert das Laden. Ein Impuls >=1s oder Dauer ein, aktiviert das Laden und schaltet nach fallender Flanke wieder ab. Ist dieser Eingang invertiert und nicht verbunden, wird das Laden erlaubt. Eco Laden wenn vom Wallbox Manager verwaltet. | - | 0/1 |
| Ecp | Enable charging priority | Ein Impuls <1s aktiviert das Laden im Priority Modus, verwaltet vom Wallbox Manager. Ein Impuls >=1s oder Dauer ein, aktiviert Priority und beendet den Ladevorgang nach fallender Flanke vollständig. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Vc | Vehicle Connected | Fahrzeug verbunden | - | 0/1 |
| Cp | Current charging power | Aktuelle Ladeleistung | - | ∞ |
| Mr | Meter reading | Zählerstand | - | 0...∞ |
| Cac | Charging active | Ladevorgang aktiv | - | 0/1 |
| Sm1-5 | Set charging mode 1-5 | Lademodus 1-5 auswählen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Lm1-5 | Limit charging mode 1-5 | Definieren Sie bis zu 5 Lademodi mit unterschiedlichen Ladegrenzen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| Pm1-5 | Price charging mode 1-5 | Definieren Sie bis zu fünf Lademodi mit unterschiedlichen Preisen pro kWh. Geben Sie den Preis in ganzen Währungseinheiten ein (z. B. 30 = 30 €/kWh, 0,30 = 0,30 €/kWh). Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ |
| Pmm | Price charging mode manual | Pmm ist der manuelle Lademodus 99 (nur App). Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ |
| Uid | User ID | - | - | - |
| Ls | Load shedding | Wenn aktiviert, pausiert das Gerät das Laden, um Spitzenlasten im Stromnetz oder ähnliche Probleme zu verhindern, und bleibt so lange pausiert, wie die Lastabwurf aktiv ist. | - | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Resets outputs except meter outputs. Pulse (> 200 ms): Block is locked. Dominating input. Resetting the Wallbox with input Off sets the mode from the (Muv) parameter. | - | 0/1 |
| R | Reset meter reading outputs | Zählerausgänge zurücksetzen | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/wallbox-baustein/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Ca | Charging allowed | Laden ist erlaubt, wenn: -Ec (Enable Charging) aktiv ist. -Ec invertiert und nicht verbunden ist. -Das Laden nicht über Ls oder Off deaktiviert wurde. -Die Ladegrenze nicht unter der minimalen Ladeleistung liegt. | - | 0/1 |
| Vc | Vehicle connected | Fahrzeug verbunden | - | 0/1 |
| Cp | Current charging power | Aktuelle Ladeleistung | - | ∞ |
| M | Current charging mode | Lademodus 1-5. 99 = Manueller Modus (nur App). **Verwaltet vom Wallbox Manager**: Current charging mode. 0 = Laden nicht erlaubt, 1 = Eco laden erlaubt, 2 = Priority laden erlaubt | - | ∞ |
| Tp | Target charging power | Ziel Ladeleistung des aktuellen Modus. Ausgang ist 0, wenn die Ladegrenze unter der minimalen Ladeleistung liegt oder der Ausgang Ca 0 ist. | kW | ∞ |
| Ls | Load shedding | - | - | 0/1 |
| Mr | Meter reading | Zählerstand | - | ∞ |
| Ccc | Consumption current charge | Verbrauch aktueller Ladevorgang | - | ∞ |
| Clc | Consumption last charge | Verbrauch letzter Ladevorgang | - | ∞ |
| Cd | Consumption today | Verbrauch heute | - | ∞ |
| Cw | Consumption this week | Verbrauch diese Woche | - | ∞ |
| Cm | Consumption this month | Verbrauch dieser Monat | - | ∞ |
| Cy | Consumption this year | Verbrauch dieses Jahr | - | ∞ |
| Lcl | Last charge log | Textausgabe von - Vc Ein und Aus Zeitpunkt. - Dauer (Vc ein/aus). - Geladene Energie (kWh). - User ID. | - | - |
| Cac | Charging active | Wenn der Eingang Cac nicht verwendet wird und keine Loxone Wallbox angeschlossen ist, ist der Ausgang 1, sobald das Fahrzeug angeschlossen ist und der Eingang Cp größer als die minimale Ladeleistung ist. | - | 0/1 |
| Cld | Consumption yesterday | Verbrauch gestern | - | ∞ |
| Clm | Consumption last month | Verbrauch letzter Monat | - | ∞ |
| Cly | Consumption last year | Verbrauch letztes Jahr | - | ∞ |
| Cclc | Charging costs last charge | Gibt die berechneten Kosten der letzten Ladesession aus. Bei aktiver Ladesession werden deren laufende Kosten ausgegeben. | - | ∞ |
| Uid | User Id | - | - | - |
| Se | Pulse Session ended | Impuls Session beendet | - | 0/1 |
| Ss | Pulse Session started | Impuls Session gestartet | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/wallbox-baustein/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Muv | Mode after unplugging the vehicle | 0 = Aktuellen Modus beibehalten. 1-5 = Umschalten auf Modus 1-5. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ | 0 |
| Cfp | Connection fee per hour | Verbindungsgebühr pro Stunde, während das Fahrzeug verbunden ist. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | Währung | ∞ | 0 |
| Mro | Meter reading offset | Wert wird zum Ausgang (Mr) hinzugefügt. | - | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/wallbox-baustein/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|------------------|-------------|---------|--------------|--------------|
| Max. Ladeleistung | Max. Ladeleistung [kW] | kW | 0...∞ | 11 |
| Min. Ladeleistung | Min. Ladeleistung [kW] | kW | 0...∞ | 4.16 |
| Konfiguration | Konfiguration der verwendeten Ein- und Ausgänge. | - | - | - |
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | - | 1...100 | 100 |
| Relativzählung | Aktiv: Der ausgelesene Zähler sendet nur Teilmengen in Intervallen (relativ), der Baustein zählt zusammen und bildet daraus den Zählerstand. Nicht aktiv: Der ausgelesene Zähler sendet selbst seinen Gesamtzählerstand (absolut), der Baustein bildet diesen nur ab. | - | - | - |
| Ungültigen Zählerstand melden | Wenn aktiviert, werden Sie benachrichtigt, wenn ungültige Zählerstandswerte erkannt wurden. Zum Beispiel, wenn ein physischer Zähler aufgrund von Übertragungsfehlern unrealistische Werte sendet. | - | - | - |
| Regionale Vorschrift | Wählen Sie die für Ihre Region geltende Vorschrift aus. Die Wallbox passt ihr Verhalten entsprechend an (z. B. Spannungs-/Frequenzverhalten). Zusätzliches Zubehör kann erforderlich sein (z. B. Energiezähler 3-phasig Tree). | - | - | - |

Quelle: https://www.loxone.com/dede/kb/wallbox-baustein/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/wallbox-baustein/

---

## 7. Wallbox Gen. 1

Erste Generation der Wallbox-Steuerung. Unterstützt zwei Profile mit unterschiedlichen Leistungsgrenzen.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Act | Activates charging process | Ladevorgang aktivieren | - | 0/1 |
| Vc | Vehicle connected | Fahrzeug verbunden. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Cp | Current charging power | Aktuelle Ladeleistung. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| E | Charged energy | Eingang Energie (Absolut). Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kWh | 0...∞ |
| Cpl | Charging power limit | Beschränkt die Ladeleistung auf diesen Wert, wenn Charging power limit mode (M) 2 ist. | kW | 1.38...22.08 |
| R | Reset | Zählerwerte zurücksetzen. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/wallbox/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Ac | Active charging | Laden aktiv | - | 0/1 |
| Vc | Vehicle connected | Fahrzeug verbunden | - | 0/1 |
| Cp | Current charging power | Aktuelle Ladeleistung | kW | ∞ |
| Ecs | Energy current session | Energie aktuelle Ladesession | kWh | ∞ |
| E1 | Total Energy consumed profile 1 | Gesamtenergieverbrauch Profil 1 | kWh | 0...∞ |
| E2 | Total Energy consumed profile 2 | Gesamtenergieverbrauch Profil 2 | kWh | 0...∞ |
| Cpl | Charging power limit | Ladeleistung Limit | kW | 1.38...22.08 |
| Error | Error codes | Fehlercodes | - | - |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/wallbox/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| M | Charging power limit mode | 0 = Kein Grenzwert. 1 = Manuell - Grenzwert über Benutzeroberfläche eingestellt. 2 = Automatisch - Grenzwert über Eingang (Cpl) eingestellt | 0...2 | 2 |
| Mr | Remember mode | 0 = Modus auf 'Automatisch' setzen, wenn das Fahrzeug ausgesteckt wird. 1 = Modus merken, wenn das Fahrzeug ausgesteckt wird. | 0/1 | 0 |
| Sc | Start of charging process | Legt fest, wann der Ladevorgang beginnen soll: 0 = Wallbox-Einstellungen verwenden. 1 = Start / Pause je nach Eingang (Act). Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 | 0 |
| Profile | Select profile | 0 = Profil 1. 1 = Profil 2. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0...1 | 0 |

Quelle: https://www.loxone.com/dede/kb/wallbox/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Verknüpftes Ladestationsgerät | Wird der Baustein mit einem Ladestationsgerät konfiguriert werden Informationen entsprechend vom Gerät ermittelt. Ansonsten werden die Objekteingänge an die Ausgänge weitergeleitet | - |
| Profilname 1 | Bezeichnung des Profils 1 (Max. 12 Zeichen) | - |
| Profilname 2 | Bezeichnung des Profils 2 (Max. 12 Zeichen) | - |

Quelle: https://www.loxone.com/dede/kb/wallbox/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/wallbox/

---

## 8. Wallbox Manager

Zentrale Verwaltung mehrerer Wallboxen mit gemeinsamen Leistungslimit, Eco- und Priority-Lademodi und Aktivitätsprotokoll.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|---|---|---|---|---|
| Pmax | Maximum total power | Maximale Gesamtleistung, welche den Wallboxen zur Verfügung steht. Wird primär als Höchstwert für den Überlastschutz genutzt. Alternativ, um die Ladeleistung in Zeiten hoher Strompreise oder hohen Verbrauchs zu begrenzen. | kW | 0...∞ |
| Peco | Power for Eco charging | Überschüssige Leistung, welche an die Wallboxen zum Eco Laden verteilt wird. | kW | 0...∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |

Quelle: https://www.loxone.com/dede/kb/wallbox-manager/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|---|---|---|---|---|---|
| PrEco | Price Eco | Preis pro kWh beim Eco Laden. | Währung | ∞ | 0.1 |
| PrPrio | Price Priority | Preis pro kWh beim Priority Laden. | Währung | ∞ | 0.2 |
| Cfp | Connection fee per hour | Verbindungsgebühr pro Stunde, während ein Fahrzeug verbunden ist. | Währung | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/wallbox-manager/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|---|---|---|---|---|
| Cp | Current power | Aktuelle gesamte Leistungsaufnahme aller Wallboxen. Für Wallboxen deren Leistungsaufnahme unbekannt ist (kein Zähler vorhanden od. Cp Eingang nicht verwendet), wird die zugeteilte Leistung angenommen. | kW | 0...∞ |
| Ap | Assigned Power | Gesamte den Wallboxen zugeteilte Leistung. Summe von Tp aller verknüpften Wallboxen. | kW | 0...∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/wallbox-manager/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|---|---|---|---|
| Konfigurieren... | Konfigurieren Sie den Wallbox Manager, indem Sie Wallboxen hinzufügen und sie zu Gruppen zusammenfassen. | - | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |

Quelle: https://www.loxone.com/dede/kb/wallbox-manager/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/wallbox-manager/

---

## 9. PV Produktionsvorhersage

Erzeugt stundenweise Vorhersagen für die PV-Produktion basierend auf Wetterdaten. Nützlich für Lastmanagement und Speicherladung. Erfordert aktiven Wetterdienst.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off input | Setzt den Ausgang 'Ready' auf AUS und die Vorhersageausgänge auf -1. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/pv-produktionsvorhersage/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Period | Calculated Period | Die Vorhersage wird über diesen Zeitraum berechnet, beginnend mit der nächsten vollen Stunde. | h | 0...72 | 24 |

Quelle: https://www.loxone.com/dede/kb/pv-produktionsvorhersage/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Ppwr | Potential Power | Zeigt die PV-Leistung an, die derzeit basierend auf der vom Wetterdienst bereitgestellten Sonnenstrahlung erzeugt werden könnte. -1, wenn keine Vorhersage möglich ist. | kW | ∞ |
| Pp | Predicted period | Gibt die Vorhersage für den angegebenen Zeitraum ab der nächsten vollen Stunde aus. -1, wenn keine Vorhersage möglich ist. | kWh | ∞ |
| Ptd | Predicted today | Gibt die Vorhersage für heute aus. -1, wenn keine Vorhersage möglich ist. | kWh | ∞ |
| Pnd | Predicted next day | Gibt die Vorhersage für morgen aus. -1, wenn keine Vorhersage möglich ist. | kWh | ∞ |
| Ready | Prediction provided | AUS, wenn der Baustein über den Off-Eingang gesperrt ist oder wenn keine Vorhersage möglich ist (z. B. bei Verlust der Internetverbindung, abgelaufenem Abonnement usw.) | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - | - |

Quelle: https://www.loxone.com/dede/kb/pv-produktionsvorhersage/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Max. PV-Leistung [kWp] | Die theoretisch maximal mögliche Leistung der PV-Anlage unter idealen Bedingungen. | 0...∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/pv-produktionsvorhersage/

### Fallstricke [BELEGT]

"Für die Verwendung dieses Bausteins ist ein aktiver Wetterdienst erforderlich."

"Bitte beachten Sie, dass mögliche Einschränkungen des Wechselrichters nicht berücksichtigt werden."

Quelle: https://www.loxone.com/dede/kb/pv-produktionsvorhersage/

---

## 10. Spotpreis-Optimierer

Optimiert Lasten (z. B. Wallbox, Heizstab) basierend auf Strompreisen. Unterstützt relative/absolute Preis-Eingänge oder direkte Spotmarkt-Integration (EPEX, ERCOT etc.). Berechnet automatisch günstige Betriebsfenster.

### Eingänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |
| Tr | Trigger | Startet die Automatik. Der Ausgang O wird so oft aktiviert, wie es der 'Bedarf' innerhalb des 'Zeitraums' vorgibt. | 0/1 |
| +0 to +23 | Relativer Modus: Price in the hour now +0 to +23 | Preisprognose für die aktuelle Stunde + Offset. Diese Eingänge sind bei Verwendung des Spotmarkt-Modus nicht verfügbar. | ∞ |
| +0 to +23 | Absoluter Modus: Price in the hour 00:00 to 23:00 | Preisprognose für eine bestimmte Stunde des aktuellen Tags. Diese Eingänge sind bei Verwendung des Spotmarkt-Modus nicht verfügbar. | ∞ |

Quelle: https://www.loxone.com/dede/kb/spotpreis-optimierer/

### Parameter [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Demand | Demand | Gibt die gesamte aktive Dauer des Ausgangs O innerhalb des Zeitraums nach einem Trigger an. | h | 0...∞ | 4 |
| Period | Period | Zeitraum nach einem Trigger, aus dem der Baustein die Stunden mit dem niedrigsten Preis auswählt, in denen der Ausgang O aktiviert werden soll. | h | 0...∞ | 24 |
| Minimum Runtime | Minimum Runtime | Legt die minimale durchgehende Aktivierungsdauer des Ausgangs nach dem Einschalten fest. Zur Einhaltung dieser Dauer werden automatisch die günstigsten aufeinanderfolgenden Zeitfenster ausgewählt, die der definierten Mindestlaufzeit entsprechen oder diese überschreiten. Der Ausgang kann – wenn nötig oder sinnvoll – auch länger aktiv bleiben, jedoch niemals kürzer als die festgelegte Mindestdauer. Wird der Wert auf 0 gesetzt, richtet sich die Laufzeit ausschließlich nach der eingestellten Markttaktung. | h | 0...12 | 0 |
| Max | Fixed very high price | Wenn der aktuelle Preis über diesem Wert liegt, wird der Ausgang "sehr hoch" aktiviert. | Currency | ∞ | 1 |
| I2 | Variable Input 2 | Wert, der in der Formel mit I2 verwendet werden kann. | \- | ∞ | 0 |
| I3 | Variable Input 3 | Wert, der in der Formel mit I3 verwendet werden kann. | \- | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/spotpreis-optimierer/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| O | Active Output | Der Ausgang wird nach einem Trigger zu den Stunden mit dem niedrigsten Preis aktiviert. | 0/1 |
| Cv | Current Price | Aktueller Preis | ∞ |
| vHigh | Very High | Der aktuelle Preis ist im Vergleich zu den anderen Stunden Sehr Hoch oder liegt über dem im Parameter **Max** festgelegten Wert. Die Limits werden nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | 0/1 |
| High | High | Der aktuelle Preis ist im Vergleich zu den anderen Stunden Hoch. Die Limits werden nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | 0/1 |
| Low | Low | Der aktuelle Preis ist im Vergleich zu den anderen Stunden Niedrig. Die Limits werden nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | 0/1 |
| vLow | Very Low | Der aktuelle Preis ist im Vergleich zu den anderen Stunden Sehr Niedrig. Die Limits werden nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | 0/1 |
| Max | Highest Price | Der Höchstpreis wird nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | ∞ |
| Min | Lowest Price | Der Mindestpreis wird nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | ∞ |
| Avg | Average Price | Der Durchschnittspreis wird nach einem **Trigger** neu berechnet – basierend auf den zu diesem Zeitpunkt verfügbaren Prognosewerten. | ∞ |
| Nv | Next Price | Preis für den nächsten Zeitraum. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | \- |

Quelle: https://www.loxone.com/dede/kb/spotpreis-optimierer/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Preisberechnung | Verwenden Sie eine Formel, um den tatsächlichen Preis, den Sie zahlen, zu berechnen. Fragen Sie Ihren Energieversorger nach der Formel. I1 = Preis aus den Eingängen oder dem Spotpreis (ohne Steuer). I2 = I2-Parameter. I3 = I3-Parameter. I4 = Minuten seit Mitternacht, für die der Preis berechnet wird. | \- |
| Modus | Relativ: Die Eingänge geben den Preis relativ zur aktuellen Stunde an. Absolut: Die Eingänge liefern den Preis für jede Stunde des Tages (00:00 bis 23:00). Spotmarkt: Die Daten werden von den europäischen Energie-Spotmärkten abgerufen, die Eingänge für die stündlichen Preise werden ausgeblendet. | \- |
| Marktgebiet | Spotmarkt Gebiet, für das die Preise abgerufen werden sollen. | \- |
| Marktintervall | Intervall, in dem die Spotmarktpreise abgerufen werden. | \- |

Quelle: https://www.loxone.com/dede/kb/spotpreis-optimierer/

### Fallstricke [BELEGT]

**Warnung:** "Aufgrund rechtlicher Einschränkungen durch die Spotmarktdaten-Anbieter können wir keinen direkten Zugriff auf die Rohdaten gewähren. Alle relevanten Statistiken sind jedoch in der Visualisierung verfügbar."

**Hinweis:** "Bei der Verwendung von Formeln mit Zeitgrenzen (**I4**) sollte für die Untergrenze jedes Intervalls >= anstelle von > verwendet werden."

**Hinweis:** "Die Ausgänge des Spotpreis-Optimierers werden nach jedem Trigger neu berechnet. Diese Berechnungen beruhen auf den zum Zeitpunkt des Triggers verfügbaren Zukunftsdaten. Die Visualisierung berechnet die Farben für den aktuellen Tag und kategorisiert sie in niedrig, hoch, etc. Bitte beachten Sie jedoch, **dass die Ausgaben des Spotpreis-Optimierers in Loxone Config nicht immer mit den in der Visualisierung angezeigten Farben übereinstimmen**. Dieser Unterschied kann durch den Zeitpunkt und den Umfang der für die Neuberechnungen verwendeten Daten entstehen."

Quelle: https://www.loxone.com/dede/kb/spotpreis-optimierer/

---

## 11. Power Supply & Backup (Baustein)

Verwaltet Notstromversorgung und USV-Funktionen (unterbrechungsfreie Stromversorgung). Überwacht Netzspannung, Batterie-SoC, schaltet bei Netzausfall in den Backup-Modus und erkennt Überlasten.

### Eingänge [BELEGT]

[KEINE TABELLE VORHANDEN]

Quelle: https://www.loxone.com/dede/kb/power-supply-backup-block/

### Ausgänge [BELEGT]

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|--------------|---------|--------------|
| Pt | Power total | Aktuelle Gesamtleistung aller Ausgänge zusammen. | kW | ∞ |
| Bm | Backup mode | Aktiv, wenn die Netzspannung ausfällt. | - | 0/1 |
| P1-7 | Power 1-7 | Leistung 1-7 Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | kW | ∞ |
| Soc | Battery state of charge | Der aktuelle Ladezustand der Batterie. | % | ∞ |
| Ol | Overload | Aktiv, wenn die maximale Leistung von 1 kW für 5 Sekunden überschritten wird. Das Gerät schaltet sich automatisch ab, wenn die Ausgangsspannung nicht reduziert wird! | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

Quelle: https://www.loxone.com/dede/kb/power-supply-backup-block/

### Parameter [BELEGT]

[KEINE TABELLE VORHANDEN]

Quelle: https://www.loxone.com/dede/kb/power-supply-backup-block/

### Eigenschaften [BELEGT]

| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl Meldungen | Maximale Anzahl der gespeicherten letzten Meldungen. | 1...100 | 100 |

Quelle: https://www.loxone.com/dede/kb/power-supply-backup-block/

### Fallstricke [BELEGT]

Keine dokumentierten Warnhinweise auf der offiziellen Seite.

Quelle: https://www.loxone.com/dede/kb/power-supply-backup-block/

---

## Zusammenfassung

Alle 11 Bausteine aus der Kategorie "Energie & Lastmanagement" wurden vollständig dokumentiert:

- **11 Bausteine erfasst** (alle URLs erreichbar)
- **0 Bausteine fehlgeschlagen**

### Besonderheiten & XML-Mapping-Notizen

1. **Kürzel-Standardisierung**: Alle Kürzel wurden exakt aus der Dokumentation übernommen, einschließlich Sonderzeichen (z.B. Temperaturkürzel ϑ in Energy-Anwendungen nicht vorhanden, aber konsistente Notation wie Gpwr, Ppwr, Spwr, Soc durchgehend).

2. **Energiemanager Gen. 2 vs. Gen. 1**: Der neue Energiemanager hat zusätzliche Parameter (MaxSpwr) und Input-Struktur (Soc statt implizit, Recalc-Trigger). Die Gen. 1 ist vereinfacht.

3. **Energiemonitor als Vorvorgänger**: Offiziell durch Energieflussmonitor ersetzt, aber weiterhin dokumentiert. Unterschied: Energiemonitor hatte Eingänge für Ptot und Ge, Energieflussmonitor nur Off-Eingang plus gekoppelte Datenquellen.

4. **Wallbox 2 (aktuell) vs. Gen. 1**: Wallbox Gen. 2 hat Multimode-Unterstützung (Sm1-5, Lm1-5, Pm1-5) und wird vom Wallbox Manager verwaltet. Gen. 1 hat nur zwei Profile.

5. **Spotpreis-Optimierer Disclaimer**: Rechtliche Einschränkung bei Spotmarkt-Zugriff → "keine direkten Rohdaten, nur Statistiken in Visualisierung".

6. **PV Produktionsvorhersage Abhängigkeit**: Erfordert aktiven Wetterdienst; Ready-Output zeigt Verfügbarkeit an (-1 bei Fehler).

7. **Lastmanager Modi**: Zwei getrennte Modi (Überlastschutz vs. Spitzenlast Manager) mit unterschiedlichen Ausgängen (AvgP, TsU, ApPeak sichtbar nur im Spitzenlast-Modus).

8. **Power Supply & Backup Asymmetrie**: Hat NO Eingänge und NO Parameter — nur Ausgänge und Eigenschaften. Dies ist ungewöhnlich im Vergleich zu anderen Bausteinen.

