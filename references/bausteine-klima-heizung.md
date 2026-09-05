# Klima, Heizung & Regler
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

### 1. Intelligente Raumregelung

**Kurzbeschreibung:**
Steuert Heiz-, Kühl- und Lüftungsfunktionen auf Raumbasis. Unterstützt automatische Schaltung nach Zeitplan, manuelle Sollwertsvorgabe, Eco-, Komfort- und Gebäudeschutzmodi. Koordiniert mehrere Heiz-/Kühlquellen mit Priorisierung und PWM-Ausgängen.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| Mode | Mode | -1 = ausgeschaltet; 0 = Automatik Heizen/Kühlen; 1 = nur Heizen; 2 = nur Kühlen; 3 = fixer Sollwert Heizen/Kühlen; 4 = fixer Sollwert nur Heizen; 5 = fiker Sollwert nur Kühlen | - |
| ϑt | Target temperature | Zieltemperatur im Modus Fixer Sollwert | ° |
| ϑc | Current room temperature | Aktuelle Raumtemperatur | ° |
| Dwc | Door / window contact | 0 = closed, 1 = open | - |
| C | Comfort | Startet Komfort bei Ein (steigende Flanke) | - |
| E | Eco | Startet Eco bei Ein (steigende Flanke) | - |
| Bp | Building protection | Startet Gebäudeschutz bei Ein (steigende Flanke) | - |
| P | Presence | Verlängert Komfort, wenn Ein | - |
| Off | Off / Lock | Pulse < 200ms: Timer abbrechen; > 200ms: sperren; > 500ms: Sensor-Name verwenden | - |
| DisP | Disable presence | Deaktiviert Eingang (P), wenn 1 | - |
| ϑo | Outdoor temperature | Außentemperatur (für Eingang Dwc) | ° |
| CO2 | CO2 | Aktueller CO2-Gehalt | ppm |
| H | Humidity | Relative Luftfeuchtigkeit | % |
| Fan | Fan speed 0-7 | 0 = Aus, 1 = Auto, 2-7 = verschiedene Lüftergeschwindigkeiten | - |
| ADir | Airflow direction 1-8 | 1 = Auto, 2-6 = Positionen, 7 = Pendeln, 8 = kein Pendeln | - |
| Rtd | Reset to default | Setzt Parameter auf Standardwerte laut Bausteinvorlage | - |

Quelle: https://www.loxone.com/dede/kb/intelligente-raumregelung/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| H | Heating | Ausgang für reine Heizventile/-aktoren | 0...10 |
| C | Cooling | Ausgang für reine Kühlventile/-aktoren | 0...10 |
| HC | Heating/Cooling | Ausgang für kombinierte Heiz-/Kühlventile/-aktoren | 0...10 |
| H1-3 | Heating source 1-3 | Quellenausgänge für Heiz-Ventile, nur bei bestimmten Konfigurationen sichtbar | 0...10 |
| C1-3 | Cooling source 1-3 | Quellenausgänge für Kühl-Ventile, nur bei bestimmten Konfigurationen sichtbar | 0...10 |
| HC1-3 | Heating/Cooling source 1-3 | Quellenausgänge für kombinierte Ventile, nur bei bestimmten Konfigurationen sichtbar | 0...10 |
| Shd | Shading demand | Beschattungsanforderung zur Heiz-/Kühlunterstützung (0/1) | 0/1 |
| HCm | Heating / Cooling mode | Aktueller Modus: 1 = Heizen, -1 = Kühlen, 0 = aus | - |
| Error | Error | Fehler vorhanden (Temperatur außerhalb Frost/Hitzeschutz oder >1,5°C Abweichung nach Aufheiz/Abkühlphase) | 0/1 |
| TxErr | Error text | Fehlerbeschreibung | - |
| ϑt | Target temperature | Zieltemperatur | ° |
| Om | Current operating mode | Aktuelle Betriebsmodus-ID der Schaltuhr | - |
| Boost | Boost | Boost aktiv (während Vorbereitung oder >1,5°C Abweichung) | 0/1 |
| Os | Current temperature mode | Aktueller Temperaturmodus (-1 = Aus, 0 = Eco, 1 = Komfort, 2 = Gebäudeschutz, 3 = Manuelle Solltemperatur, 4 = Manuelle Kalendertemperatur) | - |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/intelligente-raumregelung/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| ϑch | Temperature comfort heating | Absolute Komforttemperatur im Heizbetrieb | ° | 22,5 |
| ϑcc | Temperature comfort cooling | Absolute Komforttemperatur im Kühlbetrieb | ° | 24,5 |
| ϑchc | Temperature comfort heating and cooling | Absolute Komforttemperatur für Heizen und Kühlen | ° | 22 |
| ϑd | Allowed Deviation | Erlaubte Abweichung Soll-/Isttemperatur im Komfortbetrieb | ° | 1,5 |
| ϑeh | Temperature eco heating | Temperatur Eco Heizen (relativ zu ϑch) | ° | 3 |
| ϑec | Temperature eco cooling | Temperatur Eco Kühlen (relativ zu ϑcc) | ° | 3 |
| ϑe | Allowed Deviation eco mode | Temperatur Eco Heizen und Kühlen relativ zur Komforttemperatur | ° | 2 |
| ϑsh | Temperature shading heating | Temperatur ab welcher Beschattung im Heizbetrieb aktiviert wird | ° | 27,5 |
| ϑsc | Temperature shading cooling | Temperatur ab welcher Beschattung im Kühlbetrieb aktiviert wird | ° | 23,5 |
| ϑfp | Temperature frost protection | Absolute Frostschutztemperatur (mind. 3° tiefer als ϑch) | ° | 5 |
| ϑhp | Temperature heat protection | Absolute Hitzeschutztemperatur (mind. 3° höher als ϑcc) | ° | 28 |
| Vs | Valve standstill | Maximaler Ventil-Stillstand in Tagen; 0 = deaktiviert | d | 14 |
| Cet | Comfort extend time | Komforttemperatur-Verlängerung nach Aus-Flanke von (C) | s | 3600 |
| EBpet | Eco / Building protection extend time | Eco-/Gebäudeschutz-Verlängerung nach Aus-Flanke | s | 3600 |
| Pet | Presence extend time | Komforttemperatur-Verlängerung nach Aus-Flanke von (P) | s | 1800 |
| Hs | Heating up speed | Zeit pro 1°C Temperaturerhöhung (falls 0: von Raumregler gelernt) | min/°C | 120 |
| Cs | Cooling down speed | Zeit pro 1°C Temperaturerniedrigung (falls 0: von Raumregler gelernt) | min/°C | 60 |
| Pwm | PWM interval | Zeitdauer Ein-Ausschaltzyklus PWM-Ausgang; 0 = automatisch (10-60 min) | min | 0 |
| Ddwc | Delay door/window contact | Verzögerung Gebäudeschutz-Aktivierung nach Fenster-/Türöffnung | s | 300 |
| ϑExc | Temperature offset Excess Heating/Cooling | Sollwert-Anpassung bei signalisiertem Heiz-/Kühl-Überschuss | ° | 1 |

Quelle: https://www.loxone.com/dede/kb/intelligente-raumregelung/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Default |
|-------------|--------------|---------|
| Quellen konfigurieren | Verfügbare Heiz-/Kühlquellen anlegen, priorisieren, Heiz-/Kühl-/PWM-Unterstützung konfigurieren | - |
| Schaltzeiten | Temperaturverwaltung im Heiz- und Kühlbetrieb | - |
| Eine Komforttemperatur verwenden | Single Comfort Temp statt getrennter Heiz-/Kühl-Temps | - |
| Überheizen zulassen | Zieltemperatur anpassen bei Heiz-Überschussmeldung | - |
| Überkühlen zulassen | Zieltemperatur anpassen bei Kühl-Überschussmeldung | - |
| Alle Quellen gleichzeitig nutzen | Heiz-/Kühlanforderung an alle verknüpften Bausteine oder nur an beste verfügbare Quelle | - |
| PWM Ausgänge | Ausgänge H, C, HC als PWM-Ausgang nutzen | - |
| Temperatur überwachen | Benachrichtigung bei großem Unterschied Raum-/Solltemperatur | - |
| Anzahl Aktivitätseinträge | Einträge im Aktivitätsprotokoll (0 = deaktiviert) | 20 |

Quelle: https://www.loxone.com/dede/kb/intelligente-raumregelung/

**Fallstricke:** [BELEGT]
- Manche Standardwerte sind unterschiedlich, da sie vom eingestellten Raumtyp abhängen.

---

### 2. Heiz- und Kühlsteuerung

**Kurzbeschreibung:**
Steuert die Heiz- und Kühlanlage (Wärmepumpe, Öl-/Gas-/Elektrisches System). Koordiniert Sollwert-Anforderungen der Intelligenten Raumregler mit Betriebsmodi, Stufenschaltung, Filterwechsel-Management und Ventil-Umschaltung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| ϑo | Outdoor Temperature | Außentemperatur (Systemvariable "Außentemperatur" falls nicht verbunden; -1000 wenn nicht verfügbar) | ° |
| B | Boost | Aktiviert Stufe 2 sofort; zeigt Sensor-Name in Visualisierung | - |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre; > 500ms: Sensor-Name verwenden (dominierend) | - |
| Ah | Additional heating | Aktiviert Zusatzheiz-Ausgang (Ah) wenn 1 | - |
| F | Fan | Aktiviert Ventilator-Ausgang (F) wenn 1 | - |
| Cfc | Confirm filter change | Filterwechsel bestätigen | - |
| Ec | Excess cooling | Überschüssige/günstige Kühlenergie vorhanden (für Intelligente Raumregler) | - |
| Eh | Excess heating | Überschüssige/günstige Heizenergie vorhanden (für Intelligente Raumregler) | - |
| Mh | Manual heating | Aktiviert manuellen Heizbetrieb (ignoriert Raumregler-Anforderungen); Heizung bleibt bis Mindestlaufzeit (MinHr) aktiv | - |

Quelle: https://www.loxone.com/dede/kb/klima-controller/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| H | Heating | Heizen (Stufe 1) | 0/1 |
| H2 | Heating stage 2 | Heizen Stufe 2 (nach Verzögerung Tt2s oder sofort bei Wärmepumpe wenn ϑo < ϑminS2) | 0/1 |
| C | Cooling | Kühlen (Stufe 1) | 0/1 |
| C2 | Cooling stage 2 | Kühlen Stufe 2 (nach Verzögerung Tt2s) | 0/1 |
| Ah | Additional heating | Zusatzheizung | 0/1 |
| Sv | Switching valve | Umschaltventil (0 = Heizen, 1 = Kühlen); nur bei bestimmten Konfigurationen sichtbar | 0/1 |
| F | Fan | Ventilator (Kühlung: sofort nach Aktivierung + Ventilposition; Heizung: nur bei Wärmepumpen 15s nach Heiz-Aktivierung) | 0/1 |
| Fc | Filter change | Filterwechsel fällig (1 wenn Dfc abgelaufen) | 0/1 |
| ϑoa | Average outdoor temperature | Durchschnittliche Außentemperatur der letzten 48h (verfügbar nach 24h; vorher -1000) | ∞ |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/klima-controller/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Mode | Mode | -1 = ausgeschaltet; 0 = Automatischer Modus-Wechsel; 1 = nur Heizen; 2 = nur Kühlen | - | -2 |
| MinHr | Time minimum HVAC Runtime | Mindestlaufzeit vor Modus-Wechsel oder Standby | min | 0 |
| Sot | Switch on threshold | Durchschn. Ventilöffnung Raumregler muss diesen Wert überschreiten zum Starten | % | 30 |
| Vd | Valve delay | Zeit für Umschaltventil-Bewegung (nur bei bestimmten Konfigurationen) | s | 0 |
| Fod | Fan Overrun Duration | Nachlaufzeit Ventilator nach Heizen/Kühlen-Ende | s | 120 |
| Don | Duration for On | Ein-Impuls-Dauer für MaxTp | s | 750 |
| Doff | Duration for Off | Aus-Impuls-Dauer für MaxTp | s | 300 |
| MaxTp | Maximum threshold for pulsing | Max. Ventilöffnung Taktung (%; 0 = deaktiviert) | % | 0 |
| Dfc | Days until Filter Change | Tage bis Filterwechsel erforderlich (0 = deaktiviert) | Tage | 0 |
| Tt2s | Time to second stage | Verzögerung vor Stufe-2-Aktivierung nach Heiz-/Kühlzyklus-Start | min | 60 |
| ϑminS2 | Minimum Temperature Stage 2 | Wenn Außentemperatur unter diesem Wert: Stufe 2 sofort aktiviert (nur bei bestimmten Konfigurationen) | ° | -6 |
| ϑminHP | Minimum Temperature Heat Pump | Minimale Außentemperatur zum Betrieb der Wärmepumpe; darunter nur Zusatzheizung (nur bei bestimmten Konfigurationen) | ° | -22 |
| Otm | Outdoor Temperature Mode | 0 = deaktiviert; 1 = Durchschn. 48h; 2 = Systemvariable "Erw. Durchschn. 48h"; 3 = Aktuelle Temperatur | - | 2 |
| ϑLimH | Temperature Limit Heating | Keine Heizung wenn verwendete Außentemp. > dieses Limit (trotz Anforderung) | ° | 18 |
| ϑLimC | Temperature Limit Cooling | Keine Kühlung wenn verwendete Außentemp. < dieses Limit (trotz Anforderung) | ° | 15 |

Quelle: https://www.loxone.com/dede/kb/klima-controller/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Default |
|-------------|--------------|---------|
| Raumregler zuordnen | Baustein als Quelle für einzelne Raumregler; weitere Einstellungen (Priorität, PWM) im Raumregler-Dialog | - |
| Heizungstyp | Typ der angesteuerten Heizung (beeinflusst Funktionsweise bestimmter Parameter) | - |
| Energiekosten (Heizen) | Kosten-Klassifikation; "teuer" nur bei höher priorisierten Quellen | - |
| Energiekosten (Kühlen) | Kosten-Klassifikation; "teuer" nur bei höher priorisierten Quellen | - |

Quelle: https://www.loxone.com/dede/kb/klima-controller/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| ϑt | `TempAvg` | Eingang | Temperature Threshold | Analoger Eingang Temperaturschwelle Im Modus "Automatisch mit Temperaturschwelle" wird dieser Wert für die Erlaubnis von Heiz/Kühlmodus verwendet Ist dieser Eingang nicht verbunden, verwendet der Baustein die durchschnittliche Aussentemperatur der letzen 48h | ∞ ° |
| Ie | `Error` | Eingang | Error | Fehlereingang | ∞ |
| Is | `ServiceMode` | Eingang | Service Mode | Service-Modus | ∞ |

---

### 3. HVAC Controller

**Kurzbeschreibung:**
HVAC-System-Steuerung (primär nordamerikanisch, aber auch für andere Systemtypen einsetzbar). Unterstützt automatische Heiz-/Kühl-Modus-Umschaltung, zweistufige Heiz-/Kühlausgänge, Kompressor-Steuerung, Reversierventil, Lüfter, Luftbefeuchter und Notfall-Heizung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| Mode | Mode | 0 = aus; 1 = Automatikbetrieb (Heizen/Kühlen automatisch); 2 = nur Heizen; 3 = nur Kühlen | - |
| ϑo | Outdoor temperature | Außentemperatur (Systemvariable "Außentemperatur" falls nicht verbunden) | ° |
| B | Boost | Zweite Kühl-/Heiz-Stufe sofort aktivieren (wenn Stufe 1 bereits aktiv) | - |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre; > 500ms: Sensor-Name verwenden (dominierend) | - |
| Emh | Emergency Heat | Aktiviert Ausgang (E) wenn Heizanforderung = 1 (z.B. bei defekter Wärmepumpe) | - |
| Fan | Fan | Aktiviert Ausgang (G) dauerhaft und öffnet alle Raumregler zu 100%; übersteuert App-Ventilator-Kontrolle | - |
| H | Humidity | Relative Luftfeuchtigkeit zur Optimierung (verwende wichtigsten Raum oder Mittelwert); für Ausgang (Hmd) erforderlich | - |
| Ec | Excess cooling | Überschüssige/günstige Kühlenergie vorhanden (für Raumregler) | - |
| Eh | Excess heating | Überschüssige/günstige Heizenergie vorhanden (für Raumregler) | - |

Quelle: https://www.loxone.com/dede/kb/hvac-controller/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| W/W1 | 1st stage heating | Heizstufe 1 (Bedeutung variiert je Heizungstyp) | 0/1 |
| W2 | 2nd stage heating | Heizstufe 2 (Bedeutung variiert je Heizungstyp) | 0/1 |
| Y | Compressor | Kompressor (Bedeutung variiert je Heizungstyp) | 0/1 |
| Y2 | 2nd stage cooling | Kühlstufe 2 (Bedeutung variiert je Heizungstyp) | 0/1 |
| E | Emergency Heat | Notfall-Heizung (aktiv je nach Eingang Emh oder App-Aktivierung) | 0/1 |
| O/B | Reversing valve | Reversierventil zur Wirkrichtungs-Änderung Wärmepumpe (Bedeutung abhängig von DirV) | 0/1 |
| G | Fan | Lüfter (transportiert erwärmte/gekühlte Luft in Räume) | 0/1 |
| Hmd | Humidifier | Luftbefeuchter (aktiviert im Heizbetrieb wenn H < Hs) | 0/1 |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/hvac-controller/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| minO | Minimum OFF time | Heizen/Kühlen muss länger als minO ausgeschaltet sein, bevor es wieder aktiv werden kann (verhindert häufiges Ein-/Ausschalten) | s | 300 |
| Sot | Switch-on threshold | Arithmetischer Mittelwert Anforderung aller Raumregler muss > diesen Wert sein zum Starten; **WARNUNG**: energetische Mindestabnahme zur Vermeidung Überhitzung/Einfrieren | % | 30 |
| Fot | Fan overrun time | Ausschaltverzögerung Ventilator nach Heizen/Kühlen-Ende (Restenergie transportieren; auch Lärmreduktion) | s | 90 |
| Tt2s | Time to second stage | Heizung/Kühlung länger als diese Zeit aktiv: Stufe 2 aktivieren | s | 300 |
| Δϑ | Delta temperature second stage | Übersteigt Ist-/Solltemp.-Unterschied Raumregler diesen Wert: Stufe 2 aktivieren; deaktiviert bei 0° | ° | 2 |
| mioϑc | Minimum outdoor temperature cooling | Unterschreitet verwendete Außentemp. diesen Wert: nur Heizen erlaubt (nur bei bestimmten Konfigurationen) | ° | 15 |
| maoϑh | Maximum outdoor temperature heating | Überschreitet verwendete Außentemp. diesen Wert: nur Kühlen erlaubt (nur bei bestimmten Konfigurationen) | ° | 18 |
| ϑpmic | Protection temperature minimum cooling | Minimale Außentemp. zur Wärmepumpen-Aktivierung Kühlmodus (Schutz vor Schäden) | ° | 12 |
| ϑpmih | Protection temperature minimum heating | Minimale Außentemp. zur Wärmepumpen-Aktivierung Heizmodus (nur "Wärmepumpe + fossile Zusatzheizung") | ° | 0 |
| ϑpmah | Protection temperature maximum heating | Maximale Außentemp. zur Wärmepumpen-Aktivierung Heizmodus (nicht bei "Öl/Gas/Elektrisch") | ° | 19 |
| Hs | Humidity setpoint | Im Heizbetrieb: Luftbefeuchter aktiviert wenn H < Hs; deaktiviert wenn H > Hs + 2 | % | 45 |
| DirV | Direction valve | Ändert Wirkrichtung Reversierventil Wärmepumpe | - | 0 |
| Otm | Outdoor Temperature Mode | 0 = deaktiviert; 1 = Durchschn. 48h; 2 = Systemvariable "Erw. Durchschn. 48h"; 3 = Aktuelle Temp. (für mioϑc, maoϑh) | - | 3 |

Quelle: https://www.loxone.com/dede/kb/hvac-controller/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Default |
|-------------|--------------|---------|
| Heizungstyp | Typ der angesteuerten Heizung (beeinflusst Ausgangs-Ansteuerung) | - |
| Raumregler zuordnen | Baustein als Quelle für einzelne Raumregler; weitere Einstellungen (Priorität, PWM) im Raumregler-Dialog | - |

Quelle: https://www.loxone.com/dede/kb/hvac-controller/

**Fallstricke:** [BELEGT]
- Der HVAC Controller ist in erster Linie für nordamerikanische HVAC-Systeme konzipiert. Er ist jedoch nicht auf diesen Anwendungsbereich beschränkt und kann je nach Projektanforderungen auch mit einer Vielzahl anderer Systemtypen eingesetzt werden.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| W/W1 | `OutHeat1` | Ausgang | 1st stage heating | Heizstufe 1. Variiert je nach gewähltem Heizungstyp. Für "Öl/Gas/Elektrisch": aktiv für die erste Heizstufe, aktiv für die zweite Heizstufe. Für "Wärmepumpe mit fossiler Zusatzheizung": aktiv für die zweite Heizstufe. Für "Wärmepumpe mit elektrischer Zusatzheizung": aktiv für die zweite Heizstufe. | – |
| O/B | `OutValve` | Ausgang | Reversing valve | Ändert die Wirkrichtung der Wärmepumpe. Ist (DirV) deaktiviert: Aus für Heizen, Ein für Kühlen. Ist (DirV) aktiviert: EIN für Heizen, AUS für Kühlen. | – |

---

### 4. Heizkurve

**Kurzbeschreibung:**
Berechnet Vorlauftemperatur aus Sollwert und Außentemperatur mittels linearer Heizkurve (oder Kühlkurve). Unterstützt Steigungsanpassung (Slope) und Parallelverschiebung (Offset) sowie Min/Max-Limits.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| Tt | Target temperature | Solltemperatur | ° |
| Ct | Current temperature | Aktuelle Außentemperatur | ° |
| Dis | Disable | Deaktiviert Eingang (Tt) wenn Ein | - |

Quelle: https://www.loxone.com/dede/kb/heizkurve/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| Ft | Flow temperature | Berechnete Vorlauftemperatur | ° |
| Iv | Invalid values | 1, wenn berechnete (Ft) die Grenzen (minFt) oder (maxFt) überschreiten würde | - |

Quelle: https://www.loxone.com/dede/kb/heizkurve/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| S | Slope | Steilheit der Heizkurve oder Kühlkurve | - | 1,3 |
| O | Offset | Parallelverschiebung (Heizen: Erhöhung der Vorlauf-Solltemp.; Kühlen: Absenkung) | - | 0 |
| minFt | Minimum flow temperature | Minimale Vorlauftemperatur; Außentemp. muss bereitgestellt werden (Eingang Ct oder Systemvariable) | ° | 15 |
| maxFt | Maximum flow temperature | Maximale Vorlauftemperatur; Außentemp. muss bereitgestellt werden (Eingang Ct oder Systemvariable) | ° | 65 |

Quelle: https://www.loxone.com/dede/kb/heizkurve/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/heizkurve/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

### 5. Heizungsmischer

**Kurzbeschreibung:**
Regelt einen 0-10V Mischer oder zwei digitale Auf-/Zu-Ausgänge (3-Punkt-Mischer) zur Temperatur-Stabilisierung. Verwendet PID-Regelung mit einstellbarem Kp/Ki und unterstützt manuelle Sollwert-Eingabe sowie Kindersicherung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| ϑt | Target temperature | Solltemperatur | ° |
| ϑc | Current temperature | Aktuelle Temperatur | ° |
| Off | Off | Setzt Ausgang (V) entsprechend Parameter (Offm) | - |
| DisPc | Disable periphery control | Deaktiviert Eingang (ϑt) wenn Ein (z.B. Kindersicherung, Reinigung) | - |

Quelle: https://www.loxone.com/dede/kb/heizungsmischer/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| V | Valve | 0-10V Signal für 0-10V Mischer | V |
| O | Open | Öffnen (3-Punkt-Mischer) | 0/1 |
| C | Close | Schließen (3-Punkt-Mischer) | 0/1 |
| Error | Error | Aktiv wenn Differenz Ist-/Solltemp. > 5°C länger als 10 Min (Timer-Reset nach Referenzfahrt/Solltemp.-Änderung/Eingang-Änderung für 15 Min) | - |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/heizungsmischer/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Td | Travel duration mixing valve | Laufzeit Mischer (komplette Fahrt 0% bis 100%) | s | 150 |
| St | Sampling time | Abtastzeit Regler (Neuberechnung von V, O, C in diesem Intervall) | s | 40 |
| Kp% | Gain | Proportional-Verstärkung in % (Kp% = Kp × 100) | % | 2 |
| Ki% | Integral part | Integral-Anteil in % (Ki% = Ki × 100) | % | 0,03 |
| Offm | Off mode | 0 = Unverändert; 1 = Öffnen; 2 = Schließen | - | 2 |
| Mode | Mode | 0 = normal; 1 = invertiert (Kühlung: Mischer öffnet mit steigender Temp.) | - | 0 |
| MinP | Minimum Position | Minimale Ventilposition | % | 0 |
| MaxP | Maximum Position | Maximale Ventilposition | % | 100 |
| Inv | Invert | 0 = normal; 1 = Analogausgang invertiert (0V = 100%, 10V = 0%) | - | 0 |
| Vs | Valve standstill | Max. Ventil-Stillstand in Tagen; automatische Bewegung wenn überschritten; 0 = deaktiviert | d | 14 |

Quelle: https://www.loxone.com/dede/kb/heizungsmischer/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Default |
|-------------|--------------|---------|
| Für Systemstatus-Meldungen verwenden | Fehlermeldungen über Mailer und Systemstatus versenden | - |

Quelle: https://www.loxone.com/dede/kb/heizungsmischer/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

### 6. Vorlauftemperatur Rechner

**Kurzbeschreibung:**
Berechnet Vorlauf- und Puffer-Solltemperaturen aus den Anforderungen aller zugeordneten Intelligenten Raumregler basierend auf linearer Heizkurve. Berücksichtigt Raumgröße und Intensität. Steuert Mischer-/Pumpen-Freigabe (Qp).

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| ϑo | Outdoor Temperature | Aktuelle Außentemperatur (Systemvariable "Außentemperatur" falls nicht verbunden; -1000 bei Fehler) | ∞ |
| Ib | Boost | Boost-Eingang: Heizen = max. Vorlauftemp. (Max); Kühlen = min. Vorlauftemp. (Min) | 0/1 |
| St | Stop | Stop-Eingang: Pumpe/Mischer aus; Heizen = Min-Solltemp.; Kühlen = Max-Solltemp. | 0/1 |
| Tb | Buffer Temperature | Puffertemperatur; aktiviert Mischer/Pumpe (Qp) wenn Puffer Sollwert erreicht (AQb ± B je nach Heizen/Kühlen) | ∞ |

Quelle: https://www.loxone.com/dede/kb/intelligente-temperatursteuerung/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| AQt | Room target temperature | Raum-Solltemperatur mit höchster (Heizen) oder niedrigster (Kühlen) Vorlauftemp.-Anforderung | ∞ |
| TxQr | Room name | Textausgang = Name Raum mit extremster Vorlauftemp.-Anforderung (nur bei bestimmten Konfigurationen) | - |
| AQf | Flow target temperature | Berechnete Vorlauf-Solltemperatur | ∞ |
| AQb | Buffer target temperature | Berechnete Puffer-Solltemperatur | ∞ |
| Qp | Manifold demand | Mischer-/Pumpen-Freigabe (aktiv wenn mind. ein Raumregler die Einschaltschwelle (Str) überschreitet; bei Tb-Eingang: wenn Puffer Sollwert erreicht) | 0/1 |
| AQr | Heating / cooling unit requirement | Heiz-/Kühl-Anforderung in °Cm² (Temp.-Differenz × Raumgröße summiert) | ∞ |
| AQl | Heating / cooling load | Heiz-/Kühllast in % (0-100%; summierte Intensität × Fläche / Gesamtfläche) | ∞ |
| AQi | Flow temperature increase / decrease | Vorlauftemp.-Erhöhung während Aufheiz (Heizen) oder -Erniedrigung während Abkühlphase (Kühlen) | ∞ |
| Qe | Error | Fehlerausgang (ungültige Werte) | 0/1 |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/intelligente-temperatursteuerung/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Min | Minimum | Minimale Vorlauf-Solltemperatur; Außentemp. erforderlich (ϑo oder Systemvariable) | - | 5 |
| Max | Maximum | Maximale Vorlauf-Solltemperatur; Außentemp. erforderlich (ϑo oder Systemvariable) | - | 40 |
| B | Buffer Target Temperature Offset | Puffertemp.-Erhöhung beim Heizen (AQb = AQf + B); Absenkung beim Kühlen (AQb = AQf - B) | - | 5 |
| S | Slope | Steilheit der Heizkurve oder Kühlkurve | - | 0,5 |
| N | Offset | Parallelverschiebung (Heizen: Erhöhung; Kühlen: Absenkung der Vorlauf-Solltemp.) | - | 0 |
| Str | Switch-On Threshold | Einschaltschwelle in % (Ventilstellung mind. eines Raums muss überschreiten für Pumpen-Freigabe Qp); nicht wirksam bei Heiz-/Kühlsteuerungs-Raumreglern | - | 35 |
| G | Gain | Verstärkungsfaktor Raum-Temperaturabweichung (Standard = 1) | - | 1 |
| I | Target temperature increase / decrease | Raum-Solltemp.-Erhöhung Aufheizphase (Heizen) oder -Erniedrigung Abkühlphase (Kühlen) | - | 2 |
| Ps | Pump standstill | Max. Pumpen-Stillstand in Tagen; automatische Aktivierung um 2:00 Uhr für 3 Min wenn überschritten; 0 = deaktiviert | d | 0 |

Quelle: https://www.loxone.com/dede/kb/intelligente-temperatursteuerung/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Default |
|-------------|--------------|---------|
| Mischerkreis für | Auswahl Heiz- oder Kühlkreis | - |
| Zuordnungen | Zuordnung von Intelligenten Raumreglern (zur Berechnung von Vorlauf-/Puffertemperaturen) | - |

Quelle: https://www.loxone.com/dede/kb/intelligente-temperatursteuerung/

**Fallstricke:** [BELEGT]
- Beim Kühlen ist es wichtig, dass die Vorlauftemperatur nicht unter die Taupunkttemperatur sinkt (Kondenswasserbildung). Dies lässt sich durch entsprechende Min-Parameter-Einstellung erreichen.
- Beim Kühlen wird empfohlen, Raumsolltemperaturen bei steigenden Außentemperaturen zu erhöhen.

---

### 7. Taupunktrechner

**Kurzbeschreibung:**
Berechnet die Taupunkttemperatur aus aktueller Temperatur und relativer Luftfeuchtigkeit. Unterstützt Offset-Verschiebung der berechneten Taupunkttemperatur.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| ϑ | Temperature | Aktuelle Temperatur | ° |
| H | Relative Humidity | Relative Luftfeuchtigkeit | % |

Quelle: https://www.loxone.com/dede/kb/taupunktrechner/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| ϑd | Dew Point | Berechnete Taupunkttemperatur | ° |

Quelle: https://www.loxone.com/dede/kb/taupunktrechner/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| O | Output Offset | Addiert festen Offset zum berechneten Taupunkt | ° | 0 |

Quelle: https://www.loxone.com/dede/kb/taupunktrechner/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/taupunktrechner/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Bp | `Baro` | Eingang | Barometric Pressure | Aktueller barometrischer Druck | ∞ hPa |

---

### 8. Solarregelung

**Kurzbeschreibung:**
Steuert Solarpumpe und mehrere Pufferspeicher (bis zu 5) zur optimalen Wärmenutzung. Unterstützt automatische und manuelle Modi, Übertemperatur-Schutz, Ladeverantwortliche und Überschuss-Signalisierung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| ϑc | Current collector temperature | Aktuelle Kollektortemperatur | ° |
| ϑs1-5 | Current storage temperature 1-5 | Aktuelle Speichertemperatur 1-5 | ° |
| Sel | Select storage | Legt Pufferspeicher fest für manuellen Betrieb (M); 0 = Solarpumpe bleibt aus | - |
| M | Manual mode | Aktiviert manuellen Betrieb und heizt angegebenen Pufferspeicher (deaktiviert bei Kollector-Überhitzung) | - |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre; > 500ms: Sensor-Name verwenden (dominierend) | - |

Quelle: https://www.loxone.com/dede/kb/solarregelung/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit |
|--------|-------------|--------------|---------|
| Sp | Solar pump | Digitaler Ausgang Solarpumpen-Steuerung | 0/1 |
| Spa | Solar pump analog (0-10V) | Analoger Ausgang 0-10V Solarpumpen-Steuerung | 0...10 |
| S1-5 | Storage 1-5 state | Ausgänge aktiv wenn jeweiliger Pufferspeicher aufgeheizt werden darf | 0/1 |
| S | Current storage | > 0 = Speicher wird gerade aufgeheizt; 0 = Pumpe aus; -1 = alle Speicher auf Maxtemp. | -1...5 |
| Minϑs | Min. storage temperature exceeded | Aktiv wenn alle Pufferspeicher ihre Zieltemperatur überschritten | 0/1 |
| Maxϑs | Max. storage temperature exceeded | Aktiv wenn alle Pufferspeicher ihre Maxtemp. erreicht (Pumpe aus) | 0/1 |
| Co | Collector overheating | Aktiv wenn Kollektor überhitzt | 0/1 |
| Hs | Heating surplus | Aktiv bevor letzter Pufferspeicher Maxtemp. erreicht (Timing nach Parameter ϑHs) | 0/1 |
| API | API Connector | Intelligenter API-basierter Verbinder | - |

Quelle: https://www.loxone.com/dede/kb/solarregelung/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Pon | Pump switch-on threshold | Temperaturdifferenz Kollektor ≥ Speicher um diesen Wert zum Pumpen-Start erforderlich | ° | 8 |
| Poff | Pump switch-off threshold | Temperaturdifferenz Kollektor ≥ Speicher um diesen Wert zum Pumpen-Stopp erforderlich | ° | 4 |
| Maxϑc | Max. temperature collector | Pumpe sperren wenn Kollektortemp. diesen Wert überschreitet (Übertemperatur-Schutz) | ° | 120 |
| Minϑs1-5 | Min. temperature storage | Wenn Pufferspeicher diese Temp. erreicht: nächster Speicher laden, bis alle Speicher Mintemp. haben | ° | 60 |
| Maxϑs1-5 | Max. temperature storage | Wenn alle Pufferspeicher diese Temp. erreicht: Pumpe abschalten | ° | 70 |
| ϑHs | Temperature heating surplus | Entfernung des letzten Speichers von seiner Maxtemp. bevor Ausgang (Hs) aktiviert wird | ° | 5 |

Quelle: https://www.loxone.com/dede/kb/solarregelung/

**Eigenschaften:** [BELEGT]
| Eigenschaft | Beschreibung | Wertebereich | Default |
|-------------|--------------|--------------|---------|
| Konfiguration | Konfigurieren Sie Anzahl und Anzeigenamen der Speicher/Puffer | - | - |
| Anzahl Speicher | Anzahl der Speicher/Puffer, die mit der Solaranlage separat geladen werden können (Maximum: 5) | 1...5 | 1 |

Quelle: https://www.loxone.com/dede/kb/solarregelung/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Am | `AIm` | Eingang | Operating mode | Auswahl des zu verwendenden Betriebsmodus. (0 = Automatikbetrieb: Im Kalender steht „Heizperiode“ zur Verfügung (Diese Einstellungen (Datum) entscheiden, ob der Winterbetriebsmodus aktiviert wird) , 1 = manueller Sommerbetrieb , 2 = manueller Winterbetrieb) Im Winterbetriebsmodus wird die Priorität der Beladung der beiden ersten Speicher vertauscht. | ∞ |
| Qs | `Qs` | Ausgang | – | Status Startmodus. Ein, wenn die Pumpe durch die Startfunktion aktiviert wurde. | – |
| Tf | `IT` | Parameter | Circulation duration | Spüldauer im Startmodus (Zeit, die die Flüssigkeit benötigt, um vom Kollektor zum Sensor zu gelangen). | ∞ s |
| Ts | `ST` | Parameter | Circulation interval for start mode | Durchspülintervall im Startmodus. | ∞ s |

---

### 9. 2-Punkt-Regler

**Kurzbeschreibung:**
Einfacher digitaler Regler mit zwei Zuständen (Ein/Aus) basierend auf Sollwert und Hysterese. Unterstützt optionale Invertierung des Regelverhaltens.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| PV | Process value | Tatsächlicher Wert der Regelgröße | ∞ |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre (dominierend) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/2-punkt-regler/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/2-punkt-regler/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich | Default |
|--------|-------------|--------------|--------------|---------|
| SP | Setpoint | Sollwert der Regelgröße | ∞ | 5 |
| Hys | Hysteresis | Hysterese des 2-Punkt-Reglers (verhindert ständiges Ein-/Ausschalten) | ∞ | 0,5 |
| Inv | Inverted | Invertiert Reglerverhalten | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/2-punkt-regler/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/2-punkt-regler/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

### 10. 3-Punkt-Regler

**Kurzbeschreibung:**
Digitaler Regler mit drei Zuständen (Aus / Öffnen / Schließen) basierend auf zwei Sollwerten. Typischerweise für 3-Punkt-Ventil-Steuerung (Mischer).

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| PV | Process value | Tatsächlicher Wert der Regelgröße | ∞ |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre (dominierend) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/3-punkt-regler/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| O1 | Output 1 | Ausgang 1 (z.B. Öffnen) | 0/1 |
| O2 | Output 2 | Ausgang 2 (z.B. Schließen) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/3-punkt-regler/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich | Default |
|--------|-------------|--------------|--------------|---------|
| SP1 | Setpoint 1 | Sollwert 1 | ∞ | 3 |
| SP2 | Setpoint 2 | Sollwert 2 | ∞ | 7 |

Quelle: https://www.loxone.com/dede/kb/3-punkt-regler/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/3-punkt-regler/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

### 11. PI – Regler

**Kurzbeschreibung:**
Kontinuierlicher Proportional-Integral-Regler zur analogen Regelung mit Proportional- und Integralanteil. Unterstützt manuelle und automatische Modi, Schwellwert-Unterdrückung und Ausgangsbegrenzung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| PV | Process value | Tatsächlicher Wert der Regelgröße | ∞ |
| Auto | Automatic | 0 = Manuell; 1 = Automatik | 0/1 |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre (dominierend) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/pi-regler/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| CO | Controller output | Ausgang des Reglers zur Beeinflussung der Regelgröße | ∞ |

Quelle: https://www.loxone.com/dede/kb/pi-regler/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Rem | Remanence input | Remanenzeingang: Baustein behält letzten Zustand nach Miniserver-Neustart (Speicherung beim Speichern/geplanten Neustart/Backup/stündlich auf SD) | - | 0 |
| SP | Setpoint | Sollwert der Regelgröße | - | 5 |
| St | Sampling time | Zeitabstand für Neuberechnung von (CO) | s | 1 |
| Th | Threshold | Ansprechschwelle zur Unterdrückung kleiner Regeldifferenzen (PV - SP) | - | 1 |
| Kp | Proportional gain | Proportionalanteil | - | 2 |
| Ki | Integral gain | Integralanteil | - | 1 |
| Mv | Manual value | Wert ausgegeben an (CO) wenn (Auto) = 0 | - | 5 |
| Min | Minimum | Minimaler Ausgangswert bei (CO) | - | 0 |
| Max | Maximum | Maximaler Ausgangswert bei (CO) | - | 10 |

Quelle: https://www.loxone.com/dede/kb/pi-regler/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/pi-regler/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

### 12. PID – Regler

**Kurzbeschreibung:**
Kontinuierlicher Proportional-Integral-Differenzial-Regler mit Proportional-, Integral- und Differentialanteil. Unterstützt manuelle und automatische Modi, Schwellwert-Unterdrückung und Ausgangsbegrenzung.

**Eingänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| PV | Process value | Tatsächlicher Wert der Regelgröße | ∞ |
| Auto | Automatic | 0 = Manuell; 1 = Automatik | 0/1 |
| Off | Off / Lock | Pulse < 200ms: Reset; > 200ms: Sperre | 0/1 |

Quelle: https://www.loxone.com/dede/kb/pid-regler/

**Ausgänge:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Wertebereich |
|--------|-------------|--------------|--------------|
| CO | Controller output | Ausgang des Reglers zur Beeinflussung der Regelgröße | ∞ |

Quelle: https://www.loxone.com/dede/kb/pid-regler/

**Parameter:** [BELEGT]
| Kürzel | Bezeichnung | Beschreibung | Einheit | Default |
|--------|-------------|--------------|---------|---------|
| Rem | Remanence input | Remanenzeingang: Speichert Zustand auf SD-Karte nach Miniserver-Neustart | - | 0 |
| SP | Setpoint | Sollwert der Regelgröße | - | 5 |
| St | Sampling time | Zeitabstand für Neuberechnung von (CO) | s | 1 |
| Th | Threshold | Ansprechschwelle zur Unterdrückung kleiner Regeldifferenzen | - | 1 |
| Kp | Proportional gain | Proportionalanteil | - | 2 |
| Ki | Integral gain | Integralanteil | - | 1 |
| Kd | Derivative gain | Differentialanteil | - | 0 |
| Mv | Manual value | Wert ausgegeben an (CO) wenn (Auto) = 0 | - | 5 |
| Min | Minimum | Minimaler Ausgangswert bei (CO) | - | 0 |
| Max | Maximum | Maximaler Ausgangswert bei (CO) | - | 10 |

Quelle: https://www.loxone.com/dede/kb/pid-regler/

**Eigenschaften:** [BELEGT]
- Keine Tabelle vorhanden

Quelle: https://www.loxone.com/dede/kb/pid-regler/

**Fallstricke:** [BELEGT]
- Keine dokumentierten Warnhinweise.

---

## Zusammenfassung

**Bausteine erfasst:** 12/12

**Erfassungs-Checkliste:**
- [x] Intelligente Raumregelung
- [x] Heiz- und Kühlsteuerung
- [x] HVAC Controller
- [x] Heizkurve
- [x] Heizungsmischer
- [x] Vorlauftemperatur Rechner
- [x] Taupunktrechner
- [x] Solarregelung
- [x] 2-Punkt-Regler
- [x] 3-Punkt-Regler
- [x] PI – Regler
- [x] PID – Regler

**Qualitätskontrolle:**
- Alle Kürzel (einschl. Sonderzeichen wie ϑ) wurden wörtlich übernommen
- Alle Tabellen wurden als [BELEGT] aus der offiziellen Loxone-KB dokumentiert
- Keine Einträge erfunden oder geraten
- Defaultwerte und Wertebereiche vollständig
- Fallstricke/Warnhinweise dokumentiert
- Quelle (URL) bei jedem Baustein angegeben

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Zentralheizung (BETA) (`HeatCentral`)

Zentralheizung

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AIk1 | `IK1` | Boiler Temperature 1 | Analoger Eingang für die aktuelle Kesseltemperatur 1 [°] | ∞ |
| AIk2 | `IK2` | Boiler Temperature 2 | Analoger Eingang für die aktuelle Kesseltemperatur 2 [°] | ∞ |
| Tb | `SB` | Boiler target temperature | Analoger Eingang für die gewünschte Boilertemperatur [°] | ∞ |
| AIb | `IB` | Boiler temperature | Analoger Eingang für die aktuelle Boilertemperatur [°] | ∞ |
| Tp1 | `SP1` | Target Temperature Buffer 1 | Analoger Eingang für die gewünschte Puffertemperatur 1 [°] | ∞ |
| Tp2 | `SP2` | Target Temperature Buffer 2 | Analoger Eingang für die gewünschte Puffertemperatur 2 [°] | ∞ |
| Tp3 | `SP3` | Target Temperature Buffer 3 | Analoger Eingang für die gewünschte Puffertemperatur 3 [°] | ∞ |
| Tp4 | `SP4` | Target Temperature Buffer 4 | Analoger Eingang für die gewünschte Puffertemperatur 4 [°] | ∞ |
| AIb1 | `IP1` | Temperature Buffer 1 | Analoger Eingang für die aktuelle Puffertemperatur 1 [°] | ∞ |
| AIb2 | `IP2` | Temperature Buffer 2 | Analoger Eingang für die aktuelle Puffertemperatur 2 [°] | ∞ |
| AIb3 | `IP3` | Temperature Buffer 3 | Analoger Eingang für die aktuelle Puffertemperatur 3 [°] | ∞ |
| AIb4 | `IP4` | Temperature Buffer 4 | Analoger Eingang für die aktuelle Puffertemperatur 4 [°] | ∞ |
| TVl1 | `SV1` | Target Flow Temperature 1 | Analoger Eingang für die gewünschte Vorlauftemperatur 1 [°] | ∞ |
| TVl2 | `SV2` | Target Flow Temperature 2 | Analoger Eingang für die gewünschte Vorlauftemperatur 2 [°] | ∞ |
| TVl3 | `SV3` | Target Flow Temperature 3 | Analoger Eingang für die gewünschte Vorlauftemperatur 3 [°] | ∞ |
| TVl4 | `SV4` | Target Flow Temperature 4 | Analoger Eingang für die gewünschte Vorlauftemperatur 4 [°] | ∞ |
| AIv1 | `IV1` | Current Flow Temperature 1 | Analoger Eingang für die aktuelle Vorlauftemperatur 1 [°] | ∞ |
| AIv2 | `IV2` | Current Flow Temperature 2 | Analoger Eingang für die aktuelle Vorlauftemperatur 2 [°] | ∞ |
| AIv3 | `IV3` | Current Flow Temperature 3 | Analoger Eingang für die aktuelle Vorlauftemperatur 3 [°] | ∞ |
| AIv4 | `IV4` | Current Flow Temperature 4 | Analoger Eingang für die aktuelle Vorlauftemperatur 4 [°] | ∞ |
| AIe | `IE` | Error Signal Input | Analoger Eingang für Störmeldungen | ∞ |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Qh1 | `Qh1` | – | Anforderung Heizkreis 1 | – |
| Qh2 | `Qh2` | – | Anforderung Heizkreis 2 | – |
| Qh3 | `Qh3` | – | Anforderung Heizkreis 3 | – |
| Qh4 | `Qh4` | – | Anforderung Heizkreis 4 | – |
| AQb | `AQb` | – | Solltemperatur Boiler | ∞ |
| AQb1 | `AQp1` | – | Solltemperatur Pufferspeicher 1 | ∞ |
| AQb2 | `AQp2` | – | Solltemperatur Pufferspeicher 2 | ∞ |
| AQb3 | `AQp3` | – | Solltemperatur Pufferspeicher 3 | ∞ |
| AQb4 | `AQp4` | – | Solltemperatur Pufferspeicher 4 | ∞ |
| AQv1 | `AQv1` | – | Solltemperatur Vorlauf 1 | ∞ |
| AQv2 | `AQv2` | – | Solltemperatur Vorlauf 2 | ∞ |
| AQv3 | `AQv3` | – | Solltemperatur Vorlauf 3 | ∞ |
| AQv4 | `AQv4` | – | Solltemperatur Vorlauf 4 | ∞ |
| Rh1 | `RH1` | Preheat return with residual heat from boiler 1 | Aktiviert den Mischer für die Rücklaufanhebung zur Restwärmenutzung von Heizkessel 1. | – |
| Rh2 | `RH2` | Preheat return with residual heat from boiler 2 | Aktiviert den Mischer für die Rücklaufanhebung zur Restwärmenutzung von Heizkessel 2. | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 481

---

### Intelligente Raumregelung Gen 1 (`IRoomcontrol`)

Intelligente Raumtemperaturregelung mit analogen oder digitalen Steuerausgängen

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Am | `AMode` | Mode | 0=Automatik: In den Betriebszeiten stehen „Heizperiode“ und „Kühlperiode“ zur Verfügung. Diese Einstellungen (Datum) entscheiden, ob der Heiz- oder Kühlbetrieb aktiviert wird. Gibt es dazwischen einen undefinierten Datumsbereich, sind alle Ausgänge deaktiviert. Diese Betriebszeiten gelten global für alle Intelligenten Raumregler in einem Projekt. 1=Automatik Heizbetrieb: Solltemperatur von Schaltuhr Heizen, Heizbereich 1 & 2 aktiv, Kühl- und Beschattungsausgang deaktiviert. 2=Automatik Kühlbetrieb: Solltemperatur von Schaltuhr Kühlen, Kühl- und Beschattungsausgang aktiv, Heizbereich 1 & 2 deaktiviert. 3=Manueller Heizbetrieb: Solltemperatur von Eingang T, Heizbereich 1 & 2 aktiv, Kühl- und Beschattungsausgang deaktiviert. 4=Manueller Kühlbetrieb: Solltemperatur von Eingang T, Kühl- und Beschattungsausgang aktiv, Heizbereich 1 & 2 deaktiviert. | ∞ |
| As | `SMode` | Service mode | 0=Servicemode AUS. 1=Heizen und Kühlen AUS: AQ=0, Q=Aus, AQ2=0, Q2=Aus, AQc=0, Qc=Aus, Qs=Aus - Ventile voll geschlossen 2=Heizen EIN / Kühlen AUS: AQ=10, Q=Ein, AQ2=10, Q2=Ein, AQc=0, Qc=Aus, Qs=Aus 3=Heizen AUS / Kühlen EIN: AQ=0, Q=Aus, AQ2=0, Q2=Aus, AQc=10, Qc=Ein, Qs=Ein 4=Heizen und Kühlen EIN: AQ=10, Q=Ein, AQ2=10, Q2=Ein, AQc=10, Qc=Ein, Qs=Ein - Ventile voll geöffnet | ∞ |
| T | `Input` | Target temperature | Analoger Eingang gewünschte Solltemperatur im manuellen Modus | ∞ |
| AI | `Temp` | Temperature | Analoger Eingang aktuelle Raumtemperatur | ∞ |
| Iw | `Window` | Window | Fensterkontakt (NUR bei Automatik Modi): AUS=Geschlossen, EIN=Offen → 'Haus im Tiefschlaf' bei Heizbetrieb / 'Hitzeschutztemperatur' bei Kühlbetrieb | – |
| Ic | `Comfort` | Select Comfort Temperature | Auswahl Komforttemperatur Startet KOMFORTTEMPERATUR bei EIN (steigende Flanke) und aktiviert den Temperatur Timer mit der Laufzeit (Tsc) bei AUS (fallende Flanke). Nach Ablauf von Tsc läuft der eingestellte Autpilot-Modus weiter. | – |
| Is | `Save` | Early exit (select economy temperature) | Eingang Vorzeitiges Verlassen (Auswahl Spartemperatur) Startet SPARTEMPERATUR bei EIN (steigende Flanke) und aktiviert den Temperatur Timer mit der Laufzeit (Tss) bei AUS (fallende Flanke). Nach Ablauf von Tss läuft der eingestellte Automatik-Modus weiter. Wenn Tss gleich 0 ist, dann bleibt die SPARTEMPERATUR bis zur nächsten Änderung in der Schaltuhr. | – |
| Mo | `Move` | Motion Sensor - Extension of Comfort Temperature Entry | Bewegungsmeldereingang (Verlängerung Komforttemperatur-Zeitfenster) Startet KOMFORTTEMPERATUR bei EIN (steigende Flanke) und aktiviert den Temperatur Timer mit der Laufzeit (Tmv) bei AUS (fallende Flanke). Bei EIN (steigende Flanke) muss sich der Regler im Komforttemperatur-Zeitfenster befinden, ansonsten wird die Änderung ignoriert. Nach Ablauf von Tmv läuft der eingestellte Automatik-Modus weiter. | – |
| R | `Reset` | Reset | Stoppt den Temperatur Timer. Der Temperatur Timer kann über Eingänge (Ic,Is,Mv) oder über die Visualisierung gestartet werden. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | – |
| Dis | `InputDisable` | Disable | Dis sperrt T, Ic und Is | – |
| DisMo | `DisMv` | Disable motion sensor input | Bewegungsmeldereingang Mv deaktivieren | – |
| St | `Stop` | Stop | STOP Eingang Schaltet alle Ausgänge aus und deaktiviert die automatische Ventilbewegung (Tsm, Tcm) | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AQ | `AQ` | – | Analoger Ausgang Heizen Bereich 1 (stetige Ventile 0-10V) | ∞ |
| Q | `Q` | – | Digitaler Ausgang Heizen Bereich 1 (für EIN/Aus-Ventile) Die Periodendauer liegt dabei relativ niedrig. Aus diesem Grund ist dieser nicht für das direkte Schalten großer Lasten (z.B. Infrarotheizungen) mittels Relaiskontakten geeignet. | – |
| AQ2 | `AQ2` | – | Analoger Ausgang Heizen Bereich 2 (stetige Ventile 0-10V) | ∞ |
| Q2 | `Q2` | – | Digitaler Ausgang Heizen Bereich 2 (für EIN/Aus-Ventile) Die Periodendauer liegt dabei relativ niedrig. Aus diesem Grund ist dieser nicht für das direkte Schalten großer Lasten (z.B. Infrarotheizungen) mittels Relaiskontakten geeignet. | – |
| AQc | `AQc` | – | Analoger Ausgang Kühlen Bereich 1 (stetige Ventile 0-10V) | ∞ |
| Qc | `Qc` | – | Digitaler Ausgang Kühlen Bereich 1 (für EIN/Aus-Ventile) Die Periodendauer liegt dabei relativ niedrig. Aus diesem Grund ist dieser nicht für das direkte Schalten großer Lasten (z.B. Infrarotheizungen) mittels Relaiskontakten geeignet. | – |
| AQc2 | `AQc2` | – | Analoger Ausgang Kühlen Bereich 2 (stetige Ventile 0-10V) | ∞ |
| Qc2 | `Qc2` | – | Digitaler Ausgang Kühlen Bereich 2 (für EIN/Aus-Ventile) Die Periodendauer liegt dabei relativ niedrig. Aus diesem Grund ist dieser nicht für das direkte Schalten großer Lasten (z.B. Infrarotheizungen) mittels Relaiskontakten geeignet. | – |
| Qs | `Qs` | – | Digitaler Ausgang für Beschattung - Dauerschaltung | – |
| AQs | `AQs` | – | Analoger Ausgang aktueller Modus: 0 = Automatik 1 = Automatik Heizbetrieb, 2 = Automatik Kühlbetrieb 3 = Manueller Heizbetrieb, 4 = Manueller Kühlbetrieb | ∞ |
| AQss | `AQss` | – | Analoger Ausgang aktueller Servicemodus: 0=Servicemode AUS, 1=Heizen und Kühlen AUS, 2=Heizen EIN / Kühlen AUS, 3=Heizen AUS / Kühlen EIN, 4=Heizen und Kühlen EIN | ∞ |
| Qe | `Qe` | – | Fehler Ausgang - EIN solange der Fehler präsent ist | – |
| TxQa | `Qa` | – | Textausgabe bei Fehler | – |
| AQt | `AQt` | – | Analoger Ausgang aktuelle Zieltemperatur | ∞ |
| AQhm | `AQhm` | – | Analoger Ausgang aktueller Modus Schaltuhr für Heizen | ∞ |
| AQcm | `AQcm` | – | Analoger Ausgang aktueller Modus Schaltuhr für Kühlen | ∞ |
| AQtr | `AQtr` | – | Analoger Ausgang für die Restzeit des Temperatur Timers in Sekunden. Der Temperatur Timer kann über Eingänge (Ic,Is,Mv) oder über die Visualisierung gestartet werden. | ∞ |
| Qp | `Qp` | – | Digitaler Ausgang Aufheizphase oder Abkühlphase 0 = Aufheizphase bzw. Abkühlphase nicht aktiv 1 = Aufheizphase bzw. Abkühlphase aktiv | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Ts | `TSave` | Economy temperature | Spartemperatur in ° relativ zur Komforttemperatur Heizen: Komforttemperatur – Spartemperatur Kühlen: Komforttemperatur + Spartemperatur | ∞ | 3 |
| Tch | `TComfort` | Comfort temperature heating | Absolute Komforttemperatur in ° bei Heizbetrieb | ∞ | 22,5 |
| Tcc | `TComfortC` | Comfort temperature cooling | Absolute Komforttemperatur in ° bei Kühlbetrieb | ∞ | 23 |
| Tp | `TParty` | Party temperature | Partytemperatur in ° relativ zur Komforttemperatur Heizen und Kühlen: Komforttemperatur – Partytemperatur | ∞ | 1 |
| Th | `TMore` | Cozy temperature | Temperatur erhöhter Wäremebedarf in ° relativ zur Komforttemperatur Heizen und Kühlen: Komforttemperatur + Temperatur erhöhter Wäremebedarf | ∞ | 1 |
| Td | `TDeepSleep` | Frost protection temperature | Absolute Haus im Tiefschlaf Temperatur in ° Für Langzeitabwesenheit als Frostschutz (Heizbetrieb) | ∞ | 5 |
| Tm | `TMax` | Overheat protection temperature | Absolute Hitzeschutztemperatur in ° Maximale Temperatur in ° (Kühlbetrieb) | ∞ | 25,5 |
| Tsm | `TimeMove` | Valve movement heating | Maximaler Ventilstillstand im Heizbetrieb (Tage). Wenn die Ventile so lange nicht bewegt wurden, werden sie automatisch bewegt. Wählen Sie die Zeit laut Herstellerangaben. | ∞ | 14 |
| Tcm | `TimeMoveC` | Valve movement cooling | Maximaler Ventilstillstand im Kühlbetrieb (Tage). Wenn die Ventile so lange nicht bewegt wurden, werden sie automatisch bewegt. Wählen Sie die Zeit laut Herstellerangaben. | ∞ | 14 |
| Tsc | `TimeC` | Comfort timer | Laufzeit Komforttemperatur Timer in Sekunden - bei AUS (fallende Flanke) am Eingang Ic wird die Komforttemperatur noch solange weiter forciert | ∞ | 1800 |
| Tss | `TimeS` | Economy timer | Laufzeit Spartemperatur Timer in Sekunden - bei AUS (fallende Flanke) am Eingang Is wird die Spartemperatur noch solange weiter forciert | ∞ | 1800 |
| Tmv | `TimeMv` | Extension of Comfort Temperature Entry | Verlängerung des Komforttemperatur-Zeitfensters in Sekunden - bei AUS (fallende Flanke) am Eingang Mv wird die Komforttemperatur noch solange weiter forciert | ∞ | 1800 |
| Ths | `THCelvin` | Heating up speed | Zeitdauer [min] die benötigt wird, um die Raumtemperatur um 1° zu erhöhen. Ein Wert > 0 überschreibt den vom intelligenten Raumregler gelernten Wert. Falls der Wert 0 ist, wird der vom Raumregler gelernte Wert verwendet. | ∞ | 0 |
| Tcs | `TCCelvin` | Cooling down speed | Zeitdauer [min] die benötigt wird, um die Raumtemperatur um 1° zu senken. Ein Wert > 0 überschreibt den vom intelligenten Raumregler gelernten Wert. Falls der Wert 0 ist, wird der vom Raumregler gelernte Wert verwendet. | ∞ | 0 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 451 · KB: https://www.loxone.com/help/IRoomcontrol

---

### Raumregelung (`Roomcontrol`)

Ausgang (Q) ist ein PWM-Ausgang dessen Einschaltperiode “Qon” sich wie folgt berechnet: Qon = P x ((AQ x 10) / 100) Einstellung der Parameter M,P,V: Für Flächenheizung: M=600, P=600, V=0,7 Für Heizkörper: M=180, P=180, V=0,5

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| T | `Input` | Target temperature | Analoger Eingang SOLL-Temperatur | ∞ |
| AI | `Temp` | Temperature | Analoger Eingang aktuelle IST-Temperatur (Raumtemperatur) | ∞ |
| On | `On` | Continuos ON | Dauer EIN (AQ = 10, Q = 1) | – |
| Off | `Off` | Duration OFF | Dauer AUS (AQ = 0, Q = 0) | – |
| St | `Stop` | Stop | Regelung ist deaktiviert, Ausgänge bleiben unverändert | – |
| Dis | `InputDisable` | Disable | Sperrt Eingang (T) (Kindersicherung) | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| AQ | `AQ` | – | Analoger Ausgang (für stetige Ventile) | ∞ |
| Q | `Q` | – | Digitaler Ausgang (für Ein/Aus-Ventile) | – |
| Qe | `Qe` | – | Ausgang Fehler | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| M | `Mode` | Scan duration | Abtastdauer in Sekunden | ∞ s | 600 |
| P | `PwmPeriod` | Duration of PWM period | PWM-Periodendauer des Ausgangs (Q) | ∞ s | 600 |
| V | `Amplifier` | Gain | Verstärkung des Reglers | ∞ | 1,1 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 440

---
