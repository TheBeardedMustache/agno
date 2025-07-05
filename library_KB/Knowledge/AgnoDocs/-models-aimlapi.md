AI/ML API - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Models

AI/ML API

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

Models

Copy page

AI/ML API
=========

Learn how to use AI/ML API with Agno.

AI/ML API is a platform providing unified access to 300+ AI models including **Deepseek**, **Gemini**, **ChatGPT**, and more — with production-grade uptime and high rate limits.

[​](#authentication) Authentication
-----------------------------------

Set your `AIMLAPI_API_KEY` environment variable. Get your key at [aimlapi.com](https://aimlapi.com/?utm_source=agno&utm_medium=github&utm_campaign=integration).

Mac

Windows

Copy

Ask AI

```
export AIMLAPI_API_KEY=***

```

[​](#example) Example
---------------------

Use `AI/ML API` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.aimlapi import AIMLApi

agent = Agent(
    model=AIMLApi(id="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"),
    markdown=True,
)

agent.print_response("Explain how black holes are formed.")

```

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gpt-4o-mini"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AIMLApi"` | The name identifier for the AI/ML API agent. |
| `provider` | `str` | `"AIMLApi:" + id` | The provider of the model, combining `"AIMLApi"` with the model ID. |
| `api_key` | `Optional[str]` | – | The API key for authenticating requests to the AI/ML API service. Retrieved from the environment variable `AIMLAPI_API_KEY`. |
| `base_url` | `str` | `"https://api.aimlapi.com/v1"` | The base URL for making API requests to the AI/ML API service. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |

`AIMLApi` also supports the params of [OpenAI](/reference/models/openai), where applicable.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/aimlapi.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/aimlapi)

[OpenAI Like](/models/openai-like)[Anthropic Claude](/models/anthropic)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
