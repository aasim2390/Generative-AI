# What Are Generative AI Agents?

Think of them as **smart robot helpers** that can think, use tools, remember things, plan steps, and sometimes work on their own — but with a grown-up watching for safety.

---

## Key Features

### Reflection (Thinking About Their Own Thinking)
- **What it means:** The agent reviews the steps it just took and asks,  
  *“Did I do that right? What can I do better next time?”*  
- **Why it’s useful:** Helps the agent learn from mistakes and improve problem-solving.
- #### How It Works: The Three-Step Cycle

1. **AI does a task.**  
2. **AI reviews what happened** — what worked and what didn’t.  
3. **AI changes its plan** for the next try.

#### Reflection Idea  
The AI “talks to itself,” saves those thoughts as feedback, and uses them later. This cycle repeats.

#### Why It Helps  
- Learns from mistakes  
- Gets better at solving problems  
- Can explain why it chose certain steps

#### Where It’s Useful  
- Virtual worlds like AlfWorld  
- Answering hard questions  
- Writing computer code

#### Simple Takeaway  
> Reflection helps AI learn from its experiences and become more reliable over time, just like you learn from your mistakes after a test.
---

### Tool Use (Using Other Apps and Data)
- **What it can do:** Look things up on the web, run code, analyze data, open files, and control other software.  
- **If no direct tool:** It can still work by clicking buttons or filling forms on a website.

#### What It Means
AI can use other software, apps, websites, and data sources to do more than just write or draw.

#### What It Can Do
- Get real-time information  
- Do calculations  
- Analyze data  
- Manage files or calendars  
- Run multi-step workflows (like a mini automatic plan)  

#### Examples
- Browsing the web to find current news  
- Running code to solve a problem  
- Creating charts from data  
- Managing customer records in a CRM (e.g., Salesforce’s Einstein GPT)  
- Generating code and diagrams from AWS documentation (e.g., AWS’s Solution Architect Agent)  

#### Why This Matters
- Real-world tasks aren’t perfect: data may be missing, APIs can fail, and situations change.  
- The AI can handle problems by retrying, adjusting, or asking for help when needed.  

#### What If There’s No API?
The AI can still work by acting like a person using an app:  
- Read what’s on the screen (HTML or screenshots)  
- Decide what to click or type next  
- Check if it worked (look for a confirmation)  
- Keep adjusting as the interface changes  

#### Bottom Line
> Tool use makes AI agents more **useful** and **flexible**, able to handle complicated and changing tasks.

---

### Memory (Remembering Things)
- **Short-term memory:** Keeps track of current happenings to stay on task.  
- **Long-term memory:** Stores past experiences to use later (like recalling previous projects).  
- **Why it matters:** Better memory leads to more coherent and helpful actions over time.

#### What Is Memory for an AI Agent?

Memory means the AI can remember facts, past actions, and past interactions so it can use that info later. This helps it stay on topic, learn, and give better answers.

### Two Main Types of Memory

#### Short-term Memory
- Keeps recent details needed for the current task.  
- **Example:** Remembering the last few messages in a chat.  
- Temporary and can be cleared or moved to long-term memory later.

#### Long-term Memory
- Stores knowledge, experiences, and patterns for a long time.  
- Often uses a **vector database** to find and recall information quickly.  
- Divided into:  
  - **Episodic memory:** Remembers specific past events (e.g., what happened in a previous task)  
  - **Semantic memory:** Remembers facts and concepts (e.g., what a lever is and how it works)  
  - **Procedural memory:** Remembers how to do things (e.g., steps to complete a process)  

#### Why Memory Matters
- Agents with memory can keep track of context and personalize responses.  
- They perform better in complex, changing situations because they learn from past experiences.

#### Example
The **JARVIS-1** agent uses memory from different sources — text, images, and other data types — to plan and complete tasks in tricky environments. This makes it more adaptable and capable.

#### Quick Takeaway

> Memory helps AI agents **remember past stuff**, **learn from it**, and **act more wisely** in the future.
---

### Planning (Figuring Out Steps to Reach a Goal)
- **What it does:** Breaks a big goal into smaller tasks and makes a plan.  
- **Example:** Planning a school project by deciding topics, researching, outlining, writing, and proofreading.

#### What It Means
AI uses **smart planning** to figure out the steps needed to reach a big goal.

#### How It Works
- An AI with planning analyzes the goal and splits it into smaller tasks.  
- It decides the order to do tasks and can adjust the plan as it goes.

#### Recent Advances (Easy Version)
- **Reflexion Framework:** The AI makes a plan, then reviews what happened, learns from it, and improves the plan for next time.  
- **TPTU (Task Planning and Tool Usage):** Studies how AI plans tasks and uses tools, in two ways:  
  - All at once: one big plan  
  - Step by step: plan, then adjust after each step based on feedback  

#### Why It’s Useful
Planning helps AI tackle complex jobs that need both **flexibility** and **knowledge**.

#### Example
Automating a home garden:  
- Install sensors  
- Set watering schedules  
- Check plant health  
- Send updates to your phone  

#### Challenge
Plans can be unpredictable because the AI is making them on the fly.  
With guardrails and some human oversight, planning is getting more reliable.

#### Quick Activity (Optional)
Plan a school project:  
- List 3 sub-tasks and the order you’d do them.  
- Then think about one thing that might cause you to adjust the plan.

#### Bottom Line
>  Planning helps AI break big goals into doable steps and adapt as things change.

---

### Multi-Agent Collaboration (Teamwork)
- **Idea:** Several small helpers (agents) work on different parts of a big task.  
- **Benefit:** They can review each other’s work and combine efforts for better results.

#### What It Means
Instead of one AI doing everything, several AI agents work together like a team. Each one handles a different part of a big task.

#### How It Works
- Each agent has a specific role and clear instructions.  
- They work on their parts, share results, and critique each other to improve the final answer or product.  
- A main planner or human supervisor helps keep everything coordinated.

#### Example: A Marketing Campaign
- **Content Creator:** writes ads and social posts  
- **Market Analyst:** studies customer trends  
- **Campaign Strategist:** plans the overall approach  
- **Performance Evaluator:** checks how well the campaign is doing  

#### Sample Prompts for Each Role
- **Content Creator:** “You are an expert copywriter. Write engaging content for the new product.”  
- **Market Analyst:** “You are a market expert. Analyze recent data and suggest strategies.”  
- **Campaign Strategist:** “Plan the overall marketing approach and schedule.”  
- **Performance Evaluator:** “Review results, explain what’s working, and suggest improvements.”  

#### Why It Works
- Studies show many helpers together can do better than one alone.  
- When agents critique each other’s work, they tend to produce smarter, more accurate results.

#### Optional Quick Class Activity
- Split into small groups.  
- Pick a big project (like planning a school event) and assign simple roles to pretend AI agents.  
- Have each group write one sentence for what their role would do and how they’d share results with the team.  
- Then discuss how the team could improve the final plan.

## Bottom Line
>  Teamwork among AI agents helps tackle big, tricky tasks more effectively by dividing work and sharing feedback.

---

### Autonomy (Independence with Supervision)
- **What it means:** The agent can make some decisions independently to move tasks forward.  
- **Important balance:** A human overseer checks important or risky decisions for safety and correctness.

#### What It Means
Autonomy is when an AI can make decisions and act by itself, without a human guiding every step.

#### How It Works (In Simple Terms)
- It understands data from its environment (sensors, user inputs, etc.).  
- It learns from past experiences (what happened before).  - It adapts to new situations in real time (adjusts its actions when things change).

#### Examples
- **Self-driving cars:** They read sensor data, spot obstacles, and decide how to drive safely all on their own.  
- **Customer service AI:** It learns from past chats to give better answers next time.

#### Important Caveat
Full autonomy isn’t always the best. We need a balance between letting AI act independently and having humans supervise to keep things safe and aligned with goals.

#### Other Notes
Not every task needs all features. Depending on what you want, you might enable some abilities and skip others.

#### Optional Class Activity
- Think of a task (like running a school event).  
- List one thing the AI should do automatically and one part you’d want a human to supervise.  
- Discuss how you’d keep things safe and on track.
  
#### Bottom Line
>  Autonomy lets AI do things on its own, but with safeguards to ensure safety, ethics, and goal alignment.

---

### UI/UX (How People Interact With It)
- **Why it matters:** A clear interface lets you see what the agent is doing, fix mistakes, and trust its decisions.  
- **Good design:** Shows actions and reasons clearly, with easy ways to give corrections or stop tasks.

#### What They Are
- **UI (User Interface):** How the software looks and how easy it is to use.  
- **UX (User Experience):** The overall feel of using the software—how smooth, accessible, and helpful it is.

#### Why They Matter
- Good UI/UX helps people learn faster, make fewer mistakes, and get things done more easily.  
- People are more likely to use and trust software that feels good to use.

#### UI/UX with AI Agents (The Big Idea)
- AI agents with big language models (LLMs) sometimes make mistakes, so chat-style interfaces are common.  
- They let you see what the AI is doing, fix it, and ask questions—keeping humans in the loop.  
- This means the AI acts more like a helpful co-pilot than a fully independent worker.

#### How to Make It Better
- Be transparent and keep logs: show what the AI did, so you can review or change it later.  
- Make things easy at home or in business apps: for example, a simple interface to adjust device schedules while the AI handles day-to-day tasks.  
- Learn from feedback: the AI should improve when you tell it what you liked or didn’t like.  
- Proactive features: AI can send helpful updates or ask questions without you opening the app.  
  - *Example:* Energy use is high today—should I lower the thermostat?

#### Practical Examples
- **Home automation:** You see, edit, and approve suggested changes to lights, thermostat, or security.  
- **Energy app:** AI notices high energy use and asks if you want it to cut back.  
- **Customer support AI:** Shows what it’s doing in a chat, lets you correct it, and uses that feedback to improve.

#### Design Tips (Simple)
- Keep controls obvious: where to click, what will happen next.  
- Show short explanations: a quick reason for the AI’s choice.  
- Let users review and undo: easy way to fix mistakes.  
- Make it polite and helpful, not creepy or pushy.

#### Quick Activity (Optional)
Think of a task (like planning a school event).  
- List 3 UI features that would help you use an AI agent for it.  
- List one way the AI could proactively help you.

#### Key Takeaways
- Good UI/UX makes AI tools easy to use, trusted, and more productive.  
- AI agents with LLMs are often best used as helpful co-pilots, not fully autonomous workers, because they can make mistakes.  
- Transparency matters: keep logs of what the AI did and let users review or undo actions.  
- Interfaces should be simple for real tasks (e.g., adjust home device schedules) while the AI handles routine work.  
- The best designs learn from feedback and can be proactive, sending useful updates or asking questions without being asked.  
- Use clear, polite, and helpful prompts, with easy ways to correct or override the AI.

---

### How Generative AI Agents Differ from Traditional Software
- **Traditional software:** Always does the same thing exactly as programmed.  
- **AI agents:** Learn, adapt, and make choices but need guardrails and human checks because results aren’t always perfect.

### Traditional Software Development (Easy Version)

#### Six Steps:
1. **Requirements:** Figure out what the software should do.  
2. **Design:** Plan how to build it.  
3. **Implementation:** Write the code.  
4. **Testing:** Test everything to fix problems.  
5. **Deployment:** Release it for people to use.  
6. **Maintenance:** Keep improving it over time.

#### Why This Works:
- The process is predictable, so big projects and teams can manage it effectively.

#### AI Agents: A Different, Less Predictable World
#### How It Works:
- **Pick a use case:** Not all tasks fit AI well, because AI outputs are guesses, not fixed rules.  
- **Choose AI models:** Models are complex and often updated.  
- **Costs:** High costs from cloud APIs or buying hardware to run models.  
- **Guardrails & human checks:** AI can make surprising or wrong answers, so safety rules and human review are essential.

#### Testing AI Agents Is Harder
- AI responses aren’t fixed like normal software outputs, so simple tests don’t work well.  
- Testing needs new methods:  
  - Compare different outputs  
  - Watch for improvements or mistakes  
  - Look for regressions  
- Tools for monitoring and debugging AI are still being developed.

#### How People Try to Make AI More Accurate
- Use company data in special databases so AI has the right facts.  
- Fine-tune models or use **Retrieval-Augmented Generation (RAG):** helps AI pull in relevant info to answer better.  
- **Example:** Building a help chatbot connected to company documents and policies for accurate answers.

#### Key Takeaways
- Traditional software is predictable; AI agents are more flexible but also more unpredictable.  
- Guardrails and human oversight are common and important with AI.  
- Testing AI focuses on comparing outputs and monitoring changes over time.  
- Using real data and tools like RAG helps AI provide better, more accurate answers.

---

## Related Concepts: LLMs, Copilots, and RPA
- **General-purpose LLMs:** Great at writing and talking but not always perfect at complex tasks.  
- **Copilots:** Domain-specific helpers (e.g., marketing, law) that assist in specific areas.  
- **RPA (Robotic Process Automation):** Automates repetitive, rule-based tasks; combined with AI, it handles more complex thinking.  
- **Trend:** These ideas blend over time to create more capable AI agents.

### LLMs

#### What They Do
- Great at chatting and generating text from prompts.

#### What They Can Do With Tools
- Some can use web search or APIs, but usually don’t plan or act on complex tasks.

#### Main Job
- Provide information and have conversations.
- Not designed to make big decisions or run tasks independently.

#### Example
- A chat assistant that explains concepts or answers questions.

### Copilots

#### What They Are
- Specialized AI helpers focused on specific jobs or industries (e.g., marketing, law, HR).

#### What They Do
- More than just chat—assist with tasks like writing ads, analyzing data, drafting reports.

#### How They Work
- Pull info from emails, databases, and other sources.
- Provide suggestions that users can accept or edit.

#### Why It’s Useful
- Makes work faster and easier in their area of expertise.

### Robotic Process Automation (RPA)

#### What It Is
- Bots that automate simple, repetitive tasks (like clicking buttons or entering data) using fixed rules.

#### Limitation
- They don’t “think” or make decisions like AI.

#### How AI Helps
- Adding AI to RPA enables handling smarter, more complex jobs.

#### The Future: AI Agents Will Dominate
>  Over time, LLMs, copilots, and RPAs may blend into versatile AI agents that handle many tasks, not just one.

#### Business Impact: Changing How Software Is Sold
- The software market is huge—over $261 billion today.
- **Outcome-based pricing:** Instead of paying per user or per month, customers pay based on how much AI improves productivity, saves money, or helps make better decisions.
- This pricing focuses on results, not just seats or usage.

---

## Real-World Use Cases

- **Flight rebooking**: AI agents help passengers automatically rebook flights when cancellations happen.
- **Policy review**: Agents find conflicting or contradictory points between new and existing company policies.
- **Document creation**: AI helps write long documents with built-in fact checking and validation.  
- **Research assistants**: Agents gather and analyze information from multiple sources to complete complex tasks that would take humans much longer.

---

## Case Study: Sierra

- Builds AI agents for big companies to improve customer experience.  
- Focuses on security, privacy, safe data handling, and pricing based on real problem-solving rather than just usage time.

---

## Business Models and Pricing

- Moving from paying per user or per month to **outcome-based pricing** — charging based on actual improvements delivered.

---

## Bottom Line

AI agents are **smart helpers** that think about tasks, use tools, remember things, plan steps, and work together.  
They’re more flexible than normal software but need safety checks and people watching important decisions.  
They’re already speeding up work and saving money in the real world, with new ways to pay for them being explored.
