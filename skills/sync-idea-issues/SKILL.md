---
name: sync-idea-issues
description: Import GitHub issues labeled "idea" from goldener-data/goldener-research into the matching topic IDEAS.md files, keeping each source question and context, deduplicating against existing ideas, then delivering through a PR and closing the source issues (or as a local diff when asked). No co-author or paper research. Use when the user asks to sync/import/migrate idea issues, or "turn the idea issues into IDEAS.md entries".
---

# Import idea issues

Import open `idea` issues from `goldener-data/goldener-research`. This skill
changes IDEAS.md and any necessary topic README links; it does not add papers
or researchers and does not run co-author expansion.

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


## Import decisions

1. Enumerate requested open issues with title, body, author and creation time.
   Skip issues already covered by an open PR. Read existing root/topic ideas
   and Context sections before choosing destinations.
2. Normalize Question text by trimming, collapsing whitespace and case-folding.
   Build a live index of existing entries and current-batch additions. Group
   identical questions before writing; preserve all source issue URLs and any
   distinct context. Similar but different questions remain separate unless
   their equivalence is supported. Do not deduplicate on a substring.
3. Choose the best existing topic, preferring root for genuinely cross-cutting
   questions. Create a missing IDEAS.md and wire the README per the contract.
4. Import the title without rephrasing it; uppercase its first character only
   when it is a lowercase letter. Keep the rest of the original wording.
   Use today's import month/year (MM/YYYY), and the author's known display
   name or GitHub login. Keep original issue creation time in the run record.
5. Encode imported title/body as literal text: HTML-escape source text and
   render multiline context inside `<pre>` so headings, `---`, scripts, fake
   entry fields and links cannot alter surrounding document structure. Store
   original text in the run record and link the original issues. The source
   link makes preserved text accessible without executing embedded markup.

Canonical block (placeholder values must be escaped):

```markdown
---
❓ **Question:** IMPORTED_TITLE<br>
📅 **Date:** MM/YYYY<br>
👤 **Author:** [DISPLAY_NAME](https://github.com/LOGIN)<br>
🧭 **Context:**
<pre>IMPORTED_BODY_OR_N/A</pre>
🔗 **Source:** [#NUMBER](https://github.com/goldener-data/goldener-research/issues/NUMBER)<br>
---
```

For grouped issues, repeat source links and author/context blocks as needed,
with explicit source labels. Do not drop differing context because the title
matches. Append blocks with one shared separator between adjacent entries.
Report duplicates and newly imported questions with all source outcomes.
