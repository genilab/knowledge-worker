# Graph-Based Multi-Agent Project Model

Every project created or maintained through Knowledge-worker is a graph-based
multi-agent system. Its `AGENTS.md` is the authoritative orchestration
contract: it declares how public actions enter the project, how an
orchestrator routes work, which agent roles own the available capabilities,
and when the work returns, transfers, or escalates.

## Model

- **Orchestrator** is the control node. It interprets a confirmed public
  action, selects the next agent role and bounded skill, evaluates returned
  evidence, and either completes the action, routes a handoff, or asks for a
  decision. It does not silently make external or destructive changes.
- **Agent role** is a named graph node with a bounded responsibility. A role
  may be performed through local skills today and supplied by an independently
  running external agent later. Declaring a role never claims that a persistent
  external agent is already deployed.
- **Skill** is a bounded capability owned by one primary agent role. Its
  `SKILL.md` states the role in its Scope, its plan specifies the required
  behavior, and its QA records verification.
- **Public action** is a user-facing entry point. It always resolves through
  the orchestrator; it does not bypass the graph directly into a skill.

The normal graph is:

```text
public action -> orchestrator -> agent role -> skill workflow -> evidence
      ^                                                        |
      +------ complete, route next handoff, or escalate -------+
```

## Required AGENTS.md Contract

Every managed project `AGENTS.md` must contain a `## Multi-agent
orchestration` section with:

1. a statement that the project is graph-based and multi-agent;
2. the orchestrator's responsibility and authority boundary;
3. an Agent graph table with **Agent role**, **Responsibility**, **Skills**,
   and **Handoffs** columns;
4. a deliberation rule: action to orchestrator to role to skill to evidence;
5. escalation and approval boundaries, particularly for external writes,
   irreversible work, conflicts, or missing requirements; and
6. an explicit statement that listed roles are capability nodes, not a claim
   of continuously running external agents.

Only roles necessary to the project are required. `orchestrator` is universal;
the remaining roles are selected from the project's actual responsibilities.
Each listed skill must have exactly one primary role in its `SKILL.md` Scope.
When a project includes the standard `assets/` area, its graph also declares
an `asset-agent` responsible for asset classification, preservation, and the
handoff of approved public assets to the publication role.

## Adoption and Evolution

`project-structure-manage` applies this model when a project is created or
reconciled. `skill-create` assigns a primary agent role before a skill is
created or revised, and `skill-validate` checks that declaration. Projects can
later replace a role's local execution with an external agent without changing
their public action, evidence, or escalation contract.

For a public repository, the `asset-agent` hands an approved infographic and
factual accessibility details to the publication role. The publication role
uses `readme-maintain` to present the public README in this order: centered
title and catch phrase, centered infographic, centered badges, public
explanation, setup, and actions. When GitHub versioning is selected,
the publication role uses `github-maintain` to publish the stable
`{project-slug}_latest.zip` archive for direct extraction into a user's chosen
destination folder.
