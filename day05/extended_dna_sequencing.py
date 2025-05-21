# extended_dna_sequencing.py
import sys
import re

def main():
    # Prompt the user to enter a DNA sequence interactively
    sequence = input("Please type in a sequence:\n").upper().strip()

    # Check if the input is empty
    if not sequence:
        print("Error: No sequence entered. Please provide a DNA sequence containing A, C, T, G and possibly foreign characters.")
        sys.exit(1)

    # Check for RNA base 'U'
    if 'U' in sequence:
        print("Error: RNA detected (sequence contains 'U').")
        print("Please provide a DNA sequence containing only A, C, T, G and foreign characters.")
        sys.exit(1)

    # Define valid DNA bases
    valid_bases = set('ACTG')

    # Use regex to split sequence into fragments containing only valid bases
    # The pattern '[^ACTG]+' matches one or more characters NOT in ACTG, used as separators
    fragments = re.split(r'[^ACTG]+', sequence)

    # Filter out empty strings resulting from splitting
    fragments = [frag for frag in fragments if frag]

    # Validate fragments contain only valid DNA bases (should be redundant due to regex, but double-check)
    for frag in fragments:
        if not all(base in valid_bases for base in frag):
            print(f"Error: Invalid characters found in fragment '{frag}'. Only A, C, T, G are allowed.")
            sys.exit(1)

    # Sort fragments by length descending
    fragments.sort(key=len, reverse=True)

    # Print the sorted fragments list
    print(fragments)

if __name__ == '__main__':
    main()
