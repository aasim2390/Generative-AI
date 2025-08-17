## Example

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
import os
from dotenv import load_dotenv

# ---------------------------
# Load API Key and Environment Setup
# ---------------------------

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# If the key is not found, raise an error
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# ---------------------------
# Model Initialization
# ---------------------------

# Create an OpenAI model client that the agent will use to call GPT models
openai_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",  # Smaller, faster GPT model
    api_key=api_key
)

# ---------------------------
# Custom Tool Definition
# ---------------------------

def reverse_string(text: str) -> str:
    """
    Reverse the given text.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed version of the input string.
    """
    return text[::-1]

# Wrap the function inside a FunctionTool so that the agent can call it like a plugin
reverse_tool = FunctionTool(
    reverse_string,
    description='A tool to reverse a string'
)

# ---------------------------
# Agent Creation
# ---------------------------

# AssistantAgent is a stateful agent that:
# - Can call tools
# - Holds memory of conversation (messages, tool use, reflections)
# - Follows termination conditions to know when to stop a run
agent = AssistantAgent(
    name="ReverseAgent",
    model_client=openai_client,
    system_message="You are a helpful assistant that can reverse text using the reverse_string tool. Give the result with the summary",
    tools=[reverse_tool],
    reflect_on_tool_use=True,  # lets agent reflect after using tools
)

# ---------------------------
# Task Definition
# ---------------------------

# This is the user request that will be passed into agent.run()
task = "Reverse the text 'Hello, how are you Doing?'"

# ---------------------------
# Run Logic
# ---------------------------

async def main():
    # Run the agent once with the given task.
    # NOTE: run() is *stateful* — it keeps track of messages, tools used, and termination signals.
    # BUT after every run(), the termination conditions automatically reset.
    # This means the agent starts fresh for each new run() call,
    # even though its memory still contains the past conversation if enabled.
    result = await agent.run(task=task)

    # Print the final assistant response (last message in the result)
    print(f"Agent Response: {result.messages[-1].content}")

    # Show that the tool itself still works independently
    print(reverse_string('Hello, how are you Doing?'))

# ---------------------------
# Script Entrypoint
# ---------------------------

if __name__ == "__main__":
    # asyncio.run() ensures the async agent.run() is executed properly
    asyncio.run(main())

```

### 👉 Key part explained inside comments:

- run() is stateful → keeps track of the flow of messages, tool calls, etc.

- But termination conditions reset automatically after each run → so if the last run had “stop after 2 tool calls,” the next run starts fresh with no stop condition carried over.
