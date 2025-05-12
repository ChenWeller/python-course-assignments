import random

# Generate a random number between 1 and 20
number = random.randint(1, 20)

# Keep asking until the user guesses the correct number
while True:
    guess = int(input("Guess the number between 1 and 20: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break  # Exit loop when guessed correctly
