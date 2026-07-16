# IT — Italy jurisdiction pack

> the agent-facing orientation; complements the backend `IT` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Civil law. Codes: Codice civile, Codice penale, Codice di procedura civile/penale.
Heavy EU overlay. No stare decisis; *Corte di cassazione* (esp. *sezioni unite*)
lines are highly persuasive; *Corte costituzionale* on constitutionality.

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `art. <N> c.c.` / `art. <N> c.p.`; case law
  `Cass., sez. <X>, n. <num>/<anno>` (e.g. `Cass., sez. un., n. 12345/2020`) +
  **ECLI**; `Corte cost., n. <num>/<anno>`.
- **Hard locks**: number/year is the key; no paid-DB locators from memory.
- **Official free whitelist**: **Normattiva** / **dati.normattiva.it** (statutes,
  Akoma Ntoso, ELI URIs); **Italgiure SentenzeWeb** (last ~5 yrs Cassazione,
  free); cortecostituzionale.it; EUR-Lex.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Statutes | **dati.normattiva.it** (new open API/exports) | none |
| Case law | Italgiure **SentenzeWeb** (recent Cassazione, free) | none |
| Both + calcs | **capazme/mcp-legal-it** (146 legal-fiscal calculators + Normattiva/EUR-Lex/Italgiure) | none |
| Entities | Registro Imprese (InfoCamere, paid); VAT check (Agenzia Entrate) | — |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: **`it_normattiva`** adapter enabled — grounds `art. … c.c.` verbatim
  (upgradeable to the new dati.normattiva API).
- Case law: **discovery-first** — SentenzeWeb covers recent Cassazione (free); the
  full ItalgiureWeb archive is reserved/paid, so older decisions are discovery-only
  via `sourceHint`.

## Compliance limits
Garante per la protezione dei dati personali (GPDP); client data stays client-side.
Full Italgiure archive = reserved tiers (don't assume bulk access).

## Method notes
- Civil-law syllogism; cite the *massima* + the decision. EU overlay (regulations
  direct, directives transposed — check the *decreto di recepimento*).
- Draft in Italian; formal register for *atto di citazione* / *comparsa*.

## Community skills to consult
**`capazme/mcp-legal-it`** (unusually deep — calculators + sources)
(interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
*Prescrizione ordinaria* **10 anni** (art. 2946 c.c.); **5 anni** for some
(art. 2948, e.g. periodic payments); shorter for specific actions.
