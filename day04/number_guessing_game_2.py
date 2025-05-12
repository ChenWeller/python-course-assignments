import random

number = random.randint(1, 20)

while True:
    guess = input("Guess the number between 1 and 20 (or 'x' to exit): ")

    # Allow user to exit
    if guess.lower() == 'x':
        print("Game exited.")
        break

    # Handle numeric guesses
    if guess.isdigit():
        guess = int(guess)
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            break
    else:
        print("Invalid input. Enter a number or 'x' to quit.")
