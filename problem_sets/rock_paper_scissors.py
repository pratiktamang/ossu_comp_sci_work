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
#
# RUBY
# require 'io/console'

# def get_user_choice(options)
#   while true
#     print "\nChoose Rock, Paper or Scissors. or type quit to exit: "
#     user_choice = STDIN.gets.chomp.downcase
#     if options.include?(user_choice) || user_choice == "quit"
#       return user_choice
#     end
#     puts "Naughty naughty! that is not allowed, please choose rock, paper or scissors"
#   end
# end

# def display_result(message, round, user_score, computer_score)
#   puts "\n" + "-" * 20
#   puts "Round: #{round}\n#{message}\nUser: #{user_score}, Computer: #{computer_score}\n" + "-" * 20
# end

# def check_winner(user_choice, computer_choice, win_combos)
#   if user_choice == computer_choice
#     return "draw", "you both chose #{user_choice} its a draw!"
#   elsif win_combos[user_choice] == computer_choice
#     return "user", "you chose #{user_choice}, computer chose #{computer_choice}. You win!"
#   else
#     return "computer", "you chose #{user_choice}, computer chose #{computer_choice}. Computer got you!"
#   end
# end

# def play_game(win_combos)
#   user_score = computer_score = round = 0
#   while user_score < 2 && computer_score < 2
#     round += 1
#     user_choice = get_user_choice(win_combos.keys)

#     if user_choice == "quit"
#       return "quit"
#     end

#     computer_choice = win_combos.keys.sample
#     winner, message = check_winner(user_choice, computer_choice, win_combos)
#     if winner == "user"
#       user_score += 1
#     elsif winner == "computer"
#       computer_score += 1
#     end

#     display_result(message, round, user_score, computer_score)
#   end

#   if user_score == 2
#     puts "\n🎉🎉🎉 CONGRATS you won! 🎉🎉🎉"
#     return "user_won"
#   else
#     puts "\n😭😭😭computer won! better luck next time 😭😭"
#   end
# end

# def display_end_game_message(game, win_count)
#   message = "You played #{game} games and won #{win_count} of them!"
#   bye = "Thanks for playing! Bye bye :)"
#   puts "\n" + "*" * (message.length + 4)
#   puts "* #{message} *"
#   puts "* #{bye}#{' ' * (message.length - bye.length)} *"
#   puts "*" * (message.length + 4) + "\n"
# end

# def ask_if_user_wants_to_replay(game, win_count)
#   while true
#     print "Do you want to play again? Y/N: "
#     answer = STDIN.gets.chomp.downcase
#     if answer == "y"
#       return
#     end

#     if answer == "n"
#       display_end_game_message(game, win_count)
#       return "end game"
#     end

#     puts "\n invalid, y or n homie? 👀"
#   end
# end

# game = win_count = 0
# win_combos = {"rock" => "scissors", "scissors" => "paper", "paper" => "rock"}
# while true
#   game += 1
#   res = play_game(win_combos)

#   if res == "quit"
#     display_end_game_message(game, win_count)
#     break
#   end
#   if res == "user_won"
#     win_count += 1
#   end

#   if ask_if_user_wants_to_replay(game, win_count) == "end game"
#     break
#   end
# end