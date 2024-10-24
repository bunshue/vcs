"""

建立資料的寫法


"""


import sys
import numpy as np

print("------------------------------------------------------------")  # 60個

cc = np.arange(-5, 5, 0.1)


MIN = -5
MAX = 5
N = 21
print("從", MIN, "到", MAX, "平均分成", N, "點")
cc = np.linspace(MIN, MAX, N)
print("共", len(cc), "點")
print(cc)

print("------------------------------------------------------------")  # 60個

"""
cc = np.mgrid[0 : 2.0 * np.pi : 20j]
print('共', len(cc), '點')
print(cc)
"""
MIN = -5
MAX = 5
N = 21
print("從", MIN, "到", MAX, "平均分成", N, "點")

cc = np.mgrid[0 : 2.0 * np.pi : 21j]  # 要多一個j => 複數
print("共", len(cc), "點")
print(cc)


cc = np.mgrid[0:10:11j]
print("共", len(cc), "點")
print(cc)


sys.exit()

print("------------------------------------------------------------")  # 60個

print("np.mgrid : mesh-grid")
print("mesh結構")
cc = np.mgrid[0:5, 0:5]
print(cc)
print(cc.shape)

MIN = -5
MAX = 5
N = 21
print("從", MIN, "到", MAX, "平均分成", N, "點")
cc = np.mgrid[MIN:MAX:21j]
print(cc)
print(cc.shape)

cc = np.mgrid[0:4]
print(cc)
print(cc.shape)

print("mesh結構")
cc = np.mgrid[0:4, 0:5, 0:6]
# print(cc)
print(cc.shape)

# (3, 4, 5, 6)


print("------------------------------------------------------------")  # 60個

z = np.linspace(0, 1, 300)
r = np.linspace(0, 1.2, 40)
x = np.linspace(0, 10, 100)
y = np.sin(x)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
