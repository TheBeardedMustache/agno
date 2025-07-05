Session Storage - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Session Storage

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

  + [Overview](/agents/introduction)
  + [Running your Agent](/agents/run)
  + [Metrics](/agents/metrics)
  + [Sessions](/agents/sessions)
  + [Agent State](/agents/state)
  + [Memory](/agents/memory)
  + [Tools](/agents/tools)
  + [Structured Output](/agents/structured-output)
  + [Multimodal Agents](/agents/multimodal)
  + [User Control Flows](/agents/user-control-flow)
  + [Prompts](/agents/prompts)
  + [Knowledge](/agents/knowledge)
  + [Session Storage](/agents/storage)
  + [Agent Context](/agents/context)
  + [Agent Teams [Deprecated]](/agents/teams)
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

Agents

Copy page

Session Storage
===============

Use **Session Storage** to persist Agent sessions and state to a database or file.

**Why do we need Session Storage?**

Agents are ephemeral and the built-in memory only lasts for the current execution cycle.

In production environments, we serve (or trigger) Agents via an API and need to continue the same session across multiple requests. Storage persists the session history and state in a database and allows us to pick up where we left off.

Storage also let’s us inspect and evaluate Agent sessions, extract few-shot examples and build internal monitoring tools. It lets us **look at the data** which helps us build better Agents.

Adding storage to an Agent, Team or Workflow is as simple as providing a `Storage` driver and Agno handles the rest. You can use Sqlite, Postgres, Mongo or any other database you want.

Here’s a simple example that demostrates persistence across execution cycles:

storage.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    add_history_to_messages=True,
    num_history_runs=3,
)
agent.print_response("What was my last question?")
agent.print_response("What is the capital of France?")
agent.print_response("What was my last question?")
pprint(agent.get_messages_for_session())

```

The first time you run this, the answer to “What was my last question?” will not be available. But run it again and the Agent will able to answer properly. Because we have fixed the session id, the Agent will continue from the same session every time you run the script.

[​](#benefits-of-storage) Benefits of Storage
---------------------------------------------

Storage has typically been an under-discussed part of Agent Engineering — but we see it as the unsung hero of production agentic applications.

In production, you need storage to:

* Continue sessions: retrieve sessions history and pick up where you left off.
* Get list of sessions: To continue a previous session, you need to maintain a list of sessions available for that agent.
* Save state between runs: save the Agent’s state to a database or file so you can inspect it later.

But there is so much more:

* Storage saves our Agent’s session data for inspection and evaluations.
* Storage helps us extract few-shot examples, which can be used to improve the Agent.
* Storage enables us to build internal monitoring tools and dashboards.

Storage is such a critical part of your Agentic infrastructure that it should never be offloaded to a third party. You should almost always use your own storage layer for your Agents.

[​](#example%3A-use-postgres-for-storage) Example: Use Postgres for storage
---------------------------------------------------------------------------

1

Run Postgres

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **Postgres** on port **5532** using:

Copy

Ask AI

```
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agno/pgvector:16

```

2

Create an Agent with Storage

Create a file `agent_with_storage.py` with the following contents

Copy

Ask AI

```
import typer
from typing import Optional, List
from agno.agent import Agent
from agno.storage.postgres import PostgresStorage
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
storage = PostgresStorage(table_name="pdf_agent", db_url=db_url)

def pdf_agent(new: bool = False, user: str = "user"):
    session_id: Optional[str] = None

    if not new:
        existing_sessions: List[str] = storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        session_id=session_id,
        user_id=user,
        knowledge=knowledge_base,
        storage=storage,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
        # We can also automatically add the chat history to the messages sent to the model
        # But giving the model the chat history is not always useful, so we give it a tool instead
        # to only use when needed.
        # add_history_to_messages=True,
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
    )
    if session_id is None:
        session_id = agent.session_id
        print(f"Started Session: {session_id}\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    # Runs the agent as a cli app
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    # Load the knowledge base: Comment after first run
    knowledge_base.load(upsert=True)

    typer.run(pdf_agent)

```

3

Run the agent

Install libraries

Mac

Windows

Copy

Ask AI

```
pip install -U agno openai pgvector pypdf "psycopg[binary]" sqlalchemy

```

Run the agent

Copy

Ask AI

```
python agent_with_storage.py

```

Now the agent continues across sessions. Ask a question:

Copy

Ask AI

```
How do I make pad thai?

```

Then message `bye` to exit, start the app again and ask:

Copy

Ask AI

```
What was my last message?

```

4

Start a new run

Run the `agent_with_storage.py` file with the `--new` flag to start a new run.

Copy

Ask AI

```
python agent_with_storage.py --new

```

[​](#schema-upgrades) Schema Upgrades
-------------------------------------

When using `AgentStorage`, the SQL-based storage classes have fixed schemas. As new Agno features are released, the schemas might need to be updated.

Upgrades can either be done manually or automatically.

### [​](#automatic-upgrades) Automatic Upgrades

Automatic upgrades are done when the `auto_upgrade_schema` parameter is set to `True` in the storage class constructor.
You only need to set this once for an agent run and the schema would be upgraded.

Copy

Ask AI

```
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
storage = PostgresStorage(table_name="agent_sessions", db_url=db_url, auto_upgrade_schema=True)

```

### [​](#manual-upgrades) Manual Upgrades

Manual schema upgrades can be done by calling the `upgrade_schema` method on the storage class.

Copy

Ask AI

```
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
storage = PostgresStorage(table_name="agent_sessions", db_url=db_url)
storage.upgrade_schema()

```

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `storage` | `Optional[AgentStorage]` | `None` | Storage mechanism for the agent. |

[​](#developer-resources) Developer Resources
---------------------------------------------

* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/storage)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/storage.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/storage)

[Knowledge](/agents/knowledge)[Agent Context](/agents/context)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Benefits of Storage](#benefits-of-storage)
* [Example: Use Postgres for storage](#example%3A-use-postgres-for-storage)
* [Schema Upgrades](#schema-upgrades)
* [Automatic Upgrades](#automatic-upgrades)
* [Manual Upgrades](#manual-upgrades)
* [Params](#params)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
