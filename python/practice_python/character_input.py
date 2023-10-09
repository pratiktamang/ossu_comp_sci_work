"""
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they
    will turn 100 years old. Note: for this exercise, the expectation is that
    you explicitly write out the year

    Concepts
    1. Getting user input
    2. Manipulating strings (string concatenation)
"""


def express_when_100():
    name = input("Give me your name: ")
    age = int(input("Give me your age: "))
    delta = 100 - age
    current_year = 2023

    print(f"hey {name} you will 100 years in {current_year+ delta}")


express_when_100()
