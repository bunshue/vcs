# 計算兩個數的和
def add(x, y):
    return x + y

# 計算一個列表的平均值
def avg(lst):
    return sum(lst) / len(lst)

# 將字串反轉
def reverse_str(s):
    return s[::-1]

# 計算一個字串中指定字符的出現次數
def count_char(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count
