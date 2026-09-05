⚠️ **WARNUNG: NICHT OFFIZIELLE DOKUMENTATION**

Diese Datei sammelt praktisches Wissen aus Loxone-Community-Quellen (LoxWiki, Loxforum).
Das ist **KEINE offizielle Loxone-Dokumentation** und kann veraltet oder fehlerhaft sein.
Jede Aussage wird mit Quelle und Kennzeichnung belegt — vertrau auf keine unmarkierte Zeile.

---

# Loxone Community-Praxiswissen — Bausteine, Bugs, Workarounds

## Intelligente Raumregelung (IRR)

### Aufheizphase zu früh (bekanntes Verhalten)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1520762947/Intelligente+Raumregelung

Die Aufheizphase startet in den ersten Tagen nach Erstinbetriebnahme wesentlich zu früh.
**Workaround:** Mind. 7 Tage beobachten, bevor Konfigurationsfehler angenommen werden.
Der Algorithmus braucht historische Daten; anfangs wird mit nur 0,1 °C/h Aufheizrate gerechnet.

### Keine Kühlvorphase
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1520762947/Intelligente+Raumregelung

Das System heizt mit Vorlaufzeit, um Sollwerte pünktlich zu erreichen, leitet aber KEINE Kühlvorphase ein.

### Komforttimer-Neustart-Bug
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1520762947/Intelligente+Raumregelung

Wenn Komforttimer in der Visualisierung aktiviert ist, endet dieser nach Miniserver-Neustart.

### Kühlmodus aktiviert sich nicht / bleibt aktiv
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/390867-intelligente-raumregelung-gibt-k%C3%BChlen-nicht-frei

Benutzerbericht: Temp. 24 °C, Kühl-Komfort 23 °C, Modus Auto → nichts passiert. 
Erst im Modus "Kühlen nur" funktioniert es.
**Workaround:** Miniserver-Neustart half teilweise; auch auf HC1-Ausgang prüfen (muss ≠ 0 sein).

### Kühlmodus hält nicht an, wenn Sollwert erreicht
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/438213-intelligente-klima%C2%ADanlagen%C2%ADsteuerung-ausschalten-bei-erreichen-der-temperatur

Symptom: Klima kühlt weiter, obwohl Solltemp. schon erreicht.
**Workaround:** HC1-Ausgang mit Verzögerung (Laufzeitschalter 2 min) entprellen, um stabile Aus-Befehle zu geben.

### Fensterkon­takt invertiert
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/43728-intelligente-raumregelung-t%C3%BCrkontakt-auf-lw-problem

Einige Fensterkontakte senden invertierte Signale.
**Workaround:** NOT-Gatter vor den Eingang schalten.

---

## Automatikbeschattung / Automatikjalousie

### Beschattung-Aus-Signal fehlt
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696659/Automatikjalousie

**Dokumentierte Limitation:** Das Automatikmoddul kann das Ende der Beschattung (AS off) nicht selbst implementieren.
Wenn Schlechtwetter vorüber ist, bleiben Jalousien trotzdem zu.
**Workaround:** Manuelle oder externe Logik zur Freigabe der Jalousien bei Sonnenwendel / Bewölkung bauen.

### Vollfahrt-Befehle (Cu/Cd) unreliabel
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696659/Automatikjalousie

Wenn Visualisierung eine Bewegung startet und gleichzeitig Logik Cu/Cd sendet → Jalousien bleiben stehen.
**Workaround:** Impulse statt Dauerbefehle nutzen; Verzögerungen einbauen.

### Rolljalousie-Visualisierungsfehler (Typ 1)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696659/Automatikjalousie

Typ-1-Jalousien (Rollos): Die Anzeige berücksichtigt nicht die Öffnungszeit der Lamellen.
**Anzeige-Bug:** Zeigt ~60 % Schließung, wenn Rollo wirklich ganz zu ist (Lamellen offen).

### Safety-Shutdown sperrt Jalousien
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696659/Automatikjalousie

Nach Safety-Shutdown (Sp-Eingang) bleiben Jalousien in dieser Position; Automatik bleibt deaktiviert, auch nach Ende der Notbedingung.

### Autopilot-Ma-Parameter funktioniert nicht
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696659/Automatikjalousie

Bug ID 150961003: Parameter "Ma" (Autopilot deaktivieren wenn zu) funktioniert nicht.

---

## Lichtsteuerung

### Licht schaltet mit Schalter-Typ auf 0%
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/340818-lichtsteuerung-v2-lichtkreise-typ-schalter

Wenn Lichtkreis-Typ auf "Schalter" für Nicht-Loxone-Leuchten gesetzt: System schaltet mit 0 % Helligkeit (wird als "aus" interpretiert).

### Szenen per Taster direkt ein/aus schwierig
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/135547-lichtsteuerung-v2-lichtszenen-direkt-mit-einfachem-taster-ein-und-aus

Lichtszenen können nicht direkt mit einfachem Taster geschaltet werden ohne Doppelklick oder Durchschalten durch mehrere Szenen.
**Workaround:** Zusätzliche Logik (NOT-Gatter, Flankenmelder) nötig.

### Präsenz + Helligkeitsschalter-Integration
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/451687-lichtsteuerung-pr%C3%A4senz-automatik-hilfe

Bewegungsmelder (EG-Tiny) an Mo-Eingang: benötigt UND-Gatter.
Helligkeitswert an Br-Eingang: Schwellwerte in Lichtsteuerung setzen (wann Licht an soll).

---

## Bewegungs- & Präsenzmelder

### Keine DIN-Standardisierung (Präsenz vs. Motion)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1516077236/Bewegungs-+Pr+senzmelder

Es gibt keinen verbindlichen DIN-Standard für Präsenz- vs. Bewegungsmelder — Hersteller wählen Bezeichnungen frei.
**Wichtig für Loxone:** Bei Verarbeitung im Miniserver (Sensor-Daten zu Config) sind diese Unterschiede irrelevant.

### Helligkeitssensor: Entscheidung im Miniserver treffen
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1516077236/Bewegungs-+Pr+senzmelder

Die Frage "Licht ein?" kann der Sensor nicht selbst beantworten. Loxone muss den Helligkeitswert verarbeiten.
**Best Practice:** Helligkeitswert ins System führen, Schwellen dort definieren.

### Loxone Motion Sensor Tree (24V)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1522696589/Loxone+Bewegungsmelder+Tree

24V-Oberflächenmelder, Bewegung + Helligkeitssensor, Decken- oder Wandmontage.

### Loxone Motion Sensor Air (24V oder Batterie)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1521975392/Loxone+Bewegungsmelder+Air

Batterie- oder 24V-Oberflächenmelder, Bewegung + Helligkeit.

---

## Alarmanlage

### False-Alarm-Probleme: Bewegungsmelder triggern zu leicht
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/253798-alarmanlage-l%C3%B6st-schon-beim-1-bwm-aus

Alarm löst schon beim 1. Bewegungsmelder aus, obwohl Konfiguration zwei Melder verlangt.

### Sabotage-Alarm bei fehlenden Sirenen
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/257167-loxone-alarmanlage-sabotage-alarm

Alarmbaustein merkt sich aktivierte Sirenen; erkennt, wenn Sirenen fehlen → kann Sabotage-Alarm auslösen.
**Status:** Unklar, ob beabsichtigt oder Bug.

### Zustand-Fehler nach Software-Updates
[COMMUNITY] https://loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/23418-warnung-an-alarmanlagen-nutzer-undefinierter-zustand

Nach Updates kann Alarmbaustein in undefiniertem Zustand verbleiben.
**Workaround:** Miniserver-Neustart.

### Performance-Bug: Verzögerter Toggle nach Update
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/195790-das-neue-loxone-os-10-2-ist-da/page2

Nach Software-Update: Alarmbaustein laggt beim Umschalten scharf/unscharf, Countdown-Anzeige aktualisiert nicht.
**Status:** Gelöst in folgenden Versionen.

### AIR-Melder sendet mehrfach, obwohl Nachlaufzeit gesetzt
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/198007-heute-3-fehlalarme-alarmbaustein-mit-wartezeit-auf-2ten-melder-wie-fehler-finden

Symptom: AIR-Bewegungsmelder triggert mehrfach, obwohl Nachlaufzeit lang gesetzt.
**Mögliche Ursachen:** Melder bekommt neue Settings nicht, oder Bug im Sensor.
**Workaround:** Config neu hochfahren, Melder-Batterie prüfen.

---

## Energiemanager / Eigenverbrauchsoptimierung (EVO)

### Verfügbarkeit nur ab Config 10.0.x.x
[ABGELEITET] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1521975519/Energiemanager+Eigenverbrauchsoptimierung+EVO

Energiemanager-Baustein war bis Config 6.4.xxx aktiv, dann weggelassen, ab 10.0.x.x wieder vorhanden.
**Konsequenz:** Alte Projekte (7.x–9.x) müssen umgestellt werden.

### Funktioniert auch ohne Wechselrichter-Daten
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1521975519/Energiemanager+Eigenverbrauchsoptimierung+EVO

Einfache Verbrauchsoptimierung mit Speichern (Wärmepuffer, Kaltspeicher) funktioniert ohne Inverter-Daten.

### EVO mit Fronius / SolarEdge möglich
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1521975519/Energiemanager+Eigenverbrauchsoptimierung+EVO

LoxWiki hat Dokumentation zur Integration von Fronius- und SolarEdge-Wechselrichtern.

### [OFFEN] Bekannte Performance-Grenzen bei EVO
Keine Community-Berichte zu Performance-Fallen oder Bugs gefunden. Status: [OFFEN].

---

## Programm-Bausteine / Funktionen (PicoC)

### Keine benutzerdefinierten Funktionen möglich
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/186797-functionblock-erstellen-create-custom-function-block

Loxone hat keinen Built-in User-Defined-Function-Block. Jede Logik muss mit vordefinierten Bausteinen verdrahtet werden.
**Workaround:** Komplexe Logik in PicoC-Programm auslagern oder Baustein-Kombos kopieren/multi-instanzieren.

### Logik-Reusability eingeschränkt
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/371052-wiederverwendung-von-logiken

Klassische Funktions-Parametrierung (wie in anderen Programmiersprachen) nicht möglich.
**Praxis-Tipp:** Bewährte Logik-Muster speichern, von Hand neu verdrahten. Oder in einem Read-Only-Backup-Projekt verwalten.

### Best Practice: Schritt-für-Schritt testen
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/11280-brauche-hilfe

Forum-Tipp: Logik nicht spekulativ schreiben, sondern jeden Schritt aufbauen und testen. Mit Vorbausteine "nix kaputtzumachen" — sicherer als Code.

---

## Statusbaustein

### Zeichenketten aus Statusblöcken bauen
[ABGELEITET] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1602650207/Wertanzeige+mit+Zeitstempel

Mehrere Statusbausteine hintereinander: Jeder Block ein Zeichen, wird zur Text-Zeichenkette verkettet.
**Anwendung:** ASCII-Konvertierung, Status-Strings für Visualisierung oder Text-to-Speech.

### Ausgabe: Statustext + Statuswert (0–20)
[COMMUNITY] LoxWiki, Seiten-URL nicht mitprotokolliert — vor Verwendung gegen die offizielle KB-Seite prüfen

Statusbaustein liefert Text (Zeichenkette) und numerischen Wert (0 bis 20).

### Verwendung für Visualisierungen & TTS
[ABGELEITET] (aus Fetch-Ergebnissen)

Statusbausteine u. a. für Loxone-App-Textfeld, Text-to-Speech oder Visualisierungs-Statusanzeige.

### [OFFEN] Bekannte Bugs oder Grenzen
Keine Community-Berichte zu spezifischen Bugs gefunden. Status: [OFFEN].

---

## Formel-Bausteine / Formelsyntax

### Komma statt Punkt als Dezimaltrennzeichen
[COMMUNITY] Loxforum, mehrere Diskussionen — Einzel-URL nicht mitprotokolliert

Formel-Baustein erwartet Komma (German locale): `3,14` nicht `3.14`.

### Integer-Rundungsfehler (Floating-Point-Artefakt)
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/205063-integer-runden

INT() und Int-Funktion runden nicht immer korrekt. 
**Root Cause:** 32-Bit Float speichert z. B. 30 intern als 29.9999999999...
**Workaround:** +0.5 addieren vor INT(): `INT(x + 0.5)` statt `INT(x)`.

### Formel-Fehler bei $ in Variablen
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/127413-frage-formelprogrammierung-in-loxone

"Fehler in Position 2!" beim Verwenden von `$variable` in Formeln.
**Workaround:** $ nicht in Programmierung nutzen (nur in Config-UI).

### Bitweise Fehlerauswertung möglich
[COMMUNITY] https://www.loxforum.com/forum/german/software-konfiguration-programm-und-visualisierung/386452-bitweise-fehlerauswertung

Formel-Bausteine können Bit-Operationen für Fehler-Flags nutzen — schwach dokumentiert, aber möglich.
**Status:** Wenig Community-Tipps verfügbar, experimentell.

---

## Pico / Virtuelle Schalter & Eingänge

### [OFFEN] Verdrahtungs-Best-Practices
Wenig zentralisierte Dokumentation gefunden. Community hat einzelne Tipps in Hardware-Subforen.
Status: [OFFEN] für umfassende Pico-Verdrahtungsrichtlinie.

### Virtuelle Eingänge in Shelly möglich (extern)
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/2076803254/Virtuelle+Eing+nge+in+der+Shelly+anlegen

Nicht Pico-nativ, aber: Shelly kann virtuelle Eingänge erhalten (z. B. per HTTP Boolean.Set).

### Pico-C-Programme für Dekodierung lean
[COMMUNITY] https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1536590990/Home+Assistant

Pico-C kann mit nur 3 Programmblöcken Fehler-Meldungen dekodieren und anzeigen.
**Konzept:** Small, focused PicoC-Snippets sind praktisch.

---

## Zusammenfassung der Kennzeichnungen

| Kürzel | Bedeutung | Vertrauensgrad |
|--------|-----------|-----------------|
| `[COMMUNITY]` | Aus LoxWiki oder Loxforum — **das gilt für jede Zeile dieser Datei** | je nach Alter und Quelle |
| `[ABGELEITET]` | Aus anderen Daten geschlossen, so nirgends nachzulesen | Mittel |
| `[OFFEN]` | Unbekannt, fehlende Info | — |

`[BELEGT]` kommt hier bewusst **nicht** vor — dieses Kürzel ist der offiziellen Loxone-KB
vorbehalten. Wer eine Aussage von hier belastbar braucht, prüft sie gegen die
Baustein-Referenzen (`bausteine-*.md`) und deren Quell-URLs.

**Wichtig:** Community-Berichte (insb. ältere) können sich auf ältere Config-Versionen beziehen. Versionsnummern beim Lesen beachten!

---

## Quellen (alphabetisch)

- [LoxWiki (Atlassian)](https://loxwiki.atlassian.net/wiki/spaces/LOX/overview)
- [Loxforum (deutsch)](https://www.loxforum.com/forum/german/)
- [LoxBerry Wiki](https://wiki.loxberry.de/) *(nicht einzeln durchsucht, aber verfügbar)*

---

**Datei erstellt:** 2026-07-30  
**Last Updated:** [wird bei Bedarf aktualisiert]  
**Wartung:** Bitte neue Community-Erkenntnisse mit Quell-URL und Kennzeichnung hinzufügen.
