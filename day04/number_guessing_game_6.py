import random

# Function to play one full game
def play_game():
    number = random.randint(1, 20)
    debug = False
    move_mode = False

    while True:
        if debug:
            print(f"[DEBUG] Current number is: {number}")

        guess = input("Guess (1-20) | x=exit s=show d=debug m=move n=new: ")

        if guess.lower() == 'x':
            print("Game exited.")
            return False  # Exit all games
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
        elif guess.lower() == 'n':
            print("Starting new game...")
            return True  # Restart game
        elif guess.isdigit():
            guess = int(guess)
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Correct!")
                return True
        else:
            print("Invalid input.")

        if move_mode:
            number += random.choice([-2, -1, 0, 1, 2])
            number = max(1, min(20, number))  # Keep number in range

# Loop to allow playing multiple games
while True:
    if not play_game():
        break  # Exit if user types 'x'
