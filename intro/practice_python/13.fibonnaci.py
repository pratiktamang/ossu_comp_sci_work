"""
Exercise 13 (and Solution)
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence
to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next
number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def gen_fib_sequence():
    while True:
        try:
            qty = int(input("how many fibs should I generate? "))
            break
        except:
            print("ensure to give a number")

    fibs = [1, 1]

    for i in range(1, qty - 1):
        next_num_in_sequence = fibs[i] + fibs[i - 1]
        fibs.append(next_num_in_sequence)

    print(fibs)


gen_fib_sequence()
