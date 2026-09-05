# TechDoc: die offizielle Bausteindoku als XML — direkt aus dem Config-Paket

**Erarbeitet:** 05.09.2026 · Loxone Config 17.1.7.27 · Fund beim Durchsuchen des Config-Pakets
nach der Meldungstabelle des Miniservers. **[VERIFIZIERT]** an beiden Sprachpaketen.

Loxone Config liefert die Hilfetexte aller Bausteine **maschinenlesbar** mit — samt internem
XML-Konnektornamen, Doku-Kürzel, Einheit, Wertebereich und Vorgabewert. Das ist die Quelle,
aus der Config die Konnektor-Tooltips und die Auto-Konfiguration speist, und sie kommt mit
**jedem Config-Update automatisch mit**. Für den Skill ersetzt sie das Scrapen der KB-Seiten
und schließt die Lücke aus [xml-doku-mapping.md](xml-doku-mapping.md): dort waren 29
Vorlagentypen erhoben, hier stehen **220 typisierte Bausteine**.

## Fundort und Format

| Datei | Inhalt |
|---|---|
| `C:\ProgramData\Loxone\Loxone Config <Ver>\SDcard\sys\sys_DEU.zip` | `tdc_DEU.LxRes` (TechDoc deutsch), `DEU.LxRes` (Meldungstabelle des Miniservers), dazu `tdc_DEV`/`DEV` |
| `…\sys_ENG.zip` | dasselbe englisch |
| weitere `sys_*.zip` | 22 Sprachen, gleicher Aufbau |

Das sind die Dateien, die Config beim Update nach `/sys` auf den Miniserver schreibt
(siehe [miniserver-dateizugriff.md](miniserver-dateizugriff.md), Verzeichnis `/sys`). Sie sind
daher auch **per FTP oder `fsget` vom Miniserver** zu holen, wenn kein Config installiert ist.

`.LxRes` ist **dasselbe Format wie `sps*.LoxCC`**: 16-Byte-Header (`<4I`: Magic `0xAABBCCEE`,
komprimierte Größe, entpackte Größe, Prüfsumme) und dahinter ein LZ4-Block. Entpacken:

```
py -3 scripts/decode_lxres.py "C:\ProgramData\Loxone\Loxone Config 17.1.7.27\SDcard\sys\sys_DEU.zip"
py -3 scripts/decode_lxres.py <zip|LxRes> --list                 # alle Bausteine mit LxType
py -3 scripts/decode_lxres.py <zip|LxRes> --block AutoJalousie   # Konnektortabelle als Markdown
```

Das Skript braucht keine Fremdbibliothek. Es nimmt ZIP, `.LxRes` oder `.LoxCC`.

## Aufbau von `tdc_*.LxRes`

```xml
<TechDoc>
  <Templates>                <!-- 20 Blöcke, 162 gemeinsame Konnektoren -->
    <IO Id="10001" TemplateId="0" Name="Remanence" ShortName="Rem" …/>
    <IO Id="…"     TemplateId="APICONNECTOR" …/>
  </Templates>
  <FunctionBlock Name="Automatikbeschattung" LxType="AutoJalousie" ControlType="348"
                 Abbrevation="…" Keywords="…" ShortLink="www.loxone.com/help/…">
    <IOGroup Type="Input">      <IO Id="14" Name="AutoShade" ShortName="Sps" ShortDescription="…"/> … </IOGroup>
    <IOGroup Type="Output">     … </IOGroup>
    <IOGroup Type="Parameter">  <IO Id="1" Name="TDiff" ShortName="ϑd" Unit="°" Min="0.5" Max="5" Default="1.5"/> … </IOGroup>
    <AutoDesigner Id="348000"> <AutoDesignerEntry Id="348001" RText="__name__ __operator__ __value0__"/> … </AutoDesigner>
  </FunctionBlock>
  …
</TechDoc>
```

Zählung (17.1.7.27): **506 `FunctionBlock`**, davon **220 mit `LxType`**; 3.178 `IO`;
IOGroups: 234 Input, 280 Output, 174 Parameter; 86 `AutoDesigner`-Blöcke.

| Attribut | Bedeutung | Für den Skill |
|---|---|---|
| `FunctionBlock/@LxType` | **der XML-Typname** aus `<C Type="…">` | Schlüssel zu allem anderen. Fehlt bei Peripherie-Einträgen, Geräten und Dialogen (286 Stück) |
| `FunctionBlock/@ControlType` | numerische Baustein-ID, Präfix der AutoDesigner-IDs | — |
| `FunctionBlock/@Name`, `@ShortDescription`, `@Description` | Anzeigename und Hilfetext, `$$BR$$` = Zeilenumbruch, `$$LINK::…$$` = Verweis | Hilfetext wörtlich, wie die KB |
| `IO/@Name` | **interner Konnektorname = `Co/@K` im Projekt-XML** | genau das, was [xml-doku-mapping.md](xml-doku-mapping.md) bisher per Hand erhob |
| `IO/@ShortName` | **Doku-Kürzel** aus KB und Config-Oberfläche | `EnAutoShade` ↔ `DisSp` steht hier schwarz auf weiß |
| `IO/@Id` | laufende Nummer je Gruppe | nicht die Konnektor-UUID |
| `IO/@Unit`, `@Min`, `@Max`, `@Step`, `@Default` | Wertebereich und Vorgabe | Vorgabewerte der Auto-Konfiguration prüfen |
| `IO/@TemplateId` | Verweis auf `Templates/IO[@TemplateId]` — dort stehen Name, Kürzel, Text | ohne Auflösung fehlt beim Konnektor alles außer der Id |
| `IO/@Combines`, `@Condition` | Konnektor gehört zu einer Gruppe / erscheint nur unter Bedingung | 86 bzw. 29 Fälle |
| `Name="AQh%d"`, `ShortName="H%d-%e"` | **Platzhalter für nummerierte Konnektoren** (`%d` = Index, `%e` = Endindex) | aus `AQh%d` werden im Projekt `AQh1`…`AQh3` |
| `AutoDesignerEntry/@RText` | Satzvorlagen des Autopilot-Designers (`__name__ __operator__ __value0__`) | zeigt, welche Konnektoren als Auslöser/Aktion taugen |

## Was TechDoc nicht liefert

- **Kein `Nio`, kein vollständiger Konnektorsatz zum Einfügen.** Bausteine ohne Vorlage
  lassen sich damit **nicht** erzeugen — Falle 3 in [SKILL.md](../SKILL.md) gilt weiter.
  TechDoc sagt, *wie* ein Konnektor heißt, die Vorlage sagt, *welche* im XML stehen.
- **Kein Attributname für Baustein-Eigenschaften** (`Wap`, `TimeEnd`, `Dir` …). Parameter mit
  Konnektor stehen drin, Eigenschaften aus dem Eigenschaftenfenster nicht durchgängig.
- `ShortDescription` ist im deutschen Paket teils **englisch**; `Name` und `Description` sind
  übersetzt. Wer deutsche Kürzel-Beschreibungen braucht, nimmt `Description`.
- Kein Zusammenhang zu `FactoryPresets.xml` — die Auto-Konfiguration-Raumvorlagen bleiben dort.

## Nebenfund: `DEU.LxRes` / `ENG.LxRes` — die Meldungstabelle des Miniservers

3.674 Strings (`<String IDV="…" Text="…"/>`), mit denen der Miniserver Systemmeldungen,
Loxone-Monitor-Zeilen und Fehlertexte formatiert. Für die Frage „Was pusht der Miniserver
außerhalb der Visualisierung?" ist sie die Referenz — Befund in
[miniserver-dateizugriff.md](miniserver-dateizugriff.md), Abschnitt 4.

## Offen

- **[OFFEN]** Ob `ControlType` mit der Typnummer im Projekt-XML (`Document/@…` oder
  `C/@…`) übereinstimmt — nicht geprüft.
- **[OFFEN]** Abgleich aller 220 `LxType`-Einträge gegen den 179-Baustein-Katalog des Skills
  (`bausteine-*.md`) und gegen [xml-doku-mapping.md](xml-doku-mapping.md). Erst danach darf
  der Katalog als „aus TechDoc verifiziert" gelten.
