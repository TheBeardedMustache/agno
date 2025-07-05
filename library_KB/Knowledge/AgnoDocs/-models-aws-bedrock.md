AWS Bedrock - Agno

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

AWS Bedrock

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

AWS Bedrock
===========

Learn how to use AWS Bedrock with Agno.

Use AWS Bedrock to access various foundation models on AWS. Manage your access to models [on the portal](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/model-catalog).

See all the [AWS Bedrock foundational models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). Not all Bedrock models support all features. See the [supported features for each model](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

We recommend experimenting to find the best-suited model for your use-case. Here are some general recommendations:

* For a Mistral model with generally good performance, look at `mistral.mistral-large-2402-v1:0`.
* You can play with Amazon Nova models. Use `amazon.nova-pro-v1:0` for general purpose tasks.
* For Claude models, see our [Claude integration](/models/aws-claude).

Async usage of AWS Bedrock is not yet supported. When using `AwsBedrock` with an `Agent`, you can only use `agent.run` and `agent.print_response`.

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

Use `AwsBedrock` with your `Agent`:

agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.aws import AwsBedrock

agent = Agent(
    model=AwsBedrock(id="mistral.mistral-large-2402-v1:0"),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")

```

View more examples [here](/examples/models/aws/bedrock).

[​](#parameters) Parameters
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | `"mistral.mistral-large-2402-v1:0"` | The specific model ID used for generating responses. |
| `name` | `str` | `"AwsBedrock"` | The name identifier for the AWS Bedrock agent. |
| `provider` | `str` | `"AwsBedrock"` | The provider of the model. |
| `max_tokens` | `int` | `4096` | The maximum number of tokens to generate in the response. |
| `temperature` | `Optional[float]` | `"None"` | The sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic. |
| `top_p` | `Optional[float]` | `"None"` | The nucleus sampling parameter. The model considers the results of the tokens with top\_p probability mass. |
| `stop_sequences` | `Optional[List[str]]` | `"None"` | A list of sequences where the API will stop generating further tokens. |
| `request_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional parameters for the request, provided as a dictionary. |
| `client_params` | `Optional[Dict[str, Any]]` | `"None"` | Additional client parameters for initializing the `AwsBedrock` client, provided as a dictionary. |

`AwsBedrock` is a subclass of the [Model](/reference/models/model) class and has access to the same params.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/models/aws-bedrock.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /models/aws-bedrock)

[Anthropic Claude](/models/anthropic)[AWS Claude](/models/aws-claude)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Authentication](#authentication)
* [Example](#example)
* [Parameters](#parameters)

Assistant

Responses are generated using AI and may contain mistakes.
