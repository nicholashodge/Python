import sys

mem = [0] * 8000
MP = 0
index = 0
k = 0
i = 0
prnt = ""

fread = open(sys.argv[1])

fin = open(sys.argv[2])

pgm = fread.read()

pgmlst = list(pgm)

inp = fin.read()

inplst = list(inp)

while i < len(pgmlst):

    if pgmlst[i] == '+':
        mem[MP] = (mem[MP] + 1) % 256

    if pgmlst[i] == '-':
        mem[MP] = (mem[MP] - 1) % 256

    if pgmlst[i] == '>':
        if MP < len(mem):
            MP += 1

    if pgmlst[i] == '<':
        if MP > 0:
            MP -= 1

    if pgmlst[i] == '.':
        prnt += chr(mem[MP])

    if pgmlst[i] == ',':
        mem[MP] = ord(inplst[k])
        k += 1

    if pgmlst[i] == '[':
        if mem[MP] == 0:
            for j in range(len(pgmlst)):
                if pgmlst[j] == ']':
                    i = j
               # else:
                 #   print("**** unmatched braces at PP " + str(i))
                  #  exit(0)
            
    if pgmlst[i] == ']':
        if mem[MP] != 0:
            for j in range(len(pgmlst)):
                if pgmlst[j] == '[':
                    i = j
              #  else:
               #     print("**** unmatched braces at PP " + str(i))
                #    exit(0)
            
            
    index += 1
    i += 1

print(prnt)
