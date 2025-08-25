## 🔑 DataExtract – Key Data Extraction Tool

A **Streamlit + LangChain** project for extracting structured data (e.g., product reviews → product name, rating, features, summary) from unstructured text.
Built with **PydanticOutputParser** for reliable, type-safe extraction and includes an **LLM-as-a-Judge** evaluation step to score extraction quality.

---

### 🚀 Features
- 📝 Paste custom text or use sample inputs
- 📊 Extracts structured data using LangChain + Pydantic
- ⚖️ Evaluation step (LLM-as-Judge)
- 📥 Download results as JSON
- 🎯 Modular codebase (chains, schemas, utils, config)

---

### 📂 Project Structure

```bash
dataextract/
│── app.py                 # Main Streamlit app
│── requirements.txt
│── README.md
│
├── config/
│   └── settings.py         # API keys, model settings
│
├── chains/
│   ├── extractor.py        # Extraction chain
│   └── evaluator.py        # Evaluation chain (LLM-as-Judge)
│
├── schemas/
│   └── product_schema.py   # Pydantic schema
│
├── utils/
│   ├── helpers.py          # Helpers (JSON, etc.)
│
└── examples/
    └── sample_inputs.py    # Example texts

```

---

### ⚙️ Setup & Installation

#### 1. Clone the repo

```bash
git clone https://github.com/your-username/dataextract.git
cd dataextract

```

#### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

```

#### 3. Install dependencies

```bash
pip install -r requirements.txt

```

#### 4. Configure API key

```ini
OPENAI_API_KEY=your_openai_api_key

```

### ▶️ Run the App

```bash
streamlit run app.py

```

---

#### Output

<img width="800" height="750" alt="image" src="https://github.com/user-attachments/assets/ccbd3b20-0e4a-47bd-9611-0f3dfd5c24d3" />

---




