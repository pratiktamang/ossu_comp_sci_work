"""
  Generate a random number between 1 and 9 (including 1 and 9).
  Ask the user to guess the number, then tell them whether they
  guessed too low, too high, or exactly right.

  (Hint: remember to use the user input lessons from the very first exercise)

  Extras:

  Keep the game going until the user types “exit”
  Keep track of how many guesses the user has taken,
  and when the game ends, print this out.

"""

import random


def guessing_game():
    guesses = 0
    correct = 0
    while True:
        user_input = input("Guess a number between 1 and 10: ")
        user_num = None

        if user_input == "exit":
            print_game_stats(guesses, correct)
            break

        user_num = int(user_input)
        rand_num = random.randint(1, 10)
        user_guess = input("Guess Low(l), high(h) or exactly right(e) ?:")
        guesses, correct = check_guess_score(
            user_num, rand_num, user_guess, guesses, correct
        )


def check_guess_score(u, r, g, guesses, correct):
    if (u == r and g == "e") or (u < r and g == "l") or (u > r and g == "h"):
        guesses += 1
        correct += 1
        print("You guessed correctly! 😊")
    else:
        guesses = guesses + 1
        print("You guessed incorrectly! 😭")

    return guesses, correct


def print_game_stats(guesses, correct):
    if guesses > 0:
        print(f"You guessed {guesses} times and got {correct} correct")


guessing_game()
