import sys, signal, random, math
import multiprocessing as mp

seed = int(sys.argv[1])
numpoint = int(sys.argv[2])
procnum = int(sys.argv[3])

random.seed(seed)

def dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return math.sqrt(x**2 + y**2 + z**2) 

def pcs(a, b, q, lst):
    import signal
    signal.alarm(60)
    mx = 0
    mn = 100
    for i in lst[a:b]:
        for j in lst[a:b]:
            if i != j:
                d = dist(i, j)
                if d > mx:
                    mx = d
                if d < mn:
                    mn = d
    q.put((mn, mx))

points = []
chunks = int(numpoint / procnum)

for i in range(procnum):
    points.append([])
    for j in range(chunks):
        points[i].append((random.random(), random.random(), random.random()))
        

procs = []
q = mp.Queue()

for i in range(procnum):
    lo = i * chunks
    hi = (i + 1) * chunks-1
    p = mp.Process(target=pcs, args=(lo,hi,q,points[i]))
    procs.append(p)

    
for p in procs:
    p.start()

for p in procs:
    p.join()

mn = 100
mx = 0

for p in procs:
    num = q.get()
    if num[0] < mn:
        mn = num[0]
    if num[1] > mx:
        mx = num[1]

print("{:.12f}".format(mn))
print("{:.12f}".format(mx))
