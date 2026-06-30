import re


def clean_text(text):

    # lowercase
    text = text.lower()

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    return text
