"""
    6.5 Write code using find() and string slicing (see section 6.10) to
    extract the number at the end of the line below.
    Convert the extracted value to a floating point number and print it out.
"""
text = "X-DSPAM-Confidence:    0.8475"

# number_pos = text.find("0")
# print(float(text[number_pos:]))


# number_pos = None
# for idx, char in enumerate(text):
#     if char.isNumeric():
#         number_pos = idx
#         break
# print(float(text[number_pos:]))

index = None
for char in text:
    if char.isdigit():
        index = text.index(char)
        break

extract_number = text[index:]
print(float(extract_number))
