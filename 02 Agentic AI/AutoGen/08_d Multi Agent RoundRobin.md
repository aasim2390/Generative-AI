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
# ----------------------------
# Import required libraries
# ----------------------------
import asyncio  # For handling async/await operations (event loop management)
from autogen_agentchat.agents import AssistantAgent  # Class to create assistant agents
from autogen_agentchat.teams import RoundRobinGroupChat  # Team structure where agents take turns
from autogen_agentchat.conditions import MaxMessageTermination  # Rule to stop conversation
from autogen_ext.models.openai import OpenAIChatCompletionClient  # OpenAI API client

# ----------------------------
# 1️⃣ Initialize the model client
# ----------------------------
# This connects to the OpenAI API using your API key and chosen model.
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",   # Use the GPT-4o mini model for efficiency
    api_key=OPENAI_API_KEY  # Your OpenAI API key must be defined before this line
)

# ----------------------------
# 2️⃣ Define a simple tool (increment function)
# ----------------------------
# Agents can call this function as a "tool".
def increment(number: int) -> int:
    return number + 1  # Simply adds 1 to the input number

# ----------------------------
# 3️⃣ Create two assistant agents
# ----------------------------
# Each agent has a role and can use the "increment" tool.

agent_a = AssistantAgent(
    "AgentA",                  # Name of agent
    model_client=model_client, # Attach the model client
    tools=[increment],         # Give this agent access to the increment tool
    system_message="You are AgentA, increment the number."  # Instructions for this agent
)

agent_b = AssistantAgent(
    "AgentB",                  
    model_client=model_client,
    tools=[increment],
    system_message="You are AgentB, increment the number."
)

# ----------------------------
# 4️⃣ Define when the chat should stop
# ----------------------------
# MaxMessageTermination ensures the conversation doesn’t go on forever.
termination = MaxMessageTermination(max_messages=4)  
# This means: stop after 4 messages total (2 turns per agent).

# ----------------------------
# 5️⃣ Create a RoundRobin Team
# ----------------------------
# RoundRobinGroupChat means agents take turns responding in order.
team = RoundRobinGroupChat(
    [agent_a, agent_b],                # Members of the team
    termination_condition=termination  # Stop rule
)

# ----------------------------
# 6️⃣ Define the task
# ----------------------------
# This is the starting prompt given to the team.
task = "Start at 1 and take turns incrementing the number."

# ----------------------------
# 7️⃣ Reset the team (clean state)
# ----------------------------
# Always reset before starting a new task.
await team.reset()  

# ----------------------------
# 8️⃣ Run the team and stream outputs
# ----------------------------
# Console() will print the messages from agents as they respond.
# NOTE: Console must be imported from autogen_agentchat.ui or similar.
await Console(team.run_stream(task=task))  

```


```bash
---------- TextMessage (user) ----------
Start at 1 and take turns incrementing the number.
---------- ToolCallRequestEvent (AgentA) ----------
[FunctionCall(id='call_XjYiQdZlWy2QuZLDta7cRKNn', arguments='{"number":1}', name='increment')]
---------- ToolCallExecutionEvent (AgentA) ----------
[FunctionExecutionResult(content='2', name='increment', call_id='call_XjYiQdZlWy2QuZLDta7cRKNn', is_error=False)]
---------- ToolCallSummaryMessage (AgentA) ----------
2
---------- ToolCallRequestEvent (AgentB) ----------
[FunctionCall(id='call_ul0QbmyxoRJESN7xXyq2oPg8', arguments='{"number":2}', name='increment')]
---------- ToolCallExecutionEvent (AgentB) ----------
[FunctionExecutionResult(content='3', name='increment', call_id='call_ul0QbmyxoRJESN7xXyq2oPg8', is_error=False)]
---------- ToolCallSummaryMessage (AgentB) ----------
3
---------- ToolCallRequestEvent (AgentA) ----------
[FunctionCall(id='call_cjeN59uCa2VqcfYBkOByOCdX', arguments='{"number":3}', name='increment')]
---------- ToolCallExecutionEvent (AgentA) ----------
[FunctionExecutionResult(content='4', name='increment', call_id='call_cjeN59uCa2VqcfYBkOByOCdX', is_error=False)]
---------- ToolCallSummaryMessage (AgentA) ----------
4
TaskResult(messages=[TextMessage(id='098dfea9-2761-48e1-945d-9a00f6dcc02a', source='user', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 27, 59, 624914, tzinfo=datetime.timezone.utc), content='Start at 1 and take turns incrementing the number.', type='TextMessage'), ToolCallRequestEvent(id='3382b361-e26a-4f35-bf11-ea3791225492', source='AgentA', models_usage=RequestUsage(prompt_tokens=64, completion_tokens=13), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 62204, tzinfo=datetime.timezone.utc), content=[FunctionCall(id='call_XjYiQdZlWy2QuZLDta7cRKNn', arguments='{"number":1}', name='increment')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(id='f41039fe-8dd6-4a04-b857-ad3f61e55e78', source='AgentA', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 65432, tzinfo=datetime.timezone.utc), content=[FunctionExecutionResult(content='2', name='increment', call_id='call_XjYiQdZlWy2QuZLDta7cRKNn', is_error=False)], type='ToolCallExecutionEvent'), ToolCallSummaryMessage(id='6144b5dc-ddcb-404d-b05a-03702c920f73', source='AgentA', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 65805, tzinfo=datetime.timezone.utc), content='2', type='ToolCallSummaryMessage', tool_calls=[FunctionCall(id='call_XjYiQdZlWy2QuZLDta7cRKNn', arguments='{"number":1}', name='increment')], results=[FunctionExecutionResult(content='2', name='increment', call_id='call_XjYiQdZlWy2QuZLDta7cRKNn', is_error=False)]), ToolCallRequestEvent(id='1d2034e0-ef83-49c2-8f42-98573cef277a', source='AgentB', models_usage=RequestUsage(prompt_tokens=72, completion_tokens=13), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 837820, tzinfo=datetime.timezone.utc), content=[FunctionCall(id='call_ul0QbmyxoRJESN7xXyq2oPg8', arguments='{"number":2}', name='increment')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(id='7da685d5-f626-4a4b-a856-0e2e62ca9710', source='AgentB', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 840073, tzinfo=datetime.timezone.utc), content=[FunctionExecutionResult(content='3', name='increment', call_id='call_ul0QbmyxoRJESN7xXyq2oPg8', is_error=False)], type='ToolCallExecutionEvent'), ToolCallSummaryMessage(id='1ce0182f-8bc3-41a9-8112-a5af76d704d8', source='AgentB', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 2, 840458, tzinfo=datetime.timezone.utc), content='3', type='ToolCallSummaryMessage', tool_calls=[FunctionCall(id='call_ul0QbmyxoRJESN7xXyq2oPg8', arguments='{"number":2}', name='increment')], results=[FunctionExecutionResult(content='3', name='increment', call_id='call_ul0QbmyxoRJESN7xXyq2oPg8', is_error=False)]), ToolCallRequestEvent(id='db3b253d-6867-4a92-9612-cf3a3fafb6aa', source='AgentA', models_usage=RequestUsage(prompt_tokens=93, completion_tokens=13), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 3, 890770, tzinfo=datetime.timezone.utc), content=[FunctionCall(id='call_cjeN59uCa2VqcfYBkOByOCdX', arguments='{"number":3}', name='increment')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(id='97455fea-da06-4200-b379-a3b2d1f68982', source='AgentA', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 3, 893738, tzinfo=datetime.timezone.utc), content=[FunctionExecutionResult(content='4', name='increment', call_id='call_cjeN59uCa2VqcfYBkOByOCdX', is_error=False)], type='ToolCallExecutionEvent'), ToolCallSummaryMessage(id='aff68b01-273d-4228-9a85-a66d6315a13c', source='AgentA', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 28, 3, 894089, tzinfo=datetime.timezone.utc), content='4', type='ToolCallSummaryMessage', tool_calls=[FunctionCall(id='call_cjeN59uCa2VqcfYBkOByOCdX', arguments='{"number":3}', name='increment')], results=[FunctionExecutionResult(content='4', name='increment', call_id='call_cjeN59uCa2VqcfYBkOByOCdX', is_error=False)])], stop_reason='Maximum number of messages 4 reached, current message count: 4')

```

### 🔎 What happened in this run?

1. User Prompt: The task given was → "Start at 1 and take turns incrementing the number."
2. AgentA’s First Turn:
   - Calls the tool increment(1) → gets result 2.
   - Sends back summary message "2".
3. AgentB’s Turn:
   - Calls the tool increment(2) → gets result 3.
   - Sends back summary message "3".
4. AgentA’s Second Turn:
   - Calls the tool increment(3) → gets result 4.
   - Sends back summary message "4".
5. Termination Condition:
   - The MaxMessageTermination(max_messages=4) rule was triggered.
   - Conversation stopped after 4 total messages (A → B → A).

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
import asyncio  # Provides tools to run asynchronous code (like async/await)
from autogen_agentchat.agents import AssistantAgent  # Import AssistantAgent class to define agents
from autogen_agentchat.teams import RoundRobinGroupChat  # Import team type that makes agents talk in round-robin style
from autogen_agentchat.conditions import MaxMessageTermination  # Import termination condition to stop after fixed turns
from autogen_ext.models.openai import OpenAIChatCompletionClient  # Import OpenAI client wrapper for chat completion
from autogen_agentchat.ui import Console  # Console helper to print agent messages in terminal

# ​​​ Initialize the model client (this connects to OpenAI API with your key & model)
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

# 2️⃣ Create Assistant agent
assistant = AssistantAgent(
        "Assistant",  # Name of the agent
        model_client=model_client,  # Connect this agent to the OpenAI model client
        system_message="You are a helpful assistant. Provide clear answers to questions."  # Role/instructions for the agent
    )

# 3️⃣ Create Critic agent
critic = AssistantAgent(
        "Critic",  # Name of this second agent
        model_client=model_client,  # Same model client (could be different if needed)
        system_message="You are a critic. Review the assistant's answers and suggest improvements or corrections."  
        # This role is to act like a reviewer/critic for assistant's answers
    )

# 4️⃣ Termination condition: stop after 4 messages (2 from Assistant + 2 from Critic)
termination = MaxMessageTermination(max_messages=4)

# Task for the agents to discuss/answer
task = "Explain why the sky is blue in simple terms."

# 5️⃣ Create a RoundRobin team with assistant and critic
# This means Assistant speaks → Critic replies → Assistant again → Critic again → (until termination condition is met)
team = RoundRobinGroupChat([assistant, critic], termination_condition=termination)

# 6️⃣ Run the conversation in console (stream messages as they are generated)
await Console(team.run_stream(task=task))

# 7️⃣ Close the model client connection (clean up resources after conversation is done)
await model_client.close()

```


```bash
---------- TextMessage (user) ----------
Explain why the sky is blue in simple terms.
---------- TextMessage (Assistant) ----------
The sky looks blue because of a process called scattering. When sunlight enters the Earth's atmosphere, it hits tiny particles and gases in the air. Sunlight is made up of many colors, and each color has a different wavelength. Blue light has a shorter wavelength, so it gets scattered in all directions more than other colors. This scattering makes the sky appear blue to our eyes during the day.
---------- TextMessage (Critic) ----------
The explanation provided is quite clear and captures the essence of why the sky appears blue. However, there are a few areas that could be improved for simplicity and clarity:

1. **Simplify Vocabulary**: The term "scattering" might be too technical for some audiences. Consider using "spread out" or "bounced around" to make it more relatable.

2. **Add a Visual Element**: A brief mention of how this phenomenon relates to the colors of a rainbow could help provide a more comprehensive understanding.

3. **Contextual Comparison**: Including a comparison to other times when the sky changes color (like sunrise and sunset) could help illustrate why the blue sky occurs during the day specifically.

Revised explanation: 
"The sky looks blue because of a process where sunlight gets spread out when it hits tiny particles in the air. Sunlight has many colors, like red, green, and blue. The blue light gets bounced around more than the other colors because it travels in shorter waves. That's why, during the day, we see a blue sky. At sunrise and sunset, the sky can look orange or red because the sunlight has to pass through more air, which scatters the blue light away."
---------- TextMessage (Assistant) ----------
Thank you for the feedback! Here’s a revised explanation incorporating your suggestions:

"The sky looks blue because of a process where sunlight gets spread out when it hits tiny particles in the air. Sunlight is made up of many colors, like red, green, and blue. The blue light gets bounced around more than the other colors because it travels in shorter waves. That’s why, during the day, we see a blue sky. 

At sunrise and sunset, the sky can look orange or red because the sunlight has to pass through more air. This means that most of the blue light gets scattered away, allowing the warmer colors to shine through."
TaskResult(messages=[TextMessage(id='b29b49cf-f8b0-45c7-af30-f563369619b6', source='user', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 41, 25, 980422, tzinfo=datetime.timezone.utc), content='Explain why the sky is blue in simple terms.', type='TextMessage'), TextMessage(id='563c092d-4c5e-4cb3-860b-015f639e9529', source='Assistant', models_usage=RequestUsage(prompt_tokens=34, completion_tokens=78), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 41, 27, 825361, tzinfo=datetime.timezone.utc), content="The sky looks blue because of a process called scattering. When sunlight enters the Earth's atmosphere, it hits tiny particles and gases in the air. Sunlight is made up of many colors, and each color has a different wavelength. Blue light has a shorter wavelength, so it gets scattered in all directions more than other colors. This scattering makes the sky appear blue to our eyes during the day.", type='TextMessage'), TextMessage(id='64d69d94-6296-4ca5-8bfc-e040a8387011', source='Critic', models_usage=RequestUsage(prompt_tokens=122, completion_tokens=244), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 41, 31, 428259, tzinfo=datetime.timezone.utc), content='The explanation provided is quite clear and captures the essence of why the sky appears blue. However, there are a few areas that could be improved for simplicity and clarity:\n\n1. **Simplify Vocabulary**: The term "scattering" might be too technical for some audiences. Consider using "spread out" or "bounced around" to make it more relatable.\n\n2. **Add a Visual Element**: A brief mention of how this phenomenon relates to the colors of a rainbow could help provide a more comprehensive understanding.\n\n3. **Contextual Comparison**: Including a comparison to other times when the sky changes color (like sunrise and sunset) could help illustrate why the blue sky occurs during the day specifically.\n\nRevised explanation: \n"The sky looks blue because of a process where sunlight gets spread out when it hits tiny particles in the air. Sunlight has many colors, like red, green, and blue. The blue light gets bounced around more than the other colors because it travels in shorter waves. That\'s why, during the day, we see a blue sky. At sunrise and sunset, the sky can look orange or red because the sunlight has to pass through more air, which scatters the blue light away."', type='TextMessage'), TextMessage(id='b55a9d16-2457-4bcd-acd6-1390109c8a0f', source='Assistant', models_usage=RequestUsage(prompt_tokens=367, completion_tokens=129), metadata={}, created_at=datetime.datetime(2025, 8, 17, 13, 41, 33, 759535, tzinfo=datetime.timezone.utc), content='Thank you for the feedback! Here’s a revised explanation incorporating your suggestions:\n\n"The sky looks blue because of a process where sunlight gets spread out when it hits tiny particles in the air. Sunlight is made up of many colors, like red, green, and blue. The blue light gets bounced around more than the other colors because it travels in shorter waves. That’s why, during the day, we see a blue sky. \n\nAt sunrise and sunset, the sky can look orange or red because the sunlight has to pass through more air. This means that most of the blue light gets scattered away, allowing the warmer colors to shine through."', type='TextMessage')], stop_reason='Maximum number of messages 4 reached, current message count: 4')

```
### Key Insight from Output: 

> This output shows how multi-agent collaboration can refine an explanation: the Assistant provides an initial answer, the Critic improves clarity and accessibility,
> and the Assistant revises accordingly. The process demonstrates how an iterative, feedback-driven workflow leads to a clearer, more audience-friendly explanation.
> 
## 🔹 How It Works

- **Turn 1** → Assistant: Answers the question.
- **Turn 2** → Critic: Reviews the assistant’s answer and suggests improvements.
- **Termination:** MaxTurnsTermination ensures the team stops after 4 turns.
- **Collaboration:** Each agent uses the **shared context** to see previous messages.
