﻿Memory - Agno

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

Memory

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

Memory
======

Memory gives an Agent the ability to recall relavant information. Memory is a part of the Agent’s context that helps it provide the best, most personalized response.

If the user tells the Agent they like to ski, then future responses can reference this information to provide a more personalized experience.

In Agno, Memory covers chat history, user preferences and any supplemental information about the task at hand. **Agno supports 3 types of memory out of the box:**

1. **Session Storage (chat history and session state):** Session storage saves an Agent’s sessions in a database and enables Agents to have multi-turn conversations. Session storage also holds the session state, which is persisted across runs because it is saved to the database after each run. Session storage is a form of short-term memory **called “Storage” in Agno**.
2. **User Memories (user preferences):** The Agent can store insights and facts about the user that it learns through conversation. This helps the agents personalize its response to the user it is interacting with. Think of this as adding “ChatGPT like memory” to your agent. **This is called “Memory” in Agno**.
3. **Session Summaries (chat summary):** The Agent can store a condensed representations of the session, useful when chat histories gets too long. **This is called “Summary” in Agno**.

It is relatively easy to use your own memory implementation using `Agent.context`.

To become an expert in Agentic Memory, you need to learn about:

1. [Default, built-in Memory](/agents/memory#default-memory)
2. [Session Storage](/agents/memory#session-storage)
3. [User Memories](/agents/memory#user-memories)
4. [Session Summaries](/agents/memory#session-summaries)

[​](#show-me-the-code%3A-memory-%26-storage-in-action) Show me the code: Memory & Storage in Action
---------------------------------------------------------------------------------------------------

Here’s a simple but complete example of using Memory and Storage in an Agent.

memory\_demo.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint

# UserId for the memories
user_id = "ava"
# Database file for memory and storage
db_file = "tmp/agent.db"

# Initialize memory.v2
memory = Memory(
    # Use any model for creating memories
    model=OpenAIChat(id="gpt-4.1"),
    db=SqliteMemoryDb(table_name="user_memories", db_file=db_file),
)
# Initialize storage
storage = SqliteStorage(table_name="agent_sessions", db_file=db_file)

# Initialize Agent
memory_agent = Agent(
    model=OpenAIChat(id="gpt-4.1"),
    # Store memories in a database
    memory=memory,
    # Give the Agent the ability to update memories
    enable_agentic_memory=True,
    # OR - Run the MemoryManager after each response
    enable_user_memories=True,
    # Store the chat history in the database
    storage=storage,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

memory.clear()
memory_agent.print_response(
    "My name is Ava and I like to ski.",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Ava:")
pprint(memory.get_user_memories(user_id=user_id))

memory_agent.print_response(
    "I live in san francisco, where should i move within a 4 hour drive?",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Ava:")
pprint(memory.get_user_memories(user_id=user_id))

```

### [​](#notes) Notes

* `enable_agentic_memory=True` gives the Agent a tool to manage memories of the user, this tool passes the task to the `MemoryManager` class. You may also set `enable_user_memories=True` which always runs the `MemoryManager` after each user message.
* `add_history_to_messages=True` adds the chat history to the messages sent to the Model, the `num_history_runs` determines how many runs to add.
* `read_chat_history=True` adds a tool to the Agent that allows it to read chat history, as it may be larger than what’s included in the `num_history_runs`.

[​](#default-memory) Default Memory
-----------------------------------

Every Agent comes with built-in memory which keeps track of the messages in the session i.e. the chat history.

You can access these messages using `agent.get_messages_for_session()`.

We can give the Agent access to the chat history in the following ways:

* We can set `add_history_to_messages=True` and `num_history_runs=5` to add the messages from the last 5 runs automatically to every message sent to the agent.
* We can set `read_chat_history=True` to provide a `get_chat_history()` tool to your agent allowing it to read any message in the entire chat history.
* **We recommend setting all 3: `add_history_to_messages=True`, `num_history_runs=3` and `read_chat_history=True` for the best experience.**
* We can also set `read_tool_call_history=True` to provide a `get_tool_call_history()` tool to your agent allowing it to read tool calls in reverse chronological order.

The default memory is not persisted across execution cycles. So after the script finishes running, or the request is over, the built-in default memory is lost.

You can persist this memory in a database by adding a `storage` driver to the Agent.

1

Built-in memory example

agent\_memory.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from rich.pretty import pprint

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    # Set add_history_to_messages=true to add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # Number of historical responses to add to the messages.
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

# -*- Create a run
agent.print_response("Share a 2 sentence horror story", stream=True)
# -*- Print the messages in the memory
pprint([m.model_dump(include={"role", "content"}) for m in agent.get_messages_for_session()])

# -*- Ask a follow up question that continues the conversation
agent.print_response("What was my first message?", stream=True)
# -*- Print the messages in the memory
pprint([m.model_dump(include={"role", "content"}) for m in agent.get_messages_for_session()])

```

2

Run the example

Install libraries

Copy

Ask AI

```
pip install google-genai agno

```

Export your key

Copy

Ask AI

```
export GOOGLE_API_KEY=xxx

```

Run the example

Copy

Ask AI

```
python agent_memory.py

```

[​](#session-storage) Session Storage
-------------------------------------

The built-in memory is only available during the current execution cycle. Once the script ends, or the request is over, the built-in memory is lost.

**Storage** help us save Agent sessions and state to a database or file.

Adding storage to an Agent is as simple as providing a `storage` driver and Agno handles the rest. You can use Sqlite, Postgres, Mongo or any other database you want.

Here’s a simple example that demonstrates persistence across execution cycles:

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

Read more in the [storage](/agents/storage) section.

[​](#user-memories) User Memories
---------------------------------

Along with storing session history and state, Agents can also create user memories based on the conversation history.

To enable user memories, give your Agent a `Memory` object and set `enable_agentic_memory=True`.

Enabling agentic memory will also add all existing user memories to the agent’s system prompt.

1

User memory example

user\_memory.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini

memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
memory = Memory(db=memory_db)

john_doe_id = "john_doe@example.com"

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memory,
    enable_agentic_memory=True,
)

# The agent can add new memories to the user's memory
agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    stream=True,
    user_id=john_doe_id,
)

agent.print_response("What are my hobbies?", stream=True, user_id=john_doe_id)

# The agent can also remove all memories from the user's memory
agent.print_response(
    "Remove all existing memories of me. Completely clear the DB.",
    stream=True,
    user_id=john_doe_id,
)

agent.print_response(
    "My name is John Doe and I like to paint.", stream=True, user_id=john_doe_id
)

# The agent can remove specific memories from the user's memory
agent.print_response("Remove any memory of my name.", stream=True, user_id=john_doe_id)


```

2

Run the example

Install libraries

Copy

Ask AI

```
pip install google-genai agno

```

Export your key

Copy

Ask AI

```
export GOOGLE_API_KEY=xxx

```

Run the example

Copy

Ask AI

```
python user_memory.py

```

User memories are stored in the `Memory` object and persisted in the `SqliteMemoryDb` to be used across multiple users and multiple sessions.

[​](#session-summaries) Session Summaries
-----------------------------------------

To enable session summaries, set `enable_session_summaries=True` on the `Agent`.

1

Session summary example

session\_summary.py

Copy

Ask AI

```
    from agno.agent import Agent
    from agno.memory.v2.db.sqlite import SqliteMemoryDb
    from agno.memory.v2.memory import Memory
    from agno.models.google.gemini import Gemini

    memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
    memory = Memory(db=memory_db)

    user_id = "jon_hamm@example.com"
    session_id = "1001"

    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        memory=memory,
        enable_session_summaries=True,
    )

    agent.print_response(
        "What can you tell me about quantum computing?",
        stream=True,
        user_id=user_id,
        session_id=session_id,
    )

    agent.print_response(
        "I would also like to know about LLMs?",
        stream=True,
        user_id=user_id,
        session_id=session_id
    )

    session_summary = memory.get_session_summary(
        user_id=user_id, session_id=session_id
    )
    print(f"Session summary: {session_summary.summary}\n")

```

2

Run the example

Install libraries

Copy

Ask AI

```
pip install google-genai agno

```

Export your key

Copy

Ask AI

```
export GOOGLE_API_KEY=xxx

```

Run the example

Copy

Ask AI

```
python session_summary.py

```

[​](#attributes) Attributes
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `memory` | `Memory` | `Memory()` | Agent’s memory object used for storing and retrieving information. |
| `add_history_to_messages` | `bool` | `False` | If true, adds the chat history to the messages sent to the Model. Also known as `add_chat_history_to_messages`. |
| `num_history_runs` | `int` | `3` | Number of historical responses to add to the messages. |
| `enable_user_memories` | `bool` | `False` | If true, create and store personalized memories for the user. |
| `enable_session_summaries` | `bool` | `False` | If true, create and store session summaries. |
| `enable_agentic_memory` | `bool` | `False` | If true, enables the agent to manage the user’s memory. |

[​](#developer-resources) Developer Resources
---------------------------------------------

* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/memory)
* View [Examples](/examples/concepts/memory)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/memory.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/memory)

[Agent State](/agents/state)[Tools](/agents/tools)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Show me the code: Memory & Storage in Action](#show-me-the-code%3A-memory-%26-storage-in-action)
* [Notes](#notes)
* [Default Memory](#default-memory)
* [Session Storage](#session-storage)
* [User Memories](#user-memories)
* [Session Summaries](#session-summaries)
* [Attributes](#attributes)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
