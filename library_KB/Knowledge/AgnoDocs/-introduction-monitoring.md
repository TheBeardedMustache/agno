Monitoring & Debugging - Agno

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

Monitoring & Debugging

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

Monitoring & Debugging
======================

Monitor your Agents, Teams and Workflows in real-time.

[​](#monitoring) Monitoring
===========================

You can track your Agent in real-time on [app.agno.com](https://app.agno.com).

[​](#authenticate) Authenticate
-------------------------------

Authenticate with [agno.com](https://app.agno.com) to start monitoring your sessions.
Check out [Authentication guide](how-to/authentication) for instructions on how to Authenticate with Agno.

[​](#enable-monitoring) Enable Monitoring
-----------------------------------------

Enable monitoring for a single agent or globally for all agents by setting `AGNO_MONITOR=true`.

### [​](#for-a-specific-agent) For a Specific Agent

Copy

Ask AI

```
agent = Agent(markdown=True, monitoring=True)

```

### [​](#globally-for-all-agents) Globally for all Agents

Copy

Ask AI

```
export AGNO_MONITOR=true

```

[​](#monitor-your-agents) Monitor Your Agents
---------------------------------------------

Run your agent and view the sessions on the [sessions page](https://app.agno.com/sessions).

1

Create a file with sample code

monitoring.py

Copy

Ask AI

```
from agno.agent import Agent

agent = Agent(markdown=True, monitoring=True)
agent.print_response("Share a 2 sentence horror story")

```

2

Run your Agent

Copy

Ask AI

```
python monitoring.py

```

3

View your sessions

View your sessions at [app.agno.com/sessions](https://app.agno.com/sessions)

Facing issues? Check out our [troubleshooting guide](/faq/cli-auth)

[​](#debug-logs) Debug Logs
---------------------------

Want to see the system prompt, user messages and tool calls?

Agno includes a built-in debugger that will print debug logs in the terminal. Set `debug_mode=True` on any agent or set `AGNO_DEBUG=true` in your environment.

debug\_logs.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
    debug_mode=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)

```

Run the agent to view debug logs in the terminal:

Copy

Ask AI

```
python debug_logs.py

```

[](https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/debug_logs.mp4)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/introduction/monitoring.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /introduction/monitoring)

[Playground](/introduction/playground)[Community & Support](/introduction/community)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Monitoring](#monitoring)
* [Authenticate](#authenticate)
* [Enable Monitoring](#enable-monitoring)
* [For a Specific Agent](#for-a-specific-agent)
* [Globally for all Agents](#globally-for-all-agents)
* [Monitor Your Agents](#monitor-your-agents)
* [Debug Logs](#debug-logs)

Assistant

Responses are generated using AI and may contain mistakes.
