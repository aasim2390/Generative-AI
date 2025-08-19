## 📝 LangChain Notes (2025 Edition)

### 🔹 Overview

LangChain is a framework for building applications around LLMs (Large Language Models) by wiring together:
  - **Models** (LLMs, embeddings)
  - **Prompts**
  - **Memory**
  - **Data sources / Indexes**
  - **Orchestration logic** (chains, agents, tools)

**👉 Core Idea:** Separate what you want to do (prompting, retrieval, reasoning) from how you connect data and tools.

---

### 🔹 Two Core Model Types

#### 1. Language Models (LLMs)

Used for text/chat generation, reasoning, summarization, Q&A, etc.
  - Examples: OpenAI GPT, Claude, HuggingFace models.

**Example: Chat-based LLM**
```python
# Use the specific provider package, which is the new best practice.
from langchain_openai import ChatOpenAI

chat_llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

# Use .invoke() instead of the deprecated .predict() or .run() methods.
response = chat_llm.invoke("Write a haiku about LangChain.")
print(response.content)
```

#### 2. Embedding Models
Convert text → vectors for semantic search, similarity, clustering.
  - Examples: OpenAIEmbeddings, CohereEmbeddings, local models.

**Example: Embeddings**
```python
# Use the specific provider package.
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()
vector = embedding_model.embed_query("What is LangChain?")
```

---

### Core Components

#### 1. Models

**Definition:** Interfaces to communicate with AI providers.

**Why:** Swap models with minimal code changes. The new best practice is to import directly from the provider-specific package (e.g., `langchain-openai`).

**❌ Text-based LLM:** `langchain.llms.OpenAI` is now deprecated. It is better to use ChatOpenAI.

**✅ Chat-based LLM (preferred)**
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
```

#### 2. Prompts

**Definition:** Instructions to LLMs.

**Why:** Outputs depend heavily on how prompts are framed.

**✅ System + User Prompt**

```python
from langchain_core.prompts import ChatPromptTemplate

# `SystemMessagePromptTemplate` and `HumanMessagePromptTemplate` are
# typically no longer imported separately.
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{text}")
])
```

**✅ Few-shot Prompt**

The previous approach using `FewShotPromptTemplate` and `LLMChain` is deprecated. The new approach uses **LangChain Expression Language (LCEL)** to compose a runnable sequence.

```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

example_prompt = PromptTemplate.from_template("Q: {question}\nA: {answer}\n")

examples = [
    {"question": "What is AI?", "answer": "Artificial Intelligence."},
    {"question": "What is ML?", "answer": "Machine Learning."}
]

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are a concise tutor.",
    suffix="Q: {question}\nA:",
    input_variables=["question"],
)

# Use LCEL to chain the prompt to the model.
chain = few_shot | llm

# Use .invoke() instead of the deprecated .run() method.
response = chain.invoke({"question": "What is deep learning?"})
print(response.content)
```

#### 3. Chains (LCEL)

**Definition:** Orchestration pipelines connecting multiple steps. The legacy `SequentialChain` is deprecated. 
LCEL is now the standard for building flexible pipelines.

**Example: Two-step LCEL Chain**

This example uses the `|` operator to chain components together, a core feature of LCEL.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# Define the individual steps as runnables
summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
summarize_chain = summarize_prompt | llm

rewrite_prompt = PromptTemplate.from_template("Rewrite as bullet points: {summary}")
rewrite_chain = rewrite_prompt | llm

# The new LCEL way to create a sequential pipeline
from langchain_core.runnables import RunnablePassthrough

# Use RunnablePassthrough to pass inputs through the chain
overall = {
    "summary": summarize_chain,
    "text": RunnablePassthrough()
} | rewrite_chain

response = overall.invoke({
    "text": "Photosynthesis is the process by which plants make food..." 
})
print(response.content)
```

#### 4. Memory

**Definition:** Keeps past interactions for continuity.
  - **ConversationBufferMemory:** Full chat history
  - **ConversationBufferWindowMemory:** Last N turns
  - **ConversationSummaryMemory:** Compact summary
  - **EntityMemory:** Tracks facts/entities

**✅ Example: Windowed Memory**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# Prompts for chat history now use `MessagesPlaceholder`.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{text}")
])

memory = ConversationBufferWindowMemory(k=3, return_messages=True)

# LCEL pipeline for a chat history-aware chain
chain = (
    RunnablePassthrough.assign(
        history=lambda x: memory.load_memory_variables(x)["history"]
    )
    | prompt
    | llm
)

# Invoke the chain, then save the output to memory
inputs = {"text": "What is the capital of France?"}
response = chain.invoke(inputs)
memory.save_context(inputs, {"output": response.content})

inputs_2 = {"text": "What country is that in?"}
response_2 = chain.invoke(inputs_2)
print(response_2.content)
```

#### 5. Indexes (Data Sources)

**Definition:** Connect LLMs to external knowledge (PDFs, websites, DBs).

**Workflow:** Load data → Embed → Store in vector DB → Query with retriever.

❌ The legacy `RetrievalQA` chain is now deprecated in favor of LCEL.

**✅ Example: Ask Questions from PDF (LCEL)**
```python

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Load and process documents
loader = PyPDFLoader("docs/sample.pdf")
docs = loader.load()

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})

# Define the prompt for combining documents and a question
prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}
""")

# Create the LCEL-based retrieval chain
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Invoke the chain
response = retrieval_chain.invoke({"input": "What is the main idea of this PDF?"})
print(response["answer"])
```

#### 6. Agents + Tools

**Definition:** Agents use reasoning + tools to take actions.

**Why:** Lets LLMs do more than text generation (e.g., web search, DB query).

❌ `initialize_agent` is deprecated. The new approach uses a factory function (e.g., `create_react_agent`) combined with LCEL.

**✅ Example: Web Search Agent**

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.duckduckgo_search import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# Define the prompt for the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create the agent and executor
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Use .invoke()
agent_executor.invoke({"input": "What are the latest LangChain features in 2025?"})
```

**✅ Example: Python Code Execution**

```python
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = [PythonREPLTool()]

# Create a tool-calling agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an agent that can execute Python code to answer questions."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Use .invoke()
agent_executor.invoke({"input": "Write a Python function for factorial."})
```

---

## 🔹 Latest Additions in LangChain (2025)

  - **LCEL (LangChain Expression Language):** The most important update. It provides a declarative way to compose chains with first-class streaming, async support, and parallel execution. This replaces the older, more rigid Chain classes.
  - **LangGraph:** A powerful extension for building multi-step, multi-actor state machines with cyclic graphs, useful for complex agentic workflows.
  - **LangSmith:** The platform for building, debugging, and monitoring your LLM applications. It's now an indispensable part of the LangChain ecosystem.
  - **Provider-specific packages:** Many components, including ChatOpenAI, OpenAIEmbeddings, and others, have been moved to dedicated packages like langchain-openai and langchain-community. This modularizes the framework and reduces the core package size.
  - **Enhanced Memory:** The Memory classes are now more seamlessly integrated into LCEL pipelines.

---

##  Best Practices

  - **Check version:** LangChain evolves fast; verify imports **(pip show langchain)**.
  - **Use LCEL:** Embrace LCEL for building chains. It's the future-proof, recommended method.
  - **Cost awareness**: Use **summary/window memory** to avoid token explosion.
  - **Build incrementally:** Start with a simple LCEL chain **(prompt | llm)**, then add other components like retrievers, memory, and tools.
  - **Test locally:** Use mock LLMs for quick dev cycles before hitting paid APIs.
  - **Use LangSmith**: For any serious project, use LangSmith for debugging and observability.
  
