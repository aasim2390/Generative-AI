import json
from pathlib import Path
from openai import OpenAI
from utils.config import USER_THREAD_FILE
from utils.config import OPENAI_API_KEY

client =  OpenAI(api_key=OPENAI_API_KEY)
THREAD_FILE = Path(USER_THREAD_FILE)

def load_threads():
    if THREAD_FILE.exists():
        with open(THREAD_FILE, "r") as f:
            return json.load(f)
    return {}

def save_threads(thread_dict):
    with open(THREAD_FILE, "w") as f:
        json.dump(thread_dict, f, indent=2)

def get_or_create_thread(email):
    threads = load_threads()
    if email in threads:
        return threads[email]
    else:
        thread = client.beta.threads.create()
        threads[email] = thread.id
        save_threads(threads)
        return thread.id
