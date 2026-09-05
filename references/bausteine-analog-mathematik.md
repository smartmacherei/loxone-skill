# Analog & Mathematik

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## 1. Addierer

Addiert zwei analoge Werte und gibt die Summe aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Wertebereich |
|--------|------------------|--------------|
| O | (O) = (V1) + (V2) | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/addierer/

---

## 2. Addierer 4

Addiert vier analoge Werte und gibt die Summe aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Wertebereich |
|--------|------------------|--------------|
| O | (O) = (V1) + (V2) + (V3) + (V4) | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-4 | Value 1-4 | Wert 1-4 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/addierer-4/

---

## 3. Subtrahierer

Subtrahiert zwei analoge Werte und gibt die Differenz aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Beschreibung | Wertebereich |
|--------|--------------|--------------|
| O | (O) = (V1) - (V2) | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/subtrahierer/

---

## 4. Multiplizierer

Multipliziert zwei analoge Werte und gibt das Produkt aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Beschreibung | Wertebereich |
|--------|---|---|
| O | (O) = (V1) x (V2) | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|---|---|---|---|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
"Der Baustein verfügt über folgende besondere Funktionalität: Wenn einer der beiden Eingänge nicht angeschlossen ist oder den Wert 0 anzeigt, wird der Wert 0 ignoriert. In diesem Fall wird nur der verbleibende, angeschlossene Eingang multipliziert."

Quelle: https://www.loxone.com/dede/kb/multiplizierer/

---

## 5. Dividierer

Dividiert zwei analoge Werte und gibt das Ergebnis aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Beschreibung | Wertebereich |
|--------|--------------|--------------|
| O | (O) = (V1) / (V2) | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1 | Value 1 | Wert 1 | ∞ | 0 |
| V2 | Value 2 | Wert 2 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/dividierer/

---

## 6. Modulo

Dividiert analoge Werte als ganze Zahlen oder Dezimalzahlen und gibt den Rest der Division aus.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Int | Integer | Ergebnis der ganzzahligen Berechnung | ∞ |
| Dec | Decimals | Ergebnis der dezimalen Berechnung | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

**Funktionsbeschreibung** [BELEGT]
"Der Modulo-Baustein dividiert analoge Werte als ganze Zahlen oder Dezimalzahlen und gibt den Rest der Division aus."
Beispiele: Int-Ausgang: 13 mod 5 = 3; Dec-Ausgang: 13,3 mod 5,2 = 2,9.

Quelle: https://www.loxone.com/dede/kb/modulo/

---

## 7. Ganzzahl

Rundet einen analogen Wert auf oder ab.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| R | Result | Ergebnis | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V | Value | Analoger Eingang, Wert der auf-oder abgerundet werden soll | ∞ | 0 |
| Ro | Round | R=0:es wird immer abgerundet  R=1:es wird kaufmännisch gerundet, liegt die erste Kommastelle unter 5 wird abgerundet, sonst auf | 0/1 | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/ganzzahl/

---

## 8. Formel

Berechnet das Ergebnis einer benutzerdefinierten Formel mit bis zu 4 analogen Eingängen.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| R | Result | Ergebnis | ∞ |
| E | Error | Bspw. bei einer verbotenen Rechenoperation. | - |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| I1-4 | Value 1-4 | Dieser Wert kann in der Formel verwendet werden. In den Eigenschaften kann auch ein fixer Wert vergeben werden. | ∞ | 0 |

**Eigenschaften** [BELEGT]
| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|--------------|--------------|
| Formel | Die 4 Eingänge/Parameter werden angesprochen mit I1,I2,I3,I4. Folgende Operationen stehen zur Verfügung: +,-,*,/,^ Folgende Funktionen stehen zur Verfügung: PI, ABS, SQRT, LN, LOG, EXP, SIN, COS, TAN, ARCSIN, ARCCOS, ARCTAN, SINH, COSH, TANH, RAD, DEG, SIGN, INT, IF, MIN, MAX. Winkelfunktionen arbeiten im Bogenmaß, Eingangswerte in Grad müssen vorher umgewandelt werden (z.B. SIN(RAD(I1))). Beispiel: (I1+(I2*0,005))/SIN(I3) | - |

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/formel/

---

## 9. Skalierer

Skaliert einen analogen Eingangswert linear auf einen anderen Wertebereich.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Sv | Scaled value | Skalierter Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1 | Value 1 | Wert 1 | ∞ | 0 |
| Sv1 | Scaled value 1 | Skalierter Wert 1 | ∞ | 0 |
| V2 | Value 2 | Wert 2 | ∞ | 10 |
| Sv2 | Scaled value 2 | Skalierter Wert 2 | ∞ | 10 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/skalierer/

---

## 10. MinMax

Ermittelt den kleinsten und größten Wert aus bis zu 4 analogen Eingängen.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Min | Current minimum value | Aktueller Minimumwert | ∞ |
| Max | Current maximum value | Aktueller Maximumwert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-4 | Value 1-4 | Wert 1-4 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/minmax/

---

## 11. MinMax seit Reset

Ermittelt den kleinsten und größten Wert seit dem letzten Reset.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Analoger Eingang, über dessen Werte Minimum und Maximum ermittelt werden. | ∞ |
| R | Reset | Setzt (Min) und (Max) auf den aktuellen Wert (V) zurück. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Wertebereich |
|--------|------------------|--------------|
| Min | Minimum | ∞ |
| Max | Maximum | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/minmax-seit-reset/

---

## 12. Analog MinMax-Begrenzer

Begrenzt einen analogen Wert auf einen Minimalwert und einen Maximalwert.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| V | Value | Wert | ∞ |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| V | Value | Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|
| Min | Minimum | ∞ | 0 |
| Max | Maximum | ∞ | 10 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/analog-min-max-begrenzer/

---

## 13. Mittelwert

Berechnet den Durchschnitt von bis zu 4 analogen Werten.

**Eingänge** [BELEGT]
[nicht vorhanden]

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Avg | Average | Mittelwert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-4 | Value 1-4 | Wert 1-4 | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
"Der Baustein berechnet von mehreren Analogwerten den Durchschnitt und gibt diesen am Ausgang (Avg) aus. Die Verarbeitung mehrerer Werte pro Eingang wird ab Loxone Config 14.5 unterstützt."

Quelle: https://www.loxone.com/dede/kb/mittelwert/

---

## 14. Gleitender Mittelwert

Berechnet den gleitenden Durchschnitt eines kontinuierlichen analogen Eingangssignals.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Analoger Eingang aus dem der Gleitende Mittelwert gebildet werden soll | ∞ |
| R | Reset | Deaktiviert die Mittelwertbildung. Ausgang (Avg) ist gleich dem Wert am Eingang (V). | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Avg | Average | Mittelwert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | 0/1 | 0 |
| C | Polling cycle | Bestimmt in welchem Zeitabstand der Eingangswert abgefragt wird. | s | 0...∞ | 60 |
| N | Number of readings | Anzahl der Werte, die für die Mittelwertbildung herangezogen werden. | – | 0...1000 | 60 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/gleitender-mittelwert/

---

## 15. Analogwahlschalter

Wählt zwischen zwei analogen Eingangswerten basierend auf einem digitalen Steuersignal.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V1 | Value 1 | Wert 1 | ∞ |
| V2 | Value 2 | Wert 2 | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Sel | Select value | 0: (V) = (V1)  1: (V) = (V2) | 0/1 | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/analogwahl-schalter/

---

## 16. Analogwahlschalter 4-fach

Wählt zwischen bis zu vier analogen Eingangswerten basierend auf einem digitalen Steuersignal.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V1-4 | Value 1-4 | Wert 1-4 | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Sel | Select value | 0: (V) = 0 / 1: (V) = (V1) / ... / 4: (V) = (V4) | 0...4 | 1 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/analogwahl-schalter-4-fach/

---

## 17. Analogwertvalidierung

Validiert einen analogen Eingangswert gegen Minimum-, Maximum- und Änderungskriterien.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Zu überprüfender Wert | ∞ |
| En | Enable | Wenn der Eingang angeschlossen ist, wird der Wert nach der Aktivierung des Eingangs und nach Ablauf der Verzögerung **D** ausgegeben. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Validierter Ausgangswert | ∞ |
| E | Error | Ausgang ist aktiv, wenn der Eingangswert ungültig oder **Minimum Change Interval** abgelaufen ist. | 0/1 |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Tmc | Minimum Change Interval | Wenn der Wert > 0 ist, muss sich der Wert des Eingangs in diesem Intervall ändern. Das Intervall wird nicht überprüft, wenn der Eingang **Enable** deaktiviert ist. | s | ∞ | 3600 |
| Min | Minimum Value | Kleinster gültiger Wert. Der Ausgang wird nicht gesetzt, wenn der Eingangswert unter dem Minimum liegt. | - | ∞ | -1000 |
| Max | Maximum Value | Größter gültiger Wert. Der Ausgang wird nicht gesetzt, wenn der Eingangswert über dem Maximum liegt. | - | ∞ | 1000 |
| D | Delay | Der validierte Wert wird nach der konfigurierten Verzögerung am Ausgang gesetzt, wenn der Eingang **Enable** angeschlossen und aktiviert ist. Bei mehreren Wertänderungen während der Verzögerungszeit wird der zuletzt validierte Wert ausgegeben. Bei jeder Aktivierung des Eingangs **Enable** wird die Verzögerung einmal abgewartet. | s | ∞ | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/analogwertvalidierung/

---

## 18. Analogwertüberwachung

Überwacht einen analogen Wert gegen obere und untere Schwellwerte und gibt einen Impuls aus, wenn die Grenzwerte überschritten werden.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Te | 1 when threshold exceeded | 1 wenn Schwellwert überschritten | 0/1 |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| TU | Upper threshold | Oberer Schwellwert | ∞ | 7 |
| TL | Lower threshold | Unterer Schwellwert | ∞ | 3 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/analogwert-ueberwachung/

---

## 19. Schwellwertschalter

Schaltet einen Ausgang um, wenn ein analoger Wert ein und ein anderer Schwellwert unterschreitet.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |
| On | Pulse at rising edge | Gibt einen Impuls bei steigender Flanke aus. | 0/1 |
| Off | Pulse at falling edge | Gibt einen Impuls bei fallender Flanke aus. | 0/1 |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|--------|--------------|--------------|
| Von | Value output (O) turns on | Wert bei dem Ausgang (O) Ein schaltet | \- | ∞ | 5 |
| Voff | Value output (O) turns off | Wert bei dem Ausgang (O) Aus schaltet | \- | ∞ | 1 |
| Pd | Pulse duration | Impulsdauer an den Ausgängen, wenn eine Flanke erkannt wurde. | s | 0...∞ | 1 |
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert beim Speichern in den Miniserver, bei geplanten Neustarts, vor Backups und einmal pro Stunde. Daten werden auf der SD gespeichert. | \- | 0/1 | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/schwellwert-schalter/

---

## 20. Differenzschwellwertschalter

Schaltet abhängig von einem Schwellwert und einer Differenz zum Schwellwert.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| T | 1 depending on the set threshold values. | Schaltet abhängig der eingestellten Schwellwerte. | 0/1 |
| Teon | Pulse on rising edge | Impuls bei steigender Flanke | 0/1 |
| Teoff | Pulse on falling edge | Impuls bei fallender Flanke | 0/1 |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| T | Threshold | Schwellwert | ∞ | 5 |
| D | Difference | Differenz | ∞ | 2 |
| Rem | Remanence input | "Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart." | 0/1 | 0 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/differenzschwellwertschalter/

---

## 21. Rampensteuerung

Steigt oder fällt linear zu einem Zielwert mit einer konfigurierten Schrittweite.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |
| S | Step selection - 0 = (L1), 1 = (L2) | Stufenauswahl - 0 = (L1), 1 =( L2) | 0/1 |
| St | Stop | Wenn 1 (V) = (Sv) | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |
| Sv | Start value | Wenn 1 (V) = (Sv) | ∞ | 5 |
| Sts | Step size | (V) wird alle 100 ms um diesen Wert geändert, bis der Zielwert erreicht ist. | 0...∞ | 1 |
| L1 | Step 1 | Stufe 1 | ∞ | 7 |
| L2 | Step 2 | Stufe 2 | ∞ | 3 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/rampensteuerung/

---

## 22. Pulsweitenmodulator

Wandelt einen analogen Eingangswert (0...10) in ein PWM-Signal (Pulse Width Modulation) um.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | 0...10 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| PWM | PWM output | PWM Ausgang | 0/1 |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| P | Period | Periode | s | 0...∞ | 1 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/pulsweiten-modulator/

---

## 23. Stepper

Setzt einen Ausgangswert schrittweise hoch oder runter.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Step | Schritt | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Set value | Gesetzter Wert | ∞ |

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand wird gespeichert: beim Speichern in den Miniserver, bei geplanntem Neustart, vor Backup, einmal pro Stunde. Daten werden auf SD gespeichert. | 0/1 | 0 |
| Dir | Direction | 0 = auf, 1 = ab | 0/1 | 0 |
| Sts | Step size | Schrittweite | ∞ | 1 |
| M | Maximum | Maximum von Ausgang (V) | ∞ | 10 |

**Eigenschaften** [BELEGT]
[nicht vorhanden]

**Fallstricke** [BELEGT]
[nicht vorhanden]

Quelle: https://www.loxone.com/dede/kb/stepper/

---

## Zusammenfassung

**Recherche abgeschlossen: 23/23 Bausteine erfasst**

Alle Bausteine wurden aus den offiziellen Loxone-Dokumentationsseiten recherchiert. Die Kennzeichnung [BELEGT] weist auf wörtliche Übernahmen aus der Loxone Knowledge Base hin.

**Besonderheiten:**
- Alle Kürzel wurden exakt wie in der Original-Dokumentation übernommen
- Remanenz-Parameter sind bei mehreren Bausteinen vorhanden (Min/Max seit Reset, Gleitender Mittelwert, Analogwertüberwachung, Schwellwertschalter, Differenzschwellwertschalter, Rampensteuerung, Stepper)
- Der "Off / Lock" Eingang findet sich bei mehreren Bausteinen (MinMax, Analogwahlschalter, Analogwahlschalter 4-fach, Analogwertüberwachung, Rampensteuerung, Pulsweitenmodulator, Stepper)
- Der Formel-Baustein bietet die umfassendste Konfigurierbarkeit mit verschiedenen mathematischen Funktionen
- Viele Bausteine haben keine separaten "Eingänge"-Tabellen in der Original-Dokumentation, sondern nutzen Parameter für die Eingangswerte
