"""
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.

```
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

name = "mbox-short.txt"
handle = open(name)
count_hour = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        count_hour[hour] = count_hour.get(hour, 0) + 1

list_of_tup_hours = count_hour.items()
sorted_list = sorted(list_of_tup_hours)

for key, value in sorted_list:
    print(key, value)
