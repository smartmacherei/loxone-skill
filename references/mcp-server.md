# Loxone MCP-Server — Referenz

**Stand:** 28.08.2026 · Loxone Config 17.1.7.27 · Plugin `McpServer` (Katalog-Version 1.0.0, laut
Changelog in 17.1.7.27 bereits 1.0.5)

**Quellen — alles verifiziert, nichts geraten:**

| Quelle | Was daraus stammt |
|---|---|
| Plugin-Doku `McpServer_DEU.xml` aus `McpServer_1_0_0.LxAddOn` | Einrichtung, URL-Bildung, Berechtigungen, Client-Anleitungen, Reverse-Proxy |
| Plugin-Manifest `McpServer.json` (gleiches Paket) | Parameter, Regex, `needGen2`, `minVersion`, Instanzlimit |
| `/sys/addons.json` vom Miniserver | Katalogeintrag, Download-URL |
| Live-Abfrage eines Miniservers FW 17.1.6.30 | OAuth-Metadaten, `WWW-Authenticate`, Rate-Limit |
| Plugin-Binary `LxMcpServer` | Werkzeugnamen — **nicht offiziell dokumentiert** |
| [ivantichy/loxone-mcp-proxy](https://github.com/ivantichy/loxone-mcp-proxy), [Smarteon/lox-mcp](https://github.com/Smarteon/lox-mcp) | Fallback-Bridges |

> Kein Cloud-Dienst nötig: Der Server läuft **auf dem Miniserver**. Der Assistent authentifiziert
> sich direkt dort, jede Anfrage läuft mit den Rechten des angemeldeten Loxone-Benutzers.

---

## 1. Voraussetzungen

| Punkt | Wert | Quelle |
|---|---|---|
| Miniserver-Generation | **Gen 2 zwingend** (`"needGen2": true`) — **Gen 1 wird nicht unterstützt** | Manifest |
| Mindest-Firmware | `minVersion: 17010603` → Config/FW **17.1.6.x**; Feature laut Changelog ab **17.1.6.30** | Manifest, Changelog |
| Instanzen | **maximal 1 pro Miniserver** (`maxCountPerMiniserver: 1`) | Katalog |
| An Miniserver gebunden | nein (`boundToMiniserver: false`) | Katalog |
| Client | MCP-fähiger Assistent, der den veröffentlichten Endpunkt erreicht | Plugin-Doku |
| Konto | eigener Loxone-Benutzer für den Assistenten | Plugin-Doku |

Das Plugin ist **kein physisches Gerät** (`isPhysicalDevice: false`), braucht **weder Raum noch
Kategorie** (`needRoom`/`needCategory`: false) und hat genau ein Kind-Objekt vom Typ `online`.

---

## 2. Einrichtung in Loxone Config

1. **Netzwerkperipherie → MCP-Server** als Netzwerkgerät anlegen (Plugin `McpServer` zur
   Installation hinzufügen). Erscheint erst ab Config/FW 17.1.6.x.
2. Optional die beiden URL-Parameter setzen (§ 6) — **im Normalfall leer lassen.**
3. **Eigenen Loxone-Benutzer** für den Assistenten anlegen, mit minimalen Rechten (§ 4).
4. **Speichern und in den Miniserver laden.** Das Plugin startet danach selbst.
5. MCP-URL ermitteln (§ 3) und im Client eintragen (§ 7).

---

## 3. Die MCP-URL

Die Adresse endet **immer** auf `/mcp`. Es gibt zwei, beide werden aus der Loxone-Cloud-DNS
gebildet — Muster `<ip-mit-bindestrichen>.<seriennummer>.dyndns.loxonecloud.com`:

| Zugriffsweg | So ermitteln | Beispiel |
|---|---|---|
| **Über das Internet** | `https://connect.loxonecloud.com/<SERIENNUMMER>` im Browser öffnen, Weiterleitung abwarten, angezeigten Host kopieren, `/mcp` anhängen | `https://203-0-113-42.504f94aabbcc.dyndns.loxonecloud.com/mcp` |
| **Im lokalen Netz** | lokale IP `https://<MINISERVER-IP>` aufrufen, Weiterleitung abwarten, Host kopieren, `/mcp` anhängen | `https://192-0-2-10.504f94aabbcc.dyndns.loxonecloud.com/mcp` |

Die Seriennummer ist die MAC ohne Doppelpunkte.

**Was das Plugin wirklich veröffentlicht**, zeigt seine Diagnoseseite — angemeldet aufrufen:

```
https://<MINISERVER-IP>/dev/sps/io/<uuid>/hello
```

`<uuid>` ist die Kennung des MCP-Server-Objekts in Loxone Config. Die Seite listet die wirksame
Internet- und lokale URL und markiert sie als *automatisch* oder *benutzerdefiniert*.

---

## 4. Authentifizierung — OAuth 2.1, nicht Basic-Auth

Ein `GET /mcp` ohne Token antwortet mit `401` und verweist auf die Protected-Resource-Metadaten:

```
www-authenticate: Bearer realm="lx-mcp",
  resource_metadata="https://<host>/mcp/.well-known/oauth-protected-resource"
```

**Basic-Auth mit Loxone-Benutzer und Passwort funktioniert am `/mcp`-Endpunkt nicht** — auch mit
gültigen Zugangsdaten kommt `401`. Häufigster Irrtum beim manuellen Testen.

Metadaten unter `/mcp/.well-known/oauth-authorization-server` (live abgefragt):

| Feld | Wert |
|---|---|
| `issuer` / `resource` | `https://<host>/mcp` |
| `authorization_endpoint` | `https://<host>/mcp/oauth/authorize` |
| `token_endpoint` | `https://<host>/mcp/oauth/token` |
| `registration_endpoint` | `https://<host>/mcp/oauth/register` (Dynamic Client Registration) |
| `grant_types_supported` | `authorization_code`, `refresh_token` |
| `code_challenge_methods_supported` | `S256` — PKCE ist Pflicht |
| `response_types_supported` / `response_modes_supported` | `code` / `query` |
| `token_endpoint_auth_methods_supported` | `none` (Public Client) |
| `scopes_supported` | **leer** — Rechte kommen aus dem Loxone-Benutzer, nicht aus Scopes |

Im Binary existiert zusätzlich ein `revoke`-Endpunkt (`lx_mcp_server::oauth::endpoints::revoke`),
der **nicht** in den Metadaten steht — *unbestätigt*, ob öffentlich nutzbar.

Beim ersten Verbinden erscheint eine Consent-Seite („… möchte auf Ihren Loxone Miniserver
zugreifen"), auf der Benutzername und Passwort eingegeben werden.

### Berechtigungen

Der Assistent handelt **als der angemeldete Loxone-Benutzer** — exakt dessen Räume, Kategorien und
Steuerungen, nicht mehr. Das ist die einzige Zugriffsbeschränkung, die der Miniserver selbst
erzwingt.

| Nicht unterstützt — braucht erweiterte Rechte |
|---|
| Benutzerverwaltung: Benutzer, Rechte und Berechtigungen anlegen oder ändern |
| Expertenmodus und Konfigurationsänderungen aus Loxone Config |
| Automatik-Designer |

**Visu-Passwort:** Bausteine mit Visualisierungspasswort kann der Assistent bedienen, wenn das
Visu-Passwort mitgegeben wird. Es gilt nur für den einzelnen Befehl und wird nicht gespeichert.
Das ist ein **anderes** Passwort als das für erweiterte Rechte.

---

## 5. Werkzeuge

Offiziell dokumentiert ist nur die Zweiteilung: **Read** (Struktur, Zustand, Historie, Statistik —
ändert nichts) und **Write** (Befehle). Das Plugin setzt dafür MCP-Annotationen (`readOnlyHint`,
`destructiveHint`, `idempotentHint`, `openWorldHint`); viele Clients lassen sich darüber auf reinen
Lesezugriff einschränken.

Die konkreten Namen sind **aus dem Binary v1.0.0 extrahiert und nicht offiziell dokumentiert** —
als Orientierung brauchbar, für Verlass darauf zu dünn:

| Werkzeug | Art | vermutlich |
|---|---|---|
| `control_find` | Read | Steuerungen suchen |
| `control_describe` | Read | Steuerung samt Konnektoren beschreiben |
| `control_state` | Read | aktuellen Zustand lesen |
| `control_history` | Read | aufgezeichneten Verlauf lesen |
| `control_statistics` | Read | Statistiken lesen |
| `control_types` | Read | verfügbare Steuerungstypen |
| `control_command` | Write | Befehl senden |
| `control_secured_command` | Write | Befehl mit Visu-Passwort |
| `system_status` · `system_messages` · `system_time` | Read | Systemzustand, Meldungen, Zeit |

---

## 6. Reverse-Proxy oder eigene Domain

**Die meisten Installationen brauchen das nicht.** Nötig wird es für **Cloud-Assistenten**: die
verbinden nur über Standard-HTTPS auf **Port 443** mit öffentlich vertrauenswürdigem Zertifikat,
während Remote Connect den Miniserver auf einem **nicht standardmäßigen Port** veröffentlicht.

| Parameter (`id`) | Wann setzen | Wert |
|---|---|---|
| `custom-remote-url` — „Benutzerdefinierte externe URL" | Proxy erreicht den Miniserver über dessen **externe** Adresse (öffentliche IP oder Remote Connect) | öffentliche MCP-URL des **Proxys**, z. B. `https://mcp.example.com/mcp` |
| `custom-local-url` — „Benutzerdefinierte lokale URL" | Proxy erreicht den Miniserver über dessen **lokale** LAN-Adresse | dito |

Beide: Vorgabe leer = automatisch. Beide akzeptieren laut Regex **nur `https://`**, optional mit
Port und optional mit `/mcp` am Ende. Ein leeres Feld behält für diesen Pfad die automatische
Adresse; man kann eines, das andere oder beide setzen.

Ausschlaggebend ist, **wie der Proxy den Miniserver erreicht** — nicht, wo der Assistent läuft.

---

## 7. Clients anbinden

Immer die URL aus § 3 einsetzen: Internet-Adresse für Cloud-Assistenten, lokale Adresse für
Assistenten im selben Netz.

| Client | Weg | Port 443 Pflicht? |
|---|---|---|
| **claude.ai** (Browser) | Settings → Connectors → benutzerdefinierter Connector, MCP-URL einfügen, danach im Connector mit Loxone-Konto anmelden | **ja** — läuft aus Claudes Cloud |
| **Claude Desktop → Connectors** | wie claude.ai, die URL geht an Claudes Cloud | **ja** |
| **Claude Desktop → Local MCP Server** | Settings → Developer → Edit Config; Bridge läuft auf dem eigenen Rechner | nein — jeder Port, auch Remote Connect |
| **Claude Code** | `claude mcp add --transport http loxone <MCP-URL>`, danach `/mcp` ausführen und Login im Browser abschließen | nein |
| **LM Studio** | Program Tab → Edit mcp.json, Eintrag mit `url`-Feld | nein |

**Claude Desktop** (`claude_desktop_config.json`) — die offiziell dokumentierte Variante nutzt
`mcp-remote` als lokale Bridge:

```json
{
  "mcpServers": {
    "loxone": {
      "command": "npx",
      "args": ["mcp-remote", "https://203-0-113-42.504f94aabbcc.dyndns.loxonecloud.com/mcp"]
    }
  }
}
```

Danach Claude Desktop neu starten; für den Loxone-Login öffnet sich ein Browserfenster.

**Claude Code:**

```
claude mcp add --transport http loxone https://203-0-113-42.504f94aabbcc.dyndns.loxonecloud.com/mcp
```

**LM Studio** (`mcp.json`):

```json
{
  "mcpServers": {
    "loxone": { "url": "https://203-0-113-42.504f94aabbcc.dyndns.loxonecloud.com/mcp" }
  }
}
```

---

## 8. Fallback: Community-Bridges

Nur nötig, wenn der native Server ausscheidet — Gen-1-Miniserver, FW < 17.1.6, oder wenn ein
**headless** Login ohne Browser gebraucht wird.

### 8.1 `loxone-mcp-proxy` (ivantichy) — Bridge **vor** den nativen Server

Löst genau zwei Probleme des nativen Servers: die **rotierende Relay-URL** und den **Browser-Zwang**
beim OAuth-Login. Setzt den nativen MCP-Server also voraus.

| Punkt | Wert |
|---|---|
| Voraussetzung | Node.js ≥ 20 (zero dependencies), Gen-2-Miniserver FW 17.1+ **mit** MCP-Plugin |
| Installation | `git clone https://github.com/ivantichy/loxone-mcp-proxy.git` — kein `npm install` nötig |
| Konfiguration | `.env` aus `.env.example`; Prüflauf `npm run login-check` |
| Transport zum Client | stdio |

| Env-Variable | Vorgabe | Zweck |
|---|---|---|
| `LOXONE_SERIAL` | — | **Pflicht** — Seriennummer (MAC ohne Doppelpunkte) |
| `LOXONE_USER` · `LOXONE_PASSWORD` | — | **Pflicht** — Loxone-Benutzer des Assistenten |
| `LOXONE_CONNECT_BASE` | `https://connect.loxonecloud.com` | Cloud-Connect-Einstieg |
| `LOXONE_CACHE_PATH` | `~/.loxone-mcp-proxy/cache.json` | Token-Cache, Mode `0600` |
| `LOXONE_REDIRECT_PORT` | `41678` | Loopback-Port für den OAuth-Redirect |
| `LOXONE_REQUEST_TIMEOUT_MS` | `120000` | Zeitlimit je MCP-Aufruf |
| `LOXONE_MAX_ATTEMPTS` | `6` | Anmeldeversuche |
| `LOXONE_CONNECT_MIN_INTERVAL_MS` | `2000` | Mindestabstand der Connect-Aufrufe (Rate-Limit) |
| `LOXONE_STATE_WARMUP` · `LOXONE_WARMUP_SWEEP` | `0` · `0` | Zustandstabellen nach dem Start anstoßen |
| `LOXONE_WARMUP_DELAY_MS` · `LOXONE_WARMUP_SPACING_MS` | `1000` · `150` | Timing des Warmlaufs |
| `LOXONE_WARMUP_MAX_CONTROLS` | `500` | Obergrenze der durchlaufenen Steuerungen |
| `LOXONE_DEBUG` · `LOXONE_LOG_LEVEL` | `0` · `info` | Diagnose |

```json
{
  "mcpServers": {
    "loxone": {
      "command": "node",
      "args": ["/absolute/path/to/loxone-mcp-proxy/src/index.js"]
    }
  }
}
```

Unter Windows die Backslashes im Pfad escapen.

Der Login läuft headless: Client-Registrierung → Benutzername und Passwort direkt an das
HTML-Login-Formular posten → Code gegen Token tauschen (PKCE) → Token cachen und automatisch
erneuern.

**Grenzen:** Zustandsdaten füllen sich beim nativen Plugin erst aus Änderungen — frische Sitzungen
zeigen zunächst Lücken. Der Connect-Endpunkt ist rate-limitiert (HTTP 429). Unter Windows greift
`0600` nicht; der Token-Cache hängt an den NTFS-ACLs. Die Token-Audience zeigt je nach Firmware auf
teils unerreichbare Relays — der Proxy routet stattdessen über den auflösbaren Connect-Eintrag.

### 8.2 `lox-mcp` (Smarteon) — eigenständiger Server **statt** des nativen

Redet direkt per WebSocket mit dem Miniserver, braucht das Plugin **nicht** — und läuft daher auch
mit **Gen 1**.

| Punkt | Wert |
|---|---|
| Voraussetzung | Java 21+, Miniserver Gen 1 **oder** Gen 2 |
| Installation | `lox-mcp-*-all.jar` aus den Releases, oder die Configurator-App |
| Verbindung | WebSocket für Live-Zustände; HTTP/SSE alternativ |
| Lizenz | AGPL-3.0 für privat/intern/Open-Source, sonst kommerzielle Lizenz |

```json
{
  "mcpServers": {
    "loxone": {
      "command": "java",
      "args": ["-jar", "/path/to/lox-mcp-all.jar", "--stdio", "--resources-as-tools"],
      "env": {
        "LOXONE_HOST": "http://192.0.2.10",
        "LOXONE_USER": "<BENUTZER>",
        "LOXONE_PASS": "<PASSWORT>"
      }
    }
  }
}
```

Werkzeuge: `control_device` (per UUID), `control_devices_by_room`, `control_devices_by_type`,
`control_devices_by_category`, `send_command` (roher Loxone-Befehl). Ressourcen unter
`loxone://structure/summary`, `loxone://rooms`, `loxone://devices/all`, `loxone://devices/states`,
`loxone://docs`. `--resources-as-tools` für Clients ohne Ressourcen-Unterstützung.

**Grenzen:** Zugangsdaten stehen im Klartext in der Client-Konfiguration — keine Rechtetrennung
über OAuth, der Loxone-Benutzer ist die einzige Schranke. Für Gen 2 mit aktueller Firmware ist der
native Server die bessere Wahl.

---

## 9. Fallen

**1. Basic-Auth am `/mcp` schlägt fehl — auch mit korrekten Zugangsdaten.**
`GET /mcp` mit `-u benutzer:passwort` liefert `401`. Der Endpunkt will einen OAuth-Bearer-Token.
Zum Prüfen, ob der Server *überhaupt* läuft, taugt der Statuscode trotzdem: **`401` heißt „da",
`404` heißt „nicht da"** — unbekannte Pfade auf dem Miniserver liefern `404`.

**2. Der Miniserver rate-limitet `/mcp` hart.**
Wenige Anfragen in schneller Folge quittiert er mit `429 {"error":"rate_limited"}` und
`retry-after: 300` — **fünf Minuten Sperre** (beobachtet auf FW 17.1.6.30). Beim Debuggen einzeln
und mit Abstand testen, nie in einer Schleife.

**3. Die MCP-URL ist nicht stabil.**
Sie enthält die IP im DNS-Namen und ändert sich bei Miniserver-Neustart und Relay-Wechsel. Fest
eingetragene URLs brechen irgendwann. Dafür gibt es `loxone-mcp-proxy` (§ 8.1).

**4. Remote Connect funktioniert für Cloud-Assistenten nicht.**
claude.ai und die *Connectors* von Claude Desktop verbinden nur über Port 443. Remote Connect
veröffentlicht auf einem anderen Port. Lösung: Reverse-Proxy oder eigene Domain (§ 6) — oder eine
lokale Bridge (Claude Desktop *Local MCP Server*, Claude Code, LM Studio), die jeden Port erreicht.

**5. Ein Reverse-Proxy muss den ganzen Host durchreichen, nicht nur `/mcp`.**
Der Login holt die Discovery unter `https://<host>/.well-known/oauth-authorization-server/mcp` —
das liegt **außerhalb** von `/mcp`. Ein Proxy, der nur `/mcp` weiterleitet, lässt den Assistenten
den Server finden, aber nicht den Login-Dienst. Die Verbindung scheitert dann ohne brauchbare
Meldung.

**6. Proxy gesetzt, aber falsches Feld — Login scheitert.**
`custom-remote-url` gegen `custom-local-url` richtet sich danach, **wie der Proxy den Miniserver
erreicht**, nicht danach, wo der Assistent läuft. Bleibt das Feld leer, veröffentlicht das Plugin
die automatische Adresse — und die zeigt hinter den Proxy statt auf ihn.

**7. Ein Assistent kann irren — die Benutzerrechte sind die einzige echte Bremse.**
Die Plugin-Doku warnt ausdrücklich: KI-Assistenten können eine Anfrage falsch verstehen oder die
falsche Steuerung bedienen. **Immer einen eigenen Benutzer mit Minimalrechten** anlegen, nie den
Admin. Entzug jederzeit durch Deaktivieren des Benutzers oder Entfernen der Verbindung.

**8. Gen 1 kann den nativen Server nicht.**
`needGen2: true` im Katalog. Für Gen 1 bleibt nur `lox-mcp` (§ 8.2).

**9. Nur eine Instanz je Miniserver.**
`maxCountPerMiniserver: 1` — mehrere MCP-Server-Objekte im Projekt sind nicht vorgesehen.

**10. Zustandsdaten sind direkt nach dem Start unvollständig.**
Das Plugin füllt seine Zustandstabellen aus Änderungen und beginnt erst mit der ersten
Zustandsabfrage zu sammeln. Direkt nach dem Verbinden können Werte fehlen, bis sich physisch etwas
ändert.
