project="Smart Procurement Document Summarizer" file="document_processor.py" type="code"
import PyPDF2
import io

def process_document(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text