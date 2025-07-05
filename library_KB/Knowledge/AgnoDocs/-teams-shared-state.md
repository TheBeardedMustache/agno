Team State - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Teams

Team State

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

  + [Overview](/teams/introduction)
  + [Running your Team](/teams/run)
  + [Team State](/teams/shared-state)
  + Team Modes
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

Teams

Copy page

Team State
==========

Learn about the shared state of Agent Teams.

There are multiple ways to share state between team members.

[​](#shared-team-state) Shared Team State
-----------------------------------------

Team Session State enables sophisticated state management across teams of agents, with both shared and private state capabilities.

Teams often need to coordinate on shared information (like a shopping list) while maintaining their own private metrics or configuration. Agno provides an elegant three-tier state system for this.

Agno’s Team state management provides three distinct levels:

* Team’s team\_session\_state - Shared state accessible by all team members.
* Team’s session\_state - Private state only accessible by the team leader
* Agent’s session\_state - Private state for each agent members

Team state propagates through nested team structures as well

### [​](#how-to-use-team-session-state) How to use Team Session State

You can set the `team_session_state` parameter on `Team` to share state between team members.
This state is available to all team members and is synchronized between them.

For example:

Copy

Ask AI

```
team = Team(
    members=[agent1, agent2, agent3],
    team_session_state={"shopping_list": []},
)

```

Members can access the shared state using the `team_session_state` attribute in tools.

For example:

Copy

Ask AI

```
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list and return confirmation.

    Args:
        item (str): The item to add to the shopping list.
    """
    # Add the item if it's not already in the list
    if item.lower() not in [
        i.lower() for i in agent.team_session_state["shopping_list"]
    ]:
        agent.team_session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list"
    else:
        return f"'{item}' is already in the shopping list"

```

### [​](#example) Example

Here’s a simple example of a team managing a shared shopping list:

team\_session\_state.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team


# Define tools that work with shared team state
def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    if item.lower() not in [
        i.lower() for i in agent.team_session_state["shopping_list"]
    ]:
        agent.team_session_state["shopping_list"].append(item)
        return f"Added '{item}' to the shopping list"
    else:
        return f"'{item}' is already in the shopping list"


def remove_item(agent: Agent, item: str) -> str:
    """Remove an item from the shopping list."""
    for i, list_item in enumerate(agent.team_session_state["shopping_list"]):
        if list_item.lower() == item.lower():
            agent.team_session_state["shopping_list"].pop(i)
            return f"Removed '{list_item}' from the shopping list"
    
    return f"'{item}' was not found in the shopping list"


# Create an agent that manages the shopping list
shopping_agent = Agent(
    name="Shopping List Agent",
    role="Manage the shopping list",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[add_item, remove_item],
)


# Define team-level tools
def list_items(team: Team) -> str:
    """List all items in the shopping list."""
    # Access shared state (not private state)
    shopping_list = team.team_session_state["shopping_list"]
    
    if not shopping_list:
        return "The shopping list is empty."
    
    items_text = "\n".join([f"- {item}" for item in shopping_list])
    return f"Current shopping list:\n{items_text}"


def add_chore(team: Team, chore: str) -> str:
    """Add a completed chore to the team's private log."""
    # Access team's private state
    if "chores" not in team.session_state:
        team.session_state["chores"] = []
    
    team.session_state["chores"].append(chore)
    return f"Logged chore: {chore}"


# Create a team with both shared and private state
shopping_team = Team(
    name="Shopping Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    members=[shopping_agent],
    # Shared state - accessible by all members
    team_session_state={"shopping_list": []},
    # Team's private state - only accessible by team
    session_state={"chores": []},
    tools=[list_items, add_chore],
    instructions=[
        "You manage a shopping list.",
        "Forward add/remove requests to the Shopping List Agent.",
        "Use list_items to show the current list.",
        "Log completed tasks using add_chore.",
    ],
    show_tool_calls=True,
)

# Example usage
shopping_team.print_response("Add milk, eggs, and bread", stream=True)
print(f"Shared state: {shopping_team.team_session_state}")

shopping_team.print_response("What's on my list?", stream=True)

shopping_team.print_response("I got the eggs", stream=True)
print(f"Shared state: {shopping_team.team_session_state}")
print(f"Team private state: {shopping_team.session_state}")

```

Notice how shared tools use `agent.team_session_state`, which allows state to propagate and persist across the entire team — even for subteams within the team. This ensures consistent shared state for all members.

In contrast, tools specific to a team use `team.session_state`, allowing for private, team-specific state. For example, a team leader’s tools would maintain their own session state using team.session\_state.

See a full example [here](/examples/teams/shared_state/team_shared_state).

[​](#agentic-context) Agentic Context
-------------------------------------

The Team Leader maintains a shared context that is updated agentically (i.e. by the team leader) and is sent to team members if needed.

Agentic Context is critical for effective information sharing and collaboration between agents and the quality of the team’s responses depends on how well the team leader manages this shared agentic context.
This could require higher quality models for the team leader to ensure the quality of the team’s responses.

The tasks and responses of team members are automatically added to the team context, but Agentic Context needs to be enabled by the developer.

### [​](#enable-agentic-context) Enable Agentic Context

To enable the Team leader to maintain Agentic Context, set `enable_agentic_context=True`.

This will allow the team leader to maintain and update the team context during the run.

Copy

Ask AI

```
team = Team(
    members=[agent1, agent2, agent3],
    enable_agentic_context=True,  # Enable Team Leader to maintain Agentic Context
)

```

### [​](#team-member-interactions) Team Member Interactions

Agent Teams can share interactions between members, allowing agents to learn from each other’s outputs:

Copy

Ask AI

```
team = Team(
    members=[agent1, agent2, agent3],
    share_member_interactions=True,  # Share interactions
)

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/teams/shared-state.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /teams/shared-state)

[Running your Team](/teams/run)[Route](/teams/route)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Shared Team State](#shared-team-state)
* [How to use Team Session State](#how-to-use-team-session-state)
* [Example](#example)
* [Agentic Context](#agentic-context)
* [Enable Agentic Context](#enable-agentic-context)
* [Team Member Interactions](#team-member-interactions)

Assistant

Responses are generated using AI and may contain mistakes.
