Cohere - Agno

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

Cohere

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

Cohere
======

Learn how to use Cohere models in Agno.

Leverage Cohere’s powerful command models and more.

[Cohere](https://cohere.com) has a wide range of models and is really good for fine-tuning. See their library of models [here](https://docs.cohere.com/v2/docs/models).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `command` model is good for most basic use-cases.
* `command-light` model is good for smaller tasks and faster inference.
* `command-r7b-12-2024` model is good with RAG tasks, complex reasoning and multi-step tasks.

Cohere also supports fine-tuning models. Here is a [guide](https://docs.cohere.com/v2/docs/fine-tuning) on how to do it.

Cohere has tier-based rate limits. See the [docs](https://docs.cohere.com/v2/docs/rate-limits) for more information.

[​](#authentication) Authentication
-----------------------------------

Set your `CO_API_KEY` environment variable. Get your key from [here](https://dashboard.cohere.com/api-keys).

Mac

Windows

Copy

Ask AI

```
export CO_API_KEY=***

```

[​](#example) Example
---------------------

Use `Cohere` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.cohere import Cohere

agent = Agent(
    model=Cohere(id="command-r-08-2024"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/cohere).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"command-r-plus"` | The specific model ID used for generating responses. |
| `name` | `str` | `"cohere"` | The name identifier for the agent. |
| `provider` | `str` | `"Cohere"` | The provider of the model. |
| `temperature` | `Optional[float]` | `None` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `top_k` | `Optional[int]` | `None` | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `frequency_penalty` | `Optional[float]` | `None` | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `presence_penalty` | `Optional[float]` | `None` | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `add_chat_history` | `bool` | `False` | Whether to add chat history to the Cohere messages instead of using the conversation\_id. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating requests to the Cohere service. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `cohere_client` | `Optional[CohereClient]` | `None` | A pre-configured instance of the Cohere client. |
| `structured_outputs` | `bool` | `False` | Whether to use structured outputs with this Model. |
| `supports_structured_outputs` | `bool` | `True` | Whether the Model supports structured outputs. |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content. |
| `override_system_role` | `bool` | `True` | Whether to override the system role. |
| `system_message_role` | `str` | `"system"` | The role to map the system message to. |

`Cohere` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/cohere.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/cohere)

[Cerebras OpenAI](/models/cerebras_openai)[DeepInfra](/models/deepinfra)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
