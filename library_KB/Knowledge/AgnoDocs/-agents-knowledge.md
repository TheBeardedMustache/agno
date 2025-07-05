Knowledge - Agno

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

Knowledge

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

Knowledge
=========

**Knowledge** is domain-specific information that the Agent can **search** at runtime to make better decisions (dynamic few-shot learning) and provide accurate responses (agentic RAG). Knowledge is stored in a vector db and this **searching on demand** pattern is called Agentic RAG.

Dynamic Few-Shot Learning: Text2Sql Agent

Example: If we’re building a Text2Sql Agent, we’ll need to give the table schemas, column names, data types, example queries, common “gotchas” to help it generate the best-possible SQL query.

We’re obviously not going to put this all in the system prompt, instead we store this information in a vector database and let the Agent query it at runtime.

Using this information, the Agent can then generate the best-possible SQL query. This is called dynamic few-shot learning.

**Agno Agents use Agentic RAG** by default, meaning when we provide `knowledge` to an Agent, it will search this knowledge base, at runtime, for the specific information it needs to achieve its task.

The pseudo steps for adding knowledge to an Agent are:

Copy

Ask AI

```
from agno.agent import Agent, AgentKnowledge

# Create a knowledge base for the Agent
knowledge_base = AgentKnowledge(vector_db=...)

# Add information to the knowledge base
knowledge_base.load_text("The sky is blue")

# Add the knowledge base to the Agent and
# give it a tool to search the knowledge base as needed
agent = Agent(knowledge=knowledge_base, search_knowledge=True)

```

We can give our agent access to the knowledge base in the following ways:

* We can set `search_knowledge=True` to add a `search_knowledge_base()` tool to the Agent. `search_knowledge` is `True` **by default** if you add `knowledge` to an Agent.
* We can set `add_references=True` to automatically add references from the knowledge base to the Agent’s prompt. This is the traditional 2023 RAG approach.

If you need complete control over the knowledge base search, you can pass your own `retriever` function with the following signature:

Copy

Ask AI

```
def retriever(agent: Agent, query: str, num_documents: Optional[int], **kwargs) -> Optional[list[dict]]:
  ...

```

This function is called during `search_knowledge_base()` and is used by the Agent to retrieve references from the knowledge base.

[​](#vector-databases) Vector Databases
---------------------------------------

While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly. Here’s how vector databases are used with Agents:

1

Chunk the information

Break down the knowledge into smaller chunks to ensure our search query
returns only relevant results.

2

Load the knowledge base

Convert the chunks into embedding vectors and store them in a vector
database.

3

Search the knowledge base

When the user sends a message, we convert the input message into an
embedding and “search” for nearest neighbors in the vector database.

Knowledge filters are currently supported on the following knowledge base types: **PDF**, **PDF\_URL**, **Text**, **JSON**, and **DOCX**.
For more details, see the [Knowledge Filters documentation](/filters/introduction).

[​](#example%3A-rag-agent-with-a-pdf-knowledge-base) Example: RAG Agent with a PDF Knowledge Base
-------------------------------------------------------------------------------------------------

Let’s build a **RAG Agent** that answers questions from a PDF.

### [​](#step-1%3A-run-pgvector) Step 1: Run PgVector

Let’s use `PgVector` as our vector db as it can also provide storage for our Agents.

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

Copy

Ask AI

```
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16

```

### [​](#step-2%3A-traditional-rag) Step 2: Traditional RAG

Retrieval Augmented Generation (RAG) means **“stuffing the prompt with relevant information”** to improve the model’s response. This is a 2 step process:

1. Retrieve relevant information from the knowledge base.
2. Augment the prompt to provide context to the model.

Let’s build a **traditional RAG** Agent that answers questions from a PDF of recipes.

1

Install libraries

Install the required libraries using pip

Mac

Windows

Copy

Ask AI

```
pip install -U pgvector pypdf "psycopg[binary]" sqlalchemy

```

2

Create a Traditional RAG Agent

Create a file `traditional_rag.py` with the following contents

traditional\_rag.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    # Read PDF from this URL
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Store embeddings in the `ai.recipes` table
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
# Load the knowledge base: Comment after first run
knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Enable RAG by adding references from AgentKnowledge to the user prompt.
    add_references=True,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=False,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup")

```

3

Run the agent

Run the agent (it takes a few seconds to load the knowledge base).

Mac

Windows

Copy

Ask AI

```
python traditional_rag.py

```

How to use local PDFs

If you want to use local PDFs, use a `PDFKnowledgeBase` instead

agent.py

Copy

Ask AI

```
from agno.knowledge.pdf import PDFKnowledgeBase

...
knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)
...

```

### [​](#step-3%3A-agentic-rag) Step 3: Agentic RAG

With traditional RAG above, `add_references=True` always adds information from the knowledge base to the prompt, regardless of whether it is relevant to the question or helpful.

With Agentic RAG, we let the Agent decide **if** it needs to access the knowledge base and what search parameters it needs to query the knowledge base.

Set `search_knowledge=True` and `read_chat_history=True`, giving the Agent tools to search its knowledge and chat history on demand.

1

Create an Agentic RAG Agent

Create a file `agentic_rag.py` with the following contents

agentic\_rag.py

Copy

Ask AI

```
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)
# Load the knowledge base: Comment out after first run
knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Add a tool to search the knowledge base which enables agentic RAG.
    search_knowledge=True,
    # Add a tool to read chat history.
    read_chat_history=True,
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What was my last question?", markdown=True)

```

2

Run the agent

Run the agent

Mac

Windows

Copy

Ask AI

```
python agentic_rag.py

```

Notice how it searches the knowledge base and chat history when needed

[​](#attributes) Attributes
---------------------------

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `knowledge` | `AgentKnowledge` | `None` | Provides the knowledge base used by the agent. |
| `search_knowledge` | `bool` | `True` | Adds a tool that allows the Model to search the knowledge base (aka Agentic RAG). Enabled by default when `knowledge` is provided. |
| `add_references` | `bool` | `False` | Enable RAG by adding references from AgentKnowledge to the user prompt. |
| `retriever` | `Callable[..., Optional[list[dict]]]` | `None` | Function to get context to add to the user message. This function is called when add\_references is True. |
| `context_format` | `Literal['json', 'yaml']` | `json` | Specifies the format for RAG, either “json” or “yaml”. |
| `add_context_instructions` | `bool` | `False` | If True, add instructions for using the context to the system prompt (if knowledge is also provided). For example: add an instruction to prefer information from the knowledge base over its training data. |

[​](#developer-resources) Developer Resources
---------------------------------------------

* View [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/knowledge)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/agents/knowledge.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /agents/knowledge)

[Prompts](/agents/prompts)[Session Storage](/agents/storage)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.agno.com)

On this page

* [Vector Databases](#vector-databases)
* [Example: RAG Agent with a PDF Knowledge Base](#example%3A-rag-agent-with-a-pdf-knowledge-base)
* [Step 1: Run PgVector](#step-1%3A-run-pgvector)
* [Step 2: Traditional RAG](#step-2%3A-traditional-rag)
* [Step 3: Agentic RAG](#step-3%3A-agentic-rag)
* [Attributes](#attributes)
* [Developer Resources](#developer-resources)

Assistant

Responses are generated using AI and may contain mistakes.
