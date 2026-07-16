# CH — Switzerland jurisdiction pack

> the agent-facing orientation; complements the backend `CH` module. Pair with
> `relex-research` + `relex-citations`. **Note:** a dedicated backend CH method
> module may be thin — lean on this pack + the community Swiss pack.

## Legal family & sources of law
Civil law; **federal law + 26 cantons**; **trilingual** (DE/FR/IT, all
authentic). Federal codes: ZGB (civil), OR (obligations), StGB, ZPO, StPO, SchKG
(debt/bankruptcy). Cantonal law governs procedure-adjacent, tax, public matters.
No stare decisis (Bundesgericht decisions are persuasive, not binding).

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `Art. <N> OR` / `Art. <N> ZGB` (+ Abs./lit.). Published
  case law `BGE/ATF <vol> <part> <page> E. <consideration>` (e.g. `BGE 145 III 72
  E. 3.2`); unpublished by docket `<chamber>_<num>/<year>` (e.g. `4A_123/2023`).
- **Hard locks**: cite in the **language of the decision/canton**; the
  consideration (E./consid.) is the pinpoint. No proprietary-DB cites from memory.
- **Official free whitelist**: **Fedlex** (fedlex.admin.ch — SR/AS/BBl, +SPARQL
  fedlex.data.admin.ch); **entscheidsuche.ch** (BGer + all 26 cantons,
  licence-free); bger.ch; cantonal via lexfind.ch.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Case law | **entscheidsuche.ch** + its official MCP (mcp.entscheidsuche.ch) | none |
| Statutes | Fedlex (SPARQL + downloads); cantonal lexfind.ch | none |
| Entities | **Zefix** REST API (zefix.admin.ch) | free, email-registered |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: **`ch_fedlex`** adapter enabled — a `statute` directive grounds
  `Art. … OR/ZGB` verbatim.
- Case law: **discovery-first** (no dedicated adapter yet) — find on
  entscheidsuche.ch, pass its URL as `sourceHint` on a `case_law` directive.

## Compliance limits
EDÖB (federal data-protection authority); revDSG (revised Swiss data-protection
act) governs client data — Relex keeps PII client-side. FINMA/WEKO for
financial/competition. No bulk-scraping restrictions on entscheidsuche (open).

## Method notes
- **Language**: draft and cite in the cantonal/decision language; a matter may
  span DE/FR/IT — surface which applies.
- Civil-law method (no precedent-binding); but *ständige Rechtsprechung* of the
  Bundesgericht carries strong persuasive weight.
- OR/ZGB claim structure; SchKG for debt-enforcement matters.

## Community skills to consult
**`fedec65/bettercallclaude`** (Swiss pack — agents + skills + bundled MCPs);
`entscheidsuche-mcp`, `fedlex-mcp` (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
OR prescription (revised 2020): general contractual **10 yrs** (Art. 127 OR);
periodic **5 yrs** (Art. 128); **tort 3 yrs** relative / 10 yrs absolute
(Art. 60, revised); personal-injury absolute 20 yrs.
