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


CHOICES = ["rock", "paper", "scissors"]
WINNING_COMBINATIONS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


def game():
    user_choice = user_input()
    comp_choice = computer_input()
    check_winner(user_choice, comp_choice)
    play_next_round()


def user_input():
    while True:
        user_input = input("Choose your weapon: ")
        if user_input in CHOICES:
            return user_input
        else:
            print("Not a valid options try again")


def computer_input():
    return random.choice(CHOICES)


def check_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
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

# while True:
#     game_dict = {"rock": 1, "scissors": 2, "paper": 3}
#     player_a = str(input("Player a: "))
#     player_b = str(input("Player b: "))
#     a = game_dict.get(player_a)
#     b = game_dict.get(player_b)
#     dif = a - b

#     if dif in [-1, 2]:
#         print("player a wins.")
#         if str(input("Do you want to play another game, yes or no?\n")) == "yes":
#             continue
#         else:
#             print("game over.")
#             break
#     elif dif in [-2, 1]:
#         print("player b wins.")
#         if str(input("Do you want to play another game, yes or no?\n")) == "yes":
#             continue
#         else:
#             print("game over.")
#             break
#     else:
#         print("Draw.Please continue.")
#         print("")
