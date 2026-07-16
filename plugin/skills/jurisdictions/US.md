# US — United States jurisdiction pack

> the agent-facing orientation; **complements** the backend's agent-facing `US`
> module (which owns the full citation tables, forums, regulators, tones). Pair
> with `relex-research` + `relex-citations`.

## Legal family & sources of law
Common law; **federal law layered over 50 states + DC + territories**. State law
governs most private-law disputes (contract, tort, property, family); federal law
governs federal causes of action, diversity cases, federal regulation, and
constitutional questions. **Local ordinances** (municipal/county) govern zoning,
short-term rentals, noise, licensing. When the state is unclear, infer the most
likely from facts (harm location, residence, contract performance) and **flag the
state-confirmation gap** in the ontology — don't guess silently.

## Citation — schema + hard locks + official whitelist
- **Schema**: Bluebook. Federal statutes `<title> U.S.C. § <section>`; regs
  `<title> C.F.R. § <section>`; SCOTUS `<v>, <vol> U.S. <page> (<yr>)`; Circuit
  `F.3d … (<circuit> <yr>)`; state by reporter (`52 Cal.4th 541, 555`). Full
  tables live in the backend module — the reason directive applies them.
- **Hard locks**: **pinpoint pages are required** in every controlling-case cite;
  `passim`/`et seq.` forbidden. **Mark controlling vs persuasive** authority (a
  9th-Cir. holding does not control the 2nd Cir.). No Westlaw/Lexis pin cites or
  headnote paraphrases from memory — cite the reporter/official text.
- **Official free whitelist**: CourtListener / free.law (opinions, dockets);
  GovInfo (`api.govinfo.gov` — USC, CFR, Fed. Reg.); eCFR (`ecfr.gov`);
  uscode.house.gov; Congress.gov; state legislature sites; the court's own
  slip-opinion site.

## Discovery channels (you find authority here)
| Layer | Channel | Key |
|---|---|---|
| Case law + dockets | **CourtListener official MCP** (mcp.courtlistener.com) — opinions, PACER/RECAP, citation verify, semantic search | free acct |
| Federal statutes/regs | GovInfo API, eCFR API, uscode.house.gov | GovInfo needs a free key |
| State statutes | OpenStates API (50-state aggregator); individual legislature sites | OpenStates key |
| **Local ordinances** | **`GET /research/locus`** (backend LOCUS search, below) | via Relex |
| Entities | SEC **EDGAR** (full-text + submissions APIs); state SoS registers | EDGAR open (UA header) |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- **US case law → CourtListener** is **enabled** (token provisioned) — issue
  `POST /research/scrape {jurisdiction:"US", code:"<court>", article:"<cite/URL>",
  authorityType:"case_law", sourceHint:"<courtlistener URL>"}`.
- **Federal statutes/CFR**: add GovInfo/eCFR as `sourceHint` on a `statute`
  directive; the generic fetch ladder handles the official HTML/XML.
- **State statutes**: US-IL (ILGA), US-TX (texas.public.law), US-NY (OpenLeg,
  key-gated) have adapters; other states are discovery-first with a `sourceHint`.
- **Local ordinances**: **LOCUS** — `GET /research/locus?state=CA&city=…&query=…`
  returns coverage (`matched`/`covered_no_match`/`not_in_locus` — never invent an
  ordinance); then `?locusId=…` fetches the section's verbatim public-domain text
  for a grounded cite. (LOCUS analytical layer = CC-BY-NC, user-side only —
  `relex-research`.)

## Compliance limits
- CourtListener/RECAP: free-tier rate caps (5/min, 50/hr, 125/day) — targeted
  directives only, never bulk. PACER pages cost $0.10 (waived ≤ $30/qtr).
- EDGAR: send a descriptive `User-Agent`; respect fair-use rate limits.
- Court opinions are public domain; **headnotes/keynotes (West) are copyrighted**
  — cite the opinion text, not the vendor's editorial matter.

## Method notes
- **Claim construction**: elements per the controlling jurisdiction's law; a real
  citation for the wrong proposition is still false (`relex-citations` topic-match).
- **Erie / choice of law** in diversity: substantive state law + federal
  procedure — surface the assumption.
- **Controlling vs persuasive** is load-bearing: label every authority.
- **FRE 408** gates settlement/demand content; **privilege** conservative by
  default (attorney work product, common-interest).

## Community skills to consult
Anthropic `the agent-for-legal` (litigation-legal for demands/claim-charts/dockets;
ip-legal; privacy-legal) for generic US drafting playbooks; `master-the agent-for-legal`
for verification/privilege governance (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
Statutes of limitations are **state-specific and claim-specific** (e.g. personal
injury 1–6 yrs; written contract 3–6 yrs; fraud from discovery). Federal claims
have their own (e.g. § 1983 borrows the state PI period; securities 10b-5 = 2yr
discovery / 5yr repose). Court deadlines come only from the docket/order.
