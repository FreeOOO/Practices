#!/usr/bin/env python3
import math
def avg(num):
    count = 0
    sum_n = 0
    for num_1 in num:
        count = count + 1
        sum_n = sum_n + int(num_1)
    return sum_n/count

def drop_first_last(grades):
#    print(grades)
#    for num in grades:
#        print(num)
    first,*middle,last = grades
    return avg(middle)

if __name__ == "__main__":
    s ring = input("输入一串数字，以分号隔开:")
    string = string.split(',')
    print("去掉首末数字的平均数为:" + str(drop_first_last(string)))

