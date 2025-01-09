project="Smart Procurement Document Summarizer" file="app.py" type="code"
import streamlit as st
import PyPDF2
from transformers import pipeline
from googletrans import Translator

from document_processor import process_document
from summarizer import summarize_text
from key_point_extractor import extract_key_points

def main():
    st.title("Smart Procurement Document Summarizer")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Process the document
        text = process_document(uploaded_file)

        # Detect language and translate if not English
        translator = Translator()
        detected_lang = translator.detect(text[:1000]).lang  # Detect language from first 1000 characters
        if detected_lang != 'en':
            st.info(f"Detected language: {detected_lang}. Translating to English...")
            text = translator.translate(text, dest='en').text

        # Summarize the document
        summary = summarize_text(text)

        # Extract key points
        key_points = extract_key_points(text)

        # Display results
        st.subheader("Document Summary")
        st.write(summary)

        st.subheader("Key Points")
        for point in key_points:
            st.write(f"- {point}")

if __name__ == "__main__":
    main()