---
name: sync-lab-issues
description: Screen a lab or research group (named, linked, or from GitHub issues labeled "lab") for papers relevant to goldener-research. Resolves the lab website and publication list, confirms relevance from abstracts, tracks authors reaching 3+ relevant papers as researchers (checking their wider record and co-authors up to 2 levels, within overridable budgets), reports coverage, opens a PR updating BIBLIOGRAPHY.md/RESEARCHERS.md and closes fully handled issues. Use when the user asks to sync lab issues, or "add <lab> to goldener research", "look at <lab website>".
---

# Import a lab's research

Accept a lab/group name, website, or both directly or from open `lab` issues
of `goldener-data/goldener-research`.

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


## Lab workflow

1. Resolve the target from its official site and record its type: lab, group,
   department, or person. Verify who owns the site. If a broad department
   page was supplied for a specifically named PI/group, locate that group's
   own output first. A PI publication-profile fallback is allowed, but label
   the substituted target and explain that it is not the lab's full output.
2. Inventory publication sources, pages and available years. Default to a
   declared last-eight-calendar-year window including the current year when
   a large list requires scoping; honor an explicit user date range instead.
   Record the actual window, omissions, list pagination and screening counts.
   Do not present a partial window as the lab's complete history. Requests
   for all output remain incomplete until all requested years are processed.
3. Title-screen the output and abstract-confirm plausible papers. Record
   complete author lists/identity evidence. Add confirmed lab-sourced papers
   to justified bibliography topics regardless of researcher qualification.
4. Tally each author's distinct relevant lab-sourced and existing repo papers
   across all topics. Three qualify them for researcher entries. For authors
   with one or two, inspect their broader publication record within the
   shared author/abstract/request budgets. Count confirmed wider-record
   papers with the seed/existing works, avoiding duplicates.
5. When the total reaches three, add the researcher and confirmed broader-
   record papers in matching topics. Below threshold, retain evidence in the
   run record but do not add wider-record probe papers or a researcher entry.
6. Only newly added papers found through those broader-record checks become
   level-0 seeds for further co-author expansion. The lab's own output
   authors were tallied directly and are not separately re-seeded. Apply
   shared identity, queue, depth and budget rules.
7. Report target substitution, covered years/sources and deferred work. If
   requested lab coverage is partial, keep source issues open. Zero relevant
   papers after complete screening differs from unavailable publication lists.
