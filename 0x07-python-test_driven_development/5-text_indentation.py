#!/usr/bin/python3
def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: . , ? and :
    Args:
        text: string
    Raise:
        TypeError: if text not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    separ = ['.','?',':']
    current_line = ""
    for char in text:
        current_line += char
        if char in separ:
            print(current_line.strip())
            print()
            current_line = ""
    if current_line.strip():
        print(current_line.strip())