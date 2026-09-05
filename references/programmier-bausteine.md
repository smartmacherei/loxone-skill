# Programmier-Bausteine: Ablaufsteuerung und Programm (PicoC)

Teil des Loxone-Baustein-Katalogs, aber eigenständig — diese beiden Bausteine sind die einzigen,
in denen **Text statt Verdrahtung** die Logik trägt. Entsprechend anders sehen sie im XML aus,
und entsprechend andere Fallen haben sie.

Legende: `[BELEGT]` = wörtlich/inhaltlich aus der offiziellen KB, Quell-URL dabei ·
`[ABGELEITET]` = geschlossen, nirgends so nachzulesen · `[OFFEN]` = unbekannt, nicht geraten ·
`[VERIFIZIERT]` = an einer echten Projektdatei geprüft, Datum dabei.

XML-Befund verifiziert am **05.08.2026** an `Bestandsprojekt V5.Loxone`, Loxone Config 17.1.7.27,
`ControlList Version 273`, Objektversion `V="175"`.

---

## 1. Welches Werkzeug wofür

Die wichtigste Entscheidung fällt **vor** der ersten Zeile Code. Beide Bausteine sehen mächtig
aus und verleiten dazu, Dinge zu programmieren, die als Gatterlogik kürzer, robuster und
diagnostizierbar wären.

| | **Gatterlogik** (Und/Oder/Schwellwert/Flanke/RS) | **Ablaufsteuerung** (`SequenceController`) | **Programm** (`Code16`, PicoC) |
|---|---|---|---|
| Modell | kombinatorisch, jeder Zweig **jeden SPS-Zyklus** ausgewertet | **ein Programmzähler**, blockiert an `sleep`/`waitcondition` | eigener Task, **asynchron zur SPS** |
| Stark bei | Dauerüberwachung, Verriegelungen, Freigaben | zeitlich gestaffelte Abläufe, Schritt-für-Schritt-Prozesse | String-/Protokollverarbeitung, HTTP, Dateien, Mathe |
| Schwach bei | lange Schrittketten (Wust aus Verzögerungen und Flipflops) | alles, was **gleichzeitig** überwacht werden muss | alles Einfache — Aufwand und Risiko stehen selten dafür |
| Diagnose | Live-View zeigt an jedem Gatter den Zustand | nur „Sequenz N, Zeile M" (`S`/`L`) | nur `Etxt` und das Log-Fenster |
| Risiko bei Fehler | lokal | Sequenz hängt, reagiert auf nichts mehr | **Miniserver-Sicherheitsneustart** [BELEGT] |
| Support | ja | ja | **nein** — „Da dieser Baustein für Entwickler gedacht ist, wird kein Support angeboten." [BELEGT] |

**Die Faustregel:** *Bedingungen* gehören in Gatter, *Abläufe* in die Ablaufsteuerung,
*Fremdformate* in PicoC.

### Der typische Fehlgriff
Eine Feuchte-/Temperatur-/Wetter-Überwachung (Duscherkennung, Lüftungsbedarf, Beschattungs-
freigabe) in eine Ablaufsteuerung zu gießen. Das sind **Zustandsbedingungen**, keine Abläufe.
Während die Sequenz in `sleep 30 s` steht oder auf `waitcondition` wartet, sieht sie
Windwarnung, Regen, Handbedienung und den Feuchteabfall **nicht**. Verriegelungen, die heute
der Fachbaustein selbst mitbringt (`RoofWindow.Protection`, `AutoJalousie.Wa`, `ToiletFan`-
Nachlauf), müsste man von Hand nachbauen — und genau dort passieren die gefährlichen Fehler.

### Wo die Ablaufsteuerung dagegen das richtige Werkzeug ist
Morgen-/Abendszenen mit Staffelung („Bad auf, 20 s später Küche, dann Wohnzimmer nur Lamellen"),
Heimkommen-Szenen, Aufheizprogramme (Sauna), Bewässerungszyklen über mehrere Kreise,
Anwesenheitssimulation, Rückspülroutinen, Dosieranlagen.

**Mischform, die gut funktioniert:** Freigabe und Verriegelung bleiben in der Gatterlogik und
landen auf **einem** Eingang der Ablaufsteuerung (`AI1` via UND). Die Sequenz wartet mit
`waitcondition AI1 == 1` darauf und übernimmt danach nur noch den Takt. So bleibt die
Sicherheitslogik dort, wo sie jeden Zyklus gerechnet wird.
*(Muster aus einem dokumentierten Praxisfall, Chemikaliendosierung Pool — [COMMUNITY], LoxBerry-Wiki.)*

---

## 2. Ablaufsteuerung — `SequenceController`

### XML-Repräsentation [VERIFIZIERT 05.08.2026]

```xml
<C Type="SequenceController" V="175" U="…" Title="Ablaufsteuerung"
   Px="…" Py="…" Px2="…" Py2="…" Cl="141,255,112" Nio="32"
   SpStates="…,…,…"
   CNAME=" ; ; ; … "                                   <!-- 31 Felder, semikolongetrennt -->
   VNAME="value1;value2;value3;value4;value5"
   STEP="500">
  <Co K="AI1"/> … <Co K="AI8"/>
  <Co K="Trigger1"/> … <Co K="Trigger8"/>
  <Co K="ATrigger"/>
  <Co K="Reset"/>
  <Co K="Remanence" Inv="true"/>
  <Co K="Param"/>
  <Co K="AQ1"/> … <Co K="AQ8"/>
  <Co K="OutputCurrSequence"/>
  <Co K="OutputCurrLine"/>
  <Co K="TQ"/>
  <Co K="OutputAPI"/>
  <IoData Cr="…"/>                                     <!-- nur Kategorie, kein Pr = kein Raum -->
  <Display Unit="&lt;v.1&gt;"/>
  <SEQ CFG="" NAM="Sequenz_1"/>                        <!-- eine Sequenz -->
</C>
```

### Konnektor-Mapping XML ↔ Doku

| XML (`Co/@K`) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `AI1` … `AI8` | `AI1-8` | Eingänge 1–8, umbenennbar | E | [ABGELEITET] |
| `Trigger1` … `Trigger8` | `S1-8` | Sequenz 1–8 aktivieren | E | [ABGELEITET] |
| `ATrigger` | `S` | Sequenz per Nummer wählen (0…8) | E | [ABGELEITET] |
| `Reset` | `Off` | Off / Lock — dominierend | E | [ABGELEITET] |
| `Remanence` (`Inv`) | `Rem` | Remanenz | P | [ABGELEITET] |
| `Param` | – | – | E/P | **[OFFEN]** — die KB kennt 19 Eingänge, das XML hat 20 |
| `AQ1` … `AQ8` | `AQ1-8` | Ausgänge 1–8, umbenennbar | A | [ABGELEITET] |
| `OutputCurrSequence` | `S` | aktuell aktive Sequenz | A | [ABGELEITET] |
| `OutputCurrLine` | `L` | aktuelle Programmzeile | A | [ABGELEITET] |
| `TQ` | `TQ` | Textausgang | A | [BELEGT] |
| `OutputAPI` | `API` | API-Konnektor | A | [ABGELEITET] |

Deckung: XML 32 Konnektoren, Doku 31 (19 E/P + 12 A). Die Ausgangsseite ist **1:1 und in gleicher
Reihenfolge**; auf der Eingangsseite bleibt `Param` übrig.

> ⚠️ **Die Doku verwendet `S` zweimal** — einmal als Eingang „Sequenz auswählen", einmal als
> Ausgang „aktuell aktive Sequenz". Im XML sind das `ATrigger` und `OutputCurrSequence`.

### Attribute

| Attribut | Bedeutung | Status |
|---|---|---|
| `STEP` | **Intervall [ms]** zwischen zwei Programmzeilen. KB: 20…1000, Default **500**. Der beobachtete Wert 500 deckt sich mit dem KB-Default. | [ABGELEITET] |
| `VNAME` | Namen der 5 Variablen, semikolongetrennt. Default `value1;…;value5`. | [VERIFIZIERT] |
| `CNAME` | Klartextnamen der umbenennbaren Konnektoren, semikolongetrennt. **31 Felder**, Reihenfolge **identisch mit der `Co`-Reihenfolge**, ohne `OutputAPI`. Leeres Feld = ein Leerzeichen. | **[VERIFIZIERT 05.08.2026]** |
| `Desc` | Beschreibung. Config zeigt sie als **Titelzeile des Sequenz-Editors** — der beste Platz für eine Versions-/Bibliothekskennung. Der senkrechte Strich `\|` wird dort nicht als Trenner dargestellt; besser `·` oder ` - ` verwenden. | [VERIFIZIERT 05.08.2026] |

**Verifikation der `CNAME`-Reihenfolge (05.08.2026):** Ein per Skript erzeugter Baustein mit
Namen auf den Indizes 0–5 und 20–24 zeigte in Config exakt die erwartete Belegung —
`Raumfeuchte`…`Sperre` an AI1…AI6, `Kippen`…`Grund` an AQ1…AQ5. Damit ist die Zuordnung
Index ↔ Konnektor belegt, und die Konnektor-Reihenfolge der Tabelle oben bestätigt sich mit:
`S1`…`S8` = `Trigger1`…`Trigger8`, `S` = `ATrigger`, `Off` = `Reset`. `Param` erscheint in der
GUI **nicht** als Eingang — es ist kein bedienbarer Konnektor.

**Die Auswahlliste im Editor** („Bibliothek", links) führt nur die im Sequenztext verwendbaren
Konnektoren: `AI1`…`AI8`, `AQ1`…`AQ8` und `TQ`. Umbenannte Konnektoren erscheinen dort mit ihrem
Klartextnamen — **die Namen sind also direkt im Code verwendbar**. Doppelklick fügt sie in die
markierte Zeile ein.
| `<SEQ NAM="…" CFG="…"/>` | **Je Sequenz ein Element.** `NAM` = Sequenzname (Default `Sequenz_1`), `CFG` = der Programmtext. | `NAM` [VERIFIZIERT], `CFG` **[VERIFIZIERT 05.08.2026]** an `Bestandsprojekt V6.Loxone`: **Zeilen sind semikolongetrennt**, nicht durch Zeilenumbrüche — `set Schritt = 1;set Sperrgrund = 0;…;goto 12; ; ;end`. Einrückung als **rohe Tabs** im Attributwert; `&#x9;` statt rohem Tab bricht Configs CFG-Parser (verifiziert 05.08.2026). Kommentarzeilen sind eigene Einträge, Abschluss ist `…; ; ;end`. Folgen: **ein `;` in einem Sequenz-Kommentar würde die Zeile teilen** — Semikolons im Sequenztext meiden; und die Zeilenumbruch-Falle aus Abschnitt 4 trifft `CFG` nur über die Tabs (Attribut-Normalisierung macht daraus Leerzeichen), nicht über die Zeilenstruktur. |

> ⚠️ **Vor dem Splitten auf `;` unescapen** [VERIFIZIERT 27.08.2026]. `CFG` steht XML-escaped in
> der Datei, und `&lt;` / `&gt;` bringen ein **eigenes Semikolon** mit. Wer den rohen Attributwert
> teilt, zerlegt jedes `if x &lt; 1` in zwei Einträge: die Sequenz SMH-DUSCH ergibt so 86 statt
> der echten 70 Zeilen, und jede Prüfung von `goto`-Zielen rechnet mit falschen Nummern.
> Richtige Reihenfolge: **unescapen → auf `;` splitten → bearbeiten → joinen → escapen.**
> Beim Umbenennen von Konnektoren oder Variablen zählt nur, dass die **Eintragszahl gleich
> bleibt** — dann bleiben alle `goto` gültig.

**`CFG=""` erzeugt keinen leeren Editor.** Ein per Skript angelegter Baustein mit leerem `CFG`
zeigt in Config den **Werks-Beispieltext** ([VERIFIZIERT 05.08.2026]):

```
1  waitcondition AI1 > 0
2  set AQ1 = AI1 * 2.7
3  sleep 30 s
4  end
```

Zeile 4 **`end`** ist der Sequenz-Abschluss und wird vom Editor grau dargestellt und selbst
verwaltet — eigener Sequenztext wird **davor** eingefügt, `end` nicht mitschreiben.
Der Befehl `end` steht in der KB-Befehlsliste nicht.

### Befehlsreferenz [BELEGT]
Quelle: https://www.loxone.com/dede/kb/ablaufsteuerung/

| Befehl | Syntax | Wirkung |
|---|---|---|
| `sleep` | `sleep <Wert> <s\|m>` | pausiert. `sleep 300 s`, `sleep 10 m` |
| `waitcondition` | `waitcondition <IO> <Op> <Wert>` | blockiert, bis die Bedingung erfüllt ist. `waitcondition AI1 > AQ1`, `waitcondition AI1 + 3 > value1` |
| `set` | `set <IO> = <Ausdruck>` | Zuweisung an Eingang, Ausgang oder Variable. Rechenoperationen wie im Formel-Baustein. `set AQ1 = AI1 - AI2` |
| `setpulse` | `setpulse <IO>` bzw. `setpulse <IO> = <Wert>` | kurzer Impuls |
| `startsequence` | `startsequence <Nr>` bzw. `startsequence <Name>` | startet eine andere Sequenz |
| `return` | `return` | zurück in die aufrufende Sequenz, dort nächste Zeile |
| `goto` | `goto <Zeilennummer>` | Sprung |
| `if` | `if <links> <Op> <rechts>` … `endif` | Bedingungsblock |

**Operatoren:** `==` `>=` `>` `<=` `<` `!=`
**Kommentare:** `//` — ganze Zeile oder Zeilenende
**Variablen:** `value1`…`value5` (umbenennbar)
**Textausgang:** `set TQ = "Wert ist" AQ2` → *Wert ist 27.5*; ohne Anführungszeichen wird gerechnet

### Fallstricke [BELEGT]

- **Angeschlossene Eingänge überschreiben, was die Sequenz setzt.** Wer `set AI1 = …` schreibt
  und gleichzeitig etwas auf `AI1` verdrahtet hat, verliert den gesetzten Wert.
- **Namen dürfen nur alphanumerisch und Unterstrich sein** — Variablen wie benutzerdefinierte
  Eingangsnamen.
- **Leere oder ungültige Zeilen werden übersprungen**, nicht als Fehler gemeldet.
- **Niedriges Intervall = höhere CPU-Last.** Der Default 500 ms heißt: eine Zeile pro halbe
  Sekunde. Eine Sequenz aus 20 Zeilen braucht 10 s, bevor sie wieder von vorn schaut.
- **Liveview braucht ein vollständig in den Miniserver gespeichertes Dokument.**

---

## 3. Programm — `Code16` (PicoC)

### XML-Repräsentation [VERIFIZIERT 05.08.2026]

```xml
<C Type="Code16" V="175" U="…" Title="Programm"
   Px="…" Py="…" Px2="…" Py2="…" Cl="141,255,112" Nio="34"
   Code="// write program here in PicoC&#xA;&#xA;"      <!-- siehe Abschnitt 4! -->
   Task="1">
  <Co K="TI1"/><Co K="TI2"/><Co K="TI3"/>
  <Co K="AI1"/> … <Co K="AI13"/>
  <Co K="Remanence"/>
  <Co K="TQ1"/><Co K="TQ2"/><Co K="TQ3"/>
  <Co K="AQ1"/> … <Co K="AQ13"/>
  <Co K="TeQ"/>
</C>
```

**Kein `IoData`** — der Baustein hat weder Raum noch Kategorie und erscheint in der App als
„Nicht zugeordnet". Das ist der Normalzustand, kein Fehler.

### Konnektor-Mapping XML ↔ Doku — vollständige 1:1-Deckung

| XML (`Co/@K`) | Doku-Kürzel | Bezeichnung | Richtung | Status |
|---|---|---|---|---|
| `TI1` … `TI3` | `T1-3` | Texteingang 1–3 | E | [ABGELEITET] |
| `AI1` … `AI13` | `I1-13` | Eingang 1–13 | E | [ABGELEITET] |
| `Remanence` | `Rem` | Remanenz | P | [ABGELEITET] |
| `TQ1` … `TQ3` | `Txt1-3` | Textausgang 1–3, max. 4096 Byte | A | [ABGELEITET] |
| `AQ1` … `AQ13` | `O1-13` | Ausgang 1–13 | A | [ABGELEITET] |
| `TeQ` | `Etxt` | Fehlertext | A | [ABGELEITET] |

17 Eingänge + 17 Ausgänge = 34 = `Nio`. Doku 17 + 17. **Keine Lücke** — die Zuordnung ist
belastbar, obwohl formal abgeleitet.

| Attribut | Bedeutung | Status |
|---|---|---|
| `Code` | der komplette PicoC-Quelltext | [VERIFIZIERT] |
| `Task` | laufende Nummer des Programm-Bausteins. Die KB nennt **maximal 8** Programm-Bausteine — dazu passt ein Index. | [ABGELEITET] |

> ⚠️ **`Code` ist ein doppelt vergebener Attributname.** Am `<C Type="Document">` bedeutet `Code`
> die **Postleitzahl** (`Code="4563"`). Wer per Textsuche nach `Code="` greift, erwischt zuerst
> die PLZ. Immer über den Typ `Code16` gehen.

### 🛑 Index-Falle: `getinput(0)` ist Eingang **I1**

PicoC zählt **ab 0**, die Bausteinbeschriftung **ab 1**. Und Text- und Analogeingänge haben
**getrennte Indexräume**:

```
getinput(0)      → I1        setoutput(0, v)      → O1
getinput(12)     → I13       setoutput(12, v)     → O13
getinputtext(0)  → T1        setoutputtext(0, s)  → Txt1
```

`[ABGELEITET]` aus der 0-basierten Indexierung in der KB-Funktionsliste und dem offiziellen
Beispiel. Vor sicherheitsrelevantem Einsatz mit einem Testwert verifizieren.

**Ungeklärt:** die Bitmaske von `getinputevent()`. Das offizielle Beispiel prüft `nEvents & 0xe`
(Bits 1–3) und liest danach `getinput(0..2)`. Entweder ist Bit *N* = Eingang *N* und das Beispiel
prüft die falschen Bits, oder Bit 0 ist anderweitig belegt und Eingang *N* liegt auf Bit *N+1*.
**[OFFEN]** — im Zweifel die Maske am lebenden Objekt ausmessen, nicht annehmen.

### PicoC-Funktionsreferenz [BELEGT]
Quelle: https://www.loxone.com/eses/kb/programacion-script/ ·
PDF: https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/CustomScriptProgramming.pdf

**Sprache und Speicher:** `int` (32 bit, little endian), `float`, `char`, Zeiger. Strings UTF-8.
**128 kB gemeinsam für Heap und Stack.** Der volle C-Sprachumfang wird *nicht* erfüllt.

**Sprachumfang jenseits der Loxone-KB** `[COMMUNITY]` — aus dem Quellcode des zugrunde liegenden
*picoc*-Interpreters (github.com/jpoirier/picoc u. a. Forks). Loxones Fassung ist eine Anpassung,
diese Punkte sind für Loxone **nicht** verifiziert:

| | |
|---|---|
| `switch` / `case` | **implementiert** — der Interpreter kennt einen eigenen Laufmodus zur Case-Suche |
| `goto` | **nur vorwärts.** Rückwärtssprünge gibt es nicht — Schleifen ausschließlich über `while`/`for` |
| Funktionszeiger | **nicht unterstützt** |
| Ziel | „nicht C90, aber nah genug, dass die meisten Programme unverändert laufen" |

> ⚠️ Der Unterschied zur **Ablaufsteuerung** ist hier groß: die kennt **kein** `switch`/`case`,
> dafür aber einen **rückwärts** springenden `goto` — genau umgekehrt. Schrittketten werden dort
> mit `if`/`endif` und `goto <Schleifenanfang>` gebaut.

**Baustein-I/O (0-basiert)**
```c
int    getinputevent()                              // Bitmaske geänderter Eingänge
float  getinput(int input)
char  *getinputtext(int input)
void   setoutput(int output, float value)
void   setoutputtext(int output, char *str)
float  getio(char *str)                             // virtuelle IOs, z. B. "VI1"
int    setio(char *str, float value)
```

**Zeit** — Zeitwerte sind **Sekunden seit 1.1.2009 00:00 UTC**, nicht Unix-Epoche.
```c
void          sleep(int ms)
void          sleeps(int s)
unsigned int  getcurrenttime()
int           getyear/getmonth/getday/gethour/getminute/getsecond(unsigned int time, int local)
unsigned int  gettimeval(int y,int mo,int d,int h,int mi,int s,int local)
unsigned int  convertutc2local(unsigned int t)
unsigned int  convertlocal2utc(unsigned int t)
```

**String / Ausgabe**
```c
char *getprogramname()
void  printf(char *fmt, ...)            // landet im Log-Fenster von Loxone Config
char *sprintf(char *ptr, char *fmt, ...)
void  errorprintf(char *fmt, ...)
void  setlogtext(char *str)
int   atoi(char*)      float atof(char*)
int   batoi(char*)     float batof(char*)      // tolerieren führende Leerzeichen
void  strcpy/strncpy/strcat(...)      char *strdup(char*)
int   strcmp/strncmp/strlen(...)
char *strstr(char *str, char *find)
char *strstrskip(char *str, char *find)        // Zeiger HINTER den Fund
int   strfind(char *str, char *find, int pos)
char *index(char *str, int ch)
char *getxmlvalue(char *str, int index, char *name)
int   lineno()
```

**Speicher** — `malloc` `calloc` `realloc` `free` `memset` `memcpy` `memcmp`

**Mathe** — `sin cos tan asin acos atan sinh cosh tanh exp fabs log log10 pow sqrt round ceil floor`
> ⚠️ [BELEGT] „Der Prozessor im Miniserver hat **keine Hardware-Recheneinheit**" — sparsam einsetzen.

**Netz / Dateien / Streams**
```c
char *httpget(char *address, char *page)
char *localwebservice(char *str)                    // liefert XML
FILE *fopen(...)  fclose fprintf fputc fputs fflush fwrite fgetc fgets fread fseek remove rename
STREAM *stream_create(char *filename, int read, int append)
void    stream_printf/stream_flush/stream_close(...)
int     stream_write/stream_read/stream_readline(...)
```
Stream-Ziele: `/pfad/datei` · `/dev/tcp/adresse/port` · `/dev/udp/adresse/port` · `/dev/syslog` ·
`/dev/tty/name` (RS232/RS485)

**Binärpuffer** — `getshort getushort getint getuint getfloat getdouble(void *p, int bBigEndian)`

**Diagnose** — `getcpuinfo()` (% CPU) · `getheapusage()` / `getmaxheap()` (kB) · `getspsstatus()`

### Grenzen und Warnungen [BELEGT]

- **Ein fehlerhafter Programm-Baustein löst einen Sicherheitsneustart des Miniservers aus.**
  Danach bleibt das Programm deaktiviert, bis es in Config korrigiert ist.
- **Jeder Zeiger-Rückgabewert muss mit `free()` freigegeben werden** — außer der Zeiger kam als
  Parameter herein. Betrifft besonders `httpget()`, `localwebservice()`, `getxmlvalue()`.
- **Endlosschleifen brauchen ein `sleep()`.** Ohne das blockiert der Task.
- Das Programm läuft in einem **eigenen Task asynchron zur SPS** — es ist *nicht* zyklussynchron.
  Werte, die es setzt, erscheinen unabhängig vom SPS-Takt.
- **Maximal 8 Programm-Bausteine.**
- Programme sind **interpretiert** — Code kurz halten.
- Für Ausführung muss das Dokument **in den Miniserver gespeichert** sein.
- **Kein Loxone-Support** für diesen Baustein.

### Grundmuster [BELEGT] — offizielles Beispiel

```c
char szBuffer[128];
float f1, f2, f3, f4;
int nEvents;
while(TRUE) {
  nEvents = getinputevent();
  if (nEvents & 0xe) {
    f1 = getinput(0);
    f2 = getinput(1);
    f3 = getinput(2);
    f4 = f1 * f2 + f3;
    setoutput(0, f4);
    sprintf(szBuffer, "%f * %f + %f = %f", f1, f2, f3, f4);
    setoutputtext(0, szBuffer);
    printf(szBuffer);
  }
  sleep(100);
}
```

Das `sleep(100)` am Schleifenende ist nicht optional — es ist das, was den Task atmen lässt.

---

## 4. 🛑 Die Zeilenumbruch-Falle — betrifft **jedes** Skript, das solche Projekte anfasst

**[VERIFIZIERT 05.08.2026]**, Testlauf auf einer Kopie von `Bestandsprojekt V5.Loxone`.

Loxone Config schreibt den Programmtext als **rohe CRLF-Zeichen im Attributwert**:

```
Code="// write program here in PicoC<CR><LF><CR><LF>"
```

Im gesamten Projektfile kommt `&#xA;` **kein einziges Mal** vor — Config maskiert Zeilenumbrüche
in Attributen also nie.

Der XML-Standard schreibt für Attributwerte **Attribute-Value Normalization** vor: jeder
Zeilenumbruch wird beim Parsen durch ein **Leerzeichen** ersetzt. `System.Xml.XmlDocument` hält
sich daran. Folge:

```
vorher :  int n;⏎while(TRUE) {⏎  n = getinputevent();⏎  sleep(100);⏎}
nachher:  int n; while(TRUE) {   n = getinputevent();   sleep(100); }
```

**Ein einziger Roundtrip mit dem bisherigen Rezept macht aus einem PicoC-Programm eine Zeile.**
Kein Fehler, keine Warnung, Objekt- und Verbindungszahl unverändert — alle üblichen Prüfsummen
schlagen nicht an. Bei einem Mehrzeiler mit `//`-Kommentaren wird dabei aus dem Kommentar heraus
der **Rest des Programms auskommentiert**.

`<SEQ CFG="…">` der Ablaufsteuerung ist **anders kodiert und darum weniger gefährdet**
[VERIFIZIERT 05.08.2026]: Zeilen sind dort **semikolongetrennt**, rohe Zeilenumbrüche kommen im
`CFG` nicht vor. Ein Roundtrip normalisiert nur die rohen **Tabs** (Einrückung) zu Leerzeichen —
die Zeilenstruktur bleibt erhalten. Achtung: `&#x9;` als Ersatz für einen rohen Tab bricht
Configs CFG-Parser.

### Das korrigierte Rezept

Rohe Umbrüche **vor** dem Parsen in Attributwerten maskieren. Danach hält .NET sie beim
Speichern als `&#xA;` fest, und ein erneutes Einlesen liefert exakt den Originalstring.

```powershell
function Protect-AttrNewlines([string]$text) {
    # Attributwerte sind durch " begrenzt; ein rohes " kann darin nicht vorkommen (waere &quot;)
    $sb = New-Object System.Text.StringBuilder
    $inAttr = $false
    for ($i = 0; $i -lt $text.Length; $i++) {
        $ch = $text[$i]
        if ($ch -eq '"')                { $inAttr = -not $inAttr; [void]$sb.Append($ch); continue }
        if ($inAttr -and $ch -eq "`r")  { continue }                       # CR verwerfen
        if ($inAttr -and $ch -eq "`n")  { [void]$sb.Append('&#xA;'); continue }
        if ($inAttr -and $ch -eq "`t")  { [void]$sb.Append('&#x9;'); continue }
        [void]$sb.Append($ch)
    }
    return $sb.ToString()
}

$safe = Protect-AttrNewlines ([System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8))
[xml]$doc = New-Object System.Xml.XmlDocument
$doc.LoadXml($safe)
# … Änderungen … dann speichern wie in xml-bearbeitung.md
```

Testergebnis: naives Rezept → 4 von 4 Umbrüchen verloren, String **≠** Original.
Mit Schutz → 4 von 4 erhalten, String **identisch**.

### Prüfung vor jedem Roundtrip

```powershell
$raw = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$inAttr=$false; $n=0
for($i=0;$i -lt $raw.Length;$i++){
  $c=$raw[$i]
  if($c -eq '"'){ $inAttr=-not $inAttr; continue }
  if($inAttr -and $c -eq "`n"){ $n++ }
}
if ($n) { Write-Host "ACHTUNG: $n rohe Zeilenumbrueche in Attributwerten - Schutz noetig" }
```

> **Noch offen:** ob **Loxone Config** `&#xA;` im `Code`-Attribut beim Einlesen wieder als
> Zeilenumbruch darstellt. Für Notiztexte behauptet [xml-bearbeitung.md](xml-bearbeitung.md),
> Config akzeptiere das — für `Code` ist es **nicht** verifiziert. Erster Test: Zwei-Zeiler
> eintippen, speichern, Skript-Roundtrip mit Schutz, Config öffnen, Editor ansehen.
> Solange das offen ist: **an Projekten mit PicoC-Code lieber gar nicht per XmlDocument
> patchen**, sondern gezielt per Textersetzung — oder den Code vor dem Patch herauskopieren
> und danach in Config wieder einfügen.

### Verwandter Altschaden, den man daran erkennt
Steht in einem Attribut die **Zeichenfolge** `&amp;#xA;` (im XML-Rohtext), enthält der Wert die
fünf sichtbaren Zeichen `&#xA;` statt eines Umbruchs. Das ist die Narbe eines früheren Skripts,
das auf dem *Wert* statt auf dem *serialisierten XML* ersetzt hat. In der App erscheint dann
wörtlich `&#xA;` mitten im Text.

---

## Quellen

- Ablaufsteuerung: https://www.loxone.com/dede/kb/ablaufsteuerung/
- Programm-Baustein: https://www.loxone.com/enus/kb/program/
- PicoC-Referenz: https://www.loxone.com/eses/kb/programacion-script/
- PDF „Custom Script Programming": https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/CustomScriptProgramming.pdf
- Baustein-Tabellen (Ein-/Ausgänge wörtlich): [bausteine-system-schnittstellen.md](bausteine-system-schnittstellen.md)
- [COMMUNITY] Praxisbeispiel Dosieranlage: LoxBerry-Wiki, *Automatische Chemikaliendosierung und Regelung*
- [COMMUNITY] PicoC-Praxisbeispiele: loxwiki.atlassian.net · nikolaus-lueneburg.de/2013/07/loxone-und-picoc/
