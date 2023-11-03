# F1750 練習 17

def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys() | second.keys())
 
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
d2 = {'a': 1, 'b': 2, 'd': 4, 'e': 6}
print(dict_diff(d1, d2))
