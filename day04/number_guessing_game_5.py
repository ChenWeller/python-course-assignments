import random

number = random.randint(1, 20)
debug = False
move_mode = False  # Toggle flag for move mode

while True:
    if debug:
        print(f"[DEBUG] Current number is: {number}")

    guess = input("Guess (1-20), x=exit s=show d=debug m=move: ")

    if guess.lower() == 'x':
        print("Game exited.")
        break
    elif guess.lower() == 's':
        print(f"The hidden number is: {number}")
        continue
    elif guess.lower() == 'd':
        debug = not debug
        print(f"Debug mode {'on' if debug else 'off'}.")
        continue
    elif guess.lower() == 'm':
        move_mode = not move_mode
        print(f"Move mode {'on' if move_mode else 'off'}.")
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

    # If move mode is on, modify the number slightly
    if move_mode:
        number += random.choice([-2, -1, 0, 1, 2])
        number = max(1, min(20, number))  # Keep number in [1, 20]
