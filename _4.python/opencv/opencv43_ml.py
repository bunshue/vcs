"""
OpenCV + ML


"""
print("------------------------------------------------------------")  # 60個

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第1步 準備數據
# A等級的筆試、面試分數
a = np.random.randint(95, 100, (20, 2)).astype(np.float32)
# B等級的筆試、面試分數
b = np.random.randint(90, 95, (20, 2)).astype(np.float32)

# 合并數據
data = np.vstack((a, b))
data = np.array(data, dtype="float32")

# 第2步 建立分組標簽，0代表A等級，1代表B等級
# aLabel對應著a的標簽，為類型0-等級A
aLabel = np.zeros((20, 1))
# bLabel對應著b的標簽，為類型1-等級B
bLabel = np.ones((20, 1))
# 合并標簽
label = np.vstack((aLabel, bLabel))
label = np.array(label, dtype="int32")

# 第3步 訓練
# ml 機器學習模塊 SVM_create() 創建
svm = cv2.ml.SVM_create()
# 屬性設置，直接采用默認值即可。
# svm.setType(cv2.ml.SVM_C_SVC) # svm type
# svm.setKernel(cv2.ml.SVM_LINEAR) # line
# svm.setC(0.01)
# 訓練
result = svm.train(data, cv2.ml.ROW_SAMPLE, label)

# 第4步 預測
# 生成兩個隨機的(筆試成績、面試成績)，可以用隨機數生成
test = np.vstack([[99, 90], [90, 99]])  # 0-A級 1-B級
test = np.array(test, dtype="float32")
# 預測
(p1, p2) = svm.predict(test)

# 第5步 觀察結果
# 可視化
plt.scatter(a[:, 0], a[:, 1], 80, "g", "o")
plt.scatter(b[:, 0], b[:, 1], 80, "b", "s")
plt.scatter(test[:, 0], test[:, 1], 80, "r", "*")
show()

# 打印原始測試數據test，預測結果
print(test)
print(p2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取樣本（特征）圖像的值
s = "data\\images\\"  # 圖像所在路徑
num = 100  # 共有樣本數量
row = 240  # 每個數字圖像的行數
col = 240  # 每個數字圖像的列數
a = np.zeros((num, row, col))  # 用來存儲所有樣本的數值
# print(a.shape)
n = 0  # 用來存儲當前圖像的編號。
for i in range(0, 10):
    for j in range(1, 11):
        a[n, :, :] = cv2.imread(s + str(i) + "\\" + str(i) + "-" + str(j) + ".bmp", 0)
        n = n + 1

# 提取樣本圖像的特征
feature = np.zeros((num, round(row / 5), round(col / 5)))  # 用來存儲所有樣本的特征值
# print(feature.shape)  #看看feature的shape長什么樣子
# print(row)            #看看row的值，有多少個特征（100）個

for ni in range(0, num):
    for nr in range(0, row):
        for nc in range(0, col):
            if a[ni, nr, nc] == 255:
                feature[ni, int(nr / 5), int(nc / 5)] += 1
f = feature  # 簡化變量名稱

#####計算當前待識別圖像的特征值
o = cv2.imread("data\\images\\test\\5.bmp", 0)  # 讀取待測圖像
##讀取圖像值
of = np.zeros((round(row / 5), round(col / 5)))  # 用來存儲測試圖像的特征值
for nr in range(0, row):
    for nc in range(0, col):
        if o[nr, nc] == 255:
            of[int(nr / 5), int(nc / 5)] += 1

###開始計算，數字識別，計算最近的times個數字是誰，判斷結果
d = np.zeros(100)
for i in range(0, 100):
    d[i] = np.sum((of - f[i, :, :]) * (of - f[i, :, :]))
# print(d)
d = d.tolist()
temp = []
Inf = max(d)
# print(Inf)
k = 7
for i in range(k):
    temp.append(d.index(min(d)))
    d[d.index(min(d))] = Inf
# print(temp)   #看看都被識別為哪些特征值了。

temp = [i / 10 for i in temp]
# 也可以返回去，處理為array,使用函數處理，意思差不多。
# temp=np.array(temp)
# temp=np.trunc(temp/10)
# print(temp)
# 數組r用來存儲結果，r[0]表示k近鄰中0的個數，r[n]K近鄰中n的個數
r = np.zeros(10)
for i in temp:
    r[int(i)] += 1
# print(r)
print("當前的數字可能為:" + str(np.argmax(r)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用于訓練的數據
# rand1數據位于(0,30)
rand1 = np.random.randint(0, 30, (20, 2)).astype(np.float32)
# rand2數據位于(70,100)
rand2 = np.random.randint(70, 100, (20, 2)).astype(np.float32)
# 將rand1和rand2拼接為訓練數據
trainData = np.vstack((rand1, rand2))
# 數據標簽，兩類：0,1
# r1Label對應著rand1的標簽，為類型0
r1Label = np.zeros((20, 1)).astype(np.float32)
# r2Label對應著rand2的標簽，為類型1
r2Label = np.ones((20, 1)).astype(np.float32)
tdLable = np.vstack((r1Label, r2Label))
# 使用綠色標注類型0
g = trainData[tdLable.ravel() == 0]
plt.scatter(g[:, 0], g[:, 1], 80, "g", "o")
# 使用藍色標注類型1
b = trainData[tdLable.ravel() == 1]
plt.scatter(b[:, 0], b[:, 1], 80, "b", "s")

show()

# test用于測試的隨機數，該數在0到100之間
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 80, "r", "*")
# 調用OpenCV內的KNN，并訓練
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, tdLable)
# 使用KNN分類
ret, results, neighbours, dist = knn.findNearest(test, 5)
# 顯示處理結果
print("當前隨機數可以判定為類型：", results)
print("距離當前點最近的5個鄰居是：", neighbours)
print("5個最近鄰居的距離: ", dist)
# 可以觀察一下顯示，對比上述輸出

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取樣本（特征）圖像的值
s = "data\\images\\"  # 圖像所在路徑
num = 100  # 共有樣本數量
row = 240  # 每個數字圖像的行數
col = 240  # 每個數字圖像的列數
a = np.zeros((num, row, col))  # 用來存儲所有樣本的數值
# print(a.shape)
n = 0  # 用來存儲當前圖像的編號。
for i in range(0, 10):
    for j in range(1, 11):
        a[n, :, :] = cv2.imread(s + str(i) + "\\" + str(i) + "-" + str(j) + ".bmp", 0)
        n = n + 1

# 提取樣本圖像的特征
feature = np.zeros((num, round(row / 5), round(col / 5)))  # 用來存儲所有樣本的特征值
# print(feature.shape)  #看看feature的shape長什么樣子
# print(row)            #看看row的值，有多少個特征（100）個


for ni in range(0, num):
    for nr in range(0, row):
        for nc in range(0, col):
            if a[ni, nr, nc] == 255:
                feature[ni, int(nr / 5), int(nc / 5)] += 1
f = feature  # 簡化變量名稱
# 將feature處理為單行形式
train = feature[:, :].reshape(-1, round(row / 5) * round(col / 5)).astype(np.float32)
# print(train.shape)
# 貼標簽，需要注意range(0,100)不是range(0,101)
trainLabels = [int(i / 10) for i in range(0, 100)]
trainLabels = np.asarray(trainLabels)
# print(*trainLabels)   #打印測試看看標簽值
##讀取圖像值
o = cv2.imread("data\\images\\test\\5.bmp", 0)  # 讀取待測圖像
of = np.zeros((round(row / 5), round(col / 5)))  # 用來存儲測試圖像的特征值
for nr in range(0, row):
    for nc in range(0, col):
        if o[nr, nc] == 255:
            of[int(nr / 5), int(nc / 5)] += 1

test = of.reshape(-1, round(row / 5) * round(col / 5)).astype(np.float32)
# 調用函數識別
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, trainLabels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
print("當前隨機數可以判定為類型：", result)
print("距離當前點最近的5個鄰居是：", neighbours)
print("5個最近鄰居的距離: ", dist)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 隨機生成兩組數組
# 生成60粒直徑大小在[0,50]之間的xiaoMI
xiaoMI = np.random.randint(0, 50, 60)
# 生成60粒直徑大小在[200,250]之間的daMI
daMI = np.random.randint(200, 250, 60)
# 將xiaoMI和daMI組合為MI
MI = np.hstack((xiaoMI, daMI))
# 使用reshape函數將其轉換為(120,1)
MI = MI.reshape((120, 1))
# 將MI的數據類型轉換為float32
MI = np.float32(MI)
# 調用kmeans模塊
# 設置參數criteria的值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 設置參數flags的值
flags = cv2.KMEANS_RANDOM_CENTERS
# 調用函數kmeans
retval, bestLabels, centers = cv2.kmeans(MI, 2, None, criteria, 10, flags)
"""
#打印返回值
print(retval)
print(bestLabels)
print(centers)
"""
# 獲取分類結果
XM = MI[bestLabels == 0]
DM = MI[bestLabels == 1]
# 繪制分類結果
# 繪制原始數據
plt.plot(XM, "ro")
plt.plot(DM, "bs")
# 繪制中心點
plt.plot(centers[0], "rx")
plt.plot(centers[1], "bx")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 隨機生成兩組數值
# xiaomi組,長和寬的大小都在[0,20]
xiaomi = np.random.randint(0, 20, (30, 2))
# dami組,長和寬的大小都在[40,60]
dami = np.random.randint(40, 60, (30, 2))
# 組合數據
MI = np.vstack((xiaomi, dami))
# 轉換為float32類型
MI = np.float32(MI)
# 調用kmeans模塊
# 設置參數criteria值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 調用kmeans函數
ret, label, center = cv2.kmeans(MI, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
"""
#打印返回值
print(ret)
print(label)
print(center)
"""
# 根據kmeans處理結果，將數據分類，分為XM和DM兩大類
XM = MI[label.ravel() == 0]
DM = MI[label.ravel() == 1]
# 繪制分類結果數據及中心點
plt.scatter(XM[:, 0], XM[:, 1], c="g", marker="s")
plt.scatter(DM[:, 0], DM[:, 1], c="r", marker="o")
plt.scatter(center[0, 0], center[0, 1], s=200, c="b", marker="o")
plt.scatter(center[1, 0], center[1, 1], s=200, c="b", marker="s")
plt.xlabel("Height"), plt.ylabel("Width")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取待處理圖像
img = cv2.imread(filename_lena_gray)
# 使用reshape將一個RGB像素點值的三個值作為一個單元
data = img.reshape((-1, 3))
# 轉換為kmeans可以處理的類型
data = np.float32(data)
# 調用kmeans模塊
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# 轉換為uint8數據類型，將每個像素點值都賦值為當前組的中心點值
# 將center的值轉換為uint8
center = np.uint8(center)
# 使用center內的值替換原有像素點值
res1 = center[label.flatten()]
# 使用reshape調整替換后圖像
res2 = res1.reshape((img.shape))
# 顯示處理結果
plt.subplot(121)
plt.imshow(img)
plt.axis("off")
plt.subplot(122)
plt.imshow(res2)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

num = 30  # 數據數量

# 建立訓練數據 train, 需轉為 32位元浮點數
trains = np.random.randint(0, 100, size=(num, 2)).astype(np.float32)

# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1)).astype(np.float32)

# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小

# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小

# test 為測試數據, 需轉為 32位元浮點數
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

num = 30  # 數據數量

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
digits.png 2000 X 1000 橫100字 直50字 每字 20X20
手寫數字0~9, 每個數字重複寫500次, 共5000個手寫數字
"""
img = cv2.imread("data/digits.png")

cv2.imshow("digits", img)
cv2.waitKey()
cv2.destroyAllWindows()

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

# 儲存模型
np.savez("tmp_knn_digit.npz", train=train, train_labels=train_labels)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取模型
# 下載數據
with np.load("tmp_knn_digit.npz") as data:
    train = data["train"]
    train_labels = data["train_labels"]

# 讀取數字影像
test_img = cv2.imread("data/8.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("img", test_img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.resize(test_img, (20, 20)).reshape((1, 400))
test_data = img.astype(np.float32)  # 將資料轉成foat32

# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test_data, k=5)
print(f"識別的數字是 = {int(result[0,0])}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("SVM 範例")

# Set up training data
## [setup1]
labels = np.array([1, -1, -1, -1])
trainingData = np.matrix(
    [[501, 10], [255, 10], [501, 255], [10, 501]], dtype=np.float32
)
## [setup1]

# Train the SVM
## [init]
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
## [init]
## [train]
svm.train(trainingData, cv2.ml.ROW_SAMPLE, labels)
## [train]

# Data for visual representation
width = 512
height = 512
image = np.zeros((height, width, 3), dtype=np.uint8)

# Show the decision regions given by the SVM
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        sampleMat = np.matrix([[j, i]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]
        if response == 1:
            image[i, j] = GREEN
        elif response == -1:
            image[i, j] = BLUE

# Show the training data
cv2.circle(image, (501, 10), 10, BLACK, -1)
cv2.circle(image, (255, 10), 10, WHITE, -1)
cv2.circle(image, (501, 255), 10, WHITE, -1)
cv2.circle(image, (10, 501), 10, WHITE, -1)

# Show support vectors
## [show_vectors]
thickness = 2
sv = svm.getUncompressedSupportVectors()

""" wrong
for i in range(sv.shape[0]):
    cv2.circle(image, (sv[i,0], sv[i,1]), 6, (128, 128, 128), 10)
## [show_vectors]
"""
# cv2.imwrite("tmp_result.png", image)  # 存圖

cv2.imshow("SVM Simple Example", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
