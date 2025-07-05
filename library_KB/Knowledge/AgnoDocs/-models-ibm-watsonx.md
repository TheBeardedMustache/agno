IBM WatsonX - Agno

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

IBM WatsonX

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

IBM WatsonX
===========

Learn how to use IBM WatsonX models in Agno.

IBM WatsonX provides access to powerful foundation models through IBM’s cloud platform.

See all the IBM WatsonX supported models [here](https://www.ibm.com/products/watsonx-ai/foundation-models).

* We recommend using `meta-llama/llama-3-3-70b-instruct` for general use
* We recommend `ibm/granite-20b-code-instruct` for code-related tasks
* We recommend using `meta-llama/llama-3-2-11b-vision-instruct` for image understanding

#### [​](#multimodal-support) Multimodal Support

With WatsonX we support `Image` as input

[​](#authentication) Authentication
-----------------------------------

Set your `IBM_WATSONX_API_KEY` and `IBM_WATSONX_PROJECT_ID` environment variables. Get your credentials from [IBM Cloud](https://cloud.ibm.com/).
You can also set the `IBM_WATSONX_URL` environment variable to the URL of the WatsonX API you want to use. It defaults to `https://eu-de.ml.cloud.ibm.com`.

Mac

Windows

Copy

Ask AI

```
export IBM_WATSONX_API_KEY=***
export IBM_WATSONX_PROJECT_ID=***

```

[​](#example) Example
---------------------

Use `WatsonX` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.ibm import WatsonX

agent = Agent(
    model=WatsonX(id="meta-llama/llama-3-3-70b-instruct"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")


```

View more examples [here](../examples/models/ibm).

[​](#params) Params
-------------------

[​](#parameters) Parameters
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| id | str | `"ibm/granite-20b-code-instruct"` | The model ID to use |
| frequency\_penalty | float | `None` | Penalty for using frequent tokens. Higher values discourage repetition |
| presence\_penalty | float | `None` | Penalty for using tokens already present in the text. Higher values encourage new topics |
| max\_tokens | int | `None` | Maximum number of tokens to generate in the response |
| temperature | float | `None` | Controls randomness in responses. Higher values make output more random |
| top\_p | float | `None` | Controls diversity of responses via nucleus sampling |
| logprobs | int | `None` | Number of log probabilities to return |
| top\_logprobs | int | `None` | Number of most likely tokens to return log probabilities for |
| response\_format | Any | `None` | Format specification for the response |
| api\_key | str | `None` | IBM WatsonX API key |
| project\_id | str | `None` | IBM WatsonX project ID |
| url | str | `"https://eu-de.ml.cloud.ibm.com"` | IBM WatsonX API endpoint URL |
| verify | bool | `True` | Whether to verify SSL certificates |
| client\_params | Dict[str, Any] | `None` | Additional parameters to pass to the client |

`WatsonX` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/ibm-watsonx.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/ibm-watsonx)

[HuggingFace](/models/huggingface)[LiteLLM](/models/litellm)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Multimodal Support](#multimodal-support)
* [Authentication](#authentication)
* [Example](#example)
* [Params](#params)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
