import random
from words import words
import string

def correct_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = correct_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 10
    

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. ", "Your guessed letters: ", ''.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print("Guess the word: ", ''.join(word_list))
            
            
        user_letter = input("Enter a letter: ").upper()

        if user_letter in alphabets - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
            
        elif user_letter in guessed_letters:
            print("You have guessed this letter already. Guess again.")
        else:
            print("Wrong guess. Guess again.")

    if lives == 0:
        print(f"You lost. Your word was {word}.")
    else:
        print(f"Congratulations! You guess the {word} word corretcly.")

hangman()