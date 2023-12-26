# ch11_10_3.py
def is_None(string, x):
    if x is None:
        print(f"{string} = None")
    elif x:
        print(f"{string} = True")
    else:
        print(f"{string} = False")

is_None("空串列", [])                 # 空串列
is_None("空元組", ())                 # 空元組
is_None("空字典", {})                 # 空字典
is_None("空集合", set())              # 空集合
is_None("None  ", None)
is_None("True  ", True)
is_None("False ", False)







