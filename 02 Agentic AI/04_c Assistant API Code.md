# OpenAI Assistants API – Simple Explanation

In November 2023, OpenAI introduced the **Assistants API**.  
Think of it as a way to create **smart AI helpers** that can do specific jobs for you.  

These helpers can:  
- Follow **special instructions**.  
- Use **extra knowledge** to help you.  
- Run **tools** like a code calculator or file search.  

It’s like a **supercharged version** of the regular OpenAI API, designed to handle more complex tasks automatically.  
This is also the technology behind **custom GPTs**.

---

## Two Main Parts

### 1. The Assistant
- Your **AI helper**.  
- Has a **unique ID**.  
- Connected to an **OpenAI language model**.  
- Can use tools like:  
  - **Code Interpreter** – runs Python code for math, data analysis, or charts.  
  - **File Search** – looks through files you provide.  
  - **Custom functions** – special tasks you program it to do.  

### 2. The Thread
- This is where you **chat with the Assistant**.  
- Every message you send is **saved in the thread**.  
- The AI uses all messages to give **smarter answers**.  
- While the AI itself doesn’t remember things forever, the thread acts like a **short-term memory**.

---

## How It Works
1. You ask the Assistant something (e.g., “How much return is needed to double an investment?”).  
2. The Assistant decides **which tools to use** and calculates the answer.  
3. You get the **answer back**.  
4. This process can repeat until your question or task is fully solved.

---

## Cost
- **Code Interpreter:** $0.03 per session.  
- **File Search:** $0.10 per GB stored per day (**first 1 GB is free**).  
- **Model usage:** You pay for the AI processing itself.

---

# OpenAI Assistants Playground – Notes

---

## 1. What is the Playground?
- A **low-code environment** to experiment with the Assistants API.  
- Allows you to **create, configure, and test custom AI assistants**.  
- **URL:** [https://platform.openai.com/assistants](https://platform.openai.com/assistants)

---

## 2. Playground Interface
- **Left Panel:** Lists all Assistants you’ve created.  
- **Right Panel:** Shows details for the selected Assistant.  
- **Top Right:** Options to **Create, Clone, or Delete** an Assistant.

---

## 3. Creating a New Assistant
- **Name:** Give your Assistant any name.  

- **Instructions:**  
  - Like the **system message** for the LLM.  
  - Defines the **persona, role, or behavior** of the Assistant.

- **Model Selection:**  
  - Default = most advanced model.  
  - Can pick others from a **drop-down menu**.

- **Tools (optional):**  
  - **File Search** – allow Assistant to search and use uploaded files.  
  - **Code Interpreter** – enable running code (e.g., Python).  
  - **Functions** – define custom callable functions.

- **Model Configuration:**  
  - **Temperature (0–2):** Lower = deterministic, Higher = creative.  
  - **Top P:** Selects the most probable tokens until cumulative probability reaches P.  
  - **Output in JSON:** Enable for structured responses.  
  - **API version:** Usually default (latest) is fine.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/567912f5-bf37-4bf3-a7ee-4e464747b72d" />

---

## 4. Using the Playground
- Click **Playground** (top right) after creating/configuring your Assistant.  

- **Left Panel:** Configuration options.  
- **Middle Panel:** Conversation thread with messages.  
- **Input Box:** Type your message to the Assistant.  
- **Add Files/Images:** Optional uploads to enhance context.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/7d68bc6e-78c8-4254-b4b0-c689ee5672f8" />


**Example Message:**

```vbnet
Assume the average return on my investments is 5% and I make $5,000 contributions each year. How long will it take to reach $100,000?
```

**Assistant** uses Code Interpreter to run a Python program.

**Result:** 14 years to reach $100,000.

## 5. Additional Features

- **Logs (Right Side):**  
  - Shows Assistant actions and execution.  
  - Helpful for debugging.

- **Token Count:**  
  - Top right of the thread – shows the number of tokens used.

- **Thread Management:**  
  - Clear thread history.  
  - View list of files being used.

---

## ✅ Summary

- **Playground** = low-code AI testing environment.  
- You can **create Assistants, give instructions, select models, add tools, and test queries**.  
- Useful for **debugging, experimentation, and generating structured outputs**.

---

# OpenAI Assistants API – code

---

## 1. Setup
Import the OpenAI class and create a client instance:

```python
from openai import OpenAI
client = OpenAI()
```

## 2. Creating an Assistant
Use `client.beta.assistants.create()` to create a new Assistant.

**Parameters:**
- `name`: Name of your Assistant (any string, e.g., `"Investing Bot"`).  
- `instructions`: System message describing the Assistant’s role.  
- `tools`: Tools the Assistant can use (e.g., Code Interpreter).  
- `model`: The model to use (e.g., `"gpt-4o-mini"`).  

```python
assistant = client.beta.assistants.create(
    name="Investing Bot",
    instructions="You are an expert in calculating investments.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini",
)
```

## 3. Creating a Conversation Thread

Create a new thread for messages:

```python
thread = client.beta.threads.create()
```
Add a message from the user:

```python
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="You have $10,000 to invest. You want to double your money in 20 years. What average return will you need to get?"
)

```
## 4. Running the Assistant

Execute the Assistant on the thread with additional instructions:

```python
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Provide detailed analysis."
)
```
**Parameters:**
- `thread_id`: Identifies the conversation thread.
- `assistant_id`: Specifies which Assistant to use.
- `instructions`: Extra instructions for this run.


## 5. Checking Run Status

Use a while loop to wait until the Assistant completes:

```python
import time

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print(run.status)
    time.sleep(5)
```

> The loop repeatedly checks the status every 5 seconds until completed.

## 6. Retrieving Messages

Get all messages in the thread:

```python
messages = client.beta.threads.messages.list(thread_id=thread.id)
```
Print messages in order from oldest to newest:
```python
for thread_message in messages.data[::-1]:
    print(thread_message.content[0].text.value)
    print('\n')

```
`[::-1]` reverses the list so that messages are printed oldest first.

## 7. Extracting Rate of Return

Function to extract percentage values from the Assistant’s response:

```python
def extract_rate_of_return(response):
    import re
    match = re.search(r'(\d+(\.\d+)?%)', response)
    if match:
        return match.group(1)
    return None
```

Extract and print the rate of return:

```python
for thread_message in messages.data[::-1]:
    if thread_message.role == "assistant":
        rate_of_return = extract_rate_of_return(thread_message.content[0].text.value)
        if rate_of_return:
            print(f"The average rate of return will need to be at least {rate_of_return}.")
        else:
            print("Could not extract the rate of return from the response.")
        break
```

## 8. Managing Multiple Assistants

List existing Assistants (limit 20, descending order):

```python
my_assistants = client.beta.assistants.list(order="desc", limit=20)
print(my_assistants.data)
```

Delete an Assistant by ID:

```python
response = client.beta.assistants.delete(my_assistants.data[0].id)
print(response)
```

## Summary
- **Assistant**: Encapsulates AI behavior with instructions, tools, and a model.
- **Thread**: Holds the conversation context.
- **Run**: Executes the Assistant on a thread with optional extra instructions.
- **Messages**: Retrieved and processed for user or Assistant responses.
- **Utility**: Extract information (e.g., rate of return) from Assistant responses.

---

<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/c58c1d89-fedf-47ef-a870-af263d52c358" />

---
# OpenAI Assistants API – Q&A Notes

---

### Q1: What does the code do?

**A:**
- Creates an Assistant (Investing Bot) with specific instructions and tools.  
- Starts a conversation thread and sends a user message (e.g., investment question).  
- Runs the Assistant on the thread to generate a response.  
- Checks the run status until the Assistant finishes processing.  
- Retrieves messages from the thread and extracts information (e.g., rate of return).  
- Optionally lists, manages, or deletes Assistants.

---

### Q2: Is memory persistent?

**A:**
- By default, the Assistant remembers the context of a single thread.  
- Persistent memory across sessions is optional.  
- The memory size is limited by the model’s token limits (a few thousand tokens per thread).

---

### Q3: What happens if I delete the Assistant?

**A:**
- The Assistant is deleted.  
- All associated memory and threads linked to it are also removed.  
- Any past conversations or context cannot be recovered.

---

### Q4: How are responses retrieved and processed?

**A:**
- Messages are retrieved using `client.beta.threads.messages.list()`.  
- You can process them in order or reverse order and extract data using functions (e.g., `extract_rate_of_return`).

---

### Q5: How can multiple Assistants be managed?

**A:**
- List Assistants:
  
```python
client.beta.assistants.list(order="desc", limit=20)
```
- Delete an Assistant:
  
```python
client.beta.assistants.delete(assistant_id)
```

### Q6 : How communication between multiple Assistants works
**A:**
  1. **Separate Assistants:** Each Assistant has its own instructions, tools, and memory. By default, they do not share context.
  2. **Manual passing of messages:** To `communicate` between Assistants, you retrieve the response from one Assistant and then send it as a user message to another Assistant’s thread.

     Example: Send Assistant A message to Assistant B

```python
    message_from_A = "Response from Assistant A"
    message_to_B = client.beta.threads.messages.create(
    thread_id=thread_B.id,
    role="user",
    content=message_from_A)
```
    
  4. **Thread context:** Each Assistant maintains context only within its thread, so you must manually feed messages from one thread to another if you want the second Assistant to “know” the first Assistant’s output.
  5. **Use cases:** This is useful for multi-step workflows, delegation of tasks, or chaining Assistants with specialized roles.

     <img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/3b64290b-3809-4ff8-9329-0bba9acb181c" />
