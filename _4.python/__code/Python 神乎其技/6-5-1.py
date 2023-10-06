# 6-5-1 永遠不會停的產生器函式

def repeater(value):
    while True:
        yield value


for item in repeater('Hey'):
    print(item)