
# 🧠 AI-Powered Ticket Classifier

### 🚀 Overview

This project implements an **AI-driven ticket classification system** that automatically categorizes IT or support requests into predefined categories such as **Login Issue**, **Bug**, or **Data Extraction**.
It uses **LangChain**, **OpenAI embeddings**, and **cosine similarity** to dynamically route user queries to the most relevant prompt chain, generating a structured JSON response.

---

### 🏗️ Features

* 🔍 **Semantic Routing:** Automatically detects the intent of the user’s request using cosine similarity on embeddings.
* 🤖 **LLM-Powered Responses:** Uses GPT-based models to generate structured, human-readable summaries.
* 🧩 **Modular Chains:** Separate prompt chains for each category ensure domain-specific, context-aware answers.
* 💾 **Embedding Optimization:** Normalized embeddings improve similarity accuracy for better routing.
* 🧠 **Structured Output:** Responses follow a unified schema using Pydantic-based validation.

---

### 🧰 Tech Stack

* **Python 3.10+**
* **LangChain**
* **OpenAI API**
* **dotenv**
* **pydantic**
* **cosine similarity** from `langchain_community.utils.math`

---

### ⚙️ How It Works

1. **User inputs a ticket** → e.g., “I can’t log in to Outlook.”
2. **Embedding generated** → Converts request and chains into vector space.
3. **Cosine similarity computed** → Finds most relevant chain (Login/Bug/Data).
4. **Chain invoked** → Generates structured JSON response like:

   ```json
   {
     "user_request": "I can’t log in to Outlook.",
     "request_category": "Login Issue",
     "response": "Please reset your password or contact IT support for account verification."
   }
   ```

---

### 💡 Example Use Case

Support teams can automate triage of incoming tickets, reducing manual effort and response time while maintaining consistent communication.

---

### 📦 Future Enhancements

* 🧠 Add more categories dynamically.
* 🗂️ Save and load embeddings using **pickle** for performance.
* 🪄 Integrate with **Power Automate** or **Jira API** for workflow automation.

---
