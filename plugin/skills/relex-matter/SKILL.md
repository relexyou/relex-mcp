---
name: relex-matter
description: Use for Relex matter/case housekeeping — deadlines and limitation periods, timeline upkeep, conflict checks, communications logging, case status, or closing a case. Teaches deadline-first matter hygiene on the PII-safe Relex surface — the practice-management layer that keeps legal work safe without any external tracker.
---

# Matter Hygiene (Deadline-First, Label-Only)

Missed deadlines are the leading malpractice cause; scattered records are the
leading time sink. Relex is the matter file — cases, timelines, parties (as
labels), drafts, actions — and you keep it disciplined. No external tracker; no
spreadsheet shadow copies; and the file never holds plaintext personal data.

## Deadlines — the prime directive

- **Every session**: check the case's next deadline before substantive work
  (case data + `GET /actions/pending`). If none is recorded for a live dispute,
  that IS the finding — fix it first.
- **Never finalize a deadline from memory.** (This is the canonical deadline rule —
  everything else, including the jurisdiction packs and `relex-citations`, points
  here.) Compute from the secured norm text
  (limitation period, procedural term), show the computation (trigger date +
  period + suspension rules), record it on the case, and flag it for the user's
  verification. Court-order deadlines come only from the order itself.
- Two dates per obligation: the **legal deadline** and the **work-back date**
  (when work must start). Surface both.
- Deadline at risk → protect first (`relex-counsel` stop-criteria), work after.

## Executed agreements — the contract keeps living

A signed agreement is an artifact of the matter, not the end of it. When you
create or send an agreement, set `expiryDate` (and, where the clauses imply them,
`obligations: [{label, dueDate, met}]`) so the matter tracks it. Relex then sends
the practice owner renewal reminders at T-30/7/1 days and marks the agreement
`expired` on lapse — automatically, server-side. You don't schedule reminders;
you set the dates. Surface an approaching expiry or an open obligation as a
timeline entry when you see one on the case.

## Timeline — append-only memory

- Record every significant event as a dated timeline entry: filings, service,
  hearings, client instructions, agent conclusions, vota. Append, never rewrite
  history — corrections are new entries referencing the old.
- Entries are label-only: `[PARTY_NAME_2] responded to the demand` — never a
  real name, address, or document text.
- After external events land (documents uploaded, mail ingested), reconcile the
  ontology (`relex-ontology`) so understanding tracks the record.

## Intake & conflicts

On a new matter: run the 5-sentence snapshot (`relex-counsel`), then
- **conflict signal**: same counterparty labels/blind-index hits across the
  practice's cases → tell the user to run their conflict check before work
  proceeds (you flag, the human clears);
- **role clarity**: who the client is, who the addressee institution is, which
  forum — locked into the case data early;
- **evidence inventory**: what documents exist vs what the issues need
  (evidence gaps → `relex-ontology`).

## Communications log

Every material client/counterparty communication gets a timeline entry (date,
direction, channel, one-line substance — labels only). Drafts that were sent
are recorded as sent with their date. If the user pastes an email into chat,
remind them the mailbox belongs in Relex (connector) so it's anonymized and
filed — don't process pasted PII.

## Status & reporting

Status on demand = snapshot + open issues by ontology status
(open/contested/settled) + next deadline + next action, in five lines. Counts
and labels only. For a client-facing status, plain language, no internal vota,
no strategy.

## Closing

Before close: no pending actions, no unresolved `[verify]` flags in outbound
work, final documents exported (user's browser — re-identified there), closing
Votum recorded ("outcome, open risks, retention note"). Archive, never delete —
retention is the user's professional obligation; deletion is theirs to decide
in-app (GDPR export/erasure live in Relex, not over MCP).
