Groq - Agno

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

Groq

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

Groq
====

Learn how to use Groq with Agno.

Groq offers blazing-fast API endpoints for large language models.

See all the Groq supported models [here](https://console.groq.com/docs/models).

* We recommend using `llama-3.3-70b-versatile` for general use
* We recommend `llama-3.1-8b-instant` for a faster result.
* We recommend using `llama-3.2-90b-vision-preview` for image understanding.

#### [​](#multimodal-support) Multimodal Support

With Groq we support `Image` as input

[​](#authentication) Authentication
-----------------------------------

Set your `GROQ_API_KEY` environment variable. Get your key from [here](https://console.groq.com/keys).

Mac

Windows

Copy

Ask AI

```
export GROQ_API_KEY=***

```

[​](#example) Example
---------------------

Use `Groq` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/groq).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"llama-3.3-70b-versatile"` | The specific model ID used for generating responses. |
| `name` | `str` | `"Groq"` | The name identifier for the agent. |
| `provider` | `str` | `"Groq"` | The provider of the model. |
| `frequency_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `logit_bias` | `Optional[Any]` | `None` | A JSON object that modifies the likelihood of specified tokens appearing in the completion by mapping token IDs to bias values between -100 and 100. |
| `logprobs` | `Optional[bool]` | `None` | Whether to return log probabilities of the output tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| `response_format` | `Optional[Dict[str, Any]]` | `None` | Specifies the format that the model must output. Setting to `{ "type": "json_object" }` enables JSON mode, ensuring the message generated is valid JSON. |
| `seed` | `Optional[int]` | `None` | A seed value for deterministic sampling, ensuring repeated requests with the same seed and parameters return the same result. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_logprobs` | `Optional[int]` | `None` | The number of top log probabilities to return for each generated token. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `user` | `Optional[str]` | `None` | A unique identifier representing your end-user, helping to monitor and detect abuse. |
| `extra_headers` | `Optional[Any]` | `None` | Additional headers to include in API requests. |
| `extra_query` | `Optional[Any]` | `None` | Additional query parameters to include in API requests. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating requests to the service. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for making API requests to the service. |
| `timeout` | `Optional[int]` | `None` | The timeout duration for requests, specified in seconds. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retry attempts for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all API requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all API requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | A custom HTTP client for making API requests. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[GroqClient]` | `None` | An instance of GroqClient provided for making API requests. |
| `async_client` | `Optional[AsyncGroqClient]` | `None` | An instance of AsyncGroqClient provided for making asynchronous API requests. |

`Groq` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/groq.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/groq)

[Gemini](/models/google)[HuggingFace](/models/huggingface)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Multimodal Support](#multimodal-support)
* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
