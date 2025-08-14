# CrewAI – Financial Planning Workflow
## 1) Intro

This example demonstrates how to use CrewAI to run three specialized AI agents:

**Budgeting Advisor** – Creates a monthly budget to manage income and expenses.

**Investment Advisor** – Suggests investment options tailored to goals and risk tolerance.

**Debt Management Specialist** – Designs a debt repayment strategy to reduce interest and improve financial health.

You provide your financial data (income, expenses, debts, savings goals) and the system returns a combined report containing:
- A budget plan with savings allocation and spending tips.
- An investment plan suited to your profile.
- A debt repayment plan with priorities and strategies.

## 2) Requirements

Before running the code, ensure:

- Python 3.8+ is installed.

The following Python packages are installed:
```bash
pip install crewai
pip install crewai crewai-tools
```

Execution environment: Jupyter Notebook, Google Colab, or any Python script.

## 3) Short Description and Related Code

#### Step 1 – Import Libraries
```python
from crewai import Agent, Task, Crew
```
- **Agent:** the individual expert
- **Task:** what the agent should do
- **Crew:** the group that runs the agents and tasks together

#### Step 2 – Create Agents

**Budgeting Agent**
```python
budgeting_agent = Agent(
    role="Budgeting Advisor",
    goal="Create a monthly budget to help users manage their income and expenses effectively.",
    backstory=(
        "You are an experienced financial advisor specializing in personal finance. "
        "Your goal is to help users allocate their income efficiently, ensuring they cover "
        "all necessary expenses while also saving for the future."
    ),
    allow_delegation=False,
    verbose=True
)
```

- This agent is the budgeting expert. The backstory gives it a persona so responses feel consistent and helpful.
- allow_delegation=False means this agent handles its tasks itself (no passing off to others).
- verbose=True makes the agent print more details about what it’s doing (useful for learning).

**Investment Agent**
```python
investment_agent = Agent(
    role="Investment Advisor",
    goal="Recommend suitable investment options based on the user's financial goals and risk tolerance.",
    backstory=(
        "You are an investment expert with years of experience in the financial markets. "
        "Your goal is to help users grow their wealth by providing sound investment advice "
        "tailored to their risk tolerance and financial objectives."
    ),
    allow_delegation=False,
    verbose=True
)
```
- This agent focuses on choosing investments that fit the user’s goals and comfort with risk.
  
**Debt Management Agent**
```python
debt_management_agent = Agent(
    role="Debt Management Specialist",
    goal="Help users manage and reduce their debt through effective strategies.",
    backstory=(
        "You specialize in helping individuals overcome debt by creating personalized repayment plans. "
        "Your focus is on reducing interest payments and improving the user's financial health."
    ),
    allow_delegation=False,
    verbose=True
)
```
- This agent designs a plan to pay down debts smartly and may suggest consolidation or rate negotiation.

  
#### Step 3 – Create Tasks

```python
budgeting_task = Task(
    description=(
        "1. Analyze the user's income and expenses. Financial Data: {financialdata}\n"
        "2. Create a detailed monthly budget including essential expenses, savings, and discretionary spending.\n"
        "3. Provide tips for optimizing spending and increasing savings."
    ),
    expected_output="A comprehensive monthly budget with recommendations for optimizing spending and savings.",
    agent=budgeting_agent
)

investment_task = Task(
    description=(
        "1. Assess the user's financial goals and risk tolerance.\n"
        "2. Recommend investment options (stocks, bonds, mutual funds, ETFs).\n"
        "3. Provide a brief overview of potential risks and returns."
    ),
    expected_output="A personalized investment plan with recommendations and risk assessments.",
    agent=investment_agent
)

debt_management_task = Task(
    description=(
        "1. Analyze the user's current debts with interest rates and balances.\n"
        "2. Create a repayment plan prioritizing high-interest debt.\n"
        "3. Suggest strategies for faster debt repayment and interest reduction."
    ),
    expected_output="A debt management plan with actionable steps to reduce and eliminate debt.",
    agent=debt_management_agent
)
```
- The task tells the budgeting agent exactly what to do with the provided data.
- The placeholder {financialdata} will be replaced by your actual data when kickoff runs.

#### Step 4 – Assemble the Crew
```python
crew = Crew(
    agents=[budgeting_agent, investment_agent, debt_management_agent],
    tasks=[budgeting_task, investment_task, debt_management_task],
    verbose=True
)
```
- The Crew ties together all three agents and their corresponding tasks so they can work in concert.

  
#### Step 5 – Provide Financial Data

```python
user_financial_data = {
    "financialdata": {
        "income": 5000,
        "expenses": {
            "rent": 1500,
            "utilities": 300,
            "groceries": 400,
            "transportation": 200,
            "entertainment": 150,
            "other": 450
        },
        "debts": {
            "credit_card": {
                "balance": 2000,
                "interest_rate": 0.18
            },
            "student_loan": {
                "balance": 15000,
                "interest_rate": 0.045
            }
        },
        "savings_goal": 500
    }
}

```

#### Step 6 – Run and Display Results
```python
result = crew.kickoff(inputs=user_financial_data)
raw_result = result.raw

from IPython.display import Markdown
Markdown(raw_result)  # For notebooks
# print(raw_result)  # For scripts

```

- Kick off the crew with your data

  
## 4) Final Output

After running the above code, you will get:

- **Budget Plan** – Covers essential expenses, allocates savings, and suggests spending cuts.
- **Investment Plan** – Matches your financial goals with risk/return analysis.
- **Debt Management Plan** – Prioritizes high-interest debts and outlines repayment strategies.
