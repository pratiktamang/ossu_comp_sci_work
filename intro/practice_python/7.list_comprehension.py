"""
    Let’s say I give you a list saved in a variable:
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

    Write one line of Python that takes this list a and makes a new list
    that has only the even elements of this list in it.
"""


def list_comprehension():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    even_nums_list = []

    for num in a:
        if num % 2 == 0:
            even_nums_list.append(num)

    print(even_nums_list)

    # one liner
    even_nums_list_two = [num for num in a if num % 2 == 0]
    print(even_nums_list_two)


list_comprehension()

"""
    # Examples of list compreshension:

    # 1. Squaring each number in a list:
        numbers = [1, 2, 3, 4, 5]
        squares = [num**2 for num in numbers]
        print(squares)  # Output: [1, 4, 9, 16, 25]

    # 2. Filtering out negative numbers from a list:
        numbers = [-2, -1, 0, 1, 2]
        positive_numbers = [num for num in numbers if num >= 0]
        print(positive_numbers)  # Output: [0, 1, 2]

    # 3. Creating a list of tuples from two separate lists:
        names = ["Alice", "Bob", "Charlie"]
        ages = [25, 30, 35]
        people = [(name, age) for name, age in zip(names, ages)]
        print(people)  # Output: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
"""
