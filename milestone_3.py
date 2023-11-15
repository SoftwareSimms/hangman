# Example random word
random_word = "example"

def check_guess(guess):
    # Convert guess to lower case
    guess = guess.lower()
    if guess in random_word:
        print(f"Good guess, {guess} is in the random word!")
        return True  # Indicate a correct guess
    else:
        print(f"Sorry, {guess} is not in the word")
        return False  # Indicate an incorrect guess

def ask_for_input():
    while True:
        guess = input("Guess a letter, any letter: ")

        # Check if the guess is a single alphabetic character
        if guess.isalpha() and len(guess) == 1:
            if check_guess(guess):
                break  # Exit the loop after a correct guess
        else:
            print("Invalid input, please enter a single letter")  # Inform the user about invalid input

ask_for_input()
