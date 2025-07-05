Running your Agent - Agno

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

Running your Agent

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

Running your Agent
==================

Learn how to run an agent and get the response.

The `Agent.run()` function runs the agent and generates a response, either as a `RunResponse` object or a stream of `RunResponse` objects.

Many of our examples use `agent.print_response()` which is a helper utility to print the response in the terminal. It uses `agent.run()` under the hood.

[​](#running-your-agent) Running your Agent
-------------------------------------------

Here’s how to run your agent. The response is captured in the `response`.

Copy

Ask AI

```
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

# Run agent and return the response as a variable
response: RunResponse = agent.run("Tell me a 5 second short story about a robot")

# Print the response in markdown format
pprint_run_response(response, markdown=True)

```

[​](#runresponse) RunResponse
-----------------------------

The `Agent.run()` function returns a `RunResponse` object when not streaming. It has the following attributes:

Understanding Metrics

For a detailed explanation of how metrics are collected and used, please refer to the [Metrics Documentation](/agents/metrics).

See detailed documentation in the [RunResponse](/reference/agents/run-response) documentation.

[​](#streaming-responses) Streaming Responses
---------------------------------------------

To enable streaming, set `stream=True` when calling `run()`. This will return an iterator of `RunResponseEvent` objects instead of a single response.

From `agno` version `1.6.0`, the `Agent.run()` function returns an iterator of `RunResponseEvent`, not of `RunResponse` objects.

Copy

Ask AI

```
from typing import Iterator
from agno.agent import Agent, RunResponseEvent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4-mini"))

# Run agent and return the response as a stream
response_stream: Iterator[RunResponseEvent] = agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True
)

# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)

```

### [​](#streaming-intermediate-steps) Streaming Intermediate Steps

For even more detailed streaming, you can enable intermediate steps by setting `stream_intermediate_steps=True`. This will provide real-time updates about the agent’s internal processes.

Copy

Ask AI

```
# Stream with intermediate steps
response_stream: Iterator[RunResponseEvent] = agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True,
    stream_intermediate_steps=True
)

```

### [​](#handling-events) Handling Events

You can process events as they arrive by iterating over the response stream:

Copy

Ask AI

```
response_stream = agent.run("Your prompt", stream=True, stream_intermediate_steps=True)

for event in response_stream:
    if event.event == "RunResponseContent":
        print(f"Content: {event.content}")
    elif event.event == "ToolCallStarted":
        print(f"Tool call started: {event.tool}")
    elif event.event == "ReasoningStep":
        print(f"Reasoning step: {event.content}")
    ...

```

You can see this behavior in action in our [Playground](https://app.agno.com/playground/agents?endpoint=demo.agnoagents.com&agent=reasoning-agent).

### [​](#storing-events) Storing Events

You can store all the events that happened during a run on the `RunResponse` object.

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"), store_events=True)

response = agent.run("Tell me a 5 second short story about a lion", stream=True, stream_intermediate_steps=True)
pprint_run_response(response)

for event in agent.run_response.events:
    print(event.event)

```

By default the `RunResponseContentEvent` event is not stored. You can modify which events are skipped by setting the `events_to_skip` parameter.

For example:

Copy

Ask AI

```
agent = Agent(model=OpenAIChat(id="gpt-4o-mini"), store_events=True, events_to_skip=[RunEvent.run_started.value])

```

### [​](#event-types) Event Types

The following events are yielded by the `Agent.run()` and `Agent.arun()` functions depending on the agent’s configuration:

#### [​](#core-events) Core Events

| Event Type | Description |
| --- | --- |
| `RunStarted` | Indicates the start of a run |
| `RunResponseContent` | Contains the model’s response text as individual chunks |
| `RunCompleted` | Signals successful completion of the run |
| `RunError` | Indicates an error occurred during the run |
| `RunCancelled` | Signals that the run was cancelled |

#### [​](#control-flow-events) Control Flow Events

| Event Type | Description |
| --- | --- |
| `RunPaused` | Indicates the run has been paused |
| `RunContinued` | Signals that a paused run has been continued |

#### [​](#tool-events) Tool Events

| Event Type | Description |
| --- | --- |
| `ToolCallStarted` | Indicates the start of a tool call |
| `ToolCallCompleted` | Signals completion of a tool call, including tool call results |

#### [​](#reasoning-events) Reasoning Events

| Event Type | Description |
| --- | --- |
| `ReasoningStarted` | Indicates the start of the agent’s reasoning process |
| `ReasoningStep` | Contains a single step in the reasoning process |
| `ReasoningCompleted` | Signals completion of the reasoning process |

#### [​](#memory-events) Memory Events

| Event Type | Description |
| --- | --- |
| `MemoryUpdateStarted` | Indicates that the agent is updating its memory |
| `MemoryUpdateCompleted` | Signals completion of a memory update |

See detailed documentation in the [RunResponseEvent](/reference/agents/run-response) documentation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/run.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/run)

[Overview](/agents/introduction)[Metrics](/agents/metrics)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Running your Agent](#running-your-agent)
* [RunResponse](#runresponse)
* [Streaming Responses](#streaming-responses)
* [Streaming Intermediate Steps](#streaming-intermediate-steps)
* [Handling Events](#handling-events)
* [Storing Events](#storing-events)
* [Event Types](#event-types)
* [Core Events](#core-events)
* [Control Flow Events](#control-flow-events)
* [Tool Events](#tool-events)
* [Reasoning Events](#reasoning-events)
* [Memory Events](#memory-events)

Assistant

Responses are generated using AI and may contain mistakes.
