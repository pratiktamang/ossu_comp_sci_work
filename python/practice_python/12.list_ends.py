"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list.

For practice, write this code inside a function.
"""


def list_ends(arr=[5, 10, 15, 20, 25]):
    print(f"The first and last elements are: {arr[0]} and {arr[-1]}")
    return [arr[0], arr[-1]]


list_ends()
