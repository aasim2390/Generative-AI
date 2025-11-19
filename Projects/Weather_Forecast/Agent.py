from openai import OpenAI
from dotenv import load_dotenv
import requests
import json

# -----------------------------
# TOOL: Weather fetcher
# -----------------------------
def get_weather(city):
    print(f"[DEBUG] Running get_weather() for: {city}")

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    print(f"[DEBUG] HTTP Status {city}: {response.status_code}")

    if response.status_code != 200:
        print(f"[DEBUG] ERROR fetching weather for {city}")
        return {"error": "Something went wrong"}

    print(f"[DEBUG] Weather fetched successfully for {city}")

    data = response.json()

    return data.get("current_condition", [{}])[0]



# -----------------------------
# SYSTEM PROMPT
# -----------------------------
weather_prompt = """
You are a weather assistant that uses the tool get_weather(city: str) to fetch weather.

The steps Plan → Tool → Observe → Output must remain internal.

Rules:
1. If the user asks for a single city → call get_weather.
2. If the user asks for multiple cities:
   - Identify all cities.
   - Call get_weather separately for each one.
   - After all tool results, generate a final combined summary.
3. After tool calls:
   - Parse JSON weather data.
   - Produce clear, readable, friendly weather summaries.
4. Do NOT show your reasoning or process.
"""


# -----------------------------
# SETUP
# -----------------------------
load_dotenv()
client = OpenAI()


# -----------------------------
# MAIN LOGIC
# -----------------------------
def main():
    while True:
        user_query = input("\n> ")

        # stop command
        if user_query.lower() in ["exit", "quit", "bye", "stop"]:
            print("BOB: Goodbye!")
            break

        print("\n[DEBUG] Sending initial request to GPT...")
        print("[DEBUG] User query:", user_query)

        # -----------------------------
        # FIRST CALL TO GPT (to get tool calls)
        # -----------------------------
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": weather_prompt},
                {"role": "user", "content": user_query}
            ],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_weather",
                        "description": "Retrieve live weather using wttr.in",
                        "parameters": {
                            "type": "object",
                            "properties": {"city": {"type": "string"}},
                            "required": ["city"]
                        }
                    }
                }
            ]
        )

        msg = response.choices[0].message

        print("[DEBUG] GPT initial response:")
        print(json.dumps(msg.model_dump(), indent=2))

        # DOES GPT WANT TO CALL TOOLS?
        if msg.tool_calls:
            print(f"[DEBUG] GPT requested {len(msg.tool_calls)} tool call(s)")

            tool_results_messages = []

            # -----------------------------
            # EXECUTE TOOL CALLS
            # -----------------------------
            for tool_call in msg.tool_calls:

                print("\n[DEBUG] Tool call received:")
                print(json.dumps(tool_call.model_dump(), indent=2))

                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                if tool_name == "get_weather":
                    city = tool_args["city"]
                    print(f"[DEBUG] Calling get_weather('{city}')")

                    result = get_weather(city)

                    print(f"[DEBUG] Tool output for {city} (first 200 chars):")
                    print(result, "...\n")

                    tool_results_messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result)
                    })

            # -----------------------------
            # SECOND CALL TO GPT (FINAL ANSWER)
            # prevent infinite loop with tool_choice="none"
            # -----------------------------
            print("[DEBUG] Sending tool results back to GPT (final response)...")
            print("Messages : \n",tool_results_messages)

            final_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": weather_prompt},
                    {"role": "user", "content": user_query},
                    msg,
                    *tool_results_messages
                ]
            )

            print("[DEBUG] Final GPT response received")

            print("\nBOB:", final_response.choices[0].message.content)

        else:
            # Model gave final answer with no tools needed
            print("[DEBUG] GPT produced direct answer (no tools used)")
            print("\nBOB:", msg.content)


# Run interactively
main()

#get_weather("goa")
