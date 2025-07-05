DeepInfra - Agno

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

DeepInfra

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

DeepInfra
=========

Learn how to use DeepInfra models in Agno.

Leverage DeepInfra’s powerful command models and more.

[DeepInfra](https://deepinfra.com) supports a wide range of models. See their library of models [here](https://deepinfra.com/models).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `deepseek-ai/DeepSeek-R1-Distill-Llama-70B` model is good for reasoning.
* `meta-llama/Llama-2-70b-chat-hf` model is good for basic use-cases.
* `meta-llama/Llama-3.3-70B-Instruct` model is good for multi-step tasks.

DeepInfra has rate limits. See the [docs](https://deepinfra.com/docs/advanced/rate-limits) for more information.

[​](#authentication) Authentication
-----------------------------------

Set your `DEEPINFRA_API_KEY` environment variable. Get your key from [here](https://deepinfra.com/dash/api_keys).

Mac

Windows

Copy

Ask AI

```
export DEEPINFRA_API_KEY=***

```

[​](#example) Example
---------------------

Use `DeepInfra` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.deepinfra import DeepInfra

agent = Agent(
    model=DeepInfra(id="meta-llama/Llama-2-70b-chat-hf"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/deepinfra).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"meta-llama/Llama-2-70b-chat-hf"` | The specific model ID used for generating responses. |
| `name` | `str` | `"DeepInfra"` | The name identifier for the DeepInfra agent. |
| `provider` | `str` | `"DeepInfra" + id` | The provider of the model, combining "DeepInfra" with the model ID. |
| `api_key` | `Optional[str]` | - | The API key for authenticating requests to the DeepInfra service. Retrieved from the environment variable `DEEPINFRA_API_KEY`. |
| `base_url` | `str` | `"https://api.deepinfra.com/v1/openai"` | The base URL for making API requests to the DeepInfra service. |

`DeepInfra` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/deepinfra.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/deepinfra)

[Cohere](/models/cohere)[DeepSeek](/models/deepseek)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
