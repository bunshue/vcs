animals = {"cat", "dog", "pig"} # 建立集合
print("cat" in animals)   # 檢查是否有此元素: 顯示 "True"
print("fish" in animals)  # 顯示 "False"
animals.add("fish")       # 新增集合元素
print("fish" in animals)  # 顯示 "True"
print(len(animals))       # 元素數: 顯示 "4"
animals.add("cat")        # 新增存在的元素
print(len(animals))       # 顯示 "4"
animals.remove('cat')     # 刪除集合元素
print(len(animals))       # 顯示 "3"


