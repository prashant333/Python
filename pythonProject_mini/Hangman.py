"""
This is a word guessing game

You get a fixed number of lives or attempts to guess the word. Word guessing is done letter by letter.
"""

import string
from words import words
import random


def get_valid_word(words):        # function to get valid words, word list has many letters with whitespace and hyphen.
    word = random.choice(words)           # choose a random word from list
    while " " in word or "-" in word:     # loop until valid word is obtained
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)              # getting each letter of word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()                  # all the letters used by user so far.

    lives = 5

    while len(word_letter) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used these many letters', ' '.join(used_letter))
        word_list = [letter if letter in used_letter else "-" for letter in word]
        print(f"lives left {lives}")
        print('Current word: ', ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet-used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
                print("")

            else:
                lives -= 1
                print(f"Your letter \'{user_input}\' is not in the word")
                # print("please try again.")

        elif user_input in used_letter:
            print("You have already used the letter before, Please try another letter: ")

        else:
            print("That is invalid input.")

    if lives == 0:
        print(f"You lost, total remaining lives is {lives}")
        print("The word was: ", word)
    else:
        print("That's correct. You won!!")


if __name__ == '__main__':
    hangman()
