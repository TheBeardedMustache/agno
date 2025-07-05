AWS Claude - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

AWS

AWS Claude

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

    - [AWS Bedrock](/models/aws-bedrock)
    - [AWS Claude](/models/aws-claude)
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

AWS

Copy page

AWS Claude
==========

Learn how to use AWS Claude models in Agno.

Use Claude models through AWS Bedrock. This provides a native Claude integration optimized for AWS infrastructure.

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `anthropic.claude-3-5-sonnet-20241022-v2:0` model is good for most use-cases and supports image input.
* `anthropic.claude-3-5-haiku-20241022-v2:0` model is their fastest model.

[​](#authentication) Authentication
-----------------------------------

Set your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variables.

Get your keys from [here](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/home).

Mac

Windows

Copy

Ask AI

```
export AWS_ACCESS_KEY_ID=***
export AWS_SECRET_ACCESS_KEY=***
export AWS_REGION=***

```

[​](#example) Example
---------------------

Use `Claude` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.aws import Claude

agent = Agent(
    model=Claude(id="anthropic.claude-3-5-sonnet-20240620-v1:0"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](../examples/models/aws/claude).

[​](#parameters) Parameters
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"anthropic.claude-3-5-sonnet-20240620-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrockAnthropicClaude"` | The name identifier for the Claude agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `client` | `Optional[AnthropicBedrock]` | `None` | The client for making requests to the Anthropic Bedrock service. |
| `async_client` | `Optional[AsyncAnthropicBedrock]` | `None` | The asynchronous client for making requests to the Anthropic Bedrock service. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | `"None"` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `"None"` | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `top_k` | `Optional[int]` | `"None"` | The number of highest probability vocabulary tokens to keep for top-k-filtering. |
| `stop_sequences` | `Optional[List[str]]` | `"None"` | A list of sequences where the API will stop generating further tokens. |
| `request_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |

`Claude` is a subclass of [`AnthropicClaude`](/models/anthropic) and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/aws-claude.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/aws-claude)

[AWS Bedrock](/models/aws-bedrock)[Azure AI Foundry](/models/azure-ai-foundry)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
