# LiteLLM

> Integrate LiteLLM with Agno for a unified LLM experience.

[LiteLLM](https://docs.litellm.ai/docs/) provides a unified interface for various LLM providers, allowing you to use different models with the same code.

Agno integrates with LiteLLM in two ways:

1. **Direct SDK integration** - Using the LiteLLM Python SDK
2. **Proxy Server integration** - Using LiteLLM as an OpenAI-compatible proxy

## Prerequisites

For both integration methods, you'll need:

```shell
# Install required packages
pip install agno litellm
```

Set up your API key:
Regardless of the model used(OpenAI, Hugging Face, or XAI) the API key is referenced as `LITELLM_API_KEY`.

```shell
export LITELLM_API_KEY=your_api_key_here
```

## SDK Integration

The `LiteLLM` class provides direct integration with the LiteLLM Python SDK.

### Basic Usage

```python
from agno.agent import Agent
from agno.models.litellm import LiteLLM

# Create an agent with GPT-4o
agent = Agent(
    model=LiteLLM(
        id="gpt-4o",  # Model ID to use
        name="LiteLLM",  # Optional display name
    ),
    markdown=True,
)

# Get a response
agent.print_response("Share a 2 sentence horror story")
```

### Using Hugging Face Models

LiteLLM can also work with Hugging Face models:

```python
from agno.agent import Agent
from agno.models.litellm import LiteLLM

agent = Agent(
    model=LiteLLM(
        id="huggingface/mistralai/Mistral-7B-Instruct-v0.2",
        top_p=0.95,
    ),
    markdown=True,
)

agent.print_response("What's happening in France?")
```

### Configuration Options

The `LiteLLM` class accepts the following parameters:

| Parameter        | Type                       | Description                                                                           | Default   |
| ---------------- | -------------------------- | ------------------------------------------------------------------------------------- | --------- |
| `id`             | str                        | Model identifier (e.g., "gpt-4o" or "huggingface/mistralai/Mistral-7B-Instruct-v0.2") | "gpt-4o"  |
| `name`           | str                        | Display name for the model                                                            | "LiteLLM" |
| `provider`       | str                        | Provider name                                                                         | "LiteLLM" |
| `api_key`        | Optional\[str]             | API key (falls back to LITELLM\_API\_KEY environment variable)                        | None      |
| `api_base`       | Optional\[str]             | Base URL for API requests                                                             | None      |
| `max_tokens`     | Optional\[int]             | Maximum tokens in the response                                                        | None      |
| `temperature`    | float                      | Sampling temperature                                                                  | 0.7       |
| `top_p`          | float                      | Top-p sampling value                                                                  | 1.0       |
| `request_params` | Optional\[Dict\[str, Any]] | Additional request parameters                                                         | None      |

### SDK Examples

<Note> View more examples [here](../examples/models/litellm). </Note>
