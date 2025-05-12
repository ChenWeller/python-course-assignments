import random

number = random.randint(1, 20)

while True:
    guess = input("Guess (1-20), 'x'=exit, 's'=show answer: ")

    # Exit the game
    if guess.lower() == 'x':
        print("Game exited.")
        break

    # Show the number (cheat mode)
    elif guess.lower() == 's':
        print(f"The hidden number is: {number}")
        continue

    # Handle numeric input
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
        print("Invalid input. Use a number, 'x', or 's'.")
