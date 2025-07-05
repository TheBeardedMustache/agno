HuggingFace - Agno

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

HuggingFace

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

HuggingFace
===========

Learn how to use HuggingFace models in Agno.

Hugging Face provides a wide range of state-of-the-art language models tailored to diverse NLP tasks,
including text generation, summarization, translation, and question answering.
These models are available through the Hugging Face Transformers library and are widely
adopted due to their ease of use, flexibility, and comprehensive documentation.

Explore HuggingFace’s language models [here](https://huggingface.co/docs/text-generation-inference/en/supported_models).

[​](#authentication) Authentication
-----------------------------------

Set your `HF_TOKEN` environment. You can get one [from HuggingFace here](https://huggingface.co/settings/tokens).

Mac

Windows

Copy

Ask AI

```
export HF_TOKEN=***

```

[​](#example) Example
---------------------

Use `HuggingFace` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.huggingface import HuggingFace

agent = Agent(
    model=HuggingFace(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=4096,
    ),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](../examples/models/huggingface).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"meta-llama/Meta-Llama-3-8B-Instruct"` | The id of the HuggingFace model to use. |
| `name` | `str` | `"HuggingFace"` | The name of this chat model instance. |
| `provider` | `str` | `"HuggingFace"` | The provider of the model. |
| `store` | `Optional[bool]` | `None` | Whether or not to store the output of this chat completion request for use in the model distillation or evals products. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `logit_bias` | `Optional[Any]` | `None` | Modifies the likelihood of specified tokens appearing in the completion. |
| `logprobs` | `Optional[bool]` | `None` | Include the log probabilities on the logprobs most likely tokens. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the chat completion. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `response_format` | `Optional[Any]` | `None` | An object specifying the format that the model must output. |
| `seed` | `Optional[int]` | `None` | A seed for deterministic sampling. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Up to 4 sequences where the API will stop generating further tokens. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. |
| `top_logprobs` | `Optional[int]` | `None` | How many log probability results to return per token. |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request. |
| `api_key` | `Optional[str]` | `None` | The Access Token for authenticating with HuggingFace. |
| `base_url` | `Optional[Union[str, httpx.URL]]` | `None` | The base URL for API requests. |
| `timeout` | `Optional[float]` | `None` | The timeout for API requests. |
| `max_retries` | `Optional[int]` | `None` | The maximum number of retries for failed requests. |
| `default_headers` | `Optional[Any]` | `None` | Default headers to include in all requests. |
| `default_query` | `Optional[Any]` | `None` | Default query parameters to include in all requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | An optional pre-configured HTTP client. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |
| `client` | `Optional[InferenceClient]` | `None` | The HuggingFace Hub Inference client instance. |
| `async_client` | `Optional[AsyncInferenceClient]` | `None` | The asynchronous HuggingFace Hub client instance. |

`HuggingFace` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/huggingface.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/huggingface)

[Groq](/models/groq)[IBM WatsonX](/models/ibm-watsonx)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
