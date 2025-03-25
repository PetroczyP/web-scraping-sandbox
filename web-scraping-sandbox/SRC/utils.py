import re

def extract_emails(text):
    """
    Extracts all email addresses from the given text.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_phone_numbers(text):
    """
    Extracts all phone numbers from the given text.
    """
    phone_pattern = r'\+?\d[\d -]{8,12}\d'
    return re.findall(phone_pattern, text)

def clean_text(text):
    """
    Cleans the given text by removing extra whitespace and special characters.
    """
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.strip()
