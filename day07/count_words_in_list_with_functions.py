# count_words_in_list_with_functions.py

def get_celestial_objects():
    """
    Return the predefined list of celestial objects.
    """
    return ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

def count_words(word_list):
    """
    Count occurrences of each word in the list.
    """
    word_counts = {}
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def display_counts(word_counts):
    """
    Display each word and its count.
    """
    for word, count in word_counts.items():
        print(f"{word:<10} {count}")

def main():
    """
    Main function to run the word counting.
    """
    words = get_celestial_objects()
    counts = count_words(words)
    display_counts(counts)

if __name__ == '__main__':
    main()
