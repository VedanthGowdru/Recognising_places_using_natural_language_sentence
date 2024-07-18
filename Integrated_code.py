
import re
import spacy
from spacy.tokens import Span
from spacy.util import filter_spans
from spacy import displacy
import easyocr

def image_to_text(image_path):
    # Initialize the easyocr reader
    reader = easyocr.Reader(['en'])  # Specify the languages you need, here 'en' is for English

    # Read the text from the image
    result = reader.readtext(image_path, detail=0)

    # Combine the text parts into a single string
    text = ' '.join(result)
    return text

# Example usage
image_path = 'ks6apligrwhc1.jpeg'
text = image_to_text(image_path)
print(text)



# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the regex patterns
# Pattern for general locations (excluding falls)
location_pattern = r"\b\w*(pura|pur|kode|puram|giri|ool|luru|halli|nagar|nagara|ssan|Goa|Udupi|bad|kesh|sthan|pal|pradesh|garh|hati|shik)\b"

# Pattern specifically for falls
# Pattern for specific cities
city_pattern = r"\b(Surat|Patna|Bangalore|Mysore|Kolkata|Kochi|Andhra|Assam|Bhopal)\b"

# Find all matches for locations, falls, and specific cities
location_matches = re.finditer(location_pattern, text)

city_matches = re.finditer(city_pattern, text)

# Process the text with SpaCy
doc = nlp(text)

# List to store custom entities
new_entities = []

# Add location entities
for match in location_matches:
    start, end = match.span()
    span = doc.char_span(start, end, label="LOC", alignment_mode="strict")
    if span is not None:
        new_entities.append(span)

# Add specific city entities
for match in city_matches:
    start, end = match.span()
    span = doc.char_span(start, end, label="CITY", alignment_mode="strict")
    if span is not None:
        new_entities.append(span)

# Filter out overlapping spans
new_entities = filter_spans(new_entities)

# Set the new entities in the doc
doc.set_ents(new_entities, default="unmodified")

# Print the entities
for ent in doc.ents:
    print(ent.text, ent.label_)

# Visualize the entities
displacy.render(doc, style="ent", jupyter=True)