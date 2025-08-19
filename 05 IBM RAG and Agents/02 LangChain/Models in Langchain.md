# Models in LangChain 🧠

Models are the "brains" of **LangChain**, a special toolkit that helps you build applications using powerful AI.  
Think of LangChain as a framework that makes it easy to connect different types of AI models to your apps—like using different kinds of engines in the same car.  

LangChain lets you **swap one model for another** without having to rewrite all your code.

---

## Language Models

Language models are AI models that can read and generate human-like text.  
They're what power **chatbots, summarization tools, and other text-based applications**.  

In LangChain, there are two main types you'll encounter:

### Closed Models 🔐
- Like a secret recipe from a company.  
- You can use them through an **API**, but you can’t see or change how they work.  
- Usually require payment.  

**Examples:** GPT-4 (OpenAI), Gemini (Google).

### Open Models (Hugging Face) 🤝
- Open to the public.  
- Can be downloaded, used (sometimes with restrictions), and even modified.  
- Found mostly on **Hugging Face**, a big library of open-source AI models.  

**Examples:** Mistral, Llama 3.

---

## Code Example: A Simple Chatbot 💬

Here’s a simple example of how you can use a closed model like **OpenAI’s GPT-4** with LangChain:

```python
# First, you'll need to install the necessary libraries
# pip install langchain langchain-openai

# Import the 'os' module to interact with the operating system, like accessing environment variables.
import os

# Import the 'ChatOpenAI' class from the LangChain library to work with OpenAI's chat models.
from langchain_openai import ChatOpenAI

# Import 'HumanMessage' and 'SystemMessage' to create structured conversation inputs for the model.
from langchain_core.messages import HumanMessage, SystemMessage

# Import 'userdata' from Google Colab to securely get your API key.
from google.colab import userdata

# Get the OpenAI API key from Colab's user data secrets.
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

# Set the API key as an environment variable so the LangChain library can find it.
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Create an instance of the ChatOpenAI model, specifying which model to use.
chat_model = ChatOpenAI(model="gpt-4o-mini")

# Define a list of messages to send to the model.
messages = [
    # A system message to tell the model what role to play.
    SystemMessage(content="You are a helpful assistant that answers questions about science."),
    # A human message containing the user's question.
    HumanMessage(content="What is the process of photosynthesis?")
]

# Send the list of messages to the model and get its response.
response = chat_model.invoke(messages)

# Print the text content of the model's response.
print(response.content)

# A simple example: directly invoke the model with a single text string.
response_simple = chat_model.invoke("What is langchain in 100 words")

# Print the text content of the simple response.
print(response_simple.content)
```

> 🔎 In this code, LangChain acts as the connector. It takes your messages, sends them to the model, and returns the response.
>

### Open Models - Using Hugging Face

Hugging Face gives access to open-source AI models. You can use them in two ways:

#### 1. Run via Hugging Face API (Cloud) 🌐

This means you don’t run the model yourself. Instead, you send requests to Hugging Face Hub (like OpenAI API).

- ✅ Pros: No need for heavy GPU/CPU, just an internet connection.
- ❌ Cons: Requires a Hugging Face account + API token.

Steps:

- Create an account at huggingface.com
- Go to Settings → Access Tokens and generate a token.
- Install required packages: `pip install langchain langchain-huggingface huggingface_hub`

```python

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_hf_token_here"

from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage

# Choose a model from Hugging Face Hub
chat_model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.7
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain photosynthesis simply.")
]

response = chat_model.invoke(messages)
print(response.content)

```

#### 2. Run Locally on Your Machine 💻

This means you download the model and run it on your system (CPU or GPU).

- ✅ Pros: No API costs, full control, works offline.
- ❌ Cons: Needs strong hardware (esp. for big models).

Steps:
  1. Install libraries:
```bash
pip install langchain langchain-huggingface transformers accelerate bitsandbytes
```
  2. Load a model locally with `HuggingFacePipeline`:
```python
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.messages import HumanMessage, SystemMessage

# Load a small model for local use (better for CPU)
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",   # you can replace with another model
    device_map="auto"                    # auto-select CPU/GPU
)

chat_model = HuggingFacePipeline(pipeline=pipe)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain photosynthesis simply.")
]

response = chat_model.invoke(messages)
print(response.content)

```

### 🔓 Open Models vs 🔐 Closed Models

#### 🔓 Open Models (Hugging Face style)

- Free or community-driven.
- You can download weights, fine-tune, run offline.
- Examples: Mistral, LLaMA 3, Falcon, BLOOM.
- Found on Hugging Face Hub.

#### 🔐 Closed Models (API only)

- Proprietary (company-owned).
- No access to weights or internals.
- Must use API, usually paid.
- Examples: OpenAI GPT-4, Google Gemini, Anthropic Claude.

**✅ Quick Rule of Thumb:**

- Use **closed models (API)** if you need top performance + don’t mind paying.
- Use **open models (Hugging Face, local)** if you want free/controllable models or need offline setups.

---

## Embedding Models

Imagine you want to teach a computer what words mean.
Computers don’t understand words, they understand numbers.

An embedding model translates words/sentences into vectors (lists of numbers) that capture meaning.

👉 Example: The vector for “king” will be close to “queen” because their meanings are similar.
This is useful for semantic search, clustering, and recommendations.

### Closed Models 🔐

Embedding models accessed via API from companies.

Examples: OpenAI Embeddings, Cohere.

### Open Models (Hugging Face) 🤝

Free-to-use, downloadable embedding models.

Examples: all-MiniLM-L6-v2, bge-small-en-v1.5.

---

### Code Example: Finding Similar Sentences 🧐

Here’s how to use embeddings + FAISS for semantic similarity search:

```python
# You might need to install these libraries:
# pip install langchain langchain-openai faiss-cpu

import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Set your API key
# os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# Create a list of sentences (documents)
documents = [
    "The cat sat on the mat.",
    "The dog chased the ball.",
    "A feline rested on a rug."
]

# Initialize the embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Create a vector store (FAISS handles fast similarity search)
vector_store = FAISS.from_texts(documents, embedding_model)

# The sentence to compare
query_text = "The kitten was sleeping on the carpet."

# Search for the most similar sentence
results = vector_store.similarity_search(query_text, k=1) 
most_similar_document = results[0].page_content

print(f"The most similar sentence is: '{most_similar_document}'")

```
> 📝 Here, LangChain:
> - Converts sentences into vectors using embeddings.
> - Stores them in a vector database (FAISS).
> - Finds the most semantically similar sentence to the query.


