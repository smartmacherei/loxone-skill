# Seitenlayout: Blattgrenzen vor und nach dem Umordnen prüfen

## Sichtbarer Befund und belastbare Grenzen

Bei Layoutarbeiten zuerst klären, ob das **gesamte weiße Seitenblatt einschließlich rechter und unterer Kante** sichtbar ist. Bausteine, Referenzen, Notizen oder Leitungen im grauen Außenbereich sind ein Überstand. Eine vergrößerte, beschnittene Ansicht oder eine bestandene XML-/Verbindungsprüfung beweist keine Blattpassung. Herauszoomen verändert die Ansicht, nicht die Blattgröße oder die Objektkoordinaten.

Ein vorhandener Screenshot kann den Überstand bereits belegen. Zur rechnerischen Korrektur die sichtbaren Blattkanten mit mindestens zwei bekannten Objektpositionen aus `Px/Py/Px2/Py2` abgleichen. Ränder und Fußzeile aussparen. Unbekannte Formatnummern oder Maße nicht schätzen und nicht als allgemein verifiziert ausgeben. `Document/@PaperFormat` steht im Projekt; seine numerische Zuordnung zu physischen Maßen ist ohne passenden Nachweis offen. Falls der Blattrand nicht erkennbar ist, diese Grenze ausdrücklich benennen.

**Projektbeleg 10.11.2026, Config 17.2.10.21, PaperFormat=2:** Ein Screenshot mit vollständigem weißen Blatt und vorhandenen Objektkoordinaten erlaubte die konservative Innenfläche `x=384..23040`, `y=384..15360`. Das ist eine für diesen Projekt-/Darstellungsstand belegte Arbeitsfläche mit Rand-/Fußzeilenreserve, keine allgemeine Formatnummerntabelle.

## Direkte Bearbeitung

Die vollständige Koordinatenprüfung direkt aus der Projektdatei durchführen; dafür nicht jede Seite einzeln über die GUI durchklicken. Alle direkten `C`-Kinder jeder Programmseite prüfen, einschließlich InputRef, OutputRef, Merker und Text. Ein vorhandener Screenshot ist zusätzlich der Sichtbeleg, kein Ersatz für den vollständigen Scan.

- Eine neue Ausgabedatei verwenden, wenn das bisherige Projekt noch in Config geöffnet ist. Die im Speicher geöffnete Datei nicht parallel überschreiben.
- Je Objekt das **ganze Rechteck** prüfen: `Px >= links`, `Py >= oben`, `Px2 <= rechts`, `Py2 <= unten`. Nur der Ankerpunkt reicht nicht. Ungültige oder fehlende Rechtecke ausdrücklich melden.
- Raum-/Funktionsabschnitte zusammenhalten, Überschrift oberhalb, auf einem gemeinsamen Raster mit Abstand ausrichten. Bei dichten Seiten kompakter packen; Bausteine nicht einfach verkleinern, denn Config kann native Bausteinmaße beim Öffnen wiederherstellen. Wenn es bei lesbaren nativen Größen nicht passt, das Format oder die Seitenaufteilung bewusst mit dem Nutzer klären.
- Nur Layoutkoordinaten ändern. UUIDs, Miniserver-/Raumseitenzuordnung, Objektgrößen, Konnektoren, Verbindungen, Parameter, Timer, Szenen und Zentralmitglieder erhalten. Bei einer reinen Positionskorrektur bleibt `NumO` unverändert.
- Nachher jede Seite auf Überstände **und rechteckige Überlappungen** prüfen. Vorher-/Nachher-Zahlen pro Seite protokollieren; Verbindungspaare und Nicht-Layout-Inhalte vergleichen. Verbindungsdarstellung/Leitungswege werden von Config erzeugt; ein Rechtecktest beweist deren optische Lesbarkeit nicht.
- Falls anschließend in Config gespeichert wird: dieselben Geometrie- und Inhaltsprüfungen erneut auf der gespeicherten Datei ausführen. Rechnerische Prüfung und aktuelle native Sichtprüfung im Ergebnis getrennt benennen. Ohne erneute Sichtprüfung keine visuelle Freigabe behaupten.

## Wiederholbarer Prüfer

`scripts/blattgrenzen_pruefen.cjs` liest das native XML ohne Attribut-Normalisierung, verändert das Projekt nicht und benötigt nur Node.js. Die vier Grenzen sind explizit anzugeben. Beispiel für den oben belegten Projektstand, als PowerShell-Einzeiler:

```powershell
node 'scripts\blattgrenzen_pruefen.cjs' 'C:\Pfad\Projekt.Loxone' 384 384 23040 15360 'C:\Pfad\Blattpruefung.json'
```

Exitcode `0`: keine Rechtecküberstände, ungültigen Rechtecke oder Überlappungen innerhalb der angegebenen Grenzen. `1`: geometrische Befunde; `2`: fehlende/ungültige Argumente. Ein Überlappungsbefund kann eine absichtliche Notizanordnung sein und muss beurteilt werden; er darf nicht still als geprüft verschwinden. Der Prüfer ersetzt weder die Funktionsprüfung noch die Prüfung der durch Config erzeugten Leitungsführung.
