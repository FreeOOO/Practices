#!/usr/bin/env python3
for x in range(1,5):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print()

for x in range(1,7):
    print(repr(x).rjust(2),str(x*x).rjust(3),repr(x*x*x).rjust(4))
