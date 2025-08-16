
# AutoGen v0.4 Overview  

AutoGen v0.4 is a framework for building multi-agent AI systems with an asynchronous, event-driven architecture.  

## Key Improvements Over Previous Versions  
- A redesigned **Core layer** for scalability.  
- **AgentChat**, a simplified high-level API for agent interactions.  
- **Extensions** for integrating external tools and data.  

---

## Agents in AutoGen AgentChat  

`AutoGen AgentChat` provides a set of preset Agents, each with variations in how an agent might respond to messages.  

### Shared Attributes & Methods  

- **name**: The unique name of the agent.  
- **description**: The description of the agent in text.  
- **run**:  
  - Executes the agent given a task as a string or a list of messages.  
  - Returns a **TaskResult**.  
  - Agents are expected to be **stateful**, and this method is expected to be called with **new messages only**, not the complete history.  
- **run_stream**:  
  - Similar to `run()` but returns an **iterator of messages** that subclass `BaseAgentEvent` or `BaseChatMessage`.  
  - The last item in the iteration is a **TaskResult**.  

---

## Example Usage (Python)  

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from dotenv import load_dotenv
import os

model_client = OpenAIChatCompletionClient(model='gpt-4o', api_key=api_key)

async def web_search(query: str) -> str:
    """Find information on the web"""
    return "The Labrador Retriever or simply Labrador is a British breed of retriever gun dog. "

agent = AssistantAgent(
    name='assistant',
    model_client=model_client,
    tools=[web_search],
    system_message='Use Tools to solve tasks', #This system message will go to brain - model_client
    description='An agent which uses tool to help solve task'
)

# Create agents
result = await agent.run(task='Find information about Labrador Retriever')
print(result.messages[-1].content)

```

<img width="682" height="427" alt="image" src="https://github.com/user-attachments/assets/f9592596-14dc-469a-8c07-ae1670498b00" />


---

# Understanding `run` in AutoGen AgentChat

## 🔹 What is `run`?
The **`run` method** is how you "talk" to an agent and ask it to do something.  
Think of it like giving instructions to a person — you say *"Do this task"* and they give you back the result.

---

## 🔹 How it works
- You give `run` a **task** → this can be:
  - A single string (example: `"Summarize this article"`), or  
  - A list of messages (like a chat history).  

- The agent thinks, processes the task, and returns a **TaskResult** (the output).  

- Important: The agent is **stateful** → it remembers context from earlier runs.  
  So, when you call `run`, you’re expected to give it **only new input**, not the whole history again.

---

## 🔹 Example
```python
result = agent.run("Translate this sentence to French: Hello, how are you?")
print(result.output)
```

👉 Here, you ask the agent to translate a sentence.
👉 The run method sends your instruction to the agent.
👉 It gives back the translation inside TaskResult.

### 🔹 In Simple Words

- run = “Ask the agent to do something now”
- Input = task (string or messages)
- Output = TaskResult (agent’s answer)

Don’t resend old chat history every time — just the new message
