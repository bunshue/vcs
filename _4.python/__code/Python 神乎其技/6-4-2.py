# 6-4-2 __iter__ 與 __next__ 二合一的走訪器

class Repeater:
    
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value


repeater = Repeater('Hello')

for item in repeater:
    print(item)