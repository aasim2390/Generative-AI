## Customer Call Center Processing with CrewAI

This example shows how a call center process can be automated using CrewAI with multiple specialized agents working together.

### 1. Import Libraries

We first bring in required libraries:

- `ChatOpenAI` → LLM that manages the team
- `Crew`, `Process`, `Agent` ,`Task`→ CrewAI components to create agents, tasks, and workflows
  ```python
  from langchain_openai import ChatOpenAI
  from crewai import Crew, Process, Agent, Task
  from pydantic import BaseModel
  ```
> ChatOpenAI is the Supervisor in the hierarchical workflow. Without it, the agents wouldn’t know who to pass work to or how to escalate properly.
> 
👉 Why: These are the building blocks for defining agents, their tasks, and how they collaborate.

### 2. Define Agents (Roles in Call Center)

Each agent has a role, a goal, and a backstory.
This makes them act like specialized employees.

**Example: Call Handling Agent**
```python
    call_handling_agent = Agent(
    role="Call Handling Agent",
    goal="Manage and resolve customer inquiries via phone: {call_action_taken}",
    tools=[],
    allow_delegation=True,  # can escalate issues
    verbose=True,
    backstory=("Handles calls, routes to departments, resolves basic queries efficiently.")
)

```
Note: **call_action_taken** is a runtime variable describing what the Call Handling Agent actually did during the customer’s call.
It personalizes the goal of the agent to the actual action taken in that call. Few examples:

- "Resolved password reset request without escalation"
- "Transferred customer to Billing Agent for payment dispute"
- "Provided troubleshooting steps and escalated to Technical Support"
- "Handled account information update and closed the call"


👉 Why: This agent takes the first customer call and decides if it can be solved or must be escalated.

**Technical Support Agent**
```python
    tech_support_agent = Agent(
    role="Technical Support Agent",
    goal="Troubleshoot technical issues: {technical_action_taken}",
    tools=[],
    allow_delegation=True,  # can escalate if unresolved
    verbose=True,
    backstory=("Provides remote assistance, troubleshooting, and ticketing.")
)
```

Note: **technical_action_taken** = what the Technical Support Agent actually did while troubleshooting.
It makes the goal text dynamic and specific to the real interaction. E.g.

- "Provided step-by-step troubleshooting for connectivity issue and resolved successfully"
- "Performed remote assistance to reinstall drivers, issue resolved"
- "Escalated unresolved software bug to engineering team"
- "Created a support ticket for hardware replacement and updated customer"


👉 Why: Focused only on technical problems.

**Billing Agent**
```python
billing_agent = Agent(
    role="Billing & Payments Agent",
    goal="Handle billing inquiries, process payments: {billing_action_taken}",
    tools=[],
    allow_delegation=False,  # billing handled directly
    verbose=True,
    backstory=("Expert in invoices, payments, and resolving disputes.")
)
```

Note: **billing_action_taken** = the specific resolution (or action taken) by the Billing & Payments Agent for the customer’s billing issue. E.g.

- "Processed payment successfully and confirmed with customer"
- "Corrected invoice error and reissued updated invoice"
- "Resolved duplicate charge and initiated refund"
- "Explained billing policy and reassured customer about next cycle charges"

👉 Why: Directly resolves billing issues (no delegation).

**Feedback Agent**
```python
feedback_agent = Agent(
    role="Customer Feedback & Surveys Agent",
    goal="Gather customer feedback: {customer_feedback}",
    tools=[],
    allow_delegation=False,
    verbose=True,
    backstory=("Specialized in surveys and sentiment analysis.")
)
```
Note: customer_feedback is the placeholder that the Feedback Agent fills in at the end of the workflow.
It captures the customer’s reaction after the agent handled their issue (billing, technical, or call).
This gives the workflow a “closing loop” — we don’t just log what action was taken, but also how the customer felt about it. E.g.

- "Customer expressed satisfaction and thanked support team"
- "Customer requested follow-up call tomorrow to confirm issue is fully resolved"
- "Customer was unhappy with resolution and requested escalation"
- "Customer confirmed refund was received and appreciated the quick response"

  
👉 Why: Collects feedback after interaction.

### 3. Define Data Models

We use ***Pydantic BaseModel*** for structured storage of reports.

```python
class CallHandlingData(BaseModel):
    call_summary: str
    resolved_queries: str
    escalated_issues: str
```
(similar models for TechSupport, Billing, Feedback)

👉 Why: Ensures consistent output structure (reports for each department).

### 4. Define Tasks

Each task has:
- **description** → what needs to be done
- **expected_output** → what we want as result
- **context** → priority & SLA
- **callback** → log after completion

**Example: Call Handling Task**
```python
call_handling_task = Task(
    description="Handle incoming calls, resolve or escalate if needed.",
    expected_output="Report on calls handled and escalations.",
    human_input=True,
    output_json=CallHandlingData,
    output_file="call_handling_report.json",
    context={'priority': 'high', 'expected_resolution_time': '15 minutes'},
    agent=call_handling_agent,
    callback=lambda result: print(f"Done by {call_handling_agent.role}: {result}")
)
```

👉 Why: Defines scope, priority, and output format for the agent.

(Other tasks follow same pattern for Technical, Billing, Feedback)

### 5. Assemble the Crew

Bring all agents & tasks into one crew.

```python
customer_service_crew = Crew(
    agents=[call_handling_agent, tech_support_agent, billing_agent, feedback_agent],
    tasks=[call_handling_task, tech_support_task, billing_task, feedback_task],
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4o"), # Supervisor
    process=Process.hierarchical,  # tasks follow escalation path
    memory=True,   # remember past tasks
    planning=True  # allocate resources smartly
)
```

**Notes:**

`Process.hierarchical:`
- This means the agents work in a hierarchy rather than all in parallel or sequentially.
- A supervisor (manager_llm), here powered by ChatOpenAI, decides:
    - Which agent should handle which task
    - Whether tasks need to be escalated
    - In what order tasks should be executed

Example:
- Call Handling Agent answers a call.
- If it’s technical → Supervisor routes it to Tech Support Agent.
- If it’s billing → Supervisor routes it to Billing Agent.
- Finally → Feedback Agent collects the customer’s experience.

So the Supervisor AI (manager_llm) acts like a team lead managing escalation & delegation.

`memory=True`
- This enables context retention across tasks and agents.
- Without memory, each agent/task would behave as if it’s seeing the customer for the first time.
- With memory:
    - Agents can recall what happened in previous steps.
    - Example: If Call Handling Agent noted the customer’s account number, Tech Support Agent won’t ask again.
    - It also helps Feedback Agent know what issues were resolved earlier.

Think of it like a **shared notepad** for the whole crew.

`planning=True`
- This tells the crew to strategize execution of tasks instead of just running them blindly in order.
- Planning enables:
    - Smart task allocation (deciding which agent should act first)
    - Parallelization where possible
    - Re-ordering tasks if dependencies exist

Example:
Instead of always asking for feedback at the end, the supervisor may decide:
- First, resolve billing
- Then check if tech issues exist
- Only after both are done, trigger feedback

So planning makes the crew adaptive, not rigid.
      
👉 Why: The crew acts like a virtual call center team, coordinated by the LLM.

### 6. Provide Input (Customer Case)

We give details of a real customer interaction.

```json
customer_service_details = {
    'call_handling': {
        'queries_to_resolve': [
            'Update phone number',
            'Complaint about slow service'
        ],
        'call_action_taken': 'Phone updated, call transferred to technical support'
    },
    'escalations': {
        'technical_support': {
            'issue': 'Product malfunction after update',
            'technical_action_taken': 'Ticket created, transferred to billing'
        },
        'billing': {
            'issue': 'Overcharged invoice',
            'priority': 'High',
            'billing_action_taken': 'Refund issued, customer sent to feedback survey'
        }
    },
    'customer_feedback': {
        'feedback_sentiment': {'positive': '50%', 'neutral': '30%', 'negative': '20%'}
    }
}

```

👉 Why: Mimics live call data from customers.

### 7. Run the Crew

Kick off the workflow with the input.

```python
task_result = customer_service_crew.kickoff(inputs=customer_service_details)
```

👉 Why: This triggers the whole automation process.

### 8. Show Results

Finally, display the processed reports.

```python
from IPython.display import Markdown

def handle_task_completion(task_result):
    raw_result = task_result.raw
    print("Task completed:")
    Markdown(raw_result)
```

👉 Why: Gives a human-readable summary of what each agent did.

### ✅ Summary

- Step 1: Import libraries
- Step 2: Define agents (roles)
- Step 3: Define structured data models
- Step 4: Define tasks with context & outputs
- Step 5: Assemble the crew (hierarchical process)
- Step 6: Input customer details
- Step 7: Run the crew
- Step 8: Display results

This creates a mini virtual call center with automation + escalation + reporting.
