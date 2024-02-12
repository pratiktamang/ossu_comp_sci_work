import random


def get_user_choice(options):
    print()
    while True:
        user_choice = input("Choose Rock, Paper or Scissors. or type quit to exit: ").lower()
        if user_choice in options or user_choice == "quit":
            return user_choice
        print("Naughty naughty! that is not allowed, please choose rock, paper or scissors")

def display_result(message, round,  user_score, computer_score):
    print("\n" + "-" *20)
    print(f"Round: {round}\n{message}\nUser: {user_score}, Computer: {computer_score}\n" + "-" * 20)

def check_winner(user_choice, computer_choice, win_combos):
    if user_choice == computer_choice:
        return  "draw", f"you both chose {user_choice} its a draw!"
    elif win_combos[user_choice] == computer_choice:
        return  "user", f"you chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        return "computer", f"you chose {user_choice}, computer chose {computer_choice}. Computer got you!"

def play_game(win_combos):
    user_score = computer_score = round = 0
    while user_score < 2 and computer_score < 2:
        round += 1
        user_choice = get_user_choice(list(win_combos.keys()))

        if user_choice == "quit":
            return "quit"

        computer_choice = random.choice(list(win_combos.keys()))
        winner, message = check_winner(user_choice, computer_choice, win_combos)
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score +=1

        display_result(message, round, user_score, computer_score)

    if user_score == 2:
        print("\n🎉🎉🎉 CONGRATS you won! 🎉🎉🎉")
        return "user_won"
    else:
        print("\n😭😭😭computer won! better luck next time 😭😭")

def display_end_game_message(game, win_count):
    message = f"You played {game} games and won {win_count} of them!"
    bye = "Thanks for playing! Bye bye :)"
    print("\n" + "*" * (len(message) + 4))
    print(f"* {message} *")
    print(f"* {bye}{' ' * (len(message) - len(bye))} *")
    print("*" * (len(message) + 4) + "\n")

def ask_if_user_wants_to_replay(game, win_count):
    while True:
        answer = input("Do you want to play again? Y/N: ").lower()
        if answer == "y":
            return

        if answer == "n":
            display_end_game_message(game, win_count)
            return "end game"

        print("\n invalid, y or n homie? 👀")

if __name__ == '__main__':
    game = win_count = 0
    win_combos = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    while True:
        game += 1
        res = play_game(win_combos)

        if res == "quit":
            display_end_game_message(game, win_count)
            break
        if res == "user_won":
            win_count += 1

        if ask_if_user_wants_to_replay(game, win_count) == "end game":
            break