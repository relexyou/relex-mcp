# JP — Japan jurisdiction pack

> the agent-facing orientation; complements the backend `JP` module. Pair with
> `relex-research` + `relex-citations`.

## Legal family & sources of law
Civil law (German/French-influenced). Codes: 民法 (Civil Code), 商法 (Commercial),
会社法 (Companies Act), 刑法 (Penal), 民事訴訟法 (Civil Procedure). No stare
decisis, but Supreme Court (最高裁) precedents are strongly followed.

## Citation — schema + hard locks + official whitelist
- **Schema**: statutes `<Law name>第<N>条` (e.g. `民法第709条`) with 項 (paragraph)
  / 号 (item). Case law `最判平成<N>年<M>月<D>日民集<vol>巻<no>号<page>頁`
  (Supreme Court judgment, official reporter 民集/刑集). de-facto standard:
  「法律文献等の出典の表示方法」.
- **Hard locks**: court + date + official reporter (民集/刑集) are the keys; no
  paid-DB (Westlaw Japan / LEX/DB / 判例秘書) locators from memory.
- **Official free whitelist**: **e-Gov 法令検索** (laws.e-gov.go.jp — statutes,
  API v2); **裁判所 courts.go.jp 裁判例検索** (selected decisions).

## Discovery channels
| Layer | Channel | Key |
|---|---|---|
| Statutes | **e-Gov Laws API v2** (laws.e-gov.go.jp/api/2) | none |
| MCP | ryoooo/e-gov-law-mcp | none |
| Case law | courts.go.jp (selected published decisions) | none |
| Entities | 法人番号 Web-API (NTA); gBizINFO REST API | free key |

## Grounding availability (harness caches verbatim)
`GET /research/sources` is the live registry — what it lists enabled can be
cached by directive; everything else is discovery-only via `sourceHint`.
- Statutes: **`jp_egov`** adapter enabled (verify it targets API v2) — grounds
  `<法>第N条` verbatim.
- Case law: **discovery-first, limited** — only selected decisions are published
  free (courts.go.jp); commercial DBs hold the rest (out of scope). Pass a
  courts.go.jp URL as `sourceHint`.

## Compliance limits
PPC (個人情報保護委員会 — APPI, data protection); client data stays client-side.
Most case law sits behind paid DBs — don't assume comprehensive free coverage.

## Method notes
- Civil-law method; requisite-facts (要件事実) analysis is central in litigation.
- Draft in Japanese; formal register for 訴状 (complaint) / 答弁書 (answer);
  vertical vs horizontal conventions per court practice.
- Reiwa/Heisei era dates in citations — convert carefully.

## Community skills to consult
`ryoooo/e-gov-law-mcp` (statutes) (interop framing → `references/interop.md`).

## Limitation / deadline heuristics (orientation only — never finalize from memory)
Civil Code (2020 reform) 消滅時効: **5 yrs** from when the creditor knew they could
exercise the right / **10 yrs** objective (民法第166条); torts 3 yrs from
knowledge / 20 yrs (民法第724条).
