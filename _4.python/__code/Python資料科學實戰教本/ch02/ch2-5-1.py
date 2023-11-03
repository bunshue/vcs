ls = [6, 4, 5]    # 建立清單
print(ls, ls[2])  # 顯示 "[6, 4, 5] 5"
print(ls[-1])     # 負索引從最後開始: 顯示 "5"
ls[2] = "py"      # 指定字串型態的項目
print(ls)         # 顯示 "[6, 4, 'py']"
ls.append("bar")  # 新增項目
print(ls)         # 顯示 "[6, 4, 'py', 'bar']"
ele = ls.pop()    # 取出最後項目
print(ele, ls)    # 顯示 "bar [6, 4, 'py']"


