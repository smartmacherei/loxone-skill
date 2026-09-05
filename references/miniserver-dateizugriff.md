# Miniserver-Dateizugriff und LoxCC-Format — Referenz

**Stand:** 28.08.2026 · verifiziert an einem Miniserver Gen 2, FW 17.1.6.30 (`MsType 2`)

Wie man an das **laufende Programm im Miniserver** kommt — lesend und schreibend — und was das
Binärformat dahinter ist. Betrifft nicht die lokale `.Loxone`-Datei; die behandelt
[xml-bearbeitung.md](xml-bearbeitung.md).

> Alle Adressen, Seriennummern und Zugangsdaten hier sind Platzhalter.

---

## 1. Die zwei Zugangswege

| Weg | Kann | Kann nicht |
|---|---|---|
| **HTTP** `http://<MINISERVER-IP>/dev/fs…` mit Basic-Auth | auflisten, lesen | **schreiben** |
| **FTP** Port 21, Pure-FTPd mit TLS, gleiche Zugangsdaten | auflisten, lesen, **schreiben** | — |

### HTTP — lesen

| Aufruf | Liefert |
|---|---|
| `/dev/fslist/<verzeichnis>` | Verzeichnislisting (`d`/`-`, Größe, Datum, Name) |
| `/dev/fsget/<pfad>` | Dateiinhalt roh |
| `/data/LoxAPP3.json` | Strukturdatei (nur visualisierte Controls) |
| `/dev/cfg/version` · `/dev/cfg/api` | Firmware, Seriennummer, `local`-Flag |

**Es gibt keinen HTTP-Schreibendpunkt.** Geprüft und jeweils `404`: `fsput`, `fsset`, `fsupload`,
`fscreate`, `fsdelete`, `fsmove`, `fsgetsize`. Nur `fslist` und `fsget` antworten mit `200`.
Unbekannte Pfade liefern generell `404` — das macht Endpunkt-Sondierung zuverlässig.

### FTP — lesen und schreiben

Der Miniserver fährt **Pure-FTPd** auf Port 21 mit TLS-Unterstützung (`privsep`, max. 50 Nutzer).
Anmeldung mit denselben Zugangsdaten wie die Weboberfläche. `/prog` und die übrigen Verzeichnisse
sind `drwxrwxrwx`, die Dateien `-rw-rw-rw-`.

```bash
curl --ssl --insecure -u "<BENUTZER>:<PASSWORT>" "ftp://<MINISERVER-IP>/prog/"
```

Gesteuert wird der Dienst über `/sys/config.xml`:

| Feld | Bedeutung |
|---|---|
| `FTPport` / `FTPmode` | Port und Aktivierung (`1` = an) |
| `FTPTelnetLoxPLANLocalOnly` | `true` schränkt FTP/Telnet/LoxPLAN auf das lokale Netz ein |
| `MsType` | `2` = Gen 2 |
| `MsVersion` | Firmware als Zahl, z. B. `17010630` = 17.1.6.30 |

---

## 2. Verzeichnisse

| Pfad | Inhalt |
|---|---|
| `/prog` | **das Programm** — `sps_*.LoxCC` bzw. `sps_*.zip`, dazu `Emergency.LoxCC`, `permissions.bin`, `Music.json`, `sps.LoxPLAN`, die `Default*.Loxone`-Vorlagen |
| `/sys` | `config.xml`, `addons.json` (Plugin-Katalog), `tokens.xml`, Sprachpakete `sys_*.zip`, `IconLibrary.zip` |
| `/backup` · `/log` · `/stats` | Sicherungen, Logs, Statistiken |
| `/update` · `/updateweb` | Firmware-Update-Ablage |
| `/user` | `admin`, `common`, `custom`, `dbgCustom` |
| `/docs` · `/tools` | im getesteten Gerät **leer** |

---

## 3. Das LoxCC-Format

Ein Programm liegt entweder als nacktes `sps_*.LoxCC` oder als `sps_*.zip` mit `sps0.LoxCC` darin.
Der Container ist simpel:

```
Offset  Größe  Feld           Wert
0       4      magic          0xAABBCCEE   (LE: ee cc bb aa)
4       4      comp_size      Länge des LZ4-Blocks
8       4      uncomp_size    Länge des XML
12      4      crc32          CRC32 (IEEE) über das ENTPACKTE XML
16      …      payload        LZ4-Block (Raw-Block-Format, kein Frame)
```

`comp_size + 16` ist immer die Dateigröße — brauchbare Plausibilitätsprüfung.

**Das Prüfsummenfeld ist CRC32 über das entpackte XML**, nicht über die komprimierten Daten und
nicht über den Header. Verifiziert an zwei unabhängigen Dateien (`sps0.LoxCC` und
`Emergency.LoxCC` desselben Geräts); getestet und ausgeschlossen wurden Summen-, XOR- und
Fletcher-Varianten sowie CRC32 über Payload und Header+Payload.

### Zurückschreiben ohne echte Kompression

Das LZ4-**Block**-Format erlaubt reine Literal-Sequenzen. Ein Encoder muss also gar nicht
komprimieren: Token mit `lit`-Länge, dann die Rohbytes. Für Blöcke ab 15 Literalen folgt die
Längenerweiterung in 255er-Schritten. Ergebnis ist minimal größer als das Original und für jeden
LZ4-Dekompressor gültig.

Reihenfolge beim Bauen: XML serialisieren → CRC32 darüber → LZ4-Literalblock → Header davor.

### Welches Programm ist das aktive?

`/prog` enthält typischerweise **mehrere** `sps_*`-Dateien aus früheren Speichervorgängen. Der
Zeitstempel steckt im Dateinamen (`sps_<nr>_<JJJJMMTTHHMMSS>`).

> **Falle:** Je nach Speichervorgang legt Config das Programm als nacktes `.LoxCC` **oder** als
> `.zip` ab. Wer nur nach `.LoxCC` sucht, erwischt stillschweigend ein veraltetes Programm — neue
> Geräte fehlen dann komplett. Immer beide Endungen berücksichtigen und nach Zeitstempel wählen.

---

## 4. Was der WebSocket liefert — und was nicht

**Gemessen:** 90 Sekunden Mitschnitt am WebSocket-Stream eines Miniservers mit 23 Visu-Controls
und 65 nicht visualisierten Klemmen:

| | |
|---|---|
| UUIDs im Push-Stream gesamt | 191 |
| davon nicht visualisierte Klemmen | **0 von 65** |

**Der Miniserver pusht ausschließlich, was in der Visualisierung steht.** Was kein Visu-Häkchen
hat, steht nicht in `LoxAPP3.json` und kommt nie über den Stream — unabhängig davon, wie oft es
sich ändert. Kein Client-seitiger Trick ändert daran etwas.

Die einzigen Auswege:

1. **Visu-Häkchen setzen** (`IoData@Visu="true"`) — dann ist die Klemme ein regulärer Control,
   wird gepusht, und Impulse gehen nicht verloren. Nebenwirkung: sie erscheint auch in der
   **Loxone-App des Kunden**.
2. **Zyklisch per HTTP nachziehen** — `/jdev/sps/io/<uuid>` je Klemme. Kostet wenig
   (gemessen: 65 Abfragen in 0,14 s, ~2 ms pro Anfrage), verpasst aber prinzipbedingt kurze
   Impulse zwischen zwei Abfragen.

---

## 5. Offen / unbestätigt

**Wie ein hochgeladenes Programm aktiviert wird, ist nicht verifiziert.** Eine Datei nach `/prog`
zu legen genügt vermutlich nicht — der Miniserver muss sie laden. Kandidaten (**ungetestet**):
ein Neustart über die dokumentierte API, oder ein Kommando, das Loxone Config nach dem Upload
sendet. Die offizielle PDF „Communicating with the Miniserver" ließ sich nicht maschinell
auswerten. **Vor dem ersten Schreibversuch klären** — an einem Gerät, dessen Ausfall egal ist.

---

## 6. Fallen

**1. HTTP kann nicht schreiben — FTP schon.**
Wer nur die `/dev/fs…`-API kennt, hält Schreibzugriff für unmöglich. Der Weg ist FTP, und der ist
standardmäßig aktiv.

**2. `401` heißt „Pfad existiert", `404` heißt „gibt es nicht".**
Gilt für Endpunkt-Sondierung am Miniserver generell — siehe auch [mcp-server.md](mcp-server.md).

**3. Das Prüfsummenfeld nicht mit dem Payload verwechseln.**
CRC32 über das **entpackte XML**. Wer über die komprimierten Daten rechnet, baut ein Programm,
das der Miniserver ablehnt.

**4. `.zip` gegen `.LoxCC` — siehe § 3.**
Die häufigste stille Fehlerquelle beim Programm-Download.

**5. Ein aufgespieltes Programm startet die Anlagenlogik neu.**
Das ist kein reines Dateikopieren. Beim Kunden bedeutet es eine kurze Unterbrechung — nicht
nebenbei im laufenden Betrieb machen.

**6. Config gewinnt, wenn aus einer lokalen Master-Datei gearbeitet wird.**
Schreibt ein Werkzeug Änderungen direkt in den Miniserver und der Errichter lädt danach sein
lokales Projekt hoch, sind sie **spurlos weg**. Unkritisch nur, wenn der Ablauf lautet: Projekt
**erst aus dem Miniserver ziehen**, dann bearbeiten, dann zurückladen. Diese Disziplin ist
Voraussetzung, nicht Nebensache.

**7. Zugangsdaten stehen im Klartext auf dem Gerät.**
`/sys/config.xml` und `/sys/tokens.xml` sind über FTP und `fsget` lesbar. Wer Dateien vom
Miniserver in Repos oder Logs kopiert, prüft sie vorher.
