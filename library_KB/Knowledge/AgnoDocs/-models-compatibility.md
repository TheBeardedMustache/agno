Models Compatibility - Agno

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

Models Compatibility

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

Models Compatibility
====================

### [​](#core-features) Core Features

| Agno Supported Models | Tool Support | Response Models | Knowledge | History / Storage | Async Execution | Async Tool Support |
| --- | --- | --- | --- | --- | --- | --- |
| Anthropic Claude | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AWS Bedrock | ✅ | ✅ | ✅ | ✅ |  |  |
| AWS Bedrock Claude | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Azure AI Foundry | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Azure OpenAI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cohere | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DeepInfra | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| DeepSeek | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Fireworks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemini | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Groq | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HuggingFace | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| IBM WatsonX | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| InternLM | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LiteLLM | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LiteLLMOpenAI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LM Studio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nvidia | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nebius | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ollama | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OllamaTools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAIChat | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAIResponses | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenRouter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Perplexity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sambanova | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Together | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| XAI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

HuggingFace supports tool calling through the Agno framework, but not for streaming
responses.

Perplexity supports tool calling through the Agno framework, but their models don't
natively support tool calls in a straightforward way. This means tool usage may
be less reliable compared to other providers.

### [​](#multimodal-support) Multimodal Support

| Agno Supported Models | Image Input | Audio Input | Audio Responses | Video Input | File Upload |
| --- | --- | --- | --- | --- | --- |
| Anthropic Claude | ✅ |  |  |  | ✅ |
| AWS Bedrock | ✅ |  |  |  |  |
| AWS Bedrock Claude | ✅ |  |  |  |  |
| Azure AI Foundry | ✅ |  |  |  |  |
| Azure OpenAI | ✅ |  |  |  |  |
| Cohere |  |  |  |  |  |
| AWS Bedrock | ✅ |  |  |  |  |
| AWS Bedrock Claude | ✅ |  |  |  |  |
| Azure AI Foundry | ✅ |  |  |  |  |
| Azure OpenAI | ✅ |  |  |  |  |
| Cohere | ✅ |  |  |  |  |
| DeepInfra |  |  |  |  |  |
| DeepSeek |  |  |  |  |  |
| Fireworks |  |  |  |  |  |
| Gemini | ✅ | ✅ |  | ✅ | ✅ |
| Groq | ✅ |  |  |  |  |
| HuggingFace | ✅ |  |  |  |  |
| IBM WatsonX | ✅ |  |  |  |  |
| InternLM |  |  |  |  |  |
| LiteLLM |  |  |  |  |  |
| LiteLLMOpenAI |  |  |  |  |  |
| LM Studio | ✅ |  |  |  |  |
| Mistral | ✅ |  |  |  |  |
| Nvidia |  |  |  |  |  |
| Nebius |  |  |  |  |  |
| Ollama | ✅ |  |  |  |  |
| OllamaTools |  |  |  |  |  |
| OpenAIChat | ✅ | ✅ | ✅ |  |  |
| OpenAIResponses | ✅ | ✅ | ✅ |  | ✅ |
| OpenRouter |  |  |  |  |  |
| Perplexity |  |  |  |  |  |
| Sambanova |  |  |  |  |  |
| Together | ✅ |  |  |  |  |
| XAI | ✅ |  |  |  |  |

### [​](#structured-outputs) Structured Outputs

| Agno Supported Models | Structured Outputs | JSON Mode |
| --- | --- | --- |
| Anthropic Claude |  | ✅ |
| AWS Bedrock |  | ✅ |
| AWS Bedrock Claude |  | ✅ |
| Azure AI Foundry |  | ✅ |
| Azure OpenAI | ✅ | ✅ |
| Cohere |  | ✅ |
| DeepInfra |  | ✅ |
| DeepSeek |  | ✅ |
| Fireworks | ✅ | ✅ |
| Gemini | ✅ | ✅ |
| Groq |  | ✅ |
| HuggingFace |  | ✅ |
| IBM WatsonX |  | ✅ |
| InternLM | ✅ | ✅ |
| LiteLLMOpenAI | ✅ | ✅ |
| LiteLLM |  | ✅ |
| LM Studio | ✅ | ✅ |
| Mistral | ✅ | ✅ |
| Nvidia |  | ✅ |
| Nebius | ✅ | ✅ |
| Ollama | ✅ | ✅ |
| OllamaTools | ✅ | ✅ |
| OpenAIChat | ✅ | ✅ |
| OpenAIResponses | ✅ | ✅ |
| OpenRouter | ✅ | ✅ |
| Perplexity | ✅ | ✅ |
| Sambanova |  | ✅ |
| Together | ✅ | ✅ |
| XAI | ✅ | ✅ |

LM Studio supports JSON schema output, but not structured outputs.

Read more about [Structured Outputs](/faq/structured-outputs).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/compatibility.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/compatibility)

[Overview](/models/introduction)[OpenAI Like](/models/openai-like)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Core Features](#core-features)
* [Multimodal Support](#multimodal-support)
* [Structured Outputs](#structured-outputs)

Assistant

Responses are generated using AI and may contain mistakes.
