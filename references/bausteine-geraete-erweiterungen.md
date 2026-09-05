# Geräte, Extensions und Systemobjekte — aus der TechDoc
Teil des Loxone-Baustein-Katalogs. Quelle: maschinenlesbare Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)). Erzeugt von `scripts/techdoc_katalog.py`.

---

## Aus der TechDoc ergänzt

Stand 05.09.2026, Loxone Config 17.1.6.30. Diese Bausteine haben keine eigene Seite in der KB-Kategorie „Funktionsbausteine"; Ein-/Ausgänge und Parameter stammen aus der maschinenlesbaren Bausteindoku des Config-Pakets ([techdoc-lxres.md](techdoc-lxres.md)), Kennzeichnung `[BELEGT-TECHDOC]`. Eigenschaften und Fallstricke kennt die TechDoc nicht. Erzeugt von `scripts/techdoc_katalog.py` — nicht von Hand bearbeiten, sondern das Skript nach einem Config-Update erneut laufen lassen.

### Einträge ohne Konnektoren

Extensions, Geräte und Systemobjekte: die TechDoc kennt zu ihnen Name und Beschreibung, aber keine Ein-/Ausgänge (ihre Klemmen entstehen erst mit dem Gerät im Projekt).

| Name | LxType | ControlType | Beschreibung | KB |
|---|---|---|---|---|
| Audioserver | `AudioServer` | 223 | – | – |
| 1-Wire Extension | `Comm1wire` | 8 | – | https://www.loxone.com/help/Comm1wire |
| RS232 Extension | `Comm232` | 10 | – | https://www.loxone.com/help/Comm232 |
| RS485 Extension | `Comm485` | 9 | – | https://www.loxone.com/help/Comm485 |
| DMX Extension | `CommDMX` | 11 | – | https://www.loxone.com/help/CommDMX |
| Datenbank | `DbConT` | 249 | Verbindet eine Exosphere-Datenbank mit Loxone Config | https://www.loxone.com/help/DatabaseConnector |
| DeviceMonitor | `Devicemonitor` | 305 | DeviceMonitor | – |
| Gegensprechanlage | `IntercomDevice` | 88 | – | – |
| AI Extension Gen. 1 | `LoxAin` | 199 | – | – |
| AO Extension | `LoxAout` | 200 | – | – |
| Dimmer Extension | `LoxDIMM` | 6 | – | https://www.loxone.com/help/LoxDIMM |
| DI Extension | `LoxDigin` | 195 | – | https://www.loxone.com/help/LoxDigin |
| KNX Extension | `LoxKnx` | 197 | – | – |
| Miniserver | `LoxLIVE` | 4 | – | https://www.loxone.com/help/LoxLIVE |
| Extension | `LoxMORE` | 5 | – | https://www.loxone.com/help/LoxMORE |
| EnOcean Extension | `LoxOCEAN` | 7 | – | https://www.loxone.com/help/LoxOCEAN |
| M-Bus Extension | `MBusExtension` | 243 | – | – |
| Systemstatus | `MessageCenter` | 98 | Aktuell anliegende Benachrichtigungen, Warnungen, Fehler und schwere Fehler werden hier gesammelt angezeigt und verwaltet. | – |
| Modbusserver | `ModbusServer` | 48 | Modbus TCP Gerät mit Netzwerkverbindung, eingebunden über das Modbus Protokoll. | https://www.loxone.com/help/Modbus-TCP |
| Plugin (In Development) | `Plugin` | 226 | – | – |
| Schüco Extension | `SchuecoExtension` | 204 | – | – |
| Sonnen Batteriespeicher | `SonnenBatteryDevice` | 89 | – | – |
| Anlagenschema | `SystemScheme` | 321 | Vereinfachen Sie durch Verwendung eines Anlagenschemas die Abbildung einer komplexen Anlage oder Logik. Durch Auswählen von bereits visualisierten Objekten und platzieren dieser auf einem von Ihnen definierten Bild können Sie zum Beispiel Ihr Heizungssystem einfach abbilden. | – |
| Notiz | `Text` | 322 | Beliebiger Text zur Dokumentation | – |
| Tracker | `Tracker` | 94 | Dient zur Visualisierung von Ereignissen. | https://www.loxone.com/help/Tracker |
| Wetterserver | `WeatherServer` | 36 | Mit dem Loxone Wetter Service können Sie Wetterdaten innerhalb Ihres Systems verwalten und nutzen. | https://www.loxone.com/help/WeatherServer |
