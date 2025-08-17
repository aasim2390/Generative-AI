
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
```

```python
from autogen_ext.models.openai import OpenAIChatCompletionClient

openai_model_client = OpenAIChatCompletionClient(
    model="gpt-4o-2024-08-06",
    # api_key="sk-...", # Optional if you have an OPENAI_API_KEY environment variable set.
)

```
