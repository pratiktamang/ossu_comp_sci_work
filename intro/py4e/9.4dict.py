"""
    9.4 Write a program to read through the mbox-short.txt and
     figure out who has sent the greatest number of mail messages.
     The program looks for 'From ' lines and takes the second word
     of those lines as the person who sent the mail. The program
     creates a Python dictionary that maps the sender's mail address
     to a count of the number of times they appear in the file.
     After the dictionary is produced, the program reads through
     the dictionary using a maximum loop to find the most
     prolific committer.
"""

name = input("Enter file:")
handle = open(name)
res = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        res[email] = res.get(email, 0) + 1

max = None
email = None

# for key in res:
#     if email is None or res[key] > max:
#         email = key
#         max = res[key]

for key, value in res.items():
    if email is None or value > max:
        email = key
        max = value

print(email, max)
