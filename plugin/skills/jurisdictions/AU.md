# AU — Australia jurisdiction pack

> the agent-facing orientation; complements the backend `AU` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Common law; **federal (Commonwealth) + 6 states + 2 territories**. Commonwealth
statutes coexist with state Acts; the Constitution divides powers. Stare decisis
applies (High Court binds all). Establish **which jurisdiction (Cth / state)** and
which court hierarchy before citing.

## Citation — schema + hard locks + official whitelist
- **Schema**: **AGLC4**. Statutes `<Short Title> <Year> (<Jurisdiction>) s <N>`
  (e.g. `Competition and Consumer Act 2010 (Cth) s 18`). Case law with **neutral
  citation** `<Party> v <Party> [<Year>] <Court> <Num>` (e.g. `[2020] HCA 5`) +
  authorised report (`(2020) 270 CLR 1`).
- **Hard locks**: neutral citation + pinpoint paragraph; **jurisdiction tag**
  `(Cth)`/`(NSW)`/… is mandatory on statutes. No paid-DB (Westlaw AU/LexisNexis AU)
  locators from memory.
- **Official free whitelist**: **legislation.gov.au** (Federal Register of
  Legislation) + state registers (legislation.nsw.gov.au …); **AustLII**
  (austlii.edu.au); court sites (hcourt.gov.au, fedcourt.gov.au).

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Case law + legislation | **AustLII** (read; don't bulk-scrape) | none |
| Federal legislation | legislation.gov.au | none |
| Both (local-first) | **russellbrenner/jurisd** (offline GraphRAG + AGLC4 linting) | none |
| Entities | **ABN Lookup** web services; ASIC data on data.gov.au | free key |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: add a `legislation.gov.au` directive (federal) — the generic ladder
  fetches the official text (a dedicated adapter is a backend follow-up). State
  registers via `sourceHint`.
- Case law: **discovery-first** — AustLII discourages scraping, so read the
  decision and pass its AustLII/court URL as `sourceHint`.

## Compliance limits
OAIC (Privacy Act 1988 — APPs); client data stays client-side. **AustLII
discourages automated scraping** — discovery is read-then-`sourceHint`, not bulk.
jade.io is freemium (own cookie).

## Method notes
- **Jurisdiction first** (Cth vs state) — changes courts, statutes, limitation.
- Stare decisis; High Court + intermediate appellate courts bind.
- Draft in Australian English; AGLC4 citation discipline.

## Community skills to consult
**`russellbrenner/jurisd`** (local-first GraphRAG, AGLC4 linting, offline citation
graph — architecturally strong) (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
State Limitation Acts govern — commonly **6 yrs** contract/tort (e.g. Limitation
Act 1969 (NSW) s 14), **3 yrs** personal injury in several states, with
discoverability rules; Cth causes have their own.
