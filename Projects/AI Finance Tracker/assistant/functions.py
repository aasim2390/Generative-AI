from db.db_manager import add_expense, get_expense_summary, get_weekly_expense
from assistant.thread_manager import client,get_or_create_thread
import time

def add_expense_fn(params):
    # 1. Add to DB
    add_expense(
        email=params["email"],
        category=params["category"],
        amount=params["amount"],
        expense_date=params["date"],
        thread_id = params["thread_id"]
    )

    # 2. Add message to thread
    thread_id = get_or_create_thread(params["email"])
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=f"Added an expense: {params['category']} - ₹{params['amount']} on {params['date']}"
    )

    # ✅ Return success response
    return {
        "message": f"Expense of ₹{params['amount']} for {params['category']} added successfully!"
    }




def get_summary_fn(params):

    db_response = get_expense_summary(email=params["email"])

    prompt = f""" Based on user query, conversation history and the database response generate the summary of the financial expense of the user.
    <user query>
    {params["user_message"]}
    </user query>

    <database response>
    {db_response}
    </database response>
    """
    
    # Add user message
    client.beta.threads.messages.create(
    thread_id=params["thread_id"],
    role="user",
    content=prompt
      
    )

    # Run assistant
    run = client.beta.threads.runs.create(
    thread_id=params["thread_id"],
    assistant_id=params["ASSISTANT_ID"]
    )

    # --- Wait until run completes ---
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=params["thread_id"],
            run_id=run.id
        )
        print("Current status:", run_status.status)

        if run_status.status == "completed":
            break
        elif run_status.status == "requires_action":
            # Extract tool calls
            tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
            outputs = []

            for tool_call in tool_calls:
                if tool_call.function.name == "get_expense_summary":
                    result = get_expense_summary(email=params["email"])
                    outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": str(result)
                    })
            # Submit results back to the run
            client.beta.threads.runs.submit_tool_outputs(
            thread_id=params["thread_id"],
            run_id=run.id,
            tool_outputs=outputs
            )

        elif run_status.status in ["failed", "expired", "cancelled"]:
            raise Exception(f"Run failed with status {run_status.status}")
        time.sleep(5)
        
        
    # --- Now fetch assistant reply ---
    response = client.beta.threads.messages.list(thread_id=params["thread_id"])

    print("response is \n", response)

    for msg in response.data:
        if msg.role == "assistant":
            assistant_reply = msg.content[0].text.value
            print("Assistant:", assistant_reply)
            return assistant_reply

    return "No assistant reply found."

def get_weekly_stats_fn(params):
    return get_weekly_expense(email=params["email"])
