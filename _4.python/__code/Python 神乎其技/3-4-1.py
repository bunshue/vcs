# 3-4-1 *args 與 **kwargs 選用性與關鍵字參數

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello')

print('')

foo('hello', 1, 2, 3)

print('')

foo('hello', 1, 2, 3, key='value', key2=999)