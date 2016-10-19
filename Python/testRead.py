#!/usr/bin/env python3
f = open('test.txt','w+')
f.write('123\n')
f.seek(2)
print(f.read())
f.seek(0)
print(f.read())
#print(f.readline())
#print('===============')
#print(f.readline())
#print('---------------')
#for line in f:
#    print(line,end='')
