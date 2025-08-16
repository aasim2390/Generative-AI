# -*- coding: utf-8 -*-
"""CrewAI Invoice Extractor.ipynb
"""

!pip install pytesseract -q
!sudo apt update
!sudo apt install tesseract-ocr

!pip install langchain-community --upgrade
!pip install unstructured --upgrade
!pip install crewai --upgrade
!pip install crewai-tools --upgrade

from google.colab import userdata
import os

OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from crewai import Agent, Task, Crew, Process

#pdf_path=r'/content/invoice-0-4.pdf'
pdf_path = r'/content/invoice_sample.pdf'

!pip install PyMuPDF

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

#ocr_extractor_tool.run(pdf_path)

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

# Example usage (uncomment and replace with your actual file path)
# if __name__ == "__main__":
#     from google.colab import files
#     uploaded = files.upload()
#     pdf_path = list(uploaded.keys())[0]
#     run_crew(pdf_path)

"""============================================================================"""

run_crew(r'/content/invoice-0-4.pdf')

run_crew(r'/content/RandomSamplePDF.pdf')
