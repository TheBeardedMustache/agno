DeepSeek - Agno

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

DeepSeek

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

DeepSeek
========

Learn how to use DeepSeek models in Agno.

DeepSeek is a platform for providing endpoints for Large Language models.
See their library of models [here](https://api-docs.deepseek.com/quick_start/pricing).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `deepseek-chat` model is good for most basic use-cases.
* `deepseek-reasoner` model is good for complex reasoning and multi-step tasks.

DeepSeek does not have rate limits. See their [docs](https://api-docs.deepseek.com/quick_start/rate_limit) for information about how to deal with slower responses during high traffic.

[​](#authentication) Authentication
-----------------------------------

Set your `DEEPSEEK_API_KEY` environment variable. Get your key from [here](https://platform.deepseek.com/api_keys).

Mac

Windows

Copy

Ask AI

```
export DEEPSEEK_API_KEY=***

```

[​](#example) Example
---------------------

Use `DeepSeek` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.deepseek import DeepSeek

agent = Agent(model=DeepSeek(), markdown=True)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/deepseek).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"deepseek-chat"` | The specific model ID used for generating responses. |
| `name` | `str` | `"DeepSeek"` | The name identifier for the DeepSeek model. |
| `provider` | `str` | `"DeepSeek"` | The provider of the model. |
| `api_key` | `Optional[str]` | - | The API key used for authenticating requests to the DeepSeek service. Retrieved from the environment variable `DEEPSEEK_API_KEY`. |
| `base_url` | `str` | `"https://api.deepseek.com"` | The base URL for making API requests to the DeepSeek service. |

`DeepSeek` also supports the params of [OpenAI](/reference/models/openai).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/deepseek.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/deepseek)

[DeepInfra](/models/deepinfra)[Fireworks](/models/fireworks)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
