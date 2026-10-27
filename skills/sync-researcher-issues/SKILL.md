---
name: sync-researcher-issues
description: Add researchers to goldener-research, named directly or from GitHub issues labeled "researcher". Verifies identity and affiliation (mainly from Google Scholar/DBLP), adds their abstract-confirmed relevant papers to BIBLIOGRAPHY.md and an entry to RESEARCHERS.md, recursively checks co-authors (3+ relevant papers, up to 2 levels, within overridable budgets), opens a PR and closes fully handled issues. Use when the user asks to sync researcher issues, or "add <Name> to goldener research", "add <Name> as a researcher".
---

# Import researchers

Accept names and optional identity/topic hints directly or from open
`researcher` issues of `goldener-data/goldener-research`.

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


## Researcher workflow

1. Build `{name, hint, source_issue}` inputs. Confirm the intended identity
   using publications/stable IDs, not a name or fuzzy score alone. Resolve
   genuine namesake ambiguity with the user when evidence cannot settle it.
2. Prefer verified personal/institutional publication pages or bibliographic
   profiles, with Scholar/DBLP/index fallbacks. Record publication coverage
   and affiliation source/date; do not infer a current employer from an old
   paper. An unavailable source is unresolved, not proof of irrelevance.
3. Title-screen publications and abstract-confirm plausible papers. Directly
   nominated researchers qualify with at least one relevant paper. Discovered
   co-authors require three; preserve that intentional distinction.
4. Select topics per confirmed paper. Match existing entries with identity
   evidence, including legacy headings with affiliation suffixes after ` - `
   or `: `. Append genuinely new papers to the matching entry; create an
   entry only when that identity is absent in the destination. Do not merge
   namesakes or overwrite affiliation without verified updated evidence.
5. Add matching bibliography placements for every confirmed paper, using
   canonical IDs/verified versions rather than exact URL equality alone.
   Fetch full author lists even for already-covered papers. Entries may be
   duplicates for the nominee while still supplying valid expansion seeds.
6. Run co-author expansion from all confirmed papers as level-0 seeds, within
   the shared budgets and depth cap. Report each discovered researcher's
   qualifying count, seed, topics and depth. Preserve evidence for probes
   that fall below threshold without committing their probe-only papers.
7. Distinguish fully screened no-relevance outcomes from incomplete/blocked
   research before applying the shared per-issue completion rules.
