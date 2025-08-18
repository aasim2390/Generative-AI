# LangChain Core Concepts

## What is LangChain?
LangChain is an **open-source interface** that simplifies building apps with **Large Language Models (LLMs)**.  
It provides a **structured way** to use LLMs for tasks like:
- Natural Language Processing (NLP)  
- Data retrieval  
- Chatbots  
- Structured data handling  

---

## Main Components of LangChain
LangChain is made up of **several core building blocks**:

### 1. **Language Models (LMs)** 🧠
- **Foundation of LangChain** → takes **text input** and produces **text output**.  
- Useful for tasks like **document summarization**, **content creation**, and **answer generation**.  
- Supported LLM providers: **OpenAI, Google, Meta, Anthropic**.  

**Example (OpenAI):**  
Use OpenAI’s *GPT-4* model.  
- Adjust parameters like `max_tokens` (response length) and `temperature` (creativity).  
- Model generates text such as a *new sales strategy idea*.  

👉 Memory Hook: **LM = Text-in, Text-out engine**  

---

### 2. **Chat Models** 💬
- Built on top of LMs → designed for **conversations**.  
- They remember context and act more **human-like** in dialogue.  

**How it works:**  
- Convert a base LLM (e.g., OpenAI GPT-4) into a **Chat Model**.  
- Engage in **multi-turn dialogue**.  

**Example:**  
Question: *“Who is man’s best friend?”*  
→ Chat model answers: *“Dogs are often called man’s best friend.”*  

👉 Memory Hook: **LM talks, Chat Model chats**  

---

### 3. **Chat Messages** 📨
Every chat has messages with two properties:
- **Role** → Who is speaking (system, human, AI, tool, function)  
- **Content** → What is being said  

**Types of Messages:**  
- **Human Message** → User input  
- **AI Message** → Model’s reply  
- **System Message** → Instructions for model behavior  
- **Function Message** → Call outcomes with parameters  
- **Tool Message** → Helps models interact with tools  

**Example (OpenAI Chat):**  
System: *“You are a fitness coach. Reply briefly.”*  
Human: *“What should I eat today?”*  
AI: *“Eat fruits and vegetables.”*  

👉 Memory Hook: **5 Roles = Human, AI, System, Function, Tool**  

---

### 4. **Prompt Templates** 📝
Prompts = instructions for the model. Templates help standardize them.  

**Types of Prompt Templates:**  
- **String Prompt Template** → simple text with placeholders  
- **Chat Prompt Template** → structured for conversations  
- **Message Prompt Templates** → role-specific (AI, System, Human)  
- **Messages Placeholder** → full control over rendering messages  
- **Few-Shot Prompt Template** → provides examples to guide the model  

**Example (OpenAI):**  
System: *“You are a travel assistant.”*  
Human: *“Plan a 3-day trip to Paris.”*  
→ Template ensures clear, consistent instructions to GPT-4.  

👉 Memory Hook: **Prompt Templates = Blueprints for model instructions**  

---

### 5. **Example Selectors** 📚
Helps choose the **right examples** for Few-Shot learning.  

**Techniques used:**  
- **Semantic Similarity** → pick examples closest in meaning  
- **Max Marginal Relevance (MMR)** → balance similarity + diversity  
- **N-Gram Overlap** → pick examples with overlapping words  

**Example:**  
If the chatbot is helping with **resume writing**, the selector finds past **resume samples** that best match the user’s request.  

👉 Memory Hook: **Selectors = Smart librarians for prompts**  

---

### 6. **Output Parsers** 🗂️
LLMs produce free-form text. Parsers **convert it into structured formats** like:
- JSON  
- XML  
- CSV  
- Pandas DataFrame  

**Example (OpenAI):**  
Ask GPT-4: *“List 3 fruits.”*  
Raw output: *“Apple, Banana, Orange”*  
→ Output Parser converts to **CSV**

👉 Memory Hook: **Parser = Text-to-Structure converter**  

---

## Recap
LangChain = **Framework for LLM apps** with these main components:  
1. **Language Model** → Text in, text out  
2. **Chat Model** → Conversations like a human  
3. **Chat Messages** → Roles (Human, AI, System, Function, Tool)  
4. **Prompt Templates** → Instructions for clarity  
5. **Example Selectors** → Pick best examples  
6. **Output Parsers** → Structured data formats  

---

## Final Memory Formula
**LM 🧠 + Chat 💬 + Messages 📨 + Templates 📝 + Selectors 📚 + Parsers 🗂️ = LangChain 🚀**


---

## 🔑 Detailed Notes on LangChain with OpenAI

### 1. LangChain Overview

- LangChain is a framework that makes it easier to build applications powered by Large Language Models (LLMs).
- It helps developers connect LLMs with data sources, APIs, and reasoning workflows.

💡 Think of LangChain as the “glue” that connects OpenAI models with your application logic.

### 2. Core Components of LangChain
#### a) LLM Wrappers

- Allow you to use OpenAI’s GPT models easily.

Example: call GPT-4 to generate text, answer questions, or summarize.

```python
# Preferred Chat Model
from langchain_openai import ChatOpenAI

# Use ChatOpenAI for GPT-4, GPT-4.1, GPT-4o, GPT-3.5-turbo, etc.
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Simple query
response = llm.invoke("Explain LangChain in simple words.")
print(response.content)

##################

# Non-chat Nodel
from langchain_openai import OpenAI

# Use this only for text completion models (like GPT-3.5-instruct)
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)
response = llm.invoke("Explain LangChain in simple words.")
print(response)



```

### 📌 Memorable Rule

- Chat Models (GPT-4, GPT-4o, GPT-3.5-turbo) → ChatOpenAI
- Completion Models (GPT-3.5-instruct, legacy models) → OpenAI

  
#### b) Prompts

- Structured templates to interact with LLMs.

- Makes responses more predictable and reusable.

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("You are a teacher. Explain {topic} in simple terms.")

print(prompt.format(topic="LangChain"))


```


#### c) Chains

- Chains combine multiple steps (prompts + LLMs + tools).

- Example: take user input → fetch context → ask GPT → return answer.

```python

### Type 1
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# ✅ Use ChatOpenAI (preferred for GPT-4 / GPT-4o / GPT-4.1)
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Prompt template
prompt = PromptTemplate.from_template(
    "You are a teacher. Explain {topic} in simple terms."
)

# Build chain
chain = LLMChain(llm=llm, prompt=prompt)

# Preferred usage with .invoke() and dict input
result = chain.invoke({"topic": "Retrieval-Augmented Generation (RAG)"})

print(result["text"])  # result is a dict, "text" contains the answer

```

```python
### Type 2

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Define model
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Define prompt
prompt = PromptTemplate.from_template(
    "You are a teacher. Explain {topic} in simple terms."
)

# Pipe syntax (prompt → llm)
chain = prompt | llm

# Invoke chain
result = chain.invoke({"topic": "Retrieval-Augmented Generation (RAG)"})
print(result.content)


```

#### d) Memory

- Helps LangChain remember previous conversations.

- Useful for chatbots and assistants.

```python
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Use ChatOpenAI (latest recommended wrapper)
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Use ConversationBufferMemory to keep track of history
memory = ConversationBufferMemory(return_messages=True)

# Build the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True   # optional, logs the reasoning steps
)

# Invoke instead of run (latest standard)
response1 = conversation.invoke({"input": "Hi, I am Asim."})
print(response1["response"])

response2 = conversation.invoke({"input": "What did I just tell you my name is?"})
print(response2["response"])


```

> The | pipe operator is meant for chaining Runnable objects together, not for supplying input.

#### ⚡ Think of it this way:

- ✅ `|` is for wiring components
- ✅ `.invoke()` is for sending input data


#### e) Agents & Tools

- Agents: Decide what to do next (using LLM reasoning).

- Tools: Functions the agent can call (like search, calculator, DB query).

```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_openai_functions_agent, tool
from langchain import hub
from langchain.agents import AgentExecutor  # or: from langchain.agents import AgentExecutor

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Tools (keep securely evaluating expressions)
@tool
def calculator(query: str) -> str:
    """Do math calculations like square roots, powers, etc."""
    import math
    allowed = {"sqrt": math.sqrt, "pow": pow}
    try:
        # Use a restricted environment for safety
        return str(eval(query, {"__builtins__": {}}, allowed))
    except Exception as e:
        return f"Error: {e}"

@tool
def discovery_info(subject: str) -> str:
    """Dummy implementation for discovery info."""
    if "square root" in subject.lower():
        return "The concept of square roots was known to ancient Babylonians and Greeks."
    return "I don’t know yet."

tools = [calculator, discovery_info]

# Use a prebuilt prompt template from LangChain Hub
prompt = hub.pull("hwchase17/openai-functions-agent")

# Build the function-calling agent
agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)

# Create an executor to run the agent
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

# Run the agent
response = agent_executor.invoke({"input": "What's the square root of 144 and search who discovered it?"})
print(response)


```

## 3. LangChain with RAG (Retrieval-Augmented Generation)

- RAG connects LLMs with external data for factual answers.

- Example: use OpenAI GPT + vector database to search company docs.

```python
# --- Imports ---
from langchain_openai import OpenAIEmbeddings, ChatOpenAI   # OpenAI embeddings + chat LLM wrappers
from langchain_community.vectorstores import FAISS          # FAISS in-memory vector store (similarity search)
from langchain.chains import RetrievalQA                     # (Imported but NOT used below; classic RAG chain helper)
from langchain_core.prompts import ChatPromptTemplate        # Message-based prompt builder
from langchain_core.runnables import RunnablePassthrough     # Lets raw input flow through a pipeline unchanged
from langchain_core.output_parsers import StrOutputParser    # Converts LLM output to a plain string

# 1) ----- Build the knowledge index (embeddings + FAISS) -----
embeddings = OpenAIEmbeddings()                              # Creates a callable that turns text -> embedding vectors
db = FAISS.from_texts(                                       # Build a FAISS index directly from a list of texts
    ["LangChain helps build LLM apps.",                      # Corpus document #1
     "OpenAI provides GPT models."],                         # Corpus document #2
    embedding=embeddings                                     # Use OpenAIEmbeddings to embed the texts
)

# 2) ----- Create a retriever over the vector store -----
retriever = db.as_retriever(search_kwargs={"k": 5})          # Wrapper that, given a query, returns top-matching docs, Bydefault return 4

# 3) ----- Initialize the chat LLM -----
llm = ChatOpenAI(model="gpt-3.5-turbo")                      # The model to call (use any available model, e.g. gpt-4o-mini)

# 4) ----- Define the prompt the LLM will see -----
prompt = ChatPromptTemplate.from_messages([                  # Build a chat-style prompt with multiple roles
    ("system", "You are a helpful assistant that answers based on the given context."),  # System behavior instruction
    ("human",  "Context: {context}\n\nQuestion: {question}") # Human message with placeholders to be filled later
])

# 5) ----- Build a RAG pipeline using LCEL pipes (|) -----
rag_chain = (
    {                                                        # Map step: build the dict of inputs for the prompt
        "context": retriever,                                # For key "context": run the retriever on the incoming input
        "question": RunnablePassthrough()                    # For key "question": pass the raw user input unchanged
    }
    | prompt                                                 # Format those into the chat prompt messages
    | llm                                                    # Send the messages to the chat model
    | StrOutputParser()                                      # Extract the assistant's text as a simple string
)
# Notes:
# - The curly-brace mapping fan-outs the single input into two branches:
#     * retriever(input) -> docs -> becomes {context}
#     * passthrough(input) -> the same string -> becomes {question}
# - The pipe operator (|) composes Runnables into a sequence.
# - 'rag_chain.invoke(user_input)' actually executes the pipeline.

# 6) ----- Run a query end-to-end -----
print(rag_chain.invoke("Who provides GPT models?"))          # Pass a single string; it feeds both retriever & question
# Expected behavior:
# - retriever gets "Who provides GPT models?" and returns the doc about OpenAI/GPT.
# - prompt fills {context} with retrieved snippets and {question} with the input.
# - llm answers grounded in that context.
# - StrOutputParser returns the final string, which we print.

```

***Note:***

**a) The Mapping Step**
```json
{
  "context": retriever,
  "question": RunnablePassthrough()
}
```
- This is a **Runnable mapping**:
  - The same input (say: "Who provides GPT models?") is sent to both branches.
      - `"context"` : retriever → converts the query into an embedding, does similarity search in FAISS, returns docs.
      - `"question"`: RunnablePassthrough() → just echoes back the original input string unchanged.
- Result after this step:
```json
  {
  "context": ["OpenAI provides GPT models."],  # top doc retrieved
  "question": "Who provides GPT models?"       # original user input
  }
```

So, the next flow goes like this

<img width="700" height="650" alt="image" src="https://github.com/user-attachments/assets/76b1313f-5466-4fb3-8ba8-9a1492a67284" />


### 4. Why LangChain + OpenAI Matters

- ✅ Easy integration with OpenAI models (GPT-4, GPT-3.5).
- ✅ Supports multi-step workflows.
- ✅ Enables context-aware chatbots.
- ✅ Connects to databases, APIs, search engines.
- ✅ Helps with automation + reasoning + knowledge retrieval.


### 🔥 Memorable Analogy:

- LLM (OpenAI GPT) → The brain
- LangChain → The nervous system (connects brain to body)
- Tools/APIs → The hands & legs (actions)
- Memory → The long-term memory
