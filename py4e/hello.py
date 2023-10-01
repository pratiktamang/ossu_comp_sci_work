r = 0.016  # Annual interest rate
n = 12  # Compounded monthly

# Initial amount
P_initial = 4000
# Calculating the future value of the initial amount after one year
A_total = P_initial * (1 + r / n) ** n

# Monthly deposits
P_monthly = 2000
# Calculating the future value of each monthly deposit and adding it to the total amount
for i in range(1, 13):  # For each of the next 12 months
    A_total += P_monthly * (1 + r / n) ** (n * (1 - (i - 1) / 12))

print(A_total)


# x = 0.6
# print(f"first value of x: {x}.")
# y = 3.9 * x * (1 - x)
# print(f"second value of x: {y}.")

# function


# def hello(num):
#     if num > 10:
#         print("Hello World!")
#     else:
#         print("Goodbye World!")


# hello(2)
# hello(11)


# def is_pratik(name):
#     return True if name == "Pratik" else False


# match switch case

# def check_house(name):
# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

# loop

# i=3

# while i != 0
#     print("loop number: " i)
#     i++
