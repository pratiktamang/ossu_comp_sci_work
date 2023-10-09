"""
Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates). Make sure your
    program works on two lists of different sizes.

    Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out
    at this point - we’ll get to it soon)
"""

import random


def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    rand_a = random.sample(range(100), 15)
    rand_b = random.sample(range(100), 10)

    common_elements = []

    for i in a:
        include = False
        if i not in common_elements:
            for j in b:
                if i == j:
                    include = True
                    break

        if include is True:
            common_elements.append(i)
    print(common_elements)

    # using built in set method
    common_elements_in_random = list(set(rand_a) & set(rand_b))
    print(common_elements_in_random)


list_overlap()
