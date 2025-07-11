﻿User Control Flows - Agno

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

User Control Flows

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

User Control Flows
==================

Learn how to control the flow of an agent’s execution in Agno. This is also called “Human in the Loop”.

User control flows in Agno enable you to implement “Human in the Loop” patterns, where human oversight and input are required during agent execution. This is crucial for:

* Validating sensitive operations
* Reviewing tool calls before execution
* Gathering user input for decision-making
* Managing external tool execution

[​](#types-of-user-control-flows) Types of User Control Flows
-------------------------------------------------------------

Agno supports four main types of user control flows:

1. **User Confirmation**: Require explicit user approval before executing tool calls
2. **User Input**: Gather specific information from users during execution
3. **Dynamic User Input**: Have the agent collect user input as it needs it
4. **External Tool Execution**: Execute tools outside of the agent’s control

[​](#pausing-agent-execution) Pausing Agent Execution
-----------------------------------------------------

User control flows interrupt the agent’s execution and require human oversight. The run can then be continued by calling the `continue_run` method.

For example:

Copy

Ask AI

```
agent.run("Perform sensitive operation")

if agent.is_paused:
    # The agent will pause while human input is provided
    # ... perform other tasks

    # The user can then continue the run
    response = agent.continue_run()
    # or response = await agent.acontinue_run()

```

The `continue_run` method continues with the state of the agent at the time of the pause. You can also pass the `run_response` of a specific run to the `continue_run` method, or the `run_id`.

[​](#user-confirmation) User Confirmation
-----------------------------------------

User confirmation allows you to pause execution and require explicit user approval before proceeding with tool calls. This is useful for:

* Sensitive operations
* API calls that modify data
* Actions with significant consequences

The following example shows how to implement user confirmation.

Copy

Ask AI

```
from agno.tools import tool
from agno.agent import Agent
from agno.models.openai import OpenAIChat

@tool(requires_confirmation=True)
def sensitive_operation(data: str) -> str:
    """Perform a sensitive operation that requires confirmation."""
    # Implementation here
    return "Operation completed"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[sensitive_operation],
)

# Run the agent
agent.run("Perform sensitive operation")

# Handle confirmation
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_confirmation:
        # Get user confirmation
        print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
        confirmed = input(f"Confirm? (y/n): ").lower() == "y"
        tool.confirmed = confirmed

  # Continue execution
  response = agent.continue_run()

```

You can also specify which tools in a toolkit require confirmation.

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.yfinance import YFinanceTools
from agno.utils import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(requires_confirmation_tools=["get_current_stock_price"])],
)

agent.run("What is the current stock price of Apple?")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_confirmation:
        print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
        confirmed = input(f"Confirm? (y/n): ").lower() == "y"

        if message == "n":
            tool.confirmed = False
        else:
            # We update the tools in place
            tool.confirmed = True

    run_response = agent.continue_run()
    pprint.pprint_run_response(run_response)

```

[​](#user-input) User Input
---------------------------

User input flows allow you to gather specific information from users during execution. This is useful for:

* Collecting required parameters
* Getting user preferences
* Gathering missing information

In the example below, we require all the input for the `send_email` tool from the user.

Copy

Ask AI

```
from typing import List
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.function import UserInputField

# We still provide a docstring to the tool; This will be used to populate the `user_input_schema`
@tool(requires_user_input=True)
def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email to the user.

    Args:
        to (str): The address to send the email to.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    # Implementation here
    return f"Email sent to {to} with subject {subject} and body {body}"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[send_email],
)

agent.run("Send an email please")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_user_input:
        input_schema: List[UserInputField] = tool.user_input_schema

        for field in input_schema:
            # Display field information to the user
            print(f"\nField: {field.name} ({field.field_type.__name__}) -> {field.description}")

            # Get user input
            user_value = input(f"Please enter a value for {field.name}: ")

            # Update the field value
            field.value = user_value

    run_response = (
        agent.continue_run()
    )

```

The `RunResponse` object has a list of tools and in the case of `requires_user_input`, the tools that require input will have `user_input_schema` populated.
This is a list of `UserInputField` objects.

Copy

Ask AI

```
class UserInputField:
    name: str  # The name of the field
    field_type: Type  # The required type of the field
    description: Optional[str] = None  # The description of the field
    value: Optional[Any] = None  # The value of the field. Populated by the agent or the user.

```

You can also specify which fields should be filled by the user while the agent will provide the rest of the fields.

Copy

Ask AI

```

# You can either specify the user_input_fields leave empty for all fields to be provided by the user
@tool(requires_user_input=True, user_input_fields=["to_address"])
def send_email(subject: str, body: str, to_address: str) -> str:
    """
    Send an email.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_address (str): The address to send the email to.
    """
    return f"Sent email to {to_address} with subject {subject} and body {body}"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[send_email],
)

agent.run("Send an email with the subject 'Hello' and the body 'Hello, world!'")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_user_input:
        input_schema: List[UserInputField] = tool.user_input_schema

        for field in input_schema:
            # Display field information to the user
            print(f"\nField: {field.name} ({field.field_type.__name__}) -> {field.description}")

            # Get user input (if the value is not set, it means the user needs to provide the value)
            if field.value is None:
                user_value = input(f"Please enter a value for {field.name}: ")
                field.value = user_value
            else:
                print(f"Value provided by the agent: {field.value}")

    run_response = (
        agent.continue_run()
    )

```

[​](#dynamic-user-input) Dynamic User Input
-------------------------------------------

This pattern provides the agent with tools to indicate when it needs user input. It’s ideal for:

* Cases where it is unknown how the user will interact with the agent
* When you want a form-like interaction with the user

In the following example, we use a specialized tool to allow the agent to collect user feedback when it needs it.

Copy

Ask AI

```
from typing import Any, Dict

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.toolkit import Toolkit
from agno.tools.user_control_flow import UserControlFlowTools
from agno.utils import pprint

# Example toolkit for handling emails
class EmailTools(Toolkit):
    def __init__(self, *args, **kwargs):
        super().__init__(
            name="EmailTools", tools=[self.send_email, self.get_emails], *args, **kwargs
        )

    def send_email(self, subject: str, body: str, to_address: str) -> str:
        """Send an email to the given address with the given subject and body.

        Args:
            subject (str): The subject of the email.
            body (str): The body of the email.
            to_address (str): The address to send the email to.
        """
        return f"Sent email to {to_address} with subject {subject} and body {body}"

    def get_emails(self, date_from: str, date_to: str) -> str:
        """Get all emails between the given dates.

        Args:
            date_from (str): The start date.
            date_to (str): The end date.
        """
        return [
            {
                "subject": "Hello",
                "body": "Hello, world!",
                "to_address": "test@test.com",
                "date": date_from,
            },
            {
                "subject": "Random other email",
                "body": "This is a random other email",
                "to_address": "john@doe.com",
                "date": date_to,
            },
        ]


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[EmailTools(), UserControlFlowTools()],
    markdown=True,
    debug_mode=True,
)

run_response = agent.run("Send an email with the body 'How is it going in Tokyo?'")

# We use a while loop to continue the running until the agent is satisfied with the user input
while run_response.is_paused:
    for tool in run_response.tools_requiring_user_input:
        input_schema: List[UserInputField] = tool.user_input_schema

        for field in input_schema:
            # Display field information to the user
            print(f"\nField: {field.name} ({field.field_type.__name__}) -> {field.description}")

            # Get user input (if the value is not set, it means the user needs to provide the value)
            if field.value is None:
                user_value = input(f"Please enter a value for {field.name}: ")
                field.value = user_value
            else:
                print(f"Value provided by the agent: {field.value}")

    run_response = agent.continue_run(run_response=run_response)

    # If the agent is not paused for input, we are done
    if not run_response.is_paused:
        pprint.pprint_run_response(run_response)
        break

```

[​](#external-tool-execution) External Tool Execution
-----------------------------------------------------

External tool execution allows you to execute tools outside of the agent’s control. This is useful for:

* External service calls
* Database operations

Copy

Ask AI

```
import subprocess

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.utils import pprint


# We have to create a tool with the correct name, arguments and docstring for the agent to know what to call.
@tool(external_execution=True)
def execute_shell_command(command: str) -> str:
    """Execute a shell command.

    Args:
        command (str): The shell command to execute

    Returns:
        str: The output of the shell command
    """
    return subprocess.check_output(command, shell=True).decode("utf-8")


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[execute_shell_command],
    markdown=True,
)

run_response = agent.run("What files do I have in my current directory?")
if run_response.is_paused:
    for tool in run_response.tools_awaiting_external_execution:
        if tool.tool_name == execute_shell_command.name:
            print(f"Executing {tool.tool_name} with args {tool.tool_args} externally")

            # We execute the tool ourselves. You can execute any function or process here and use the tool_args as input.
            result = execute_shell_command.entrypoint(**tool.tool_args)
            # We have to set the result on the tool execution object so that the agent can continue
            tool.result = result

    run_response = agent.continue_run()
    pprint.pprint_run_response(run_response)

```

[​](#best-practices) Best Practices
-----------------------------------

1. **Sanitise user input**: Always validate and sanitize user input to prevent security vulnerabilities.
2. **Error Handling**: Always implement proper error handling for user input and external calls
3. **Input Validation**: Validate user input before processing

[​](#developer-resources) Developer Resources
---------------------------------------------

* View more [Examples](/examples/concepts/user-control-flows)
* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/user_control_flows)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/user-control-flow.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/user-control-flow)

[Multimodal Agents](/agents/multimodal)[Prompts](/agents/prompts)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Types of User Control Flows](#types-of-user-control-flows)
* [Pausing Agent Execution](#pausing-agent-execution)
* [User Confirmation](#user-confirmation)
* [User Input](#user-input)
* [Dynamic User Input](#dynamic-user-input)
* [External Tool Execution](#external-tool-execution)
* [Best Practices](#best-practices)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
