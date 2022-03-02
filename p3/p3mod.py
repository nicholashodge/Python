#Author: Nicholas Hodge
#Due Date: 6/10/21 7:30

#ERROR: when passed second (lo, hi), nums turns into a NoneType in p3main.py

import sys

def get_nums():

    tup = yield

    while 1:

        lst = []
        ret = []

        #recieve the range as a tuple from the .send() function

        #split the tuple into low and high ends of the range
        lo = tup[0]
        hi = tup[1]

        x = lo

        while x < hi + 1:
            total = 0;
            strx = str(x)
            for i in range(len(strx)):
                lst.append(strx[i])
            for j in lst:
                total += int(j) ** int(len(strx))
            if int(total) == int(x):
                ret.append(x)
            lst.clear()
            x += 1

        tup = yield ret
