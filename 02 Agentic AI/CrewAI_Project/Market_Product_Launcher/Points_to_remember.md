## The ScrapeWebsiteTool for AI

Imagine you're an AI assistant and you need to get the latest news from a website. 
You can't just "look" at the internet like a human. You need a special tool to do it. 
That's where the **ScrapeWebsiteTool** comes in. It's like a digital hand that can grab information from websites for an AI to read and understand. This is called "web scraping."

To make this work, the AI needs another tool called **SerperDevTool**, which is like a super-fast search engine. 
You have to get a special key from the serper.dev website to use it, just like you need a key to get into a locked building. This key lets the AI use the search tool to find the right website before it scrapes the information.

### The SerperDevTool is a tool that allows an AI to perform a Google search.

Instead of seeing a messy web page, the AI gets the search results in a clean, organized format, making it easy to understand and use the information. 
This is especially useful for AI agents that need to access real-time, up-to-date information from the internet for tasks like research or content creation.

**SerperDevTool (The Search Engine):** This is the first step. The SerperDevTool is like a smart search engine for AI. 
It takes a user's question or command and performs a search on the internet using the Serper API. 
Instead of getting a visual webpage, the AI receives a structured list of results, including titles, links, and short descriptions. This organized data makes it easy for the AI to find the most relevant sources.

**ScrapeWebsiteTool (The Data Extractor):** Once the SerperDevTool finds the right websites, the ScrapeWebsiteTool takes over. 
Its job is to "scrape" or extract the actual content from a specific webpage. If the search tool finds a promising news article, the scraping tool will go to that link and pull out the text of the article itself. 
This allows the AI to read the full content, not just the search snippet.

>  Together, they allow an AI to first find information on the web and then collect the detailed data it needs from those sources.


```python
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from pydantic import BaseModel

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

market_researcher = Agent(
    role="Market Researcher",
    goal="Conduct thorough market research to identify target demographics and competitors.",
    model="gpt-3.5-turbo",
    max_tokens=1500,
    max_words=2500,
    tools=[search_tool, scrape_tool],  # Using Tools
    verbose=True,
    backstory=(
        "Analytical and detail-oriented, you excel at gathering insights about the market, "
        "analyzing competitors, and identifying the best strategies to target the desired audience."
    )
)
```
---

## What's a pydantic.BaseModel?

Think of a **pydantic.BaseModel** as a blueprint for data. Let's say you're building a character for a video game. 
The blueprint would say things like "this character must have a name (which is text)," "this character must have a health score (which is a number)," and "this character's special ability must be an item from a list."

The BaseModel does the same thing for data. It's a way to tell the computer exactly what kind of information to expect. 
If the AI is trying to scrape a website, the BaseModel makes sure the information it gets back is in the right format, like a title, a date, and the article's text. This prevents errors and makes the whole process run smoothly.

```python
class MarketResearchData(BaseModel):
    target_demographics: str
    competitor_analysis: str
    key_findings: str


market_research_task = Task(
    description="Conduct market research for the {product_name} launch, focusing on target demographics and competitors.",
    expected_output="A detailed report on market research findings, including target demographics and competitor analysis.",
    human_input=True,
    output_json=MarketResearchData, # Using Base Model
    output_file="market_research.json",
    agent=market_researcher
)
```

---

Imagine you're baking a cake. You have a few main jobs to do: mixing the batter, baking the cake, and decorating it.

async_execution=False is like deciding you have to finish mixing the batter completely before you can put the cake in the oven. It's a step-by-step process where one step can't start until the previous one is 100% done. It ensures the whole team waits until the content creator is finished with their part of the project before moving on.

human_input=True is like pausing after the cake is decorated to get approval from a friend or a family member before serving it. It means the process will stop and wait for a person to give feedback or permission. The AI won't finalize the content until a human has reviewed it, which is a great way to ensure the final product is high quality and error-free.


```python
content_creation_task = Task(
   description="Create content for the {product_name} launch, including blog posts, social media updates, and promotional videos.",
    expected_output="A collection of content pieces ready for publication.",
    human_input=True,
    async_execution=False,  # Change to synchronous
    output_file="content_plan.txt",
    agent=content_creator
)
```
