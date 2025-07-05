Cerebras - Agno

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

Cerebras

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

Cerebras
========

Learn how to use Cerebras models in Agno.

[Cerebras Inference](https://inference-docs.cerebras.ai/introduction) provides high-speed, low-latency AI model inference powered by Cerebras Wafer-Scale Engines and CS-3 systems. Agno integrates directly with the Cerebras Python SDK, allowing you to use state-of-the-art Llama models with a simple interface.

[​](#prerequisites) Prerequisites
---------------------------------

To use Cerebras with Agno, you need to:

1. **Install the required packages:**

   Copy

   Ask AI

   ```
   pip install cerebras-cloud-sdk

   ```
2. **Set your API key:**
   The Cerebras SDK expects your API key to be available as an environment variable:

   Copy

   Ask AI

   ```
   export CEREBRAS_API_KEY=your_api_key_here

   ```

[​](#basic-usage) Basic Usage
-----------------------------

Here’s how to use a Cerebras model with Agno:

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.cerebras import Cerebras

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("write a two sentence horror story")

```

[​](#supported-models) Supported Models
---------------------------------------

Cerebras currently supports the following models (see [docs](https://inference-docs.cerebras.ai/introduction) for the latest list):

| Model Name | Model ID | Parameters | Knowledge |
| --- | --- | --- | --- |
| Llama 4 Scout | llama-4-scout-17b-16e-instruct | 109 billion | August 2024 |
| Llama 3.1 8B | llama3.1-8b | 8 billion | March 2023 |
| Llama 3.3 70B | llama-3.3-70b | 70 billion | December 2023 |
| DeepSeek R1 Distill Llama 70B\* | deepseek-r1-distill-llama-70b | 70 billion | December 2023 |

\* DeepSeek R1 Distill Llama 70B is available in private preview.

[​](#configuration-options) Configuration Options
-------------------------------------------------

The `Cerebras` class accepts the following parameters:

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `id` | str | Model identifier (e.g., “llama-4-scout-17b-16e-instruct”) | **Required** |
| `name` | str | Display name for the model | ”Cerebras” |
| `provider` | str | Provider name | ”Cerebras” |
| `api_key` | Optional[str] | API key (falls back to `CEREBRAS_API_KEY` env var) | None |
| `max_tokens` | Optional[int] | Maximum tokens in the response | None |
| `temperature` | float | Sampling temperature | 0.7 |
| `top_p` | float | Top-p sampling value | 1.0 |
| `request_params` | Optional[Dict[str, Any]] | Additional request parameters | None |

[​](#resources) Resources
-------------------------

* [Cerebras Inference Documentation](https://inference-docs.cerebras.ai/introduction)
* [Cerebras API Reference](https://inference-docs.cerebras.ai/api-reference/chat-completions)

### [​](#sdk-examples) SDK Examples

* View more examples [here](../examples/models/cerebras).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/cerebras.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/cerebras)

[Azure OpenAI](/models/azure-openai)[Cerebras OpenAI](/models/cerebras_openai)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Prerequisites](#prerequisites)
* [Basic Usage](#basic-usage)
* [Supported Models](#supported-models)
* [Configuration Options](#configuration-options)
* [Resources](#resources)
* [SDK Examples](#sdk-examples)

Assistant

Responses are generated using AI and may contain mistakes.
