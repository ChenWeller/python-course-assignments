#!/usr/bin/env python3
"""
count_digits_in_file.py

Reads a text file with numbers and counts the occurrence of each digit (0-9).
Saves the count report to 'report.txt'.

Usage:
    python count_digits_in_file.py <input_filename>

Example:
    python count_digits_in_file.py examples/files/numbers.txt

Output:
    report.txt containing digit counts in the format:
    0 <count_of_0>
    1 <count_of_1>
    ...
    9 <count_of_9>
"""

import sys
import os

def count_digits(text):
    """
    Count occurrences of each digit (0-9) in the given text.

    Args:
        text (str): The input string to count digits in.

    Returns:
        dict: A dictionary with keys '0'-'9' and integer counts as values.
    """
    # Initialize counts for all digits to zero
    digit_counts = {str(d): 0 for d in range(10)}

    for char in text:
        if char.isdigit():
            digit_counts[char] += 1

    return digit_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_digits_in_file.py <input_filename>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Read the file content
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Count digits in the content
        counts = count_digits(content)

        # Write the counts to report.txt
        with open('report.txt', 'w', encoding='utf-8') as report_file:
            for digit in sorted(counts.keys()):
                report_file.write(f"{digit} {counts[digit]}\n")

        print("Digit counts have been saved to 'report.txt'.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
