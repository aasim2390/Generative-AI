# ConversableAgent

## 📌 What it is
**ConversableAgent** is a specialized AI agent in **AutoGen** designed to handle **natural-language conversations**.  
It can act as:
- A **friendly assistant**  
- A **curious learner**  
- Or any role you define  

👉 Useful for **chatbots, virtual assistants, or two-agent dialogues.**

---

## 💡 How it works
1. **Define roles** → Each agent gets a persona (system message).  
2. **Set goals** → Assistant helps, learner asks, critic verifies, etc.  
3. **Orchestrate dialogue** → Agents talk to each other in a structured conversation.  
4. **Inspect results** → Capture chat logs for analysis or further automation.  

---

## 🛠️ Clean, Ready-to-Run Example

### Installation
```bash
pip install --upgrade pyautogen
```

### Python Code
```python
from autogen import ConversableAgent

# LLM configuration
llm_config = {"model": "gpt-4o-mini"}

# Define the two agents
alice = ConversableAgent(
    name="alice",
    system_message="Your name is Alice, and you are a friendly AI assistant ready to help with any questions.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

bob = ConversableAgent(
    name="bob",
    system_message="Your name is Bob, and you are a curious learner who loves asking questions.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Start the conversation: Bob asks Alice about photosynthesis
chat_result = bob.initiate_chat(
    recipient=alice,
    message="Hi Alice! Can you tell me how photosynthesis works?",
    max_turns=2,  # controls how many back-and-forth turns happen
)

print(chat_result)
```

## 📝 Notes & Quick Tips

`max_turns` → Defines how many conversational turns before stopping.
- In this example:
    - **Bob asks** → “Hi Alice! …”
    - **Alice replies** → Explanation of photosynthesis
- `chat_result` → Stores the full conversation. You can print, log, or analyze it.
- **Extend further** → Add:
    - Memory → Keep context across sessions
    - Tools → Give agents external capabilities (e.g., web search, APIs)
    - More agents → Simulate debates, Q&A panels, or workflow collaboration
 
## 🎯 Takeaway

ConversableAgent makes it easy to build talking agents that:
- Stay in **role**
- Manage **autonomous conversations**
- Form the building blocks for multi-agent systems in **AutoGen**

## 🧠 Mental Model

Think of ConversableAgent like a role-playing chatbot:
- Each agent has a **persona** (system prompt).
- You decide **who talks first**.
- They carry out a **mini-drama** of Q&A or task solving.
