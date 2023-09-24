# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay should be the normal rate for hours up to 40 and
# time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation. The function should return
# a value. Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). # You should use input to read a
# string and float() # to convert the string to a number.
# Do not worry about error checking the user # input unless you want to
# - you can assume the user types numbers properly. Do not name
# your variable sum or use the sum() function.


# def computepay(h, r):
#     regular_rate = r
#     overtime_rate = 1.5 * regular_rate
#     regular_hours = 40

#     if h <= regular_hours:
#         return regular_hours * regular_rate
#     else:
#         overtime_hours = h - regular_hours
#         regular_pay = regular_hours * regular_rate
#         overtime_pay = overtime_hours * overtime_rate

#         return regular_pay + overtime_pay


# hrs = float(input("Enter Hours:"))
# rate = float(input("Enter rate:"))
# p = computepay(hrs, rate)
# print("Pay", p)


def calculate_regular_pay(hours, rate):
    return hours * rate


def calculate_overtime_pay(overtime_hours, rate):
    overtime_rate = 1.5 * rate
    return overtime_hours * overtime_rate


def compute_total_pay(hours, rate):
    regular_hours = 40
    if hours <= regular_hours:
        return calculate_regular_pay(hours, rate)
    else:
        overtime_hours = hours - regular_hours
        regular_pay = calculate_regular_pay(regular_hours, rate)
        overtime_pay = calculate_overtime_pay(overtime_hours, rate)
        return regular_pay + overtime_pay


hours = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
pay = compute_total_pay(hours, rate)
print(f"Pay: {pay}")
