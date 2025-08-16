## CrewAI Invoice Executor

This project demonstrates a powerful and scalable solution for automated invoice data extraction using a multi-agent system powered by CrewAI. 
It leverages a combination of optical character recognition (OCR) and large language models (LLMs) to accurately parse and extract key information from unstructured invoice documents.

## Key Features
- **Automated Data Extraction:** Automatically identifies and extracts crucial data points like invoice number, total amount, due date, and line items.
- **Scalable Architecture:** Built on the CrewAI framework, the system uses a team of specialized AI agents working together, making it easy to add more agents or tasks.
- **OCR Integration:** Uses PyTesseract for robust text recognition from images.
- **Flexible Parsing:** Utilizes Unstructured and LangChain to handle a wide variety of document formats.

## Technologies Used
- **CrewAI:** The orchestration framework for the multi-agent system.
- **LangChain:** For building powerful LLM-powered applications.
- **Unstructured:** For parsing and cleaning data from diverse document types.
- **PyTesseract:** A Python wrapper for Google's Tesseract-OCR Engine.
- **Tesseract OCR:** The open-source OCR engine.
- **Python:** The core programming language.

## Prerequisites
Before running the project, you need to install the Tesseract OCR engine and the required Python libraries.

```python
!pip install pytesseract -q
!sudo apt update
!sudo apt install tesseract-ocr
```

```bash
!pip install langchain-community --upgrade
!pip install unstructured --upgrade
!pip install crewai --upgrade
!pip install crewai-tools --upgrade

```

## Project Code
Here is the complete Python code for the invoice extraction system.

```python
# ----------------------
# PDF Extraction Function
# ----------------------
import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF

def extractor(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = []

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text()
        if not text.strip():
            # Convert page to image and run OCR
            pix = page.get_pixmap()
            img_bytes = pix.tobytes(output="png")  # get PNG bytes
            img = Image.open(io.BytesIO(img_bytes))
            ocr_text = pytesseract.image_to_string(img)
            full_text.append(ocr_text)
        else:
            full_text.append(text)

    doc.close()
    return "\n".join(full_text)

# Example usage:
# text = extract_text_from_pdf("sample.pdf")
# print(text)

from crewai.tools import BaseTool

# Create a tool class for your extractor function
class ExtractorTool(BaseTool):
    name: str = "Invoice OCR Extractor"
    description: str = "A tool to extract all text content from an invoice PDF using advanced OCR methods."
    
    def _run(self, invoice_path: str) -> str:
        """
        The method that will be executed by the agent.
        It calls the custom extractor function.
        """
        return extractor(invoice_path)

# Instantiate the custom tool
ocr_extractor_tool = ExtractorTool()

from crewai import Agent, Task, Crew, Process

# Define Agents
ocr_agent = Agent(
    role="OCR Specialist",
    goal="Extract all text content from an invoice PDF using advanced OCR methods.",
    backstory=(
        "You are an OCR expert. Your job is to meticulously scan the entire invoice PDF "
        "and convert all text, including tables and figures, into a raw text format. "
        "You are the first step in the data pipeline."
    ),
    tools=[ocr_extractor_tool], # Pass the function directly as a tool
    verbose=True,
    model="gpt-4o-mini"
)

'''llm_extraction_agent = Agent(
    role="LLM-based Data Extractor",
    goal="Extract specific data points from raw invoice text.",
    backstory=(
        "You are a highly skilled data extractor powered by a Large Language Model. "
        "You receive raw text from the OCR agent and your mission is to identify and "
        "extract key information like invoice number, date, total amount, and vendor "
        "details. You must be accurate and fast."
    ),
    #tools=[search_tool], # Uncomment and define search_tool if needed
    verbose=True,
    model="gpt-4o-mini"
)'''

llm_extraction_agent = Agent(
    role="LLM-based Data Extractor",
    goal="Accurately extract specific data points from raw invoice text.",
    backstory=(
       "You are a highly skilled and precise data extractor. Your mission is to "
    "identify and extract all key information for a structured JSON output. "
    "This includes the **invoice number**, **date**, **total amount**, **vendor details**, "
    "and **line items** or **description**. "
    "You must only extract values that are clearly labeled. "
    "For example, only extract an **invoice number** if the text explicitly "
    "says 'Invoice Number', 'Invoice #', or 'Invoice ID'. "
    "Similarly, only extract a **date** if it's labeled as 'Date', 'Invoice Date', or 'Due Date'. "
    "**Crucially, you must ignore any field labeled as 'Reference Number'** "
    "or similar, as this is not an invoice number."
),
    #tools=[search_tool], # Uncomment and define search_tool if needed
    verbose=True,
    model="gpt-4o-mini"
)

validation_agent = Agent(
    role="Data Validator",
    goal="Ensure the extracted data is accurate and complete.",
    backstory=(
        "You are a meticulous validator. Your task is to check the data extracted by the "
        "LLM against a set of predefined rules. If any data is missing or improperly "
        "formatted, you flag it for a retry."
    ),
    verbose=True,
    model="gpt-4o-mini"
)

json_builder_agent = Agent(
    role="JSON Formatter",
    goal="Transform validated data into a structured JSON format.",
    backstory=(
        "You are the final formatter. Your mission is to take the clean, validated data "
        "and build a perfect JSON object, ready for downstream systems."
    ),
    verbose=True,
    model="gpt-4o-mini"
)
# Define Tasks
task_ocr = Task(
    description=(
        "Use the extractor to read the invoice PDF located at '{pdf_path}' and extract "
        "all text content. Provide the raw text output to the next agent."
    ),
    expected_output="The complete, raw text content of the invoice, including all text from the PDF.",
    agent=ocr_agent
)

task_extract = Task(
    description=(
        "From the raw text, extract key fields. For 'invoice number', "
        "look for labels like 'invoice', 'invoice_number', or 'inv#'. "
        "For 'date', look for labels like 'date', 'invoice date', or 'due date'."
        "**DO NOT** extract any 'reference number' as an invoice number."
    ),
    expected_output="A JSON object containing the extracted fields.",
    agent=llm_extraction_agent
)

task_validate = Task(
    description=(
        "Validate the JSON output from the data extraction agent. "
        "Ensure the 'invoice number' and 'date' fields are present. "
        "If either is missing, flag the data as invalid. Do not validate 'reference number' as an invoice."
    ),
    expected_output="A JSON object with a 'status' key (valid or invalid) and the validated data.",
    agent=validation_agent
)

'''task_build_json = Task(
    description=(
        "Take the validated and corrected data from the previous steps and convert it into "
        "a final, clean JSON object. The JSON should only contain the extracted fields."
    ),
    expected_output="A valid JSON object containing the extracted invoice data.",
    agent=json_builder_agent
)'''

task_build_json = Task(
    description=(
        "Take the validated data from the previous step. "
        "If the input data's 'status' is 'invalid', your final output must be a JSON object "
        "like this: `{\"error\": \"Invalid input format. Missing required fields.\"}`. "
        "If the data is valid, convert it into a final, clean JSON object. "
        "The final JSON should only contain the extracted fields and no 'status' key."
    ),
    expected_output="A valid JSON object containing either the extracted invoice data or an error message.",
    agent=json_builder_agent
)

# ----------------------
# Crew Setup 
# ----------------------

invoice_processing_crew = Crew(
    agents=[
        ocr_agent,
        llm_extraction_agent,
        validation_agent,
        json_builder_agent
    ],
    tasks=[
        task_ocr,
        task_extract,
        task_validate,
        task_build_json
    ],
    process=Process.sequential,
    verbose=True
)
# The code execution block
# This is where the process is initiated and the PDF path is passed.
def run_crew(pdf_path):
    print("Running the invoice processing crew...")
    result = invoice_processing_crew.kickoff(inputs={'pdf_path': pdf_path})
    print("\n✅ Final Output:")
    print(result)
```

## How to Run
- Clone this repository.
- Install the prerequisites as described above.
- Replace the placeholder for OPENAI_API_KEY with your actual API key.
- Place your invoice file (e.g., invoice.pdf) in a location and update the invoice_file_path variable in the script.
- Run the script from your terminal:

  ```python
  run_crew(pdf_path)
  ```

  ## Example Output
After running the script, the console output will show the extracted and validated invoice data in a structured JSON format.

1) Valid Case
```json
{
  "invoice_number": "BPXINV-00550",
  "date": "23.05.2021",
  "total_amount": 6610.95,
  "vendor_details": {
    "name": "Bioplex",
    "address": "5 Rue Bader, Narbonne, Aude, 11100",
    "phone": "+33 140 260294"
  },
  "line_items": [
    {
      "quantity": 10,
      "description": "Dextromethorphan polistirex",
      "unit_price": 12.45,
      "total": 124.50
    },
    {
      "quantity": 25,
      "description": "Venlafaxine Hydrochloride",
      "unit_price": 16.00,
      "total": 400.00
    },
    {
      "quantity": 25,
      "description": "Metoclopramide Hydrochloride (BPXPO-00537)",
      "unit_price": 9.99,
      "total": 249.75
    },
    {
      "quantity": 10,
      "description": "Avobenzone, octinoxate (BPXPO-00538)",
      "unit_price": 4.45,
      "total": 44.50
    },
    {
      "quantity": 10,
      "description": "Verapamil hydrochloride",
      "unit_price": 7.89,
      "total": 78.90
    },
    {
      "quantity": 15,
      "description": "Tiagabine hydrochloride",
      "unit_price": 10.25,
      "total": 153.75
    },
    {
      "quantity": 10,
      "description": "Ziprasidone hydrochloride (BPXPO-00537)",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 10,
      "description": "Risperidone",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 10,
      "description": "Metoprolol succinate",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 10,
      "description": "Acetaminophen",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 15,
      "description": "Sorafenib",
      "unit_price": 16.00,
      "total": 240.00
    },
    {
      "quantity": 15,
      "description": "Telmisartan",
      "unit_price": 9.99,
      "total": 149.85
    },
    {
      "quantity": 15,
      "description": "Famotidine",
      "unit_price": 4.45,
      "total": 66.75
    },
    {
      "quantity": 15,
      "description": "Methylphenidate Hydrochloride",
      "unit_price": 7.89,
      "total": 118.35
    },
    {
      "quantity": 100,
      "description": "Ibuprofen (BPXPO-00538)",
      "unit_price": 0.99,
      "total": 99.00
    },
    {
      "quantity": 2,
      "description": "Metformin Hydrochloride (BPXPO-00538)",
      "unit_price": 2.15,
      "total": 32.25
    },
    {
      "quantity": 15,
      "description": "Avobenzone, Octisalate and Octocrylene",
      "unit_price": 16.99,
      "total": 254.85
    },
    {
      "quantity": 10,
      "description": "Carisoprodol",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 10,
      "description": "Losartan Potassium",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 10,
      "description": "Pentazocine Hydrochloride and Naloxone Hydrochloride",
      "unit_price": 34.99,
      "total": 349.90
    },
    {
      "quantity": 25,
      "description": "Omeprazole",
      "unit_price": 9.99,
      "total": 249.75
    },
    {
      "quantity": 25,
      "description": "Losartan Potassium",
      "unit_price": 4.45,
      "total": 111.25
    },
    {
      "quantity": 10,
      "description": "Saline",
      "unit_price": 7.89,
      "total": 78.90
    },
    {
      "quantity": 25,
      "description": "Titanium dioxide",
      "unit_price": 10.25,
      "total": 256.25
    },
    {
      "quantity": 25,
      "description": "Bicalutamide (BPXPO-00538)",
      "unit_price": 2.15,
      "total": 53.75
    },
    {
      "quantity": 15,
      "description": "Ampicillin sodium",
      "unit_price": 16.99,
      "total": 254.85
    },
    {
      "quantity": 15,
      "description": "Octinoxate, Titanium Dioxide, Octisalate",
      "unit_price": 12.45,
      "total": 186.75
    },
    {
      "quantity": 25,
      "description": "Cavia porcellus hair and cavia porcellus skin",
      "unit_price": 12.45,
      "total": 311.25
    }
  ]
```

2) Invalid Case

```json
{"error": "Invalid input format. Missing required fields."}   
```
