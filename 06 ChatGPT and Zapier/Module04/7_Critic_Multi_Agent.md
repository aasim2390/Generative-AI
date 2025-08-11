# 🤯 Your AI's "Proofreader" Superpower: The Critic AI

Imagine your AI helper finishes a task — like writing an email or logging an expense.  
Instead of sending it straight to you, what if it could **get a second opinion** from another AI?  

That’s the idea behind the **Critic AI**.

---

## ✨ The Problem: Even Smart AIs Miss Things
Even the best AI can:
- Miss a detail 📝
- Misinterpret instructions ⚠️
- Leave out important info ❌

If you’re sending an important email or finalizing a report, you want to be **extra sure** it’s perfect.

---

## 🚀 The Solution: A Second AI for Quality Control
The **Critic AI** is:
- A **separate AI** whose *only job* is to review and critique the first AI’s work.
- Like a strict proofreader, editor, or quality-control inspector.

**Why two AIs?**
- **Main AI**: Focuses on *doing* the task (e.g., adding an expense).
- **Critic AI**: Focuses on *finding flaws* in the main AI’s work.
- This separation makes each AI better at its job.

---

## 🛠 Building a Critic AI
You’ll create a **second Custom GPT** with a **strict, detail-oriented persona**.

**Example Persona & Instructions:**
> "Act as a detailed critic. Carefully review the provided travel expense entry.  
> Check if it has: category, vendor, amount, and date.  
> If time is missing, tell the user they need to provide the exact date/time.  
> Be tough and thorough."

---

## 🔄 How the Two AIs Work Together

### 1. You Give an Instruction
You: `"Add Uber $7.20"`

### 2. Main AI Processes the Request
- Extracts known info (`vendor: Uber`, `amount: $7.20`).
- Decides: *"I need this reviewed by the expert!"*

### 3. Main AI Sends Details to Critic AI  
- Uses a Zapier action like `check_travel_expense_with_travel_expert`.
- Sends the details (`Uber $7.20`) to the **Critic AI**.

### 4. Critic AI Reviews
- Finds missing info (date, time, purpose, etc.).
- Writes a clear critique.

### 5. Critic AI Sends Feedback Back
- Sends its findings to the main AI via Zapier.

### 6. Main AI Communicates to You
Main AI:  
> "The travel expense expert found that the date of this expense is missing. Please provide the exact date."

---

## 💡 Example Interaction
**You:** `"Add Uber $7.20"`  
**Main AI:** `"Sending details to the travel expense expert..."`  
**Critic AI:** `"Missing: Date, Purpose, Origin/Destination, Receipt"`  
**Main AI:**  
> "To log this expense, I need:  
> - Date of the Uber ride  
> - Purpose of the trip  
> - Starting & ending locations  
> - Receipt (digital copy)  
> Please provide these before I proceed."

---

## 🤯 Why Critic AI is a Game-Changer
- **Super Accurate** → Catches errors and missing info before work is finalized.
- **Reliable Systems** → Reduces mistakes, increases trust in AI output.
- **Specialization** → Each AI has a clear role, making them more effective.
- **No Coding Required** → You can set this up with clear instructions + Zapier.

---

## 📌 Takeaway
The **Critic AI** pattern gives you:
- A *doer* AI (main agent)
- A *checker* AI (quality control)
- Seamless AI-to-AI collaboration

The result?  
Fewer mistakes, higher quality, and more trust in your AI’s work.


## Steps taken:

1. Created Conversational Action (Critic Agent)

   <img width="500" height="450" alt="image" src="https://github.com/user-attachments/assets/56d4b80f-46ea-40b1-a9b0-2f42d07f292d" />


2. Instruction of Critic Agent:

```
Act as detailed critic. Carefully critic my travel expenses entry. Is it missing anything? If so, give me feedback what is missing.  All expenses should have Category, Vendor, Amount, Date.

Allowed Categories are:

Air Fare
Ground Transportation
hotel
Breakfast
Lunch 
Dinner
Registration
Parking 
Gas
Other expenses related to travel


if the time is not known, give the feedback that user need to be asked for the date/time of the expense.

```
3. Action Name of Critic - "Check Expense with Travel Expert"

  <img width="500" height="450" alt="image" src="https://github.com/user-attachments/assets/6a9b98bb-5d18-4a1b-861b-1b26fe5e22de" />


4. Update the Instructions for Main agent:

```
You are going to help me catalog my travel expenses. Whenever I give you new expense, you will use add the travel expense action.

Before you add any expenses, do the following:
1. Get my current expenses and check if this expenses already entered. If it appears to be duplicate, confirm if I want to add it anyway.

2. Make sure and check them with the Travel Expense Expert first! If they tell you to correct something, make the necessary corrections or ask user for additional information

### Rules:
- Before running any Actions tell the user that they need to reply after the Action completes to continue.

### Instructions for Zapier AI Actions:
Step 1. Check for required action(s):
    - Call `list_available_actions` to generate available actions list
    - If required action exists → Step 4
    - If not → Step 2
Step 2. For missing required action(s):
    - Send configuration link
    - Wait for user to confirm they've configured the required action
Step 3. After user confirms configuration → proceed to Step 4 with original request
Step 4. Execute `run_action`:
    - Use the action ID from the results array of the `list_available_actions` response
    - Fill in required parameters based on user request

Required Actions:
- Action: "add_travel_expense"
- Action: "Get Travel Expenses"
- Action: "Check Expense with Travel Expert"

```


### Final Conversation:
```
Add uber 7.20
ChatGPT said:
Got it — before I can add your Uber expense of $7.20, I need to:

Get your current expenses to check for duplicates.

Run it by the Travel Expense Expert to make sure everything is correct.

Let’s start by listing the available actions so I can see if we have:

Get Travel Expenses

Check Expense with Travel Expert

Add Travel Expense

[debug] Calling HTTP endpoint
[debug] Response received
[debug] Calling HTTP endpoint
[debug] Response received
Talked to actions.zapier.com
✅ All required actions are available:

Get Travel Expenses

Check Expense with Travel Expert

Add Travel Expense

First, I’ll get your current expenses to check for duplicates.
After that, I’ll send it to the Travel Expense Expert for review.

Please reply after each action completes so we can continue.

[debug] Calling HTTP endpoint
[debug] Response received
Talked to actions.zapier.com
I’ve retrieved your current expenses — no Uber charges for $7.20 are listed, so this isn’t a duplicate.

Next, I’ll send the expense to the Travel Expense Expert for review before adding it. Please reply once that action completes so we can proceed.

[debug] Calling HTTP endpoint
[debug] Response received
Talked to actions.zapier.com
The Travel Expense Expert says your entry is missing:

Category (should be “Ground Transportation”)

Date of the expense

Explicit Vendor (“Uber”)

Can you give me the date for this Uber ride so we can add it correctly?

You said:
today's date
ChatGPT said:
Got it — we’ll log it as:

Category: Ground Transportation

Vendor: Uber

Amount: $7.20

Date: 2025-08-12

I’ll add this to your travel expenses now. Please reply after the action completes so we can finalize.

[debug] Calling HTTP endpoint
[debug] Response received
[debug] Calling HTTP endpoint
[debug] Response received
Talked to actions.zapier.com
✅ Added successfully:

Category: Ground Transportation

Vendor: Uber

Amount: $7.20

Date: 2025-08-12
```
