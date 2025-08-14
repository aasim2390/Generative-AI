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

```bash
Personalized Debt Management Plan
1. Current Financial Overview:
Monthly Income: $5,000

Expenses*:

Fixed Expenses:

Rent: $1,500
Utilities: $300
Variable Expenses:

Groceries: $400
Transportation: $200
Entertainment: $150
Other: $450
Total Expenses: $3,000

Debt Repayment*:

Credit Card:

Balance: $2,000
Minimum Payment: $60
Student Loan:

Balance: $15,000
Minimum Payment: $150
Total Minimum Debt Repayment: $210

Savings Goal*: 
500∗∗TotalAllocated∗∗:3,710

Remaining Balance*: $1,290

2. Debt Repayment Strategy:
Immediate Actions:

Pay Off High-Interest Credit Card Debt: Use $1,050 of the remaining balance to pay off the credit card debt entirely. This action eliminates high-interest payments, which can be around 15-25% annually.

Adjusted Allocation After Credit Card Payoff:

Remaining balance after credit card payoff: $240
Continue making the minimum student loan payment of $150.
3. Monthly Surplus Allocation:
After the credit card payment is completed, you will redirect all remaining monthly surpluses ($1,290) to accelerate your financial goals. Here’s a proposed breakdown:

Savings Goal Completion: Regularly allocate your savings to build your emergency fund (
500monthlyuntilreaching12,000, which should take 24 months).

Debt Reduction Strategy: Redirect surplus funds towards your student loan after fully addressing immediate credit card debt. Allocate the remainder of your monthly surplus as follows once the credit card is cleared:

$500/month into an aggressive ETF or diversified stock portfolio for potential growth.
$100/month into a bond fund for stability.
$690/month more towards aggressive student loan repayments.
4. Additional Strategies for Faster Debt Reduction:
Review Discretionary Spending:

Cut down on entertainment and "other" expenses by 15-20%, potentially saving an additional 
90
−
90−120 monthly, which can also be redirected to your debt payments.
Smart Grocery Shopping:

Implement meal planning, using coupons, and buying in bulk, which could save you an additional $60 monthly.
Limit Transportation Costs:

Explore public transportation or carpooling options to decrease your transportation budget, saving at least 
50
−
50−100 monthly.
5. Long-Term Financial Goals:
Short-Term (1-3 years):

Build an emergency fund covering 3-6 months of expenses (approximately $12,000).
Aggressively pay down student loan debt while maintaining smaller investments.
Long-Term (5-20 years):

Save for a home purchase or other significant investments.
Contribute 10-15% of your income to retirement savings (Roth IRA/401(k)).
6. Investment Options:
Once the high-interest debts are settled, consider the following conservative to aggressive strategies based on your risk tolerance:
Conservative: Invest in bond funds or short-term treasury bonds.
Moderate: Invest in broad market ETFs (e.g., S&P 500) for balanced growth.
Aggressive: Invest in individual stocks or high-growth sectors for potential high returns.
7. Review and Adjust:
Periodic Reviews: Regularly assess your budget, debt repayment progress, and investment performance quarterly to align with your financial goals.
Tracking Tools: Utilize budgeting apps or spreadsheets to monitor your spending patterns and adjust as necessary.
By implementing this structured debt management plan, you can significantly reduce your financial stress related to high-interest debt, while also building a solid foundation for future wealth growth. Remember to remain disciplined and committed to your goals—progress will come with consistency and focus!
```
## 4) Final Output

After running the above code, you will get:

- **Budget Plan** – Covers essential expenses, allocates savings, and suggests spending cuts.
- **Investment Plan** – Matches your financial goals with risk/return analysis.
- **Debt Management Plan** – Prioritizes high-interest debts and outlines repayment strategies.
