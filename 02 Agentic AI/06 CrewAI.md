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

---

# Tasks in CrewAI – Notes

## What is a Task?
A **Task** = A specific job, assignment, or mission for an agent to complete.  
Each task includes clear instructions and resources (like tools) so the agent understands exactly what needs to be done.  
Tasks can be simple or complex and sometimes involve teams of agents working together (collaborative tasks).

## Why are Tasks Important?
- They break down bigger projects into manageable chunks.
- Each task is organized so the agent knows its job, tools, and what success looks like.

## Key Task Attributes (Features)

| Attribute          | What it Means (Simple Explanation) |
|-------------------|-----------------------------------|
| description        | What needs to be done (the goal or summary of the task) |
| expected_output    | What a successful result should look like (clear outcome or report) |
| agent              | Who/what will do the task (name of the agent assigned) |
| tools              | Helpful software/tools the agent can use when working on the task |
| max_iter           | How many times the agent can retry or refine the task |
| verbose            | Should the agent give detailed progress updates? |
| allow_delegation   | Can the agent pass this task to another agent if needed? |
| callbacks          | Special actions that happen at certain points (like sending notifications) |

### Other Special Attributes

| Attribute          | What it Does (Simple) |
|-------------------|----------------------|
| async_execution    | Lets the task run in the background, not making the whole system wait for it to finish—good for big or slow tasks |
| context            | Can use results from other tasks as extra information |
| config             | Extra settings for customizing how the task behaves |
| output_json        | Output will be structured as a JSON file (good for computers to read the data easily; needs certain tech setup) |
| output_pydantic    | Output follows a special data model (Pydantic); great for strict data rules (needs special setup) |
| output_file        | Saves the final result to a file (plain text, JSON, or Pydantic—but just one format at a time) |
| human_input        | Do you need a person to check the output before finishing? Default: No |

## Summary Table

| What is it? | An assignment for an agent, with clear instructions and resources |
|-------------|--------------------------------------------------------------|
| Who does it? | One or more agents (sometimes in a team) |
| What does it need? | Description, tools, the agent to do it, what a good result looks like |
| Why use it? | To break complex projects into clear, manageable jobs |

## Code
```python
task = Task(
    description='Research and compile a list of best practices for cybersecurity in cloud environments',
    expected_output='A detailed report outlining the top 10 best practices for securing cloud environments, including explanations and examples.',
    agent=cybersecurity_agent,
    tools=[cloud_security_tool, research_tool]
)
```

**Remember:**  
- Tasks give agents step-by-step instructions, tools, and clear expectations for success.  
- Tasks can be simple, complex, or part of teamwork.  
- You can further control tasks using extra features—like running them in the background or saving the results to files.  

**In short:**  
> Tasks = clear, organized jobs for agents, with instructions, resources, and a standard for success!

---

## Can a single task be executed by multiple agents in CrewAI?

**Normally:**  
- Each task is usually assigned to **one specific agent** at a time using the `agent` attribute.

**But for teamwork:**  
If you want multiple agents to work together, you have two options:

### Collaborative Tasks
- Split the work into smaller tasks, with each small task assigned to a different agent.  
- These tasks can share information using the `context` attribute.

### Processes and Crews
- Organize agents into a **crew** and use CrewAI’s built-in teamwork and process management features.  
- Allows agents to delegate and pass tasks to each other, so it feels as if multiple agents are tackling the same task.

**So:**  
- **Directly:** One task = one agent  
- **Indirectly (with collaboration):** Coordinate multiple agents to work on parts of a bigger project using several connected tasks or delegation.

### Summary Table

| Situation | Possible in CrewAI? |
|-----------|-------------------|
| One Task, Multiple Agents (directly) | ❌ Not as a standard option |
| One Project, Multiple Tasks, Multiple Agents (collaborative) | ✅ Yes, using crews, context, and delegation |

**In short:**  
> A single task is usually done by one agent, but multiple agents can work together by splitting the job into several smaller, connected tasks.

---

# Tools in CrewAI – Notes

## What is a Tool?
A **Tool** is a special ability or function that an agent can use to help complete a task.  
Tools let agents do specific jobs better, like searching the web, reading files, analyzing data, or generating images.  
Think of a tool like a useful app or gadget the agent gets to use.

## Why are Tools Important?
- Tools make agents more powerful and flexible.  
- With the right tool, an agent can work much faster and do more complicated things.  
- Developers can use pre-made tools, or build custom ones for special jobs.

## Where Do Tools Come From?
- **CrewAI Toolkit:** Built-in tools that come with CrewAI.  
- **LangChain Tools:** Tools from another framework that works well with CrewAI.  
- **Custom Tools:** Developers can also make custom tools if needed.

## Key Features of Tools
- **Integrated:** Fit right into agent workflows.  
- **Customizable:** You can use existing tools or create new ones for your needs.  
- **Error Handling:** Tools have built-in systems to deal with problems, so agents don't get stuck.  
- **Caching:** Tools are smart—they save results, so if the same job is needed again, it's faster.

## Examples of Tools in CrewAI

| Tool Name           | What It Does |
|--------------------|--------------|
| BrowserbaseLoadTool | Lets agent interact with web browsers & gather data |
| CodeDocsSearchTool  | Searches through code documentation & manuals |
| CSVSearchTool       | Searches and works with data in CSV files |
| DALL-E Tool         | Creates images using the DALL-E AI model |
| DOCXSearchTool      | Searches inside MS Word (DOCX) files |
| PDFSearchTool       | Searches inside PDF files |
| ScrapeWebsiteTool   | Collects (scrapes) lots of data from websites |
| XMLSearchTool       | Searches through XML files (a type of structured data) |

## Summary
- **Tools = Superpowers for agents**, helping them do tasks like searching, analyzing, creating, and collecting data easily.  
- Tools are vital—they make agents smarter, faster, and more versatile.  
- Agents can use **one or more tools** as needed when working on tasks.  

**In short:**  
> Think of an agent as a worker and tools as the specialized gadgets they use to get their work done more efficiently!
---
