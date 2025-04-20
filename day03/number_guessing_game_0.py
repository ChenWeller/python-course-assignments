import random

# Computer selects a random number between 1 and 20
secret_number = random.randint(1, 20)

# Ask the user for their guess
guess = int(input("Guess a number between 1 and 20: "))

# Compare the guess to the secret number
if guess < secret_number:
    print("you guessed a smaller number than me!")
elif guess > secret_number:
    print("you guessed a bigger number than me")
else:
    print("Correct! You guessed it!")
