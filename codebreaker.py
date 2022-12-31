import random

# Constants
MAX_GUESSES = 6
SECRET_COMBINATION_LENGTH = 4

# Variables
guesses = 0
game_over = False
secret_combination = [random.randint(0, 9) for i in range(SECRET_COMBINATION_LENGTH)]

# Main game loop
while not game_over:
    # Get the player's guess
    player_input = list(map(int, input("Enter your guess (4 digits): ")))

    # Validate the player's guess
    if len(player_input) != SECRET_COMBINATION_LENGTH:
        print("Error: Your guess must be a 4-digit combination.")
        continue

    # Increment the number of guesses
    guesses += 1

    # Check the player's guess
    correct = 0
    incorrect = 0
    for i in range(SECRET_COMBINATION_LENGTH):
        if player_input[i] == secret_combination[i]:
            correct += 1
        else:
            incorrect += 1

    # Print the results
    if correct == SECRET_COMBINATION_LENGTH:
        print("Congratulations! You guessed the secret combination!")
        game_over = True
    else:
        print(f"You have {correct} correct digits and {incorrect} incorrect digits.")

    # Check if the player has reached the maximum number of guesses
    if guesses == MAX_GUESSES:
        print("You didn't guess the secret combination! You lost!")
        game_over = True
