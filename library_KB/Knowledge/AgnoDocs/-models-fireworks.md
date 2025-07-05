Fireworks - Agno

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

Fireworks

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

Fireworks
=========

Learn how to use Fireworks models in Agno.

Fireworks is a platform for providing endpoints for Large Language models.

[​](#authentication) Authentication
-----------------------------------

Set your `FIREWORKS_API_KEY` environment variable. Get your key from [here](https://fireworks.ai/account/api-keys).

Mac

Windows

Copy

Ask AI

```
export FIREWORKS_API_KEY=***

```

[​](#prompt-caching) Prompt caching
-----------------------------------

Prompt caching will happen automatically using our `Fireworks` model. You can read more about how Fireworks handle caching in [their docs](https://docs.fireworks.ai/guides/prompt-caching#using-prompt-caching).

[​](#example) Example
---------------------

Use `Fireworks` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.fireworks import Fireworks

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/firefunction-v2"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/fireworks).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"accounts/fireworks/models/llama-v3p1-405b-instruct"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Fireworks: {id}"` | The name identifier for the agent. Defaults to "Fireworks: " followed by the model ID. |
| `provider` | `str` | `"Fireworks"` | The provider of the model. |
| `api_key` | `Optional[str]` | - | The API key for authenticating requests to the service. Retrieved from the environment variable FIREWORKS\_API\_KEY. |
| `base_url` | `str` | `"https://api.fireworks.ai/inference/v1"` | The base URL for making API requests to the Fireworks service. |

`Fireworks` also supports the params of [OpenAI](/reference/models/openai).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/fireworks.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/fireworks)

[DeepSeek](/models/deepseek)[Gemini](/models/google)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Prompt caching](#prompt-caching)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
