# EU — European Union (supranational overlay)

> the agent-facing orientation; complements the backend `EU` module. Pair with
> `relex-research` + `relex-citations`. **This is an OVERLAY** — most matters are a
> national jurisdiction pack + this EU layer.

## Legal family & sources of law
Supranational. **Regulations** apply directly in all member states; **Directives**
bind as to result and are **transposed** into national law (always check the
national implementing act + deadline); **Decisions** bind their addressees. CJEU
(Court of Justice + General Court) gives binding interpretation; the Charter of
Fundamental Rights applies when member states implement EU law.

## Citation — schema + hard locks + official whitelist
- **Schema**: legislation `Regulation (EU) 2016/679`, `Directive 2014/24/EU`, with
  article refs `Art. <N>(<x>)`. Case law `Case C-<num>/<yr> <Name>, EU:C:<yr>:<num>`
  (ECLI) — e.g. `Case C-131/12 Google Spain, EU:C:2014:317`.
- **Hard locks**: the CELEX/ECLI is the key; for a Directive, **never rely on it
  directly against a private party without checking transposition** (no horizontal
  direct effect) — cite the national implementing provision.
- **Official free whitelist**: **EUR-Lex** (+ **CELLAR SPARQL**,
  publications.europa.eu — no auth); CURIA (curia.europa.eu) for CJEU.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Legislation + case law | **EUR-Lex CELLAR SPARQL** (no auth, 60s timeout) | none |
| MCP | cyanheads/eur-lex-mcp-server (CELLAR graph, EuroVoc, hosted); scimorph/eur-lex-mcp | none |
| Case law | CURIA (via ECLI → CELLAR) | none |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Legislation: **`eu_eurlex`** (Cellar) adapter enabled — grounds a Regulation/
  Directive article verbatim by CELEX.
- CJEU case law: reachable via CELLAR/ECLI — pass the EUR-Lex/CURIA URL as
  `sourceHint` on a `case_law` directive.

## Compliance limits
CELLAR/EUR-Lex are open (respect the SPARQL timeout / fair use). No PII concern in
EU primary sources; client data stays client-side per the relevant national pack.

## Method notes
- **Regulation vs Directive**: direct application vs transposition — this changes
  what you cite and whether it binds the parties.
- **Primacy + consistent interpretation**: national law read in light of EU law;
  CJEU preliminary rulings bind.
- Pair with the national pack for the forum, limitation and procedure (EU rarely
  sets private-claim limitation — national procedural autonomy).

## Community skills to consult
`cyanheads/eur-lex-mcp-server`, `Ansvar EU_compliance_MCP` (61 regulations),
`Hack23/European-Parliament-MCP` (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
EU law usually leaves limitation to national law (equivalence + effectiveness).
Specific EU regimes have their own: competition-damages (Dir. 2014/104, **5 yrs**
min.), state-aid recovery **10 yrs**, EU staff/institution actions have Treaty
time-limits.
