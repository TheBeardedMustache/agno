Multi Agent Systems - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Introduction

Multi Agent Systems

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

Introduction

Copy page

Multi Agent Systems
===================

Teams of Agents working together towards a common goal.

[​](#level-4%3A-agent-teams-that-can-reason-and-collaborate) Level 4: Agent Teams that can reason and collaborate
-----------------------------------------------------------------------------------------------------------------

Agents are the atomic unit of work, and work best when they have a narrow scope and a small number of tools. When the number of tools grows beyond what the model can handle or you need to handle multiple concepts, use a team of agents to spread the load.

Agno provides an industry leading multi-agent architecture that allows you to build Agent Teams that can reason, collaborate and coordinate. In this example, we’ll build a team of 2 agents to analyze the semiconductor market performance, reasoning step by step.

level\_4\_team.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests and general research",
    model=OpenAIChat(id="gpt-4.1"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    add_datetime_to_instructions=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Handle financial data requests and market analysis",
    model=OpenAIChat(id="gpt-4.1"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True,analyst_recommendations=True, company_info=True)],
    instructions=[
        "Use tables to display stock prices, fundamentals (P/E, Market Cap), and recommendations.",
        "Clearly state the company name and ticker symbol.",
        "Focus on delivering actionable financial insights.",
    ],
    add_datetime_to_instructions=True,
)

reasoning_finance_team = Team(
    name="Reasoning Finance Team",
    mode="coordinate",
    model=Claude(id="claude-sonnet-4-20250514"),
    members=[web_agent, finance_agent],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Collaborate to provide comprehensive financial and investment insights",
        "Consider both fundamental analysis and market sentiment",
        "Use tables and charts to display data clearly and professionally",
        "Present findings in a structured, easy-to-follow format",
        "Only output the final consolidated analysis, not individual agent responses",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has provided a complete financial analysis with data, visualizations, risk assessment, and actionable investment recommendations supported by quantitative analysis and market research.",
)

if __name__ == "__main__":
    reasoning_finance_team.print_response("""Compare the tech sector giants (AAPL, GOOGL, MSFT) performance:
        1. Get financial data for all three companies
        2. Analyze recent news affecting the tech sector
        3. Calculate comparative metrics and correlations
        4. Recommend portfolio allocation weights""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

```

Install dependencies and run the Agent team

1

Install dependencies

Mac

Windows

Copy

Ask AI

```
uv pip install -U agno anthropic openai duckduckgo-search yfinance

```

2

Export your API keys

Mac

Windows

Copy

Ask AI

```
export ANTHROPIC_API_KEY=sk-***
export OPENAI_API_KEY=sk-***

```

3

Run the agent team

Copy

Ask AI

```
python level_4_team.py

```

[​](#level-5%3A-agentic-workflows-with-state-and-determinism) Level 5: Agentic Workflows with state and determinism
-------------------------------------------------------------------------------------------------------------------

Workflows are deterministic, stateful, multi-agent programs built for production applications. We write the workflow in pure python, giving us extreme control over the execution flow.

Having built 100s of agentic systems, **no framework or step based approach will give you the flexibility and reliability of pure-python**. Want loops - use while/for, want conditionals - use if/else, want exceptional handling - use try/except.

Because the workflow logic is a python function, AI code editors can vibe code workflows for you.

Add `https://docs.agno.com` as a document source and vibe away.

Here’s a simple workflow that caches previous outputs, you control every step: what gets cached, what gets streamed, what gets logged and what gets returned.

level\_5\_workflow.py

Copy

Ask AI

```
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow


class CacheWorkflow(Workflow):
    # Add agents or teams as attributes on the workflow
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

    # Write the logic in the `run()` method
    def run(self, message: str) -> Iterator[RunResponse]:
        logger.info(f"Checking cache for '{message}'")
        # Check if the output is already cached
        if self.session_state.get(message):
            logger.info(f"Cache hit for '{message}'")
            yield RunResponse(
                run_id=self.run_id, content=self.session_state.get(message)
            )
            return

        logger.info(f"Cache miss for '{message}'")
        # Run the agent and yield the response
        yield from self.agent.run(message, stream=True)

        # Cache the output after response is yielded
        self.session_state[message] = self.agent.run_response.content


if __name__ == "__main__":
    workflow = CacheWorkflow()
    # Run workflow (this is takes ~1s)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)
    # Run workflow again (this is immediate because of caching)
    response: Iterator[RunResponse] = workflow.run(message="Tell me a joke.")
    # Print the response
    pprint_run_response(response, markdown=True, show_time=True)

```

Run the workflow

Copy

Ask AI

```
python level_5_workflow.py

```

[​](#next) Next
---------------

* Checkout the [Agent Playground](/introduction/playground) to interact with your Agents, Teams and Workflows.
* Learn how to [Monitor](/introduction/monitoring) your Agents, Teams and Workflows.
* Get help from the [Community](/introduction/community).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/introduction/multi-agent-systems.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /introduction/multi-agent-systems)

[Your first Agents](/introduction/agents)[Playground](/introduction/playground)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Level 4: Agent Teams that can reason and collaborate](#level-4%3A-agent-teams-that-can-reason-and-collaborate)
* [Level 5: Agentic Workflows with state and determinism](#level-5%3A-agentic-workflows-with-state-and-determinism)
* [Next](#next)

Assistant

Responses are generated using AI and may contain mistakes.
