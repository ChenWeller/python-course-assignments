import random

number = random.randint(1, 20)
debug = False  # Toggle flag for debug mode

while True:
    # Show the current number if debug mode is on
    if debug:
        print(f"[DEBUG] Current number is: {number}")

    guess = input("Guess (1-20), 'x'=exit, 's'=show, 'd'=debug toggle: ")

    if guess.lower() == 'x':
        print("Game exited.")
        break
    elif guess.lower() == 's':
        print(f"The hidden number is: {number}")
        continue
    elif guess.lower() == 'd':
        debug = not debug  # Toggle debug mode
        print(f"Debug mode {'on' if debug else 'off'}.")
        continue
    elif guess.isdigit():
        guess = int(guess)
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            break
    else:
        print("Invalid input.")
