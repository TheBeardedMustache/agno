Metrics - Agno

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

Metrics

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

Metrics
=======

Understanding agent run and session metrics in Agno

[​](#overview) Overview
-----------------------

When you run an agent in Agno, the response you get (**RunResponse**) includes detailed metrics about the run. These metrics help you understand resource usage (like **token usage** and **time**), performance, and other aspects of the model and tool calls.

Metrics are available at multiple levels:

* **Per-message**: Each message (assistant, tool, etc.) has its own metrics.
* **Per-tool call**: Each tool execution has its own metrics.
* **Aggregated**: The `RunResponse` aggregates metrics across all messages in the run.

Where Metrics Live

* `RunResponse.metrics`: Aggregated metrics for the whole run, as a dictionary.
* `ToolExecution.metrics`: Metrics for each tool call.
* `Message.metrics`: Metrics for each message (assistant, tool, etc.).

[​](#example-usage) Example Usage
---------------------------------

Suppose you have an agent that performs some tasks and you want to analyze the metrics after running it. Here’s how you can access and print the metrics:

You run the following code to create an agent and run it with the following configuration:

Copy

Ask AI

```
from typing import Iterator

from agno.agent import Agent, RunResponse
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from rich.pretty import pprint

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
    show_tool_calls=True,
)

agent.print_response(
    "What is the stock price of NVDA", stream=True
)

# Print metrics per message
if agent.run_response.messages:
    for message in agent.run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

# Print the aggregated metrics for the whole run
print("---" * 5, "Collected Metrics", "---" * 5)
pprint(agent.run_response.metrics)
# Print the aggregated metrics for the whole session
print("---" * 5, "Session Metrics", "---" * 5)
pprint(agent.session_metrics)

```

You’d see the outputs with following information:

### [​](#tool-execution-metrics) Tool Execution Metrics

This section provides metrics for each tool execution. It includes details about the resource usage and performance of individual tool calls.

### [​](#message-metrics) Message Metrics

Here, you can see the metrics for each message response from the agent. All “assistant” responses will have metrics like this, helping you understand the performance and resource usage at the message level.

### [​](#aggregated-run-metrics) Aggregated Run Metrics

The aggregated metrics provide a comprehensive view of the entire run. This includes a summary of all messages and tool calls, giving you an overall picture of the agent’s performance and resource usage.

Similarly for the session metrics, you can see the aggregated metrics across all runs in the session, providing insights into the overall performance and resource usage of the agent across multiple runs.

[​](#how-metrics-are-aggregated) How Metrics Are Aggregated
-----------------------------------------------------------

* **Per-message**: Each message (assistant, tool, etc.) has its own metrics object.
* **Run-level**: RunResponse.metrics is a dictionary where each key (e.g., input\_tokens) maps to a list of values from all assistant messages in the run.
* **Session-level**: `SessionMetrics` (see `agent.session_metrics`) aggregates metrics across all runs in the session.

[​](#messagemetrics-params) `MessageMetrics` Params
---------------------------------------------------

| Field | Description |
| --- | --- |
| input\_tokens | Number of tokens in the prompt/input to the model. |
| output\_tokens | Number of tokens generated by the model as output. |
| total\_tokens | Total tokens used (input + output). |
| prompt\_tokens | Tokens in the prompt (same as input\_tokens in the case of OpenAI). |
| completion\_tokens | Tokens in the completion (same as output\_tokens in the case of OpenAI). |
| audio\_tokens | Total audio tokens (if using audio input/output). |
| input\_audio\_tokens | Audio tokens in the input. |
| output\_audio\_tokens | Audio tokens in the output. |
| cached\_tokens | Tokens served from cache (if caching is used). |
| cache\_write\_tokens | Tokens written to cache. |
| reasoning\_tokens | Tokens used for reasoning steps (if enabled). |
| prompt\_tokens\_details | Dict with detailed breakdown of prompt tokens (used by OpenAI). |
| completion\_tokens\_details | Dict with detailed breakdown of completion tokens (used by OpenAI). |
| additional\_metrics | Any extra metrics provided by the model/tool (e.g., latency, cost, etc.). |
| time | Time taken to generate the message (in seconds). |
| time\_to\_first\_token | Time until the first token is generated (in seconds). |

> Note: Not all fields are always present; it depends on the model/tool and the run.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/metrics.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/metrics)

[Running your Agent](/agents/run)[Sessions](/agents/sessions)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Overview](#overview)
* [Example Usage](#example-usage)
* [Tool Execution Metrics](#tool-execution-metrics)
* [Message Metrics](#message-metrics)
* [Aggregated Run Metrics](#aggregated-run-metrics)
* [How Metrics Are Aggregated](#how-metrics-are-aggregated)
* [MessageMetrics Params](#messagemetrics-params)

Assistant

Responses are generated using AI and may contain mistakes.
