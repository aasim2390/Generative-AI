
## Models in Autogen

- Agents often need access to LLM model services (e.g., OpenAI, Azure OpenAI, or local models).
- Different providers use different APIs, making direct integration harder.
- autogen-core defines a protocol for model clients (a standard way to communicate with any model service).
- autogen-ext provides ready-made model clients for popular services (like OpenAI, Azure, etc.).
- AgentChat uses these model clients to interact seamlessly with model services.



<img width="550" height="450" alt="image" src="https://github.com/user-attachments/assets/5ce41c3a-ab43-42b3-932f-000cecfb73a7" />

_source - https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html

### OpenAI

```bash
pip install "autogen-ext[openai]"
pip install "autogen-agentchat"
```

```python
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_agentchat.agents import AssistantAgent


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

openai_model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)

# UserMessage
response = await openai_model_client.create([UserMessage(content="Who are you?", source="user")])
print(response.content)

#AssistantAgent
agent = AssistantAgent(
    name='assistant',
    model_client=openai_model_client,
    system_message='You are a helpful assistant',
)
result = await agent.run(task='Capital of France?')
print(result.messages[-1].content)

```
