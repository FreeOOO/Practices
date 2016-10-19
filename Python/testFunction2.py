#!/usr/bin/env python3
def fib(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b, a + b
    return result

num = int(input("请输入一个数:"))
print(fib(num))
