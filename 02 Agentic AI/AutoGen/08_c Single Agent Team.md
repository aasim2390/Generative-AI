# 🧑‍💻 Single-Agent Team in AutoGen

---

## 🔹 What is a Single-Agent Team?
- A **single agent** running inside a **team configuration**.
- Useful when you want the agent to **loop through multiple steps** until a **termination condition** is met.
- Different from calling `agent.run()` or `agent.run_stream()` which only perform **one step**.

---

## 🔹 Why Use It?
- To run the **AssistantAgent in a loop** (like an iterative worker).
- Example use cases:
  - Keep **calling a tool** until a condition is satisfied.
  - Perform **step-by-step reasoning** until completion.

---

## 🔹 Important Note
- **Since v0.6.2**:  
  You can use `AssistantAgent` with `max_tool_iterations` for multi-step tool calls.  
  - ✅ In many cases, you may **not need a single-agent team** if looping tool calls is your only goal.  

---

## 🔹 Example Behavior
- Agent is placed in a **RoundRobinGroupChat** team (even though it's just one agent).  
- A **TextMessageTermination** condition stops execution when the goal is reached.  
- Example task:  
  - Agent starts with number = 1.  
  - Keeps calling a **tool to increment** the number.  
  - Stops when the number reaches **10**, returning a final `TextMessage`.

---

## ✅ Key Takeaways
- **Single-Agent Team** = useful for iterative runs with termination logic.  
- **`agent.run()`** = single step only.  
- **Single-Agent Team** = multi-step until condition is met.  
- **`max_tool_iterations`** (v0.6.2+) = simpler alternative for tool-calling loops.

---

## Code Example

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ext.models.openai import OpenAIChatCompletionClient

async def main():
    # 1️⃣ Create the model client
    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # 2️⃣ Define a simple tool to increment a number
    def increment(number: int) -> int:
        return number + 1

    # 3️⃣ Create a single-agent with max_turns=3
    agent = AssistantAgent(
        "counter_agent",
        model_client=model_client,
        tools=[increment],
        system_message="Increment the number using the tool.",
        max_turns=3  # Agent will run 3 iterations
    )

    # 4️⃣ Wrap the agent in a RoundRobinGroupChat team (even if single agent)
    team = RoundRobinGroupChat([agent])

    # 5️⃣ Run the team with a task
    async for msg in team.run_stream("Start at number 1 and increment 3 times."):
        print(msg)

    # 6️⃣ Close the model client
    await model_client.close()

asyncio.run(main())

```

### Step-by-Step Explanation

- Model client: Connects to OpenAI GPT model.
- Tool: increment(number) → adds 1 to a number.
- AssistantAgent:
  - Has the tool registered.
  - max_turns=3 → will automatically run 3 iterations.
- Single-Agent Team:
  - Wrapped in a RoundRobinGroupChat.
  - Even though there’s only one agent, team structure allows iteration handling.
- Run:
  - Task: “Start at 1, increment 3 times.”
  - Agent calls increment → number goes 1 → 2 → 3 → 4.
- Stop: After 3 turns, the run automatically ends.

### ✅ Key Points

- Single-Agent Team can loop the agent using max_turns.
- No explicit termination condition is needed for a fixed number of iterations.
- Useful for repetitive tool-calling tasks.
