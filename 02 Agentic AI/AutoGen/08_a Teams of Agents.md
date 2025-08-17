

## Multi-Agent Team in AutoGen

**A team**= group of agents working together toward a common goal.

Learning path:
- How to create and run a team.
- How to observe team behavior (important for debugging & performance analysis).
- Common operations to control and manage team behavior.


<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/876ec0de-8462-4e7e-992a-04b477da9a73" />

### ✅ When to Use a Team in AutoGen

Use a team when:
- Task is complex and needs collaboration.
- Task requires diverse expertise (e.g., research + writing + coding).

Teams need more scaffolding:
- You must guide/steer them more than a single agent.
- More planning and coordination overhead.

Best practice:
- Start with a single agent for simple tasks.
- Optimize single agent first (use right tools, clear instructions).
- Move to a team only if a single agent is not enough.

👉 Simple analogy:

- Single Agent = A student doing homework alone.
- Team = A group project where one person researches, another writes, another presents.
- You wouldn’t form a group for a 2-mark math question, but you’d need one for a full science project.

---

### Team Presets in AgentChat

#### 1. RoundRobinGroupChat
- Agents take turns in a round-robin manner.
- Good for structured discussions.

***Analogy: Like players in cricket batting one after another, taking turns.***

> Everyone must speak in order: **A → B → C → A → B → C**.
> 
> **Example:**
>   - Agent A: “Let’s plan a birthday.”
>   - Agent B: “We should buy a cake.”
>   - Agent C: “Don’t forget balloons.”
>   - Then back to Agent A.

#### 2. SelectorGroupChat

- After each message, the next speaker is chosen by a ChatCompletion model.
- More dynamic than round-robin.

***Analogy: Like in a classroom where after one student speaks, the teacher decides who talks next.***
> Next speaker is chosen (not fixed order).
>
> **Example:**
>   - Agent A: “Let’s solve 5 + 7.”
>   - AI Selector: “Agent C should go next.”
>   - Agent C: “The answer is 12.”
>   - AI Selector: “Now Agent B should add more.”


#### 3 MagenticOneGroupChat

- A generalist multi-agent system.
- Designed for solving open-ended tasks (web, files, multiple domains).

***Analogy: Like a project team where different experts jump in whenever their skills are needed.***
> Can handle many types of tasks (math, writing, searching the web, analyzing files).
>
> **Example:**
>   - User: “Write me a report about climate change.”
>   - Research Agent: finds facts online.
>   - Writer Agent: writes the report.
>   - Reviewer Agent: checks mistakes.
>   - Together, they finish the task.

#### 4. Swarm

- Uses HandoffMessage to explicitly transfer control between agents.
- Useful for workflows where one agent should hand over to another.

***Analogy: Like a relay race 🏃‍♂️🏃‍♀️ where runners pass the baton to the next runner.***
> Each agent hands over the task to the next one when their part is done.
>
> **Example:**
>   - Agent A: “I’ll collect today’s weather.” → hands over.
>   - Agent B: “I’ll analyze the weather data.” → hands over.
>   - Agent C: “I’ll create a chart of the results.”
>   - Task completed step by step.
>

---

## 🔑 How Teams Share Context

- In AgentChat, all agents in a team can see the conversation history (messages exchanged so far).

- This means if Agent A says something, then Agent B already knows what A said, and can build on it.

- The context is like a shared notebook where everyone can read what’s written before adding their own notes.

---

