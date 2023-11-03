str1 = 'hello'     # 使用單引號建立字串
str2 = "python"    # 使用雙引號建立字串
print(str1)        # 顯示 "hello"
print(len(str1))   # 字串長度: 顯示 "5"
str3 = str1 + ' ' + str2  # 字串連接
print(str3)        # 顯示 "hello python"
str4 = '%s %s %d' % (str1, str2, 12)  # 格式化字串
print(str4)        # 顯示 "hello python 12"


