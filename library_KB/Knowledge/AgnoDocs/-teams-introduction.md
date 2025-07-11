﻿What are Agent Teams? - Agno

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

What are Agent Teams?

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

What are Agent Teams?
=====================

Build autonomous multi-agent systems with Agno Agent Teams.

Agent Teams are a collection of Agents (or other sub-teams) that work together to accomplish tasks. Agent Teams can either **“coordinate”**, **“collaborate”** or **“route”** to solve a task.

* [**Route Mode**](/teams/route): The Team Leader routes the user’s request to the most appropriate team member based on the content of the request.
* [**Coordinate Mode**](/teams/coordinate): The Team Leader delegates tasks to team members and synthesizes their outputs into a cohesive response.
* [**Collaborate Mode**](/teams/collaborate): All team members are given the same task and the team coordinator synthesizes their outputs into a cohesive response.

[​](#example) Example
---------------------

Let’s walk through a simple example where we use different models to answer questions in different languages. The team consists of three specialized agents and the team leader routes the user’s question to the appropriate language agent.

multilanguage\_team.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agno.models.mistral.mistral import MistralChat
from agno.models.openai import OpenAIChat
from agno.team.team import Team

english_agent = Agent(
    name="English Agent",
    role="You only answer in English",
    model=OpenAIChat(id="gpt-4o"),
)
chinese_agent = Agent(
    name="Chinese Agent",
    role="You only answer in Chinese",
    model=DeepSeek(id="deepseek-chat"),
)
french_agent = Agent(
    name="French Agent",
    role="You can only answer in French",
    model=MistralChat(id="mistral-large-latest"),
)

multi_language_team = Team(
    name="Multi Language Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[english_agent, chinese_agent, french_agent],
    show_tool_calls=True,
    markdown=True,
    description="You are a language router that directs questions to the appropriate language agent.",
    instructions=[
        "Identify the language of the user's question and direct it to the appropriate language agent.",
        "If the user asks in a language whose agent is not a team member, respond in English with:",
        "'I can only answer in the following languages: English, Chinese, French. Please ask your question in one of these languages.'",
        "Always check the language of the user's input before routing to an agent.",
        "For unsupported languages like Italian, respond in English with the above message.",
    ],
    show_members_responses=True,
)


if __name__ == "__main__":
    # Ask "How are you?" in all supported languages
    multi_language_team.print_response("Comment allez-vous?", stream=True)  # French
    multi_language_team.print_response("How are you?", stream=True)  # English
    multi_language_team.print_response("你好吗？", stream=True)  # Chinese
    multi_language_team.print_response("Come stai?", stream=True)  # Italian

```

[​](#team-memory-and-history) Team Memory and History
-----------------------------------------------------

Teams can maintain memory of previous interactions, enabling contextual awareness:

Copy

Ask AI

```
from agno.team import Team

team_with_memory = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    add_history_to_messages=True,
    num_history_runs=5,
)

# The team will remember previous interactions
team_with_memory.print_response("What are the key challenges in quantum computing?")
team_with_memory.print_response("Elaborate on the second challenge you mentioned")

```

The team can also manage user memories:

Copy

Ask AI

```
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

# Create a memory instance with persistent storage
memory_db = SqliteMemoryDb(table_name="memory", db_file="memory.db")
memory = Memory(db=memory_db)

team_with_memory = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    memory=memory,
    enable_agentic_memory=True,
)

team_with_memory.print_response("Hi! My name is John Doe.")
team_with_memory.print_response("What is my name?")

```

[​](#session-summaries) Session Summaries
-----------------------------------------

To enable session summaries, set `enable_session_summaries=True` on the `Team`.

Copy

Ask AI

```
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

team_with_session_summaries = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    enable_session_summaries=True,
)

team_with_session_summaries.print_response("Hi! My name is John Doe and I live in New York City.")

session_summary = team_with_session_summaries.get_session_summary()
print("Session Summary: ", session_summary.summary)

```

[​](#team-knowledge) Team Knowledge
-----------------------------------

Teams can use a knowledge base to store and retrieve information:

Copy

Ask AI

```
from pathlib import Path

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType

# Setup paths
cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

# Initialize knowledge base
agno_docs_knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/llms-full.txt"],
    vector_db=LanceDb(
        uri=str(tmp_dir.joinpath("lancedb")),
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
)

team_with_knowledge = Team(
    name="Team with Knowledge",
    members=[web_agent],
    model=OpenAIChat(id="gpt-4o"),
    knowledge=agno_docs_knowledge,
    show_members_responses=True,
    markdown=True,
)

if __name__ == "__main__":
    # Set to False after the knowledge base is loaded
    load_knowledge = True
    if load_knowledge:
        agno_docs_knowledge.load()

    team_with_knowledge.print_response("Tell me about the Agno framework", stream=True)

```

The team can also manage user memories:

Copy

Ask AI

```
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

# Create a memory instance with persistent storage
memory_db = SqliteMemoryDb(table_name="memory", db_file="memory.db")
memory = Memory(db=memory_db)

team_with_memory = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    memory=memory,
    enable_user_memories=True,
)

team_with_memory.print_response("Hi! My name is John Doe.")
team_with_memory.print_response("What is my name?")

```

[​](#examples) Examples
-----------------------

### [​](#content-team) Content Team

Let’s walk through another example where we use two specialized agents to write a blog post. The team leader coordinates the agents to write a blog post.

content\_team.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools

# Create individual specialized agents
researcher = Agent(
    name="Researcher",
    role="Expert at finding information",
    tools=[DuckDuckGoTools()],
    model=OpenAIChat("gpt-4o"),
)

writer = Agent(
    name="Writer",
    role="Expert at writing clear, engaging content",
    model=OpenAIChat("gpt-4o"),
)

# Create a team with these agents
content_team = Team(
    name="Content Team",
    mode="coordinate",
    members=[researcher, writer],
    instructions="You are a team of researchers and writers that work together to create high-quality content.",
    model=OpenAIChat("gpt-4o"),
    markdown=True,
)

# Run the team with a task
content_team.print_response("Create a short article about quantum computing")

```

### [​](#research-team) Research Team

Here’s an example of a research team that combines multiple specialized agents:

1

Create HackerNews Team

Create a file `hackernews_team.py`

hackernews\_team.py

Copy

Ask AI

```
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from pydantic import BaseModel

class Article(BaseModel):
    title: str
    summary: str
    reference_links: List[str]


hn_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

article_reader = Agent(
    name="Article Reader",
    role="Reads articles from URLs.",
    tools=[Newspaper4kTools()],
)

hackernews_team = Team(
    name="HackerNews Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[hn_researcher, web_searcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the article reader to read the links for the stories to get more information.",
        "Important: you must provide the article reader with the links to read.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    response_model=Article,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
)

# Run the team
report = hackernews_team.run(
    "What are the top stories on hackernews?"
).content

print(f"Title: {report.title}")
print(f"Summary: {report.summary}")
print(f"Reference Links: {report.reference_links}")

```

2

Run the team

Install libraries

Copy

Ask AI

```
pip install openai duckduckgo-search newspaper4k lxml_html_clean agno

```

Run the team

Copy

Ask AI

```
python hackernews_team.py

```

[​](#developer-resources) Developer Resources
---------------------------------------------

* View [Usecases](/examples/teams)
* View [Examples](/examples/concepts/storage/team_storage)
* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/examples/teams)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/teams/introduction.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /teams/introduction)

[Agent Teams [Deprecated]](/agents/teams)[Running your Team](/teams/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Example](#example)
* [Team Memory and History](#team-memory-and-history)
* [Session Summaries](#session-summaries)
* [Team Knowledge](#team-knowledge)
* [Examples](#examples)
* [Content Team](#content-team)
* [Research Team](#research-team)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
