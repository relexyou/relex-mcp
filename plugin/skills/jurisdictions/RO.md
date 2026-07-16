# RO — Romania jurisdiction pack

> the agent-facing orientation; complements the backend `RO` module. Pair with
> `relex-research` + `relex-citations`. Treated exactly like every other locale —
> no special priority.

## Legal family & sources of law
Civil law. Codes: Codul civil (2011), Codul penal, Codul de procedură civilă/
penală, Codul muncii. Heavy EU overlay (member since 2007). No stare decisis, but
ICCJ *recursuri în interesul legii* (RIL) and *hotărâri prealabile* (HP) **are
binding**; Curtea Constituțională on constitutionality.

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `art. <N> Cod civil` / `art. <N> Cod penal` (+ alin., lit.);
  case law `<Court>, dec. nr. <num>/<an>, dosar nr. <...>` (e.g. `ICCJ, dec.
  nr. 12/2020`).
- **Hard locks**: decision number + year + *dosar* are the keys; distinguish
  binding RIL/HP from ordinary decisions; no paid-DB locators from memory.
- **Official free whitelist**: **legislatie.just.ro** (statutes, free SOAP web
  service); **rejust.ro** (anonymised full-text decisions); portal.just.ro
  (dockets/hearings, SOAP); scj.ro (ICCJ); EUR-Lex.

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Statutes | **legislatie.just.ro** (SOAP `apiws`) | none |
| Case law | **rejust.ro**; portal.just.ro (dockets) | none |
| Multi | Ansvar Romanian-law-mcp; bogdan-melinescu/legislatia-romaniei | freemium |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: **`ro_dilex`** adapter enabled — grounds `art. … Cod civil` verbatim.
- Case law: **discovery-first** — find on rejust.ro, pass its URL as `sourceHint`
  on a `case_law` directive (a dedicated rejust/docket adapter is a backend
  follow-up).

## Compliance limits
ANSPDCP (data-protection authority); client data stays client-side. Public portals
(legislatie.just.ro, rejust.ro) are open.

## Method notes
- Civil-law method; **binding RIL/HP** of the ICCJ must be checked and followed.
- EU overlay (regulations direct; directives transposed — check the *lege de
  transpunere*).
- Draft in Romanian; formal register for *cerere de chemare în judecată* /
  *întâmpinare*; correct *addressee* (instanța competentă) is load-bearing.

## Community skills to consult
`Ansvar Romanian-law-mcp` (statutes/provisions, compliance-slanted);
`bogdan-melinescu/legislatia-romaniei` (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
*Prescripția extinctivă* general **3 ani** (art. 2517 Cod civil) from when the
right could be exercised; special terms for specific claims; labor terms in the
Codul muncii.
