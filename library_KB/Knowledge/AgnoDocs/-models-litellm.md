LiteLLM - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

LiteLLM

LiteLLM

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

  + [Overview](/models/introduction)
  + [Models Compatibility](/models/compatibility)
  + [OpenAI Like](/models/openai-like)
  + [AI/ML API](/models/aimlapi)
  + [Anthropic Claude](/models/anthropic)
  + AWS
  + Azure
  + Cerebras
  + [Cohere](/models/cohere)
  + [DeepInfra](/models/deepinfra)
  + [DeepSeek](/models/deepseek)
  + [Fireworks](/models/fireworks)
  + [Gemini](/models/google)
  + [Groq](/models/groq)
  + [HuggingFace](/models/huggingface)
  + [IBM WatsonX](/models/ibm-watsonx)
  + LiteLLM

    - [LiteLLM](/models/litellm)
    - [LiteLLM OpenAI](/models/litellm_openai)
  + [LM Studio](/models/lmstudio)
  + [Meta](/models/meta)
  + [Mistral](/models/mistral)
  + [Nvidia](/models/nvidia)
  + [Nebius](/models/nebius)
  + [Ollama](/models/ollama)
  + [OpenAI](/models/openai)
  + [OpenAI Responses](/models/openai-responses)
  + [OpenRouter](/models/openrouter)
  + [Perplexity](/models/perplexity)
  + [Sambanova](/models/sambanova)
  + [Together](/models/together)
  + [Vercel v0](/models/vercel)
  + [vLLM](/models/vllm)
  + [xAI](/models/xai)
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

LiteLLM

Copy page

LiteLLM
=======

Integrate LiteLLM with Agno for a unified LLM experience.

[LiteLLM](https://docs.litellm.ai/docs/) provides a unified interface for various LLM providers, allowing you to use different models with the same code.

Agno integrates with LiteLLM in two ways:

1. **Direct SDK integration** - Using the LiteLLM Python SDK
2. **Proxy Server integration** - Using LiteLLM as an OpenAI-compatible proxy

[​](#prerequisites) Prerequisites
---------------------------------

For both integration methods, you’ll need:

Copy

Ask AI

```
# Install required packages
pip install agno litellm

```

Set up your API key:
Regardless of the model used(OpenAI, Hugging Face, or XAI) the API key is referenced as `LITELLM_API_KEY`.

Copy

Ask AI

```
export LITELLM_API_KEY=your_api_key_here

```

[​](#sdk-integration) SDK Integration
-------------------------------------

The `LiteLLM` class provides direct integration with the LiteLLM Python SDK.

### [​](#basic-usage) Basic Usage

Copy

Ask AI

```
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

### [​](#using-hugging-face-models) Using Hugging Face Models

LiteLLM can also work with Hugging Face models:

Copy

Ask AI

```
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

### [​](#configuration-options) Configuration Options

The `LiteLLM` class accepts the following parameters:

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `id` | str | Model identifier (e.g., “gpt-4o” or “huggingface/mistralai/Mistral-7B-Instruct-v0.2”) | “gpt-4o” |
| `name` | str | Display name for the model | ”LiteLLM” |
| `provider` | str | Provider name | ”LiteLLM” |
| `api_key` | Optional[str] | API key (falls back to LITELLM\_API\_KEY environment variable) | None |
| `api_base` | Optional[str] | Base URL for API requests | None |
| `max_tokens` | Optional[int] | Maximum tokens in the response | None |
| `temperature` | float | Sampling temperature | 0.7 |
| `top_p` | float | Top-p sampling value | 1.0 |
| `request_params` | Optional[Dict[str, Any]] | Additional request parameters | None |

### [​](#sdk-examples) SDK Examples

View more examples [here](../examples/models/litellm).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/litellm.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/litellm)

[IBM WatsonX](/models/ibm-watsonx)[LiteLLM OpenAI](/models/litellm_openai)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Prerequisites](#prerequisites)
* [SDK Integration](#sdk-integration)
* [Basic Usage](#basic-usage)
* [Using Hugging Face Models](#using-hugging-face-models)
* [Configuration Options](#configuration-options)
* [SDK Examples](#sdk-examples)

Assistant

Responses are generated using AI and may contain mistakes.
