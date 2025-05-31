import streamlit as st
import PyPDF2

st.title("PDF Text Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    st.subheader("Extracted Text:")
    st.text_area("PDF Content", text, height=400)