# Retrieval‑Augmented Generation (RAG) with CrewAI — Step‑by‑Step Guide

> **Goal:** Understand *what RAG is*, *how CrewAI implements it*, and *how to build a working example* using `WebsiteSearchTool` to extract facts from a single web page and ground an LLM’s answer.

---

## 1) First, the Big Picture: What is RAG?
RAG = **Retrieve → Augment → Generate**.

1. **Retrieve** relevant facts from trusted sources (files, sites, databases).
2. **Augment** the LLM prompt with those facts (context window).
3. **Generate** an answer that cites or reflects the retrieved evidence.

**Why it matters:** RAG reduces hallucinations and keeps answers **grounded** in real content you control.

---

## 2) How CrewAI Fits In
CrewAI models a mini‑organization:
- **Agents** (specialists with roles/goals/tools)
- **Tasks** (clear instructions + expected outputs)
- **Crew** (orchestrates agents + tasks in a process: sequential or hierarchical)

For RAG, CrewAI agents use **tools** (like `WebsiteSearchTool`, `PDFSearchTool`, etc.) to fetch context that will ground the LLM’s response.

---

## 3) The Tool We’ll Use: `WebsiteSearchTool`
- Purpose: Search and extract text **from a specific website or page**.
- Great for: quickly grounding an answer in **one URL** (e.g., a Wikipedia page).
- Limitation: It won’t crawl the whole web; it focuses on what you point it to.

> **Example URL:** `https://en.wikipedia.org/wiki/Alan_Turing`

---

## 4) Mental Hook (Memorize This): **TURING** 🔑
Use **T‑U‑R‑I‑N‑G** to remember the build steps.

- **T**arget your source (URL)
- **U**se the right Tool (`WebsiteSearchTool`)
- **R**ole your Agent (who does what, with which tool)
- **I**nstruct a Task (clear description + expected output)
- **N**avigate the Process (sequential or hierarchical)
- **G**o! Kick off with inputs

---

## 5) Install & Prepare
Make sure your environment is ready.

- Install **crewai** and **crewai-tools**.
- (Optional) Install `langchain-openai` and `openai` if you want to specify a concrete LLM.
- Set your LLM provider key (e.g., `OPENAI_API_KEY`).
- Use Python ≥ 3.9.

---

## 6) Complete Example (WebsiteSearchTool)
A compact workflow that follows the **TURING** steps:

- **Target** the source → Alan Turing Wikipedia page.
- **Use** the `WebsiteSearchTool`.
- **Role** your agent → Website Researcher.
- **Instruct** a task → Search and summarize relevant information.
- **Navigate** → Process is sequential.
- **Go** → Provide topic input (e.g., “Artificial intelligence”) and run.

**What it does:**
- Extracts relevant text from the Alan Turing page.
- Focuses on facts about **Artificial intelligence**.
- Runs sequentially and outputs a grounded summary.

---

## 7) What’s Happening Under the Hood
1. **Tool Call:** `WebsiteSearchTool` fetches content from the URL and prepares relevant snippets.
2. **Context Packing:** CrewAI passes those snippets into the agent’s prompt as supporting context.
3. **Generation:** The LLM produces a summary **conditioned** on that retrieved text.

Result: The output is **anchored** to what’s actually on the page.

---

## 8) Quality Tips (Make It Rock‑Solid)
- **Constrain scope:** Keep your topic specific.
- **Determinism where needed:** Use `temperature=0` for factual answers.
- **Signal formatting:** Define bullet points, sections, or JSON schema in `expected_output`.
- **Be explicit about sources:** Request a “Sources consulted” section.
- **Chunk the work:** Break long pages into multiple tasks.
- **Cache & reuse:** Save retrieved snippets for repeat queries.

---

## 9) Common Pitfalls & Fixes
- Forgot to instantiate `search_tool` → Make sure it’s passed to both agent and task.
- Bad/blocked URL → Ensure it begins with `http(s)://` and is public.
- No LLM configured → Set `OPENAI_API_KEY` or specify an LLM.
- Prompts too broad → Narrow focus and clarify expected output.
- Site lacks topic coverage → Use another URL or adjust query.

---

## 10) Make It Memorable (Micro‑Mnemonics)
- **RAG:** *Retrieve → Augment → Generate.*
- **TURING:** *Target → Use → Role → Instruct → Navigate → Go.*
- **GROUNDS:** *Get source • Reduce scope • Outline output • Use tools • Nudge temperature • Double‑check URL • Split tasks.*

---

## 11) Variations: Swap the Tool, Keep the Pattern
- **`CSVSearchTool`** → Search in CSV files.
- **`DOCXSearchTool`** → Extract from Word documents.
- **`PDFSearchTool`** → Extract and search PDFs.

> The choreography stays the same (TURING). Only the **U** (Tool) changes.

---

## 12) Extending the Example (Ideas)
- Add citations with snippets and headings.
- Introduce a “Reviewer” agent for claim verification.
- Run multiple URLs and merge results.
- Require JSON output for automations.

---

## 13) Quick Troubleshooting Checklist
- [ ] Can I open the URL in a browser?
- [ ] Did I pass the tool to both **agent** and **task**?
- [ ] Is my topic too broad?
- [ ] Should I set `temperature=0`?
- [ ] Do I need a Reviewer agent or stricter `expected_output`?

---

## 14) One‑Screen Recap
- **RAG:** Ground answers in retrieved facts.
- **CrewAI:** Agents + Tasks + Tools + Process.
- **Flow:** TURING → Target URL → Tool → Agent → Task → Process → Kickoff.
- **Win:** Fewer hallucinations, more trustworthy answers.

---

### Bonus: Prompt Snippet for Crisper Outputs
Write a factual summary focused on "{topic}" using only the provided website context.  
- Include 5–7 bullet points, each <25 words.  
- Add a short "Why this matters" section.  
- If the site lacks coverage, state that explicitly.

---

### Sample Code
```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import WebsiteSearchTool

# 1) Target your source (URL)
URL = "https://en.wikipedia.org/wiki/Alan_Turing"

# 2) Use the right Tool
search_tool = WebsiteSearchTool(website=URL)

# 3) Role your Agent
search_agent = Agent(
    role="Website Researcher",
    goal="Search and extract relevant information from a specific website.",
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in searching websites for the most relevant and up-to-date "
        "information. Extract concise, accurate facts and avoid speculation."
    ),
    tools=[search_tool],
)

# 4) Instruct a Task
search_task = Task(
    description=(
        "Use the provided website to find information on the topic '{topic}'. "
        "Collect the most relevant, factual details and avoid unrelated content. "
        "Return 5-7 bullet points and a brief 'Why this matters' section."
    ),
    expected_output=(
        "A well-structured summary grounded strictly in the website's content, "
        "focused on the requested topic. Include a short 'Sources consulted' section."
    ),
    tools=[search_tool],
    agent=search_agent,
)

# 5) Navigate the Process
research_crew = Crew(
    agents=[search_agent],
    tasks=[search_task],
    process=Process.sequential,
)

# 6) Go! Kick off with inputs
if __name__ == "__main__":
    inputs = {"topic": "Artificial intelligence"}
    result = research_crew.kickoff(inputs=inputs)
    print("
===== RAG RESULT =====
")
    print(result)
```
