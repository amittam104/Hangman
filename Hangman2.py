import random
from movies import movie_data
import string

#Function to get right word without spaces and dashes.
def random_movie():
    movie = random.choice(list(movie_data.keys()))
    hint = movie_data[movie]
    while ' ' in movie or '-' in movie:
        movie = random.choice(list(movie_data.keys()))
        hint = movie_data[movie]
    return movie, hint

def hangman():
    movie, hint = random_movie()
    movie = movie.upper()
    movie_letters = set(movie)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 10

    #Game loop to continue till one of the criterie is met i.e. correct guess or loss of lives
    while len(movie_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.", " Your guessed letters are: ", ' '.join(guessed_letters))

        movie_list = [letter if letter in guessed_letters else '-' for letter in movie]
        print("Guess the word: ", ' '.join(movie_list))

        if lives <= 3:
            print(f"Carefull you have only {lives} lives left.")
            print(f"Here is your hint: {hint}")
        else:
            pass

        user_letter = input("Eneter a letter: ").upper()

        #  Conditions to check whether user's input is correct or not.
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in movie_letters:
                movie_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("\nWrong guess. Guess again.")

        elif user_letter in guessed_letters:
            print("\nYou have already guessed that letter. Guess again.")
        else:
            pass

    if lives == 0:
        print(f"\nYou lost the game. Your word was {movie}.\n")
    else:
        print(f"\nCongratualtion!! You won. You guessed the {movie} word correctly.\n")

hangman()