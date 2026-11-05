<h1 align="center">Knowledge-worker</h1>

<p align="center">
  <strong>Graph-based knowledge bases maintained by multi-agent work.</strong>
</p>

<p align="center">
  <img src="assets/images/knowledge-worker-overview.png" alt="A graph-based multi-agent knowledge system connects orchestrated skills with structured, durable knowledge." width="100%">
</p>


<p align="center">
  <a href="https://github.com/genilab/knowledge-worker/releases">
    <img src="https://img.shields.io/github/v/release/genilab/knowledge-worker?display_name=tag&sort=semver&style=flat-square" alt="Latest release">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="skills/core/INDEX.md">
    <img src="https://img.shields.io/badge/Core%20Skills-15-0F766E?style=flat-square&logo=probot&logoColor=white" alt="15 core skills">
  </a>
</p>

## What is Knowledge-worker?

Knowledge-worker is a graph-based knowledge base that organizes shared
information by topic. It gives research groups, office teams, and project teams
a practical way to build knowledge for any area of work, such as a literature
review, a policy, or project discovery. You can add source material, including
PDFs, record what it means, and review what the team already knows.

The multi-agent structure maintains the knowledge base by organizing notes,
links, ideas, and files into named topics and keeping their navigation current.
Teams can extend the structure with approved skills for work such as answering
questions from recorded material, preparing reports, creating workflows, and
building dashboards. It gives people and organizations a structured path toward
AI-driven knowledge management.


### What makes it different?

- **Well-structured knowledge topics.** Each topic keeps information, ideas,
  references, and source files in clear, separate records, making it easier to
  understand what is known, what is still being explored, and where it came
  from.
- **Maintained information navigation.** Local INDEX documents are kept
  current so people and agents can quickly find skills, topics, and the
  relevant working records.
- **Clear multi-agent definitions.** The project documents how an
  orchestrator, agent roles, and reusable skills work together, so multi-agent
  work has a shared structure with clear working guidance.

## Getting started

To start, clone the repository into a folder of your choice. Cloning creates a
local knowledge project for your topics and material. You can later connect it
to your own GitHub repository with `GitHub connect {repository-url}`.

```sh
git clone https://github.com/genilab/knowledge-worker.git /path/to/your-knowledge-base
cd /path/to/your-knowledge-base
```

If you prefer a release package, download the latest archive, extract it into
your chosen folder, and open that folder:

```sh
curl -L https://github.com/genilab/knowledge-worker/releases/latest/download/knowledge-worker_latest.zip
unzip knowledge-worker_latest.zip -d /path/to/your-knowledge-base
cd /path/to/your-knowledge-base
```

With the structure installed, use one of the public actions below to begin
organizing knowledge.

### Illustrative example

You want to create a small literature-review knowledge base for Smart Cities,
with topics for urban heat, sustainable mobility, and smart infrastructure:

1. `Create topic urban-heat` creates the knowledge node and its separate
   information, ideas, references, and source-material records.
2. Repeat `Create topic {topic}` for `sustainable-mobility` and
   `smart-infrastructure` to establish the related topic nodes.
3. `Learn info about urban-heat` with a PDF, URL, text, or other supplied
   material analyzes and indexes the attributable content under that topic.
4. `Show knowledge` presents the knowledge-base dashboard of available topics.
5. `Show knowledge urban-heat` presents the dashboard and stored knowledge for
   the urban-heat topic.

## Available actions

- `Show knowledge [ALL | {topic}]` presents the knowledge-base dashboard or a
  dashboard for one topic.
- `Create topic {topic}` creates a knowledge node.
- `Learn info about {topic}` with a PDF, URL, text, or other supplied material
  analyzes and indexes attributable content under that topic.
- `GitHub connect {repository-url}` connects the local project to an existing
  GitHub repository.
- `GitHub commit` previews and publishes approved local-project changes.
- `GitHub synchronize` safely synchronizes a clean local project with its
  connected GitHub repository.
- `Show info` displays the project version, configured repositories, and
  available project content.
- `Check updates` compares core actions, workflows, skills, and `AGENTS.md`
  with the local project, then reconciles approved applicable updates.
