# Pricing and Tokens

## Cost of Using LLMs
When you use the Playground or Assistants API to access a language model (LLM), you will need to pay a fee based on how many tokens you use.  
Tokens are the basic units of measurement when it comes to processing text.

## What is a Token?
A token can be a whole word, part of a word, or even a character, depending on how the language model works.

**For example:**
- The word `cats` is **one** token.
- The word `chatting` might be broken down into **two** tokens: `chat` and `ting`.
- A punctuation mark, like a comma or period, also counts as a token.

## Pricing Trends
Currently, there is a lot of competition among different providers of language models, which has been causing the prices for using LLMs to go down.  
This trend of declining prices is expected to continue for the foreseeable future, making it more affordable to use AI technologies.

## Using OpenAI’s Tokenizer
To better understand how tokens work and how much text you are using in terms of tokens, you can use **OpenAI’s Tokenizer** tool.

🔗 **Link:** [OpenAI Tokenizer](https://platform.openai.com/tokenizer)  

This tool lets you see how different pieces of text are broken down into tokens, helping you estimate costs when using the LLM.

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/2c7bbec3-1c40-40e7-8a44-602bb1f28193" />

## Summary
When using LLMs through OpenAI’s tools, you will be charged based on the number of tokens your text uses.  
Tokens represent words or parts of words, and understanding them can help you manage costs effectively.  
As competition grows, prices are likely to decrease, making AI tools more accessible.

---

# Pricing Information for OpenAI API

## Where to Find Pricing
For the most up-to-date pricing details, visit: [OpenAI API Pricing](https://openai.com/api/pricing)

---

# Model Pricing (per 1 Million Tokens)

The cost for using OpenAI's models is typically broken down into two components:  
- **Prompt** (tokens you input)  
- **Response** (tokens the model generates)  

---

## GPT-4o
- **Prompt:** $2.50  
- **Response:** $10.00  

## GPT-4o-mini
- **Prompt:** $0.15  
- **Response:** $0.60  

## GPT-5
- **Prompt:** $1.25  
- **Response:** $10.00  

## GPT-5-mini
- **Prompt:** $0.25  
- **Response:** $2.00  

## GPT-3.5 Turbo
- **Prompt:** $0.50  
- **Response:** $1.50  

---

## Batch API
The **Batch API** offers a discounted rate for asynchronous, non-real-time processing of large volumes of data.  
- **Discount:** ~50% off standard API pricing.

---

## Embedding Models
Used for tasks like **search** and **topic classification**. Costs are based on **input tokens**.

- **text-embedding-3-small:** $0.02 per million tokens  
- **text-embedding-3-large:** $0.13 per million tokens  
- **text-embedding-ada-002:** $0.10 per million tokens  

---

## Fine-Tuning Models
Fine-tuning customizes a model with your own data. Pricing includes both **training** and **inference**.

### Fine-tuned GPT-3.5 Turbo
- **Training:** $8.00 per million tokens  
- **Input (Inference):** $3.00 per million tokens  
- **Output (Inference):** $6.00 per million tokens  

---

## Assistants API Pricing
Charges apply for the use of specific tools:

- **Code Interpreter:** $0.03 per session (session active for 1 hour).  
- **File Search:** $0.10 per GB of vector store storage per day.  
  - First GB is **free**.  
  - Fee applies when files are **attached** to an assistant or thread (not just when actively used).
 
Paying Extra for Special Tools in OpenAI's Assistants API.
>  Sometimes your helper (the AI) needs **special tools** to do certain tasks.  

Here’s how the pricing works for those tools:

#### **Code Interpreter** (The Math and Science Tutor)
- **Analogy:** Like hiring a math tutor who has a calculator and a scratchpad.
- **How it works:**  
  - You pay a fixed price for each *session* you hire them for.  
  - One session lasts about an hour, and they can do as many calculations as you want during that time for the same price.
- **Cost:** A small, fixed fee per session.

#### **File Search** (The Archivist)
- **Analogy:** Like hiring an archivist who organizes all your notes and books into a perfect library.
- **How it works:**  
  - You pay a small daily fee for every big box of notes (**gigabyte**) they store for you.  
  - The **first box is free**.
- **Cost:** A small daily fee for the storage space your files take up.


#### **Function Calling** (The Handyman)
- **Analogy:** Like your helper asking a handyman you already know to do a quick task (e.g., turn on a light).
- **How it works:**  
  - You don’t pay extra for the request itself.  
  - You only pay for the *words* (tokens) your helper uses to make the request, and the *words* the handyman uses to reply.
- **Cost:** Just the normal token cost (input + output).


---

## Tokens and Word Count
A good rule of thumb:  
>  - **1,000 tokens ≈ 750 words**  
This helps estimate your usage and costs.

---

# 1. OpenAI API (General API)

## What it is
The main service from OpenAI that lets you interact with AI models (like **GPT-4**, **GPT-4o**, etc.) to generate text, code, summaries, images, and more.

## How it works
- You send a **single prompt** → the model responds → done.
- You manage **all context, memory, and logic** in your own app.
- Example: You build a chatbot → every time the user asks a question, you send the **entire conversation so far** to the API.

**Analogy:**  
It’s like calling a smart friend every time you need help — but they forget everything after the call unless you remind them.

---

# 2. Assistants API (Framework Layer)

## What it is
A framework built **on top of the OpenAI API** that helps you create AI "assistants" with:
- Memory
- Tools
- Step-by-step task handling

## How it works
You define an assistant with:
- **Instructions** (personality, goals)
- **Tools** (code execution, file search, APIs)
- **Persistent memory** (remembers between chats or tasks)

The assistant can:
- Handle **multi-turn conversations**
- Keep **history** without you sending it every time
- **Use tools automatically** when needed

**Analogy:**  
It’s like hiring a personal secretary who:
- Knows your preferences
- Keeps notes of past conversations
- Can use your computer tools to get work done without you micromanaging

---

## Key Differences

| Feature          | OpenAI API                                          | Assistants API                                     |
|------------------|-----------------------------------------------------|----------------------------------------------------|
| **Memory**       | No built-in memory — you must send all context       | Built-in long-term memory                          |
| **Tool Use**     | You must code tool integrations yourself            | Supports tool calling natively                     |
| **Multi-step Tasks** | You handle flow manually                        | Assistant manages multi-turn workflow              |
| **Setup**        | Just model + prompt                                 | Assistant profile + tools + instructions           |
| **Best for**     | Quick single responses                              | Persistent, capable AI agents                      |

---

## In Short
- **OpenAI API** → Raw access to AI models, **you** control everything.  
- **Assistants API** → Ready-made framework for building **AI agents** that remember, reason, and use tools.

