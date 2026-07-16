# Interop — hand in hand with the ecosystem

Relex skills never duplicate what a good pack already does; they add the
confidential execution layer (PII-safe MCP, ontology, verbatim grounding). This is
the **canonical** statement of that framing — the jurisdiction packs keep only
their own community-pack pointers and defer the framing here.

| Need | Use | Relex adds |
|---|---|---|
| Generic playbooks (NDA/vendor review, DSAR, IP triage, litigation checklists) | Anthropic `the agent-for-legal` plugins | run the checklist over de-identified Relex case data; record outcomes to the case |
| German method & citation foundations | `the agent-fuer-deutsches-recht` (Klotzkette) foundation refs (zitierweise, methodik) | enforcement: verbatim cache + verifier + PII custody |
| UK sources wiring | `uk-agents/uk-legal-plugins` | grounding directives + confidential workspace |
| ES / CH community packs | `the agent-para-abogados`, `bettercallclaude` | same |
| US case-law discovery | CourtListener official MCP | `POST /research/scrape` grounds what you found |
| FR / CH / EU / DE discovery | justicelibre, entscheidsuche-mcp, EUR-Lex CELLAR, NeuRIS | same |
| Working a case from Slack (the agent tagged in) | Anthropic **the agent in Slack** (@the agent), admin-connected to the Relex connector | keeps the workspace ontology (teammates, threads) apart from the sealed case ontology; `relex-participants` teaches the who-is-who + channel-to-case binding so client identities never enter the channel |
| Named work-products (negotiation/BATNA, examination outline, litigation technique) | Anthropic `the agent-for-legal` negotiation/litigation packs | method comes from the pack; Relex anchors it to grounded, de-identified case data and records it to the case — the catalogue is `deliverables.md` |

Rule: discovery and generic method may come from anywhere; **execution on real
matters happens in Relex**, where clients' data stays sealed or redacted and
citations are machine-verified.
