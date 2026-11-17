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
Never guess mentions or trending tags.
Each thread post should make sense in context and fit with its `1/n` marker.
Optional resources/disclosure can go in the last post; count them too.

## Visual and engaging style

Apply this when the user asks for emojis, or for a prettier, more engaging,
more visual or scannable draft. Otherwise keep ordinary text.

- Start each block with one emoji that labels its role, not decorates it:
  📊/🧠 hook, 📄 paper, ✍️ authors, 💡 idea, 🔍 key result, 🧩 data-centric
  role, ⚠️ caveat, 💬 user's take, 🔗 paper link, 📚 resources, 🤖 disclosure.
  Use at most one emoji per line, never mid-sentence or inside hashtags.
- Put the hook on its own line. Requests for a prettier or more visual draft
  allow Unicode bold for that single hook line only (see below). Report it and
  offer a plain version.
- Split a method with two or three steps into short 🔹 bullet lines, and
  keep each block to one or two sentences so it reads well on a phone.
- Make it engaging with a concrete contrast or number from the review, not
  with hype. Avoid 🚀/🔥/🤯 and superlatives for modest or uncertain results.
- Give the caveat its own ⚠️ block, as visible as the headline result.
- Emojis do not replace words: every line must still make sense to a screen
  reader. Count emojis in the length check, with the platform's rules.

Unicode mathematical alphabets are not semantic bold and can impair reading,
search and accessibility. Use them only when requested. Mark short spans with
`**...**`, then run the shared helper on a safely written draft file.
`<tools-dir>` is the checkout's `skills/tools` directory:

```bash
python3 -I <tools-dir>/unicode_bold.py draft.txt > final.txt
```

The helper transforms ASCII letters/digits; accented letters remain unchanged.
Inspect unmatched markers, preserve links/handles, and count the final output
using the target's rules. Do not claim that every emoji is one character or
that `wc -m` implements a platform's counter.

Default disclosure: “AI-generated summary of the paper.” Translate as needed.
Default social resource line:
`More data-centric AI resources: https://github.com/goldener-data/goldener-research`
These defaults are editable by the user; the draft remains unpublished.
