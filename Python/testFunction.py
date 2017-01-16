#!/usr/bin/env python3
def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end=' ')
#        print(a)
        a,b=b,a+b
    print()
#num = int(input("请输入一个数:"))
#fib(num)
#print('df')
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
