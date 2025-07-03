import random

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools import tool

agent1 = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
)

agent2 = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
)


@tool
def get_stock_price(stock_symbol: str) -> str:
    """Get the current stock price of a stock."""
    return f"The current stock price of {stock_symbol} is {random.randint(100, 1000)}."


team = Team(
    name="Stock Research Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[agent1, agent2],
    markdown=True,
    show_members_responses=True,
)


team.add_tool(get_stock_price)

team.print_response("What is the current stock price of NVDA?", stream=True)