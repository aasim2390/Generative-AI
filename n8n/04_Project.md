# n8n Agentic Automation for Reliable Updates

This project automates the process of fetching, summarizing, validating, and distributing recent updates about **n8n** using an agentic workflow.  
It ensures only high-quality, reliable outputs are delivered to users, while failed evaluations automatically generate improvement suggestions for developers.

---

## 🔄 Workflow Overview

1. **Tavily Search**  
   - Fetches the most recent updates on **n8n** (last 5 days).  

2. **LLM Summarizer**  
   - Generates concise bullet-point summaries of the updates.  

3. **Evaluator Agent**  
   - Validates the quality of the LLM response (accuracy, clarity, usefulness).  

4. **Decision Step**  
   - ✅ **Pass** → Sends a summary email update to the user.  
   - ❌ **Fail** → Sends a report with improvement suggestions to the developer.  

---

## 🛠️ Tech Stack

- **n8n** – Workflow orchestration  
- **Tavily API** – Recent web search  
- **LLM (GPT-based)** – Summarization  
- **Evaluator Agent** – Quality validation  
- **Email Node** – Automated notifications  

---

## 🚀 Key Features

- Automated collection of **up-to-date insights**  
- Built-in **quality control loop**  
- **Self-improving**: failed outputs return improvement suggestions  
- Reliable delivery to the right audience (users vs developers)  

---

## 📌 Example Use Case

- Daily / Weekly digest of **n8n product updates**  
- Automated research workflows with **trusted outputs**  
- Internal team communication where **accuracy matters**  

---

## 📧 Notifications

- **User Email** → Clean and verified summaries  
- **Developer Email** → Failed evaluations + suggested improvements  

---

## 🔮 Future Enhancements

- Support for multiple topics (not just n8n)  
- Dashboard for monitoring evaluation results  
- Integration with Slack/Teams instead of email  

---


<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/6e577c3c-8108-4148-bf59-3497dbb46150" />


---

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/f179aee4-1244-4f7d-b4f6-9489ec978c38" />


---

#### Research Agent Prompt

**System Message**
```bash
You are a LinkedIn content writer for B2B tech and automation.
```
**User Message**
```bash
Based on the last 5 days’ search results about "{{ $json.MyTopic }} releases or updates," create a short, engaging LinkedIn post under 2000 characters.

Search Results:
[ Call Travily to get latest results]

Instructions:
- Start with a compelling benefit-focused hook.
- Summarize key updates into up to 4 bullet points with emojis.
- Use simple language; avoid technical jargon or inventing details.
- End with an open-ended question to encourage engagement.
- Cite the source: "📌 Source: <best URL from results>"

```

---

#### Evaluator Agent Prompt

**System Message**
```bash
You are a LinkedIn content quality evaluator. 
```

**User Message**
```bash

Task: Review the LinkedIn post below and check if it meets these requirements:
- Under 2000 characters
- Starts with a strong, benefit-focused hook
- Contains up to 4 bullet points with clear, easy-to-read benefits
- Includes an open-ended question for engagement
- Ends with a source link
- Uses simple, non-technical language
- Does NOT invent details

Respond in JSON with the following structure:
{
  "pass": true/false,
  "issues": ["list of issues if any"],
  "improvements": "suggested improvements (optional)"
}

Post to review:
[{{ $json.output }}]

```

---

#### Output HTML Prompt

**User Message**
```bash
Text: {{ $('Research Agent').item.json.output }}
```
**System Message**
```bash
You are a helpful assistant. Read the given text and rewrite it into a well-structured HTML format suitable for a LinkedIn post. Only provide the <body> section in your response, without including <html> or <head> tags.
```

---
