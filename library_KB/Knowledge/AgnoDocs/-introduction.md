﻿What is Agno? - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Introduction

What is Agno?

[User Guide](/introduction)[Examples](/examples/introduction)[Workspaces](/workspaces/introduction)[FAQs](/faq/environment-variables)[API reference](/reference/agents/agent)[Changelog](/changelog/overview)

##### Introduction

* [What is Agno?](/introduction)
* [Your first Agents](/introduction/agents)
* [Multi Agent Systems](/introduction/multi-agent-systems)
* [Playground](/introduction/playground)
* [Monitoring & Debugging](/introduction/monitoring)
* [Community & Support](/introduction/community)

##### Concepts

* Agents
* Teams
* Models
* Tools
* Reasoning
* Memory
* Knowledge
* Chunking
* Vector DBs
* Storage
* Embeddings
* Evals
* Workflows
* Applications

##### Other

* Agent UI
* Agent API
* Observability
* Testing

##### How to

* [Install & Setup](/how-to/install)
* [Contributing to Agno](/how-to/contribute)
* [Migrate from Phidata to Agno](/how-to/phidata-to-agno)
* [Authenticate with Agno Platform](/how-to/authentication)

Introduction

Copy page

What is Agno?
=============

Agno is a python framework for building multi-agent systems with shared memory, knowledge and reasoning.

Engineers and researchers use Agno to build:

* **Level 1:** Agents with tools and instructions ([example](/introduction/agents#level-1%3A-agents-with-tools-and-instructions)).
* **Level 2:** Agents with knowledge and storage ([example](/introduction/agents#level-2%3A-agents-with-knowledge-and-storage)).
* **Level 3:** Agents with memory and reasoning ([example](/introduction/agents#level-3%3A-agents-with-memory-and-reasoning)).
* **Level 4:** Agent Teams that can reason and collaborate ([example](/introduction/multi-agent-systems#level-4%3A-agent-teams-that-can-reason-and-collaborate)).
* **Level 5:** Agentic Workflows with state and determinism ([example](/introduction/multi-agent-systems#level-5%3A-agentic-workflows-with-state-and-determinism)).

**Example:** Level 1 Reasoning Agent that uses the YFinance API to answer questions:

Reasoning Finance Agent

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions="Use tables to display data.",
    markdown=True,
)

```

Watch the reasoning finance agent in action

[](https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/reasoning_finance_agent.mp4)

[​](#getting-started) Getting Started
=====================================

If you’re new to Agno, learn how to build your [first Agent](/introduction/agents), chat with it on the [playground](/introduction/playground) and [monitor](/introduction/monitoring) it on [app.agno.com](https://app.agno.com).

[Your first Agents
-----------------

Learn how to build Agents with Agno](/introduction/agents)[Agent Playground
----------------

Chat with your Agents using a beautiful Agent UI](introduction/playground)[Agent Monitoring
----------------

Monitor your Agents on [agno.com](https://app.agno.com)](introduction/monitoring)

After that, dive deeper into the [concepts below](/introduction#dive-deeper) or explore the [examples gallery](/examples) to build real-world applications with Agno.

[​](#why-agno%3F) Why Agno?
===========================

Agno will help you build best-in-class, highly-performant agentic systems, saving you hours of research and boilerplate. Here are some key features that set Agno apart:

* **Model Agnostic**: Agno provides a unified interface to 23+ model providers, no lock-in.
* **Highly performant**: Agents instantiate in **~3μs** and use **~6.5Kib** memory on average.
* **Reasoning is a first class citizen**: Reasoning improves reliability and is a must-have for complex autonomous agents. Agno supports 3 approaches to reasoning: Reasoning Models, `ReasoningTools` or our custom `chain-of-thought` approach.
* **Natively Multi-Modal**: Agno Agents are natively multi-modal, they accept text, image, audio and video as input and generate text, image, audio and video as output.
* **Advanced Multi-Agent Architecture**: Agno provides an industry leading multi-agent architecture (**Agent Teams**) with reasoning, memory, and shared context.
* **Built-in Agentic Search**: Agents can search for information at runtime using 20+ vector databases. Agno provides state-of-the-art Agentic RAG, **fully async and highly performant.**
* **Built-in Memory & Session Storage**: Agents come with built-in `Storage` & `Memory` drivers that give your Agents long-term memory and session storage.
* **Structured Outputs**: Agno Agents can return fully-typed responses using model provided structured outputs or `json_mode`.
* **Pre-built FastAPI Routes**: After building your Agents, serve them using pre-built FastAPI routes. 0 to production in minutes.
* **Monitoring**: Monitor agent sessions and performance in real-time on [agno.com](https://app.agno.com).

[​](#dive-deeper) Dive deeper
=============================

Agno is a battle-tested framework with a state of the art reasoning and multi-agent architecture, read the following guides to learn more:

[Agents
------

Learn how to build lightning fast Agents.](/agents)[Teams
-----

Build autonomous multi-agent teams.](/teams)[Models
------

Use any model, any provider, no lock-in.](/models)[Tools
-----

100s of tools to extend your Agents.](/tools)[Reasoning
---------

Make Agents “think” and “analyze”.](/reasoning)[Knowledge
---------

Give Agents domain-specific knowledge.](/knowledge)[Vector Databases
----------------

Store and search your knowledge base.](/vectordb)[Storage
-------

Persist Agent session and state in a database.](/storage)[Memory
------

Remember user details and session summaries.](/agents/memory)[Embeddings
----------

Generate embeddings for your knowledge base.](/embedder)[Workflows
---------

Deterministic, stateful, multi-agent workflows.](/workflows)[Evals
-----

Evaluate, monitor and improve your Agents.](/evals)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/introduction.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /introduction)

[Your first Agents](/introduction/agents)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Getting Started](#getting-started)
* [Why Agno?](#why-agno%3F)
* [Dive deeper](#dive-deeper)

Assistant

Responses are generated using AI and may contain mistakes.
