# DE — Germany jurisdiction pack

> the agent-facing orientation; **complements** the backend's agent-facing `DE`
> module (full citation tables + court branches). Pair with `relex-research` +
> `relex-citations`. For German method depth, lean on the community pack (below).

## Legal family & sources of law
Civil law (Romano-Germanic). Federal civil/criminal/commercial codes (BGB, HGB,
StGB, ZPO, StPO, InsO, ArbGG…); Länder handle police, public order, some
competencies. **EU law penetrates heavily** — Regulations apply directly,
Directives are transposed into the codes, CJEU jurisprudence binds. **No
stare-decisis** (except § 31 BVerfGG) — never argue precedent-binding.

## Citation — schema + hard locks + official whitelist
- **Schema**: `§ <N> Abs. <X> Satz <Y> <Code>` (e.g. `§ 437 Abs. 1 Satz 2 BGB`);
  case law `BGH, Urt. v. DD.MM.YYYY – <Az.>, <Fundstelle> Rn. <N>` (+ **ECLI**).
  Full tables in the backend module.
- **Hard locks** (the German pack's discipline — adopt it):
  - **No blind citations.** Court + Entscheidungsform + date + **Aktenzeichen** +
    a verifiable free source + **Randnummer taken from the source** are mandatory.
  - **No proprietary-DB locators from memory** (BeckRS, juris as a universal cite)
    and **no commentary margin numbers** (Grüneberg/MüKo/BeckOK/Staudinger) unless
    the user supplied them or a licensed live source verified them. If inherited
    text carries a BeckRS locator you can't verify: extract court/date/Az, find the
    free original, else drop it with a `[verify against a free official source]`.
  - **Renamed-source trap**: the former *Palandt* commentary is *Grüneberg* since
    the 81st ed. (2022) — verify a source still exists under the name you recall.
  - **No stare-decisis framing** (US-contamination guard).
- **Official free whitelist**: **NeuRIS** (rechtsinformationen.bund.de — new
  official portal, statutes + case law), gesetze-im-internet.de (statutes),
  rechtsprechung-im-internet.de + the court sites
  (bundesverfassungsgericht.de, bundesgerichtshof.de, bundesarbeitsgericht.de),
  EUR-Lex/CURIA for EU. openJur/dejure are **finding aids**, not the official
  source a cite names.

## Discovery channels (you find authority here)
| Layer | Channel | Key |
|---|---|---|
| Statutes + case law | **NeuRIS** (rechtsinformationen.bund.de) official open API; community NeuRIS MCP | none |
| Statutes | gesetze-im-internet.de (per-law XML) | none |
| Case law | rechtsprechung-im-internet.de; openJur; court sites | none |
| EU overlay | EUR-Lex + CELLAR SPARQL; CURIA via ECLI | none |
| Entities | handelsregister.de (search, no official API); offeneregister.de (stale dump) | — |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: **`de_gii`** (gesetze-im-internet) adapter is enabled — a `statute`
  directive with `code`/`article` grounds `§ … <Code>` text; add NeuRIS as a
  `sourceHint` for laws/decisions gii doesn't cover.
- Case law: **discovery-first** (no dedicated DE case-law adapter) — find the
  decision on NeuRIS/court site, pass its URL as `sourceHint` on an
  `authorityType:"case_law"` directive; the generic ladder fetches the verbatim.

## Compliance limits
- § 203 StGB (professional-secret) + § 43e BRAO + Art. 28 GDPR: client-linked
  data needs an AVV (data-processing agreement) with any processor — Relex keeps
  PII sealed or redacted client-side, so the model never sees it (that's the point). Do
  not route client PII to any third-party research tool.
- beA (the mandatory electronic lawyer mailbox, § 130d ZPO) has **no public API** —
  don't promise beA automation.

## Method notes
- **Anspruchsaufbau** (claim-construction) order: contract → c.i.c. → GoA →
  dinglich → Delikt → Bereicherung. **Gutachtenstil** for analysis, **Urteilsstil**
  for decisions.
- **Fully-written-out** deliverables (no skeletons); decimal outline `1 / 1.1`.
- EU-transposition currency: for recent directives, verify the German
  implementing act is in force before relying on it (currency gap → re-scrape).

## Community skills to consult
**`Klotzkette/the agent-fuer-deutsches-recht`** — the substantial German pack; use
its foundation refs (`zitierweise` = citation discipline, `methodik-buergerliches-
recht`, `leitentscheidungen-anker`) for method + citation depth, and its
practice-area routing (interop framing → `references/interop.md`). Its own audit
found ~30% of its memorized
docket numbers were wrong — so **treat its case-law anchors as retrieval keys, and
ground every cite through the harness**, never from its (or your) memory.

## Limitation / deadline heuristics (orientation only — never finalize from memory)
Regelverjährung 3 years (§ 195 BGB) from year-end of accrual+knowledge (§ 199);
long-stops 10/30 yrs. Kündigungsschutzklage **3-week** filing (§§ 4, 7 KSchG) — a
classic trap. AGG claims: 2-month written assertion (§ 15 IV AGG).
