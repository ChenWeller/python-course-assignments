import random

# Generate a random number between 1 and 20
number = random.randint(1, 20)

# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 20: "))

# Check if the guess is too low, too high, or correct
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct!")
