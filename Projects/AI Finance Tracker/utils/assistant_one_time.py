from openai import OpenAI
from config import OPENAI_API_KEY

client =  OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.create(
    name="Finance Tracker Assistant",
    instructions="You are a helpful finance assistant. Use the available functions to manage expenses and generate reports.",
    model="gpt-4o-mini",
    tools=[
        {"type": "function", "function": {
            "name": "add_expense_fn",
            "description": "Add an expense for the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "category": {"type": "string"},
                    "amount": {"type": "number"},
                    "expense_date": {"type": "string", "format": "date"},
                    "thread_id": {"type": "string"},
                },
                "required": ["email", "category", "amount", "date"]
            }
        }},
        {"type": "function", "function": {
            "name": "get_summary_fn",
            "description": "Get expense summary for the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "thread_id": {"type": "string"},
                    "user_message": {"type": "string"},
                    "assistant_id": {"type": "string"}
                },
                "required": ["thread_id","assistant_id","email"]
            }
        }},
        {"type": "function", "function": {
            "name": "get_weekly_stats_fn",
            "description": "Get weekly expense stats for the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"}
                },
                "required": ["email"]
            }
        }}
    ]
)

print("Your assistant_id is:", assistant.id)
