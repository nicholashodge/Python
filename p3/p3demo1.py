
def gendemo(n):
    print("starting with", n)
    while n >= 0:
        print('returning',n)
        newvalue = yield n  ## returns n then waits for new value
        print('recvd',newvalue)
        if newvalue != None:
            n = newvalue
        n -= 1


# newvalue in g will always be None for this run
g = gendemo( 4 )
for i in g:
    print('got',i)

print("----------------")

## newvalue in g will get values via send for this run
g = gendemo()
g.send(None)
for i in range(1,6):  # 0 would stop g
    x = g.send(i)
    print('got',x)
