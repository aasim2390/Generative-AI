# 👥 Multi-Agent RoundRobin Team in AutoGen

---

## 🔹 Definition
A **Multi-Agent RoundRobin Team** is a group of agents that **take turns in a fixed order** to complete a task.  
- Each agent can have its **own persona, skills, or tools**.  
- Useful for **collaborative or sequential tasks**.  
- The team continues until a **termination condition** is met (e.g., max turns, text output, or custom condition).

---

## 🔹 Key Points to Remember
1. **RoundRobin Order**: Agents speak in a predefined sequence (AgentA → AgentB → AgentC → repeat).  
2. **Shared Context**: All agents can see previous messages in the team’s conversation.  
3. **Termination**: Always define a termination condition to stop the team safely:
   - `TextMessageTermination`: stops on specific agent message.
   - `MaxTurnsTermination`: stops after a fixed number of turns.
   - Custom conditions: user-defined logic to end the task.
4. **Tools**: Each agent can have tools registered to perform actions or calculations.  
5. **Max Turns Example**: `MaxTurnsTermination(max_turns=4)` ensures the team stops after 4 turns.  
6. **Iteration & Collaboration**: Multi-agent teams allow agents to **build on each other’s outputs** in a structured way.  
7. **Use Cases**:
   - Step-by-step tasks (e.g., counting, calculations, brainstorming).  
   - Multi-step reasoning where different agents contribute different expertise.

---

## 🔹 Code Example: Multi-Agent RoundRobin with 4 Turns

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxTurnsTermination
from autogen_agentchat.ext.models.openai import OpenAIChatCompletionClient

async def main():
    # 1️⃣ Model client
    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # 2️⃣ Simple increment tool
    def increment(number: int) -> int:
        return number + 1

    # 3️⃣ Create two agents
    agent_a = AssistantAgent(
        "AgentA",
        model_client=model_client,
        tools=[increment],
        system_message="You are AgentA, increment the number."
    )

    agent_b = AssistantAgent(
        "AgentB",
        model_client=model_client,
        tools=[increment],
        system_message="You are AgentB, increment the number."
    )

    # 4️⃣ Stop the team after 4 turns
    termination = MaxTurnsTermination(max_turns=4)

    # 5️⃣ Create the RoundRobin team
    team = RoundRobinGroupChat([agent_a, agent_b], termination_condition=termination)

    # 6️⃣ Run the team
    async for msg in team.run_stream("Start at 1 and take turns incrementing the number."):
        print(msg)

    # 7️⃣ Close the model client
    await model_client.close()

asyncio.run(main())
```

### ✅ Summary

- Multi-Agent RoundRobin teams are **ideal for collaborative tasks** where turn-taking is needed.
- Always use a **termination condition** like `MaxTurnsTermination` to avoid infinite loops.
- Each agent can have **different tools or personas**, enabling flexible workflows.

---

# 👥 Multi-Agent RoundRobin: Assistant + Critic Example

---

## 🔹 Scenario
- Task: Provide an answer to a question and then review it.  
- **Agent Roles**:
  1. **AssistantAgent** → provides the answer.  
  2. **CriticAgent** → reviews, critiques, or improves the answer.  
- **Team Type**: RoundRobin → agents take turns.

---

## 🔹 Key Points
1. **Different personas**: Each agent has a unique system message describing their role.  
2. **Shared context**: Critic sees what Assistant wrote.  
3. **Termination condition**: Stops after a fixed number of turns (e.g., 2 turns: Assistant → Critic).  
4. **Collaboration**: Allows structured feedback loops in multi-agent systems.

---

## 🔹 Code Example

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxTurnsTermination
from autogen_agentchat.ext.models.openai import OpenAIChatCompletionClient

async def main():
    # 1️⃣ Model client
    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # 2️⃣ Create Assistant agent
    assistant = AssistantAgent(
        "Assistant",
        model_client=model_client,
        system_message="You are a helpful assistant. Provide clear answers to questions."
    )

    # 3️⃣ Create Critic agent
    critic = AssistantAgent(
        "Critic",
        model_client=model_client,
        system_message="You are a critic. Review the assistant's answers and suggest improvements or corrections."
    )

    # 4️⃣ Termination: stop after 2 turns (Assistant + Critic)
    termination = MaxTurnsTermination(max_turns=2)

    # 5️⃣ Create RoundRobin team
    team = RoundRobinGroupChat([assistant, critic], termination_condition=termination)

    # 6️⃣ Run the team with a task
    async for msg in team.run_stream("Explain why the sky is blue in simple terms."):
        print(msg)

    # 7️⃣ Close model client
    await model_client.close()

asyncio.run(main())
```

## 🔹 How It Works

- **Turn 1** → Assistant: Answers the question.
- **Turn 2** → Critic: Reviews the assistant’s answer and suggests improvements.
- **Termination:** MaxTurnsTermination ensures the team stops after 2 turns.
- **Collaboration:** Each agent uses the **shared context** to see previous messages.
