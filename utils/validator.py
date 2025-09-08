import re

def contains_phone_number(text: str) -> bool:
    """
    Check if the message contains a 10-digit phone number.
    """
    pattern = r"\b\d{10}\b"
    return re.search(pattern, text) is not None
