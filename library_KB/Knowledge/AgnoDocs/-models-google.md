Gemini - Agno

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

Gemini

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

Gemini
======

Learn how to use Gemini models in Agno.

Use Google’s Gemini models through [Google AI Studio](https://ai.google.dev/gemini-api/docs) or [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/overview) - platforms that provide access to large language models and other services.

We recommend experimenting to find the best-suited model for your use case. Here are some general recommendations in the Gemini `2.x` family of models:

* `gemini-2.0-flash` is good for most use-cases.
* `gemini-2.0-flash-lite` is the most cost-effective model.
* `gemini-2.5-pro-exp-03-25` is the strongest multi-modal model.

Refer to the [Google AI Studio documentation](https://ai.google.dev/gemini-api/docs/models) and the [Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models) for information on available model versions.

[​](#authentication) Authentication
-----------------------------------

You can use Gemini models through either Google AI Studio or Google Cloud’s Vertex AI:

### [​](#google-ai-studio) Google AI Studio

Set the `GOOGLE_API_KEY` environment variable. You can get one [from Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).

Mac

Windows

Copy

Ask AI

```
export GOOGLE_API_KEY=***

```

### [​](#vertex-ai) Vertex AI

To use Vertex AI in Google Cloud:

1. Refer to the [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs/start/cloud-environment) to set up a project and development environment.
2. Install the `gcloud` CLI and authenticate (refer to the [quickstart](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal) for more details):

Copy

Ask AI

```
gcloud auth application-default login

```

3. Enable Vertex AI API and set the project ID environment variable (alternatively, you can set `project_id` in the `Agent` config):

Export the following variables:

Copy

Ask AI

```
export GOOGLE_GENAI_USE_VERTEXAI="true"
export GOOGLE_CLOUD_PROJECT="your-gcloud-project-id"
export GOOGLE_CLOUD_LOCATION="your-gcloud-location"

```

Or update your Agent configuration:

Copy

Ask AI

```
agent = Agent(
    model=Gemini(
        id="gemini-1.5-flash",
        vertexai=True,
        project_id="your-gcloud-project-id",
        location="your-gcloud-location",
    ),
)

```

[​](#example) Example
---------------------

Use `Gemini` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.google import Gemini

# Using Google AI Studio
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
)

# Or using Vertex AI
agent = Agent(
    model=Gemini(
        id="gemini-2.0-flash",
        vertexai=True,
        project_id="your-project-id",  # Optional if GOOGLE_CLOUD_PROJECT is set
        location="us-central1",  # Optional
    ),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](../examples/models/gemini).

[​](#grounding-and-search) Grounding and Search
-----------------------------------------------

Gemini models support grounding and search capabilities through optional parameters. This automatically sends tools for grounding or search to Gemini. See more details [here](https://ai.google.dev/gemini-api/docs/grounding?lang=python).

To enable these features, set the corresponding parameter when initializing the Gemini model:

To use grounding:

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash", grounding=True),
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Any news from USA?")

```

To use search:

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash", search=True),
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What's happening in France?")

```

Set `show_tool_calls=True` in your Agent configuration to see the grounding or search results in the output.

[​](#parameters) Parameters
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"gemini-2.0-flash-exp"` | The specific Gemini model ID to use. |
| `name` | `str` | `"Gemini"` | The name of this Gemini model instance. |
| `provider` | `str` | `"Google"` | The provider of the model. |
| `function_declarations` | `Optional[List[FunctionDeclaration]]` | `None` | List of function declarations for the model. |
| `generation_config` | `Optional[Any]` | `None` | Configuration for text generation. |
| `safety_settings` | `Optional[Any]` | `None` | Safety settings for the model. |
| `generative_model_kwargs` | `Optional[Dict[str, Any]]` | `None` | Additional keyword arguments for the generative model. |
| `grounding` | `bool` | `False` | Whether to use grounding. |
| `search` | `bool` | `False` | Whether to use search. |
| `grounding_dynamic_threshold` | `Optional[float]` | `None` | The dynamic threshold for grounding. |
| `api_key` | `Optional[str]` | `None` | API key for authentication. |
| `vertexai` | `bool` | `False` | Whether to use Vertex AI instead of Google AI Studio. |
| `project_id` | `Optional[str]` | `None` | Google Cloud project ID for Vertex AI. |
| `location` | `Optional[str]` | `None` | Google Cloud region for Vertex AI. |
| `client_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the client. |
| `client` | `Optional[GeminiClient]` | `None` | The underlying generative model client. |
| `temperature` | `Optional[float]` | `None` | Controls randomness in the output. Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `None` | Nucleus sampling parameter. Only consider tokens whose cumulative probability exceeds this value. |
| `top_k` | `Optional[int]` | `None` | Only consider the top k tokens for text generation. |
| `max_output_tokens` | `Optional[int]` | `None` | The maximum number of tokens to generate in the response. |
| `stop_sequences` | `Optional[list[str]]` | `None` | List of sequences where the model should stop generating further tokens. |
| `logprobs` | `Optional[bool]` | `None` | Whether to return log probabilities of the output tokens. |
| `presence_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on whether they appear in the text so far. |
| `frequency_penalty` | `Optional[float]` | `None` | Penalizes new tokens based on their frequency in the text so far. |
| `seed` | `Optional[int]` | `None` | Random seed for deterministic text generation. |
| `request_params` | `Optional[Dict[str, Any]]` | `None` | Additional parameters for the request. |

`Gemini` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/google.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/google)

[Fireworks](/models/fireworks)[Groq](/models/groq)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Google AI Studio](#google-ai-studio)
* [Vertex AI](#vertex-ai)
* [Example](#example)
* [Grounding and Search](#grounding-and-search)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
