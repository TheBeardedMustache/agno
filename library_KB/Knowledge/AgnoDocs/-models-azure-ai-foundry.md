Azure AI Foundry - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Azure

Azure AI Foundry

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

    - [Azure AI Foundry](/models/azure-ai-foundry)
    - [Azure OpenAI](/models/azure-openai)
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

Azure

Copy page

Azure AI Foundry
================

Learn how to use Azure AI Foundry models in Agno.

Use various open source models hosted on Azure’s infrastructure. Learn more [here](https://learn.microsoft.com/azure/ai-services/models).

Azure AI Foundry provides access to models like `Phi`, `Llama`, `Mistral`, `Cohere` and more.

[​](#authentication) Authentication
-----------------------------------

Navigate to Azure AI Foundry on the [Azure Portal](https://portal.azure.com/) and create a service. Then set your environment variables:

Mac

Windows

Copy

Ask AI

```
export AZURE_API_KEY=***
export AZURE_ENDPOINT=***  # Of the form https://<your-host-name>.<your-azure-region>.models.ai.azure.com/models
# Optional:
# export AZURE_API_VERSION=***

```

[​](#example) Example
---------------------

Use `AzureAIFoundry` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.azure import AzureAIFoundry

agent = Agent(
    model=AzureAIFoundry(id="Phi-4"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

[​](#advanced-examples) Advanced Examples
-----------------------------------------

View more examples [here](../examples/models/azure/ai_foundry).

[​](#parameters) Parameters
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | - | The specific model ID used for generating responses. This field is required. |
| `name` | `str` | `"AzureOpenAI"` | The name identifier for the agent. |
| `provider` | `str` | `"Azure"` | The provider of the model. |
| `api_key` | `Optional[str]` | `"None"` | The API key for authenticating requests to the Azure OpenAI service. |
| `api_version` | `str` | `"2024-10-21"` | The version of the Azure OpenAI API to use. |
| `azure_endpoint` | `Optional[str]` | `"None"` | The endpoint URL for the Azure OpenAI service. |
| `client` | `Optional[ChatCompletionsClient]` | `None` | The client for making requests to the Azure OpenAI service. |
| `async_client` | `Optional[AsyncChatCompletionsClient]` | `None` | The asynchronous client for making requests to the Azure OpenAI service. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output. Higher values make output more random. |
| `max_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `frequency_penalty` | `Optional[float]` | `None` | Reduces repetition by penalizing tokens based on their frequency. |
| `presence_penalty` | `Optional[float]` | `None` | Reduces repetition by penalizing tokens that have appeared at all. |
| `top_p` | `Optional[float]` | `None` | Controls diversity by limiting cumulative probability of tokens considered. |
| `stop` | `Optional[Union[str, List[str]]]` | `None` | Sequences where the model will stop generating further tokens. |
| `seed` | `Optional[int]` | `None` | Random seed for deterministic outputs. |
| `model_extras` | `Optional[Dict[str, Any]]` | `None` | Additional model-specific parameters. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to pass with the request. |
| `timeout` | `Optional[float]` | `None` | Timeout in seconds for API requests. |
| `max_retries` | `Optional[int]` | `None` | Maximum number of retries for failed requests. |
| `http_client` | `Optional[httpx.Client]` | `None` | Custom HTTP client for making requests. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration. |

`AzureAIFoundry` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/azure-ai-foundry.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/azure-ai-foundry)

[AWS Claude](/models/aws-claude)[Azure OpenAI](/models/azure-openai)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Advanced Examples](#advanced-examples)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
