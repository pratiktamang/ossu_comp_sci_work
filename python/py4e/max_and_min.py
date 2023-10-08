"""
5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message and
ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")

#     try:
#         if num == "done":
#             break

#         num = int(num)
#         if largest is None:
#             largest = num
#         elif num > largest:
#             largest = num

#         if smallest is None:
#             smallest = num
#         elif num < smallest:
#             smallest = num
#     except:
#         print("Invalid input")


# print("Maximum is",largest)
# print("Minimum is",smallest)

# def find_smallest_and_largest():
#     largest = None
#     smallest = None

#     while True:
#         num = input("Enter a number: ")

#         try:
#             if num == "done":
#                 break

#             num = int(num)
#             largest = handle_largest(num, largest)
#             largest = handle_smallest(num, smallest)
#         except:
#             print("Invalid input")

#     print("Maximum is ", largest)
#     print("Minimum is ", smallest)


# def handle_largest(num, largest):
#     if largest is None:
#         largest = num
#         return largest
#     elif num > largest:
#         largest = num
#         return largest


# def handle_smallest(num, smallest):
#     if smallest is None:
#         smallest = num
#         return smallest
#     elif num < smallest:
#         smallest = num
#         return smallest


# find_smallest_and_largest()
largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    try:
        if num == "done":
            break
        num = int(num)
    except:
        print("Invalid input")
    else:
        if largest is None or num > largest:
            largest = num

        if smallest is None or num < smallest:
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
