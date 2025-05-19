# ch25_1.py
import numpy as np

data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_10.py

# ch25_10.py
import numpy as np

data = np.arange(16).reshape(2, 2, 2, 2)
print(f"data = \n {data}")
print(f"data = \n {np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11.py

# ch25_11.py
import numpy as np

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.hsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_1.py

# ch25_11_1.py
import numpy as np

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)
print(f"After repeat = \n{x}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_2.py

# ch25_11_2.py
import numpy as np

data = np.array([[1, 2], [3, 4]])
print(f"data = \n {data}")
x1 = np.repeat(data, 3, axis=1)
print(f"After axis=1 repeat  = \n{x1}")
x2 = np.repeat(data, 3, axis=0)
print(f"After axis=0 repeat = \n{x2}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_11_3.py

# ch25_11_3.py
import numpy as np

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)[:, np.newaxis]
print(f"After repeat = \n{x}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_12.py

# ch25_12.py
import cv2
import numpy as np

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_13.py

# ch25_13.py
import cv2
import numpy as np

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")
np.savez("knn_digit.npz", train=train, train_labels=train_labels)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_14.py

# ch25_14.py
import cv2
import numpy as np

# 下載數據
with np.load("knn_digit.npz") as data:
    train = data["train"]
    train_labels = data["train_labels"]
# 讀取數字影像
test_img = cv2.imread("8.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", test_img)
img = cv2.resize(test_img, (20, 20)).reshape((1, 400))
test_data = img.astype(np.float32)  # 將資料轉成foat32
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test_data, k=5)
print(f"識別的數字是 = {int(result[0,0])}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_2.py

# ch25_2.py
import numpy as np

np.random.seed(5)
data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_3.py

# ch25_3.py
import numpy as np

data = np.random.randint(0, 10, size=(5, 1))
print(f"輸出二維陣列 = \n{data}")
print(f"轉成一維陣列 = \n{data.ravel()}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_4.py

# ch25_4.py
import numpy as np

np.random.seed(1)
trains = np.random.randint(0, 10, size=(5, 2))
print(f"列出二維陣列 \n{trains}")
np.random.seed(5)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (5, 1))
print(f"列出顏色分類陣列 \n{labels}")
# 列出 0 代表的紅色
red = trains[labels.ravel() == 0]
print(f"輸出紅色的二維陣列 \n{red}")
print(f"配對取出 \n{red[:,0], red[:,1]}")
# 列出 1 代表的藍色
blue = trains[labels.ravel() == 1]
print(f"輸出藍色的二維陣列 \n{blue}")
print(f"配對取出 \n{blue[:,0], blue[:,1]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_5.py

# ch25_5.py
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
trains = np.random.randint(0, 100, size=(num, 2))
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_6.py

# ch25_6.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
# 建立訓練數據 train, 需轉為 32位元浮點數
trains = np.random.randint(0, 100, size=(num, 2)).astype(np.float32)
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1)).astype(np.float32)
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(10)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_7.py

# ch25_7.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

num = 30  # 數據數量
np.random.seed(5)
# 建立 0 - 50 間的訓練數據 train0, 需轉為 32位元浮點數
train0 = np.random.randint(0, 50, (num // 2, 2)).astype(np.float32)
# 建立 50 - 100 間的訓練數據 train1, 需轉為 32位元浮點數
train1 = np.random.randint(50, 100, (num // 2, 2)).astype(np.float32)
trains = np.vstack((train0, train1))  # 合併訓練數據
# 建立分類, 未來 0 代表 red,  1 代表 blue
label0 = np.zeros((num // 2, 1)).astype(np.float32)
label1 = np.ones((num // 2, 1)).astype(np.float32)
labels = np.vstack((label0, label1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(8)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_8.py

# ch25_8.py
import numpy as np

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch25\ch25_9.py

# ch25_9.py
import numpy as np

data = np.arange(8).reshape(2, 2, 2)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")


print("------------------------------------------------------------")  # 60個
