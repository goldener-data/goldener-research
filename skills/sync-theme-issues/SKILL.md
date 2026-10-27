---
name: sync-theme-issues
description: Build a goldener-research bibliography for a machine-learning theme (named directly or from GitHub issues labeled "theme", e.g. AutoML, curriculum learning). Searches, ranks candidates by citation count and keeps the most cited abstract-confirmed relevant papers (20 per theme by default, overridable), checks co-authors for 3+ relevant papers (up to 2 levels), opens a PR updating BIBLIOGRAPHY.md/RESEARCHERS.md and closes fully handled issues. Use when the user asks to sync theme issues, or "add <theme> to goldener research", "find papers and researchers on <theme>".
---

# Build a theme bibliography

Accept one or more broad ML areas directly or from open `theme` issues of
`goldener-data/goldener-research`. A search theme can span several repository
topics; placement is decided per paper.

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


## Theme search

1. Build a worklist of theme, scoping hints, and source issue IDs. Combine
   equivalent requested themes without dropping source provenance. Skip
   inputs already covered by open PRs.
2. Construct 3–6 queries using the theme, common synonyms/acronyms, hints,
   and at least one survey query. Prefer a bibliographic search capable of
   citation ranking; web search and verified bibliographic pages are valid
   fallbacks. Use structured query arguments, request timeouts and bounded
   rate-limit backoff. Never execute raw query text as shell syntax.
3. Record queries, source/index, retrieval date, pagination/truncation and
   citation counts. Use one index consistently for ranking where possible;
   counts from different indexes are not interchangeable. Unknown counts
   remain unknown and are flagged, not assigned invented zero counts.
4. Merge query results by verified paper identity. Keep at most 60 candidates
   (default pool cap) in citation-ranked order, title-screen them, then
   confirm abstracts in that order until 20 relevant papers per theme (default
   seed cap) are found or the pool is exhausted. The user may change or
   remove either cap like the shared budgets. Already-present seeds count toward 20. Do not run extra queries
   just to fill the quota. Report fewer when the evidence supports fewer.
5. Describe results as the highest-cited confirmed papers within this searched
   pool, not the global top 20. Citation count is a selection convention,
   not proof of methodological quality or relevance. Recency/balanced
   selection is available only when explicitly requested, with its ranking
   rule and date range recorded.
6. Add confirmed placements and run level-0 seed co-author expansion from
   new and duplicate papers. Retain the shared author budget (30 by default) across all
   themes/levels, prioritizing frequent authors then first/last authors of
   the higher-cited seeds. The seed cap applies to theme search, not
   recursive discoveries; shared abstract/request budgets bound those too.
7. Exhausted retries or blocked abstracts/searches leave affected work
   unresolved/deferred. Only a completed search/screen with no relevant
   findings supports a not-relevant outcome. Save queues and report ranking
   uncertainty, coverage, budget use and all deferred checks.
