"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  and write a program that prints out all the elements
  of the list that are less than 5.
"""


def list_less_than_five():
    nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    less_than_five = []
    res = []

    for x in nums:
        if x < 5:
            less_than_five.append(x)

    print(f"Numbers less than 5:", less_than_five)

    num = int(input("Less than which number?: "))

    for i in nums:
        if i < num:
            res.append(i)

    print(res)


list_less_than_five()
