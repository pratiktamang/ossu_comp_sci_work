# Problem Set 2, hangman.py
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "./ps2_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    word_guess = True
    for char in secret_word:
        if char not in letters_guessed:
            word_guess = False

    if word_guess == True:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # don't think this work with duplicate letters
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_"

    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    not_guessed = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed += letter

    return not_guessed


def print_status(allowed_guesses, warnings, letters_guessed):
    print(f"{allowed_guesses} guesses left | {3-warnings} warnings left")
    print(f"Available letters: {get_available_letters(letters_guessed)}\n")


def print_warning(message, warnings):
    print("❌❌❌❌\n")
    print(
        f"{message} This is warning number {warnings}. Careful! You have {3-warnings} remaining\n"
    )
    print("❌❌❌❌")


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    allowed_guesses = 6
    letters_guessed = []
    warnings = 0

    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("You get 3 warnings total. Don't mess up!\n")

    while True:
        if warnings >= 3:
            print("You lose, you're disqualified.")
            return
        if allowed_guesses <= 0:
            print(f"LOL ded 💀💀💀💀💀💀️️️️️️️. YOU SUCK! The word is {secret_word}\n")
            return

        print_status(allowed_guesses, warnings, letters_guessed)
        guess = input("Please guess a letter: ")

        if guess in letters_guessed:
            warnings += 1
            print_warning("You can't guess a letter you've already guessed!", warnings)
            continue

        if not str.isalpha(guess):
            warnings += 1
            print_warning("You must guess an alphabetical letter!", warnings)
            continue

        letters_guessed.append(guess)
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if guess in secret_word:
            print(f'Good guess 😀! "{guess}" is in the secret word: {guessed_word}')
            if is_word_guessed(secret_word, letters_guessed):
                print(
                    f"🎉🥳🎊\nCongratulations! You guessed the secret word '{secret_word}' correctly!\n"
                )
                return
        else:
            allowed_guesses -= 1
            print(f'Oh no! 😭 "{guess}" is not the secret word: {guessed_word}')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for my_char, other_char in zip(my_word, other_word):
        if my_char != "_" and my_char != other_char:
            return False

    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    possible_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_words.append(word)

    print(" ".join(possible_words))


def hangman_with_hints(secret_word):
    # secret_word: string, the secret word to guess.

    # Starts up an interactive game of Hangman.

    # * At the start of the game, let the user know how many
    #   letters the secret_word contains and how many guesses s/he starts with.

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("--------------------")

    guesses = 6
    letters_guessed = []
    # * The user should start with 6 guesses
    # * Before each round, you should display to the user how many guesses
    #   s/he has left and the letters that the user has not yet guessed.
    while True:
        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! The word was {secret_word}")
            break
        else:
            print(f"You have, {guesses} guesses left.")
            print(f"Available letters: {get_available_letters(letters_guessed)}\n")
            # * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
            guess = input("Please guess a letter: ")

            while True:
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if guess == "*":
                    print("Possible word matches are:")
                    show_possible_matches((guessed_word))
                    break

                elif guess.isalpha() == False:
                    guess = input("Please guess a letter: ")
                else:
                    if guess in letters_guessed:
                        print("You already guessed that letter!")
                        guess = input("Please guess a letter: ")
                    else:
                        letters_guessed.append(guess)
                        print("letter_guessed", letters_guessed)
                        break

            # * The user should receive feedback immediately after each guess
            #   about whether their guess appears in the computer's word.
            # * After each guess, you should display to the user the
            #   partially guessed word so far.
            if guess in secret_word:
                print(f"Good guess: {guessed_word}")
                print("--------------------")

            # * If the guess is the symbol *, print out all words in wordlist that
            #   matches the current guessed word.

    # Follows the other limitations detailed in the problem write-up.


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


def get_guess():
    return input("Please guess a letter: ")


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    hangman_with_hints("apple")
