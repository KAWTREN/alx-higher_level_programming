#!/usr/bin/python3
def text_indentation(text):
    """
    Print the input text with 2 new lines after each '.', '?' and ':' characters.

    Args:
        text (str): The input text.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""
    punctuation_chars = [".", "?", ":"]
    
    # Iterate through each character in the input text
    for char in text:
        formatted_text += char
        
        # If the character is a '.', '?', or ':', add 2 new lines
        if char in punctuation_chars:
            formatted_text += "\n\n"

    print(formatted_text, end='')
    print()
    print()
