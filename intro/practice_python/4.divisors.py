"""
    Create a program that asks the user for a number and then prints
    out a list of all the divisors of that number.

    (If you don’t know what a divisor is, it is a number that divides evenly
    into another number. For example, 13 is a divisor of 26
    because 26 / 13 has no remainder.)
"""


def get_divisors():
    num = int(input("What number should we divide?: "))

    possible_nums = list(range(1, num + 1))
    divisors = []

    for x in possible_nums:
        if num % x == 0:
            divisors.append(x)

    print(divisors)


get_divisors()
