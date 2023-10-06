# 3-1-2 函式的一級物件特性: 函式可被放在資料結構裡

def yell(text):
    return text.upper()

bark = yell
funcs = [bark, str.lower, str.capitalize]


print(funcs)

for func in funcs:
    print(func('hey there!'))

print(funcs[0]('hey there!'))