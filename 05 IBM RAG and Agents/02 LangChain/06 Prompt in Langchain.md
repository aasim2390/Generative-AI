## 📘 Notes on Prompts in LangChain

Prompts are the instructions we give to a language model (like GPT).

The way you design them decides what kind of answer you get.

👉 One-liner: “Prompt = Recipe. Good recipe → Good dish.”

---

### 🔹 What is a Prompt?

A prompt is text (or other input) that tells the model what to do.

It controls tone, format, and accuracy of the model’s output.

**Example:**
```python
"Explain gravity in 2 sentences."
```

### 🔹 Input Types

Text-based → normal strings.

Multimodal → some models also accept images, audio, or video, but LangChain mostly works with text.

👉 One-liner: “Prompts talk to the brain of AI—words are the language.”

| Type    | Meaning                 | Example                           |
| ------- | ----------------------- | --------------------------------- |
| Static  | Fixed, no variables     | `"Tell me a joke about cats."`    |
| Dynamic | Template with variables | `"Tell me a joke about {animal}"` |

```python
from langchain_core.prompts import PromptTemplate

tpl = PromptTemplate.from_template(
    "Explain {topic} in {length} sentences."
)
```

👉 One-liner: “Static is frozen, Dynamic adapts.”

---

### 🔹 Why use PromptTemplate?

- Validation → ensures required variables are filled.

- Reuse → save & load prompts easily.

```python
template.save("mytemplate.json")
load_prompt("mytemplate.json")
```

- Ecosystem fit → works smoothly inside LangChain chains.

👉 One-liner: “PromptTemplate = Reusable Lego block for prompts.”

---

### 🔹 ChatPromptTemplate

Lets you build multi-message conversations with roles (system, human, AI).

Good for making chatbots.

Example:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_tpl = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chat_tpl.format_messages(question="What is 2+2?")

```

👉 One-liner: “ChatPrompt = Multi-turn conversation recipe.”

---

### 🔹 MessagesPlaceholder

Special slot to insert conversation history into a prompt.

Keeps context alive.

Example:
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_tpl = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

chat_tpl.invoke({
    "history": [("human", "Hi"), ("ai", "Hello!")],
    "question": "How are you?"
})

```

👉 One-liner: “Placeholder = Memory slot for past chats.”
---

### 🔹 Simple Chatbot Example

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

chat_tpl = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Type 'quit' to exit."),
    MessagesPlaceholder("history"),
    ("human", "{user_input}")
])

history = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        print("Bye!")
        break
    history.append(("human", user_input))
    resp = llm.invoke(chat_tpl.invoke({"history": history, "user_input": user_input}))
    print("Bot:", resp.content)
    history.append(("ai", resp.content))
```

👉 One-liner: “Chatbot = ChatPrompt + Memory + Loop.”

---

### 🔹 Advanced Prompting
1. Dynamic Few-Shot

Instead of fixed examples, pick the most relevant examples at runtime.

Saves tokens and improves relevance.

Example:

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS

examples = [
    {"question": "What is GPT?", "answer": "GPT is a large language model."},
    {"question": "Define Transformer.", "answer": "Transformer is a neural model for sequence modeling."}
]

# Build simple example store
tpl = PromptTemplate.from_template("Q: {question}\nA: {answer}")
docs = [tpl.format(**ex) for ex in examples]

emb = OpenAIEmbeddings()
db = FAISS.from_texts(docs, emb)

query = "Explain what a large language model is?"
relevant = db.similarity_search(query, k=1)

few_shot = "\n".join([d.page_content for d in relevant])
prompt = f"{few_shot}\n\nQ: {query}\nA:"
llm = ChatOpenAI()
print(llm.invoke(prompt))

```

👉 One-liner: “Few-shot = Learn by example, dynamic = right example at the right time.”

---

### 2. Meta / Adaptive Prompting

Use a model to improve or rewrite prompts.

Great for refining unclear instructions.

Example:
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

# Meta-prompt
initial = "Explain photosynthesis simply."

meta_prompt = f"""
You are a prompt engineer. Rewrite this prompt to be clearer:
'{initial}'
"""
refined = llm.invoke(meta_prompt).content
print("Refined Prompt:", refined)

# Use refined prompt
print("Answer:", llm.invoke(refined).content)

```

👉 One-liner: “Meta-prompting = AI helps you write better prompts.”

---

### ✅ Quick Recap

Prompt → Instructions (the recipe).

Static vs Dynamic → Fixed vs flexible.

PromptTemplate → Reusable validated recipes.

ChatPromptTemplate → Multi-turn chat.

MessagesPlaceholder → Keeps history.

Few-Shot → Learn by examples.

Dynamic Few-Shot → Pick examples smartly.

Meta/Adaptive → AI refines prompts.

Chatbot → Glue them together.

👉 Final One-liner: “Prompts are recipes, templates are cookbooks, chat prompts serve meals, few-shot learns from past dishes, meta-prompting makes the recipe better.”
