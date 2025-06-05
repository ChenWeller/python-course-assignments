import random

def get_user_input():
    """
    Prompt the user for input and return it.
    """
    return input("Guess (1-20) | x=exit s=show d=debug m=move n=new: ").strip().lower()

def toggle_mode(mode_name, current_value):
    """
    Toggle boolean mode and print its new status.
    """
    print(f"{mode_name} mode {'on' if not current_value else 'off'}.")
    return not current_value

def move_number(number):
    """
    Slightly adjust the hidden number randomly within bounds.
    """
    number += random.choice([-2, -1, 0, 1, 2])
    return max(1, min(20, number))

def handle_guess(guess, number):
    """
    Compare the guess to the number and return status message.
    """
    if guess < number:
        print("Too low!")
        return False
    elif guess > number:
        print("Too high!")
        return False
    else:
        print("Correct!")
        return True

def play_game():
    """
    Play one session of the number guessing game.
    Returns True to start a new game, False to exit.
    """
    number = random.randint(1, 20)
    debug = False
    move_mode = False

    while True:
        if debug:
            print(f"[DEBUG] Current number is: {number}")

        user_input = get_user_input()

        if user_input == 'x':
            print("Game exited.")
            return False
        elif user_input == 's':
            print(f"The hidden number is: {number}")
        elif user_input == 'd':
            debug = toggle_mode("Debug", debug)
        elif user_input == 'm':
            move_mode = toggle_mode("Move", move_mode)
        elif user_input == 'n':
            print("Starting new game...")
            return True
        elif user_input.isdigit():
            guess = int(user_input)
            if handle_guess(guess, number):
                return True
        else:
            print("Invalid input.")

        if move_mode:
            number = move_number(number)

def main():
    """
    Main game loop to allow playing multiple games.
    """
    while play_game():
        continue

if __name__ == '__main__':
    main()
