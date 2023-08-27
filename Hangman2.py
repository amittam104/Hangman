import random
from words import words
import string

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

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.", " Your guessed letters are: ", ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print("\nGuess the word: ", ' '.join(word_list))

        user_letter = input("\nEneter a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter == word_letters:
                print("You have already guessed that letter. Guess again.\n")
            else:
                lives = lives - 1

    if lives == 0:
        print(f"\nYou lost the game. Your word was {word}.\n")
    else:
        print(f"\nCongratualtion!! You won. You guessed the {word} word correctly.\n")

hangman()