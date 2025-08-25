import streamlit as st
from chains.extractor import get_extractor_chain
from chains.evaluator import get_evaluator_chain
from examples.sample_inputs import EXAMPLES
from utils.helpers import to_json_download

st.set_page_config(page_title="DataExtract", layout="wide")
st.title("🔑 DataExtract - Key Data Extraction Tool")

option = st.selectbox("Choose an example text (or enter custom):", ["Custom"] + list(EXAMPLES.keys()))

if option == "Custom":
    user_text = st.text_area("Enter your text here:")
else:
    user_text = EXAMPLES[option]

if st.button("Extract & Evaluate") and user_text.strip():
    # Extraction
    chain, parser, ProductReview = get_extractor_chain()
    format_instructions = parser.get_format_instructions()

    result = chain.invoke({
        "input_text": user_text,
        "format_instructions": format_instructions
    })

    # Show input
    st.subheader("📝 Input Text")
    st.write(user_text)

    # Show extracted structured data
    st.subheader("📊 Extracted Data")
    st.json(result.model_dump())

    # Evaluation
    evaluator = get_evaluator_chain()
    eval_result = evaluator.invoke({
        "input_text": user_text,
        "extracted_data": result.model_dump()
    })

    st.subheader("⚖️ Evaluation (LLM-as-Judge)")
    st.json(eval_result.content)

    # Download JSON
    json_data, filename = to_json_download(result)
    st.download_button("📥 Download JSON", data=json_data, file_name=filename, mime="application/json")
