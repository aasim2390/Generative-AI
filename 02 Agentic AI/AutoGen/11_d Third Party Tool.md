### Example Code

```python
import asyncio
from dotenv import load_dotenv
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from langchain_community.utilities import GoogleSerperAPIWrapper

# ------------------------------------------------
# STEP 1: Load API keys from .env file
# ------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # This is your OpenAI key from the .env file

# ------------------------------------------------
# STEP 2: Set up Serper API key (for Google Search)
# ------------------------------------------------
# NOTE: You should keep API keys private, not hardcode them in code.
os.environ["SERPER_API_KEY"] = "8c8e65ec131852cd74158b38f7e31c921da8d5e9"

# ------------------------------------------------
# STEP 3: Initialize the Google Serper Search Tool
# ------------------------------------------------
# type='news' → means it will fetch the latest news results.
search_tool_wrapper = GoogleSerperAPIWrapper(type='news')

# ------------------------------------------------
# STEP 4: Create a function that wraps the search tool
# ------------------------------------------------
# This is like giving the agent a "search power" it can use.
def search_web(query: str) -> str:
    """Search the web using Serper API"""
    try:
        return search_tool_wrapper.run(query)  # Perform the search
    except Exception as e:
        return f"Search failed: {str(e)}"  # Handle errors safely

# ------------------------------------------------
# STEP 5: Connect to OpenAI (GPT model)
# ------------------------------------------------
# We’ll use GPT-4o-mini as the brain for our agent.
openai_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=api_key)

# ------------------------------------------------
# STEP 6: Create an Assistant Agent with the search tool
# ------------------------------------------------
# - name: Agent’s name is "SearchAgent"
# - system_message: Defines its role (search the web & answer)
# - description: Short description of its purpose
# - tools: We give it the "search_web" tool we built
# - reflect_on_tool_use: Allows the agent to check if tool use makes sense
search_agent = AssistantAgent(
    name='SearchAgent',
    model_client=openai_client,
    system_message="""You are a helpful assistant that can search the web to find current information. 
    When asked a question, use the search_web tool to find relevant information and provide a comprehensive answer based on the search results.""",
    description='Searches the internet and provides detailed answers based on search results',
    tools=[search_web],
    reflect_on_tool_use=True
)

# ------------------------------------------------
# STEP 7: Demonstrate the tool with some queries
# ------------------------------------------------
async def demonstrate_search():
    """Demonstrate the search functionality"""
    print("=== AutoGen Third-Party Tools Demonstration ===\n")
    
    # Test queries to check how our agent works
    test_queries = [
        "Who won the last IPL tournament in cricket in 2025?",  # Example search
    ]
    
    for query in test_queries:
        print(f"Query: {query}")
        print("-" * 50)
        
        try:
            # Run the agent with the query
            result = await search_agent.run(task=query)

            # Print the agent's final response
            print(f"Response: {result.messages[-1].content}")
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "="*70 + "\n")

# ------------------------------------------------
# STEP 8: Main function to start everything
# ------------------------------------------------
async def main():
    await demonstrate_search()

# ------------------------------------------------
# STEP 9: Run the program
# ------------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())

```


### 🧠 What’s happening in simple words:

- Load keys → OpenAI key (brain) + Serper key (Google search power).
- Make a tool → search_web() so AI can search Google.
- Build an agent → Give GPT the tool + instructions.
- Ask a question → e.g. "Who won IPL 2025?"
- Agent uses the tool → fetches answer from the internet.
- Agent replies → combines search results + AI reasoning.
