# Multimedia & Kommunikation

Teil des Loxone-Baustein-Katalogs. Quelle: offizielle Loxone-Dokumentation (kb-cat/config-functionblock), Stand 30.07.2026.

Legende: [BELEGT] = woertlich aus der KB - [ABGELEITET] = geschlossen - [OFFEN] = unbekannt, nicht geraten.

---

### Audio Player

Dieser Baustein steuert die Audiowiedergabe auf einem Loxone-Audiosystem. Er ermöglicht die Kontrolle von Lautstärke, Wiedergabe, Favoriten und verschiedenen Tonarten (Alarm, Klingel, Wecker).

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/audio-player/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| V+ | Volume+ | Erhöht die Lautstärke um den im Parameter (Vsts) eingestellten Wert. Doppelklick wählt den nächsten Favoriten aus. | - | 0/1 |
| V- | Volume- | Verringert die Lautstärke um den im Parameter (Vsts) eingestellten Wert. Doppelklick schaltet den Player aus. | - | 0/1 |
| V | Set volume | Ist der Player ausgeschaltet, wird die Wiedergabe automatisch gestartet. | % | 0...100 |
| Play | Play | - | 0/1 | 0/1 |
| Pause | Pause | - | 0/1 | 0/1 |
| P | Presence | Startet die Wiedergabe, wenn 1. | - | 0/1 |
| Prev | Previous track | Vorheriger Titel | - | 0/1 |
| Next | Next track | Nächster Titel | - | 0/1 |
| Fav | Set favorite | Wählt den Favorit anhand der zugewiesenen ID Nummer. Wenn die gewählte ID nicht existiert, wird der erste Favorit ausgewählt. | - | ∞ |
| Alarm | Alarm | Alarmton abspielen mit der in Parameter (Va) festgelegten Lautstärke. | - | 0/1 |
| FireAlarm | Fire alarm | Feueralarmton abspielen mit der in Parameter (Va) festgelegten Lautstärke. | - | 0/1 |
| Bell | Bell | Klingelton abspielen mit der in Parameter (Vbell) festgelegten Lautstärke. | - | 0/1 |
| Buzzer | Buzzer | Startet die in den Eigenschaften angegebene Wecker-Aktion. Wenn die Aktion "Wecker-Ton" ausgewählt ist, wird dieser mit der im Parameter (Vbuzzer) eingestellten Lautstärke abgespielt. | - | 0/1 |
| LineIn | Set Line In | Wählt den Line In eines Audioservers als Quelle anhand seiner Line In ID aus. | - | 0...∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge V+, V-, V, Play, Pause, Prev, Next, Fav, Bell, Buzzer, T5, TTS, Cs, BTp wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |
| DisP | Disable presence | Solange dieser Eingang aktiv ist, wird jede Änderung des Wertes am Eingang (P) ignoriert. | - | 0/1 |
| T5 | T5 control | Button 2: Volume up; double-click selects the next favorite. Button 5: Volume down; double-click pauses playback. A single click on button 2 or 5 starts playback when the player is off. Button 3: Double-click activates (2C); triple-click activates (3C); (Roff) = 0: pauses playback. | - | ∞ |
| TTS | Text to speech | Wandelt einen Text in Sprache um, und spielt ihn mit der im Parameter (Vtts) eingestellten Lautstärke ab. | - | - |
| Rtd | Reset to default | Setzt Parameter und Einstellungen des Bausteins auf die Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Tg | Toggle | Wechselt zwischen Play und Pause | - | 0/1 |
| Cs | Custom sound | Spielt den benutzerdefinierten Sound [Dateiname] mit der Lautstärke [vol] ab. Z.B. soundcheck.mp3:80 [Dateiname]:[vol] Benutzerdefinierte Sounds müssen auf der SD-Karte des Audioservers im Ordner Event_Sounds gespeichert sein! Nur mp3-Dateien werden unterstützt. | - | - |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/audio-player/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Stereo LR | Stereo Left & Right | Gibt das vollständige Stereo Signal aus | 0/1 |
| Play | Play status | 1 wenn der Player gerade spielt | 0/1 |
| Volume | Current volume | Aktuelle Lautstärke | ∞ |
| 2C | Pulse on double-click | Impuls bei einem Doppel- oder Dreifachklick oder Impuls bei Eingang (Off). | 0/1 |
| 3C | Pulse on triple-click | Impuls bei einem Dreifach-Klick. | 0/1 |
| Stereo L | Stereo Left | Gibt den linken Kanal des abgespielten Stereo Signals aus. | 0/1 |
| Stereo R | Stereo Right | Gibt den rechten Kanal des abgespielten Stereo Signals aus. | 0/1 |
| V+ | Pulse on Volume+ | Die Funktion ist nur aktiviert, wenn Stereoausgänge mit extern gesteuertem "Lautstärke-Modus" angeschlossen sind. | 0/1 |
| V- | Pulse on Volume- | Die Funktion ist nur aktiviert, wenn Stereoausgänge mit extern gesteuertem "Lautstärke-Modus" angeschlossen sind. | 0/1 |
| Sub | Subwoofer | Gibt den Subwoofer-Kanal des Stereosignals aus. Dieser Ausgang kann nur mit Master/Client-Subwoofern verwendet werden. | 0/1 |
| BTp | Bluetooth Pairing | Solange dieser Ausgang aktiv ist, ist die Bluetooth-Kopplung möglich. Während dieser Zeit können alle Bluetooth-fähigen Loxone-Geräte mit einem Smartphone oder anderen Bluetooth-fähigen Geräten gekoppelt werden. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/audio-player/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Von | Power on volume | Lautstärke, wenn die Wiedergabe gestartet oder fortgesetzt wird. -1 = Speichert die letzte Lautstärkeeinstellung als Startlautstärke. | % | -1...100 | 10 |
| Vm | Maximum volume | Einstellung der Maximallautstärke | % | 0...100 | 100 |
| Vsts | Step size volume | Verringert die Lautstärke um den im Parameter (Vsts) eingestellten Wert. Doppelklick schaltet den Player aus. | % | 1...100 | 1 |
| Va | Minimum volume alarm sounds | Wenn die aktuelle Wiedergabelautstärke höher ist, wird diese anstelle der Mindestlautstärke verwendet. | % | 0...100 | 75 |
| Vbell | Minimum volume doorbell | Wenn die aktuelle Wiedergabelautstärke höher ist, wird diese anstelle der Mindestlautstärke verwendet. | % | 0...100 | 40 |
| Vbuzzer | Minimum volume alarm clock | Wenn die aktuelle Wiedergabelautstärke höher ist, wird diese anstelle der Mindestlautstärke verwendet. | % | 0...100 | 10 |
| Vtts | Minimum volume TTS and announcements | Wenn die aktuelle Wiedergabelautstärke höher ist, wird diese anstelle der Mindestlautstärke verwendet. | % | 0...100 | 20 |
| Tdc | Time double-click | Zeit für Doppelklick | s | 0...10 | 0.35 |
| Roff | Ignore room off command | Raum/Haus-Aus-Geste mit T5 (Taste 3) Ignorieren | - | 0/1 | 0 |
| BuzzerFav | Alarm clock favorite | ID des Raumfavoriten für Wecker, falls die Wecker-Option Raumfavorit verwendet wird. | - | ∞ | 1 |
| BTp | Bluetooth pairing | Solange dieser Eingang aktiv ist, ist eine Bluetooth-Kopplung möglich. Während dieser Zeit können alle Bluetooth-fähigen Loxone-Geräte z.B. mit einem Smartphone oder anderen Bluetooth-fähigen Geräten gekoppelt werden. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 | 0 |
| Ft | Volume Fading Time | Lautstärkeanpassungen über den Eingang (V) werden innerhalb der konfigurierten Fadingzeit angewendet, wenn der Player bereits aktiv ist. Die Fadingzeit gilt auch für den Eingang (Buzzer). 0 = Kein Fading; Lautstärkeänderungen erfolgen sofort. | s | 15...1800 | 0 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/audio-player/

| Kurzbeschreibung | Beschreibung | Standardwert |
|------------------|-------------|--------------|
| Wecker-Aktion | Aktion, die beim Aktivieren des Weckers ausgeführt werden soll | - |
| Airplay aktivieren | Aktivieren Sie AirPlay für diesen Player. Die Option ist nicht verfügbar, wenn Musikdienste von einer Player-Gruppe verwaltet werden. | - |
| Spotify Connect aktivieren | Aktivieren Sie Spotify Connect für diesen Player. Die Option ist nicht verfügbar, wenn Musikdienste von einer Player-Gruppe verwaltet werden. | - |
| Raumfavoritenpriorität | Wenn aktiviert, wird immer der erste Raumfavorit verwendet, wenn der Player aktiviert wird. | - |
| Anzahl der Aktivitätseinträge | Anzahl der Einträge im Aktivitätsprotokoll. 0: Protokoll ist deaktiviert. Das Aktivitätsprotokoll zeichnet relevante Änderungen seit dem Programmstart auf. | 0...100 | 20 |
| Player-ID | ID des Players auf dem Audioserver oder Audiogerät | ∞ | - |
| Automatischer Hochpassfilter | Wenn ein Subwoofer an den Audio Player angeschlossen ist, stellen alle anderen Lautsprecher automatisch die Wiedergabe von Bassfrequenzen ein, wodurch ihre Belastung reduziert wird. Dieses Verhalten kann deaktiviert werden, indem das entsprechende Kontrollkästchen deaktiviert wird. Dadurch geben alle angeschlossenen Lautsprecher den gesamten Frequenzbereich wieder. | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/audio-player/

- **TTS-Funktion:** "Für die TTS Funktion ist eine Internetverbindung notwendig. Es werden Texte mit jeweils bis zu 400 Zeichen (mit Leerzeichen) unterstützt."
- **Bluetooth:** "Nur in Kombination mit Master-Lautsprechern oder Wireless Speaker verfügbar."
- **Benutzerdefinierte Sounds:** "Ein benutzerdefinierter Sound wird vollständig abgespielt und kann nicht gestoppt werden."
- **Verzögerung benutzerdefinierte Sounds:** "Alle benutzerdefinierten Sounds haben eine Verzögerung von 2 Sekunden, bedingt durch die erforderliche Synchronisationszeit vor der Wiedergabe."
- **SMB1-Protokoll:** "Die SD-Karten-Ordner verwenden das SMB1-Protokoll, das unter Windows 10 und 11 standardmäßig nicht mehr aktiviert ist."

Quelle: https://www.loxone.com/dede/kb/audio-player/

---

### Audio Player Gruppe fix

Dieser Baustein gruppiert mehrere Audio Player und ermöglicht deren gemeinsame Steuerung. Damit lassen sich mehrere Player synchronisiert steuern.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| V+ | Volume+ | Erhöht die Lautstärke um den im Parameter (Vsts) eingestellten Wert. Doppelklick wählt den nächsten Favoriten aus | — | 0/1 |
| V- | Volume- | Verringert die Lautstärke um den im Parameter (Vsts) eingestellten Wert. Doppelklick schaltet den Player aus | — | 0/1 |
| V | Set volume | Wenn die zugeordneten Audio Player auf verschiedene Lautstärken eingestellt sind, übernehmen bei einer Lautstärkeänderung nur die lautesten Player den neuen Wert, alle anderen Player folgen zwar entsprechend, behalten dabei aber das Lautstärkeverhältnis | % | 0...100 |
| Play | Play | — | — | 0/1 |
| Pause | Pause | — | — | 0/1 |
| P | Presence | Startet die Wiedergabe, wenn 1 | — | 0/1 |
| Prev | Previous track | Vorheriger Titel | — | 0/1 |
| Next | Next track | Nächster Titel | — | 0/1 |
| Fav | Set favorite | Wählt den Favorit anhand der zugewiesenen ID Nummer. Wenn die gewählte ID nicht existiert, wird der erste Favorit ausgewählt | — | ∞ |
| Alarm | Alarm | Alarmton abspielen mit der in Parameter (Va) festgelegten Lautstärke | — | 0/1 |
| FireAlarm | Fire alarm | Feueralarmton abspielen mit der in Parameter (Va) festgelegten Lautstärke | — | 0/1 |
| Bell | Bell | Klingelton abspielen mit der in Parameter (Vbell) festgelegten Lautstärke | — | 0/1 |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input | — | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge V+, V-, V, Play, Pause, Prev, Next, Fav, Bell, Buzzer, T5, TTS, Cs, BTp wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich | — | 0/1 |
| DisP | Disable presence | Solange dieser Eingang aktiv ist, wird jede Änderung des Wertes am Eingang (P) ignoriert | — | 0/1 |
| T5 | T5 control | Button 2: Volume up; double-click selects the next favorite. Button 5: Volume down; double-click pauses playback. A single click on button 2 or 5 starts playback when the player is off. Button 3: Double-click activates (2C); triple-click activates (3C); (Roff) = 0: pauses playback | — | ∞ |
| TTS | Text to speech | Wandelt einen Text in Sprache um, und spielt ihn mit der im Parameter (Vtts) eingestellten Lautstärke ab | — | — |
| LineIn | Set Line In | Wählt den Line In eines Audioservers als Quelle anhand seiner Line In ID aus | — | 0...∞ |
| Cs | Custom sound | Spielt den benutzerdefinierten Sound [Dateiname] mit der Lautstärke [vol] ab. Z.B. soundcheck.mp3:80 [Dateiname]:[vol] Benutzerdefinierte Sounds müssen auf der SD-Karte des Audioservers im Ordner Event_Sounds gespeichert sein! Nur mp3-Dateien werden unterstützt | — | — |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Tdc | Time double-click | Zeit für Doppelklick | s | 0...10 | 0.35 |
| Roff | Ignore room off command | Raum/Haus-Aus-Geste mit T5 (Taste 3) Ignorieren | — | 0/1 | 0 |
| BTp | Bluetooth pairing | Solange dieser Eingang aktiv ist, ist die Bluetooth-Kopplung verfügbar. Während dieser Zeit können alle Bluetooth-fähigen Loxone-Geräte z.B. mit einem Smartphone oder anderen Bluetooth-fähigen Geräten gekoppelt werden. Der Eingang ist nur sichtbar, wenn Dienste und Bluetooth von der Player Gruppe verwaltet werden. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar | — | 0/1 | 0 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

| Kürzel | Kurzbeschreibung | Beschreibung | API |
|--------|------------------|-------------|-----|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | — |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

| Kurzbeschreibung | Beschreibung | Standardwert | Auswahl |
|--------|------------------|-------------|--------|
| Alle ausgewählten Bausteine können gemeinsam gesteuert werden | Alle ausgewählten Bausteine können gemeinsam gesteuert werden | — | — |
| Airplay aktivieren | AirPlay für alle Player dieser Gruppe aktivieren | — | — |
| Spotify Connect aktivieren | Spotify Connect für alle Player dieser Gruppe aktivieren | — | — |
| Dienste durch Gruppe verwalten | Wenn Dienste von einer Player-Gruppe gehandhabt werden, sind die konfigurierten Audio Player in Airplay und Spotify Connect nicht sichtbar | — | — |
| Raumfavoritenpriorität | Wenn aktiviert, wird immer der erste Raumfavorit verwendet, wenn der Player aktiviert wird | — | — |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

Keine dokumentierten Warnungen oder Fallstricke vorhanden.

Quelle: https://www.loxone.com/dede/kb/audio-player-gruppe-fix/

---

### Audio Zentral

Dieser Baustein ermöglicht die zentrale Steuerung aller Audio Player und Music Server Zonen in einem Loxone-System.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/audio-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| TgZ | Toggle Zone | Wechselt Zone zwischen Aus und Ein | - | 0/1 |
| Zon | Zone On | Trigger Zone Ein | - | 0/1 |
| Zoff | Zone Off | Trigger Zone Aus; Wird eine Playliste abgespielt, wird die Wiedergabe mit Play am Anfang des Titels gestartet. | - | 0/1 |
| V+ | Volume+ | Erhöht die Lautstärke um den Parameter (Vsts); Doppelklick wählt nächsten Favoriten. | - | 0/1 |
| V- | Volume- | Verringert die Lautstärke um Parameter (Vsts); Doppelklick schaltet Player aus. | - | 0/1 |
| V | Set volume | Bei verschiedenen Lautstärken übernehmen nur lauteste Player neuen Wert, andere folgen und behalten Verhältnis. | % | 0...100 |
| S+ | Next Source / Next zone favorite | Casatunes: nächste Quelle; Loxone/Audioserver: nächster Zonen-Favorit | - | 0/1 |
| Play | Play | - | - | 0/1 |
| AIs | Source / Zone favorite | Analoger Eingang; sichtbar nur bei bestimmten Konfigurationen | - | ∞ / 0...8 |
| Pause | Pause | - | - | 0/1 |
| Stop | Stop playback | Trigger Song stoppen; bei Playliste Wiedergabe am Titelbeginn. | - | 0/1 |
| Shuffle | Shuffle | Trigger Shuffle; nur bei bestimmten Konfigurationen sichtbar. | - | 0/1 |
| Repeat | Repeat | 0=Aus, 1=Playliste fortlaufend, 2=aktuellen Titel wiederholen | - | 0...2 |
| Sleep | Sleep timer input | Zone wird nach Zeit Ts lautlos und ausgeschaltet; wird durch vorzeitiges Ausschalten zurückgesetzt. | - | 0/1 |
| TTS | Text to Speech input | Eingang Sprachausgabe; maximale Textlänge 400 Zeichen | - | - |
| Off | Off / Lock | Pulse (<200ms): Outputs zurücksetzen; Pulse (>200ms): Block gesperrt; Pulse (>500ms): Sensorname in UI. | - | 0/1 |
| Next | Next track | Nächster Titel | - | 0/1 |
| Prev | Previous track | Vorheriger Titel | - | 0/1 |
| T5 | T5 control | Button 2: Lautstärke↑/Doppelklick: nächster Favorit; Button 5: Lautstärke↓/Doppelklick: Pause; Button 3: 2C/3C aktiviert | - | ∞ |
| DisPc | Disable periphery control | Deaktiviert V+, V-, V, Play, Pause, Prev, Next, Fav, Bell, Buzzer, T5, TTS, Cs; Bedienung über Visualisierung möglich. | - | 0/1 |
| DisP | Disable presence | Änderungen am Eingang (P) werden ignoriert. | - | 0/1 |
| Alarm | Alarm | Alarmton abspielen mit Parameter (Va) Lautstärke. | - | 0/1 |
| FireAlarm | Fire alarm | Feueralarmton abspielen mit Parameter (Va) Lautstärke. | - | 0/1 |
| Bell | Bell | Klingelton abspielen mit Parameter (Vbell) Lautstärke. | - | 0/1 |
| Buzzer | Buzzer | Startet Wecker-Aktion; bei "Wecker-Ton" mit Parameter (Vbuzzer) Lautstärke. | - | 0/1 |
| Rtd | Reset to default | Setzt Parameter auf Standardwerte laut Bausteinvorlage zurück. | - | 0/1 |
| Cs | Custom sound | Spielt benutzerdefinierten Sound [Dateiname] mit Lautstärke [vol] ab; Format: soundcheck.mp3:80 | - | - |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/audio-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| API | API Connector | Intelligenter API basierter Verbinder; verknüpft Funktionen zwischen Geräten und Bausteinen. | - |
| Na | Active Audio Players | Anzahl der aktiven Audio Player | ∞ |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/audio-zentral/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Tdc | Time double-click | Zeit für Doppelklick | s | 0...10 | 0.35 |
| Roff | Ignore room off command | Raum/Haus-Aus-Geste mit T5 (Taste 3) ignorieren | - | 0/1 | 0 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/audio-zentral/

| Kurzbeschreibung | Beschreibung | Standardwert | Auswahl |
|--------|------------------|-------------|--------|
| Alle ausgewählten Music Server Zonen und Audio Player können gemeinsam gesteuert werden. | - | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/audio-zentral/

- **Zentral-Befehle und DisPc:** "Zentral-Befehle werden auch durch einen aktiven (DisPc) Eingang am jeweiligen Baustein nicht blockiert."
- **Funktionalitätsabhängigkeit:** "Die am Zentralbaustein nutzbaren Funktionen sind von den verknüpften Bausteinen abhängig, und werden über deren Parameter eingestellt."

Quelle: https://www.loxone.com/dede/kb/audio-zentral/

---

### Music Server Zone

Dieser Baustein steuert eine einzelne Musikzone auf dem Loxone Music Server oder anderen kompatiblen Musikservern.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/music-server-zone/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| TgZ | Toggle Zone | Wechselt Zone zwischen Aus und Ein | - | 0/1 |
| Zon | Zone On | Trigger Zone Ein. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Zoff | Zone Off | Trigger Zone Aus. Wird eine Playliste abgespielt, wird die Wiedergabe mit Play wieder am Beginn des Titels gestartet. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| V+ | Volume | **Casatunes Music Server**: Trigger Lauter. Doppelklick schaltet auf die nächste Quelle. **Loxone Music Server**: Trigger Lauter. Doppelklick schaltet auf den nächsten Zonen-Favorit. **Loxone Music Server Gen 2**: Trigger Lauter. Doppelklick schaltet auf den nächsten Zonen-Favorit. | - | 0/1 |
| V- | Volume | Trigger Leiser. Doppelklick schaltet die Zone aus. | - | 0/1 |
| AIv | Volume level | Analoger Eingang Lautstärke | % | 0...100 |
| S+ | **Casatunes Music Server**: Next Source | Trigger nächste Quelle. **Loxone Music Server**: Next zone favorite. Trigger nächster Zonen-Favorit. Wurde zuletzt eine benutzerdefinierte Auswahl getroffen, wird der erste Zonenfavorit abgespielt. **Loxone Music Server Gen 2**: Next zone favorite. Trigger nächster Zonen-Favorit. Wurde zuletzt eine benutzerdefinierte Auswahl getroffen, wird der erste Zonenfavorit abgespielt. | - | 0/1 |
| AIs | **Casatunes Music Server**: Source | Analoger Eingang Quelle. **Loxone Music Server**: Zone favorite. Analoger Eingang Zonen-Favorit. | - | ∞ / 0...8 |
| Play | Start playback | Trigger Song abspielen | - | 0/1 |
| Pause | Pause playback | Trigger Song pausieren. Wird eine Playliste abgespielt, wird die Wiedergabe mit Play an der aktuellen Position des Titels fortgesetzt. | - | 0/1 |
| Stop | Stop playback | Trigger Song stoppen. Wird eine Playliste abgespielt, wird die Wiedergabe mit Play wieder am Beginn des Titels gestartet. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Song+ | Next track | Trigger nächster Song | - | 0/1 |
| Song- | Previous track | Trigger vorheriger Song | - | 0/1 |
| Mute | Mute | Trigger Mute. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Shuffle | Shuffle | Trigger Shuffle | - | 0/1 |
| Repeat | Repeat | Analoger Eingang Repeat. 0 = Aus, 1 = Playliste fortlaufend wiederholen, 2 = aktuellen Titel wiederholen | - | 0...2 |
| Mo | Motion sensor | Bewegungsmelder, spielt die aktuell ausgewählte Playliste | - | 0/1 |
| T5 | Combined button input | V+ bzw. V-Taste wird verwendet. Doppelklick auf Taste 3 schaltet die Zone aus (siehe Parameter Roff). | - | ∞ |
| R | Reset | Reset, schaltet die Zone aus. Wird eine Playliste abgespielt, wird die Wiedergabe mit Play wieder am Beginn des Titels gestartet. Der Name des angeschlossenen Sensors wird in der Visualisierung verwendet. | - | 0/1 |
| Dis | Disable | Kindersicherung – sperrt alle Eingänge, aber nicht die Visualisierung | - | 0/1 |
| DisMo | Disable motion sensor | Verhindert das Einschalten der Musik über (Mo). Hat keinen Einfluss auf die automatische Abschaltung mit Parameter (MT). | - | 0/1 |
| A | Alarm input | Einbruchalarm mit Lautstärke des Parameters Va aktivieren. Während Alarmeingang aktiv ist werden alle Eingänge gesperrt. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| FA | Fire Alarm | Feueralarm mit Lautstärke des Parameters Va aktivieren. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Be | Doorbell input | Türklingel mit Lautstärke des Parameters Vbe aktivieren. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Buzzer | Alarm clock input | Weckersound mit Lautstärke des Parameters Vbu aktivieren. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Sleep | Sleep timer input | Zone wird nach Ablauf der Zeit Ts lautlos gesetzt und ausgeschaltet. Der Ausschalttimer wird durch vorzeitiges Ausschalten der Zone (Off, Pause, Stop, R) zurückgesetzt. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| TTS | Text to Speech input | Eingang Text-to-speech(Sprachausgabe). Maximale Textlänge 400 Zeichen. Dieser Eingang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | - |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/music-server-zone/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Qa | Status Zone an/aus | - | - | 0/1 |
| AQv | aktuelle Lautstärke | - | % | 0...100 |
| AQs | Aktuelle Quelle | - | - | ∞ |
| - | Aktueller Zonenfavorit | - | - | ∞ |
| - | Aktueller Zonenfavorit | - | - | ∞ |
| AQr | Remaining time of sleep timer | Verbleibende Zeit bis Zone durch den Sleeptimer ausgeschaltet wird. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ |
| Qon | - | Impulsausgang Zone Ein. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| Qoff | - | Impulsausgang Zone Aus. Dieser Ausgang ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0/1 |
| RQ | - | Resetausgang. Wird mit (R) oder Doppelklick aktiviert | - | 0/1 |
| RaQ | - | Reset 3-fach Impuls | - | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. "Music Server Zone" wird vom Touch Pure Flex nicht unterstützt. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/music-server-zone/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Tdc | Double click interval | Doppelklickzeit bei Eingangsimpuls zum Ausschalten der Zone. Wenn Sie keinen Doppelklick verwenden möchten, dann setzen Sie hier 0 ein. | s | 0...∞ | 0,35 |
| Sv | Volume step size | Schrittweite bei Lautstärkeregelung mit +/- | - | ∞ | 3 |
| Rf | First recurrence | Wenn der Eingang länger als diese Zeit in Sekunden auf EIN ist, wird der Befehl wiederholt. Betroffen ist der Eingang V+ und V- (inkl. T5) | - | ∞ | 0,5 |
| Rr | Repeat interval | Wenn der Eingang auf EIN bleibt, wird der Befehl in diesem Abstand wiederholt (in Sekunden). Betroffen ist der Eingang V+ und V- (inkl. T5) | - | ∞ | 0,2 |
| MT | Automatic switch off motion | Automatische Abschaltung der Zone nach Ende letzter Bewegung. Wenn dieser Wert ungleich 0 ist, wird der Bewegungsmelder verwendet, um die Zone auszuschalten, Unabhängig von (TH). Zur Verwendung um Musik, die vergessen wurde automatisch abzuschalten. Empfohlener Wert 30 Minuten (1800) | s | 0...∞ | 3600 |
| TH | Duration On | Aktiviert die Zone bei Bewegung und startet bei fallender Flanke des Bewegungsmeldereingangs den Nachlauftimer (TH). Wenn dieser Wert 0 ist, wird die automatische Abschaltung deaktiviert | s | 0...∞ | 900 |
| Ti | Delay of the Motion Sensor | Deaktiviert den Eingang (Mo) nach dem Ausschalten der Zone. Wenn dieser Wert 0 ist, gilt der Status von (DisMo) | s | 0...∞ | 300 |
| Vm | Maximum volume level | Maximale Lautstärke via App und Objekteingänge. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...100 | 100 |
| Vd | Startup volume | Einschaltlautstärke. Abspiellautstärke beim Einschalten der Zone. Wert -1 setzt zuletzt verwendete Lautstärke. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | -1...100 | 10 |
| Va | **Loxone Music Server**: Alarm volume | Lautstärke der Alarmtöne (Einbruch- und Feueralarm). Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. **Loxone Music Server Gen 2**: Alarm volume. Mindestausstärke der Alarmtöne (Einbruch- und Feueralarm). Spielt die Zone aktuell mit einer höheren Lautstärke, wird der Ton mit der aktuellen Lautstärke abgespielt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...100 | 75 |
| Vbe | **Loxone Music Server**: Doorbell volume | Lautstärke des Klingeltons. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. **Loxone Music Server Gen 2**: Doorbell volume. Mindestlautstärke des Klingeltons. Spielt die Zone aktuell mit einer höheren Lautstärke, wird der Ton mit der aktuellen Lautstärke abgespielt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...100 | 20 |
| Vbu | **Loxone Music Server**: Alarm clock volume | Laustärke des Weckertons. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. **Loxone Music Server Gen 2**: Alarm clock volume. Mindestausstärke des Weckertons. Spielt die Zone aktuell mit einer höheren Lautstärke, wird der Ton mit der aktuellen Lautstärke abgespielt. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...100 | 10 |
| Vt | **Loxone Music Server**: TTS volume | TTS-Lautstärke. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. **Loxone Music Server Gen 2**: TTS minimum volume. Mindestlautstärke der Sprachausgabe. Um die Sprachausgabe immer deutlich hören zu können, wird diese immer mindestens mit der aktuellen Lautstärke abgespielt. Also bei Bedarf auch lauter als Vtts. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | 0...100 | 20 |
| Ts | Sleep timer duration [s] | Zeit des Ausschalttimers in Sekunden. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ | 300 |
| Te | Event playback duration [s] | Mindestlaufzeit von Event-Sounds in Sekunden. Ein zu geringer Wert führt zu abgeschnittenen Eventsounds. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ | 8 |
| Tqo | Delay of Qoff [s] | Verzögerung für den Impuls auf QOff nachdem die Zone ausgeschaltet / pausiert wurde. Dieser Parameter ist nur bei bestimmten Baustein-Konfigurationen sichtbar. | - | ∞ | 30 |
| ROff | Ignore room off command | Wird die Raum-Aus Geste (Eingang T5, Doppelklick auf Taste 3) erkannt, so schaltet sich auch die Musik aus. | - | 0/1 | 0 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/music-server-zone/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Music Server | Referenz zum Music Server. Um diesen Baustein verwenden zu können, muss hier der entsprechende Music Server ausgewählt werden. | - |
| Zugeordnete Musikzone | Legt die zugeordnete Musikzone fest. | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/music-server-zone/

- **Zonen-Gruppierung:** "Diese Events MÜSSEN mit den gleichen ZonenIDs beendet werden: `audio/grouped/{eventtype}/off/ZoneID1,ZoneID2,...` Bsp: `audio/grouped/bell/off/1,3,9,8,10` und `audio/grouped/alarm/off/1,2,3`"
- **Zonennamen-Änderung:** "Wird eine Zone umbenannt, wird diese Änderung für Air Play und sonstige Dienste spätestens nach einem Reboot des Music Servers übernommen."

Quelle: https://www.loxone.com/dede/kb/music-server-zone/

---

### Mediensteuerung

Dieser Baustein ermöglicht die IR-basierte Steuerung von Mediengeräten wie Fernsehern, Receivern oder Set-Top-Boxen durch Integration mit IR-Aktoren.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/mediensteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich |
|--------|------------------|-------------|---------|--------------|
| Ptg | Power toggle | Schaltet um zwischen Ein und Aus im aktuellen Modus. Doppelklick beendet den aktuellen Modus. | - | 0/1 |
| Poff | Power off | Schaltet Aus. Doppelklick schaltet auch den aktuellen Modus aus. | - | 0/1 |
| Pon | Power on | Schaltet Ein. Doppelklick schaltet auch den aktuellen Modus aus. | - | 0/1 |
| V+ | Volume+ | Erhöht die Lautstärke oder startet den aktuellen Modus, wenn ausgeschaltet ist. Doppelklick führt den Befehl Channel up (Ch+) aus. | - | 0/1 |
| V- | Volume- | Verringert die Lautstärke des aktuellen Modus. Doppelklick beendet den aktuellen Modus. | - | 0/1 |
| V | Set volume | Lautstärke einstellen | % | 0...100 |
| Ch+ | Channel+ | Sender+ | - | 0/1 |
| Ch- | Channel- | Sender- | - | 0/1 |
| Ch | Set channel | Schaltet auf einen Kanal basierend auf seiner Nummer. | - | ∞ |
| Mode | Set mode | Aktiviert einen Modus anhand seiner zugewiesenen ID. | - | ∞ |
| M1-8 | Mode 1-8 | Aktiviert den Modus 1-8. Doppelklick beendet den aktuellen Modus. Steigende Flanke am Eingang führt immer 'Wechsel zum Modus'-Aktionen aus. | - | 0/1 |
| T5 | T5 control | Taste 2 : Lauter, oder startet den aktuellen Modus bei ausgeschaltetem Gerät. Doppelklick führt den Befehl Kanal hoch (Ch+) aus. Taste 5 : Leiser; Doppelklick beendet den aktuellen Modus. | - | ∞ |
| Off | Off / Lock | Pulse (< 200 ms): Outputs are reset / switched off. Pulse (> 200 ms): Block is locked. Dominating input. Pulse (> 500 ms): The name of the connected sensor is used in the user interface. | - | 0/1 |
| DisPc | Disable periphery control | Deaktiviert die Eingänge (Ptg), (Poff), (Pon), (V+), (V-), (V), (Ch+), (Ch-), (Mode), (M1-8), (T5), (Off) wenn Ein. (z.B. Kindersicherung, Reinigung) Bedienung über die Visualisierung weiterhin möglich. | - | 0/1 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/mediensteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| M | Current mode | Aktueller Modus | ∞ |
| P | Power state | Power Status | ∞ |
| O1-26 | Analog outputs 1-26. | Analoge Ausgänge 1-26. | ∞ |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/mediensteuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Rem | Remanence input | Remanenzeingang: Wenn aktiv, behält der Baustein seinen letzten Zustand nach einem Miniserver-Neustart. Der Zustand des Bausteins wird gespeichert: – Beim Speichern in den Miniserver – Bei einem geplanten Neustart – Vor einem Backup – Einmal pro Stunde Die Daten werden auf der SD gespeichert. | - | 0/1 | 0 |
| Nst | Numpad send timeout | Zeit nach letzter Eingabe, bevor die Nummer automatisch ohne weitere Bestätigung gesendet wird. | ms | 0...∞ | 3000 |
| Tdc | Time double-click | 0 = Deaktiviert Doppelklicks | s | 0...∞ | 0,35 |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/mediensteuerung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Modus | Modi des Medien-Controllers bearbeiten | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/mediensteuerung/

Keine dokumentierten Warnungen oder Fallstricke vorhanden.

Quelle: https://www.loxone.com/dede/kb/mediensteuerung/

---

### Mail Generator

Dieser Baustein erzeugt und versendet automatisierte E-Mails basierend auf definierten Triggern und Parametern.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/mail-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tr | Triggers output | Sendet die E-Mail bei steigender Flanke. | 0/1 |
| V1-8 | Value 1-8 | Eingangswerte können in der E-Mail-Nachricht und in den Eigenschaften verwendet werden. | - |
| Uid | User-ID | User-ID. Wenn vor dem Auslösen festgelegt, können die Benutzerfelder des entsprechenden Benutzers verwendet werden. | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/mail-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Td | Trigger Delay | Verzögert die E-Mail-Erzeugung nach Auslösung, um sicherzugehen, dass alle Eingänge gesetzt sind. | ms | 0...2147483647 | 0 |
| Tu | Update Interval | Intervall, in dem die E-Mail gesendet wird, solange der Trigger-Eingang aktiv ist. Kann verwendet werden, um die E-Mail-Parameter in regelmäßigen Abständen mit neuen Eingangswerten zu aktualisieren. 0 = Deaktiviert. | s | 0...2147483647 | 0 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/mail-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | API |
|--------|------------------|-------------|-----|
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) | - |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/mail-generator/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Mailer | E-Mail-Dienst, der zum Senden von E-Mails verwendet werden soll | - |
| Empfängeradresse | E-Mail-Adresse des Empfängers. Um mehrere Empfänger einzugeben, verwenden Sie ein Semikolon (;) als Trennzeichen. Platzhalter können verwendet werden (z.B. <v1>, <user.email>, <sysvar.rain> usw.) | - |
| Betreff | Betreff der E-Mail. Variablen können verwendet werden (z.B. <v1>, <user.email>, <sysvar.rain> usw.) | - |
| Nachrichtentext | Nachrichtentext der E-Mail. Platzhalter können verwendet werden (z.B. <v1>, <user.email>, <sysvar.rain> usw.) | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/mail-generator/

Keine dokumentierten Warnungen oder Fallstricke vorhanden.

Quelle: https://www.loxone.com/dede/kb/mail-generator/

---

### Call Generator

Dieser Baustein ermöglicht automatische Telefonanrufe mit Sprachmitteilung basierend auf konfigurierten Triggern.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/call-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tr | Triggers output | Ruft bei steigender Flanke eine Telefonnummer an. | 0/1 |
| V1-8 | Value 1-8 | Eingangswerte können in der Nachricht und im Telefonnummern-Eigenschaftsfeld verwendet werden. | — |
| Uid | User-ID | User-ID. Wenn vor dem Auslösen festgelegt, können die Benutzerfelder des entsprechenden Benutzers verwendet werden. | — |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/call-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Td | Trigger Delay | Verzögert den Anruf nach Auslösung, um sicherzugehen, dass alle Eingänge gesetzt sind. | ms | 0...2147483647 | 0 |
| Tu | Update Interval | Intervall, in dem der Anruf initiiert wird, solange der Trigger-Eingang aktiv ist. Kann verwendet werden, um die Anrufparameter in regelmäßigen Abständen mit neuen Eingangswerten zu aktualisieren. 0 = Deaktiviert. | s | 0...2147483647 | 0 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/call-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Dk0-9 | Dial key 0-9 | Sendet Impulse bei Tastendruck während des Anrufs. | 0/1 |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. API Commands | — |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/call-generator/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Sprache | Sprache, die beim Abspielen der Nachricht verwendet wird. | — |
| Telefonnummer | Telefonnummer, die angerufen werden soll. Platzhalter können verwendet werden (z. B. <v1>, <user.phone>, <sysvar.rain> usw.). Beachten Sie, dass nur Zahlen unterstützt werden. (z. B. 0043728770700) | — |
| Nachricht | Nachricht, die während des Anrufs abgespielt wird. Platzhalter werden unterstützt (z.B. <v1>, <user.phone>, <sysvar.rain> usw.) | — |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/call-generator/

- **Anruflimit:** "Der Caller Service ist mit 10 Anrufen an die gleiche Nummer pro Minute limitiert. Weitere Anrufe werden blockiert."
- **Anrufdauer:** "Die maximale Anrufdauer beträgt etwa 40 Sekunden."
- **Request-Limit:** "Jede Anfrage zählt zum Limit, auch wenn sie blockiert wurde."

Quelle: https://www.loxone.com/dede/kb/call-generator/

---

### Text Generator

Dieser Baustein generiert Text basierend auf definierten Mustern und Eingangswerten, die über Text-Templates an verschiedenen Ausgängen bereitgestellt werden.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/text-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Tr | Triggers output | Erzeugt den Text bei steigender Flanke. Setzt den generierten Text bei der fallenden Flanke zurück. | 0/1 |
| V1-8 | Value 1-8 | Eingangswerte können im Texteditor verwendet werden. | - |
| Uid | User-ID | User-ID. Wenn vor dem Auslösen festgelegt, können die Benutzerfelder des entsprechenden Benutzers verwendet werden. | - |

#### Parameter [BELEGT]
https://www.loxone.com/dede/kb/text-generator/

| Kürzel | Kurzbeschreibung | Beschreibung | Einheit | Wertebereich | Standardwert |
|--------|------------------|-------------|---------|--------------|--------------|
| Td | Trigger Delay | Verzögert die Texterzeugung nach Auslösung, um sicherzugehen, dass alle Eingänge gesetzt sind. | ms | 0...2147483647 | 0 |
| Tu | Update Interval | Intervall, in dem der Text aktualisiert wird, solange der Trigger-Eingang aktiv ist. Kann verwendet werden, um den Text in regelmäßigen Abständen mit neuen Eingangswerten zu aktualisieren. 0 = Deaktiviert. | s | 0...2147483647 | 0 |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/text-generator/

| Kürzel | Kurzbeschreibung | Beschreibung |
|--------|------------------|-------------|
| Txt | Generated text | Gibt den im Texteditor definierten Text aus, wenn der Eingang (Tr) getriggert wird. |
| Txt1-4 | Generated text 1-4 | Gibt den im Texteditor definierten Text aus, wenn der Eingang (Tr) getriggert wird. |
| API | API Connector | Intelligenter API basierter Verbinder. Kann verschiedene Funktionen zwischen Geräten und Bausteinen verknüpfen. [API Commands](https://updatefiles.loxone.com/KnowledgeBase/Online/Common/Documents/API_Commands.pdf) |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/text-generator/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Text Editor - Txt | Legt den Text fest, der bei steigender Flanke an Tr am entsprechenden Ausgang ausgegeben werden soll. | - |
| Text Editor - Txt1 | Legt den Text fest, der bei steigender Flanke an Tr am entsprechenden Ausgang ausgegeben werden soll. | - |
| Text Editor - Txt2 | Legt den Text fest, der bei steigender Flanke an Tr am entsprechenden Ausgang ausgegeben werden soll. | - |
| Text Editor - Txt3 | Legt den Text fest, der bei steigender Flanke an Tr am entsprechenden Ausgang ausgegeben werden soll. | - |
| Text Editor - Txt4 | Legt den Text fest, der bei steigender Flanke an Tr am entsprechenden Ausgang ausgegeben werden soll. | - |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/text-generator/

Keine dokumentierten Warnungen oder Fallstricke vorhanden.

Quelle: https://www.loxone.com/dede/kb/text-generator/

---

### Benachrichtigung

[OFFEN] Die offizielle KB-Seite zur "Benachrichtigung" enthält keine strukturierten Tabellen (Eingänge, Ausgänge, Parameter, Eigenschaften) nach dem Standard der anderen Bausteine. Die Seite behandelt konzeptionelle Themen zu Push-Benachrichtigungen, bietet aber keine technische Schnittstellendokumentation.

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/benachrichtigung/

- **Huawei-Geräte:** "Auf neuen Huawei Smartphones / Tablets funktionieren Push Notifications nicht, da diese bei Android von den Google Services abhängig sind, welche bei Huawei Geräten aufgrund des US Embargos nicht mehr enthalten sind."

#### Anmerkung
Dieser Baustein benötigt zusätzliche technische Dokumentation. Die KB-Seite enthält konzeptionelle Information zu Benachrichtigungen, aber keine Baustein-Schnittstellenbeschreibung.

Quelle: https://www.loxone.com/dede/kb/benachrichtigung/

---

### IR Steuerung

Dieser Baustein erzeugt Infrarot-Steuerbefehle aus Text-Eingaben, die an IR-Aktoren gesendet werden können, um Geräte wie Fernseher oder Receiver zu kontrollieren.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/ir-steuerung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| I1-6 | Input 1-6 | Eingang 1-6 | ∞ |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/ir-steuerung/

| Kürzel | Kurzbeschreibung | Beschreibung |
|--------|------------------|-------------|
| Txt | Text | Text |

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/ir-steuerung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| IR-Befehl | Aus diesem Text zusammen mit den Eingangswerten werden Sendedaten für einen IR-Aktor erstellt. Mehr Information in der Hilfe. | — |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/ir-steuerung/

- **Leerzeichen-Regel:** "Da in einem IR Befehl die unterschiedlichen Befehls-Blöcke durch ein Leerzeichen getrennt werden, darf innerhalb der Befehls-Blöcke kein Leerzeichen verwendet werden."
- **Längenbeschränkung:** "Die Befehlssequenz darf maximal 256 Bits lang sein."
- **Start- und End-Bit:** "Das Start- und End-Bit werden beim IR Befehl weggelassen."
- **Dezimalformat:** "Dezimalzahlen werden mit einem Trennpunkt angegeben (z.B. 16.5)."

Quelle: https://www.loxone.com/dede/kb/ir-steuerung/

---

### Befehlserkennung

Dieser Baustein extrahiert Werte aus eingehenden Textsequenzen gemäss definierten Mustern und gibt diese Werte an den Ausgang aus.

#### Eingänge [BELEGT]
https://www.loxone.com/dede/kb/befehlserkennung/

| Kürzel | Kurzbeschreibung | Beschreibung |
|--------|------------------|-------------|
| T | Text Input | Befehlstext. |

#### Ausgänge [BELEGT]
https://www.loxone.com/dede/kb/befehlserkennung/

| Kürzel | Kurzbeschreibung | Beschreibung | Wertebereich |
|--------|------------------|-------------|--------------|
| Lv | Last extracted value | Zuletzt ausgelesener Wert | ∞ |

#### Parameter
[OFFEN] Keine Parameter-Tabelle in der KB-Seite dokumentiert.

#### Eigenschaften [BELEGT]
https://www.loxone.com/dede/kb/befehlserkennung/

| Kurzbeschreibung | Beschreibung | Standardwert |
|--------|------------------|-------------|
| Befehlserkennung | Zeichen zum Auslesen eines Wertes: \\v = Wert, \\1 = Byte interpretiert als 1. Byte des Ausgabewertes (\\2, \\3, ...), \\h = Wert interpretiert als hexadezimale Zahl. Zeichen zum Navigieren durch den Text: \\. = Irgendein Zeichen, \\w = Irgendein Wort, \\# = Irgendeine Nummer, \\d = Ziffer 0-9, \\m = Zeichen A-Z/a-z/0-9, \\a = Zeichen A-Z/a-z, \\s12 = 12 Zeichen überspringen, \\iText\\i = Springe zu 'Text'. Sonderzeichen: \\x = Hexadezimale Zahl (z.B. 0x09), \\\\ = Slash, \\t = Tab (0x09), \\b = Space (0x02) oder Tab (0x09), \\r = Return (0x0d), \\n = Newline (0x0a) | \- |
| Werteinterpretation mit Vorzeichen | Wenn aktiviert, werden in der Befehlserkennung die Werte \\1, \\2, \\3, usw. mit Vorzeichen verwendet (Signed Integer). | \- |

#### Fallstricke [BELEGT]
https://www.loxone.com/dede/kb/befehlserkennung/

Keine dokumentierten Warnungen oder Fallstricke vorhanden.

Quelle: https://www.loxone.com/dede/kb/befehlserkennung/

---

## Zusammenfassung

**Erfolgreich erfasst:** 10 von 11 Bausteinen mit vollständigen oder teilweise dokumentierten Tabellen.

**Bausteine mit [OFFEN]-Status:**
- **Benachrichtigung** — Die KB-Seite enthält keine Tabellen nach dem Standard-Format; nur konzeptionelle Information zu Push-Benachrichtigungen.

**Besonderheiten:**
- Viele Bausteine unterscheiden zwischen verschiedenen Musik-Server-Typen (Casatunes, Loxone Music Server, Loxone Music Server Gen 2).
- Der Befehlserkennung-Baustein nutzt ein spezialisiertes Syntax-System mit Escape-Sequenzen (\v, \1-3, \h, etc.).
- IR-Steuerung hat strikte Längenbeschränkungen (max. 256 Bits).
- Call Generator ist mit 10 Anrufen pro Minute und pro Zielrufnummer limitiert.
- Audio-Bausteine haben umfangreiche Lautstärke-Fade- und Mindestlautstärke-Optionen.
