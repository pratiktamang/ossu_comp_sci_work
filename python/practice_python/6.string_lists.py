"""
   Ask the user for a string and print out whether this string is a palindrome or not.
   (A palindrome is a string that reads the same forwards and backwards.)
"""


def string_lists():
    str = input("Check if this word is a palindrome: ")
    reversed = reverse(str)

    if str == reversed:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")

    # built-in reversal method
    reversed_str = str[::-1]

    if str == reversed_str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")


def reverse(str):
    reversed = ""
    i = len(str) - 1

    while i >= 0:
        reversed = reversed + str[i]
        i = i - 1

    return reversed


string_lists()
