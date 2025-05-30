#!/usr/bin/env python3
"""
rot13_file.py

A script to read a file, apply ROT13 cipher on its content,
and overwrite the file with the ROT13 encoded text.

Usage:
    python rot13_file.py <filename>

The file should contain plain text. This script will replace the
file's content with its ROT13 encoded version. ROT13 shifts
letters by 13 positions in the alphabet, leaving non-letters unchanged.
"""

import sys
import os

def rot13(text):
    """
    Applies ROT13 cipher to the input text.

    ROT13 shifts each letter by 13 places in the alphabet,
    wrapping around if necessary. Case is preserved.
    Non-alphabetic characters remain unchanged.

    Args:
        text (str): Original text.

    Returns:
        str: ROT13 encoded text.
    """
    result = []

    for char in text:
        if 'A' <= char <= 'Z':
            rotated = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(rotated)
        elif 'a' <= char <= 'z':
            rotated = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(rotated)
        else:
            result.append(char)

    return ''.join(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python rot13_file.py <filename>")
        print("The file should contain plain text content.")
        print("This script replaces the file's content with its ROT13 encoded version.")
        print("ROT13 shifts letters by 13 places; non-letters remain unchanged.")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        encoded_content = rot13(content)

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(encoded_content)

        print(f"Successfully encoded the file '{filename}' with ROT13.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
