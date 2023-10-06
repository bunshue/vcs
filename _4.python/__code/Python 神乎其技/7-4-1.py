# 7-4-1 dict 鍵值的更新陷阱

print({True: '是', 1: '否', 1.0: '也許'})

print(True == 1 == 1.0)