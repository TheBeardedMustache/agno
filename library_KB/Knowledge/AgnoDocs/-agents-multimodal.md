Multimodal Agents - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Multimodal Agents

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

  + [Overview](/agents/introduction)
  + [Running your Agent](/agents/run)
  + [Metrics](/agents/metrics)
  + [Sessions](/agents/sessions)
  + [Agent State](/agents/state)
  + [Memory](/agents/memory)
  + [Tools](/agents/tools)
  + [Structured Output](/agents/structured-output)
  + [Multimodal Agents](/agents/multimodal)
  + [User Control Flows](/agents/user-control-flow)
  + [Prompts](/agents/prompts)
  + [Knowledge](/agents/knowledge)
  + [Session Storage](/agents/storage)
  + [Agent Context](/agents/context)
  + [Agent Teams [Deprecated]](/agents/teams)
* Teams
* Models
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

Agents

Copy page

Multimodal Agents
=================

Agno agents support text, image, audio and video inputs and can generate text, image, audio and video outputs. For a complete overview, please checkout the [compatibility matrix](/models/compatibility).

[​](#multimodal-inputs-to-an-agent) Multimodal inputs to an agent
-----------------------------------------------------------------

Let’s create an agent that can understand images and make tool calls as needed

### [​](#image-agent) Image Agent

image\_agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)

```

Run the agent:

Copy

Ask AI

```
python image_agent.py

```

Similar to images, you can also use audio and video as an input.

### [​](#audio-agent) Audio Agent

audio\_agent.py

Copy

Ask AI

```
import base64

import requests
from agno.agent import Agent, RunResponse  # noqa
from agno.media import Audio
from agno.models.openai import OpenAIChat

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content

agent = Agent(
    model=OpenAIChat(id="gpt-4o-audio-preview", modalities=["text"]),
    markdown=True,
)
agent.print_response(
    "What is in this audio?", audio=[Audio(content=wav_data, format="wav")]
)

```

### [​](#video-agent) Video Agent

Currently Agno only supports video as an input for Gemini models.

video\_agent.py

Copy

Ask AI

```
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

# Please download "GreatRedSpot.mp4" using
# wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4
video_path = Path(__file__).parent.joinpath("GreatRedSpot.mp4")

agent.print_response("Tell me about this video", videos=[Video(filepath=video_path)])

```

[​](#multimodal-outputs-from-an-agent) Multimodal outputs from an agent
-----------------------------------------------------------------------

Similar to providing multimodal inputs, you can also get multimodal outputs from an agent.

### [​](#image-generation) Image Generation

The following example demonstrates how to generate an image using DALL-E with an agent.

image\_agent.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DalleTools()],
    description="You are an AI agent that can generate images using DALL-E.",
    instructions="When the user asks you to create an image, use the `create_image` tool to create the image.",
    markdown=True,
    show_tool_calls=True,
)

image_agent.print_response("Generate an image of a white siamese cat")

images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(image_url)

```

### [​](#audio-response) Audio Response

The following example demonstrates how to obtain both text and audio responses from an agent. The agent will respond with text and audio bytes that can be saved to a file.

audio\_agent.py

Copy

Ask AI

```
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)
response: RunResponse = agent.run("Tell me a 5 second scary story")

# Save the response audio to a file
if response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/scary_story.wav"
    )

```

[​](#multimodal-inputs-and-outputs-together) Multimodal inputs and outputs together
-----------------------------------------------------------------------------------

You can create Agents that can take multimodal inputs and return multimodal outputs. The following example demonstrates how to provide a combination of audio and text inputs to an agent and obtain both text and audio outputs.

### [​](#audio-input-and-audio-output) Audio input and Audio output

audio\_agent.py

Copy

Ask AI

```
import base64

import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)

agent.run("What's in these recording?", audio=[Audio(content=wav_data, format="wav")])

if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/result.wav"
    )

```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/multimodal.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/multimodal)

[Structured Output](/agents/structured-output)[User Control Flows](/agents/user-control-flow)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Multimodal inputs to an agent](#multimodal-inputs-to-an-agent)
* [Image Agent](#image-agent)
* [Audio Agent](#audio-agent)
* [Video Agent](#video-agent)
* [Multimodal outputs from an agent](#multimodal-outputs-from-an-agent)
* [Image Generation](#image-generation)
* [Audio Response](#audio-response)
* [Multimodal inputs and outputs together](#multimodal-inputs-and-outputs-together)
* [Audio input and Audio output](#audio-input-and-audio-output)

Assistant

Responses are generated using AI and may contain mistakes.
