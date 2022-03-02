#Author: Nicholas Hodge
#Due Date: 5/27/21 7:30
#Project: p1

import sys

total = 0
lst = []
args = sys.argv[1]

#save the length of the integer
length = len(args)

#convert the number into a list of integers
for i in range(length):
    lst.append(args[i])

for x in lst:
    total += int(x) ** int(length)

if int(total) == int(args):
    print(str(args) + " yes")
else:
    print(str(args) + " no")
