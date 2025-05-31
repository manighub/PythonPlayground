import streamlit as st
import PyPDF2

st.title("PDF Text Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        st.subheader("Extracted Text:")
        st.text_area("PDF Content", text, height=400)
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
else:
    st.info("Please upload a PDF file to extract its text.")