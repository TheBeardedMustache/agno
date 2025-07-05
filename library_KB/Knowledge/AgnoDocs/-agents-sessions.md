Sessions - Agno

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

Sessions

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

Sessions
========

When we call `Agent.run()`, it creates a stateless, singular Agent run.

But what if we want to continue this run i.e. have a multi-turn conversation? That’s where `sessions` come in. A session is collection of consecutive runs.

In practice, a session is a multi-turn conversation between a user and an Agent. Using a `session_id`, we can connect the conversation history and state across multiple runs.

Let’s outline some key concepts:

* **Session:** A session is collection of consecutive runs like a multi-turn conversation between a user and an Agent. Sessions are identified by a `session_id` and each turn is a **run**.
* **Run:** Every interaction (i.e. chat or turn) with an Agent is called a **run**. Runs are identified by a `run_id` and `Agent.run()` creates a new `run_id` when called.
* **Messages:** are the individual messages sent between the model and the Agent. Messages are the communication protocol between the Agent and model.

Let’s start with an example where a single run is created with an Agent. A `run_id` is automatically generated, as well as a `session_id` (because we didn’t provide one to continue the conversation). This run is not yet associated with a user.

Copy

Ask AI

```
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

# Run agent and return the response as a variable
agent.print_response("Tell me a 5 second short story about a robot")

```

[​](#multi-user%2C-multi-session-agents) Multi-user, multi-session Agents
-------------------------------------------------------------------------

Each user that is interacting with an Agent gets a unique set of sessions and you can have multiple users interacting with the same Agent at the same time.

Set a `user_id` to connect a user to their sessions with the Agent.

In the example below, we set a `session_id` to demo how to have multi-turn conversations with multiple users at the same time. In production, the `session_id` is auto generated.

Note: Multi-user, multi-session currently only works with `Memory.v2`, which will become the default memory implementation in the next release.

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.v2 import Memory

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Multi-user, multi-session only work with Memory.v2
    memory=Memory(),
    add_history_to_messages=True,
    num_history_runs=3,
)

user_1_id = "user_101"
user_2_id = "user_102"

user_1_session_id = "session_101"
user_2_session_id = "session_102"

# Start the session with user 1
agent.print_response(
    "Tell me a 5 second short story about a robot.",
    user_id=user_1_id,
    session_id=user_1_session_id,
)
# Continue the session with user 1
agent.print_response("Now tell me a joke.", user_id=user_1_id, session_id=user_1_session_id)

# Start the session with user 2
agent.print_response("Tell me about quantum physics.", user_id=user_2_id, session_id=user_2_session_id)
# Continue the session with user 2
agent.print_response("What is the speed of light?", user_id=user_2_id, session_id=user_2_session_id)

# Ask the agent to give a summary of the conversation, this will use the history from the previous messages
agent.print_response(
    "Give me a summary of our conversation.",
    user_id=user_1_id,
    session_id=user_1_session_id,
)

```

[​](#fetch-messages-from-last-n-sessions) Fetch messages from last N sessions
-----------------------------------------------------------------------------

In some scenarios, you might want to fetch messages from the last N sessions to provide context or continuity in conversations.

Here’s an example of how you can achieve this:

Copy

Ask AI

```
# Remove the tmp db file before running the script
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

os.remove("tmp/data.db")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    user_id="user_1",
    storage=SqliteStorage(table_name="agent_sessions_new", db_file="tmp/data.db"),
    search_previous_sessions_history=True,  # allow searching previous sessions
    num_history_sessions=2,  # only include the last 2 sessions in the search to avoid context length issues
    show_tool_calls=True,
)

session_1_id = "session_1_id"
session_2_id = "session_2_id"
session_3_id = "session_3_id"
session_4_id = "session_4_id"
session_5_id = "session_5_id"

agent.print_response("What is the capital of South Africa?", session_id=session_1_id)
agent.print_response("What is the capital of China?", session_id=session_2_id)
agent.print_response("What is the capital of France?", session_id=session_3_id)
agent.print_response("What is the capital of Japan?", session_id=session_4_id)
agent.print_response(
    "What did I discuss in my previous conversations?", session_id=session_5_id
)  # It should only include the last 2 sessions

```

To enable fetching messages from the last N sessions, you need to use the following flags:

* `search_previous_sessions_history`: Set this to `True` to allow searching through previous sessions.
* `num_history_sessions`: Specify the number of past sessions to include in the search. In this example, it is set to `2` to include only the last 2 sessions.
  It’s advisable to keep this number to 2 or 3 for now, as a larger number might fill up the context length of the model, potentially leading to performance issues.

These flags help manage the context length and ensure that only relevant session history is included in the conversation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/sessions.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/sessions)

[Metrics](/agents/metrics)[Agent State](/agents/state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Multi-user, multi-session Agents](#multi-user%2C-multi-session-agents)
* [Fetch messages from last N sessions](#fetch-messages-from-last-n-sessions)

Assistant

Responses are generated using AI and may contain mistakes.
