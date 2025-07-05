Tools - Agno

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

Tools

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

Tools
=====

Learn how to use tools in Agno to build AI agents.

**Agents use tools to take actions and interact with external systems**.

Tools are functions that an Agent can run to achieve tasks. For example: searching the web, running SQL, sending an email or calling APIs. You can use any python function as a tool or use a pre-built **toolkit**. The general syntax is:

Copy

Ask AI

```
from agno.agent import Agent

agent = Agent(
    # Add functions or Toolkits
    tools=[...],
    # Show tool calls in the Agent response
    show_tool_calls=True
)

```

[​](#using-a-toolkit) Using a Toolkit
-------------------------------------

Agno provides many pre-built **toolkits** that you can add to your Agents. For example, let’s use the DuckDuckGo toolkit to search the web.

You can find more toolkits in the [Toolkits](/tools/toolkits) guide.

1

Create Web Search Agent

Create a file `web_search.py`

web\_search.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], show_tool_calls=True, markdown=True)
agent.print_response("Whats happening in France?", stream=True)

```

2

Run the agent

Install libraries

Copy

Ask AI

```
pip install openai duckduckgo-search agno

```

Run the agent

Copy

Ask AI

```
python web_search.py

```

[​](#writing-your-own-tools) Writing your own Tools
---------------------------------------------------

For more control, write your own python functions and add them as tools to an Agent. For example, here’s how to add a `get_top_hackernews_stories` tool to an Agent.

hn\_agent.py

Copy

Ask AI

```
import json
import httpx

from agno.agent import Agent

def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent = Agent(tools=[get_top_hackernews_stories], show_tool_calls=True, markdown=True)
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)

```

Read more about:

* [Available toolkits](/tools/toolkits)
* [Using functions as tools](/tools/tool-decorator)

[​](#attributes) Attributes
---------------------------

The following attributes allow an `Agent` to use tools

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `tools` | `List[Union[Tool, Toolkit, Callable, Dict, Function]]` | - | A list of tools provided to the Model. Tools are functions the model may generate JSON inputs for. |
| `show_tool_calls` | `bool` | `False` | Print the signature of the tool calls in the Model response. |
| `tool_call_limit` | `int` | - | Maximum number of tool calls allowed for a single run. |
| `tool_choice` | `Union[str, Dict[str, Any]]` | - | Controls which (if any) tool is called by the model. “none” means the model will not call a tool and instead generates a message. “auto” means the model can pick between generating a message or calling a tool. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool. “none” is the default when no tools are present. “auto” is the default if tools are present. |
| `read_chat_history` | `bool` | `False` | Add a tool that allows the Model to read the chat history. |
| `search_knowledge` | `bool` | `False` | Add a tool that allows the Model to search the knowledge base (aka Agentic RAG). |
| `update_knowledge` | `bool` | `False` | Add a tool that allows the Model to update the knowledge base. |
| `read_tool_call_history` | `bool` | `False` | Add a tool that allows the Model to get the tool call history. |

[​](#developer-resources) Developer Resources
---------------------------------------------

* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/tools)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/tools.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/tools)

[Memory](/agents/memory)[Structured Output](/agents/structured-output)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Using a Toolkit](#using-a-toolkit)
* [Writing your own Tools](#writing-your-own-tools)
* [Attributes](#attributes)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
