# Relex × MCP (generic)

Connect **any MCP-compatible agent** to **Relex** legal case management —
**without ever receiving client PII**.

> Relex doesn't replace your model. It lets you use it end-to-end by protecting
> PII and know-how, automating customer service, handling payments, and opening
> a new client market. See [`docs/positioning.md`](docs/positioning.md).

This is the **agent-agnostic** package. Platform-specific plugins live in:

| Agent | Repository |
|-------|------------|
| Claude | [relexyou/relex-claude](https://github.com/relexyou/relex-claude) |
| ChatGPT / Codex | [relexyou/relex-gpt](https://github.com/relexyou/relex-gpt) |
| Grok (xAI) | [relexyou/relex-grok](https://github.com/relexyou/relex-grok) |
| Gemini | [relexyou/relex-gemini](https://github.com/relexyou/relex-gemini) |

Those repos are **downstream** of the same MCP surface documented here. Skills
and workflow guidance stay shared; only client packaging and install UX differ.

## MCP endpoint (the whole product surface)

```
https://relex.you/api/mcp
```

Transport: **Streamable HTTP** (MCP). Auth: **OAuth 2.1 + PKCE** (browser
sign-in with Google/Apple — **no key to paste**). Static API keys work as a
CI/headless fallback.

Two tools, fixed ~1k-token footprint:

| Tool | Purpose |
|------|---------|
| `search` | Discover API endpoints from the OpenAPI surface |
| `execute` | Call one validated endpoint with the user's auth + PII guard |

The MCP handler lives in the **Relex backend** (`/v1/mcp`). This repo is
configuration, skills, and install docs — not a separate server to host.

## Quick connect (any MCP client)

### JSON config (Cursor, Windsurf, Claude Desktop, etc.)

```json
{
  "mcpServers": {
    "relex": {
      "type": "http",
      "url": "https://relex.you/api/mcp"
    }
  }
}
```

Some clients use `url` / `httpUrl` instead of `type`+`url`. Same endpoint.

### CLI examples

```bash
# Claude Code (HTTP + OAuth)
claude mcp add --transport http relex https://relex.you/api/mcp

# Gemini CLI
gemini mcp add --transport http relex https://relex.you/api/mcp

# API-key fallback (CI / headless)
claude mcp add --transport http relex https://relex.you/api/mcp \
  --header "Authorization: Bearer rlx_..."
```

After connect, say: **"Set up my practice workflow with Relex."**

## Personal vs Team (applies across hosts)

Most AI products mirror the same pattern:

| Plan type | Who installs the connector | Who signs in |
|-----------|----------------------------|--------------|
| **Personal** (Pro / Max / Plus / individual) | **You** add the custom connector / MCP server | **You** click Connect and complete OAuth |
| **Team / Business / Enterprise** | **Owner or admin** adds the connector once for the org | **Each member** opens Settings → Connectors (or Apps), finds Relex already listed, and clicks **Connect** to link *their* Relex account |

Members on Team plans **cannot** usually add custom connectors themselves.
If Relex is missing from the list, ask your admin to install it. If it is
listed but not connected, only you can complete the OAuth step for your account.

Full flows: [`docs/install.md`](docs/install.md).

## Layout

```
relex-mcp/
├── plugin/
│   ├── .mcp.json              Remote MCP connector URL
│   ├── skills/                PII-safe workflow skills (agent-agnostic)
│   ├── agents/                Onboarding guide
│   ├── commands/              /relex-setup, /relex-connect
│   └── references/
├── docs/
│   ├── install.md             All clients + personal vs team
│   ├── connect-generic.md     Cursor, Windsurf, custom hosts
│   └── positioning.md
├── SECURITY.md
└── README.md
```

## What the agent can do

Act as **senior counsel + steering layer** over Relex's execution harness:
start cases, steer drafting sessions, audit the case ontology, ground citations,
run intake → e-sign → invoice — while **never** receiving names, national IDs,
or document plaintext. Those steps deep-link into the browser.

## Docs on relex.you

- [MCP Server overview](https://relex.you/docs/mcp)
- [Connectors hub](https://relex.you/docs/connectors)
- [For AI Agents](https://relex.you/for-agents)

## License

AGPL-3.0-or-later — see [LICENSE](LICENSE).
