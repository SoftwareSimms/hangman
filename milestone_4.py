import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word!")

            # Loop through each letter in the word
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace the "_" with the guess

            # Check if this guess revealed a new letter
            if guess not in self.list_of_guesses:
                self.num_letters -= 1  # Reduce the count of unique letters to guess
            return True  # Indicate a correct guess
        else:
            self.num_lives -= 1  # Reduce the number of lives
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            return False  # Indicate an incorrect guess


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter, any letter: ")

            # Check if the guess is a single alphabetic character
            if guess.isalpha() and len(guess) == 1:
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break  # Exit the loop after processing the guess
            else:
                print("Invalid input, please enter a single letter")  # Inform the user about invalid input

# Example usage
word_list = ['example', 'hangman', 'python']
game = Hangman(word_list)
game.ask_for_input()
