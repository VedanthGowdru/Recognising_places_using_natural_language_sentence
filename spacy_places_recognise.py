import re
import spacy
from spacy.tokens import Span
from spacy.util import filter_spans
from spacy import displacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the text input
text = input("Enter your string here:\n")

# Define the regex patterns
# Pattern for general locations (excluding falls)
location_pattern = r"\b\w*(pura|pur|kode|puram|giri|ool|luru|halli|nagar|nagara|ssan|Goa|Udupi|bad|kesh|sthan)\b"

# Pattern specifically for falls


# Pattern for specific cities
city_pattern = r"\b(Surat|Patna|Bangalore|Mysore|Kolkata|Kochi)\b"

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
