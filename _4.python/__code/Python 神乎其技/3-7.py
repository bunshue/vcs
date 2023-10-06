# 3-7 限制函式參數為位置型 (Python 3.8+) 或關鍵字參數

def foo(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

foo(1, 2, 3, 4, e=5, f=6)
foo(1, 2, c=3, d=4, e=5, f=6)
#foo(a=1, 2, 3, 4, e=5, f=6)
#foo(1, 2, 3, 4, 5, f=6)


data = {'name': 'Dilbert'}

def foo2(name, /, **kwds):
    print(name)
    if kwds:
        print(kwds)

foo2('Bob', **data)