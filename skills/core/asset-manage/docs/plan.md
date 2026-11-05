# Plan

## Summary

Classify, preserve, inspect, and route approved project assets through one
bounded workflow.

## Description

`asset-manage` governs the durable `assets/` area for a managed project. It
places infographics and other images in `assets/images/`, generated reports in
`assets/reports/`, and only clearly named new asset types under `assets/`. It
preserves existing files and routes a requested public reference to
`readme-maintain` rather than publishing it itself.

## Script Requirements

- It must confirm the project root, asset request, type, intended use, and
  source or generation context before changing an asset location.
- It must use `assets/images/` for infographics and project images and
  `assets/reports/` for generated reports.
- It must require a descriptive stable filename and preserve existing assets.
- It must provide factual alt text and approved README-placement facts when a
  public infographic is handed to `readme-maintain`.
- It must report inventory and gaps without mutation when requested.
- It must escalate replacement, relocation, deletion, ambiguity, and public
  publication; it must hand an approved public reference to `readme-maintain`.
- It must not generate, edit, publish, or version assets itself.
- It must leave public explanatory copy, badges, and release-distribution
  instructions to the publication workflow.

## Delegation to Code

No code is delegated. Asset classification and publication eligibility require
project-specific review.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
