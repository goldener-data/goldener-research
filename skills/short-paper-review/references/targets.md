# Draft formatting targets

This reference gives layout defaults, not a promise about current platform
limits. Verify official current limits/counting rules when exact fit matters;
record the source/date or identify the count as approximate. A platform/account
or Mastodon instance can change its limits. Do not infer grapheme counts,
weighted counts or rendered emoji length from raw code points alone.

| Target | Layout default | Styling default |
|---|---|---|
| Plain text | Short paragraphs, paper link on its own line | Ordinary text; no hashtags |
| LinkedIn | Short paragraphs and a concrete opening line | Ordinary text; optional 3–5 relevant hashtags |
| X | One concise post or numbered thread | Ordinary text; optional 1–2 hashtags |
| Bluesky | Concise post or numbered thread | Ordinary text; optional 0–2 hashtags |
| Mastodon | Post/thread fitting the chosen instance | Ordinary text; optional CamelCase hashtags |
| Threads | Concise post or numbered thread | Ordinary text; optional topical tag |
| Newsletter/blog | Short title and paragraphs | Markdown where supported |
| Slack/Teams | Short paragraphs or 3–5 useful bullets | Native link/emphasis syntax where supported |

For unknown targets use the user's specification or verify official guidance.
Use emoji sparingly when requested. Never guess mentions or trending tags.
Each thread post should make sense in context and fit with its `1/n` marker.
Optional resources/disclosure can go in the last post; count them too.

Unicode mathematical alphabets are not semantic bold and can impair reading,
search and accessibility. Use them only when requested. Mark short spans with
`**...**`, then run the bundled helper on a safely written draft file:

```bash
python3 -I <skill-dir>/scripts/unicode_bold.py draft.txt > final.txt
```

The helper transforms ASCII letters/digits; accented letters remain unchanged.
Inspect unmatched markers, preserve links/handles, and count the final output
using the target's rules. Do not claim that every emoji is one character or
that `wc -m` implements a platform's counter.

Default disclosure: “AI-generated summary of the paper.” Translate as needed.
Default social resource line:
`More data-centric AI resources: https://github.com/goldener-data/goldener-research`
These defaults are editable by the user; the draft remains unpublished.
