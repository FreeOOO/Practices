#!/usr/bin/env python3
### -*- utf-8 -*- 这一行在python2中需要添加解决中文乱码
"""题目描述

    描述
    Alice writes an English composition with a length of N characters. However, her teacher requires that M illegal pairs of characters cannot be adjacent, and if 'ab' cannot be adjacent, 'ba' cannot be adjacent either.
    In order to meet the requirements, Alice needs to delete some characters.
    Please work out the minimum number of characters that need to be deleted.
    输入
    The first line contains the length of the composition N.
    The second line contains N characters, which make up the composition. Each character belongs to 'a'..'z'.
    The third line contains the number of illegal pairs M.
    Each of the next M lines contains two characters ch1 and ch2,which cannot be adjacent.
    For 20% of the data: 1 ≤ N ≤ 10
    For 50% of the data: 1 ≤ N ≤ 1000
    For 100% of the data: 1 ≤ N ≤ 100000, M ≤ 200.
    输出
    One line with an integer indicating the minimum number of characters that need to be deleted.
    样例提示
    Delete 'a' and 'd'.
    样例输入
    5
    abcde
    3
    ac
    ab
    de
    样例输出
    2
    """
while True:
    try:
        num = int(input())
        string = input()
        numadj = int(input())
        array = []
        for i in range(numadj):
            array.append(input())
        flag = True
        while flag:
            flag = False
            for j in range(1,num):
                str1 = string[j-1:j+1]
                str2 = string[j:j+2]
                bool1,bool2 = False,False
                for k in range(numadj):
                    if array[k] == str1:
                        bool1 = True
                    if array[k] == str2:
                        bool2 = True
                if bool1 == True and bool2 == True:
                    string = string[:j] + string[j+1:]
                    flag = True
        if len(string) > 1:
            str1 = string[0:2]
            str2 = string[len(string)-2:len(string)]
            for k in range(numadj):
                if str1 == array[k]:
                    string = string[1:]
                if str2 == array[k]:
                    string = string[:len(string) - 1]
        flagbo = True
        while flagbo:
            flagbo = False
            for k in range(len(string)-1):
                strtem = string[k:k+2]
                for m in range(numadj):
                    if strtem == array[m]:
                        strte1 = string[k-1:k]+string[k+1:k+2]
                        boolflag = False
                        for n in range(numadj):
                            if strte1 == array[n]:
                                boolflag = True
                        if boolflag:
                            string = string[:k+1] + string[k+2:]
                            flagbo = True
                        else:
                            string = string[:k] + string[k+1:]
                            flagbo = True
        print(num - len(string))
    except EOFError:
        break
