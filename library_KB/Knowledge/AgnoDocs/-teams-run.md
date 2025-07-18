﻿Running your Team - Agno

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

Running your Team

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

Running your Team
=================

Learn how to run a team and get the response.

The `Team.run()` function runs the team and generates a response, either as a `TeamRunResponse` object or a stream of `TeamRunResponseEvent` objects.

Many of our examples use `team.print_response()` which is a helper utility to print the response in the terminal. It uses `team.run()` under the hood.

Here’s how to run your team. The response is captured in the `response` and `response_stream` variables.

Copy

Ask AI

```
from agno.team import Team
from agno.models.openai import OpenAIChat

agent_1 = Agent(name="News Agent", role="Get the latest news")

agent_2 = Agent(name="Weather Agent", role="Get the weather for the next 7 days")

team = Team(name="News and Weather Team", mode="coordinate", members=[agent_1, agent_2])

response = team.run("What is the weather in Tokyo?")

# Synchronous execution
result = team.run("What is the weather in Tokyo?")

# Asynchronous execution
result = await team.arun("What is the weather in Tokyo?")

# Streaming responses
for chunk in team.run("What is the weather in Tokyo?", stream=True):
    print(chunk.content, end="", flush=True)

# Asynchronous streaming
async for chunk in await team.arun("What is the weather in Tokyo?", stream=True):
    print(chunk.content, end="", flush=True)

```

[​](#streaming-intermediate-steps) Streaming Intermediate Steps
---------------------------------------------------------------

Throughout the execution of a team, multiple events take place, and we provide these events in real-time for enhanced team transparency.

You can enable streaming of intermediate steps by setting `stream_intermediate_steps=True`.

Copy

Ask AI

```
# Stream with intermediate steps
response_stream = team.run(
    "What is the weather in Tokyo?",
    stream=True,
    stream_intermediate_steps=True
)

```

### [​](#handling-events) Handling Events

You can process events as they arrive by iterating over the response stream:

Copy

Ask AI

```
response_stream = team.run("Your prompt", stream=True, stream_intermediate_steps=True)

for event in response_stream:
    if event.event == "TeamRunResponseContent":
        print(f"Content: {event.content}")
    elif event.event == "TeamToolCallStarted":
        print(f"Tool call started: {event.tool}")
    elif event.event == "ToolCallStarted":
        print(f"Member tool call started: {event.tool}")
    elif event.event == "ToolCallCompleted":
        print(f"Member tool call completed: {event.tool}")
    elif event.event == "TeamReasoningStep":
        print(f"Reasoning step: {event.content}")
    ...

```

Team member events are yielded during team execution when a team member is being executed. You can disable this by setting `stream_member_events=False`.

### [​](#storing-events) Storing Events

You can store all the events that happened during a run on the `RunResponse` object.

Copy

Ask AI

```
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

team = Team(model=OpenAIChat(id="gpt-4o-mini"), members=[], store_events=True)

response = team.run("Tell me a 5 second short story about a lion", stream=True, stream_intermediate_steps=True)
pprint_run_response(response)

for event in agent.run_response.events:
    print(event.event)

```

By default the `TeamRunResponseContentEvent` and `RunResponseContentEvent` events are not stored. You can modify which events are skipped by setting the `events_to_skip` parameter.

For example:

Copy

Ask AI

```
team = Team(model=OpenAIChat(id="gpt-4o-mini"), members=[], store_events=True, events_to_skip=[TeamRunEvent.run_started.value])

```

### [​](#event-types) Event Types

The following events are sent by the `Team.run()` and `Team.arun()` functions depending on team’s configuration:

#### [​](#core-events) Core Events

| Event Type | Description |
| --- | --- |
| `TeamRunStarted` | Indicates the start of a run |
| `TeamRunResponseContent` | Contains the model’s response text as individual chunks |
| `TeamRunCompleted` | Signals successful completion of the run |
| `TeamRunError` | Indicates an error occurred during the run |
| `TeamRunCancelled` | Signals that the run was cancelled |

#### [​](#tool-events) Tool Events

| Event Type | Description |
| --- | --- |
| `TeamToolCallStarted` | Indicates the start of a tool call |
| `TeamToolCallCompleted` | Signals completion of a tool call, including tool call results |

#### [​](#reasoning-events) Reasoning Events

| Event Type | Description |
| --- | --- |
| `TeamReasoningStarted` | Indicates the start of the agent’s reasoning process |
| `TeamReasoningStep` | Contains a single step in the reasoning process |
| `TeamReasoningCompleted` | Signals completion of the reasoning process |

#### [​](#memory-events) Memory Events

| Event Type | Description |
| --- | --- |
| `TeamMemoryUpdateStarted` | Indicates that the agent is updating its memory |
| `TeamMemoryUpdateCompleted` | Signals completion of a memory update |

See detailed documentation in the [TeamRunResponse](/reference/teams/team-response) documentation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/teams/run.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /teams/run)

[Overview](/teams/introduction)[Team State](/teams/shared-state)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Streaming Intermediate Steps](#streaming-intermediate-steps)
* [Handling Events](#handling-events)
* [Storing Events](#storing-events)
* [Event Types](#event-types)
* [Core Events](#core-events)
* [Tool Events](#tool-events)
* [Reasoning Events](#reasoning-events)
* [Memory Events](#memory-events)

Assistant

Responses are generated using AI and may contain mistakes.
