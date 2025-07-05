What are Agents? - Agno

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

What are Agents?

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

What are Agents?
================

**Agents are AI programs that operate autonomously.**

Traditional software follows a pre-programmed sequence of steps. Agents dynamically determine their course of action using a machine learning **model**, its core components are:

* **Model:** controls the flow of execution. It decides whether to reason, act or respond.
* **Tools:** enable an Agent to take actions and interact with external systems.
* **Instructions:** are how we program the Agent, teaching it how to use tools and respond.

Agents also have **memory**, **knowledge**, **storage** and the ability to **reason**:

* **Reasoning:** enables Agents to “think” before responding and “analyze” the results of their actions (i.e. tool calls), this improves reliability and quality of responses.
* **Knowledge:** is domain-specific information that the Agent can **search at runtime** to make better decisions and provide accurate responses (RAG). Knowledge is stored in a vector database and this **search at runtime** pattern is known as Agentic RAG/Agentic Search.
* **Storage:** is used by Agents to save session history and state in a database. Model APIs are stateless and storage enables us to continue conversations from where they left off. This makes Agents stateful, enabling multi-turn, long-term conversations.
* **Memory:** gives Agents the ability to store and recall information from previous interactions, allowing them to learn user preferences and personalize their responses.

Let’s build a few Agents to see how they work.

[​](#level-1%3A-agents-with-tools-and-instructions) Level 1: Agents with tools and instructions
-----------------------------------------------------------------------------------------------

The simplest Agent has a model, a tool and instructions. Let’s build an Agent that can fetch data using the `yfinance` library, along with instructions to display the results in a table.

level\_1\_agent.py

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
)
agent.print_response("What is the stock price of Apple?", stream=True)

```

Create a virtual environment, install dependencies, export your API key and run the Agent.

1

Setup your virtual environment

Mac

Windows

Copy

Ask AI

```
uv venv --python 3.12
source .venv/bin/activate

```

2

Install dependencies

Mac

Windows

Copy

Ask AI

```
uv pip install -U agno anthropic yfinance

```

3

Export your Anthropic key

Mac

Windows

Copy

Ask AI

```
export ANTHROPIC_API_KEY=sk-***

```

4

Run the agent

Copy

Ask AI

```
python agent_with_tools.py

```

Set `debug_mode=True` or `export AGNO_DEBUG=true` to see the system prompt and user messages.

[​](#level-2%3A-agents-with-knowledge-and-storage) Level 2: Agents with knowledge and storage
---------------------------------------------------------------------------------------------

**Knowledge:** While models have a large amount of training data, we almost always need to give them domain-specific information to make better decisions and provide accurate responses (RAG). We store this information in a vector database and let the Agent **search** it at runtime.

**Storage:** Model APIs are stateless and `Storage` drivers save chat history and state to a database. When the Agent runs, it reads the chat history and state from the database and add it to the messages list, resuming the conversation and making the Agent stateful.

In this example, we’ll use:

* `UrlKnowledge` to load Agno documentation to LanceDB, using OpenAI for embeddings.
* `SqliteStorage` to save the Agent’s session history and state in a database.

level\_2\_agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

# Load Agno documentation in a knowledge base
# You can also use `https://docs.agno.com/llms-full.txt` for the full documentation
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Agno Assist",
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response("What is Agno?", stream=True)

```

Install dependencies, export your `OPENAI_API_KEY` and run the Agent

1

Install new dependencies

Mac

Windows

Copy

Ask AI

```
uv pip install -U lancedb tantivy openai sqlalchemy

```

2

Run the agent

Copy

Ask AI

```
python level_2_agent.py

```

[​](#level-3%3A-agents-with-memory-and-reasoning) Level 3: Agents with memory and reasoning
-------------------------------------------------------------------------------------------

* **Reasoning:** enables Agents to **“think” & “analyze”**, improving reliability and quality. `ReasoningTools` is one of the best approaches to improve an Agent’s response quality.
* **Memory:** enables Agents to classify, store and recall user preferences, personalizing their responses. Memory helps the Agent build personas and learn from previous interactions.

level\_3\_agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

memory = Memory(
    # Use any model for creating and managing memories
    model=Claude(id="claude-sonnet-4-20250514"),
    # Store memories in a SQLite database
    db=SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db"),
    # We disable deletion by default, enable it if needed
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    # User ID for storing memories, `default` if not provided
    user_id="ava",
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    memory=memory,
    # Let the Agent manage its memories
    enable_agentic_memory=True,
    markdown=True,
)

if __name__ == "__main__":
    # This will create a memory that "ava's" favorite stocks are NVIDIA and TSLA
    agent.print_response(
        "My favorite stocks are NVIDIA and TSLA",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
    # This will use the memory to answer the question
    agent.print_response(
        "Can you compare my favorite stocks?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

```

Run the Agent

Copy

Ask AI

```
python level_3_agent.py

```

You can use the `Memory` and `Reasoning` separately, you don’t need to use them together.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/introduction/agents.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /introduction/agents)

[What is Agno?](/introduction)[Multi Agent Systems](/introduction/multi-agent-systems)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Level 1: Agents with tools and instructions](#level-1%3A-agents-with-tools-and-instructions)
* [Level 2: Agents with knowledge and storage](#level-2%3A-agents-with-knowledge-and-storage)
* [Level 3: Agents with memory and reasoning](#level-3%3A-agents-with-memory-and-reasoning)

Assistant

Responses are generated using AI and may contain mistakes.
