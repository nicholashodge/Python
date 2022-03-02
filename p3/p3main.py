#!/usr/bin/env python3

import sys

import p3mod

gen = p3mod.get_nums()
gen.send(None)   # prime the generator

for rng in sys.argv[1:]:
    print(rng)
    srng = rng.split("-")
    (lo,hi) = (int(srng[0]),int(srng[1]))
    nums = gen.send( (lo,hi) )
    for num in nums:
        print("  ",num)

gen.close()
