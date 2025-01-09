project="Smart Procurement Document Summarizer" file="summarizer.py" type="code"
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Split the text into chunks of 1024 tokens (BART's max input length)
    max_chunk_length = 1024
    chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)