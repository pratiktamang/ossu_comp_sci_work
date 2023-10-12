"""
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they
    will turn 100 years old. Note: for this exercise, the expectation is that
    you explicitly write out the year

    Concepts
    1. Getting user input
    2. Manipulating strings (string concatenation)
"""

import datetime


def express_when_100():
    name = input("Give me your name: ")
    age = int(input("Give me your age: "))
    current_year = datetime.datetime.now().year
    year = current_year + (100 - age)

    print(f"hey {name}, you will be 100 years old in the year {year}")


express_when_100()


"""
  OFFICIAL SOLUTION
  name = input("What is your name: ")
  age = int(input("How old are you: "))
  year = 2014 - age + 100
  print(name + ", you will be 100 years old in the year " + str(year))
"""
