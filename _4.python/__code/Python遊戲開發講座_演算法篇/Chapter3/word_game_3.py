chinese = ["蘋果", "書籍", "貓咪", "狗狗", "雞蛋", "魚", "女孩子"]
english = ["apple", "book", "cat", "dog", "egg", "fish", "girl"]
n = len(chinese)
right = 0
for i in range(n):
    a = input(chinese[i]+"的英文單字是？ ")
    if a==english[i]:
        print("正確解答")
        right = right + 1
    else:
        print("答錯了")
        print("正確解答是"+english[i])
print("遊戲結束")
print("答對的題數", right)
print("答錯的題數", n-right)
