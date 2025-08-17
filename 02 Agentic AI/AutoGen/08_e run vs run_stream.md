## 1. run()

**Purpose:** Executes the agent for a task and returns the full result at the end.

**Behavior:**
- Agent processes the task completely.
- Returns a result object containing all messages after finishing.

**Use case:** When you only need the final output and don’t care about intermediate responses.

**Example:**

```python
result = await agent.run("Explain why the sky is blue.")
print(result.messages[-1].content)  # Final message only

```

## 2. run_stream()

**Purpose:** Executes the agent and streams messages as they are generated.

**Behavior:**
- You can iterate over messages while the agent is still thinking.
- Useful for real-time output or progress updates.

**Use case:** When you want to see the agent’s output gradually or handle messages as they arrive.

**Example:**
```python
async for msg in agent.run_stream("Explain why the sky is blue."):
    print(msg)  # Prints messages one by one as they arrive

```

| Feature     | `run()`                      | `run_stream()`                  |
| ----------- | ---------------------------- | ------------------------------- |
| Output      | Full result after completion | Messages as they are generated  |
| Use case    | Final answer only            | Real-time / progressive output  |
| Performance | Waits until agent finishes   | Can handle messages immediately |
| Iteration   | No                           | Yes (async for)                 |

## ✅ Summary

- `run()` → simple, gets the final response.
- `run_stream()` → advanced, shows output progressively.
