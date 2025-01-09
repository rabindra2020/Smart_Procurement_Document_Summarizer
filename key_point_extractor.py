project="Smart Procurement Document Summarizer" file="key_point_extractor.py" type="code"
from transformers import pipeline

ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_key_points(text):
    # Extract named entities
    entities = ner_pipeline(text)
    
    # Group entities by type
    grouped_entities = {}
    for entity in entities:
        if entity['entity'] not in grouped_entities:
            grouped_entities[entity['entity']] = []
        grouped_entities[entity['entity']].append(entity['word'])
    
    # Format key points
    key_points = []
    if 'DATE' in grouped_entities:
        key_points.append(f"Important dates: {', '.join(set(grouped_entities['DATE']))}")
    if 'ORG' in grouped_entities:
        key_points.append(f"Organizations involved: {', '.join(set(grouped_entities['ORG']))}")
    if 'MONEY' in grouped_entities:
        key_points.append(f"Financial information: {', '.join(set(grouped_entities['MONEY']))}")
    
    # Add more specific procurement-related points here
    # This would require training a custom NER model or using regex patterns
    
    return key_points