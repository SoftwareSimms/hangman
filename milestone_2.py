import random

# Define a list of words
word_list = ["strawberry", "mango", "watermelon", "pineapple", "tomato"]
print(word_list)

# Randomly select a word
word = random.choice(word_list)
print(word)

# Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Step 1: Check if the input length is 1 and if it's an alphabetical character
if len(guess) == 1 and guess.isalpha():
    # Step 2: Input is valid, print a positive message
    print("Good guess!")
else:
    # Step 3: Input is invalid, print an error message
    print("Oops! That is not a valid input.")
