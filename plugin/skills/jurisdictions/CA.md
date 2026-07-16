# CA — Canada jurisdiction pack

> the agent-facing orientation; complements the backend `CA` module. Pair with
> `relex-research` + `relex-citations`. **Note:** a dedicated backend CA method
> module may be thin — lean on this pack + CanLII.

## Legal family & sources of law
**Bijural**: common law in 9 provinces + 3 territories; **Québec is civil law**
(Code civil du Québec). **Bilingual** (EN/FR — both authentic federally and in
NB/QC/ON to degrees). Federal statutes + provincial statutes; the division of
powers (Constitution Act 1867) governs which level legislates. Stare decisis
applies in common-law provinces (SCC binds all).

## Citation — schema + hard locks + official whitelist
- **Schema**: **McGill Guide**. Statutes `<Title>, RSC 1985, c <X>, s <N>` (federal)
  / `RSO 1990, c <X>` (provincial). Case law with **neutral citation**
  `<Party> v <Party>, <Year> <Court> <Num>` (e.g. `2020 SCC 5`) + a reporter cite.
- **Hard locks**: neutral citation + pinpoint paragraph. No paid-DB (Westlaw
  Canada/Lexis) locators from memory. For a Québec matter, cite the **CcQ** and
  Québec sources, not common-law authorities.
- **Official free whitelist**: **laws-lois.justice.gc.ca** (federal, XML bulk);
  provincial (BC Laws — has an API; Ontario e-Laws); **CanLII** (canlii.org);
  decisions.scc-csc.ca.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Case law | **CanLII** (site) + `mohammadfarooqi/canlii-mcp` (metadata/citator API) | CanLII key |
| Federal statutes | laws-lois.justice.gc.ca (XML) | none |
| Provincial statutes | BC Laws API; Ontario e-Laws bulk | none |
| Entities | **Corporations Canada** Federal Corporation API (ISED) | free key |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: add a `ca_justice` directive (laws-lois XML) to ground a federal
  section — whether a dedicated adapter is live is in the registry, else the
  generic ladder + `sourceHint` handles it.
- Case law: **CanLII API is metadata/citator only, not full text**, and CanLII's
  terms restrict bulk scraping — so decisions are **discovery-only**: read on
  canlii.org / court site, cite by neutral citation, pass the URL as `sourceHint`.

## Compliance limits
OPC (federal privacy — PIPEDA; provincial equivalents in AB/BC/QC); client data
stays client-side. **CanLII full text is site-only** per terms — do not bulk-harvest.

## Method notes
- **Bijural + bilingual**: establish province first; Québec = civil law (CcQ),
  distinct method and limitation. Federal matters may run in either language.
- Division of powers: confirm federal vs provincial competence.
- Draft in the required language; McGill Guide citation discipline.

## Community skills to consult
`mohammadfarooqi/canlii-mcp` (9 tools, respects CanLII rate limits)
(interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
Provincial Limitations Acts govern — commonly a **2-yr basic** limitation from
discoverability (e.g. Ontario Limitations Act 2002, s 4) + a 15-yr ultimate;
**Québec** prescription is **3 yrs** for personal actions (art. 2925 CcQ). Federal
causes have their own.
