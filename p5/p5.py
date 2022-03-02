#Author: Nicholas Hodge
#Due Date: 6/24/21 7:30

import cffi
import sys, random

ffi = cffi.FFI()

#define the C struct and function we need to use
ffi.cdef(
"""
    struct point
    {
        double x;
        double y;
        double z;
    };
    
    double *compute_distances(int numpts, struct point *points);
"""
)

#open the shared object file
lib = ffi.dlopen("./libp5.so")

seed = int(sys.argv[1])
numpoint = int(sys.argv[2])

n = (numpoint * (numpoint-1) )/2

random.seed(seed)

#create points using the structure from the C code
pts = ffi.new("struct point[]", numpoint)

#add the random values to the blank xyz values of the points in the list of structs
for i in range(numpoint):
    pts[i].x = random.random()
    pts[i].y = random.random()
    pts[i].z = random.random()

#create a list of values created by running the imported C function
dists = lib.compute_distances(numpoint, pts)

#unpack the C data to Python readable data
distlist = ffi.unpack(dists, int(numpoint * (numpoint-1)/2))

#find the minimum value in the list
mn = 2.0
for d in distlist:
    if d < mn:
        mn = d

print(f"RMBMIN  {mn:.12f}")
