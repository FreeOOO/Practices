#!/usr/bin/env python3
def ask_ok(prompt, retries = 4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

string = input('请输入一串字符:')
ask_ok(string)
