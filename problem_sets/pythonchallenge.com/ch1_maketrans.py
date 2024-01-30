"""
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
k => m
o => q
e => g

  a
  b
a c
b d
c e
d f
e g
f h
g i
h j
i k
j l
k m
l n
m o
n p
o q
p r
q s
r t
s u
t v
u w
v x
w y
x z
y
z
"


"""
# def translate(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     res = ""

#     for char in s:
#         try:
#             if char in alphabet and char != "y" and char != "z":
#                 idx = alphabet.find(char)
#                 res += alphabet[idx + 2]
#             elif char == "y":
#                 res += "a"
#             elif char == "z":
#                 res += "b"
#             else:
#                 res += char
#         except IndexError:
#             print("IndexError: " + char)
#             res += char
#     return res


# using string.maketrans()

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def translate(str):
    input_str = "abcdefghijklmnopqrstuvwxyz"
    output_str = "cdefghijklmnopqrstuvwxyzab"
    trans_table = str.maketrans(input_str, output_str)

    return str.translate(trans_table)


print(translate(str))
