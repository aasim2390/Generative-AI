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
# Import the necessary classes and functions.
# PromptTemplate is a class for creating string-based prompts.
from langchain_core.prompts import PromptTemplate

# ChatOpenAI is the interface to the OpenAI LLM.
from langchain_openai import ChatOpenAI

# The LLM is initialized with the "gpt-4o" model and a temperature of 0.2.
# A low temperature makes the output less random and more focused.
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# --- Define the first step: Summarization ---
# A PromptTemplate is created for the summarization task. It takes a single input variable: "text".
summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
# This creates the first chain. It pipes the `summarize_prompt` to the `llm`,
# meaning the LLM will execute the prompt with the given input.
summarize_chain = summarize_prompt | llm

# --- Define the second step: Rewriting ---
# A second PromptTemplate is created for the rewriting task. It takes "summary" as input.
rewrite_prompt = PromptTemplate.from_template("Rewrite as bullet points: {summary}")
# This creates the second chain, which pipes the `rewrite_prompt` to the `llm`.
rewrite_chain = rewrite_prompt | llm

# --- Combine the steps into a single sequential pipeline using LCEL ---
# Import the RunnablePassthrough class, which is used to pass data through a chain without modification.
from langchain_core.runnables import RunnablePassthrough

# This is the core of the LCEL pipeline. We create a dictionary of "runnables" as the first step.
# - "summary": This key is assigned the `summarize_chain`. This means that when the pipeline runs,
#   it will execute the summarization chain and store its result under the key "summary".
# - "text": This key is assigned `RunnablePassthrough()`. This tells the pipeline to simply
#   pass the original input value for "text" directly through to the next step.
overall = {
    "summary": summarize_chain,
    "text": RunnablePassthrough()
} | rewrite_chain

# The output of the dictionary step (which now contains both the original text and the summary)
# is piped to the `rewrite_chain`. The `rewrite_chain` will then be able to access the "summary" key
# from the previous step's output to format its prompt correctly.

# --- Invoke the overall chain ---
# The `.invoke()` method runs the entire pipeline from start to finish.
# The input is a dictionary containing the initial text to be processed.
response = overall.invoke({
    "text": "Photosynthesis is the process by which plants make food..." 
})

# Print the final result. The response object contains the result from the last step (`rewrite_chain`),
# which is the bulleted list.
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
# Import necessary classes and functions from various LangChain packages.
# ChatPromptTemplate is used to create a prompt for a chat model.
# MessagesPlaceholder is a placeholder for dynamic messages, such as chat history.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# RunnablePassthrough is a component that passes input through a chain,
# allowing other steps to access it.
from langchain_core.runnables import RunnablePassthrough

# ConversationBufferWindowMemory stores the last 'k' messages of a conversation.
from langchain.memory import ConversationBufferWindowMemory

# ChatOpenAI is the interface for interacting with the OpenAI chat models.
from langchain_openai import ChatOpenAI

# Initialize the language model.
# ChatOpenAI is instantiated with the "gpt-4o" model and a temperature of 0.2.
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# Create a prompt for the conversational chain.
# The prompt template includes a system message, a placeholder for chat history,
# and a human message for the current input.
# The `MessagesPlaceholder(variable_name="history")` is crucial; it's where the
# conversation history from the memory component will be inserted.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{text}")
])

# Initialize the memory component.
# ConversationBufferWindowMemory is used to store the conversation history.
# `k=3` means it will only remember the last 3 turns of the conversation.
# `return_messages=True` ensures the history is returned as a list of message objects.
memory = ConversationBufferWindowMemory(k=3, return_messages=True)

# Build the LangChain Expression Language (LCEL) pipeline.
# The chain is created using the pipe operator (|).
# 1. RunnablePassthrough.assign(...) loads the chat history from memory and assigns it
#    to a new variable named 'history' in the chain's input dictionary.
#    `lambda x: memory.load_memory_variables(x)["history"]` is a function that retrieves
#    the history from the memory object.
# 2. The output from the first step is piped to the `prompt`. The prompt now has access
#    to both the user's input (`{text}`) and the conversation history (`{history}`).
# 3. The formatted prompt is piped to the `llm`, which generates the response.
chain = (
    RunnablePassthrough.assign(
        history=lambda x: memory.load_memory_variables(x)["history"]
    )
    | prompt
    | llm
)

# Invoke the chain for the first conversation turn.
# The input is a dictionary with the key "text".
inputs = {"text": "What is the capital of France?"}
response = chain.invoke(inputs)

# Save the context of the first conversation turn to memory.
# This makes the memory aware of the input and the AI's output,
# which will be used in the next turn.
memory.save_context(inputs, {"output": response.content})

# Invoke the chain for the second conversation turn.
# The new input asks a follow-up question.
# The chain will use the history saved in the previous step to answer this question.
inputs_2 = {"text": "What country is that in?"}
response_2 = chain.invoke(inputs_2)

# Print the final response from the second turn.
# The LLM is able to correctly answer because the previous interaction is in its memory.
print(response_2.content)
```

#### 5. Indexes (Data Sources)

**Definition:** Connect LLMs to external knowledge (PDFs, websites, DBs).

**Workflow:** Load data → Embed → Store in vector DB → Query with retriever.

❌ The legacy `RetrievalQA` chain is now deprecated in favor of LCEL.

**✅ Example: Ask Questions from PDF (LCEL)**
```python
# Import the necessary classes and functions from various LangChain packages.
# PyPDFLoader is a document loader specifically for PDF files.
from langchain_community.document_loaders import PyPDFLoader

# OpenAIEmbeddings is used to create vector embeddings from text.
# ChatOpenAI is the interface for the OpenAI chat models.
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Chroma is a vector store to save and retrieve our document embeddings.
from langchain_community.vectorstores import Chroma

# create_retrieval_chain is a new factory function to create a complete RAG chain.
from langchain.chains import create_retrieval_chain

# create_stuff_documents_chain is a function that creates a chain to "stuff" documents into the prompt.
from langchain.chains.combine_documents import create_stuff_documents_chain

# ChatPromptTemplate is used to create a prompt for a chat model.
from langchain_core.prompts import ChatPromptTemplate

# Initialize the language model.
# We set the model to "gpt-4o" and temperature to 0 for a more factual response.
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Load the PDF document.
# The PyPDFLoader reads the specified PDF file from the local 'docs' directory.
loader = PyPDFLoader("docs/sample.pdf")

# Load the content of the PDF into a list of "documents".
# Each document typically represents a page from the PDF.
docs = loader.load()

# Create an embeddings model.
# This model will convert the text from our documents into numerical vectors.
embeddings = OpenAIEmbeddings()

# Create a vector store from the documents.
# This step takes the documents, converts them into embeddings using the `embeddings` model,
# and stores them in a Chroma database.
db = Chroma.from_documents(docs, embeddings)

# Create a retriever from the vector store.
# A retriever is a component that can search the database for documents similar to a given query.
# The `search_kwargs={"k": 2}` argument tells the retriever to return the top 2 most relevant documents.
retriever = db.as_retriever(search_kwargs={"k": 2})

# Define the prompt for combining documents and a question.
# This is the template for the final prompt sent to the LLM.
# It explicitly tells the LLM to only use the provided context and to answer a specific question.
# `{context}` and `{input}` are placeholders that will be filled in by the chain.
prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}
""")

# Create the core document-combining chain.
# This chain takes the retrieved documents and the user's question, then formats them
# into the prompt defined above, and passes it to the LLM.
document_chain = create_stuff_documents_chain(llm, prompt)

# Create the full retrieval chain.
# This chain orchestrates the entire RAG process:
# 1. It takes the user's input (the question).
# 2. It uses the `retriever` to find relevant documents.
# 3. It passes the retrieved documents and the question to the `document_chain`.
# 4. The `document_chain` then generates the final response.
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Invoke the chain with a specific question.
# The `.invoke()` method runs the entire chain and returns the result.
# The result is a dictionary, and we extract the final answer from the "answer" key.
response = retrieval_chain.invoke({"input": "What is the main idea of this PDF?"})
print(response["answer"])

```

#### 6. Agents + Tools

**Definition:** Agents use reasoning + tools to take actions.

**Why:** Lets LLMs do more than text generation (e.g., web search, DB query).

❌ `initialize_agent` is deprecated. The new approach uses a factory function (e.g., `create_react_agent`) combined with LCEL.

**✅ Example: Web Search Agent**

```python
# Import the necessary classes and functions from various LangChain packages.
# ChatPromptTemplate is used to create a prompt for a chat model.
# MessagesPlaceholder is a placeholder for dynamic messages, like the agent's internal thoughts.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# DuckDuckGoSearchRun is a tool that allows the agent to perform a web search using DuckDuckGo.
from langchain_community.tools.duckduckgo_search import DuckDuckGoSearchRun

# create_react_agent is a factory function that creates a ReAct-style agent.
# AgentExecutor is the class that executes the agent's logic.
from langchain.agents import create_react_agent, AgentExecutor

# ChatOpenAI is the interface for interacting with the OpenAI chat models.
from langchain_openai import ChatOpenAI

# Initialize the language model.
# ChatOpenAI is instantiated with the "gpt-4o" model.
# The temperature is set to 0 for a more predictable and factual response.
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Create an instance of the DuckDuckGo search tool.
search_tool = DuckDuckGoSearchRun()

# Define the list of tools available to the agent.
# In this case, the agent only has one tool: the web search tool.
tools = [search_tool]

# Define the prompt for the agent.
# This prompt guides the agent's behavior. It consists of three parts:
# 1. "system" message: Sets the agent's role as a "helpful assistant."
# 2. "human" message: Contains a placeholder for the user's input, represented by "{input}".
# 3. "MessagesPlaceholder": This is a special placeholder for the "agent_scratchpad", which
#    will contain the agent's thoughts, actions (tool calls), and observations (tool outputs)
#    during its reasoning process. It's crucial for the ReAct pattern.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create the agent.
# The create_react_agent function combines the LLM, the available tools, and the prompt
# to create an agent that uses the ReAct (Reasoning and Acting) framework.
agent = create_react_agent(llm, tools, prompt)

# Create the AgentExecutor.
# This is the "runner" that takes the agent and its tools.
# The verbose=True flag is set to print the agent's detailed thought process,
# showing its reasoning steps before it makes a tool call. This is great for debugging.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent with a specific query.
# The .invoke() method starts the execution of the agent.
# The input is provided as a dictionary with the key "input".
# The agent will receive this question, decide it needs to search the web to answer it,
# use the DuckDuckGoSearchRun tool, and then formulate a final answer based on the search results.
agent_executor.invoke({"input": "What are the latest LangChain features in 2025?"})
```

**Note:** The `agent_scratchpad` is a key component of ***LangChain's ReAct*** (Reasoning and Acting) agents. 
It is not an external variable that you define; rather, it's an internal placeholder within the agent's prompt where the LLM's thought process is stored and recalled during a multi-step interaction. 

**✅ Example: Python Code Execution**

```python
# Import necessary classes and functions from various LangChain packages.
# TavilySearchResults is a tool for web searches, though it's not used in this specific example.
from langchain_community.tools.tavily_search import TavilySearchResults

# create_tool_calling_agent is a factory function to create an agent that uses tool-calling.
# AgentExecutor is the class that runs the agent, managing the logic of calling the LLM and tools.
from langchain.agents import create_tool_calling_agent, AgentExecutor

# ChatOpenAI is the interface for interacting with the OpenAI chat models (like GPT-4o).
from langchain_openai import ChatOpenAI

# PythonREPLTool is a tool that allows the agent to execute Python code.
from langchain_experimental.tools.python.tool import PythonREPLTool

# ChatPromptTemplate is used to create a prompt for a chat model.
# MessagesPlaceholder is used to insert agent-specific messages, like thoughts and tool outputs, into the prompt.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Instantiate the language model.
# ChatOpenAI is initialized with the "gpt-4o" model.
# The temperature is set to 0 for deterministic and factual outputs, which is good for code generation.
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Define the tools that the agent can use.
# In this case, the agent only has access to the PythonREPLTool.
tools = [PythonREPLTool()]

# Create a prompt for the agent.
# The prompt is a list of messages that define the agent's behavior and provide context.
# The "system" message tells the agent its role.
# The "human" message includes a placeholder for the user's input, which will be the question.
# The MessagesPlaceholder inserts the "agent_scratchpad", which holds the agent's internal
# dialogue, like its thoughts and the results from tool executions.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an agent that can execute Python code to answer questions."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create the agent.
# This function combines the LLM, the list of tools, and the prompt to create a runnable agent.
# The agent is now ready to receive input and decide which tools to use.
agent = create_tool_calling_agent(llm, tools, prompt)

# Create the AgentExecutor.
# This is the "runner" for the agent. It takes the agent and its tools.
# Setting verbose=True logs the agent's thought process, including its reasoning and tool usage,
# which is very helpful for debugging.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent with a specific input.
# The .invoke() method is used to execute the agent's logic.
# The input is a dictionary with the key "input" matching the placeholder in the prompt.
# The agent will receive this input, decide to use the PythonREPLTool, generate the Python code,
# execute it, and then return the final result.
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
  
