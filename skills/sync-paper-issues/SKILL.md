---
name: sync-paper-issues
description: Add papers to the goldener-research bibliography, named directly (title, link, or both) or listed in GitHub issues labeled "paper" (one issue can hold several). Confirms relevance from abstracts, places each paper in the matching topic BIBLIOGRAPHY.md, recursively checks co-authors (3+ relevant papers to become a researcher, up to 2 levels, within overridable budgets), opens a PR and closes fully handled issues. Use when the user asks to sync paper issues, or "add <title or arXiv/DOI/OpenReview link> to the bibliography / to goldener research".
---

# Import papers

Accept one or more titles, links, or both, directly or in open `paper` issues
of `goldener-data/goldener-research`. One issue can contain several papers.

## Execution contract

Read [the bundled synchronization workflow](references/sync-workflow.md) before
starting. It defines capabilities, isolated worktrees, output modes, evidence,
identity, placement, formats, budgets, saved progress, delivery, and recovery.
Use those rules together with the task-specific decisions below. No particular
agent, connector, shell session model, or interaction tool is required.

Default to full issue sync for a request to sync this category of issues and
PR delivery for directly named research; explicit user limits take precedence.
Do not process unrelated issues. A local preparation request requires no remote
write access. Preserve completed work when delivery is unavailable.


## Paper workflow

1. Build a worklist with optional title/link (at least one), hint, and source
   issue ID or null. Direct inputs do not require listing unrelated issues.
   Parse body and title together: Markdown links are candidates only when
   context or bibliographic metadata identifies a paper. Project/code links
   are context, not papers by default.
2. Resolve candidates through paper metadata. Link-only and title-only inputs
   are both valid. If a given link fails, search by known title/identifier;
   never substitute a different work. Keep ambiguous/unidentified items
   unresolved and continue independent inputs.
3. Fetch abstracts and full author lists. Confirm relevance using the shared
   criteria. Record canonical IDs, venue/year, evidence, and destination topics.
4. Deduplicate identities against the whole repository and current batch,
   then compare placements per destination. Existing placement elsewhere is
   not a reason to omit a separately justified topic placement. Report an
   already-covered input even when it yields no new entry.
5. Write confirmed entries using the canonical bibliography format. Every
   confirmed seed, new or duplicate, starts co-author expansion at level 0.
   Apply shared three-paper qualification, identity checks, depth/breadth
   budgets, and live deduplication. Keep below-threshold probe findings in
   state but do not commit probe-only papers.
6. Aggregate all papers from each source issue before delivery/closure.
   An inaccessible paper is unresolved, not irrelevant. Report optional
   expansion deferrals separately; incomplete requested research stays open.
