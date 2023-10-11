"""
Ask the user for a number and determine whether the number is prime
or not. (For those who have forgotten, a prime number is a number
that has no divisors.)

You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""


def get_divisors(num):
    return [x for x in range(2, num) if num % x == 0]


def check_prime():
    num = int(input("What number should we check if prime? "))

    divisors = get_divisors(num)

    if num > 1:
        if len(divisors) == 0:
            print(f"Nice {num} is a prime number!")
        else:
            print(f"{num} is NOT prime number \n")
            print(f"it has following divisors {divisors}")
    else:
        print(f"{num} is NOT prime number")


check_prime()
