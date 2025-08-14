# CrewAI Overview

## 1. What is CrewAI?

CrewAI is a framework for **building teams of AI agents**, like smart software team members.  
It is **easy to use**, **intuitive**, and **powerful**.

**Built on LangChain:**
- Can use many existing tools and integrations.  
- Connects with LangSmith for testing and monitoring AI applications.

---

## 2. Core Concepts

- **Agent:** An AI team member with a specific job or role.  
- **Task:** Work agents need to complete.  
- **Tool:** A resource or ability an agent uses to accomplish tasks.  
- **Process:** Rules or strategy for how tasks are completed.  
- **Crew:** A group of agents working together.  
- **Memory:** What agents remember from past actions to make smarter choices.

> **Memorable point:** Think of CrewAI as building a smart, organized team of specialized robots, each with its own mission and tools.

---

## 3. Agents in CrewAI

### Definition
An **agent** is an independent AI that can:  
- Execute tasks  
- Make decisions  
- Collaborate with other agents

### Roles
Examples of agent roles:
- Data Analyst  
- Content Creator  
- Tech Support  

### Example Agent: Content Creator

- **Role:** Content Creator  
- **Goal:** Make engaging marketing content  
- **Backstory:** Works at a digital marketing agency promoting a new product  

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
| Attribute              | Meaning                                        |
| ---------------------- | ---------------------------------------------- |
| role                   | Agent’s job                                    |
| goal                   | What the agent should accomplish               |
| backstory              | Background guiding decisions                   |
| tools                  | Programs/resources agent can use               |
| llm                    | Language model helping agent decide and create |
| function\_calling\_llm | Handles special tool/function calls            |
| max\_iter              | Max retries/refinements for tasks              |
| verbose                | Gives detailed progress updates if true        |
| allow\_delegation      | Can ask other agents for help                  |
| callbacks              | Actions triggered during agent's work          |

>    **Remember:** Agents are like specialized robots on a team, each with strengths, tools, and missions.

## 4. Tasks in CrewAI

What is a Task?

A **task** is a specific assignment or mission for an agent.
It includes instructions and resources, and can be simple or complex.

#### Importance of Tasks
- Break large projects into manageable pieces
- Provide clarity: agent knows job, tools, and success criteria

#### Key Attributes
| Attribute         | Meaning                            |
| ----------------- | ---------------------------------- |
| description       | What needs to be done              |
| expected\_output  | Success criteria or outcome        |
| agent             | Assigned agent                     |
| tools             | Helpful software/tools             |
| max\_iter         | Max retries/refinements            |
| verbose           | Show progress updates              |
| allow\_delegation | Can delegate task to another agent |
| callbacks         | Actions triggered at key points    |

#### Special Attributes
| Attribute        | Meaning                                |
| ---------------- | -------------------------------------- |
| async\_execution | Run in background for big/slow tasks   |
| context          | Use results from other tasks           |
| config           | Extra settings to customize behavior   |
| output\_json     | Output as JSON                         |
| output\_pydantic | Output as Pydantic model               |
| output\_file     | Save output to a file                  |
| human\_input     | Requires human review before finishing |

#### Code Example
```python
task = Task(
    description='Research best practices for cloud cybersecurity',
    expected_output='Top 10 practices report with explanations',
    agent=cybersecurity_agent,
    tools=[cloud_security_tool, research_tool]
)
```

>    **Memorable point:** Tasks = clear, organized jobs with instructions, resources, and success criteria.

#### Can multiple agents do the same task?

- Normally: **One task = one agent**
- Collaboration: **Split work into smaller tasks or use a crew for delegation**

| Situation                                    | Possible? |
| -------------------------------------------- | --------- |
| One Task, Multiple Agents (direct)           | ❌ No      |
| One Project, Multiple Tasks, Multiple Agents | ✅ Yes     |

## 5. Tools vs Callbacks

#### Tool

**Definition:** Resource or ability to complete a task

**Examples:** Calculator, web search, translation tool

**When used:** During the task

#### Callback

**Definition:** Code triggered at events during agent work

**Examples:** Notifications, logging, error handling

**When used:** After or during specific events

| Feature  | Purpose                  | Example                              |
| -------- | ------------------------ | ------------------------------------ |
| Tool     | Helps agent do main work | Translate text                       |
| Callback | React to events          | Send notification when task finishes |

> Analogy:
>
> **Tool** = hammer/calculator to do the work
>
> **Callback** = tell phone: “After homework, notify my friend”


## 6. CrewAI Core Concepts: Crew, Process, Memory
#### 🧑‍🤝‍🧑 Crew

- Group of agents working together
- Organize, assign, and monitor tasks

| Attribute         | Meaning                              |
| ----------------- | ------------------------------------ |
| agents            | Team members                         |
| tasks             | Assigned tasks                       |
| process           | Task management strategy             |
| full\_output      | Show all task results                |
| verbose           | Detailed progress updates            |
| share\_crew       | Share work/results to improve CrewAI |
| output\_log\_file | Save activity logs                   |
| planning          | Plan before starting tasks           |

#### Sample Code:
```python
project_team = Crew(
    agents=[data_analyst, report_creator],
    tasks=[data_analysis_task, generate_report_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
```

## ⏩ Process

- Strategy for task completion

#### Types:

- **Sequential:** One after another (A → B → C)
- **Hierarchical:** Manager assigns & checks work
- **Consensual:** Group agreement (coming soon)

#### Code Examples:

- **Sequential**
```python
crew = Crew(agents=my_agents, tasks=my_tasks, process=Process.sequential)
```

- **Hierarchical**
```python
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4")
)
```

## 🧠 Memory

- Lets agents remember, learn, and use past info

| Type          | Function                             |
| ------------- | ------------------------------------ |
| Short-Term    | Recent actions/conversations         |
| Long-Term     | Builds knowledge over time           |
| Entity Memory | Facts about people, places, ideas    |
| Contextual    | Keeps tasks/conversations consistent |

> **Why important:** Track progress, make smarter decisions, stay relevant, and learn over time

> **Analogy:** CrewAI = group project at school: everyone has a job, tasks are organized, and memories help the team succeed together.

## 7. Summary

- **CrewAI:** Framework to build smart AI teams  
- **Agents:** Specialized AI team members  
- **Tasks:** Specific assignments with clear instructions  
- **Tools:** Resources agents use to complete tasks  
- **Callbacks:** Respond to events or outcomes during task execution  
- **Crew:** Organized team of agents working together  
- **Process:** Strategy for completing tasks efficiently  
- **Memory:** Past knowledge that helps agents make smarter decisions  

**Key Takeaway:**  
> CrewAI lets you manage AI “workers” like a real team, combining specialized skills, tools, and coordination for efficient, collaborative problem-solving.

---

## Memory Sharing in CrewAI

### Simple Answer
Yes, memory **can be shared among agents**, depending on your crew and memory setup.

### How Agent Memory Works

- **Short-Term Memory:**  
  - Usually **individual** to an agent  
  - Remembers only recent actions or conversations  

- **Long-Term / Contextual / Entity Memory:**  
  - Can be **shared across a crew**  
  - Lets agents access what others have learned or done  
  - Improves teamwork and consistency  

### Shared Memory Example

- Agents working on the same project can share:
  - Project context  
  - Important facts or outputs  
  - Past conversations  
- This allows **cooperation, consistency, and context-aware decision-making**  

### Why Share Memory?

- Better **team coordination**  
- Avoid repeated work  
- Produce more **accurate and context-aware responses**


### Can Agents Have Private Memory?

- **Yes.**  
- Some agents can have memory that **other agents cannot see**  
- Useful for personal tasks or sensitive information  


### Summary Table

| Memory Type     | Who Can Access           | Typical Use                        |
|-----------------|------------------------|-----------------------------------|
| Private Memory  | One agent               | Personal tasks or info             |
| Shared Memory   | Multiple agents (crew)  | Teamwork, context, collaboration   |


### Key Takeaway
> By default, CrewAI allows shared memory for teamwork, but you can also give agents private memory. Most crews share memory so all agents stay on the same page.

---

## CrewAI Step-by-Step Flow

### 1. Crew is Created
- You create a **crew** (team) and add several agents to it.

### 2. Tasks are Added
- The crew receives a **list of tasks** to complete.

### 3. Process is Chosen
- Select a **process** (e.g., sequential or hierarchical)  
- Determines **how agents get tasks** and in what order.

### 4. Agents Get and Work on Tasks
- Each agent is assigned specific tasks according to the process.  
- Agents use their **skills and tools** to complete the tasks.

### 5. Agents Use Memory
- Agents **read from memory** to recall useful past information.  
- Agents **write new information** into memory to make the team smarter.

### 6. Tasks Completed
- Agents finish their tasks and **results are saved**.  
- Important outcomes are updated in the **crew’s memory**.

### 7. Crew Delivers Results
- The crew provides **final output**, including all completed tasks and updated memory.

---

### Diagram Flow (Text Version)
```plaintext
[ Crew ]
   |
   v
[ Agents (team members) ]
   |
   v
[ Tasks List ]
   |
   v
[ Process (task assignment strategy) ]
   |
   v
[ Agents work on tasks (using tools) ]
   |
   | <—> [ Memory accessed and updated by agents ]
   v
[ Task Results & Updated Memory ]
   |
   v
[ Crew outputs final results ]
```

---

### Quick Summary Table

| Concept | Role in the Flow |
|---------|-----------------|
| Crew    | The team that organizes everything |
| Agents  | Team members who actually perform the tasks |
| Task    | Jobs to be completed by agents |
| Process | The plan for assigning tasks to agents |
| Memory  | Information store accessed and updated by agents |

---

### Real-Life Analogy
Your **project group (crew)** assigns each student (**agent**) certain jobs (**tasks**).  
There’s a **plan (process)** for who works when, and everyone keeps **notes and progress (memory)** that anyone in the group can check.

---

**In short:**  
> Crew builds the team, agents do the tasks guided by a process, and all use and update memory as they work!

