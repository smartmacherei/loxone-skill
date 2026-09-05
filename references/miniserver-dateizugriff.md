# Miniserver-Dateizugriff und LoxCC-Format — Referenz

**Stand:** 28.08.2026 · verifiziert an einem Miniserver Gen 2, FW 17.1.6.30 (`MsType 2`) ·
**Programm-Upload und Logger-UDP verifiziert 05.09.2026** (Abschnitte 4a und 5)

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

Aus Python geht es mit `ftplib.FTP_TLS` + `login()` + `prot_p()` (verifiziert 05.09.2026); auch
`STOR` (Upload, `curl -T`) und `DELE` funktionieren, getestet in `/temp`.

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
3. **Logger-Objekt mit UDP-Ziel** — *Miniserver → Meldungen → Logger*, Adresse
   `/dev/udp/<HA-IP>/<Port>`, und je Klemme eine **Logger-Referenz auf einer Programmseite**
   (`OutputRefLM`), deren Eingang vom Wert-Konnektor der Klemme gespeist wird. Sendet **bei jeder
   Änderung sofort** (13–20 ms), erscheint **nicht** in der App und **schreibt nicht auf die
   SD-Karte**. **[VERIFIZIERT 05.09.2026]** — Details, Fallen und das Skript in Abschnitt 4a.
   Das ist etwas anderes als „Statistik" (Häkchen am Objekt, schreibt zyklisch auf die SD).

### 4a. Logger-UDP — gemessen am Koffer, 05.09.2026

Gemessen am Miniserver Gen 2 (FW 17.1.6.30) mit einem UDP-Mitschnitt auf dem HA-Rechner im
selben Subnetz. Skript, das alles Folgende erzeugt: `scripts/ha_udp_logger.py`.

**Was funktioniert — und was nicht:**

| Variante | Ergebnis |
|---|---|
| `<LoggerMailer RefLogger="…" On="…" Off="…"/>` **direkt an der Klemme** (`DigitalIn`, `TreeSensor`, `Actor`, … — 77 Stück) | **nichts.** Kein Paket, keine Datei, kein Logeintrag. Auch mit `MinimumTime="5000"` nicht. |
| dasselbe direkt an einem **Funktionsbaustein** (`PushButton`) | **nichts.** |
| `<C Type="OutputRefLM" Ref="<Logger-UUID>">` auf einer Seite, `AI` vom Quell-Konnektor gespeist, darin `<LoggerMailer RefLogger="<Logger-UUID>" On="Text;&lt;v&gt;" Off="Text;&lt;v&gt;" MinimumTime="0"/>` | **sendet bei jeder Änderung.** Das ist genau das Objekt, das Config beim Ziehen eines Loggers auf die Seite anlegt. |
| Logger-Adresse `/dev/udp/192.168.0.255/<Port>` (Subnetz-Broadcast) | **funktioniert** — der Empfänger muss seine IP nicht kennen. |
| Logger-Adresse `/log/user.log` über dieselbe `OutputRefLM`-Konstruktion | schreibt `/log/user.log` — **die UDP-Logger schreiben nichts auf die SD**, `/log` bleibt unverändert. |

Der Miniserver wertet `LoggerMailer` also **ausschließlich an `OutputRefLM`-Objekten** aus. Die
Abschnitte „Logging/Mail/Call/Track" in Config sind nichts anderes als diese Referenzobjekte.

**Paketformat** (ein Datagramm je Änderung, Quellport = Zielport):

```
2026-09-05 16:05:59;HA UDP;V1-OutputRefLM-UDP;1\r\n
<Datum Zeit>;<Titel des Logger-Objekts>;<Meldungstext, <v> ersetzt>\r\n
```

Für die HA-Integration heißt der Meldungstext `<Klemmen-UUID>;<v>`, das Datagramm also
`…;HA UDP;18f7cbc0-0169-4c6c-ffffa13734b4be2f;1`. `ExcludeTimestamp="true"` am Logger-Objekt
hat den Zeitstempel **nicht** entfernt — der Attributname stimmt so nicht **[OFFEN]**. Der
Zeitstempel hat Sekundenauflösung.

**Zeitverhalten** (Party-Schalter per `/jdev/sps/io/<uuid>/On|Off`, UDP-Ankunft auf derselben Uhr):

| | |
|---|---|
| Latenz HTTP-Antwort → UDP-Paket | **12–20 ms** (SPS-Zyklus 10 ms + Versand) |
| Impulse mit 1000 / 200 / 50 / 20 ms Länge | **alle** angekommen, Ein und Aus je ein Paket |
| Impulse mit 10 ms Länge (= ein SPS-Zyklus) | **teils verloren** — von drei Impulsen fehlte einer ganz, bei einem das Aus |

Kürzer als ein SPS-Zyklus geht nicht — das ist keine Logger-, sondern eine SPS-Grenze.

**Konnektoren, von denen das `OutputRefLM` gespeist wird:**

| Klemmentyp | Konnektoren | Quelle für `<In Input="…"/>` |
|---|---|---|
| `DigitalIn`, `TreeSensor`, `LoxAIRsensor` | `Q`, `Qe` | `Q` (Wert; `Qe` ist der Fehlerausgang) |
| `VoltageIn`, `TreeAsensor`, `LoxAIRAsensor` | `AQ`, `Q` | `AQ` (Wert; `Q` ist hier der Fehlerausgang) |
| `Online` | `Q` | `Q` |
| `Actor`, `TreeActor`, `TreeAactor`, `LoxAIRactor`, `LoxAIRAactor` | nur `I` | der Konnektor, der den Ausgang speist — steht im `<In Input>` des `I` (meist `OutputRef.AQ`). **Unverdrahtete Ausgänge haben keine Quelle** und lassen sich so nicht melden |

Ein Seitenobjekt darf einen Peripherie-Konnektor **direkt** referenzieren — genau so macht es
Config beim `InputRef` (`AI <= Klemme.AQ`, `I <= Klemme.Q`).

**Offen:** `MinimumTime` (Wirkung unbekannt, 0 und 5000 verhielten sich in den Tests gleich),
Analogwert-Format von `<v>` und ob analoge Änderungen gedrosselt werden — Messung läuft.

**Recherchiert 05.09.2026, damit es niemand ein zweites Mal sucht:**

| Weg | Befund |
|---|---|
| MQTT-Client (ab 15.3, Gen 2) | 16 Subscriptions, 16 Publish, Auswertung alle 2 s. Changelog wörtlich: „No real time communication". Unbrauchbar für Echtzeit. |
| BACnet-Server (Gen 2) | offiziell, B-SA/B-GW, Port 47808. **Welche Objekte freigegeben werden und wie, ist in der KB nicht dokumentiert** — am Koffer mit YABE prüfen. HA hat keine Core-Integration. |
| Debug-Monitor / UDP 7777 | sechs Log-Kanäle (Common, SPS, Protocol, Bus, File, Net). Der **SPS-Kanal enthält keine Meldung über Ein-/Ausgangswechsel**; der Bus-Kanal loggt nur Loxone-Link-Telegramme der Gen-1-Extensions (`LNK Value from … DigInputs`). Tree/Air laufen über einen proprietären Config-Kanal („EIP send monitor data"). Sackgasse. Quelle: Meldungstabelle `DEU.LxRes`, siehe [techdoc-lxres.md](techdoc-lxres.md). |
| `dev/sps/enumin`, `enumout` | Web-Services-KB: listet alle SPS-Ein-/Ausgänge. Nur Aufzählung, kein Push. |
| `dev/sps/log/<ip>` | **[VERIFIZIERT 05.09.2026]** schaltet den **Loxone-Monitor-Strom** auf diese IP: UDP von Port 7777 an Port 7777, sofort und ohne Neustart. Inhalt sind Textzeilen mit kleinem Binärkopf — Netzwerk-Ereignisse (`TCP socket accept`, `HTTP4 GET /jdev/sps/io/…`), Dateisystem, Bus — alle 500 ms ein Schwung von 0,2–2 KB. **Keine Ein-/Ausgangswechsel**, wie oben schon aus der Meldungstabelle geschlossen. `dev/sps/log` (ohne IP) schaltet ihn wieder ab. Für Echtzeitwerte unbrauchbar, zum Mitlesen von HTTP-Zugriffen praktisch. |
| `jdev/sys/getconfiguration` | JSON mit u. a. `port-monitor`, `port-ftp`, `http-mode`. Nur Lesen der Netzkonfiguration. |

---

## 5. Programm zurückschreiben — so macht es Loxone Config

**[VERIFIZIERT 05.09.2026]** an drei Uploads auf den Demo-Miniserver. Der Ablauf steht wörtlich
im Miniserver-Log `/log/def.log`, dort protokolliert der Miniserver jeden Config-Speichervorgang:

```
Program changed by user 'admin'
PRG got restart command; user: admin(192.168.0.101)
Loading sps_new.zip - Remove old custom changes
PRG start program
Program started: /lx/prog/sps_0272_20260713140822.LoxCC     <- Name des *vorherigen* Programms
Rename program /lx/prog/sps_0272_20260713140915.zip           <- sps_new.zip bekommt den Zeitstempel
```

1. **FTP `STOR /prog/sps_new.zip`.** Der Dateiname ist fix. Inhalt wie Configs eigene Pakete:
   `sps0.LoxCC` (das Programm), `LoxAPP3.json`, `permissions.bin`, `Emergency.LoxCC`, `Music.json`
   — alle fünf Deflate-komprimiert. Am einfachsten das zuletzt geladene `sps_*.zip` aus `/prog`
   nehmen, nur `sps0.LoxCC` ersetzen und in `LoxAPP3.json` das `lastModified` auf das neue
   `Document/@Date` setzen (die App merkt sonst nichts von der Änderung).
2. **`GET /jdev/sps/restart`** (Basic-Auth). Antwort `Code 200`, nach **einer Sekunde** ist
   `/jdev/sps/state` wieder `5` (läuft). Der Miniserver lädt `sps_new.zip`, benennt es in
   `sps_<ControlList-Version>_<JJJJMMTThhmmss>.zip` um (Zeit des Ladens, nicht des Speicherns)
   und entpackt `Emergency.LoxCC`, `permissions.bin`, `Music.json` nach `/prog`.
3. **Kontrolle:** `/data/LoxAPP3.json` → `lastModified` = neues `Document/@Date`; die
   UDP-Discovery-Antwort (`Prog:…`) zeigt dasselbe Datum; `def.log` darf **keine** der Zeilen
   `PRG new program file have errors`, `PRG restore old program file`, `PRG Error in program xml
   file` enthalten (Strings aus der Meldungstabelle — der Miniserver fällt bei einem defekten
   Programm auf das vorherige zurück).

`sps_new.zip` **ohne** Restart bleibt liegen und wird beim **nächsten Start** geladen — auch bei
einem Stromausfall. Wer hochlädt, startet also auch neu, oder löscht die Datei wieder (FTP `DELE`).

Ohne Neustart der Anlagenlogik geht es nicht: `dev/sps/restart` unterbricht die SPS für rund
eine Sekunde, Remanenzwerte werden zurückgelesen (`RestoreRemanenceState … OK`), Websocket-Clients
(auch Home Assistant) verbinden sich neu.

Das `.LoxCC` wird mit **echtem LZ4** geschrieben, wenn das Python-Paket `lz4` da ist
(`lz4.block.compress(xml, mode="high_compression", store_size=False)`), sonst als Literalblock.
Beides hat der Miniserver geladen. `Document/@DateS` ist die Speicherzeit in **Sekunden seit
2009-01-01 00:00 UTC** (`Date` steht in Ortszeit) — aus demselben Zähler stammt das erste Feld
neu angelegter UUIDs.

### Offen

- Wie Config die **Vorlagen** `Default*.Loxone` und `sps.LoxPLAN` in `/prog` nutzt — nicht angefasst.
- Ob der Miniserver ein `sps_new.LoxCC` (nackt, ohne Zip) ebenso lädt — nicht getestet.

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

**8. `LoggerMailer` direkt an der Klemme ist tot.**
Die Zeile sieht richtig aus, Config-Klassen wie `CLoggerMailerData` legen sie nahe, der
Miniserver ignoriert sie stillschweigend — kein Fehler, keine Meldung. Nur `OutputRefLM`
zählt (Abschnitt 4a). Zwei Uploads hat diese Erkenntnis gekostet.

**9. Loxone-UUIDs haben 35 Zeichen, nicht 36.**
`18f7cbc0-017e-4c9b-ffffa13734b4be2f` = 8-4-4-**16**. Ein Regex mit `{36}` oder ein UUID-Parser
findet **keine einzige** Loxone-UUID.
