# Copilot instructions for Goldener Open Research

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

## Validation and commands

- No repository-local build, test, or lint commands are defined in the repo.
- For changes here, validation is usually Markdown review and link/path consistency.

