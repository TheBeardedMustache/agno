Cerebras OpenAI - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Cerebras

Cerebras OpenAI

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

    - [Cerebras](/models/cerebras)
    - [Cerebras OpenAI](/models/cerebras_openai)
  + [Cohere](/models/cohere)
  + [DeepInfra](/models/deepinfra)
  + [DeepSeek](/models/deepseek)
  + [Fireworks](/models/fireworks)
  + [Gemini](/models/google)
  + [Groq](/models/groq)
  + [HuggingFace](/models/huggingface)
  + [IBM WatsonX](/models/ibm-watsonx)
  + LiteLLM
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

Cerebras

Copy page

Cerebras OpenAI
===============

Learn how to use Cerebras OpenAI with Agno.

[​](#openai-compatible-integration) OpenAI-Compatible Integration
-----------------------------------------------------------------

Cerebras can also be used via an OpenAI-compatible interface, making it easy to integrate with tools and libraries that expect the OpenAI API.

### [​](#using-the-openai-compatible-class) Using the OpenAI-Compatible Class

The `CerebrasOpenAI` class provides an OpenAI-style interface for Cerebras models:

First, install openai:

Copy

Ask AI

```
pip install openai

```

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.cerebras import CerebrasOpenAI

agent = Agent(
    model=CerebrasOpenAI(
        id="llama-4-scout-17b-16e-instruct",  # Model ID to use
        # base_url="https://api.cerebras.ai", # Optional: default endpoint for Cerebras
    ),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("write a two sentence horror story")

```

### [​](#configuration-options) Configuration Options

The `CerebrasOpenAI` class accepts the following parameters:

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `id` | str | Model identifier (e.g., “llama-4-scout-17b-16e-instruct”) | **Required** |
| `name` | str | Display name for the model | ”Cerebras” |
| `provider` | str | Provider name | ”Cerebras” |
| `api_key` | str | API key (falls back to CEREBRAS\_API\_KEY environment variable) | None |
| `base_url` | str | URL of the Cerebras OpenAI-compatible endpoint | ”<https://api.cerebras.ai>” |

### [​](#examples) Examples

* View more examples [here](../examples/models/cerebras_openai).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/cerebras_openai.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/cerebras_openai)

[Cerebras](/models/cerebras)[Cohere](/models/cohere)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [OpenAI-Compatible Integration](#openai-compatible-integration)
* [Using the OpenAI-Compatible Class](#using-the-openai-compatible-class)
* [Configuration Options](#configuration-options)
* [Examples](#examples)

Assistant

Responses are generated using AI and may contain mistakes.
