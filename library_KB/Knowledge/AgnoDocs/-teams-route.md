Route - Agno

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

Route

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

Route
=====

In **Route Mode**, the Team Leader directs user queries to the most appropriate team member based on the content of the request.

The Team Leader acts as a smart router, analyzing the query and selecting the best-suited agent to handle it. The member’s response is then returned directly to the user.

[​](#how-route-mode-works) How Route Mode Works
-----------------------------------------------

In “route” mode:

1. The team receives a user query
2. A Team Leader analyzes the query to determine which team member has the right expertise
3. The query is forwarded to the selected team member
4. The response from the team member is returned directly to the user

This mode is particularly useful when you have specialized agents with distinct expertise areas and want to automatically direct queries to the right specialist.

1

Create Multi Language Team

Create a file `multi_language_team.py`

multi\_language\_team.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.deepseek import DeepSeek
from agno.models.mistral.mistral import MistralChat
from agno.models.openai import OpenAIChat
from agno.team.team import Team

english_agent = Agent(
    name="English Agent",
    role="You can only answer in English",
    model=OpenAIChat(id="gpt-4.5-preview"),
    instructions=[
        "You must only respond in English",
    ],
)

japanese_agent = Agent(
    name="Japanese Agent",
    role="You can only answer in Japanese",
    model=DeepSeek(id="deepseek-chat"),
    instructions=[
        "You must only respond in Japanese",
    ],
)
chinese_agent = Agent(
    name="Chinese Agent",
    role="You can only answer in Chinese",
    model=DeepSeek(id="deepseek-chat"),
    instructions=[
        "You must only respond in Chinese",
    ],
)
spanish_agent = Agent(
    name="Spanish Agent",
    role="You can only answer in Spanish",
    model=OpenAIChat(id="gpt-4.5-preview"),
    instructions=[
        "You must only respond in Spanish",
    ],
)

french_agent = Agent(
    name="French Agent",
    role="You can only answer in French",
    model=MistralChat(id="mistral-large-latest"),
    instructions=[
        "You must only respond in French",
    ],
)

german_agent = Agent(
    name="German Agent",
    role="You can only answer in German",
    model=Claude("claude-3-5-sonnet-20241022"),
    instructions=[
        "You must only respond in German",
    ],
)
multi_language_team = Team(
    name="Multi Language Team",
    mode="route",
    model=OpenAIChat("gpt-4.5-preview"),
    members=[
        english_agent,
        spanish_agent,
        japanese_agent,
        french_agent,
        german_agent,
        chinese_agent,
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "You are a language router that directs questions to the appropriate language agent.",
        "If the user asks in a language whose agent is not a team member, respond in English with:",
        "'I can only answer in the following languages: English, Spanish, Japanese, French and German. Please ask your question in one of these languages.'",
        "Always check the language of the user's input before routing to an agent.",
        "For unsupported languages like Italian, respond in English with the above message.",
    ],
    show_members_responses=True,
)


# Ask "How are you?" in all supported languages
multi_language_team.print_response(
    "How are you?", stream=True  # English
)

multi_language_team.print_response(
    "你好吗？", stream=True  # Chinese
)

multi_language_team.print_response(
    "お元気ですか?", stream=True  # Japanese
)

multi_language_team.print_response(
    "Comment allez-vous?",
    stream=True,  # French
)

```

2

Run the team

Install libraries

Copy

Ask AI

```
pip install openai mistral agno

```

Run the team

Copy

Ask AI

```
python multi_language_team.py

```

[​](#structured-output-with-route-mode) Structured Output with Route Mode
-------------------------------------------------------------------------

One powerful feature of route mode is its ability to maintain structured output from member agents.
When using a Pydantic model for the response, the response from the selected team member will be automatically parsed into the specified structure.

### [​](#defining-structured-output-models) Defining Structured Output Models

Copy

Ask AI

```
from pydantic import BaseModel
from typing import List, Optional
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team


class StockAnalysis(BaseModel):
    symbol: str
    company_name: str
    analysis: str

class CompanyAnalysis(BaseModel):
    company_name: str
    analysis: str

stock_searcher = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
    response_model=StockAnalysis,
    role="Searches for information on stocks and provides price analysis.",
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
        )
    ],
)

company_info_agent = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches for information about companies and recent news.",
    response_model=CompanyAnalysis,
    tools=[
        YFinanceTools(
            stock_price=False,
            company_info=True,
            company_news=True,
        )
    ],
)

team = Team(
    name="Stock Research Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher, company_info_agent],
    markdown=True,
)

# This should route to the stock_searcher
response = team.run("What is the current stock price of NVDA?")
assert isinstance(response.content, StockAnalysis)

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/teams/route.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /teams/route)

[Team State](/teams/shared-state)[Coordinate](/teams/coordinate)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [How Route Mode Works](#how-route-mode-works)
* [Structured Output with Route Mode](#structured-output-with-route-mode)
* [Defining Structured Output Models](#defining-structured-output-models)

Assistant

Responses are generated using AI and may contain mistakes.
