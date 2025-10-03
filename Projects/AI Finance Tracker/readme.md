
# 💰 AI-Powered Personal Finance Tracker

## 📖 Project Description

This project is a **personal finance tracker** integrated with **OpenAI Assistants API** and a **SQL database**.
It allows users to record expenses, track their weekly spending, and query financial summaries in natural language.
The assistant maintains **conversation history (threads)** to provide context-aware insights across multiple interactions.

The application is built with:

* **Python + Streamlit** for the UI.
* **SQL Server** (via pyodbc) for storing expense data.
* **OpenAI Assistants API** for intelligent conversation and financial summaries.
* **Thread + Run Management** to ensure conversation context is preserved.

---

## 🎯 Use Cases

1. **Expense Tracking**

   * Users can add expenses with category, amount, and date.
   * Data is stored in a central SQL database.
   * Each expense is logged in both the **DB** and the **assistant’s thread**.

2. **Weekly Expense Summary**

   * Query: *"Summarize my expenses for this week"*
   * The system fetches recent expenses from the database, passes them into the assistant prompt, and generates a **natural language summary**.

3. **Category-Wise Spending Insights**

   * Query: *"How much did I spend on groceries this week?"*
   * The assistant combines DB results + conversation context to provide category-specific breakdowns.

4. **Conversation Memory (Context Awareness)**

   * Instead of answering in isolation, the assistant keeps track of prior queries.
   * Example:

     * User: *"Show me this week’s expenses."*
     * Assistant: *"You spent ₹458 this week, mainly on groceries and transport."*
     * User: *"How about just groceries?"*
     * Assistant (uses context + DB): *"₹253.25 was spent on groceries this week."*

5. **Weekly Stats API**

   * A function (`get_weekly_stats_fn`) retrieves structured weekly spending directly from the DB, useful for **dashboards**.

---

## 🛠️ Technical Workflow

1. **Adding an Expense**

   * Function: `add_expense_fn`
   * Saves expense into DB and posts a message into the assistant thread.

2. **Summarizing Expenses**

   * Function: `get_summary_fn`
   * Builds a prompt with:

     * User’s query.
     * Database response.
     * Conversation history (thread).
   * Sends to Assistant via `client.beta.threads.runs.create`.
   * Polls run status until completed → retrieves assistant reply.

3. **Weekly Stats**

   * Function: `get_weekly_stats_fn`
   * Directly fetches aggregated weekly expenses from DB (bypasses AI).

---

## 🧑‍💻 Example Interactions

* **Adding expense:**

  ```
  User: Add ₹250 for groceries today  
  System: Expense of ₹250 for groceries added successfully!  
  ```

* **Weekly summary:**

  ```
  User: Summarize this week’s expenses  
  Assistant: You spent ₹458 this week. Groceries: ₹253.25, Transport: ₹125, Snacks: ₹55, Tea: ₹25.  
  ```

* **Category query:**

  ```
  User: How much was spent on groceries?  
  Assistant: ₹253.25 was spent on groceries this week.  
  ```

---

## 🔧 Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **Database**: SQL Server (pyodbc)
* **AI/LLM**: OpenAI Assistants API (Threads + Runs)
* **Environment Management**: `.env` for API keys, `requirements.txt` for dependencies

---

## 🚀 Future Enhancements

* Add **charts & dashboards** in Streamlit.
* Export summaries to **Excel/PDF reports**.
* Integrate **budget planning** & alerts (e.g., overspending).
* Extend to **multi-user support** (one assistant per user vs shared assistant).

