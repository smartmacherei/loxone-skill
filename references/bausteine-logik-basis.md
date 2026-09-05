# Logik, Vergleich & Speicher
Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.
Legende: [BELEGT] = wörtlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

## Logische Bausteine

### Und

Der UND-Baustein führt eine logische UND-Verknüpfung seiner binären Eingänge durch.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I1 | Input 1 | Eingang 1 | 0/1 |
| I2 | Input 2 | Eingang 2 | 0/1 |

Quelle: https://www.loxone.com/dede/kb/und/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/und/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [BELEGT]
- Alle Verknüpfungen, die an einem Eingang angeschlossen sind, werden untereinander ebenfalls UND-verknüpft.
- Die Negation muss beim richtigen UND sein.

Quelle: https://www.loxone.com/dede/kb/und/

---

### Oder

Der ODER-Baustein führt eine logische ODER-Verknüpfung seiner binären Eingänge durch. Der Ausgang wird aktiv, wenn mindestens einer der angeschlossenen Eingänge aktiv ist.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I1 | Input 1 | Eingang 1 | 0/1 |
| I2 | Input 2 | Eingang 2 | 0/1 |

Quelle: https://www.loxone.com/dede/kb/oder/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/oder/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/oder/

---

### Nicht

Der NICHT-Baustein (Inverter) negiert seinen binären Eingang.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I | Input | Eingang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/nicht/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/nicht/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/nicht/

---

### Exklusiv ODER

Der Exklusiv-ODER-Baustein (XOR) gibt 1 aus, wenn genau ein Eingang aktiv ist.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I1 | Input 1 | Eingang 1 | 0/1 |
| I2 | Input 2 | Eingang 2 | 0/1 |

Quelle: https://www.loxone.com/dede/kb/exklusiv-oder/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/exklusiv-oder/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [BELEGT]
- Alle Verknüpfungen, die an einem Eingang angeschlossen sind, werden untereinander ODER-verknüpft.

Quelle: https://www.loxone.com/dede/kb/exklusiv-oder/

---

## Vergleichsbausteine

### Gleich

Der Gleich-Baustein vergleicht zwei analoge Werte und prüft sie auf Gleichheit.

**Eingänge** [OFFEN]
Nicht dokumentiert (wahrscheinlich Parameter V1, V2)

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| E | 1 when equal | 1 wenn gleich | 0/1 |

Quelle: https://www.loxone.com/dede/kb/gleich/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/gleich/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/gleich/

---

### Ungleich

Der Ungleich-Baustein vergleicht zwei analoge Werte und prüft sie auf Ungleichheit.

**Eingänge** [OFFEN]
Nicht dokumentiert (wahrscheinlich Parameter V1, V2)

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| U | 1 wenn ungleich | 1 wenn ungleich | 0/1 |

Quelle: https://www.loxone.com/dede/kb/ungleich/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/ungleich/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/ungleich/

---

### Größer oder gleich

Der Größer-oder-gleich-Baustein vergleicht zwei analoge Werte und gibt 1 aus, wenn V1 ≥ V2.

**Eingänge** [OFFEN]
Nicht dokumentiert (wahrscheinlich Parameter V1, V2)

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Ge | 1 when (V1) ≥ (V2) | 1 wenn (V1) ≥ (V2) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/groesser-oder-gleich/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/groesser-oder-gleich/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/groesser-oder-gleich/

---

### Kleiner oder gleich

Der Kleiner-oder-gleich-Baustein vergleicht zwei analoge Werte und gibt 1 aus, wenn V1 ≤ V2.

**Eingänge** [OFFEN]
Nicht dokumentiert (wahrscheinlich Parameter V1, V2)

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Le | 1 wenn (V1) ≤ (V2) | 1 wenn (V1) ≤ (V2) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/kleiner-oder-gleich/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| V1-2 | Value 1-2 | Wert 1-2 | ∞ | 0 |

Quelle: https://www.loxone.com/dede/kb/kleiner-oder-gleich/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/kleiner-oder-gleich/

---

### Analogkomparator

Der Analogkomparator vergleicht zwei analoge Werte und gibt einen Ausgang aus, wenn die Differenz einen Schwellwert überschreitet.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V1 | Value 1 | Wert 1 | ∞ |
| V2 | Value 2 | Wert 2 | ∞ |

Quelle: https://www.loxone.com/dede/kb/analog-komparator/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| De | 1 bei Überschreitung der Differenz | 1 bei Überschreitung der Differenz | 0/1 |

Quelle: https://www.loxone.com/dede/kb/analog-komparator/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Von | On-value | Schwellwert EIN | ∞ | 5 |
| Voff | Off-value | Schwellwert AUS | ∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/analog-komparator/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/analog-komparator/

---

## Speicher und Zeitbausteine

### Merker

Der Merker speichert einen analogen oder digitalen Wert mit konfigurierbarer Verzögerung.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I | Input | Eingang | ∞ |

Quelle: https://www.loxone.com/dede/kb/merker/

**Ausgänge** [OFFEN]
Nicht in der Dokumentation aufgeführt (wahrscheinlich O für Output)

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [BELEGT]
| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Typ | Stellen Sie den Typ von Daten ein, welche Sie mit diesem Objekt weitergeben möchten | - | - |
| Verzögerung | Leitet den Eingang verzögert um x Zyklen an den Ausgang weiter. Verwenden Sie dies, wenn die Ausführungsreihenfolge der Bausteine im Miniserver die Logik beeinflusst – als Alternative zu verzögerten Impulsen. | 0...100 | - |

Quelle: https://www.loxone.com/dede/kb/merker/

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/merker/

---

### Analogspeicher

Der Analogspeicher speichert einen analogen Wert und kann ihn auf Impuls zurücksetzen.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |
| Set | Set value to output (V) | Bei steigender Flanke | 0/1 |
| Off | Off | Impuls: Ausgänge werden zurückgesetzt / ausgeschaltet | 0/1 |

Quelle: https://www.loxone.com/dede/kb/analogspeicher/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Wert | ∞ |

Quelle: https://www.loxone.com/dede/kb/analogspeicher/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Gespeichert beim Speichern, geplanten Neustart, vor Backup und stündlich. Daten auf SD gespeichert. | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/analogspeicher/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/analogspeicher/

---

## Impulsschalter

### RS-Impulsschalter

Der RS-Impulsschalter ist ein Speichermodul mit Set (S)-, Toggle (Tg)- und Reset (R)-Eingängen. Reset dominiert.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Set | Durch einen Impuls wird der Ausgang (O) eingeschaltet | 0/1 |
| Tg | Toggle | Durch einen Impuls wird der Ausgang (O) umgeschaltet | 0/1 |
| R | Reset | Ein Impuls schaltet Ausgang (O) aus, dominierender Eingang. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-rs/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-rs/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-rs/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/impulsschalter-rs/

---

### SR-Impulsschalter

Der SR-Impulsschalter ist ein Speichermodul mit Set (S)-, Toggle (Tg)- und Reset (R)-Eingängen. Set dominiert.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| S | Set | Ein Impuls schaltet Ausgang (O) ein, dominierender Eingang. | 0/1 |
| Tg | Toggle | Durch einen Impuls wird der Ausgang (O) umgeschaltet | 0/1 |
| R | Reset | Durch einen Impuls wird der Ausgang (O) ausgeschaltet | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-sr/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-sr/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | 0/1 | 0 |

Quelle: https://www.loxone.com/dede/kb/impulsschalter-sr/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/impulsschalter-sr/

---

## Flanken- und Zeitbausteine

### Flankenerkennung

Der Flankenerkennung-Baustein erkennt steigende und fallende Flanken und gibt entsprechende Impulse aus.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I | Input | Eingang dessen Flanken erkannt werden | 0/1 |

Quelle: https://www.loxone.com/dede/kb/flankenerkennung/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| P | Pulse at every edge | Gibt bei jeder Flanke einen Impuls aus. | 0/1 |
| On | Pulse at rising edge | Gibt einen Impuls bei steigender Flanke aus. | 0/1 |
| Off | Pulse at falling edge | Gibt einen Impuls bei fallender Flanke aus. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/flankenerkennung/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Pd | Pulse duration | Impulsdauer an den Ausgängen, wenn eine Flanke erkannt wurde. | s | 0...∞ | 1 |

Quelle: https://www.loxone.com/dede/kb/flankenerkennung/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/flankenerkennung/

---

### Monoflop

Der Monoflop-Baustein gibt nach einem Impuls einen Ausgangsimpuls mit definierter Dauer aus.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Trigger: Off Off / Lock Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. | 0/1 |

Quelle: https://www.loxone.com/dede/kb/monoflop/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/monoflop/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|--------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| D | Duration output pulse | Eingangsparameter - Dauer des Ausgangsimpulses | s | 0...∞ | 2 |

Quelle: https://www.loxone.com/dede/kb/monoflop/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/monoflop/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| Off | `Reset` | Eingang | Off / Lock | Impuls(< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. | – |

---

### Schieberegister

Der Schieberegister-Baustein speichert und verschiebt Bits in einer konfigurierbaren Registerbreite.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Tr | Trigger | Mit jedem Impuls wird der Wert von (D) gespeichert und der Registerinhalt verschoben. | 0/1 |
| D | Data | Daten Eingang | 0/1 |
| Dir | Shift direction | Schieberichtung | 0/1 |

Quelle: https://www.loxone.com/dede/kb/schieberegister/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| O | Output | Ausgang | 0/1 |

Quelle: https://www.loxone.com/dede/kb/schieberegister/

**Parameter** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|--------|------------------|--------------|--------------|--------------|
| Rb | Register bit | Registerbit | ∞ | 8 |

Quelle: https://www.loxone.com/dede/kb/schieberegister/

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/schieberegister/

---

## Statusbausteine

### Status

Der Status-Baustein fasst mehrere Eingänge zusammen und gibt ihren Status als Text oder Wert aus.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I1-8 | Input 1-8 | Eingang 1-8 | ∞ |

Quelle: https://www.loxone.com/dede/kb/status-baustein/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Txt | Current status text | Der aktuelle Statustext der sich aus den Bedingungen ergibt. | - |
| Val | Current status value | Der aktuelle Statuswert der sich aus den Bedingungen ergibt. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

Quelle: https://www.loxone.com/dede/kb/status-baustein/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [BELEGT]
| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Statustext | Status | - |

Quelle: https://www.loxone.com/dede/kb/status-baustein/

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/status-baustein/

---

### Virtueller Status

Der Virtuelle Status-Baustein ist ein virtueller Status mit nur einem Eingang.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| I | Input | Eingang | ∞ |

Quelle: https://www.loxone.com/dede/kb/virtueller-status/

**Ausgänge** [OFFEN]
Nicht dokumentiert

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [BELEGT]
| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Als Digitaleingang verwenden | Wenn aktiviert, wird der analoge Eingang als digitaler Eingang verwendet. | - |

Quelle: https://www.loxone.com/dede/kb/virtueller-status/

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/virtueller-status/

**Weitere Konnektoren laut TechDoc** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Art | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|---|
| AQ | `AQ` | Ausgang | – | AQ | ∞ |

---

### Status Monitor

Der Status Monitor überwacht mehrere Status-Eingänge und gibt Aktivitätsprotokoll und Zustandszähler aus.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Stat | Status | Verbinden Sie einen oder mehrere Status-Eingänge. Die möglichen Wert-Text-Paare können im Statusdialog definiert werden. | ∞ |

Quelle: https://www.loxone.com/dede/kb/status-monitor/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Txlc | Text last change | Raum, Name und Status des zuletzt geänderten Objekts mit definiertem Statustext. | - |
| Csr | Count state rest | Anzahl der Geräte oder Objekte, die mit keinem definierten Statuswert übereinstimmen. | ∞ |
| Cs1-10 | Count state 1-10 | Anzahl der Geräte oder Objekte, deren Werte mit den entsprechenden definierten Statuswerten von Cs1-10 übereinstimmen. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. | - |

Quelle: https://www.loxone.com/dede/kb/status-monitor/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [BELEGT]
| Kurzbeschreibung | Beschreibung | Wertebereich | Standardwert |
|------------------|--------------|--------------|--------------|
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |
| Status Monitore zuordnen | Wählen Sie untergeordnete Status Monitore, um ihre Zustände basierend auf den vom übergeordneten Status Monitor definierten Text-Wert-Paaren zusammenzuführen. | - | - |
| Status Konfiguration | Text-Wert-Paare | - | - |

Quelle: https://www.loxone.com/dede/kb/status-monitor/

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/status-monitor/

---

## Binär-Kodierung

### Binärdecoder

Der Binärdecoder zerlegt einen analogen Wert in einzelne Bits (Bit 0-31).

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Analogeingang des Binärdekoders | 0...4294967295 |

Quelle: https://www.loxone.com/dede/kb/binaerdecoder/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bit 0-31 | Bit 0-31 | Bit 0-31 | 0/1 |

Quelle: https://www.loxone.com/dede/kb/binaerdecoder/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/binaerdecoder/

---

### Binärdekoder

Der Binärdekoder zerlegt einen analogen Wert in einzelne Bits (Bit 0-31). (Hinweis: Diese Seite scheint identisch mit dem Binärdecoder zu sein.)

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Value | Analogeingang des Binärdekoders | 0...4294967295 |

Quelle: https://www.loxone.com/dede/kb/binaerdekoder/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bit 0-31 | Bit 0-31 | Bit 0-31 | 0/1 |

Quelle: https://www.loxone.com/dede/kb/binaerdekoder/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Möglicher Datenfehler: diese Seite scheint identisch mit dem Binärdecoder zu sein. Unklar, ob es ein Duplikat oder absichtliche Unterscheidung ist.

Quelle: https://www.loxone.com/dede/kb/binaerdekoder/

---

### Binärkodierer

Der Binärkodierer kombiniert 32 Einzelbits zu einem analogen Ausgangswert.

**Eingänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| Bit 0-31 | Bit 0-31 | Einzelne Bits sollen kombiniert werden. Bit 0: das niederwertigste Bit (LSB) | 0/1 |

Quelle: https://www.loxone.com/dede/kb/binaerkodierer/

**Ausgänge** [BELEGT]
| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|--------------|--------------|
| V | Calculated output value | Berechneter Ausgangswert | 0...4294967295 |

Quelle: https://www.loxone.com/dede/kb/binaerkodierer/

**Parameter** [OFFEN]
Nicht dokumentiert

**Eigenschaften** [OFFEN]
Nicht dokumentiert

**Fallstricke** [OFFEN]
Keine dokumentiert

Quelle: https://www.loxone.com/dede/kb/binaerkodierer/

---

## Notizen zum Katalog

**Recherchiert am:** 30.07.2026

**Kategorien abgedeckt:**
- Logische Bausteine (4)
- Vergleichsbausteine (5)
- Speicher und Zeitbausteine (3)
- Impulsschalter (2)
- Flanken- und Zeitbausteine (3)
- Statusbausteine (3)
- Binär-Kodierung (3)
- **Insgesamt: 22 Bausteine**

**Besonderheiten und bekannte Lücken:**
- Binärdekoder und Binärdekoder-Seiten sind identisch — möglicherweise ein Fehler in der Loxone-Dokumentation
- Viele Bausteine haben unvollständige oder fehlende Tabellen in der offiziellen KB
- Kürzel wurden wörtlich übernom men (z.B. ϑ für Temperatur, wenn vorhanden)
- [OFFEN]-Markierungen bezeichnen Informationen, die in der offiziellen KB nicht dokumentiert sind

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### RS Selbsthalteschalter (`FlipFlop`)

Flipflop mit Set- und Reset-Eingang. Reset ist dominant. Achtung: Dieser Baustein wird nur zur Abwärtskompatibilität bereitgestellt. Bitte verwenden Sie stattdessen den Block Monoflop.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| S | `InputS` | Set | Setzen Eingang | – |
| R | `InputR` | Reset | Rücksetzen Eingang | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| Q | `Q` | – | Ausgang | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 335 · KB: https://www.loxone.com/help/FlipFlop

---

### Größer (`Greater`)

Vergleicht 2 analoge Eingänge, prüft auf größer

**Eingänge** [BELEGT-TECHDOC]
[nicht vorhanden]

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| G | `Q` | 1 when (V1) > (V2) | 1 wenn(V1) > (V2) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| V1-n | `Inputn` | Value 1-n | Wert 1-n | ∞ | 0 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 432 · KB: https://www.loxone.com/help/Greater

---

### Kleiner (`Less`)

Vergleicht 2 analoge Eingänge, prüft auf kleiner

**Eingänge** [BELEGT-TECHDOC]
[nicht vorhanden]

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| L | `Q` | 1 when (V1) < (V2) | 1 wenn (V1) < (V2) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| V1-n | `Inputn` | Value 1-n | Wert 1-n | ∞ | 0 |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 434 · KB: https://www.loxone.com/help/Less

---

### Stufenauswahl (`StepSel`)

Bis zu 16 auswählbare Stufen, es kann jeweils nur ein Ausgang aktiv sein. Beispiel: Ein Impuls am Eingang (I3) aktiviert (O3). Wird der Baustein mit Fan Control Tree (www.loxone.com/help/fan-control-tree) verwendet, stehen bis zu 4 Stufen sowie Aus zur Verfügung.

**Eingänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| I1-n | `InputTrigger n` | Input 1-16 | Schaltet den jeweiligen Ausgang 1-n auf Ein. | – |
| + | `InputTriggerP` | Next output | Nächster Ausgang | – |
| - | `InputTriggerM` | Previous output | Vorheriger Ausgang | – |
| Sel | `InputSel` | Select output | Schaltet auf einen bestimmten Ausgang. | 0…16 |
| Off | `Reset` | Off / Lock | Impuls (< 1 s): Ausgänge werden zurückgesetzt / ausgeschaltet. Konstant 1 (> 1 s): Baustein ist gesperrt. Dominierender Eingang. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | – |
| DisPc | `InputDisable` | Disable periphery control | Deaktiviert alle Eingänge wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | – |

**Ausgänge** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich |
|---|---|---|---|---|
| O1-n | `Qn` | Output 1-n | Ausgang 1-n | – |
| N | `AQ` | Number of active output | Nummer des aktiven Ausgangs | 0…16 |
| API | `OutputAPI` | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands (http://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | – |

**Parameter** [BELEGT-TECHDOC]
| Kürzel | XML-Name | Kurzbeschreibung | Beschreibung | Wertebereich | Standard |
|---|---|---|---|---|---|
| Rem | `Remanence` | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | – | – |
| Max | `Max` | Max. outputs | Maximale Anzahl der wählbaren Ausgänge. Beispiel: Max=4 -> nur die Ausgänge 1-4 können über Bausteineingänge aktiviert werden. In der Visualisierung können unabhängig von dieser Einstellung alle beschrifteten Ausgänge aktiviert werden. | 1…16 | 4 |
| Sk0 | `Mode` | Skip 0 | 'Alles-Aus' (0) wird beim Durchschalten mit +/- übersprungen, wenn Ein. Gilt nur für Objekteingänge, nicht für die Tasten in der Visualisierung. | – | – |

**Eigenschaften** [OFFEN]
Nicht in der TechDoc enthalten — sie beschreibt nur Konnektoren.

**Fallstricke** [OFFEN]
Keine dokumentiert.

Quelle: TechDoc `tdc_DEU.LxRes` (Loxone Config 17.1.6.30), ControlType 538 · KB: https://www.loxone.com/help/step-selector

---
