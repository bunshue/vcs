# ch11_37_5.py
str_len = lambda x:len(x)
strs = ['abc', 'ab', 'abcde']
strs.sort(key = str_len)
print(strs)

