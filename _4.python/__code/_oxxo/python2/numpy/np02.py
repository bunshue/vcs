import numpy as np

a = np.array([[[1, 2, 3], [5, 6, 7]]])

# 取得陣列維度的深度
print(np.ndim(a))

# 依序取得每個維度的數量
print(np.shape(a))

# 修改維度 1,2,3 -> 1,3,2
a.shape = (1, 3, 2)
print(a)

# 也可以使用 reshape，不過不知道為什麼用了之後執行沒問題，但編輯器會報錯
# b = a.reshape(1,2,3)
# print(b)
