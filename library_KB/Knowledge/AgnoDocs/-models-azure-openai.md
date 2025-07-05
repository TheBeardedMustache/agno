Azure OpenAI - Agno

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

Azure OpenAI

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

Azure OpenAI
============

Learn how to use Azure OpenAI models in Agno.

Use OpenAI models through Azure’s infrastructure. Learn more [here](https://learn.microsoft.com/azure/ai-services/openai/overview).

Azure OpenAI provides access to OpenAI’s models like `GPT-4o`, `o3-mini`, and more.

[​](#authentication) Authentication
-----------------------------------

Navigate to Azure OpenAI on the [Azure Portal](https://portal.azure.com/) and create a service. Then, using the Azure AI Studio portal, create a deployment and set your environment variables:

Mac

Windows

Copy

Ask AI

```
export AZURE_OPENAI_API_KEY=***
export AZURE_OPENAI_ENDPOINT=***  # Of the form https://<your-resource-name>.openai.azure.com/openai/deployments/<your-deployment-name>
# Optional:
# export AZURE_OPENAI_DEPLOYMENT=***

```

[​](#example) Example
---------------------

Use `AzureOpenAI` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from os import getenv

agent = Agent(
    model=AzureOpenAI(id="gpt-4o"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

[​](#prompt-caching) Prompt caching
-----------------------------------

Prompt caching will happen automatically using our `AzureOpenAI` model. You can read more about how OpenAI handle caching in [their docs](https://platform.openai.com/docs/guides/prompt-caching).

[​](#advanced-examples) Advanced Examples
-----------------------------------------

View more examples [here](../examples/models/azure/openai).

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
| `azure_deployment` | `Optional[str]` | `"None"` | The deployment name or ID in Azure. |
| `azure_ad_token` | `Optional[str]` | `"None"` | The Azure Active Directory token for authenticating requests. |
| `azure_ad_token_provider` | `Optional[Any]` | `"None"` | The provider for obtaining Azure Active Directory tokens. |
| `openai_client` | `Optional[AzureOpenAIClient]` | `"None"` | An instance of AzureOpenAIClient provided for making API requests. |

`AzureOpenAI` also supports the parameters of [OpenAI](/reference/models/openai).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/azure-openai.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/azure-openai)

[Azure AI Foundry](/models/azure-ai-foundry)[Cerebras](/models/cerebras)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Prompt caching](#prompt-caching)
* [Advanced Examples](#advanced-examples)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
