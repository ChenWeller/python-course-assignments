# count how many times each digit (0-9) appears in a given list of numbers:

numbers = [1203, 1256, 312456, 98]

# Initialize a dictionary to count digits from 0 to 9
digit_counts = {str(d): 0 for d in range(10)}

# Iterate through each number in the list
for number in numbers:
    # Convert number to string to iterate digits
    for digit in str(number):
        if digit in digit_counts:
            digit_counts[digit] += 1

# Print counts in ascending digit order
for digit in range(10):
    print(f"{digit}  {digit_counts[str(digit)]}")
