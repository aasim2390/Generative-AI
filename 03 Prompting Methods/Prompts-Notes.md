# Prompt Practice for Agentic AI Developers – Easy Notes

## 1. What is Agentic AI?  
**Definition:** Agentic AI is an AI system that can **think (reason)**, **use tools**, and **act on its own** to complete tasks.  

**Example:**  
An AI that can decide the best way to plan your holiday, search flights using an API, and then give you the results.

---

## 2. Why are Prompts Important?  
A **prompt** is the instruction you give to AI. Good prompts make AI give better answers, faster, and cheaper.  

**Example:**  
- ❌ **Bad prompt** – "Get weather." (Too vague)  
- ✅ **Good prompt** – "Use the weather API tool to get today’s temperature and condition in London."

---

## 3. Key Factors for Good Agent Prompts  
To make AI perform best, focus on:  
1. **Reasoning ability** – Asking AI to think step-by-step.  
2. **Tool-calling proficiency** – Telling AI exactly which tool to use.  
3. **Accuracy** – Making sure answers are correct.  
4. **Cost efficiency** – Keeping answers short and to the point so it’s cheaper to run.  
5. **Structured output** – Clear format (tables, bullet points, JSON, etc.).  
6. **Context size** – Giving AI only the info it needs, not too much.

---

## 4. Practice Exercises and Lessons

| # | Scenario | Good Prompt | Key Learning |
|---|----------|-------------|--------------|
| **1** | Check if a number is even/odd | “Is 42 even or odd? Think step-by-step and explain.” | Improves reasoning and accuracy. |
| **2** | Get London weather | “Use the weather API tool to get today’s temperature and condition in London, UK.” | Practice tool-calling. |
| **3** | List AI project ideas in a table | “Give 3 AI project ideas in a table with Name and Description. Example: \| Name \| Description \| …” | Structured output with example. |
| **4** | Short professional answer | “Explain AI ethics in under 50 words, in a professional tone.” | Saves cost, keeps clarity. |
| **5** | Role + tool usage | “Act as a data analyst. Use the database tool to find Q1 2025 sales trends in bullet points.” | Role assignment + clear format. |
| **6** | Summary without extra details | “Summarize this 500-word article in 100 words. Focus on key points only.” | Avoid overcomplication. |
| **7** | Step-by-step with tool | “Calculate shipping for 5kg from NY to Paris using logistics API. Steps: 1) Query API 2) Process data 3) Return cost.” | Step-by-step reasoning + tool use. |
| **8** | JSON output | “Summarize this user profile in JSON: {‘summary’:” | Output priming for efficiency. |
| **9** | Detailed plan with tools | “Make a 3-month marketing plan using analytics & budget tools. Include strategy, timeline, and cost. Explain step-by-step.” | Complex reasoning + multiple tools. |
| **10** | Fix vague prompt | Change “Use tool get data about sales fast” → “Use sales data tool to get March 2025 sales in a list.” | Be specific + structured. |
| **11** | Compare vague vs. specific | Prompt 1: Vague. Prompt 2: Uses tool, limits to top 3 trends, table format, under 500 tokens. | Manage context for accuracy + cost. |

---

## 5. Quick Tips for Writing Great Prompts
- **Be specific** → Name the tool, mention format, limit length.  
- **Add examples** → Show AI exactly what you want.  
- **Guide the thinking** → Ask for step-by-step answers when needed.  
- **Keep it short** → Avoid giving too much unnecessary information.  
- **Structure the output** → Tables, bullet points, or JSON make it easy to read.

---

💡 **Example of a Perfect Prompt Combining All Rules:**  
> “Act as a travel planner. Use the flight search API to find 3 cheapest flights from Delhi to Dubai for 15th Aug 2025. Show results in a table with Airline, Price, and Departure Time. Keep it under 100 words.”
