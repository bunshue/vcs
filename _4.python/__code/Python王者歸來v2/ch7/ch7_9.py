# ch7_9.py
fruits1 = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
fruits2 = ['香蕉', '芭樂', '西瓜']
print("目前fruits2串列 : ", fruits2)
for fruit in fruits2[:]:
    if fruit in fruits1:
        fruits2.remove(fruit)
        print(f"刪除 {fruit}")
print("最後fruits2串列 : ", fruits2)







