
import streamlit as st
from PIL import Image
import easyocr  # <-- Import easyocr instead of pytesseract
import numpy as np # <-- easyocr needs this
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import torch

# --- 1. OCR Component using easyocr ---
# We cache the reader object so it doesn't reload on every run
@st.cache_resource
def get_ocr_reader():
    """Initializes and returns an easyocr Reader object."""
    # This will download the model for English ('en') the first time it runs
    reader = easyocr.Reader(['en']) 
    return reader

def extract_text_from_image(image):
    """Takes a PIL Image and returns the extracted text as a string."""
    try:
        # Convert PIL Image to a NumPy array, which easyocr prefers
        image_np = np.array(image)
        
        # Get the reader object
        reader = get_ocr_reader()
        
        # Read text from the image
        # The result is a list of tuples, where each tuple contains the bounding box, the text, and the confidence score.
        result = reader.readtext(image_np)
        
        # Extract just the text and join it together into a single string
        extracted_text = ' '.join([text for bbox, text, conf in result])
        
        return extracted_text
    except Exception as e:
        st.error(f"Error during OCR extraction: {e}")
        return None

# --- 2. LangChain Summarization Component (This stays the same) ---
from transformers import pipeline

@st.cache_resource
def get_summarization_chain():
    """Initializes and returns a LangChain summarization chain."""
    model_id = "sshleifer/distilbart-cnn-12-6"
    
    # --- THIS IS THE CORRECTED LINE ---
    # Create a Transformers pipeline directly
    summarizer_pipeline = pipeline("summarization", model=model_id)

    # Wrap the pipeline in a LangChain LLM
    llm = HuggingFacePipeline(pipeline=summarizer_pipeline)

   # Define the new, more detailed prompt template
    template = """
    You are an expert medical assistant. 
    **Actual Prescription Text to Summarize:**
    "{text}"

    """
    prompt = PromptTemplate(template=template, input_variables=["text"])

    # Create the LLMChain
    chain = LLMChain(prompt=prompt, llm=llm)
    return chain

# --- 3. Streamlit User Interface (This stays the same) ---

st.title("🩺 Prescription Summarizer for Diabetic Patients")
st.write("Upload a clear image of your prescription to get a simple summary of your medications.")

uploaded_file = st.file_uploader("Choose a prescription image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", use_column_width=True)

    with st.spinner("Analyzing the prescription... please wait."):
        st.write("### Step 1: Extracting Text from Image...")
        extracted_text = extract_text_from_image(image)

        if extracted_text:
            with st.expander("View Extracted Text"):
                st.text_area("", extracted_text, height=250)

            st.write("### Step 2: Generating Summary...")
            
            if len(extracted_text.split()) > 20:
                summarization_chain = get_summarization_chain()
                summary = summarization_chain.run(extracted_text)
                
                st.success("### Your Prescription Summary")
                st.write(summary)
            else:
                st.warning("The extracted text is too short to summarize. It is displayed above.")
        else:
            st.error("Could not extract any text from the image. Please try a clearer image.")