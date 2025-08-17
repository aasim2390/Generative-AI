
### Example

```python

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
import os
from dotenv import load_dotenv

# --------------------------------------------
# STEP 1: Load the environment variables
# --------------------------------------------
# We keep our API key safe in a .env file instead of writing it directly in code.
# This is like keeping your house key in your pocket instead of leaving it at the door.
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")


# --------------------------------------------
# STEP 2: Initialize the OpenAI model client
# --------------------------------------------
# Think of this as connecting to the brain (GPT model) we want to use.
openai_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=api_key)


# --------------------------------------------
# STEP 3: Define a custom function
# --------------------------------------------
def reverse_string(text: str) -> str:
    """
    Reverse the given text.
    
    Example:
    input: "Hello"
    output: "olleH"
    """
    return text[::-1]  # [::-1] means flip the string backwards.


# --------------------------------------------
# STEP 4: Register the custom function as a tool
# --------------------------------------------
# Tools are like special abilities we give to the AI.
# Here we give it a 'reverse_string' tool so the AI can flip text.
reverse_tool = FunctionTool(reverse_string, description='A tool to reverse a string')


# --------------------------------------------
# STEP 5: Create an AI agent with the tool
# --------------------------------------------
# - name: The agent’s nickname is "ReverseAgent".
# - system_message: Tells the agent its job (reverse text + give a summary).
# - tools: The list of powers it has (reverse_tool).
# - reflect_on_tool_use: Lets it check its tool use.
agent = AssistantAgent(
    name="ReverseAgent",
    model_client=openai_client,
    system_message="You are a helpful assistant that can reverse text using the reverse_string tool. Give the result with the summary",
    tools=[reverse_tool],
    reflect_on_tool_use=True,
)


# --------------------------------------------
# STEP 6: Define the task
# --------------------------------------------
# This is the request we give to our agent.
# Here we ask: "Reverse the text 'Hello, how are you Doing?'"
task = "Reverse the text 'Hello, how are you Doing?'"


# --------------------------------------------
# STEP 7: Run the agent
# --------------------------------------------
async def main():
    # The agent reads the task and decides how to solve it using the tool.
    result = await agent.run(task=task)

    # Print what the agent replies back with.
    print(f"Agent Response: {result.messages[-1].content}")

    # Also show the direct output of our custom reverse_string function.
    print(reverse_string('Hello, how are you Doing?'))


# --------------------------------------------
# STEP 8: Run everything
# --------------------------------------------
# asyncio.run(main()) means: "start the program and let it handle async tasks".
if __name__ == "__main__":
    asyncio.run(main())
```




### 👉 In short:

- You connect to GPT.
- You give it a special power (tool) → reverse text.
- You create an agent with that power.
- You give the agent a task → reverse "Hello, how are you Doing?".
- It replies with the reversed text.

