# count_words_in_lists.py

celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

word_counts = {}

for word in celestial_objects:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Print words and their counts
for word, count in word_counts.items():
    print(f"{word:<10} {count}")
