Playground - Agno

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

Playground

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

Playground
==========

**Agno provides an intuitive interface for testing and interacting with your AI agents.**

Agno Platform - Playground

The Playground gives a robust interface to test your agentic systems with extensive features.

* **Streaming Support**: Real-time response streaming and intermediate states back to the user.
* **Session History**: Visualize conversation history right in the playground.
* **User Memory**: Visualize user details and preferences across conversations.
* **Configuration**: Comprehensive configuration interface allowing you to see agent parameters, model settings, tool configurations.
* **Reasoning Support**: Built-in support for detailed reasoning traces displayed in the playground interface.
* **Human in Loop Support**: Enable manual intervention in agent workflows with specialized human oversight and approval.
* **Multimodal Support**: Support for processing and generating text, images, audio, and other media types.
* **Multi-Agent Systems**: Support for multi-agent teams and workflows.

[​](#interact-with-your-agents-locally) Interact with your agents Locally
-------------------------------------------------------------------------

1

Create a file with sample code

playground.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    # Store the agent sessions in a sqlite database
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
    # Adds the current date and time to the instructions
    add_datetime_to_instructions=True,
    # Adds the history of the conversation to the messages
    add_history_to_messages=True,
    # Number of history responses to add to the messages
    num_history_responses=5,
    # Adds markdown formatting to the messages
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

playground_app = Playground(agents=[web_agent, finance_agent])
app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("playground:app", reload=True)

```

Remember to export your `OPENAI_API_KEY` before running the playground application.

Make sure the `serve()` points to the file that contains your `Playground` app.

2

Authenticate with Agno

Authenticate with [agno.com](https://app.agno.com) so your local application can let agno know which port you are running the playground on.

Check out [Authentication guide](how-to/authentication) for instructions on how to Authenticate with Agno.

No data is sent to agno.com, all agent data is stored locally in your sqlite database.

3

Run the Playground Server

Install dependencies and run your playground server:

Copy

Ask AI

```
pip install openai duckduckgo-search yfinance sqlalchemy 'fastapi[standard]' agno

python playground.py

```

4

View the Playground

* Open the link provided or navigate to `http://app.agno.com/playground` (login required).
* Add/Select the `localhost:7777` endpoint and start chatting with your agents!

[](https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/playground.mp4)

Looking for a self-hosted alternative?

Looking for a self-hosted alternative? Check out our [Open Source Agent UI](https://github.com/agno-agi/agent-ui) - A modern Agent interface built with Next.js and TypeScript that works exactly like the Agent Playground.

### [​](#get-started-with-agent-ui) Get Started with Agent UI

Copy

Ask AI

```
# Create a new Agent UI project
npx create-agent-ui@latest

# Or clone and run manually
git clone https://github.com/agno-agi/agent-ui.git
cd agent-ui && pnpm install && pnpm dev

```

The UI will connect to `localhost:7777` by default, matching the Playground setup above. Visit [GitHub](https://github.com/agno-agi/agent-ui) for more details.

Facing connection issues? Check out our [troubleshooting guide](/faq/playground-connection)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/introduction/playground.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /introduction/playground)

[Multi Agent Systems](/introduction/multi-agent-systems)[Monitoring & Debugging](/introduction/monitoring)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Interact with your agents Locally](#interact-with-your-agents-locally)

Assistant

Responses are generated using AI and may contain mistakes.
