---
name: relex-citations
description: Use whenever legal authority is cited, quoted, or relied on in Relex work — drafts, memos, ontology issues, research notes, any jurisdiction. Teaches the three-tier epistemic labeling (secured / verify / never-use), the hard citation locks, and the minimum-data citation schema that keep hallucinated law out of legal work.
---

# Citation Discipline: No Blind Citations

Community legal packs audited themselves and found ~30% of their own memorized
docket numbers were wrong. The cure is mechanical, not aspirational: label every
assertion's epistemic tier, obey the hard locks, and ground filing-grade
citations in cached verbatim text (`relex-research`).

## The three tiers — label everything you assert

1. **Secured** — quotable and filing-grade. Only: text in the Relex verbatim
   cache, the user's own documents, or an official source you (or the harness)
   fetched live this session. Cite normally.
2. **Plausible — verify** — you believe it from context or memory but it is not
   secured. Flag inline: `[verify: <what to check, where>]`. A draft may carry
   `[verify]` flags only in internal work product — never in anything that
   leaves the practice; those become directives (`POST /research/scrape`).
3. **Never-use** — from model memory alone: docket/file numbers, ECLI strings,
   commentary margin numbers, page/paragraph pinpoints, verbatim quotes,
   database identifiers. Do not write them even with a flag. Encode the
   authority as an **anchor** instead (below) and acquire.

Marking tier 2/3 honestly is clean lawyerly practice, not weakness.

## Hard locks (non-negotiable)

- **No proprietary blind cites.** Never emit a paywalled-database locator
  (BeckRS, juris, Westlaw/Lexis pin cites, La Ley…) from memory. Only if the
  user supplied it or a licensed live source verified it. When one appears in
  inherited text and can't be verified: extract court/date/docket, find the
  free official source, else replace with
  `[proprietary locator removed — verify against a free official source]`.
- **No citation without minimum data.** A case citation needs court +
  decision form + date + docket/neutral cite + a **free, checkable source**;
  a pinpoint (para/margin number) only from the source itself.
- **Renamed/moved-source traps.** Sources get renamed, re-numbered,
  consolidated (commentaries change editors; statutes get recodified;
  transpositions land). If your knowledge of a source predates today, verify
  the source still exists under that name/number before citing it.
- **Statute first.** Norm text → then verified case law → literature only when
  supplied or live-verified.
- **Topic-match check.** Before attaching any authority: does the *holding*
  actually support the proposition? A real citation for the wrong proposition
  is still a false citation.
- **No deadline from memory** — hard lock; the canonical deadline rule lives in
  `relex-matter` (compute from the secured norm text, flag for human
  verification).

## Anchors, not memorized citations

When you know the *line* of jurisprudence but not a secured citation, write an
anchor and acquire:

```
<topic/line> — <probable court/bench> — verify in <official free source>
e.g. "constructive dismissal; hearing duty — Federal Labour Court, 2nd senate
      (line since mid-2000s) — verify in the court's official database"
```

Anchors are honest retrieval keys — they contain nothing to hallucinate.

## Citation schema by family (one line each; jurisdiction packs carry detail)

- **US** — Bluebook; controlling vs persuasive marked; pin cites from source.
- **UK** — OSCOLA + neutral citation.
- **DE** — court, form, date, Aktenzeichen (+ECLI), source, Rn. from source;
  no stare-decisis framing (§ 31 BVerfGG aside).
- **CH** — BGE/ATF volume-part-page + consideration (E.); unpublished by docket.
- **FR** — court, chamber, date, n° pourvoi; ECLI where available.
- **IT/ES/RO** — court, section, number/year (+ECLI where issued).
- **EU** — case number + name + ECLI.
- **CA** — McGill Guide + neutral citation. **JP** — court, date, reporter.
- **AU** — AGLC4 + neutral citation.

## In Relex specifically

- The server verifier rejects drafts citing law without cached verbatim text —
  when it does, that's a **grounding gap**: issue the directive, re-reason.
- Record grounded issues in the ontology with their ground ("settled — grounded
  by cached § 823 BGB text"), so the understanding carries its evidence.
- Official-source whitelist per jurisdiction lives in `../jurisdictions/*.md`;
  finding aids (aggregators) are for *finding*, the citation names the official
  source.
