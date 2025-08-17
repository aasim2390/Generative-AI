# Agent Run vs Team Run in AutoGen

## 🔹 Agent Run
- **Definition:** A single agent is asked to complete a task.  
- **How it works:**
  - Uses its own **model client**, **system instructions**, and **tools**.
  - Handles the entire job **alone**.
  - Maintains its **own conversation history**.
- **When to use:**  
  - Task is **simple or well-defined**.
  - Only **one skillset/persona** is needed.

**Example:**
```python
result = await agent.run(task="Translate this text into French")
print(result.messages[-1].content)
```

👉 The agent does everything itself.

## 🔹 Team Run
- **Definition:** A group of agents (team) is asked to complete a task together.
- **How it works:**
  - Multiple agents collaborate in a shared conversation context.
  - Turn-taking depends on the team preset (RoundRobin, Selector, Swarm, MagenticOne).
  - Agents can hand over tasks, build on each other’s outputs, or specialize.
- **When to use:**
  - Rask is complex, multi-step, or requires different expertise.
  - Example: Research + Writing + Coding + Reviewing.


**Example:**
```python
result = await team.run(task="Research climate change and write a summary report")
print(result.messages[-1].content)
```
👉 Team members take turns, share context, and finish the task together.


| Feature      | Agent Run 🧑               | Team Run 👥                   |
| ------------ | -------------------------- | ----------------------------- |
| Who works?   | One agent                  | Multiple agents               |
| Context      | Private to agent           | Shared among team             |
| Best for     | Simple, single-skill tasks | Complex, multi-skill tasks    |
| Example task | Translate a sentence       | Research + summarize + review |
