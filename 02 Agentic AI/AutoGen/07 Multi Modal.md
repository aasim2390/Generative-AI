## Multi Modal Input & Structured Output

We can imaging messages as the way agent communicate - text our Friend.

When we communicate with the agents -----> sending a message when it responds ---> it too sends a message
- TextMessage
- ImageMessage
- ToolMessage
- and many more  (source- https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/messages.html)

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/64679547-d200-4197-8383-c9924596eb9a" />


### Code Example

**Install Libraries**
```bash
!pip install "autogen-agentchat"
!pip install "autogen-ext[openai]"
```
**Set API Key**

```python
import os
from google.colab import userdata

OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```

**Imports**
```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage,MultiModalMessage
from autogen_core import Image as AGImage

from PIL import Image
from io import BytesIO
import requests
import os
```

**Model Client Or Brain**

```python
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)
```

**AssistantAgent**
```python
agent = AssistantAgent(
    name = "text_agent",
    model_client=model_client,
    system_message='You are a helpful assistant. answer question accurately'
)
```


**Simplest type of message - TextMessage**

```python
async def test_text_messages():
    text_msg = TextMessage(content = 'What is the capital of USA?', source='user')
    result = await agent.run(task=text_msg)
    print(result.messages[-1].content)

await test_text_messages()
```
```bash
The capital of the United States is Washington, D.C.
```

**Multi Modal Message**

```python
async def test_multi_modal():

    response = requests.get('https://picsum.photos/id/15/200/300') # 23 for the image of folks
    pil_image = Image.open(BytesIO(response.content))
    ag_image = AGImage(pil_image)

    multi_modal_msg = MultiModalMessage(
        content = ['What is in the image?',ag_image],
        source='user'
    )

    result = await agent.run(task=multi_modal_msg)
    print(result.messages[-1].content)


await test_multi_modal()
```

```bash
The image shows a waterfall cascading down between rocky cliffs, surrounded by greenery. There are rocks and a small stream in the foreground.
```

### Structured Output

**Import**
```python
from pydantic import BaseModel
```

**Creating Output Template**

```python
class PlanetInfo(BaseModel):
    name: str
    color: str
    distance_miles: int
```

**Telling Model Client to generate ask output**

```python
model_client = OpenAIChatCompletionClient(
    model = 'gpt-4o',
    api_key=api_key,
    response_format=PlanetInfo #Output should be this format
    )
```

**Assistant Agent**
```python
agent = AssistantAgent(
    name='planet_agent',
    model_client=model_client,
    system_message="You are a helpful assistant that provides information about planets. in the structure JSON"
)
```

**Output**

```python
async def test_structured_output():
    task = TextMessage(content = "Please provide information about Mars.",source='User')
    result = await agent.run(task=task)
    structured_response = result.messages[-1].content
    print(structured_response)

resultJson = await test_structured_output()
```

```bash
{"name":"Mars","color":"Red","distance_miles":141600000}
```
