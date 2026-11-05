---
name: readme-maintain
description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
metadata:
  source: core
  action: Maintain external GitHub documentation when required.
---

# Maintain Readme

## Scope

This is an internal skill. Use it when the project's `AGENTS.md` declares a
README profile or the user directly requests a README. It selects either the
public-release or private-repository template and maintains only the root
document. Its inputs are the declared visibility/profile, approved project
identity, verified implementation evidence, existing README, and available
assets. It produces an accurate README or a clear gap report. It has no user
activation command; a calling workflow invokes it.
Primary agent role: publication-agent.

## Workflow

1. Read the Repository publication declaration in `AGENTS.md`. Escalate a
   missing visibility or README profile rather than inferring one.
2. For `public-release`, use the
   [public-release template](docs/public_release_template.md) and
   [public README process](docs/public_readme_process.md); for `private`,
   use the [private-repository template](docs/private_repo_template.md).
3. Use approved identity, verified capabilities, validation evidence, real
   assets, and accurate existing README material. Do not expose private
   operating details or planned capabilities as present facts.
   Write public explanatory copy in direct, affirmative language: state what
   the project does and how it works instead of framing its value through a
   contrast with an undesirable alternative.
   Structure the `What is` explanation in two paragraphs: first, state the
   practical value, intended audience, and outcome; second, explain the
   project structure that maintains and organizes that outcome.
4. For a public release, retain the template's ordered centered title and
   catch phrase, centered infographic, centered badge group, `What is`,
   differentiators, Getting started, and Public actions sections.
   For Knowledge-worker, use the verified knowledge-base purpose and public
   actions. Embed an infographic only when an approved file exists in
   `assets/images/` and the `asset-agent` has handed it off for public
   documentation. Express each differentiator as a concise bullet point.
   Introduce Getting started with continuous, complete sentences, explain that
   cloning creates the user's independent destination folder, and provide the
   stable latest-release ZIP alternative as an explicit download, extract, and
   open command sequence when it is published. Continue from
   setup with one concise Illustrative example that demonstrates a common
   verified public-action sequence and explains each action's purpose, then
   continue to the complete action list. Do not add a separate next-steps
   subsection. Describe only public actions that exist; future capabilities belong in the
   extensibility explanation until their skills are added.
5. Ask for clarification about any material gap before creating the affected
   section. Do not infer public claims, access rules, or release details.
6. Produce the updated README and a concise gap report for any unanswered
   question or unavailable required asset.

## Constraints

- Do not invent setup steps, capabilities, integrations, support channels, banners, or release claims.
- Preserve accurate existing material and use only real assets. If the infographic is required but unavailable, report the gap rather than adding a broken reference.
- Non-goals include using README as internal navigation, exposing private
 information, and changing implementation, plans, or release evidence.
