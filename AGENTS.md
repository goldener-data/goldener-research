# Repository working conventions

- Create new Git worktrees under this repository's `.worktree/` directory,
  using a descriptive subdirectory name, unless the user explicitly requests
  another location. This applies to future actions as well as the current task.

## Repository shape

- This repository is a research/documentation workspace for Goldener, not an application codebase.
- The top-level theme folders (for example, `augmentation/`, `batching/`, `data_selection/`, `drift/`, `frameworks/`, `labeling/`, `losses/`, `model_design/`, `out_of_distribution/`, `training_strategy/`) organize the content by AI-lifecycle topic.
- Most theme folders follow the same pattern: `README.md` for the topic overview, plus `BIBLIOGRAPHY.md`, `IDEAS.md`, and `RESEARCHERS.md`.
- The root `README.md` explains the project goal and links the theme folders.

## Content conventions

- Keep additions within the relevant theme folder instead of inventing new top-level structures.
- Match the existing Markdown style in each file:
  - `IDEAS.md` entries use repeated blocks with `Question`, `Date`, `Author`, and `Context`.
  - `BIBLIOGRAPHY.md` groups papers under short topical headings and adds a brief annotation after each link.
  - `RESEARCHERS.md` lists names followed by affiliation and a supporting paper link.
- Prefer concise, research-oriented prose over implementation details.
- Preserve the existing topic taxonomy and terminology used by the current docs.

## Adding papers and researchers

- Do not duplicate a paper within a destination file. A paper may appear in multiple justified topic files; leave an existing destination entry in place or propose a better location rather than adding another copy.
  For a discovered researcher, a verified existing paper counts once toward the
  three-publication qualification threshold; direct researcher nominations may
  qualify with one relevant paper.
- Add researchers affiliated with a public institution or research institute;
  do not add researchers who work only for for-profit companies. Verify current
  affiliations, including an eligible affiliation for jointly affiliated authors.
- Focus on papers using embeddings to improve the AI lifecycle. Also allow
  reference papers that offer competing approaches to embeddings in their field
  when they are explicitly listed in an issue or have sufficiently high citation
  counts. Assess citation counts in context and record the evidence; do not invent
  a universal numerical cutoff.

## Validation and commands

- No repository-local build, test, or lint commands are defined in the repo.
- For changes here, validation is usually Markdown review and link/path consistency.
