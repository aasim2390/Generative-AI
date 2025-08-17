# 🛑 Termination in AgentChat

In the previous section, we explored how to **define agents** and organize them into **teams** that can solve tasks.  
However, a run can go on forever, and in many cases, we need to know **when to stop them**.  
This is the role of the **termination condition**.

---

## 🔹 What is a Termination Condition?
- `AgentChat` provides a base `TerminationCondition` class and several implementations that inherit from it.
- A **termination condition** is a callable that:
  1. Takes a sequence of `BaseAgentEvent` or `BaseChatMessage` objects (since the last time it was called).
  2. Returns a **StopMessage** if the conversation should be terminated, or `None` otherwise.

---

## 🔹 Key Points
- ✅ Termination conditions are **stateful** but **reset automatically** after each run (`run()` or `run_stream()`).
- ✅ They can be combined using **`AND`** and **`OR`** operators.

---

## 🔹 Group Chat Teams
For **group chat teams** (e.g., `RoundRobinGroupChat`, `SelectorGroupChat`, and `Swarm`):
- The termination condition is called **after each agent responds**.
- While a response may contain multiple inner messages, the team calls its termination condition **once per response**.
- The condition is called with the **delta sequence** of messages since the last time it was called.

---

⚡ **Summary**:  
Termination conditions help ensure conversations stop at the right moment, preventing infinite loops and allowing structured control over agent interactions.


---

# 🛑 When to Stop a Chat (Termination) - In Simple Words

Imagine you are chatting with a group of friends.  
If no one decides when to stop, the chat could go on **forever**.  

In `AgentChat`, we use something called a **termination condition** to decide **when the chat should end**.

---

## 🔹 What is a Termination Condition?
- It’s like a **rule** that checks the conversation.
- If the rule says "✅ Stop now", the chat ends.  
- If the rule says "❌ Keep going", the chat continues.

---

## 🔹 Important Things
- The rule can remember what already happened in the chat.  
- After every full chat (a `run()`), the rule resets and forgets old stuff.  
- You can combine rules like:
  - **AND** → Chat stops only if *both* rules say stop.
  - **OR** → Chat stops if *any* rule says stop.

---

## 🔹 Group Chat Teams
For group chats (like when 3-4 agents are talking):
- The rule is checked **every time someone replies**.  
- Even if one reply has many small messages, the rule checks only **once per reply**.  
- The rule only looks at the **new messages** since the last time it checked.

---

⚡ **In Simple Words**:  
A **termination condition** is just a **stop sign** 🚦 for the chat.  
It makes sure the chat doesn’t go on forever and ends at the right time.


---

## Here are some common types:

---

## 1. MaxMessageTermination
- 📌 **What it means:** The chat ends after a certain number of messages.
- 🧑‍🏫 Example:  
  "Stop the conversation after 10 total messages (from both agents and tasks)."

---

## 2. TextMentionTermination
- 📌 **What it means:** The chat ends when a special word or phrase shows up.  
- 🧑‍🏫 Example:  
  If someone types **"TERMINATE"**, the conversation stops.

---

## 3. TokenUsageTermination
- 📌 **What it means:** The chat ends if the agents use too many tokens (words/characters).  
- 🧑‍🏫 Example:  
  Imagine you’re allowed to write only **2000 words in total**. If you reach that, the system stops.

---

## 4. TimeoutTermination
- 📌 **What it means:** The chat ends after a certain amount of time has passed.  
- 🧑‍🏫 Example:  
  "Stop this conversation after 30 seconds."

---

## 5. HandoffTermination
- 📌 **What it means:** The chat ends (or pauses) when one agent **hands the task to someone else**.  
- 🧑‍🏫 Example:  
  If Agent A says, *“I’m handing this task to Agent B”*, the system stops and waits for input.

---

# 🎯 In short:
- 📝 **MaxMessageTermination** → "Stop after X messages."  
- 🔤 **TextMentionTermination** → "Stop if you see this word."  
- 🗣️ **TokenUsageTermination** → "Stop after using too many words."  
- ⏱️ **TimeoutTermination** → "Stop after X seconds."  
- 🤝 **HandoffTermination** → "Stop when someone passes the task."  

---

## Code Example

```python
# Importing required classes from autogen libraries
from autogen_agentchat.agents import AssistantAgent   # Used to create AI agents (like chat participants)
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination  # Used to stop chat after some conditions
from autogen_agentchat.teams import RoundRobinGroupChat  # Used to make agents talk in turns
from autogen_agentchat.ui import Console  # Used to display the chat in console
from autogen_ext.models.openai import OpenAIChatCompletionClient  # Connects to OpenAI models like GPT


# ​​​ Step 1: Initialize the AI model client
# Think of this as "choosing which brain" the agents will use.
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",   # The model (brain) they will use
    api_key=OPENAI_API_KEY,  # Your OpenAI key (like a password)
    temperature=1  # Controls creativity (higher = more creative answers)
)


# Step 2: Create the first agent (helper AI)
primary_agent = AssistantAgent(
    "primary",  # Agent name
    model_client=model_client,  # The brain it uses
    system_message="You are a helpful AI assistant.",  # How it should behave
)


# Step 3: Create the second agent (critic AI)
critic_agent = AssistantAgent(
    "critic",  # Agent name
    model_client=model_client,  # Same brain as primary
    system_message=(
        "Provide constructive feedback for every message. "
        "Respond with 'APPROVE' when your feedbacks are addressed."
    ),  # This agent checks and gives feedback
)


# Step 4: Set a termination condition (when to stop the chat)

# ----------------------------
# Example with one stop condition
# ----------------------------
# Here, stop after 3 messages in total
max_msg_termination = MaxMessageTermination(max_messages=3)


# Step 5: Create a team with both agents
# RoundRobin = each agent takes turns talking
round_robin_team = RoundRobinGroupChat(
    [primary_agent, critic_agent],
    termination_condition=max_msg_termination  # Stop after 3 messages
)


# Step 6: Run the team and display chat in console
# (If running as a script, use asyncio.run(...))
await Console(round_robin_team.run_stream(task="Write a unique, Haiku about the weather in Paris"))



# ----------------------------
# Example with multiple stop conditions
# ----------------------------

# Condition 1: Stop after 10 messages
max_msg_termination = MaxMessageTermination(max_messages=10)

# Condition 2: Stop if someone says "APPROVE"
text_termination = TextMentionTermination("APPROVE")

# Combine both conditions using OR (|).
# Chat will stop if EITHER condition happens.
combined_termination = max_msg_termination | text_termination


# Create the team again with combined rules
round_robin_team = RoundRobinGroupChat(
    [primary_agent, critic_agent],
    termination_condition=combined_termination
)


# Run again with the new termination rules
await Console(round_robin_team.run_stream(task="Write a unique, Haiku about the weather in Paris"))

```
