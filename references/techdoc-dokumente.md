# Loxones eigene Dokumente aus dem Config-Paket

In jeder Loxone-Config-Installation liegt ein **121-MB-Archiv** mit Dokumentation, das
bei der Installation mitkommt und nie jemand öffnet:

```
C:\ProgramData\Loxone\Loxone Config <Ver>\TechDoc\TechDoc_Common.zip
```

**[VERIFIZIERT 18.09.2026]** an Config 17.2.8.28: 1.284 Dateien — 1.090 Bilder,
**190 PDFs**, davon 162 Gerätedatenblätter und 28 sonstige. Diese Datei wertet die
Dokumente aus, die kein Datenblatt sind und die inhaltlich etwas hergeben.

Alles hier ist **[BELEGT]** — Loxones eigene Dokumente, mit Datumsstempel.

| Dokument | Seiten | Stand | Abschnitt hier |
|---|---:|---|---|
| `API_Commands.pdf` | 7 | 2026-01-13 | 1 |
| `Loxone-Required-Ports-Domains.pdf` | 7 | 2026-01-04 | 2 |
| `OnlineOfflineHandling_AirDevices.pdf` | 2 | – | 3 |
| `Dynamic_Audio_Grouping_WebAPI_Documentation.pdf` | 8 | 2025-08-31 | 4 |
| `App_FunctionBlock_URLScheme.pdf` | 2 | – | 5 |
| `Requirements_UserDefinedIntercoms.pdf` | 1 | – | 6 |
| `IOs_StatVal_Error.pdf` | 14 | – | 7 |
| `CustomScriptProgramming.pdf` | 17 | – | → [programmier-bausteine.md](programmier-bausteine.md) |

Auspacken:

```bash
py -3 -c "import zipfile; zipfile.ZipFile(r'C:\ProgramData\Loxone\Loxone Config 17.2.8.28\TechDoc\TechDoc_Common.zip').extractall('ziel')"
```

---

## 1. API-Kommandos — die Sprache des API-Konnektors

Der Ausgang `API` taucht an Dutzenden Bausteinen im Katalog auf, und alle
`bausteine-*.md` verlinken auf `API_Commands.pdf`. **Das ist sein Inhalt.**

Die Befehle steuern einen Baustein *von außen* an — aus einem Touch Pure Flex oder über
einen API-Konnektor. Loxone schreibt selbst dazu, dass die meisten **nur für den
Touch Pure Flex** relevant sind.

| Befehl | Syntax | Zweck |
|---|---|---|
| **SET** | `SET(Baustein;Eingang;Wert)` | Wert an einen Eingang senden. Wert leer = Wert kommt vom Taster. Digital: `pulse` |
| **SETT5** | `SETT5(Baustein;Eingang;T5-Taste;[Wert])` | Eine bestimmte T5-Taste setzen. Werte: `pulse`, `On`, `Off` |
| **MENU** | `MENU(Baustein;Eingang;[Wert1:Text1];…)` | Textauswahl über die Auf-/Ab-Tasten |
| **VALUESELECT** | `VALUESELECT(Baustein;Eingang;[Wert];[Min];[Max];[Schritt];[Einheit])` | Zahlenauswahl |
| **TIMESELECT** | `TIMESELECT(Baustein;Eingang;[Startzeit];[Schritt])` | Zeitauswahl in Minuten |
| **WAIT** | `WAIT(Zeit)` | Pause in **Millisekunden** vor dem nächsten Befehl |
| **GETINPUT** | `GETINPUT(Baustein;Eingang;[Wert1:Text1];…)` | Aktuellen Wert eines Eingangs/Parameters lesen |
| **GETOUTPUT** | `GETOUTPUT(Baustein;Ausgang;[Wert1:Text1];…)` | Aktuellen Wert eines Ausgangs lesen |
| **ECHO** | `ECHO(Baustein)` | Rückmeldungen des Bausteins anzeigen |

**Die T5-Tastennummern** (für `SETT5`): `1` Beschattung auf · `2` Lauter · `3` Licht ·
`4` Beschattung ab · `5` Leiser.

**Verkettung.** Mehrere Befehle hintereinander, mit `=` am Anfang und `&` als Trenner:

```
=SET(AP;V;50)&WAIT(500)&GETOUTPUT(AP;Volume)
```

Die Befehle laufen nacheinander. Wird die Taste erneut gedrückt, **startet der laufende
Befehl neu**. Da sie sequenziell abgearbeitet werden, verzögert ein langes `WAIT` **alle**
folgenden Befehle in der Warteschlange.

**Displaytext.** Auch der Anzeigetext des Touch Pure Flex kann eine Formel sein — dann
muss sie mit `=` beginnen, sonst gilt sie als reiner Text. Sinnvoll sind dort nur `WAIT`,
`GETINPUT`, `GETOUTPUT` und `ECHO`.

**Zwei harte Grenzen, wörtlich:**

- „Nesting, for example, a GET in a SET is currently not supported!"
- `MENU` füllt die Wert-Text-Paare bei manchen Bausteinen automatisch (z. B. `Mood` der
  Lichtsteuerung, `Fav` des Audio Players). Bei allen anderen zeigt es den **nackten
  Zahlenwert** — dann muss man die Paare selbst angeben.

---

## 2. Ports und Domains — was durch die Firewall muss

Aus `Loxone-Required-Ports-Domains.pdf`, Stand 2026-01-04. Unentbehrlich bei VLANs,
gemanagten Switches und restriktiven Netzen.

### Miniserver, lokal

| Zweck | Port |
|---|---|
| **Suche/Discovery** | **UDP 7070–7071** — Anfrage auf 7070, Antwort auf 7071 mit Seriennummer und Version. Dazu mDNS und UPnP |
| App & Config | TCP 443 und der in den Einstellungen gesetzte HTTP-Port |
| FTP | TCP 21 (Steuerung), TCP 20 (Daten) |
| DNS · NTP | UDP 53 · UDP 123 |
| mDNS | UDP 224.0.0.251:5353 |
| **Debug-Monitor** | **UDP 7777** (Vorgabe, in Config änderbar) |
| BACnet | UDP + TCP 47808 |
| **Gateway/Client** | **UDP 7070–7077, Broadcasts müssen erlaubt sein** |
| Blink-Synchronisation Netzwerkgeräte | UDP-Broadcast an 255.255.255.255:7079 |
| KNX-IP (nur Gen 1) | IGMP-Multicasts |

### Miniserver, ausgehend in die Cloud

| Dienst | Adresse |
|---|---|
| Wetter | `weather.loxone.com:6066` · `weather.loxonecloud.com:443` |
| Caller · Mailer · Push | `caller.loxone.com:80/443` · `mail.loxonecloud.com:443` · `push.loxonecloud.com:443` |
| Cloud-DNS | **UDP** `dns.loxonecloud.com:7700` |
| Remote Connect | `connect.loxonecloud.com:443`, MQTT `*.ccbroker.loxonecloud.com:8443`, SSH `*.loxonecloud.com:22` |
| Update | `update.loxone.com` · `updatefiles.loxone.com` :80/443 |
| **Crash-Log** | **UDP** `log.loxone.com:7707` |
| Dienste (z. B. Spotpreise) | `services.loxonecloud.com:80/443` |

**Die Falle bei Remote Connect:** Verbindungen laufen über
`*.dyndns.loxonecloud.com:[Port]`, und **der Port wird zufällig aus 20000–65000
vergeben.** Eine Firewallregel auf einen festen Port funktioniert nicht.

**Online-Prüfung:** Der Miniserver pingt der Reihe nach `dns.loxonecloud.com`,
`icann.org`, `w3c.org` (ICMP). Antwortet der erste, hört er auf. Wer ICMP komplett
sperrt, hat einen Miniserver, der sich für offline hält.

### Audioserver / Wireless Speaker

| Zweck | Port |
|---|---|
| **Kommunikation mit dem Miniserver** | **TCP 7095**, dazu TCP 80/443 |
| **Kommunikation mit der App** | **TCP 7091** |
| Audiostreams Audioserver ↔ Audioserver | UDP 7788, UDP 14000–14999 |
| Audioserver ↔ Audio Extensions | TCP+UDP 111 (Boot/NFS), TCP+UDP 2049 |
| **PTPv2-Zeitsynchronisation** | **UDP 319 + 320**, Multicast 224.0.1.129 / FF0x::181 |
| AirPlay | TCP 7000–700x (7000 + ein Port je Player), TCP/UDP 49152–65535 |
| Spotify Connect (Stereo Extension) | mDNS/DLNA UDP 5353/1900, TCP/UDP 57621, TCP 4070 |

> **Merken: 7091 ist der Audio-Steuerport, 7095 der zum Miniserver.** Das erklärt, warum
> Music-Server-Emulationen auf 7091 lauschen → [sonos-integration.md](sonos-integration.md).

**PTP ist der häufigste Grund für zerfallende Multiroom-Synchronität.** Loxone warnt
wörtlich: „Features such as IGMP snooping or energy-saving switch modes can interfere with
PTP if misconfigured."

**Und ein Verhalten, das man kennen muss:** Der Audioserver pingt regelmäßig sein
Standardgateway. „If the gateway does not respond for 15 minutes, the Audioserver performs
a safety reboot." Ein Audioserver, der sich nachts neu startet, hat also womöglich kein
Audio-, sondern ein Gateway-Problem.

### Intercom

Suche UDP 7070–7071 · Miniserver TCP 7091 · App TCP 7091 und 80/443
(WebSocket-Signalisierung für WebRTC) · Video/Audio lokal UDP dynamisch 49152–65535 ·
extern STUN `stun.loxonecloud.com:3478`, Fallback `stun.l.google.com:19302` ·
SIP UDP 5060.

### Loxone Config

Update · `shop.loxone.com:443` (Preislisten der Projektplanung) ·
`geo.loxonecloud.com:443` (Geokoordinaten) ·
**`api.library.loxone.com:443` (Vorlagen und Vorlagenindex)** →
[library-loxone-com.md](library-loxone-com.md) · ab V16.3 wechselt die
Remote-Verbindung von `dns.loxonecloud.com` auf `connect.loxonecloud.com:443`.

---

## 3. Air-Geräte: wann sie offline gehen — und wie lange sie es bleiben

Aus `OnlineOfflineHandling_AirDevices.pdf`. Die konkreten Zeiten erklären fast jede
„das Gerät ist offline"-Frage.

### Im Miniserver

Zwei Gründe, aus denen ein Air-Gerät offline geht:

1. **Es quittiert nicht.** Die Air Base wiederholt dreimal; **nach vier erfolglosen
   Versuchen** gilt das Gerät als offline.
2. **Es meldet sich zu lange nicht.** Timeout je Gerätetyp:

| Gerätetyp | Offline nach |
|---|---|
| **netzgespeist (DC)** | **24 h** |
| **batteriebetrieben** | **52 h** |
| batteriebetrieben mit regelmäßigen Sensordaten | `Sendeintervall × 10 + 1 h` — also irgendwo zwischen 0 und 52 h |
| **Remote Air** | **geht nie offline** |

**Wiederverbindung:** Sofort, sobald der Miniserver irgendwelche Daten bekommt — auch als
Antwort auf einen Befehl. Ein offline gemeldetes Gerät kann also sofort online gehen, wenn
man einen Ausgang schaltet. Aber: „the Miniserver by itself does not try to periodically
establish a connection with an offline device. This must always be initiated by the device."

### Im Gerät

Die Status-LED am Gerät kann etwas **anderes** anzeigen als der Miniserver — das Gerät
entscheidet selbst anhand der Quittungen. Drei nicht quittierte Alive-Pakete in Folge:
LED blinkt orange. Unquittierte Nutzdaten: sofort offline.

**Das Alive-Intervall ist nicht konstant.** Beim Start kurz (z. B. 10 s bei
Batteriegeräten), nach erfolgreicher Quittung wächst es „up to multiple hours".

> **Die wichtigste Zahl:** Ein offline gegangenes Gerät verlängert seine Wiederholabstände
> **bis auf 24 Stunden**. Miniserver und Air Base können längst wieder laufen — das Gerät
> meldet sich trotzdem erst beim nächsten Versuch. Wer nicht warten will, muss das Gerät
> aufwecken (Taste, Batterie) statt den Miniserver neu zu starten.

---

## 4. Dynamische Audio-Gruppierung — HTTP-API des Audioservers

Aus `Dynamic_Audio_Grouping_WebAPI_Documentation.pdf`, Stand 2025-08-31 — eines der
neuesten Dokumente im Paket. Gedacht für Räume mit beweglichen Trennwänden (Ballsaal),
brauchbar überall dort, wo Zonen **aus der Logik heraus** gruppiert werden sollen.

### Einrichtung

Ein **virtueller Ausgang** im Miniserver auf den Audioserver:

```
http://as0a01:7091/          ← der abschließende Schrägstrich ist Pflicht
http://ms368d:7091/          ← Miniserver Compact mit internem Audiodienst: eigener Hostname
http://127.0.0.1:7091/       ← oder die lokale Adresse
```

Darunter je Gruppierung ein `VirtualOutCmd`.

### Die Befehle

```
audio/cfg/dgroup/create/<Master>,<Player 1>[,<Player N>]
audio/cfg/dgroup/delete/<Master>
```

| Aufruf | Wirkung |
|---|---|
| `audio/cfg/dgroup/create/1,2` | Gruppe aus 1 und 2. **Master ist 1** und bestimmt, was läuft |
| `audio/cfg/dgroup/create/1,2,3` | erweitert die bestehende Gruppe um Player 3 |
| `audio/cfg/dgroup/create/1,2` | löst Player 3 wieder heraus |
| `audio/cfg/dgroup/create/4,1,2` | **neue** Gruppe mit Master 4 und neuer Quelle |
| `audio/cfg/dgroup/delete/4` | löst die ganze Gruppe auf und stoppt die Musik |

**`create` ist idempotent-überschreibend:** Derselbe Befehl mit weniger Playern entfernt
die fehlenden. Man beschreibt immer den *Sollzustand*, nie eine Differenz.

Die **Player-ID** ist eine Eigenschaft des Player-Objekts in Config. `delete` funktioniert
mit jedem Player der Gruppe, Loxone empfiehlt aber ausdrücklich den Master.

Loxone legt eine Beispieldatei bei:
`VO_Dynamic Grouping AudioZones Ballroom Example.xml`.

---

## 5. App-Baustein — fremde Apps starten

Aus `App_FunctionBlock_URLScheme.pdf`. Der Baustein „App" startet auf dem Endgerät eine
App, z. B. Apple Music direkt aus dem Audio-Player-Baustein heraus.

| Plattform | Schema | Beispiel |
|---|---|---|
| **iOS** | URL-Scheme | `music://` |
| **Android** | `market://launch?id={APP_ID}` | `market://launch?id=com.apple.android.music` |
| **Windows** | Dateipfad der Anwendung | – |

**Die iOS-Einschränkung ist die wichtige Nachricht:** „Since iOS 9.0 Apple limits this
feature to system apps (e.g. Music App). Third party apps are no longer supported."
Ausgenommen sind nur Apps, die direkt mit der Loxone-App verknüpft sind — **Spotify und
Soundsuit**.

**Umweg für alle anderen iOS-Apps:** In iOS einen Kurzbefehl anlegen, der die App öffnet,
und ihn aufrufen mit `shortcuts://run-shortcut?name=[Name des Kurzbefehls]`.

Unter Android startet die App auch über einen gewöhnlichen `http`-Link, sofern in den
Systemeinstellungen hinterlegt — `https://www.netflix.com/title/70300800` öffnet Netflix.

---

## 6. Benutzerdefinierte Intercom — was die Kamera können muss

Aus `Requirements_UserDefinedIntercoms.pdf` — eine Seite, aber sie beantwortet die Frage,
warum eine Kamera nicht funktioniert.

| Anforderung | |
|---|---|
| Protokoll | HTTP/1.1 nach RFC 2616 |
| **Authentifizierung** | RFC 2617: **Basic (ohne Realm)** oder **Digest (MD5 / MD5-SESS)** |
| **Maximale Bildgröße** | **5 MB** |
| **Antworttypen** | **nur** `multipart/x-mixed-replace` und `image/jpeg` |
| Weiteres | mehrere Streams gleichzeitig; Header müssen case-insensitive behandelt werden (RFC 2616 §4.2) |

**Das schließt RTSP und H.264 aus.** Eine Kamera, die nur RTSP kann, lässt sich nicht als
benutzerdefinierte Intercom einbinden — egal wie die URL aussieht. Gebraucht wird ein
MJPEG- oder Einzelbild-Endpunkt.

Ergänzend die Falle aus dem Katalog: **Zugangsdaten gehören je nach Kamera in die URL,
nicht in die Felder „Benutzername/Kennwort Kamera"** →
[bausteine-tore-tueren-spezial.md](bausteine-tore-tueren-spezial.md).

---

## 7. `IOs_StatVal_Error.pdf` — Belimo/MP-Bus-Fehlercodes

**Der Titel führt in die Irre.** Das Dokument verspricht „Inputs, outputs, status values
and error messages", behandelt aber **ausschließlich Belimo-Geräte am MP-Bus** —
allgemeine Klemmen-Statuswerte stehen nicht drin.

Drei Fehlerebenen, je mit eigener Codeliste:

| Ebene | Betrifft |
|---|---|
| **Belimo Gateway Error** | das Loxone-Belimo-Tree-/Air-Gerät selbst |
| **Belimo Device Error** | Kommunikation Tree/Air-Gerät ↔ Belimo-Gerät |
| **Belimo Device Malfunction** | Störungen im Belimo-Gerät |

Die praktisch wichtigsten:

| Code | Ebene | Bedeutung |
|---:|---|---|
| `4` | Gateway | **Befehlspuffer übergelaufen** — MP-Bus überlastet oder Geräte antworten nicht. **Der Puffer wird geleert, Befehle gehen dabei verloren** |
| `0` | Device Error | MP-Bus-Kommunikations-Timeout |
| `1` · `2` · `3` | Device Error | Parity-Fehler · falsche Datenlänge · falscher Starttyp |
| `7` | Device Error | Adressierungsfehler: Gerät bereits in Benutzung, Adresse weicht von der Konfiguration ab — **neu adressieren** |
| `49` | Device Error | Befehl nicht erlaubt — „Missing login, login currently not supported by Loxone" |
| `54` | Device Error | fragmentierte Pakete — **„currently not supported by Loxone"** |

Dazu Profile (MP Air/Water Damper, MPL Damper, Smoke Damper, VAV Controller, Datapool
Device), Diagnose-Eingänge und ein Anhang mit den bitcodierten Gerätezuständen
*Device State 1/2/4* sowie den möglichen Werten für *Override Control* und *Command*.

Wer daran arbeitet, liest das PDF direkt — es ist 14 Seiten Codetabellen und hier nicht
sinnvoll zu verdichten. Die XML-Seite der MP-Bus-Vorlagen steht in
[peripherie-objekte-xml.md](peripherie-objekte-xml.md) 5.

---

## Was noch im Archiv liegt

**162 Gerätedatenblätter** (`Datasheet_*.pdf`): Extensions, Air- und Tree-Geräte,
Audioserver, Lautsprecher, AC-Control-Varianten, Relais. Sie enthalten Klemmenbelegung,
Stromaufnahme und Montagehinweise — Hardwarewissen, das dieser Skill bewusst nicht
abbildet, das aber offline verfügbar ist.

Außerdem: `MatterPlugin_Alpha.pdf`, `Thermal_Shutdown_Temperatures.pdf`,
`SIA_DC-09_Setup.pdf` (Alarmübertragung), `Folder_*`-Datenblätter Dritter sowie
Bedienungsanleitungen von Geiger, Peraqua und Leaf.

---

## Quellen

`C:\ProgramData\Loxone\Loxone Config 17.2.8.28\TechDoc\TechDoc_Common.zip`, ausgepackt und
ausgewertet am 18.09.2026. Alle Zitate wörtlich aus den genannten PDFs.
