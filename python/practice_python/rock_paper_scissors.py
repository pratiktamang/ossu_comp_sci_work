"""
    Make a two-player Rock-Paper-Scissors game.
    (Hint: Ask for player plays (using input), compare them,
    print out a message of congratulations to the winner,
    and ask if the players want to start a new game)

    Remember the rules:
      - Rock beats scissors
      - Scissors beats paper
      - Paper beats rock
"""

import random


CHOICES = {1: "rock", 2: "paper", 3: "scissors"}
WINNING_COMBINATIONS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


def game():
    user_choice = user_input()
    comp_choice = computer_input()

    check_winner(user_choice, comp_choice)
    play_next_round()


def user_input():
    user_input = input("Choose your weapon: ")
    return user_input


def computer_input():
    computer_input = CHOICES[random.randint(1, 3)]
    return computer_input


def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif WINNING_COMBINATIONS[user_choice] == computer_choice:
        print("User wins!")
    else:
        print("Computer wins!")


def play_next_round():
    play_next_round = input("Do you want to play another round? (y/n): ")
    if play_next_round == "y":
        game()
    else:
        print("Thanks for playing!")


game()
