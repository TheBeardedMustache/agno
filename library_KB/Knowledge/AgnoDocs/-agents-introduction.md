What are Agents? - Agno

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

What are Agents?

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

What are Agents?
================

Learn about Agno Agents and how they work.

**Agents** are AI programs that operate autonomously. Traditional software follows a pre-programmed sequence of steps. Agents dynamically determine their course of action using a machine learning **model**.

The core of an Agent is the **model**, **tools** and **instructions**:

* **Model:** controls the flow of execution. It decides whether to reason, act or respond.
* **Tools:** enable an Agent to take actions and interact with external systems.
* **Instructions:** are how we program the Agent, teaching it how to use tools and respond.

Agents also have **memory**, **knowledge**, **storage** and the ability to **reason**:

* **Reasoning:** enables Agents to “think” before responding and “analyze” the results of their actions (i.e. tool calls), this improves reliability and quality of responses.
* **Knowledge:** is domain-specific information that the Agent can **search at runtime** to make better decisions and provide accurate responses (RAG). Knowledge is stored in a vector database and this **search at runtime** pattern is known as Agentic RAG/Agentic Search.
* **Storage:** is used by Agents to save session history and state in a database. Model APIs are stateless and storage enables us to continue conversations from where they left off. This makes Agents stateful, enabling multi-turn, long-term conversations.
* **Memory:** gives Agents the ability to store and recall information from previous interactions, allowing them to learn user preferences and personalize their responses.

If this is your first time building agents, [follow these examples](/introduction/agents#basic-agent) before diving into advanced concepts.

[​](#example%3A-research-agent) Example: Research Agent
-------------------------------------------------------

Let’s build a research agent using Exa to showcase how to guide the Agent to produce the report in a specific format. In advanced cases, we should use [Structured Outputs](/agents/structured-output) instead.

The description and instructions are converted to the system message and the
input is passed as the user message. Set `debug_mode=True` to view logs behind
the scenes.

1

Create Research Agent

Create a file `research_agent.py`

research\_agent.py

Copy

Ask AI

```
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""

```

2

Run the agent

Install libraries

Copy

Ask AI

```
pip install openai exa-py agno

```

Run the agent

Copy

Ask AI

```
python research_agent.py

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/introduction.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/introduction)

[Community & Support](/introduction/community)[Running your Agent](/agents/run)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Example: Research Agent](#example%3A-research-agent)

Assistant

Responses are generated using AI and may contain mistakes.
