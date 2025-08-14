# CrewAI Overview

## 1. What is CrewAI?

CrewAI is a framework (tool) for **building teams of AI agents**, like smart software team members.  
It is **easy to use**, **intuitive**, and **powerful**.

**Built on LangChain, which means:**
- Can use many existing tools and integrations.  
- Connects with LangSmith for testing and monitoring AI applications.

---

## 2. Core CrewAI Concepts

- **Agent:** An AI team member with a specific job or role.  
- **Tasks:** The work agents need to do.  
- **Tools:** Things agents use to do their job (programs, AI features, etc.).  
- **Processes:** How agents work together to finish tasks.  
- **Crews:** Groups of agents working as a team.  
- **Memory:** What agents remember from past actions (helps them make smarter choices).

---

## 3. Agents in CrewAI

**Definition:**  
An agent is an independent AI that can:  
- Do tasks  
- Make choices  
- Work with other agents as part of a team  

**Roles:**  
Each agent has a specific job, for example:  
- Data Analyst  
- Content Creator  
- Tech Support  

### Example Agent: Content Creator

- **Role:** Content Creator  
- **Goal:** Make engaging marketing pieces (like social media posts)  
- **Backstory:** Works for a digital marketing agency, promoting a new product  

**Code Example:**

```python
agent = Agent(
    role='Content Creator',
    goal='Develop engaging marketing content',
    backstory="You're a content creator at a digital marketing agency...",
    tools=[content_tool1, content_tool2],
    llm=my_llm,
    function_calling_llm=my_llm,
    max_iter=15,
    verbose=True,
    allow_delegation=True,
    callbacks=[callback1, callback2],
)
```

| Attribute                  | Meaning                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **role**                   | Agent’s job (e.g., Content Creator)                                                |
| **goal**                   | What the agent should accomplish (e.g., Write engaging content)                    |
| **backstory**              | The “story” or background that guides the agent’s choices                          |
| **tools**                  | Programs or resources the agent can use                                            |
| **llm**                    | The smart language model (like GPT-4) that helps the agent read, write, and decide |
| **function\_calling\_llm** | Special part for using tools/functions; can use a different model                  |
| **max\_iter**              | Maximum times the agent can retry or refine its work                               |
| **verbose**                | If true, agent gives detailed updates                                              |
| **allow\_delegation**      | If true, agent can ask other agents for help                                       |
| **callbacks**              | Actions triggered during the agent’s work (e.g., notifications)                    |

---

### 5. In Summary

- **CrewAI** helps build smart teams of AI agents, each with its own job, tools, and goal.
- **Agents** can create, refine, and delegate tasks.
- Built on familiar and powerful tech for building and monitoring AI teamwork easily.

#### Remember:
> Think of agents as specialized robots on a team, each with their own strengths, tools, and missions.
> CrewAI makes managing these robots simple and effective, just like managing a real team.

---

### Callback Vs Tool

#### Callback

**What is it?**  
A callback is a piece of code (usually a function) that **automatically runs at special points** during the agent’s work—like when a task **starts, ends, or fails**.

**What is it for?**  
It is used to **react to events**, for example:  
- Sending a notification when work is done  
- Saving a log  
- Handling errors  

**Example Use:**  
- Sending a message when a task is finished  
- Keeping a record each time an agent performs an action  

---

#### Tool

**What is it?**  
A tool is a **resource or ability** the agent can use to **complete its tasks or solve problems**.

**What is it for?**  
Tools are used **to do the work itself**. Examples include:  
- A calculator  
- A web search plugin  
- A database lookup  
- A function to send emails  

**Example Use:**  
- Using a translation tool to turn English text into Spanish  
- Using a search tool to find information online  

---

#### Simple Analogy

- **Tool:** Like a **hammer or a calculator** in a worker’s toolbox—something you use to get the job done.  
- **Callback:** Like telling your phone:  
  > “When I finish my homework, send my friend a message.”  
  Your phone reacts **after** you finish, not during the homework.

---

#### Summary Table

| Feature   | Purpose                        | When Used?                  | Example                          |
|-----------|--------------------------------|-----------------------------|----------------------------------|
| **Callback** | Reacts to agent’s events       | When something happens (event) | Send a notification after task   |
| **Tool**     | Helps agent do main tasks      | During task to achieve a goal  | Use a calculator to add numbers |

---

**In short:**  
- **Tools** help the agent **do its work**.  
- **Callbacks** help you **respond to what the agent did** or **when something happens**.
