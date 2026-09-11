# Gateway/Client (Konzentrator) — Dateien, XML-Objekte, Signalverbund, API

Stand 11.09.2026. Erhoben an einem Bestandsprojekt mit vier Miniservern (ein Gateway, drei
Clients, Programmformat `V="174"`), abgeglichen mit der Loxone-KB, dem LoxWiki und den
API-PDFs (Structure File 17.1, Communicating with the Miniserver V17.0). Kundendaten
anonymisiert; Adressen sind Platzhalter. Was nur abgeleitet und nicht am Gerät bestätigt
ist, steht ausdrücklich als **abgeleitet**.

Loxone nennt es „Gateway-Client-System", das LoxWiki „Konzentrator-Funktion", viele
Errichter „Master/Client". Gemeint ist dasselbe.

## 1. Was Loxone dokumentiert (belegt)

Quelle KB [Gateway-Client-System](https://www.loxone.com/dede/kb/gateway-client/):

- Die Projekte der einzelnen Miniserver werden getrennt erstellt, dann in Config
  zusammengeführt: „Das gewählte Projekt wird nun in Loxone Config mit dem Projekt des
  bereits geöffneten Miniservers zusammengeführt." Gespeichert wird **im Gateway**.
  Der erste Speichervorgang meldet einen Fehler, weil das Gateway die Clients noch nicht
  kennt — das ist erwartet.
- „Der Gateway startet nun neu, danach verteilt er die Programmteile des
  zusammengeführten Projekts auf die Clients."
- „Alle Miniserver müssen sich im selben Subnetz befinden", „Hostnamen werden an dieser
  Stelle nicht unterstützt!" — als interne Adresse nur IP.
- Grenzen: Miniserver Gen 2 als Gateway bis 10 Clients, Miniserver Gen 1 bis 4 Clients.
- Grundsatz „Zusammen was zusammengehört", aber: „Natürlich dürfen Funktionen auch
  Miniserver übergreifend programmiert werden."

Quelle LoxWiki [Client-Gateway-Konzentrator Funktion](https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1525056219/):

- „Beim Programmieren in der Loxone Config Projektdatei wählt man beim Erstellen einer
  neuen Seite aus, auf welchem Miniserver diese Seite ausgeführt werden soll."
- „Sämtliche Ein- und Ausgänge (auch virtuelle) können direkt auf die Seite eines anderen
  Miniservers gezogen und dort verwendet werden." Sie sind in Config farblich markiert,
  die Netzwerkübertragung passiert automatisch.
- „Wird das Programm übertragen (‚Im Miniserver speichern'), wird das Programm an den
  Konzentrator-MS übertragen, dieser startet neu und überträgt nach dem Neustart das
  Programm dann weiter an die Client-MS." Alle Miniserver starten dabei neu.
- Fällt ein Client aus, „läuft das Programm auf den anderen Miniservern weiter". Fällt das
  Gateway aus, „können in der App die anderen Miniserver direkt verbunden werden" — dann
  nur als Einzelanlage.
- „In einem Zentral-Baustein können nur Bausteine des selben Miniservers ausgewählt
  werden." Umweg: je Miniserver ein Zentralbaustein, darüber ein weiterer.
- Gleicher Benutzer mit gleichem Passwort auf allen Miniservern.

Die API-PDFs erwähnen den Verbund nur an einer Stelle: Im Binär-Header des WebSockets
gibt es ein **Estimated-Bit** („eg. Gateway Miniservers"), weil ein Gateway die Größe einer
Antwort nur schätzen kann, solange es Daten von Clients einsammelt. Auf einen
Estimated-Header folgt immer ein exakter Header.

## 2. Das Programmarchiv eines Gateways

`sps_<nr>_<zeit>.zip` in `/prog` des Gateways enthält bei einem Verbund deutlich mehr als
bei einer Einzelanlage (dort: eine `sps0.LoxCC` plus vier Begleitdateien, siehe
[miniserver-dateizugriff.md](miniserver-dateizugriff.md)):

| Datei | Inhalt |
|---|---|
| `sps.Loxone` | **das Gesamtprojekt** als `ControlList`-XML, alle Miniserver — nur im Verbund vorhanden |
| `sps0.LoxCC` | Programm des Gateways |
| `sps1.LoxCC` … `spsN.LoxCC` | Programm des Clients N |
| `LoxAPP3.json` | Strukturdatei des Gateways — enthält **alle** Bausteine aller Miniserver (Abschnitt 5) |
| `LoxAPP3_N.LoxCC` | Strukturdatei des Clients N, LoxCC-verpacktes JSON, Teilmenge der Gateway-Datei |
| `permissions.bin`, `permissions_N.LoxCC` | Rechte je Miniserver |
| `Emergency.LoxCC`, `Emergency_N.LoxCC` | Notprogramm je Miniserver (`ControlList`-XML) |
| `Music.json` | einmal |

Jede `spsN.LoxCC` ist ein eigenständiges `Document` mit denselben globalen Captions
(Kategorien, Orte, Rechte, Betriebsarten …) plus **genau einem** `LoxLIVE`-Objekt (der
eigene Miniserver) und **genau einem** `Program`-Objekt. Im Beispiel: Gateway 4078 Objekte,
Clients 3862, 1831 und 1665, Gesamtprojekt 7269. Rund 1900 Objekte sind in allen Teilen
gleich — die globalen Captions.

Der Index N ist dreifach verankert: `SLAVE Type="N"` im Gateway-Objekt,
`GatewayClient ProgType="N"` im Client, Dateisuffix `_N`. Das Gateway selbst ist 0 und
trägt keine Suffixe.

## 3. Die XML-Objekte des Verbunds

**`LoxLIVE`** — ein Objekt je Miniserver, unter `Document`. Relevante Attribute:
`Serial`, `IntAddr` (interne IP), `IntAddr6`, `ExtAddr` (z. B. `dns.loxonecloud.com`),
`ExP`/`ExP2` (Ports), `HoN` (Hostname), `Miniserver` (Hardwaretyp, nicht Index),
`Installation`, `SwitchBoard`. Darunter der Hardwarebaum: `InputCaption`, `OutputCaption`,
`AnalogInputCaption`, `LoxTree`, `LoxAIR`, `EIBline`, `VirtualInCaption`, `VirtualOutCaption`,
`LoggerOutCaption`, `WeatherCaption` …

**`Program`** — ein Objekt je Miniserver, unter `Document`, mit `Ref="<U des LoxLIVE>"`.
Das ist die Zuordnung Programm → Miniserver. Darunter nur Seiten mit Logik; die Klemmen
liegen im `LoxLIVE`-Baum.

**`Gateway`** — genau eines, im `LoxLIVE` des Gateways unter `WeatherCaption`:

```xml
<C Type="Gateway" V="174" U="…" Title="…" Concentrator="true" Exts="3" APPKEY="…" APPID="…">
  <SLAVE Used="true" Name="…" IP="192.168.x.11" Serial="…" Type="1" Port="80" UP="" uuid="<U des Client-LoxLIVE>" />
  <SLAVE Used="true" Name="…" IP="192.168.x.12" Serial="…" Type="2" MiniserverType="4" Port="80" UP="" uuid="…" />
  <SLAVE Used="true" Name="…" IP="192.168.x.13" Serial="…" Type="3" Port="80" UP="" uuid="…" />
</C>
```

`Exts` = Anzahl Clients, `Type` = Index, `MiniserverType` erscheint nur bei
Nicht-Gen-1-Clients (4 = Compact, Werte wie `msInfo.miniserverType`, Abschnitt 5).

**`GatewayClient`** — eines je Client, in dessen `LoxLIVE` unter `WeatherCaption`:

```xml
<C Type="GatewayClient" V="174" U="…" Title="…" ConcentratorClient="true" ProgType="1" Serial="…" GwAddr="192.168.x.10" />
```

Wer aus dem Gesamtprojekt ableiten will, welcher Miniserver welche Klemme besitzt: der
nächste `LoxLIVE`-Vorfahre der Klemme. Wer aus einem Teilprogramm ableiten will, ob eine
Referenz fremd ist: die Ziel-UUID liegt nicht unter dem einzigen `LoxLIVE` des Teils.

## 4. Signale über Miniserver-Grenzen — was Config daraus macht

Verifiziert am Bestandsprojekt: Das Gateway-Programm verwendet 458 Referenzen auf
Ein-/Ausgänge anderer Miniserver, die Clients 15 bis 41. Im Teilprogramm des
verwendenden Miniservers sieht das so aus:

**Fremde Eingänge (`InputRef` auf Sensor, Klemme, virtuellen Eingang …):** Config erzeugt
im Teilprogramm ein `Memory`-Objekt (Merker) **mit derselben UUID wie das fremde
Quellobjekt**, auf der Seite, auf der es verwendet wird. Die Referenz zeigt also weiterhin
auf „ihre" UUID, nur ist dahinter jetzt ein Merker, den die Laufzeit über das Netz füllt.

```xml
<C Type="Memory" V="174" U="<UUID des fremden Eingangs>" Title="…" Nio="3" EU="2" WF="16400" REFST="-1" REFCT="79" Tp="1">
  <Co K="Input" U="…" /><Co K="AQ" U="…" /><Co K="Q" U="…" />
  <IoData Cr="…" Pr="…" />   <!-- Kategorie und Raum des Originals -->
</C>
```

`Tp="0"` für digitale Quellen (`DigitalIn`, `LoxAIRsensor`, digitaler `VirtualIn`,
`EIBsensor` digital), `Tp="1"` für analoge (`ModbusASensor`, `VoltageIn`, `Lox1wireAsensor`,
analoger `VirtualIn`, `VirtualUdpInCmd`, `VirtualHttpInCmd`). Im Gateway-Teil des Beispiels
sind 323 solcher Proxy-Merker enthalten; das Gesamtprojekt hat nur 89 echte Merker.
**Merker zählen taugt deshalb nicht zum Vergleich von Gesamt- und Teilprojekt.**

**Fremde Ausgänge (`OutputRef` auf Aktor, virtuellen Ausgang, KNX-Aktor, Tree-/Air-Aktor):**
kein Proxy. Die `OutputRef` behält ihr `Ref` auf die fremde UUID, die im Teilprogramm gar
nicht existiert; die Laufzeit reicht den Befehl per UUID an den Besitzer weiter. Ein
Teilprogramm mit „hängenden" `Ref`-Attributen ist also im Verbund normal. Einzige
beobachtete Ausnahme: `ApiActor` (Türsprechstelle) wird als Kopie mitgeführt.

**Keine Markierung im XML.** `LinkRefType` trägt dieselben Werte wie bei lokalen Referenzen
(siehe [xml-bearbeitung.md](xml-bearbeitung.md)), `Cl` ist fast immer `0,0,0`. Die Farbe,
die Config für fremde Ein-/Ausgänge zeigt, wird berechnet, nicht gespeichert. Fremd oder
nicht entscheidet allein die Besitzer-Zuordnung über `LoxLIVE`.

## 5. Strukturdatei und API im Verbund

Aus den Dateien belegt:

- `LoxAPP3.json` des Gateways enthält die Bausteine **aller** Miniserver; die Client-Dateien
  `LoxAPP3_N` sind exakte Teilmengen (im Beispiel 281, 67 und 56 von 655 Bausteinen,
  Objekte identisch). Räume und Kategorien sind in allen Dateien gleich.
- `msInfo.gatewayType`: `2` beim Gateway, `1` beim Client, **fehlt** bei einer Einzelanlage
  (geprüft an einem Miniserver Gen 2, Firmware 17.2.8.28). Das Feld steht nicht im
  Structure-File-PDF.
- `msInfo.miniserverType` laut PDF: 0 Miniserver Gen 1, 1 Go Gen 1, 2 Miniserver Gen 2,
  3 Go Gen 2, 4 Compact.

Daraus folgt (die App macht es genauso): Wer sich mit dem Gateway verbindet, bekommt über
den WebSocket die Zustände aller visualisierten Bausteine aller Miniserver und kann sie
mit `jdev/sps/io/<uuid>/<cmd>` über das Gateway bedienen.

**Abgeleitet, nicht belegt:** Für Klemmen **ohne** Visualisierung auf einem Client kennt
das Gateway den Wert nur, wenn sein eigenes Programm die Klemme verwendet (dann gibt es
den Proxy-Merker aus Abschnitt 4). Ob `jdev/sps/io/<uuid>` am Gateway für nicht verwendete
Client-Klemmen antwortet, ist offen. Sicher lesbar sind solche Klemmen am Client selbst:
Alle Miniserver hängen im selben Subnetz mit demselben Benutzer und Passwort, und HTTP wie
WebSocket eines Clients funktionieren wie bei einer Einzelanlage. Nur **speichern** darf man
immer nur über das Gateway.

## 6. Folgen für Werkzeuge, die Programme ändern

Gilt für `scripts/ha_udp_logger.py`, die Home-Assistant-Integration und jedes Skript nach
[miniserver-dateizugriff.md](miniserver-dateizugriff.md) § 5:

1. **Ein Verbund hat mehrere Programmdateien.** Ein Logger muss im Programm des
   Miniservers liegen, an dem die Klemme physisch hängt: `Logger` unter dessen
   `LoggerOutCaption`, `OutputRefLM` auf einer Seite seines `Program`. Ein Logger im
   Gateway-Programm für eine Client-Klemme setzt einen Proxy-Merker voraus, den Config
   erzeugt — nicht nachbauen.
2. **`sps.Loxone` mitändern.** Config lädt im Verbund das Gesamtprojekt vom Gateway. Wer
   nur die `spsN.LoxCC` ändert, verliert die Änderung beim nächsten „Im Miniserver
   speichern", und ein Werkzeug, das sie danach erneut anlegt, produziert Neustartschleifen
   über alle Miniserver.
3. **UDP-Absender je Miniserver.** Ein Logger auf einem Client sendet von der Client-IP
   (`SLAVE IP`, `LoxLIVE IntAddr`). Empfänger, die nur die Gateway-Adresse akzeptieren,
   verwerfen die Pakete.
4. **Heartbeat je Miniserver.** Der `Second`-Systemausgang existiert je Miniserver; ein
   einzelner Heartbeat sagt nichts über die Clients.
5. **Upload.** Config schreibt das Gesamtarchiv ins Gateway, das nach dem Neustart
   verteilt. Ob ein per FTP als `/prog/sps_new.zip` abgelegtes Gesamtarchiv nach
   `dev/sps/restart` genauso verteilt wird, ist **nicht belegt** und nur in einem eigenen
   Testaufbau zu klären — nie an einer Kundenanlage.
6. **Zentralbausteine** bleiben je Miniserver (Abschnitt 1).
7. **Eindeutige UUIDs.** Werden verwaltete Objekte je Miniserver angelegt, muss die
   `Program`-UUID in die Ableitung der eigenen UUIDs einfließen, sonst kollidieren vier
   gleiche Seiten-UUIDs im Gesamtprojekt.

Stand der Home-Assistant-Integration (1.5.0): Archive mit mehreren Programmen werden
erkannt und **unverändert** gelassen (`ARCHIVE_MULTIPLE_PROGRAMS`); WebSocket, Bedienung
und Räume laufen über das Gateway normal. Die Klemmen-Erkennung nimmt derzeit die erste
LoxCC im Archiv statt aller — als Nächstes geplant.

## 7. Prüfrezept am echten Verbund

Für jede Aussage aus Abschnitt 5 und 6, die „abgeleitet" ist:

1. `GET http://<gateway>/jdev/sps/io/<uuid>` für eine Client-Klemme ohne Visualisierung —
   einmal für eine, die das Gateway-Programm verwendet (Proxy vorhanden), einmal für eine
   unbenutzte. Antwortcode und Wert notieren.
2. Dieselben Abfragen an `http://<client-ip>/jdev/sps/io/<uuid>` mit denselben
   Zugangsdaten.
3. `data/LoxAPP3.json` von Gateway und Client vergleichen: Client ⊂ Gateway, `gatewayType`.
4. In Config einen Logger mit UDP-Ziel plus `OutputRefLM` auf einer **Client**-Seite anlegen,
   speichern, Absender-IP der Datagramme mit `tcpdump`/Empfänger prüfen.
5. Nur im Testaufbau: Gesamtarchiv per FTP ins Gateway, `dev/sps/restart`, prüfen, ob die
   Clients neu starten und die Änderung tragen.

## 8. Offen

- Bedeutung von `REFCT`/`REFST` am Proxy-Merker.
- Ob das Gateway für unbenutzte Client-Klemmen Werte liefert (Rezept 1).
- Verteilverhalten beim FTP-Upload (Rezept 5).
- Programmformat `174` (ältere Config) ist in den Werkzeugen nicht freigegeben; die
  verifizierten Formate sind `175` und `178` (Config 17.1/17.2).
