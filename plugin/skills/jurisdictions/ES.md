# ES — Spain jurisdiction pack

> the agent-facing orientation; complements the backend `ES` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Civil law, with **autonomous-community** (foral) civil-law variations in some
regions (Cataluña, Navarra, Aragón, País Vasco, Galicia…). Codes: Código civil,
Código penal, LEC (civil procedure), LECrim. Heavy EU overlay. No stare decisis,
but *doctrina jurisprudencial* of the Tribunal Supremo (2+ concordant STS) matters.

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `art. <N> CC` / `art. <N> CP` / `art. <N> LEC`; case law
  `STS <num>/<año>` + **ECLI:ES:TS:<año>:<num>** (or CENDOJ ROJ number);
  `STC <num>/<año>` (constitutional).
- **Hard locks**: ECLI/ROJ is the key; no paid-DB (Aranzadi/La Ley) locators from
  memory. Flag when a foral civil law displaces the common Código civil.
- **Official free whitelist**: **BOE** (boe.es — consolidated law, open-data API);
  **CENDOJ** (poderjudicial.es — case-law search); Tribunal Constitucional;
  EUR-Lex.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Statutes | **BOE open-data API** (consolidated legislation) | none |
| Case law | CENDOJ (search only — see compliance); robinlawyer spanish-law pack | none |
| Entities | Registro Mercantil (paid); **BORME** via BOE API (open) | — |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: add an `es_boe` directive with the article; the BOE consolidated-law
  API grounds it — whether a dedicated adapter is live is in the registry, else
  the generic ladder + `sourceHint` handles it.
- Case law: **discovery-only** — see compliance.

## Compliance limits
**CENDOJ prohibits bulk download / commercial reuse without authorization, and now
serves a CAPTCHA that blocks agents.** So: read individual decisions in the browser
/ via web, cite by ECLI, and pass the official URL as `sourceHint` — never bulk
harvest CENDOJ. AEPD (data protection); client data stays client-side.

## Method notes
- Civil-law method; check for **foral** civil law by the party's región.
- EU overlay (regulations direct; directives transposed — check the *ley/real
  decreto de transposición*).
- Draft in Spanish (or co-official language where applicable); formal register for
  *demanda* / *contestación*.

## Community skills to consult
**`betobetico/the agent-para-abogados`** (Spanish adaptation — 20 modules);
`robinlawyer/the agent-for-spanish-law` (BOE/CENDOJ/TC/TJUE/AEPD, early)
(interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
Personal actions **5 años** (art. 1964 CC, reduced from 15 in 2015); real actions
30 yrs; specific shorter periods. Foral regions may differ.
