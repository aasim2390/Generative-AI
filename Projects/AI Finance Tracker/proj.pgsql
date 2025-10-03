finance_tracker/
│
├─ main.py                # Streamlit app entry point
├─ db/
│   └─ db_manager.py      # MSSQL connection & CRUD functions
├─ assistant/
│   ├─ thread_manager.py  # Manage threads per user
│   └─ functions.py       # Functions callable by OpenAI assistant
├─ utils/
│   └─ config.py          # Config variables (DB credentials, API keys)
├─ data/
│   └─ user_threads.json  # Store email → thread_id mapping
└─ requirements.txt
