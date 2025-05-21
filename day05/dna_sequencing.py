# dna_sequencing.py
import sys

def main():
    # Check that exactly one argument (the DNA sequence) is provided
    if len(sys.argv) != 2:
        # Friendly message if no sequence or too many arguments are given
        print("Please provide a DNA sequence as a command-line argument.")
        print("Example usage:")
        print("  python3 dna_sequencing.py ACCGXXCXXGTTACTGGGCXTTGTXX")
        sys.exit(1)

    # Read the input sequence and normalize to uppercase to handle case-insensitivity
    sequence = sys.argv[1].upper()

    # Check for presence of 'U' which indicates RNA instead of DNA
    if 'U' in sequence:
        print("Error: RNA detected (sequence contains 'U').")
        print("Please provide a DNA sequence containing only A, C, T, G, and X as separators.")
        sys.exit(1)

    # Split the sequence into fragments by 'X' character
    # 'X' acts as a delimiter for junk/invalid parts
    segments = sequence.split('X')

    # Filter out empty segments that may occur due to consecutive 'X's or leading/trailing 'X's
    segments = [seg for seg in segments if seg]

    # Define the valid DNA bases
    valid_bases = set('ACTG')

    # Validate each segment contains only valid DNA bases
    for seg in segments:
        if not all(base in valid_bases for base in seg):
            print(f"Error: Invalid characters found in segment '{seg}'.")
            print("Only A, C, T, G are allowed within DNA segments.")
            sys.exit(1)

    # Sort the segments by their length in descending order (longest first)
    segments.sort(key=len, reverse=True)

    # Output the sorted list of DNA segments
    print(segments)

if __name__ == '__main__':
    main()
