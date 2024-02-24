# astr = "heelo Bob"
# istr = 0

# try:
#     istr = int(astr)
# except:
#     istr = -1

# print(istr)

# n = 5
# while n > 0:
#     print("count", n)
#     print("Lather")
#     print("Rinse")
#     n = n - 1
# print("Dry off!")

# while True:
#     line = input("enter a line: ")
#     if line == "done":
#         break
#     print(line)
# print("Done!")

# friends = ["Amin", "Ali", "Hassan", "Hossein"]

# for friend in friends:
#     print("Happy New Year:", friend)

# print("Done!")


# largest_so_far = -1
# for number in [9, 41, 12, 3, 74, 15]:
#     if number > largest_so_far:
#         largest_so_far = number
# print("After", largest_so_far)

# all_numbers = [9, 41, 12, 3, 74, 15]
# smallest_num = all_numbers[0]

# for number in all_numbers:
#     if number < smallest_num:
#         smallest_num = number
# print("smallest number", smallest_num)

# smallest = None
# print("Before")

# for number in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = number
#     elif number < smallest:
#         smallest = number
# print("smallest number", smallest)

"""
Capital indexes
Write a function named capital_indexes. The function takes a single parameter,
which is a string.  Your function should return a list of all the indexes in
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

"""

--INPUT-> DO WORK --OUTPUT->

INPUT. single string     : "HeLlO"
OUTPUT. List with index  : 


define function named capital_indexes
it will take single string param.

# initialise index_placholder

loop through each character of the string
    if char is Capital letter, add to indexplace_holder


return index_placholder

HeLlO

    H 0 capital? YES ->  add 0 to index_placholder
    char = H
     char with char.uppper
     H with H
    e 1 capital? NO

    char is e, char.upper() E
    e == E
    L 2 capital? YES  ->  add 2 to index_placholder
    l 3 capital? NO
    O 4 capital? YES  -> add 4 to index_placholder

return the index_placeholder

"""


# def capital_indexes(word):
#     index_placeholder = []

#     for idx, char in enumerate(word):
#         if char == char.upper():
#             index_placeholder.append(idx)

#     print(index_placeholder)


# capital_indexes("amiN")
# capital_indexes("HeLlO")

# cube = 8
# found = False

# for guess in range(abs(cube) +1):
#     print(f"guess: {guess}")
#     if guess **3 >= abs(cube):
#         break
#     if guess **3 != abs(cube):
#         print(cube, "is not a perfect cube")
#     else:
#         if cube < 0:
#             guess = -guess
#         print(f"Cube root of {cube} is {guess}")

# cube = 8
# found = False  # Flag to check if a cube root is found

# for guess in range(abs(cube) + 1):
#     print(f"guess: {guess}")
#     if guess ** 3 == abs(cube):
#         found = True
#         if cube < 0:
#             guess = -guess
#         print(f"Cube root of {cube} is {guess}")
#         break
#     elif guess ** 3 > abs(cube):
#         break

# if not found:
#     print(f"{cube} is not a perfect cube")

# # approximate solution
# cube = 27
# epsilon = 0.001
# guess = 0.0
# increment = 0.01
# num_guesses = 0
# while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
# print("num_guesses =", num_guesses)
# if abs(guess ** 3 - cube) >= epsilon:
#     print("Failed on cube root of", cube)
# else:
#     print(guess, "is close to the cube root of", cube)

# bisection search
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
    print("low =", low, "high =", high, "guess =", guess)
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1

print("num_guesses =", num_guesses)
print(guess, "is close to the cube root of", cube)
