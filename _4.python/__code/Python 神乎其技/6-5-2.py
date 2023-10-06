# 6-5-2 能自動打住的產生器函式

def bounded_repeater(value, max_repeats):
    for _ in range(max_repeats):
        yield value


for item in bounded_repeater('Hi', 4):
    print(item)