# FR — France jurisdiction pack

> the agent-facing orientation; complements the backend `FR` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Civil law (Napoleonic). Codes: Code civil, Code de commerce, Code pénal, Code de
procédure civile, Code du travail. Heavy EU overlay. No stare decisis, but
**jurisprudence constante** (settled Cour de cassation lines) carries strong
weight; the *Conseil constitutionnel* and *Conseil d'État* (administrative) are
separate orders.

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `art. <N> C. civ.` / `art. L. <N> C. trav.` (L=législatif,
  R=réglementaire). Case law `Cass. <chamber>, <date>, n° <pourvoi>` (e.g.
  `Cass. 1re civ., 15 mars 2023, n° 21-12.345`) + **ECLI** where issued; admin
  `CE, <date>, n° <req>`.
- **Hard locks**: the *numéro de pourvoi* is the docket key; no paid-DB (Dalloz/
  Lexis/Lamy) locators from memory. Two court orders — don't cite a *judiciaire*
  decision for an *administratif* question.
- **Official free whitelist**: **Légifrance** (statutes + consolidated codes);
  **Judilibre** (Cour de cassation open data); courdecassation.fr; conseil-etat.fr;
  EUR-Lex for EU. DILA bulk dumps (LEGI/JORF/KALI) on data.gouv.fr.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Case law | **justicelibre MCP** (~3M decisions, no key); Judilibre | none / PISTE |
| Statutes | Légifrance (via PISTE); DILA data.gouv.fr dumps | PISTE / none |
| Entities | **INPI RNE** API; Sirene (INSEE); annuaire-entreprises.data.gouv.fr | free key / open |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Both **`fr_dila`** (Légifrance statutes) and **`fr_judilibre`** (case law)
  adapters exist but are **gated on PISTE OAuth credentials**
  (`LEGIFRANCE_OAUTH_CLIENT_ID/SECRET`). Until provisioned (operator step),
  grounding falls back to the generic ladder + a `sourceHint` (a legifrance.gouv.fr
  or courdecassation.fr URL you found via justicelibre/web).

## Compliance limits
CNIL (data protection); client data stays client-side in Relex. AMF (markets),
Arcom, DGCCRF for sectoral matters. Judilibre decisions are pseudonymised at
source.

## Method notes
- Civil-law syllogism (majeure/mineure/conclusion); *visa* of the texts applied.
- Two jurisdictional orders (judiciaire vs administratif) — route correctly.
- Draft in French; formal register for *conclusions* / *assignation*.

## Community skills to consult
**`Dahliyaal/justicelibre`** (no-key case-law MCP — a standout),
`jmtanguy/droit-francais-mcp`, `mauryaland/mcp-magistrat-civil` (+ magistrate
reasoning skill), `pylegifrance/mcp-server-legifrance`
(interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
*Prescription* de droit commun **5 ans** (art. 2224 C. civ.) from knowledge;
real-property 30 yrs (art. 2227); *action publique* varies by offence class;
labor claims often 2–3 yrs (Code du travail).
