import functools

def log1(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def w1(*args,**kw):
                print('{0}'.format(text))
                func(*args,**kw)
            return w1
    else:
        @functools.wraps(text)
        def w2(*args,**kw):
            print('begin call')
            text(*args,**kw)
            print('end call')
        return w2

    return decorator

def log2(func):
    @functools.wraps(func)
    def w2(*args,**kw):
        print('begin call')
        func(*args,**kw)
        print('end call')
    return w2

def log3(func):
    print('begin call===')
    func()

@log1('test decorator')
def now(text):
    print('{0:.9s}test'.format(text))

@log2
def now2():
    print('===')

@log3
def now3():
    print('-------')

if __name__ == '__main__':
    now('2016')
    f = now2
    f()
    now3
