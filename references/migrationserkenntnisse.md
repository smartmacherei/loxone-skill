# Migration: Kalendertemperaturen, AQ2 und Resetpegel

Verifiziert 10.11.2026 mit offiziellen lokalen Dateien aus Loxone Config 17.2.10.21 und den unten verlinkten offiziellen KB-Seiten. Bei Generationenwechseln lesen. Das sind keine automatischen Migrationsregeln für jede Anlage.

## Freie Kalendertemperaturen werden unterstützt

Aus fehlenden Beispielen in Kundenprojekten nicht ableiten, dass die aktuelle IRR nur Komfort/Eco unterstützt. Die aktuelle TechDoc nennt Temperaturmodus 4 „Manuelle Kalendertemperatur“. Das installierte offizielle Webinterface belegt das native Encoding:

- Quelle: `SDcard/web/commonv2.agz`, darin `shared-app.js`, Module 375382 (`IrcFixedSetpoint-Util`), 395671 (Kalendereinträge), 379467 (Dekodierung), 780197 (Temperaturauswahl).
- Feature `IRC_SCHEDULE_SETPOINTS` gilt laut `scripts/scripts1.js` seit Firmware 14.2.6.13.
- Positive Temperatur in Zehntelgrad: `V = ((Math.floor(T * 10) << 8) & 0x00ffff00) | 16 | (heat ? 32 : 0) | (cool ? 64 : 0)`.
- 16 kennzeichnet festen Kalendersollwert, 32 Heizen erlaubt, 64 Kühlen erlaubt. Beispiele nur Heizen: 17 °C → 43568; 15 °C → 38448; 22 °C → 56368.
- Der native Kalender schreibt diesen Wert unverändert als `tempMode`; XML `Timer/Entry/@V` trägt das Kalendermoduswort. Vor Umsetzungen nativen Encoder/Decoder aus dem passenden Versionspaket prüfen, nicht ein neues Entry-Attribut erfinden.
- Negative Temperaturen nicht aus obiger positiver Kurzform verallgemeinern: die offizielle Utility besitzt eigene Vorzeichenbehandlung.

Bei Altprogrammen alte Temperaturen auflösen (Party = Komfort minus TParty, More = Komfort plus TMore, Tiefschlaf absolut), Kalender-/Betriebsmodusspalten samt Reihenfolge erhalten und jeden Zeitpunkt mit der dekodierten neuen Zieltemperatur vergleichen. Fehlendes `Def` getrennt von dokumentiertem Werksdefault behandeln und die verwendete Interpretation benennen. Nicht durch einen simplen numerischen Modus-Shift „migrieren“: Alt-V2 ist Party, neues V2 Gebäudeschutz.

AGZ-Primärquelle für read-only Analyse: 256-Byte-Verzeichniseinträge, Name in den ersten 248 Bytes, danach uint32 little endian Offset und Länge; Nutzdaten der hier untersuchten JS-Einträge gzip. Verzeichnisende über ersten Datenoffset ermitteln; nicht dessen konkrete Zahl einer Installation hart übernehmen. Unbekannte Varianten nicht blind dekodieren.

## Altes AQ2 ist keine unabhängige Raumregelung

`IRoomcontrol` verwendet einen gemeinsamen Raum-Istwert und Sollwert. Seine zwei analogen Heizausgänge heißen Bereich 1 (`AQ`) und Bereich 2 (`AQ2`); daraus folgen keine zwei unabhängigen Temperatursollwerte.

Die [offizielle alte Beschreibung](https://www.loxone.com/frfr/kb/controleur-de-piece-intelligent/), Abschnitt „Zones de chauffage“, beschreibt AQ2 außerhalb der Aufheizphase als halben AQ-Wert und bei AQ=100 % ebenfalls 100 %. Das kann die Ansteuerung eines zweiten Stellantriebs deutlich verändern. Der genaue Wert während der Aufheizphase wird dort nicht vollständig festgelegt; eine angenommene Nachbildung deshalb nicht als bewiesene Laufzeitgleichheit ausgeben.

Neue `HeatIRoomController2.AQh2` sind dagegen Heizquellenausgänge. Nicht allein aufgrund der Ziffer 2 umverdrahten. Erst alte physische Verbraucher verfolgen, benötigte Kennlinie/Phasenfunktion bestimmen und die konkrete Abbildung belegen. Auch keine zusätzlichen Raumregler mit unabhängigen Sollwerten erfinden.

Das aktuelle `Qb` ist laut TechDoc **Vorbereitungsphase ODER Soll-Ist-Abstand >1,5 °C**; es ist kein bewiesen identisches Signal zur alten reinen Aufheizphase. APC-Ereignis 469007 nutzt `prepareState`. Für APC-Control-Events setzt der native Serializer eine Zustands-UUID aus `control.states[...]` sowie `controlUUID`; die Objekt-UUID nicht ungeprüft als Zustands-UUID einsetzen. An zwei passenden nativen 57-Port-/V178-Reglern wurde durch Abgleich mit einer gespeicherten LoxAPP3-Struktur `states.prepareState = SpStates.split(',')[2]` belegt. Das ist ein Versions-/Vorlagenbeleg, keine allgemeine Garantie für jede SpStates-Liste. Eine APC-Phasenbrücke braucht zusätzlich einen geprüften Zustandsabgleich bei Start und ein tatsächlich ansteuerbares Ziel; Native-XML-Beleg und Laufzeitprüfung getrennt ausweisen.

## Resetwirkung vollständig nachlesen

Die kurze alte TechDoc-Tabellenzeile kann unvollständig sein. Bei Licht bestätigt der [offizielle Gen1-Grundtext](https://www.loxone.com/plpl/kb/sterownik-oswietlenia-1-generacji/), dass aktives R die Ausgänge AQ1–AQ12/AQ auf null hält. Daher ist eine bestehende Dauerquelle nicht automatisch eine neue Dauersperr-Regression von LC2. Quelle, Polarität und Pulsdauer bis zum Ursprung verfolgen, bevor aus einem Pegel ein Impuls gemacht wird.

Bei aktueller IRR beendet Off <200 ms nur Eingangstimer; UI-Timer bleiben bestehen. Eine Migration des alten Resets benötigt zusätzlich die nachgewiesene native Aktion `469105 / stopoverride`, wenn das bisherige Beenden von UI-Temperaturtimern erhalten werden soll.

## Zahlen und Vorgaben

Die deutsche offizielle TechDoc enthält z.B. `Default="22,5"`, Projekt-XML `Def="22.5"`. Vor numerischem Vergleich Dezimalkomma normalisieren. Andernfalls entstehen zahlreiche falsche Defaultabweichungen. Leere Werte, unbekannte Defaults und nicht serialisierte Werte nicht still als gleichwertige Zahlen behandeln.

Aktuelle IRR `TSaveL/TSaveU` haben laut TechDoc und Webapp-Eingabefeld Minimum 0,5 K. Das beweist die dokumentierte Eingabegrenze, aber noch keine konkrete Firmware-Reaktion auf alte XML-Werte 0 oder negative Offsets. Solche Werte weder still auf 0,5 begrenzen noch als erfolgreich übernommen ausgeben. Originalwert und fehlendes Def getrennt erhalten, effektiven Sollwert prüfen und die native Annahme beziehungsweise Begrenzung als offen benennen, solange kein Laufzeitbeleg vorliegt.


## Unabhängige Funktionskontrolle nach einer Migration

Ein vollständiger Vorher-/Nachhervergleich muss getrennt nachweisen: gespeicherte Daten, Anschlüsse, aktuelle Funktion und spätere Bedien-/Parameterkopplungen. Objektzahlen, gültige Referenzen und übereinstimmende Szenenwerte allein reichen nicht. Den Prüfstand über SHA256 fixieren und jede erhaltene, ergänzte und entfernte C-UUID in einer Kontrollliste abdecken. Die Kontrolle unabhängig von den Transformationsfunktionen gegen die tatsächlichen Dateien ausführen.

- Licht: alle Szenennamen/UUIDs/Kreiswerte/Typflags/Move-/Mix-/Skip-/ReadOnly-Merkmale, feste Auswahl und Einzel-/Doppel-/Dreifach-/Langfunktionen prüfen. Erhaltene Szenenwerte ersetzen keine verlorene Langtaster-Lernfunktion. Neue Mehrfachklickadapter bis zu ihren End-Eingängen verfolgen: Set/Reset ist anders als Toggle/Zähler/Versand.
- Gleicher Parametername/Wert bedeutet keine gleiche Semantik. Alt-Ti und neu-Pto unterscheiden sich: Pto kann ab letzter Bewegung statt ab Ausschalten laufen. Ein neuer harter Lichttimer über Reset kann zusätzlich 2C/Raum-Aus und damit Audio-/Heiztimerfolgen auslösen; diese Wirkung ausdrücklich kontrollieren.
- Klima: Heiz- UND Kühlkalender einschließlich leerer Betriebsmodusspalten und DefValue vergleichen. Wird nur TimerHeat nach M5 übernommen, ist ein separater TimerCool damit nicht erhalten. Physisch unbenutzte Kühlausgänge beweisen keinen Erhalt des Bedien-/Temperaturplans.
- Absolute Kalendersollwerte erhalten heutige Temperaturen, aber nicht automatisch alte relative Kopplungen an TComfort/TParty/TMore. Zusätzlich prüfen, was bei später geänderter Komforttemperatur geschieht.
- Verbundenes AMode kann die freie App-Moduswahl unterdrücken. Feste Monatsgrenzen ersetzen keine fortbestehende Kopplung an globale Heiz-/Kühlperioden. Sowohl heutigen Jahresverlauf als auch spätere Bedien-/Kalenderänderung prüfen.
- Bei Parametergrenzen verbundene Quellen verfolgen. Explizite Constant.AnalogConstant → InputRef.AI/AQ und rein statische Rechenpfade sind ggf. auflösbar; dynamische Werte bleiben unbekannt. Ein lokales Def ist bei angeschlossener Quelle kein belegter effektiver Wert. Rolle Parameter und Grenzen aus offizieller TechDoc auflösen, Dezimalkomma normalisieren.
- ACL/Visu/Remanenz, Hardwarekanäle/Kennlinien, Ausgangsverbraucher, invertierte Kontakte und native Zusatzparameter vollständig kontrollieren. Nicht serialisierte Defs und unbekannte WF-Bitsemantik als Nachweisgrenze ausweisen.

Belegte Abweichung, bewusst gewünschte Änderung, Altbestandsproblem und offene Laufzeitannahme getrennt benennen. Einen Dateistand mit solchen Abweichungen nicht pauschal als funktionsgleich freigeben. Allein ein bestandener Heizplanvergleich ist kein Nachweis für sämtliche Betriebszeiten.


## Funktionsfähigkeit vor Migrationsgrenzen prüfen

Ein fehlender Anschluss oder ein anderer Dialog beweist keine entfallene Funktion. Erst aktuelle offizielle Bausteindokumentation, Betriebsmodi und passende native Strukturen prüfen. Wenn der Nutzer neue Bausteine verlangt, die Migration nicht durch Rückkehr zu Gen1 als erledigt ausgeben. Ein Zwischenstand mit offenen Funktionen bleibt ausdrücklich Prüfstand.

Die offiziellen [Betriebsmodi](https://www.loxone.com/dede/kb/betriebsmodi/) lassen sich über Logik oder Betriebszeiten aktivieren. Saison UND ursprünglicher Kalendermodus können als zusätzliche native Betriebsmodi getrennte Heiz-/Kühlspalten innerhalb eines neuen M5-Kalenders abbilden. Das ist ein möglicher nativer Ansatz, keine automatische 1:1-Migration: ursprüngliche Spaltenprioritäten, Fallback-Wochentage, Richtungssperre, manuelle App-Moduswahl und Saisonlücken separat prüfen. Nicht alle Komfort-/Eco-Einträge pauschal in Festtemperaturen umwandeln; damit würde die spätere Parameterkopplung verloren gehen.

LC2 unterstützt nach dem offiziellen [Structure File V17.0, S.98](https://www.loxone.com/enen/wp-content/uploads/sites/3/2026/04/1700_Structure-File.pdf) `learn/{moodId}/{moodName}`. Die aktuelle Webapp verwendet den aktuellen Namen aus moodList; ein optionaler Name ist nicht dokumentiert. Die [Gen1-Anleitung](https://www.loxone.com/plpl/kb/sterownik-oswietlenia-1-generacji/) beschreibt Halten der Szenentaste für fünf Sekunden und anschließendes Ausschalten als Bestätigung. Beim Ersatz daher den aktuellen gewünschten Lichtzustand bis zum Lernen bewahren: sofortiges changeto auf Tastendruck kann ihn vorher zerstören. Kurz-, Doppel-, Dreifach- und Langfunktion sowie Namensänderungen prüfen. Keine erfundene APC-descID für learn verwenden.

Die alte Ti-Beschreibung sagt nach Ausschalten ohne Einschränkung auf manuelle Auslöser. Nur-manuell ist deshalb keine belegte Originalregel. Ein externer fester Ti-Timer ab echtem Ein-nach-Aus-Übergang ist eine begründete Auslegung, aber kein beobachteter Firmware-Nachweis. Anfängliches Aus darf keinen solchen Übergang vortäuschen; negative Stimmungswerte für benutzerdefinierte/gemischte Beleuchtung zählen als Ein. Neue Bewegung darf den festen Timer nicht neu starten.


## Lichtsteuerung Gen 1 → LightController2 (verifiziert 22.11.2026, Config 17.3.11.12, Kundenprojekt, 47 Stück)

Umgesetzt über den Config MCP ([config-mcp.md](config-mcp.md)), je Baustein ein `code_run`: neuen Baustein auf
derselben Seite anlegen, Eigenschaften übertragen, jede Verbindung auf denselben Konnektorschlüssel umhängen,
alten löschen, Position übernehmen, Stimmungen per `set_block_data` schreiben, im selben Skript nachlesen.
Ergebnis: 378 Verbindungen, 376 Szenen / 4.512 Werte ohne Abweichung; Config-Prüfung 0 Fehler.

**Konnektorschlüssel sind gleich** (`I1`–`I8`, `Reset`, `Sel1`–`Sel8`, `EnMove`, `Move`, `On`, `Alarm`,
`Brightness`, `InputDisable`, `Select`, `InputTriggerUp/Down`, `AQ1`–`AQ12`, `Scene`, `OutputReset`,
`OutputResetAll`, Parameter `MoveScene`, `Min` …). Ohne Gegenstück: `I9`–`I12`, `Gesture`, `Learntime`.

**Parameter (Eigenschaftsfeld-Kürzel):** Tdc→Tdc, SI→Sts, ST→Str, Min→MinBr, Max→MaxBr, W→Dm, L→Lv, TH→Moet,
Ti→Pto, MS→Pm, MT→Met, Ra→Ao, Ta→Afi, T→Brt, Ba→MaxAbr, Rem→Rem. Verdrahtete Parameter lesen sich als
„durch Logik gesetzt“ (String) — nicht schreiben, Verbindung umhängen.

**Szenenwerte:** Gen 1 speichert Dimmwerte als `0x10000000 + Prozent` (268435556 = 100 %, 268435481 = 25 %),
Schaltwerte als 0/1. `LightController2.values` erwartet je `outputTypes`: Schalter 0/1, Dimmer Prozent, Farbe
`bbbgggrrr`, **Maximum 268435455** — Gen-1-Rohwerte 1:1 kopieren ist falsch (so geschehen im Prüfstand V4
vom 10.11.2026). Bewegungsszene: Gen 1 `LightsceneC Move="true"` → `movement: true` plus
`operatingModeMoods [{operatingMode: 778, mood, action: "switchToIfOff"}]`.

**Stimmungs-IDs = alte Szenennummern** (Szene n → `moodId` n, `connectorId` 11+n = T5/n). Damit passen
Schaltuhren/Analogwerte an `MoveScene`→`Pm` ohne Umrechnung. `connectorId` ist der Index des Konnektors in
der Co-Reihenfolge (`Reset` = 11 → „Aus“, `Sel1` = 12 …). Leere unbenannte Szenen behalten, aber
`hiddenInVisu`/`skipNext` setzen.

**Lichtkreise:** `circuitNames` leer = Kreis unbenutzt (wird beim Speichern verworfen!). Namen aus `NameAI0–11`,
sonst aus dem angeschlossenen Ausgang, Bit in `customCircuitNames` setzen. `outputTypes` stempelt der Baustein
aus dem angeschlossenen Aktor → **erst Ausgänge verbinden, dann Werte schreiben**; Typ und Werte nie in
derselben Schreiboperation ändern.

**Verhaltensunterschiede, die gemeldet werden müssen:** kein Szenenlernen per 5-s-Taster mehr (nur App);
T5/n schaltet beim 2. Impuls innerhalb 30 s zur nächsten Stimmung, Langklick mischt ein; **T5/n reagiert nur
auf T5-Code 4** → digitale Quellen brauchen `Mult ×4` (bei mehreren Quellen vorher `Or`, siehe config-mcp.md
Falle 1); Pto: jede Bewegung startet die Sperre neu (Ti tat das nicht); DisP schaltet bewegungsgeschaltetes
Licht nach Moet aus.
