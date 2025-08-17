# Human-in-the-Loop in AutoGen AgentChat

In the **Teams** section, we learned how to create and control a group of agents.  
Now, let’s see how **humans can step in and provide feedback** to guide the agents.  
This process is called **Human-in-the-Loop (HITL).**

---

## Two Ways to Provide Feedback
There are **two main ways** you (the human) can interact with the agents:

1. **During a team’s run** (`run()` or `run_stream()`)  
   - Using a special agent called **UserProxyAgent**.  
   - This lets you give feedback *while* the agents are working.  

2. **After the run finishes**  
   - Provide feedback as input to the **next run**.  
   - Example: after agents finish one task, you give corrections or instructions before starting the next task.  


## 🧑‍🤝‍🧑 Two Ways to Provide Feedback to Agents  

Imagine you have a team of **robot helpers (agents)**. They are working on a project for you.  
You (the human) are their **coach**.  

There are **two times you can give feedback**:

### 1️⃣ While They’re Working (During a Run)  
- Think of it like a **sports coach shouting from the sidelines** while the players are still playing.  
- You can stop them, correct them, or guide them **immediately**.  

👉 Example:  
Robots are writing a story, and halfway through you say:  
> "Hey, make it funnier!"  

They will adjust their work right away.  
This is done using a **UserProxyAgent** (your voice inside the system).  


### 2️⃣ After They’re Done (Next Run)  
- Imagine the robots finish their work and show it to you.  
- You look at it and say:  
> "Nice, but next time add more details about the characters."  

Then, when they start the **next task**, they remember your feedback and do better.  


✅ **In short:**  
- **During run = live coaching.**  
- **After run = homework correction for next time.**

---

## 🔹 Providing Feedback During a Run
- The **UserProxyAgent** acts as a bridge between the human and the team.  
- When included in the team, it waits for the system to call it and then asks the human for input.  
- Once the human responds, the control goes back to the team.

### Example:
- In **RoundRobinGroupChat** → the `UserProxyAgent` takes its turn just like other agents.  
- In **SelectorGroupChat** → the selector logic decides when to ask the human for feedback.

---

## 🔹 How It Works (Flow)
1. Team is running → Agents take turns.  
2. Team reaches the **UserProxyAgent**.  
3. Execution **pauses** until the user responds.  
4. Once input is given, execution **resumes** with updated feedback.  

> ⚠️ **Important Note**  
> - The team **blocks (pauses)** while waiting for feedback.  
> - If the user never responds, the team is stuck in an unstable state.  
> - Best used only for **short interactions** like:
>   - Approve/Disapprove a message.  
>   - Confirm an alert.  
>   - Quick input for a critical decision.  

---

## ✅ Best Practices
- Use `UserProxyAgent` **only for quick, blocking feedback**.  
- For longer or delayed human input, prefer giving feedback **after a run** (before the next one).  

---

## Next Steps
For real-world apps, you can connect this with UI frameworks to make it interactive:
- **AgentChat + FastAPI**  
- **AgentChat + ChainLit**  
- **AgentChat + Streamlit**

---

### Example Code

```python
# Import the required tools from autogen framework
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent   # Agents (AI + human proxy)
from autogen_agentchat.conditions import TextMentionTermination       # Condition to stop chat
from autogen_agentchat.teams import RoundRobinGroupChat               # Manages chat flow between agents
from autogen_agentchat.ui import Console                              # Shows chat in the console
from autogen_ext.models.openai import OpenAIChatCompletionClient      # OpenAI model connection

# Step 1: Connect to an OpenAI model (small version of GPT-4).
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Step 2: Create two agents
assistant = AssistantAgent("assistant", model_client=model_client)   # The AI assistant
user_proxy = UserProxyAgent("user_proxy", input_func=input)          # Represents the human (takes input from console)

# Step 3: Set a stop condition for the chat.
# The chat will automatically stop when the user types the word "APPROVE".
termination = TextMentionTermination("APPROVE")

# Step 4: Create a team of agents.
# Here, we have 2 members: assistant (AI) and user_proxy (human).
# RoundRobinGroupChat makes them take turns like a ping-pong conversation.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Step 5: Start the conversation.
# The task is: "Write a 4-line poem about the ocean."
# run_stream() keeps the chat going, streaming the messages as they happen.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")

# Step 6: Display the chat in the console.
# await is used because run_stream() works asynchronously (like background tasks).
await Console(stream)

# Step 7: Close the connection to the model after finishing the chat.
await model_client.close()


```

```bash
---------- TextMessage (user) ----------
Write a 4-line poem about the ocean.
---------- TextMessage (assistant) ----------
Waves whisper secrets to the shore,  
In endless dance, they churn and roar.  
Beneath the moon's soft, silver light,  
The ocean dreams through day and night.  
TERMINATE
Enter your response: make it funny
---------- TextMessage (user_proxy) ----------
make it funny
---------- TextMessage (assistant) ----------
The ocean's like a giant soup,  
With fish that swim and seaweed scoop.  
It’s salty, splashy, and quite deep,  
Where mermaids hide and crabs do leap!  
TERMINATE
Enter your response: AOOROVE
---------- TextMessage (user_proxy) ----------
AOOROVE
---------- TextMessage (assistant) ----------
It seems like "AOOROVE" might be a mistake or a term I'm not familiar with. Could you clarify or provide more context? I'm here to help!  
TERMINATE
Enter your response: APPROVE
---------- TextMessage (user_proxy) ----------
APPROVE


```


## Code - Review in Loop

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

# ------------------------
# Step 1: Create the model client
# ------------------------
# This is the connection to OpenAI's GPT model (gpt-4o-mini in this case).
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# ------------------------
# Step 2: Create the agents
# ------------------------
# Each AssistantAgent has:
# - a name
# - a description
# - the model client (so they can use GPT)
# - a system_message that tells them how to behave

assistant = AssistantAgent(
    name='Writer',
    description='you are a great writer',
    model_client=model_client,
    system_message='You are a really helpful writer who writes in less then 30 words.'
)

assistant2 = AssistantAgent(
    name='Reviewer',
    description='you are a great reviewer',
    model_client=model_client,
    system_message='You are a really helpful reviewer who writes in less then 30 words..'
)

assistant3 = AssistantAgent(
    name='Editor',
    description='you are a great editor',
    model_client=model_client,
    system_message='You are a really helpful editor who writes in less then 30 words..'
)

# ------------------------
# Step 3: Create the team
# ------------------------
# RoundRobinGroupChat means agents take turns one by one (round-robin style).
# - participants: the 3 agents we made
# - max_turns: how many turns they can talk before stopping
team = RoundRobinGroupChat(
    participants=[assistant, assistant2, assistant3],
    max_turns=3
)

# ------------------------
# Step 4: Set the first task
# ------------------------
# This is the "prompt" that will be given to the agents
task = ' Write a 3 line poem about sky'

# ------------------------
# Step 5: Interactive loop
# ------------------------
# Keep running until the user types "exit"
while True:
    # run_stream → runs the chat between the agents as a stream
    stream = team.run_stream(task=task)

    # Console → displays the streaming conversation in the terminal
    await Console(stream)
  
    # Ask the user for feedback after the agents finish
    feedback = input('Please Provide your feedback (type "exit" to stop)')

    # If user types exit → break the loop
    if(feedback.lower().strip() == 'exit'):
        break
    
    # Otherwise → the new feedback becomes the next task
    task = feedback

```
### In short
This script creates a mini debate team of 3 AI agents (Writer, Reviewer, Editor).
They take turns (round robin) working on a given task (like writing a poem).
After each round, the user gives feedback. If the user types “exit,” the loop ends.
