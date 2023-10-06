# 6-4-3 懂得適可而止的走訪器

class BoundedRepeater:
    
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater('Hello', 5)

for item in repeater:
    print(item)
