# Sonos in Loxone einbinden

Stand 18.09.2026. Loxone-Seite **lokal verifiziert an Loxone Config 17.2.8.28**
(TechDoc `sys_DEU.zip`, `Treesort.xml`, `Templates/FactoryPresets.xml`, `ap_control.json`).
Alles, was Drittsoftware betrifft, ist `[COMMUNITY]` — Herstellerangaben, nicht nachgemessen.

---

## 1. Der Ausgangsbefund: Loxone kennt Sonos nicht

**[VERIFIZIERT 18.09.2026]** `grep -ril "sonos"` über die **komplette** Installation
`C:\ProgramData\Loxone\Loxone Config 17.2.8.28\` liefert **genau eine** Datei:
`ForbiddenPasswords.txt`, Zeilen 25405/25406 (`sonos`, `sonos123`) — die Sperrliste
schwacher Kennwörter. In der offiziellen Bausteindoku (`sys_DEU.zip`, 738 kB entpackt)
kommt „Sonos" **null** Mal vor, „Airplay" viermal.

Daraus folgt der Satz, mit dem jede Sonos-Planung anfangen muss:

> **Es gibt keinen Sonos-Treiber, kein Sonos-Gerät und keinen Sonos-Baustein in Loxone
> Config.**

Das ist keine Lücke, die ein Update schließt: Der Audioserver ist Loxones eigenes Produkt.
**[COMMUNITY]** Loxone-Support verweist bei Sonos-Anfragen auf den Kauf eines Audioservers
([loxforum](https://www.loxforum.com/forum/hardware-miniserver-extensions/16956-sonos-system-and-loxone)).

**Der Audioserver kann Sonos-Lautsprecher nicht ansteuern.** Auch nicht über Umwege —
seine Ausgänge sind physische Verstärkerkanäle (`AudioOut` an `AudioServer`/`MusicExt`).

### Aber: Loxone veröffentlicht sehr wohl eine Sonos-Vorlage

**[VERIFIZIERT 18.09.2026]** In der [Loxone Library](https://library.loxone.com/detail/sonos-speakers-28/overview)
steht unter `sonos-speakers-28` eine Vorlage, deren **Ersteller „LOXONE" ist**.

| | |
|---|---|
| Downloads | **19.168 — die meistheruntergeladene Integration der gesamten Library** |
| Version | 1.0.1 vom 16.12.2021 („Correction of analog outputs adapted") |
| Zertifiziert | **nein** |
| Form | `.LxAddon` = ein `VirtualOut` mit 19 Befehlen, UPnP/SOAP auf Port 1400 |
| Bewertung | 5,0 aus 2 Stimmen |

Loxones eigene Beschreibung, wörtlich:

> „This is a HTTP integration for a sonos speaker bassed on the API V1. Keep in mind that
> updated API versions may lead to functions not working. The Sonos S2 update, released
> June 2020, still works with this API integration. But, it might stop working in the
> future if or when Sonos decide to drop the API support (or UPNP) as the control
> protocol. Default port is 1400."

**Das ändert die Lage weniger, als es klingt.** Die Vorlage ist Weg D aus Abschnitt 6 in
Fertigform: virtuelle Ausgänge, kein Rückkanal, keine Favoriten, keine Gruppen, kein TTS.
Loxone schreibt den Vorbehalt selbst dazu und hat sie seit Dezember 2021 nicht angefasst.
Details und die vollständige Befehlsliste: **Abschnitt 6**.

Der Satz oben bleibt also richtig — nur genauer gefasst: *In Config ist nichts eingebaut;
was Loxone anbietet, ist eine importierbare Sammlung von SOAP-Aufrufen.*

---

## 2. Die vier Wege im Vergleich

| Weg | Loxone sieht | Aufwand | Bedienung in der Loxone-App | Bruchgefahr |
|---|---|---|---|---|
| **A · Music-Server-Emulation** | echten Music Server, native Zonen-Kacheln | hoch (Server + LMS + Bridge) | vollwertig: Titel, Cover, Favoriten, Gruppen | Loxone-Update **und** Sonos-Update |
| **B · HTTP-Bridge + virtuelle Ausgänge** | virtuelle Aus-/Eingänge, selbstgebaute Kacheln | mittel | selbstgebaut, kein Cover, keine Playlist-Auswahl | Sonos-Update |
| **C · Home Assistant als Brücke** | virtuelle Ein-/Ausgänge (oder gar nichts) | mittel, wenn HA ohnehin läuft | in HA vollwertig, in Loxone rudimentär | HA-/Sonos-Update |
| **D · direkt per UPnP/SOAP** | nur virtuelle Ausgänge | **gering — Loxone liefert die Vorlage** | minimal, kein Rückkanal | am höchsten |

**Empfehlung für Neuanlagen ohne Sonos-Bestand:** Audioserver kaufen. Die Wege A–D sind
Bestandsrettung, keine Systementscheidung. **[COMMUNITY]** Der Betreiber des
Sonos4Loxone-Plugins schreibt selbst: „Die Kombination Loxone, Sonos, Loxberry ist nicht
zertifiziert" ([smarthomeblog](https://smarthomeblog-online.de/loxone/sonos-in-loxone-das-hat-doch-mal-funktioniert-wie-ist-das-heute/)).

---

## 3. Weg A — Music-Server-Emulation (die sauberste Integration)

### Warum das funktioniert

**[VERIFIZIERT 18.09.2026]** In Config 17.2.8.28 existieren die Music-Server-Geräte
**weiterhin**, obwohl Loxone die Hardware 2020 abgekündigt hat. Aus der TechDoc:

| Name laut TechDoc | ControlType | LxType | Art |
|---|---|---|---|
| Casatunes Music Server | 45 | – | Gerät (Peripherie) |
| Loxone Music Server | 52 | – | Gerät (Peripherie) |
| Music Server Zone | 203 | – | Zone unter dem Gerät |
| Audioserver | 223 | `AudioServer` | Gerät (Peripherie) |
| Audio Kanal | 216 | – | Kanal am Audioserver / Stereo Extension |

Die XML-Typnamen dazu stehen in `SDcard/sys/Treesort.xml`:
`MultiMediaServer` (das Music-Server-Gerät) mit `MusicZone`-Kindern, gegenüber
`AudioServer` mit `AudioOut`/`AudioGroup` und `MusicExt` (Stereo Extension).

Solange Config das Gerät „Loxone Music Server" anlegen kann, kann sich Software als
solcher ausgeben und der Miniserver bekommt **native Zonen-Bausteine**.

### Die Kandidaten

| Projekt | Port | Basis | Sonos-Anbindung | Status |
|---|---|---|---|---|
| [MusicServer4Home (MS4H)](https://music-server.net/) | **7091** | Logitech Media Server + Squeezelite | LMS-to-uPnP-Bridge, Profil „Sonos" je Lautsprecher | gereift, kostenlos |
| [emulated-loxone-music-server](https://github.com/marcelschreiner/emulated-loxone-music-server) | **7091** (7090 intern) | Node.js, HTTP/JSON + WebSocket | direkt (Sonos + Chromecast) | früh, „nicht alles zuverlässig" |
| [loxberry-music-server-interface](https://github.com/mjesun/loxberry-music-server-interface) | **6090 / ab 6091** | Node.js, UDP `<ID>::<COMMAND>::<ARGS>` | keine — nur Gerüst | v1.2.1, LoxBerry-Status **STOPPED** |
| [lox-audioserver „sonn"](https://github.com/lox-audioserver/core) | 7090 (Web-UI) | TypeScript, Docker, Apache-2.0 | kein Sonos-Treiber; nur über AirPlay/Snapcast | 4.0 **beta** |

Alle vier: **[COMMUNITY]**, Angaben der Projekte.

### MS4H einrichten — die Loxone-Seite

**[COMMUNITY]** nach [music-server.net](https://music-server.net/help/):

1. Peripheriebaum → **Audio → Audioserver hinzufügen → Loxone Music Server →
   „Loxone Music Server *x* Zonen"**.
2. Als Adresse `<IP-des-MS4H>:7091` eintragen. Config entfernt den Port bei der
   Standardadresse selbst wieder.
3. Config legt je Zone einen Ausgang an; die zieht man auf eine Seite und bekommt
   den Baustein **Music Server Zone**.
4. Pflichtfeld ist nur der Raumname in den Baustein-Eigenschaften.

**Die Sonos-Lautsprecher kommen bei MS4H nicht direkt, sondern über den LMS hinein:**
Plugin **UPnP/DLNA-Bridge** aktivieren, Profildatei von
`https://raw.githubusercontent.com/philippe44/LMS-to-uPnP/1.0.0/plugin/profiles.xml`
holen, dann **für jeden einzelnen Lautsprecher** das Profil `Sonos` wählen und mit
*Apply* übernehmen. Ohne dieses Profil je Gerät bleibt die Wiedergabe unzuverlässig.

**Bekannte Einschränkung [COMMUNITY]:** Der Ausgang **`Qa`** des Bausteins funktioniert
zwar, beendet aber Gruppen-Events zu früh. Verstärker stattdessen über den
MS4H-PowerManager schalten — „Ihr könnt bis auf einen Ausgang alle Funktionen des Musik
Server Zone - Baustein nutzen."

### Der Baustein, den man dadurch bekommt

`MediaClient` = **Music Server Zone** (ControlType 463).

**[VERIFIZIERT 18.09.2026]** Es ist der **einzige** Audio-Baustein mit einer Klonvorlage:
`Templates/FactoryPresets.xml` enthält ihn dreimal als `<C Type="MediaClient" V="121"
Nio="54">` mit allen 54 Konnektoren. `MusicPlayer`, `MPGroup`, `CentralMusic` und `Media`
haben **keine** Vorlage — weder in FactoryPresets noch in der `bausteinvorlagen.xml`
dieses Skills. Wer eine Music Server Zone per Skript anlegt, nimmt die Vorlage von dort
(zu Vorgehen und `V`-Migration siehe [bausteine.md](bausteine.md) und Falle 3 in SKILL.md).

Konnektoren mit Vorgabewerten aus der Vorlage:

```
SvPower Trigger PowerOn PowerOff VolPlus VolMinus Volume NextSource Source Play Pause
Stop NextSong PrevSong Mute Shuffle Repeat Move Gesture Reset InputDisable DisMv Progress
Alarm Firealarm Bell Buzzer Sleeptimer TTS
DblClk=0.35 VolumeStep=3 RepeatFirst=0.5 RepeatRate=0.2 MoveTimeout=3600 MoveOn=120
MoveIgnore=300 MaxVol=100 DefVol=25 AlarmVol=75 BellVol=50 BuzzVol=50 TTSVol=40
TimeSleep=300 TimeEvent=8 TimeOutOff=30 FRoomOff
Power Vol Src RemSleep OPowerOn OPowerOff RQ RaQ
```

Doku-Kürzel zu diesen XML-Namen: [bausteine-multimedia-kommunikation.md](bausteine-multimedia-kommunikation.md),
Abschnitt *Music Server Zone*.

---

## 4. Weg B — HTTP-Bridge und virtuelle Ausgänge

Eine Bridge im Netz übersetzt HTTP-GET in Sonos-Kommandos. Loxone schickt die GETs über
`VirtualOut` + `VirtualOutCmd` (XML-Attribute siehe
[xml-bearbeitung.md](xml-bearbeitung.md)).

### node-sonos-http-api — die technische Grundlage

[jishi/node-sonos-http-api](https://github.com/jishi/node-sonos-http-api), Port **5005**.
Schema: `http://<bridge>:5005/{Zonenname}/{Aktion}[/{Parameter}]`. **[COMMUNITY]**

| Zweck | Befehl |
|---|---|
| Wiedergabe | `/Küche/play` · `/Küche/pause` · `/Küche/playpause` · `/Küche/next` · `/Küche/previous` |
| Lautstärke | `/Küche/volume/35` · `/Küche/volume/+5` · `/Küche/groupVolume/25` |
| Stumm | `/Küche/mute` · `/Küche/unmute` · `/Küche/togglemute` |
| Favorit / Playlist | `/Küche/favorite/Ö3` · `/Küche/playlist/Frühstück` |
| Gruppieren | `/Küche/join/Wohnzimmer` · `/Küche/leave` |
| Modus | `/Küche/shuffle/on` · `/Küche/repeat/all` · `/Küche/crossfade/on` |
| Sleeptimer | `/Küche/sleep/600` · `/Küche/sleep/off` |
| Line-In | `/Küche/linein` · `/Küche/linein/TV%20Room` |
| Ansage (TTS) | `/Küche/say/Das Essen ist fertig/de-de/60` · `/sayall/Achtung` |
| Klang/Gong (MP3) | `/Küche/clip/klingel.mp3/80` · `/clipall/alarm.mp3` |
| Szene | `/preset/abendessen` (JSON unter `presets/abendessen.json`) |
| Global | `/zones` · `/pauseall` · `/pauseall/5` · `/resumeall` · `/lockvolumes` |
| Zustand lesen | `/Küche/state` (JSON) |

Presets sind der eigentliche Hebel für Loxone: Ein Preset setzt Zonen, Lautstärken,
Favorit, Wiedergabemodus und Gruppierung in **einem** GET — damit wird aus
„Szene Abendessen" ein einziger virtueller Ausgang.

```json
{ "players": [ {"roomName":"Küche","volume":15},
               {"roomName":"Esszimmer","volume":25} ],
  "favorite": "Dinner Jazz",
  "playMode": {"shuffle": true, "repeat": "all"},
  "pauseOthers": true }
```

Firewall: **eingehend** TCP 3500 (Sonos-Events), TCP 5005 (API), UDP 1905;
**ausgehend** TCP 1400, UDP 1900.

### Die fertigen Produkte

| | [Sonos4Loxone](https://wiki.loxberry.de/plugins/sonos4loxone/start) | [SonoX](https://sonox.net/) |
|---|---|---|
| Form | LoxBerry-Plugin, kostenlos | LoxBerry-Plugin (SonoX-Pro) **oder** Hutschienen-Appliance, kommerziell |
| Version | 7.1.3, LoxBerry ≥ 3.0 | laufend gepflegt (Stand 2026) |
| URL-Schema | `/plugins/sonos4lox/index.php/?zone=Z&action=A&...` | `http://<IP>:5005/...` (node-sonos-http-api-Pfade) |
| Loxone-Import | vorbereitete XML-Vorlagen für virtuelle Ein-/Ausgänge | `.LxAddOn`-Datei, „Copy Path"-Knopf in der Oberfläche |
| Rückkanal | UDP **oder** MQTT, Sonos-Event-Listener | UDP oder MQTT |
| TTS | VoiceRSS, Amazon Polly, **Piper (offline)**, GoogleCloud, MS Azure, ElevenLabs, ResponsiveVoice | integriert |
| Extras | TV-Monitor (pausiert bei HDMI/SPDIF), Follow-me, Wecker, Klangprofile, Firmware-Update | 10 Klingeltöne, 2 Alarmsignale, Presets, Raumgruppen |
| Grenze | **max. 32 Player**, statische IPs zwingend | – |

Beide: **[COMMUNITY]**, Herstellerangaben.

### Loxone-seitige Fallen bei Weg B

- **„Verbindung nach dem Senden schließen" muss gesetzt sein** (XML: `CloseAfterSend` am
  `VirtualOut`). **[COMMUNITY]** Sonos4Loxone dokumentiert das ausdrücklich: sonst wird
  eine TTS-Ansage **doppelt** ausgeführt.
- **Analog- statt Digitalausgang**, sobald ein Loxone-Wert in die URL soll: Haken
  „Als Digitalausgang verwenden" entfernen (XML: `Analog` am `VirtualOutCmd`), Platzhalter
  `<v>` in die URL. Mit gesetztem Haken wird der URL-Text statisch gesendet.
- **URL-Kodierung.** Zonennamen mit Umlaut oder Leerzeichen müssen kodiert werden
  (`Bad%20EG`). Ein unkodiertes Leerzeichen bricht den GET.
- **Der Eingang `I` eines `VirtualOutCmd` lässt sich direkt aus der Logik speisen** — es
  braucht kein Referenzobjekt. Aber: wird derselbe Befehl später per Drag&Drop als
  Ausgangsreferenz auf eine Seite gezogen, **ersetzt** das die bestehende Verbindung
  (dokumentierter Datenverlust, siehe [xml-bearbeitung.md](xml-bearbeitung.md)).

### Rückweg: Sonos-Zustand nach Loxone

Die Bridge schickt Zustandsänderungen (Titel, Interpret, Play/Pause, Lautstärke,
Gruppierung) per **UDP** an den Miniserver. Loxone-seitig:

- `VirtualInUdp` mit `Port`, darunter je Wert ein `VirtualInUdpCmd` mit **Befehlserkennung**
  (`\v` = Wert, `\iText\i` = springe zu Text …, vollständige Syntax in
  [bausteine-multimedia-kommunikation.md](bausteine-multimedia-kommunikation.md),
  Abschnitt *Befehlserkennung*).
- Für Titel/Interpret **virtuelle Texteingänge**, damit der Text in der Visualisierung
  landet.

Wer statt UDP MQTT wählt, braucht zusätzlich das LoxBerry-MQTT-Gateway — ein Bauteil mehr
in der Kette, das Loxone nicht kennt.

---

## 5. Weg C — Home Assistant als Brücke

Sinnvoll, wenn HA ohnehin läuft. HA hat eine **native, gepflegte Sonos-Integration** — die
mit Abstand beste Sonos-Unterstützung aller hier genannten Wege.

### Was HA auf der Sonos-Seite kann [COMMUNITY]

Quelle [home-assistant.io/integrations/sonos](https://www.home-assistant.io/integrations/sonos/):
`media_player`-Entität je Gerät, Snapshot/Restore, Queue-Verwaltung, Sleeptimer,
Sonos-Wecker als Schalter, Sensoren für Favoriten, Batterie und Audio-Eingang,
`announce`/TTS mit eigener Lautstärke.

Netzwerk: **TCP 1400** eingehend zu HA für Push-Events (sonst bis 1500 durchprobiert),
**TCP 1443** für `announce`/TTS. **UPnP muss am Sonos-System eingeschaltet sein** — sonst
`403 Client Error: Forbidden`.

### Music Assistant — der „Music Server von HA"

[Music Assistant](https://www.music-assistant.io/) ist die Multiroom-Schicht über HA:
Bibliothek, Streamingdienste, Warteschlangen, Gruppen, Ansagen.

**Für Sonos wichtig [COMMUNITY]:** Sonos-S2-Lautsprecher gehören zu den **einzigen**
Playertypen mit *nativen Ansagen* — die Ansage wird über die laufende Musik gelegt, die
Musik geduckt, danach die Lautstärke wiederhergestellt. Bei allen anderen Playern wird die
Wiedergabe unterbrochen und neu gestartet. Wer Klingel- und Alarmansagen über Sonos fahren
will, bekommt hier die technisch beste Umsetzung —
[Play Announcement Action](https://www.music-assistant.io/faq/massannounce/).

### Die Loxone-Seite anbinden

**Richtung Loxone → HA** (Auslöser: Klingel, Alarm, Präsenz, Taster):
virtueller Ausgang auf die HA-REST-API, oder — sauberer — HA liest den Miniserver über
[PyLoxone](https://github.com/JoDehli/PyLoxone) per WebSocket mit und reagiert in einer
Automatisierung.

**Richtung HA → Loxone** (Titel/Status zurück in die Visualisierung):
PyLoxone kann direkt auf einen **virtuellen Eingang (VI)** bzw. **virtuellen Texteingang
(VTI)** schreiben — `{"uuid":"<UUID>","value":"pulse"}`. **[COMMUNITY]**

**Grenze:** In der Loxone-App bleibt es bei selbstgebauten Kacheln. Wer die native
Musikkachel will, braucht Weg A.

---

## 6. Weg D — direkt per UPnP/SOAP (Loxones eigene Vorlage)

Ohne Zusatzgerät, mit `VirtualOut` auf `http://<sonos-ip>:1400` und
`CmdOnPost`/`CmdOnHTTP` (SOAP-Envelope im POST-Body, `SOAPAction`-Header).
**Diesen Weg muss man nicht selbst bauen — Loxone liefert ihn fertig.**

### Die offizielle Vorlage holen und einspielen

```bash
curl -L -o Sonos.LxAddon https://api.library.loxone.com/downloader/config/sonos-speakers-28
```

Doppelklick auf die Datei, oder in Config über **„Vorlage importieren…"**
(→ [library-loxone-com.md](library-loxone-com.md)).

**Danach zwingend die Adresse ändern.** Die Vorlage trägt die IP des Einreichers:
`Address="http://192.168.1.232:1400"`. Je Lautsprecher eine eigene Kopie — die Vorlage
kennt keine Zonen.

### Was drinsteht

**[VERIFIZIERT 18.09.2026]** aus `sonos-speakers.xml` der Vorlage 1.0.1
(`templateType="3"`, `minVersion="12031214"` = Config 12.3.12.14):

Wurzel: `<VirtualOut Title="Sonos" Address="http://192.168.1.232:1400"
CloseAfterSend="true" CmdSep="">` — **`CloseAfterSend` ist gesetzt**, genau wie in
Abschnitt 4 als Falle beschrieben. Alle 19 Befehle sind `POST`.

| Befehl | Dienst | SOAP-Aktion | `Analog` |
|---|---|---|---|
| Play · Pause · Stop | AVTransport | `Play` · `Pause` · `Stop` | – |
| Next Track · Previous Track | AVTransport | `Next` · `Previous` | – |
| No Shuffle No Repeat · No Shuffle Repeat All · Shuffle No Repeat · Shuffle Repeat All | AVTransport | `SetPlayMode` | – |
| Sleep Timer 15 Minutes · 30 Minutes · 1 Hour | AVTransport | `ConfigureSleepTimer` | – |
| Mute · Unmute | RenderingControl | `SetMute` | – |
| **Volume** | RenderingControl | `SetVolume` | **ja** |
| **Bass** · **Treble** | RenderingControl | `SetBass` · `SetTreble` | **ja** |
| Volume Up · Volume Down | RenderingControl | `SetRelativeVolume` | – |

Control-URLs: `/MediaRenderer/AVTransport/Control` und
`/MediaRenderer/RenderingControl/Control`, `SOAPAction`-Header im Format
`"urn:schemas-upnp-org:service:{Service}:1#{Action}"`. Discovery über SSDP
`239.255.255.250:1900`; den neueren Endpunkt `https://{ip}:1443/api` dokumentiert Sonos
nicht ([sonos.svrooij.io](https://sonos.svrooij.io/sonos-communication)).

### Was fehlt

Die drei Wiedergabemodus-Befehle und die Sleeptimer sind fest verdrahtete Varianten
desselben SOAP-Aufrufs — das ist der ganze Funktionsumfang. **Nicht enthalten:**
Quellenauswahl, Favoriten, Playlisten, Gruppierung, TTS, Ansagen, und **jede Form von
Rückmeldung**. Loxone weiß mit dieser Vorlage nie, ob überhaupt etwas spielt.

**Warum das trotzdem selten die richtige Wahl ist:**

- Kein Rückkanal. Ohne Event-Subscription (die der Miniserver nicht leisten kann) weiß
  Loxone nie, was gerade läuft.
- Gruppen/Zonen muss man von Hand nachbilden.
- Jede Quellenauswahl braucht eine vollständige URI im `SetAVTransportURI` — Favoriten
  gibt es nicht.
- Es ist der Weg, der von Sonos-Firmware-Änderungen am direktesten getroffen wird.

Vertretbar für **genau eine** Sache: einen Gong oder eine MP3 auf einen einzelnen
Lautsprecher werfen. Für alles andere ist eine Bridge weniger Arbeit.

---

## 7. Die Sonos-seitigen Fallen (gelten für **alle** Wege)

### Connection Security — die größte offene Flanke

**[COMMUNITY]** [Sonos Support](https://support.sonos.com/en/article/adjust-connection-security-settings):
Sonos-App → **Account → Privacy & Security → Connection Security**.

| Schalter | Standard | Wirkung beim Umstellen |
|---|---|---|
| **Authentication** | **AUS** | EIN ⇒ Drittanbieter-Integrationen über Cloud **und LAN-API** müssen sich authentifizieren. Betrifft ausdrücklich auch AirPlay. **Jede** hier beschriebene Bridge steht danach still. |
| **UPnP** | **AN** | AUS ⇒ UPnP-basierte Integrationen tot; **auch die Sonos-App für macOS/Windows**. HA meldet dann `403 Forbidden`. |
| **Guest Access** | **AN** | AUS ⇒ Gäste im WLAN können nicht mehr steuern |

Die Vorgaben sind heute integrationsfreundlich. Aber: **Diese Schalter sitzen in der App
des Kunden, nicht in der Anlage.** Ein Kunde, der „die Sicherheit erhöht", legt die
komplette Musikintegration still, ohne dass es irgendwo eine Fehlermeldung gibt.
Das gehört in die Übergabedokumentation.

### Weitere

- **Statische IPs.** Sonos4Loxone adressiert über IP (daher auch die Grenze von 32
  Playern). Eine DHCP-Verlängerung, die eine andere Adresse vergibt, bricht die Zone.
- **Multicast muss durchs Netz.** SSDP `239.255.255.250:1900` — bei getrennten VLANs,
  managed Switches mit IGMP-Snooping oder WLAN-Isolation findet die Bridge nichts.
- **IPv6 [COMMUNITY]:** Sonos4Loxone empfiehlt, IPv6 im Router abzuschalten, sonst
  scheitert die MP3-Wiedergabe.
- **Alte Sonos-Netzwerkmodi** (Sonos Bridge/Boost-Netz „SonosNet") sollen weg; Sonos hat
  die Unterstützung für alte Netzwerke 2025 eingestellt.
- **TTS braucht Internet**, außer bei Piper (offline) in Sonos4Loxone.

---

## 8. Welcher Loxone-Baustein wofür

**[VERIFIZIERT 18.09.2026]** aus TechDoc, `Treesort.xml` und `ap_control.json`:

| Baustein (GUI) | XML-Typ | ControlType | Visu-/API-Typ | braucht |
|---|---|---|---|---|
| Music Server Zone | **`MediaClient`** | 463 | `AudioZone` | Gerät `MultiMediaServer` (Music Server / Emulation) |
| Audio Player | **`MusicPlayer`** | 507 | `AudioZoneV2` | Gerät `AudioServer` + `AudioOut` |
| Audio Player Gruppe fix | `MPGroup` | 508 | `AudioPlayerGroup` | Audioserver |
| Audio Zentral | `CentralMusic` | 491 | `CentralAudioZone` | – |
| **Medien-Steuerung** | **`Media`** | 462 | – | **nichts** |

### Der unterschätzte Baustein: Medien-Steuerung (`Media`)

Der einzige Audio-nahe Baustein, der **kein Loxone-Audiogerät voraussetzt** — und damit
der passende Rahmen für Weg B und D, wenn man eine ordentliche Kachel statt loser Taster
will. Vollständige Konnektortabellen im Katalog:
[bausteine-multimedia-kommunikation.md](bausteine-multimedia-kommunikation.md),
Abschnitt *Mediensteuerung*.

**Die KB beschreibt ihn als IR-Steuerung** („Integration mit IR-Aktoren"). Dass seine
Ausgänge stattdessen einen `VirtualOutCmd` speisen können, ist **[ABGELEITET]**: Der
Baustein hat keine Gerätebindung, seine Ausgänge sind gewöhnliche Konnektoren. Vor
produktivem Einsatz einmal an der Anlage nachstellen.

XML-Namen zu den Doku-Kürzeln der KB-Tabellen **[BELEGT-TECHDOC]** (ControlType 462):

| Art | XML-Name | Kürzel |
|---|---|---|
| E | `Power` / `PowerOn` / `PowerOff` | Ptg / Pon / Poff |
| E | `VolPlus` / `VolMinus` / `Volume` | V+ / V- / V |
| E | `PrgPlus` / `PrgMinus` / `Program` | Ch+ / Ch- / Ch — für Sonos naheliegend: Favoriten-Index |
| E | `Mode` / `Modus%d` | Mode / M*n* |
| E | `Gesture` / `Reset` / `Disable` | T5 / Off / DisPc |
| A | `AQm` / `AQp` / `Output%d` / `OutputAPI` | M / P / O*n* / API |
| P | `Remanence` / `TimeNum` / `DblClk` | Rem / Nst (3000 ms) / Tdc (0,35 s) |

**Was er nicht kann:** Titel, Interpret, Cover, Warteschlange, Favoritenliste. Dafür
gibt es nur die Music Server Zone — also nur Weg A.

### API-Kommandos einer Music Server Zone

**[VERIFIZIERT 18.09.2026]** aus `ap_control.json`, Eintrag
`controlType: ["MediaClient","AudioZone"]`, `intType: 463`. Das sind die Befehle, die eine
Visualisierung oder ein API-Client (App, Home Assistant) an die Zone schicken kann:

| Aktion | Typ | Bereich |
|---|---|---|
| `play` · `pause` · `next` · `prev` | Impuls | – |
| `playZoneFav/<n>` | analog | 0…8 |
| `volume/<n>` | analog | 0…100 % |
| `volume/+<n>` · `volume/-<n>` | analog | 0…20 % |
| `tts/<text>` | Text | mehrzeilig |

Für Weg C ist das die Gegenrichtung: Wer eine emulierte Zone betreibt, kann sie aus Home
Assistant über genau diese Kommandos fernsteuern.

---

## 9. Kurzentscheidung

- **Sonos-Bestand, Kunde will die Loxone-App wie bei einem Audioserver bedienen**
  → Weg A, MS4H. Rechne mit einem halben Tag Einrichtung und einem Dauergerät im Netz.
- **Es reicht: Play/Pause/Lautstärke je Lautsprecher, sonst nichts**
  → Weg D, Loxones eigene Vorlage importieren. Zehn Minuten Arbeit, kein Zusatzgerät.
- **Sonos-Bestand, es reicht: Klingel, Alarm, Ansage, Musik-An-Aus je Raum**
  → Weg B, Sonos4Loxone (kostenlos) oder SonoX (Support und Appliance, kommerziell).
  Weg D kann **keine** Ansagen und keinen Gong.
- **Home Assistant ist ohnehin da**
  → Weg C. Für Ansagen zusätzlich Music Assistant — Sonos S2 kann dort als einer von
  wenigen Playertypen native, geduckte Ansagen.
- **Neubau, noch nichts gekauft**
  → Audioserver. Alles andere ist eine Brücke, die zwei Hersteller unabhängig voneinander
  kaputtmachen können.

---

## Quellen

Lokal verifiziert: `C:\ProgramData\Loxone\Loxone Config 17.2.8.28\` —
`SDcard/sys/sys_DEU.zip`, `SDcard/sys/Treesort.xml`, `Templates/FactoryPresets.xml`,
`ap_control.json`, `ap_control_DEU.json`, `ForbiddenPasswords.txt`.

Web, alle abgerufen am 18.09.2026:
[Sonos4Loxone](https://wiki.loxberry.de/plugins/sonos4loxone/start) ·
[SonoX](https://sonox.net/docs/) ·
[node-sonos-http-api](https://github.com/jishi/node-sonos-http-api) ·
[MusicServer4Home](https://music-server.net/help/) ·
[emulated-loxone-music-server](https://github.com/marcelschreiner/emulated-loxone-music-server) ·
[lox-audioserver](https://github.com/lox-audioserver/core) ·
[loxberry-music-server-interface](https://github.com/mjesun/loxberry-music-server-interface) ·
[HA Sonos](https://www.home-assistant.io/integrations/sonos/) ·
[Music Assistant Announcements](https://www.music-assistant.io/integration/announcements/) ·
[PyLoxone](https://github.com/JoDehli/PyLoxone) ·
[Sonos Connection Security](https://support.sonos.com/en/article/adjust-connection-security-settings) ·
[Sonos-Protokoll](https://sonos.svrooij.io/sonos-communication) ·
[smarthomeblog](https://smarthomeblog-online.de/loxone/sonos-in-loxone-das-hat-doch-mal-funktioniert-wie-ist-das-heute/)
