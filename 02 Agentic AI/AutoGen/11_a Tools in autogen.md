# Tools in AutoGen

## What are Tools?
- Tools are **code snippets or functions** that an agent can execute.  
- They give agents the ability to **act beyond plain text**.  

## Examples of Tools
- A **simple tool**: a calculator function.  
- A **complex tool**: an API call to check stock prices or weather.  

## Why Tools Matter
- By default, an AI model can only generate text.  
- With tools, the model can **take actions**, such as running calculations or retrieving real-time data.  

## AutoGen and Tools
- AutoGen provides the `autogen_core.tools` module.  
- This module includes:
  - **Built-in tools** (ready-made, plug-and-play).  
  - **Utilities to create custom tools** (build your own functions).  

## How Tools Work
- When an agent decides it needs extra help,  
  it can **call a tool** in response to a model-generated function call.  
- This allows agents to:
  - Extend their reasoning with external actions.  
  - Connect with third-party services.  
  - Perform operations they cannot do with text alone.  


<img width="600" height="440" alt="image" src="https://github.com/user-attachments/assets/3dc0c18b-37d9-4c95-8728-cac265cf5721" />


source: https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html
