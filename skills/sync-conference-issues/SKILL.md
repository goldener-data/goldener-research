---
name: sync-conference-issues
description: Screen a conference edition (named with an optional year, or from GitHub issues labeled "conference") for papers relevant to goldener-research, across orals, posters, keynotes and co-located workshops. Resolves the edition (latest published program by default, asks only when a requested year is ambiguous), tracks authors with 3+ relevant papers as researchers (co-authors up to 2 levels, within overridable budgets), reports coverage, opens a PR and closes fully handled issues. Use when the user asks to sync conference issues, or "add NeurIPS 2024 to goldener research", "look at ICML".
---

# Import conference research

Accept conference names/URLs and optional years directly or in open
`conference` issues of `goldener-data/goldener-research`. A source issue may
name multiple conferences or editions.

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


## Edition and program workflow

1. Resolve the official conference/program archive. If no year was given,
   choose the latest edition with a published accessible accepted-paper
   program, and record the choice. Do not assume the current year's program
   is published. An explicitly requested year must match exactly.
2. If that exact year has no published program, ask about up to two nearest
   published editions: bracket it when editions exist on both sides,
   otherwise use the two nearest on the available side. Include a stop-this-
   item choice and keep it unresolved until answered. If none exists, report
   the unresolved input. Never silently replace an explicit year.
3. Build a coverage manifest for main-track orals, posters, invited talks
   accompanied by a paper/extended abstract, and every co-located workshop.
   Record each format/workshop's source, expected/observed counts where
   available, pagination, and status: complete, absent-by-design, blocked,
   partially screened, or deferred. Workshop discovery itself can be partial;
   do not claim complete edition coverage without evidence.
4. Prefer downloadable PDF/CSV/JSON/ICS accepted-paper lists; parse them
   locally. A schedule that only lists session times is not a paper list.
   Fall back to official program pages/proceedings indexes when needed.
   Follow workshop-specific official sources and record unavailable lists.
5. Merge formats and deduplicate by canonical paper identity before screening.
   Record versions and withdrawn status when exposed by the source. Do not
   count the same work twice across main/workshop/poster appearances, and
   do not describe a withdrawn work as currently accepted.
6. Title-screen using the repository/Goldener criteria, then abstract-confirm
   plausible works. Issue text identifies the venue/year; it must not change
   the shared relevance criteria. Record full author lists. Add confirmed
   papers and tally qualifying researchers across the edition's screened
   output plus verified existing repo papers.
7. For authors with one or two relevant papers, check broader records as in
   the lab workflow: qualify at three, add qualifying wider-record papers,
   and retain below-threshold evidence without committing probe-only papers.
   Newly added wider-record papers are level-0 expansion seeds; edition
   output authors have already been tallied directly.
8. Separate enumeration, abstract screening and author-expansion progress in
   the run record. The shared budgets can require resumable edition batches;
   list unprocessed program entries and workshops explicitly. Incomplete
   requested edition coverage keeps source issues open.
9. Aggregate outcomes once per source issue. If any edition/item is in
   progress or unresolved/deferred, do not close the issue; do not comment
   on in-progress issues. Already-covered complete editions count as completed,
   while fully screened editions with no relevant papers are not planned.
