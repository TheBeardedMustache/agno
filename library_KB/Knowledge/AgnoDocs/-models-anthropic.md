Anthropic Claude - Agno

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

Anthropic Claude

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

Anthropic Claude
================

Learn how to use Anthropic Claude models in Agno.

Claude is a family of foundational AI models by Anthropic that can be used in a variety of applications.
See their model comparisons [here](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* `claude-3-5-sonnet-20241022` model is good for most use-cases and supports image input.
* `claude-3-5-haiku-20241022` model is their fastest model.

Anthropic has rate limits on their APIs. See the [docs](https://docs.anthropic.com/en/api/rate-limits#response-headers) for more information.

[​](#authentication) Authentication
-----------------------------------

Set your `ANTHROPIC_API_KEY` environment. You can get one [from Anthropic here](https://console.anthropic.com/settings/keys).

Mac

Windows

Copy

Ask AI

```
export ANTHROPIC_API_KEY=***

```

[​](#example) Example
---------------------

Use `Claude` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20240620"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](../examples/models/anthropic).

[​](#params) Params
-------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"claude-3-5-sonnet-20241022"` | The id of the Anthropic Claude model to use |
| `name` | `str` | `"Claude"` | The name of the model |
| `provider` | `str` | `"Anthropic"` | The provider of the model |
| `max_tokens` | `Optional[int]` | `1024` | Maximum number of tokens to generate in the chat completion |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the model's output |
| `stop_sequences` | `Optional[List[str]]` | `None` | A list of strings that the model should stop generating text at |
| `top_p` | `Optional[float]` | `None` | Controls diversity via nucleus sampling |
| `top_k` | `Optional[int]` | `None` | Controls diversity via top-k sampling |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters to include in the request |
| `api_key` | `Optional[str]` | `None` | The API key for authenticating with Anthropic |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for client configuration |
| `client` | `Optional[AnthropicClient]` | `None` | A pre-configured instance of the Anthropic client |
| `structured_outputs` | `bool` | `False` | Whether to use structured outputs with this Model |
| `add_images_to_message_content` | `bool` | `True` | Whether to add images to the message content |
| `override_system_role` | `bool` | `True` | Whether to override the system role |
| `system_message_role` | `str` | `"assistant"` | The role to map the system message to |

`Claude` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/anthropic.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/anthropic)

[AI/ML API](/models/aimlapi)[AWS Bedrock](/models/aws-bedrock)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)

Assistant

Responses are generated using AI and may contain mistakes.
