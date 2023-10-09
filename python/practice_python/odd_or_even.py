"""
    The exercise comes first (with a few extras if you want the extra
    challenge or want to spend more time), followed by a discussion. Enjoy!

    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user. Hint: how does an even / odd
    number react differently when divided by 2?

    Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num)
    and one number to divide by (check).  If check divides evenly into num,
    tell that to the user. If not, print a different appropriate message.
"""


def odd_or_even():
    num = int(input("Give me a number :"))
    check = int(input("Give me a number to divide by :"))

    if num % 4 == 0:
        print(f"{num} is a multiple of 4")
    elif num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

    if num % check == 0:
        print(f"{num} divides evenly by {check}")
    else:
        print(f"{num} does not divide evenly by {check}")


odd_or_even()
