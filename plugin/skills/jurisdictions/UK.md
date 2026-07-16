# UK — United Kingdom jurisdiction pack

> the agent-facing orientation; complements the backend `UK` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Common law — but **three distinct legal systems**: England & Wales, **Scotland**
(mixed civil/common — different institutions, terminology, limitation), Northern
Ireland. **Always establish which system applies before citing.** UK-wide statutes
(Acts of Parliament) coexist with devolved legislation (Scottish Parliament,
Senedd, NI Assembly).

## Citation — schema + hard locks + official whitelist
- **Schema**: **OSCOLA**. Statutes `<Short Title> <Year>, s <N>` (e.g.
  `Consumer Rights Act 2015, s 9`). Case law with **neutral citation** where it
  exists: `<Party> v <Party> [<Year>] <Court> <Num>` (e.g. `[2024] UKSC 15`),
  plus a report cite (`[2024] AC 1`).
- **Hard locks**: neutral citation + pinpoint paragraph `[42]`. No paid-DB
  (Westlaw UK/LexisLibrary) locators from memory. Distinguish binding vs
  persuasive by court hierarchy and system (an E&W decision is not binding in
  Scotland).
- **Official free whitelist**: **legislation.gov.uk** (statutes, open API);
  **Find Case Law** (caselaw.nationalarchives.gov.uk, LegalDocML); the court's own
  judgment site; BAILII (finding aid, restrictive terms).

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Statutes | **legislation.gov.uk** API (CLML XML) | none |
| Case law | **Find Case Law** (National Archives); paulieb89/uk-legal-mcp (14 tools incl. Hansard, HMRC) | none |
| Entities | **Companies House** API | free key |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: add a `uk_legislation` directive with the Act + section; the
  legislation.gov.uk API/HTML grounds it — whether a dedicated adapter is live is
  in the registry, else the generic ladder + `sourceHint` handles it.
- Case law: **discovery-first, single decisions only** — see compliance below.

## Compliance limits
**Find Case Law re-use**: the **Open Justice Licence** permits reading and normal
citation, but **bulk / "computational analysis" (programmatic mass ingestion)
requires a free licence application**. So: read and cite individual decisions and
pass their URLs as `sourceHint`; do not bulk-harvest without the licence. ICO
(data protection), FCA, CMA, Ofcom for sectoral matters.

## Method notes
- **System first** (E&W / Scotland / NI) — it changes courts, terminology,
  limitation and sometimes substance.
- Statutory interpretation + binding precedent (stare decisis applies — unlike
  the civil-law packs); Supreme Court binds all below.
- OSCOLA footnote discipline for any formal document.

## Community skills to consult
**`uk-agents/uk-legal-plugins`** (BAILII/Find Case Law/legislation.gov.uk/Hansard/
Companies House/ICO/FCA wiring); `paulieb89/uk-legal-mcp`
(interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
**E&W — Limitation Act 1980**: contract/tort **6 yrs** (ss 2, 5); personal injury
**3 yrs** (s 11); latent damage 3 yrs from knowledge / 15-yr longstop (s 14A/14B);
defamation **1 yr**. **Scotland differs** (Prescription and Limitation (Scotland)
Act 1973 — 5-yr short negative prescription).
