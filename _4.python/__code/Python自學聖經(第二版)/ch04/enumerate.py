langs={"Python","Java","Kotlin"}
enum_langs=enumerate(langs) # 轉換為 enumerate 物件
print(type(enum_langs))     # <class 'enumerate'>

# 轉成串列
print(list(enum_langs)) # [(0, 'Python'), (1, 'Kotlin'), (2, 'Java')]
# 以迴圈輸出
for item in enumerate(langs):
    print(item)
    
for i,item in enumerate(langs):
    print(i,item)    
