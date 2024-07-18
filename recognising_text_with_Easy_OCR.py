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