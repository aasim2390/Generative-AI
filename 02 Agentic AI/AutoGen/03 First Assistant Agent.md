## AgentChat API with first AssistantAgent

### Install libraries

```bash
!pip install "autogen-agentchat"
!pip install "autogen-ext"
!pip install "autogen-core"
!pip install "autogen-ext"
!pip install autogen-ext['openai']
!pip install "asyncio
```

### Import libraries

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
```

### Get OpenAI Keys

```python
from google.colab import userdata
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```

### Model Client

```python
model_client = OpenAIChatCompletionClient(model='gpt-4o-mini',api_key=OPENAI_API_KEY)
```

### Assistant Agent - Versatile agent for conversations

```python
assistant = AssistantAgent(name="assistant", model_client=model_client,description="Basic assistant agent")
```

### Running Agent

```python
result =  await assistant.run(task = "What is capital of Japan?")
print(result)
```
