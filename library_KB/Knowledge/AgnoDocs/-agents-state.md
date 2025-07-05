Agent State - Agno

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

Agent State

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

Agent State
===========

**State** is any kind of data the Agent needs to maintain throughout runs.

A simple yet common use case for Agents is to manage lists, items and other “information” for a user. For example, a shopping list, a todo list, a wishlist, etc.

This can be easily managed using the `session_state`. The Agent updates the `session_state` in tool calls and exposes them to the Model in the `description` and `instructions`.

Agno’s provides a powerful and elegant state management system, here’s how it works:

* The `Agent` has a `session_state` parameter.
* We add our state variables to this `session_state` dictionary.
* We update the `session_state` dictionary in tool calls or other functions.
* We share the current `session_state` with the Model in the `description` and `instructions`.
* The `session_state` is stored with Agent sessions and is persisted in a database. Meaning, it is available across execution cycles.

Here’s an example of an Agent managing a shopping list:

session\_state.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Define a tool that increments our counter and returns the new value
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    return f"The shopping list is now {agent.session_state['shopping_list']}"


# Create an Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with a counter starting at 0
    session_state={"shopping_list": []},
    tools=[add_item],
    # You can use variables from the session state in the instructions
    instructions="Current state (shopping list) is: {shopping_list}",
    # Important: Add the state to the messages
    add_state_in_messages=True,
    markdown=True,
)

# Example usage
agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Final session state: {agent.session_state}")

```

This is as good and elegant as state management gets.

[​](#maintaining-state-across-multiple-runs) Maintaining state across multiple runs
-----------------------------------------------------------------------------------

A big advantage of **sessions** is the ability to maintain state across multiple runs. For example, let’s say the agent is helping a user keep track of their shopping list.

By setting `add_state_in_messages=True`, the keys of the `session_state` dictionary are available in the `description` and `instructions` as variables.

Use this pattern to add the shopping\_list to the instructions directly.

shopping\_list.py

Copy

Ask AI

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat


# Define tools to manage our shopping list
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list and return confirmation."""
    # Add the item if it's not already in the list
    if item.lower() not in [i.lower() for i in agent.session_state["shopping_list"]]:
        agent.session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list"
    else:
        return f"'{item}' is already in the shopping list"


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the shopping list by name."""
    # Case-insensitive search
    for i, list_item in enumerate(agent.session_state["shopping_list"]):
        if list_item.lower() == item.lower():
            agent.session_state["shopping_list"].pop(i)
            return f"Removed '{list_item}' from the shopping list"

    return f"'{item}' was not found in the shopping list"


def list_items(agent: Agent) -> str:
    """List all items in the shopping list."""
    shopping_list = agent.session_state["shopping_list"]

    if not shopping_list:
        return "The shopping list is empty."

    items_text = "\n".join([f"- {item}" for item in shopping_list])
    return f"Current shopping list:\n{items_text}"


# Create a Shopping List Manager Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with an empty shopping list
    session_state={"shopping_list": []},
    tools=[add_item, remove_item, list_items],
    # You can use variables from the session state in the instructions
    instructions=dedent("""\
        Your job is to manage a shopping list.

        The shopping list starts empty. You can add items, remove items by name, and list all items.

        Current shopping list: {shopping_list}
    """),
    show_tool_calls=True,
    add_state_in_messages=True,
    markdown=True,
)

# Example usage
agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Session state: {agent.session_state}")

agent.print_response("I got bread", stream=True)
print(f"Session state: {agent.session_state}")

agent.print_response("I need apples and oranges", stream=True)
print(f"Session state: {agent.session_state}")

agent.print_response("whats on my list?", stream=True)
print(f"Session state: {agent.session_state}")

agent.print_response("Clear everything from my list and start over with just bananas and yogurt", stream=True)
print(f"Session state: {agent.session_state}")

```

We love how elegantly we can maintain and pass on state across multiple runs.

[​](#using-state-in-instructions) Using state in instructions
-------------------------------------------------------------

You can use variables from the session state in the instructions by setting `add_state_in_messages=True`.

Don’t use the f-string syntax in the instructions. Directly use the `{key}` syntax, Agno substitutes the values for you.

state\_in\_instructions.py

Copy

Ask AI

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with a variable
    session_state={"user_name": "John"},
    # You can use variables from the session state in the instructions
    instructions="Users name is {user_name}",
    show_tool_calls=True,
    add_state_in_messages=True,
    markdown=True,
)

agent.print_response("What is my name?", stream=True)

```

[​](#persisting-state-in-database) Persisting state in database
---------------------------------------------------------------

`session_state` is part of the Agent session and is saved to the database after each run if a `storage` driver is provided.

Here’s an example of an Agent that maintains a shopping list and persists the state in a database. Run this script multiple times to see the state being persisted.

session\_state\_storage.py

Copy

Ask AI

```
"""Run `pip install agno openai sqlalchemy` to install dependencies."""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage


# Define a tool that adds an item to the shopping list
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    if item not in agent.session_state["shopping_list"]:
        agent.session_state["shopping_list"].append(item)
    return f"The shopping list is now {agent.session_state['shopping_list']}"


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Fix the session id to continue the same session across execution cycles
    session_id="fixed_id_for_demo",
    # Initialize the session state with an empty shopping list
    session_state={"shopping_list": []},
    # Add a tool that adds an item to the shopping list
    tools=[add_item],
    # Store the session state in a SQLite database
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    # Add the current shopping list from the state in the instructions
    instructions="Current shopping list is: {shopping_list}",
    # Important: Set `add_state_in_messages=True`
    # to make `{shopping_list}` available in the instructions
    add_state_in_messages=True,
    markdown=True,
)

# Example usage
agent.print_response("What's on my shopping list?", stream=True)
print(f"Session state: {agent.session_state}")
agent.print_response("Add milk, eggs, and bread", stream=True)
print(f"Session state: {agent.session_state}")

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/state.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/state)

[Sessions](/agents/sessions)[Memory](/agents/memory)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Maintaining state across multiple runs](#maintaining-state-across-multiple-runs)
* [Using state in instructions](#using-state-in-instructions)
* [Persisting state in database](#persisting-state-in-database)

Assistant

Responses are generated using AI and may contain mistakes.
