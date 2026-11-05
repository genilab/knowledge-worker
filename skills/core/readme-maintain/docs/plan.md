# Skill Plan — readme-maintain

## Summary

Maintain a verified user-facing README for a full-publication development project.

## Description

`readme-maintain` is an internal skill used when a project's `AGENTS.md`
declares a public-release or private-repository README profile, or on a direct
README request. It uses verified project evidence and reports missing facts
rather than inventing content.

For Knowledge-worker, the public-release README presents a centered title,
catch phrase, approved infographic, and badges before explaining the
graph-based multi-agent knowledge-base model and public actions.

## Script Requirements

- It must read repository visibility and README profile from `AGENTS.md`
  before deciding whether README maintenance applies.
- It must select the public-release or private-repository template without
  exposing information beyond the declared visibility.
- It must generate public-release README content in this order: centered title
  and catch phrase, centered infographic, centered badges, What is,
  differentiators, Getting started, and Public actions.
- It must express differentiators as concise bullet points and include one
  concise illustrative sequence of verified public actions in Getting started.
- It must use only approved `assets/images/` infographics and verified badges,
  clone-to-destination commands, differentiators, and public actions.
- It must maintain the root README automatically for a development project with full publication and leave an application project unchanged unless directly requested.
- It must collect composition evidence from the project plan, architecture, release and roadmap records, module requirements, QA, existing README, and available assets, preserving accurate existing content.
- It must use verified project purpose, public actions, QA-backed claims, and
  real approved assets to compose the public-release layout.
- It must use direct, affirmative explanatory prose that states what the
  project does and how it works rather than contrasting it with a negative
  alternative.
- It must structure the `What is` explanation in two paragraphs: practical
  value, intended audience, outcome, and concrete material first; the
  structure that maintains and organizes that outcome, extensible skills, and
  organizational value second.
- It must introduce clone-to-destination setup with continuous, complete
  sentences, provide a stable latest-release ZIP alternative when published,
  then direct the user to the Public actions section.
- It must express the release-package alternative as a complete download,
  extract, and open command sequence that extracts directly into the chosen
  destination folder.
- It must avoid a next-steps heading and descriptions of public actions that
  are not yet implemented.
- It must ask the embedded audience, setup, public-capability, visual-asset,
  and support/contribution/license questions when the maintained records do
  not supply a required user-facing fact.
- It must create or refresh the README when a full-publication development project is created or receives a direct request, and it must never infer that an application is safe to publish.
- It must report unavailable required facts or assets instead of fabricating content.

## Delegation to Code

- No code is delegated because README maintenance depends on project-specific evidence, audience, and editorial judgment.
- Delegate a repeated deterministic fact-extraction or structure-check function to code only when it emerges and add executable test units with it.

## Code Requirements

N/A
