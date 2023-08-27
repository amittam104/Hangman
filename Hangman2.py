import random
from words import words
import string

#Function to get right word without spaces and dashes.
def right_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = right_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 10

    #Game loop to continue till one of the criterie is met i.e. correct guess or loss of lives
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.", " Your guessed letters are: ", ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print("Guess the word: ", ' '.join(word_list))

        if lives <= 3:
            print(f"Carefull you have only {lives} lives left.")
        else:
            pass

        user_letter = input("Eneter a letter: ").upper()
        
        #  Conditions to check whether user's input is correct or not.
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("\nWrong guess. Guess again.")

        elif user_letter in guessed_letters:
            print("\nYou have already guessed that letter. Guess again.")
        else:
            pass

    if lives == 0:
        print(f"\nYou lost the game. Your word was {word}.\n")
    else:
        print(f"\nCongratualtion!! You won. You guessed the {word} word correctly.\n")

hangman()