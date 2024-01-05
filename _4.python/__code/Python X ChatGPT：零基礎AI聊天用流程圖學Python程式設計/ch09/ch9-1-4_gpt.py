str1 = """Python is a programming language that lets you work quickly
and integrate systems more effectively."""

# 將 str1 以空白字元切割成串列 lst1
lst1 = str1.split()

# 顯示 lst1 內容
print(lst1)

# 將 lst1 合併成 CSV 字串 str2
str2 = ",".join(lst1)

# 顯示 str2 內容
print(str2)
