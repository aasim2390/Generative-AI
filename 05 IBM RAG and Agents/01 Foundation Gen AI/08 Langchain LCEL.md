# 🚀 LangChain LCEL Chaining Method – Explained with Examples

---

## 1️⃣ What is LCEL?

**LangChain Expression Language (LCEL)** is a modern way to **connect AI components** in a clean, readable workflow.

 - Uses the **pipe operator** `|` to pass data from one step to another.
 - Makes AI workflows **flexible, reusable, and easy to read.**
 - Automatically converts normal functions, templates, or dictionaries into components **(type coercion).**
 - Best for **simpler chains**, can be used inside bigger systems like LangGraph.

Think of it like:
- **Recipe** → template
- **Prep station** → RunnableLambda
- **Chef** → LLM
- **Conveyor belt** → pipe `|`
- **Team of chefs** → RunnableParallel / RunnableSequential

## 2️⃣ LCEL Key Components

| Component            | What it does                             | Analogy                                                |
| -------------------- | ---------------------------------------- | ------------------------------------------------------ |
| **PromptTemplate**   | Defines instructions with placeholders   | Recipe card                                            |
| **RunnableLambda**   | Wraps a function to work in LCEL         | Prep station                                           |
| **Pipe**             | Passes output from one step to the next  |  Conveyor belt                                         |
| **RunnableSequence** | Runs steps **one after another**         | Line of chefs working sequentially                     |
| **RunnableParallel** | Runs **multiple steps at the same time** | Multiple chefs cooking at once                         |
| **StrOutputParser**  | Cleans and formats AI output             | Plate the dish nicely                                  |

## 3️⃣ LCEL Use Cases

| Use Case           | Example                                                      |
| ------------------ | ------------------------------------------------------------ |
| Summarization      | Summarize articles, homework notes, essays                   |
| Translation        | English → French/Spanish/Japanese                            |
| Sentiment Analysis | Detect if a product review is positive, negative, or neutral |
| Content Generation | Write jokes, stories, or blog posts                          |
| Parallel Tasks     | Run summary, translation, sentiment at the same time         |
| Reusable Pipelines | Reuse the chain for multiple inputs                          |


**Example:**
- Input = "AI can summarize text, translate, and write poems."
- Parallel output = summary, translation, sentiment, joke

## 4️⃣ Sequential LCEL Example (Step by Step)

### Step 1: Imports

```bash
!pip install langchain_community
```

```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
import os
from google.colab import userdata

OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

```

### Step 2: LLM Setup
```python

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo",api_key=OPENAI_API_KEY)

```

### Step 3: Prompt Templates
```python

template1 = PromptTemplate(input_variables=["text"], template="Summarize this: {text}")
template2 = PromptTemplate(input_variables=["text"], template="Translate this into French: {text}")
template3 = PromptTemplate(input_variables=["text"], template="Analyze sentiment: {text}")

```

### Step 4: Wrap Templates in RunnableLambda
```python

step1 = RunnableLambda(lambda x: template1.format_prompt(text=x))
step2 = RunnableLambda(lambda x: template2.format_prompt(text=x))
step3 = RunnableLambda(lambda x: template3.format_prompt(text=x))

```

### Step 5: Create Sequential Chain
```python

chain = RunnableSequence(step1 | llm | StrOutputParser(),
                           step2 | llm | StrOutputParser(),
                           step3 | llm | StrOutputParser())

```

### Step 6: Run Chain

```python

input_text = "AI can summarize text, translate, and write poems."
results = chain.invoke(input_text)
print(results)

```

**Output:**
```bash
Overall, the sentiment expressed in this statement is positive. It highlights the capabilities of artificial intelligence (IA) to condense text, translate languages, and create poetry. The use of words such as "capacité" (ability) and "créer de la poésie" (create poetry) suggests a tone of admiration and appreciation for the potential of AI technology.

```

**Sequential Flow:**
> ***Input → Summary → Translation → Sentiment → Output***

## 5️⃣ Parallel LCEL Example

```python

tasks = RunnableParallel({
    "summary": step1 | llm | StrOutputParser(),
    "translation": step2 | llm | StrOutputParser(),
    "sentiment": step3 | llm | StrOutputParser()
})

results = tasks.invoke(input_text)
print(results)

```
**Output:**
```bash
{'summary': 'AI technology can perform various tasks such as summarizing text, translating languages, and even creating poems.', 'translation': "L'IA peut résumer du texte, traduire et écrire des poèmes.", 'sentiment': 'Positive sentiment: The statement highlights the advanced capabilities of AI in summarizing text, translating languages, and even writing poems. This showcases the potential of AI technology to assist in various tasks and demonstrate creativity.'}

```
**Parallel Flow:**
> ***Input → Summary, Translation, Sentiment (all at the same time) → Output***

## 6️⃣ LCEL Advantages

- **Clear flow of data** using pipes `|`
- **Sequential or parallel execution**
- **Reusable and composable chains**
- **Auto type conversion** (functions → runnable components)
- **Async and streaming support**
- Perfect for LLMs and Generative AI tasks

## 7️⃣ Memorable Analogy

|     Concept      |               Analogy                  |              
| ---------------- | -------------------------------------- | 
| PromptTemplate   | Recipe card                            | 
| RunnableLambda   | Prep station                           | 
| Pipe             | Conveyor belt                          | 
| RunnableSequence | Line of chefs, one after another       | 
| RunnableParallel | Team of chefs working at the same time | 
| LLM              | Chef cooking the dish                  | 
| StrOutputParser  | Plating the dish nicely                | 
| Input            | Raw ingredients                        | 
| Output           | Finished meal                          | 


### ✅ Quick Reference Cheat Sheet

LCEL Steps

1. Create PromptTemplate
2. Wrap in RunnableLambda
3. Connect with pipe |
4. Use RunnableSequence (sequential) or RunnableParallel (parallel)
5. Send input → get output

### Example
```python

step1 | llm | StrOutputParser()  # Sequential

{"summary": step1, "sentiment": step3}  # Parallel

```

