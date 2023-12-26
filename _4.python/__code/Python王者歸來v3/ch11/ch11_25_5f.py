# ch11_25_5f.py
def counter(start=0):
    count = [start]
    def increment():
        count[0] += 1
        return count[0]
    return increment

count_from_5 = counter(5)
print(count_from_5())       # 輸出: 6
print(count_from_5())       # 輸出: 7


