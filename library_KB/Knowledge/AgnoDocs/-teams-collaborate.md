Collaborate - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Team Modes

Collaborate

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

    - [Route](/teams/route)
    - [Coordinate](/teams/coordinate)
    - [Collaborate](/teams/collaborate)
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

Team Modes

Copy page

Collaborate
===========

In **Collaborate Mode**, all team members respond to the user query at once. This gives the team coordinator to review whether the team has reached a consensus on a particular topic and then synthesize the responses from all team members into a single response.

This is especially useful when used with `async await`, because it allows the individual members to respond concurrently and the coordinator to synthesize the responses asynchronously.

[​](#how-collaborate-mode-works) How Collaborate Mode Works
-----------------------------------------------------------

In “collaborate” mode:

1. The team receives a user query
2. All team members get sent a query. When running synchronously, this happens one by one. When running asynchronously, this happens concurrently.
3. Each team member produces an output
4. The coordinator reviews the outputs and synthesizes them into a single response

1

Create a collaborate mode team

Create a file `discussion_team.py`

discussion\_team.py

Copy

Ask AI

```
import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools

reddit_researcher = Agent(
    name="Reddit Researcher",
    role="Research a topic on Reddit",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a Reddit researcher.
    You will be given a topic to research on Reddit.
    You will need to find the most relevant posts on Reddit.
    """),
)

hackernews_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Research a topic on HackerNews.",
    tools=[HackerNewsTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a HackerNews researcher.
    You will be given a topic to research on HackerNews.
    You will need to find the most relevant posts on HackerNews.
    """),
)

academic_paper_researcher = Agent(
    name="Academic Paper Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Research academic papers and scholarly content",
    tools=[GoogleSearchTools(), ArxivTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a academic paper researcher.
    You will be given a topic to research in academic literature.
    You will need to find relevant scholarly articles, papers, and academic discussions.
    Focus on peer-reviewed content and citations from reputable sources.
    Provide brief summaries of key findings and methodologies.
    """),
)

twitter_researcher = Agent(
    name="Twitter Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Research trending discussions and real-time updates",
    tools=[DuckDuckGoTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a Twitter/X researcher.
    You will be given a topic to research on Twitter/X.
    You will need to find trending discussions, influential voices, and real-time updates.
    Focus on verified accounts and credible sources when possible.
    Track relevant hashtags and ongoing conversations.
    """),
)


agent_team = Team(
    name="Discussion Team",
    mode="collaborate",
    model=OpenAIChat("gpt-4o"),
    members=[
        reddit_researcher,
        hackernews_researcher,
        academic_paper_researcher,
        twitter_researcher,
    ],
    instructions=[
        "You are a discussion master.",
        "You have to stop the discussion when you think the team has reached a consensus.",
    ],
    success_criteria="The team has reached a consensus.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    asyncio.run(
        agent_team.print_response(
            message="Start the discussion on the topic: 'What is the best way to learn to code?'",
            stream=True,
            stream_intermediate_steps=True,
        )
    )


```

2

Run the team

Install libraries

Copy

Ask AI

```
pip install openai duckduckgo-search arxiv pypdf googlesearch-python pycountry

```

Run the team

Copy

Ask AI

```
python discussion_team.py

```

[​](#defining-success-criteria) Defining Success Criteria
---------------------------------------------------------

You can guide the collaborative team by specifying success criteria for the team coordinator to evaluate:

Copy

Ask AI

```
strategy_team = Team(
    members=[hackernews_researcher, academic_paper_researcher, twitter_researcher],
    mode="collaborate",
    name="Research Team",
    description="A team that researches a topic",
    success_criteria="The team has reached a consensus on the topic",
)

response = strategy_team.run(
    "What is the best way to learn to code?"
)

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/teams/collaborate.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /teams/collaborate)

[Coordinate](/teams/coordinate)[Overview](/models/introduction)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [How Collaborate Mode Works](#how-collaborate-mode-works)
* [Defining Success Criteria](#defining-success-criteria)

Assistant

Responses are generated using AI and may contain mistakes.
