#Author: Nicholas Hodge
#Due Date: 6/10/21 7:30

import sys

def get_nums(t = None):

    while 1:
        t = yield   

        while(t != None):

            lst = []
            ret = []

            #split the tuple into low and high ends of the range
            lo = t[0]
            hi = t[1]

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

            print(ret)
            ret.clear()
            t = None
