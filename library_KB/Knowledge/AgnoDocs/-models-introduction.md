What are Models? - Agno

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

What are Models?

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

What are Models?
================

Language Models are machine-learning programs that are trained to understand natural language and code.

Models act as the **brain** of the Agent - helping it reason, act, and respond to the user. The better the model, the smarter the Agent.

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Share 15 minute healthy recipes.",
    markdown=True,
)
agent.print_response("Share a breakfast recipe.", stream=True)

```

[​](#error-handling) Error handling
-----------------------------------

You can set `exponential_backoff` to `True` on the `Agent` to automatically retry requests that fail due to third-party model provider errors.

Copy

Ask AI

```
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    exponential_backoff=True,
    retries=2,
    retry_delay=1,
)

```

[​](#supported-models) Supported Models
---------------------------------------

Agno supports the following model providers:

* [AI/ML API](/models/aimlapi)
* [Anthropic](/models/anthropic)
* [AWS Bedrock](/models/aws-bedrock)
* [Azure AI Foundry](/models/azure-ai-foundry)
* [Claude via AWS Bedrock](/models/aws-claude)
* [Cohere](/models/cohere)
* [DeepSeek](/models/deepseek)
* [Fireworks](/models/fireworks)
* [Google Gemini](/models/google)
* [Groq](/models/groq)
* [Hugging Face](/models/huggingface)
* [LiteLLM](/models/litellm)
* [Mistral](/models/mistral)
* [NVIDIA](/models/nvidia)
* [Nebius AI Studio](/models/nebius)
* [Ollama](/models/ollama)
* [OpenAI](/models/openai)
* [OpenAI Like](/models/openai-like)
* [OpenAI via Azure](/models/azure-openai)
* [OpenRouter](/models/openrouter)
* [Perplexity](/models/perplexity)
* [Sambanova](/models/sambanova)
* [Together](/models/together)
* [vLLM](/models/vllm)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/introduction.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/introduction)

[Collaborate](/teams/collaborate)[Models Compatibility](/models/compatibility)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Error handling](#error-handling)
* [Supported Models](#supported-models)

Assistant

Responses are generated using AI and may contain mistakes.
