# 🚀 LaunchMaster – Product Launch Orchestrator  

LaunchMaster is an **AI-powered product launch assistant** built with the CrewAI framework.  
It coordinates specialized agents and tools to manage research, content creation, and outreach for product launches.  

---

## 📌 Requirements  

1. **Environment Setup**  
   - Python 3.9+  
   - Install dependencies:  
     ```bash
     pip install crewai crewai-tools pydantic rich python-dotenv openai
     ```

2. **API Keys**  
   - `OPENAI_API_KEY` → for AI model usage  
   - `SERPER_API_KEY` → for search queries  

3. **Output Storage**  
   - All generated results are saved under `./outputs/<timestamp>/` in **Markdown** and **JSON** formats.  

---

## 🔧 Tools Used  

- **Built-in Tools**  
  - `SerperDevTool` → search engine integration  
  - `ScrapeWebsiteTool` → scrape information from websites  

- **Custom Tools**  
  - `SaveMarkdownTool` → save AI outputs to your computer  
  - `PauseForApprovalTool` → request human review before proceeding  

---

## 🧩 Key Concepts  

- **CrewAI Framework** – manages agents, tasks, and workflows  
- **Pydantic Models** – used as “blueprints” to validate and structure scraped or generated data  

---

## ⚙️ Workflow Steps  

1. **Market Research**  
   - Identify demographics, competitors, and trends  
   - Save summaries as structured reports  

2. **Content Creation**  
   - Draft landing page copy, ads, emails, and press releases  

3. **Influencer & Media Outreach**  
   - Generate contact lists and outreach templates  

4. **Human Review (Optional)**  
   - Pause execution for approval before saving final files  

5. **Final Delivery**  
   - Save all deliverables (Markdown + JSON)  

---
## Outputs generated:

 - research_summary.md

- content_pack.md

- outreach_plan.md

---

## ✅ Understanding in Simple Terms

- Think of **LaunchMaster** as a **project manager AI**.

- It researches the market, creates content, and builds outreach plans.

- You can approve work at checkpoints.

- All results are neatly saved in files.

