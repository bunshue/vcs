"""

cv2.matchShapes()
cv2.matchTemplate()

模板匹配 Template Matching

"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_shape/shape06.png"

image0 = cv2.imread(filename)  # 彩色讀取

src = image0.copy()

contours, hierarchy = get_image_contours(src)

# 依次繪製輪廓
n = len(contours)  # 輪廓數量
for i in range(n):
    dst = cv2.drawContours(src, contours, i, colors[i], 5)  # 畫第i個輪廓

plt.subplot(211)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(212)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("找出輪廓")
plt.axis("off")

print("------------------------------")  # 30個

print("輪廓和輪廓的比較 cv2.matchShapes()")

cnt0 = contours[3]  # 取得輪廓數據
cnt1 = contours[2]  # 取得輪廓數據
cnt2 = contours[0]  # 取得輪廓數據
cnt3 = contours[1]  # 取得輪廓數據

# 輪廓和輪廓的比較 形狀比較
print("由左到右 天青(3) 藍(2) 紅(0) 綠(1), 以天青(3)為主")
match0 = cv2.matchShapes(cnt0, cnt0, 1, 0)  # 輪廓0和0比較
print("輪廓0和0比較 :", match0)

match1 = cv2.matchShapes(cnt0, cnt1, 1, 0)  # 輪廓0和1比較
print("輪廓0和1比較 :", match1)

match2 = cv2.matchShapes(cnt0, cnt2, 1, 0)  # 輪廓0和2比較
print("輪廓0和2比較 :", match2)

match3 = cv2.matchShapes(cnt0, cnt3, 1, 0)  # 輪廓0和3比較
print("輪廓0和3比較 :", match3)

print("------------------------------")  # 30個

print("輪廓和輪廓的比較 形狀場景運算子")

# 構造距離提取算子
sd = cv2.createShapeContextDistanceExtractor()  # 建立形狀場景運算子

# 計算距離
match0 = sd.computeDistance(cnt0, cnt0)  # 輪廓0和0比較
print("輪廓0和0比較 :", match0)

match1 = sd.computeDistance(cnt0, cnt1)  # 輪廓0和1比較
print("輪廓0和1比較 :", match1)

match2 = sd.computeDistance(cnt0, cnt2)  # 輪廓0和2比較
print("輪廓0和2比較 :", match2)

match3 = sd.computeDistance(cnt0, cnt3)  # 輪廓0和3比較
print("輪廓0和3比較 :", match3)

print("------------------------------")  # 30個

print("輪廓和輪廓的比較 Hausdorff運算子")

# 構造距離提取算子
hd = cv2.createHausdorffDistanceExtractor()  # 建立Hausdorff

# 計算距離
match0 = hd.computeDistance(cnt0, cnt0)  # 輪廓0和0比較
print("輪廓0和0比較 :", match0)

match1 = hd.computeDistance(cnt0, cnt1)  # 輪廓0和1比較
print("輪廓0和1比較 :", match1)

match2 = hd.computeDistance(cnt0, cnt2)  # 輪廓0和2比較
print("輪廓0和2比較 :", match2)

match3 = hd.computeDistance(cnt0, cnt3)  # 輪廓0和3比較
print("輪廓0和3比較 :", match3)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# Opencv之利用matchshape算子实现简单的形状匹配
# 使用OpenCV的matchShape算子进行形状匹配。
# 通过将待识别图像和模板图像转换为灰度并进行阈值处理，然后找到轮廓，
# 最后通过比较轮廓的Hu不变矩来确定匹配度。匹配分值越小，轮廓越相似。
# matchShapes函数适用于识别大物体的形状，但对纹理复杂的图像识别率较低。

# --------------讀取3幅原始圖像--------------------
image1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
image2 = cv2.imread("data/cs2.bmp")  # 彩色讀取
image3 = cv2.imread("data/cc.bmp")  # 彩色讀取

# ----------打印3幅原始圖像的shape屬性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)

# --------------色彩空間轉換--------------------
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# -------------進行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0.0)

# --------------打印差值--------------------
print("相同圖像的matchShape=", ret0)
print("相似圖像的matchShape=", ret1)
print("不相似圖像的matchShape=", ret2)

# --------------顯示3幅原始圖像--------------------
plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("original1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("original2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("original3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 輪廓比對")

img_patterns = cv2.imread("data/patterns.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

patterns, _ = cv2.findContours(img_patterns, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_targets = cv2.imread("data/targets.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

targets, _ = cv2.findContours(img_targets, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

patterns = [pattern - np.min(pattern, 0, keepdims=True) for pattern in patterns]
targets = [target - np.min(target, 0, keepdims=True) for target in targets]

# approxPolyDP 輪廓近似
patterns_simple = [cv2.approxPolyDP(pattern, 5, True) for pattern in patterns]

# approxPolyDP 輪廓近似
targets_simple = [cv2.approxPolyDP(target, 8, True) for target in targets]

for method in [1, 2, 3]:
    method_str = "CONTOURS_MATCH_I{}".format(method)
    method = getattr(cv2, method_str)
    scores = [
        cv2.matchShapes(targets_simple[0], patterns_simple[pidx], method, 0)
        for pidx in range(5)
    ]
    print(method_str, ", ".join("{: 8.4f}".format(score) for score in scores))

# CV_CONTOURS_MATCH_I1  11.3737,   0.3456,   0.0289,   1.0495,   0.0020
# CV_CONTOURS_MATCH_I2   4.8051,   2.2220,   0.0179,   0.3624,   0.0013
# CV_CONTOURS_MATCH_I3   0.9164,   0.4778,   0.0225,   0.4552,   0.0016

# %figonly=使用`matchShapes()`比較由`approxPolyDP()`近似之後的輪廓
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect("equal")

width = 180
for tidx, (target, target_simple) in enumerate(zip(targets, targets_simple)):
    scores = []
    texts = []
    for pidx, (pattern, pattern_simple) in enumerate(zip(patterns, patterns_simple)):
        index = np.s_[:, 0, :]
        pattern2 = pattern[index]
        target2 = target[index]
        pattern_simple2 = pattern_simple[index]
        target_simple2 = target_simple[index]

        x0 = pidx * width + width
        y0 = tidx * width + width

        if tidx == 0:
            pattern_poly = plt.Polygon(pattern2 + [x0, 0], color="black", alpha=0.6)
            ax.add_patch(pattern_poly)
            text = ax.text(x0 + width * 0.3, -50, str(pidx), fontsize=14, ha="center")
        if pidx == 0:
            target_poly = plt.Polygon(target2 + [0, y0], color="g", alpha=0.6)
            ax.add_patch(target_poly)
            text = ax.text(-50, y0 + width * 0.3, str(tidx), fontsize=14, ha="center")

        pattern_simple_poly = plt.Polygon(
            pattern_simple2 + [x0, 0], facecolor="none", alpha=0.6
        )
        ax.add_patch(pattern_simple_poly)
        target_simple_poly = plt.Polygon(
            target_simple2 + [0, y0], facecolor="none", alpha=0.6
        )
        ax.add_patch(target_simple_poly)

        score = cv2.matchShapes(target_simple, pattern_simple, cv2.CONTOURS_MATCH_I3, 0)
        text = ax.text(
            x0 + width * 0.3,
            y0 + width * 0.2,
            "{:5.4f}".format(score),
            ha="center",
            va="center",
            fontsize=16,
        )
        scores.append(score)
        texts.append(text)
    best_index = np.argmin(scores)
    texts[best_index].set_color("red")

ax.relim()
ax.set_axis_off()
ax.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


filename1 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46.jpg"
filename2 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46_head.jpg"

src = cv2.imread(filename1, cv2.IMREAD_COLOR)

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
# plt.axis("off")

template = cv2.imread(filename2, cv2.IMREAD_COLOR)
height, width = template.shape[:2]  # 獲得模板影像的高與寬

# 使用 cv2.TM_SQDIFF_NORMED 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, GREEN, 3)  # 繪置最相似外框
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

plt.subplot(312)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
# plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = []  # 建立原始影像陣列

src1 = cv2.imread("data/matchTemplate/tennis1.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列

src2 = cv2.imread("data/matchTemplate/tennis2.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列

src3 = cv2.imread("data/matchTemplate/tennis3.jpg", cv2.IMREAD_COLOR)
src.append(src3)  # 加入原始影像串列

template = cv2.imread("data/matchTemplate/tennis0.jpg", cv2.IMREAD_COLOR)

# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
minValue = 1  # 設定預設的最小值
index = -1  # 設定最小值的索引
# 採用歸一化平方匹配法
for i in range(len(src)):
    result = cv2.matchTemplate(src[i], template, cv2.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # print(i, minVal, maxVal, minLoc, maxLoc, "\t比較小", minVal)
    print("圖 :", i, "值 :", minVal)
    if minValue > minVal:
        minValue = minVal  # 紀錄目前的最小值
        index = i  # 紀錄目前的索引

seq = "tennis" + str(index) + ".jpg"
print(f"{seq} 比較類似")

plt.subplot(221)
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))
plt.title("src1")
# plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))
plt.title("src2")
# plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))
plt.title("src3")
# plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/Angry-Birds01.jpg"
)
filename_small = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"

src = cv2.imread(filename_big, cv2.IMREAD_COLOR)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("src")
# plt.axis("off")

template = cv2.imread(filename_small, cv2.IMREAD_COLOR)

height, width = template.shape[:2]  # 獲得模板影像的高與寬

# 使用 cv2.TM_CCOEFF_NORMED 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.85:  # 值大於0.95就算找到了
            dst = cv2.rectangle(src, (col, row), (col + width, row + height), RED, 3)

plt.subplot(132)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
# plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/Angry-Birds01.jpg"
)
filename_small = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"


def myMatch(image, tmp):
    # 執行匹配
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("data/matchTemplate/mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像

temps = []
template = cv2.imread("data/matchTemplate/heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(template)  # 加入匹配串列temps

temp2 = cv2.imread("data/matchTemplate/star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp2)  # 加入匹配串列temps

match = []  # 符合匹配的圖案
for t in temps:
    myMatch(src, t)  # 調用 myMatch

for img in match:
    dst = cv2.rectangle(src, (img[0]), (img[1]), GREEN, 1)  # 繪外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = "data/matchTemplate/tmrt_map.jpg"
filename_small = "data/matchTemplate/tmrt_logo1.jpg"

start_x = 1250  # 目前位置 x
start_y = 560  # 目前位置 y
src = cv2.imread(filename_big, cv2.IMREAD_COLOR)

template = cv2.imread(filename_small, cv2.IMREAD_COLOR)

dst = cv2.circle(src, (start_x, start_y), 10, BLUE, -1)  # 實心圓

h, w = template.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), RED, 2)  # 空心長方形
            ul_x.append(col)  # 加入最佳匹配串列 x
            ul_y.append(row)  # 加入最佳匹配串列 y

print("共找到 :", len(ul_x), "個捷運站")

length = len(ul_x)
for i in range(length):
    sub_x = start_x - ul_x[i]  # 計算 x 座標差距
    sub_y = start_y - ul_y[i]  # 計算 y 座標差距
    distance = math.hypot(sub_x, sub_y)  # 計算距離
    print(f"目前位置到此捷運站的距離 = {distance:8.2f}")
    cv2.line(src, (start_x, start_y), (ul_x[i], ul_y[i]), colors[i], 2)

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("附近的捷運站")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 05")

image = cv2.imread(filename_lena_gray, 0)

image2 = image.copy()

template = cv2.imread("images/temp.bmp", 0)

th, tw = template.shape[::]
image = image2.copy()
rv = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

# 矩形之左上點
topLeft = minLoc
# 矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(image, topLeft, bottomRight, 255, 2)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(rv, cmap="gray")
plt.title("Matching Result")

plt.subplot(122)
plt.imshow(image, cmap="gray")
plt.title("Detected Point")

plt.suptitle("Matching Result 1")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 06")

image = cv2.imread(filename_lena_gray, 0)

image2 = image.copy()

template = cv2.imread("images/temp.bmp", 0)

tw, th = template.shape[::-1]
image = image2.copy()
rv = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

# 矩形之左上點
topLeft = maxLoc
# 矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(image, topLeft, bottomRight, 255, 2)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(rv, cmap="gray")
plt.title("Matching Result")

plt.subplot(122)
plt.imshow(image, cmap="gray")
plt.title("Detected Point")

plt.suptitle("Matching Result 2")
show()

print("------------------------------------------------------------")  # 60個

print("opencv 07")

image = cv2.imread("images/lena4.bmp", 0)

template = cv2.imread("images/lena4Temp.bmp", 0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), 255, 1)

plt.figure(figsize=(12, 8))

plt.imshow(image, cmap="gray")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 90")

img = cv2.resize(cv2.imread("images/soccer_practice.jpg", 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread("images/shoe.PNG", 0), (0, 0), fx=0.8, fy=0.8)
print(img.shape)
print(template.shape)
h, w = template.shape

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
]

for method in methods:
    print("matchTemplate, method = ", method)
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cvshow("Match", img2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Multi_objective_matching.py

# opencv模板匹配----多目标匹配

linewidth = 3

# 读取目标图片
target = cv2.imread("data/matchTemplate/lena_target.jpg")

# 读取模板图片
template = cv2.imread("data/matchTemplate/lena_template.jpg")

# 获得模板图片的高宽尺寸
theight, twidth = template.shape[:2]
# 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
# 归一化处理
# 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

"""
绘制矩形边框，将匹配区域标注出来
min_loc：矩形定点
min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
(0,0,225)：矩形的边框颜色；2：矩形边框宽度
"""
cv2.rectangle(
    target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2
)

# 匹配值转换为字符串
# 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
# 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
strmin_val = str(min_val)
# 初始化位置参数
temp_loc = min_loc
other_loc = min_loc
numOfloc = 1
# 第一次筛选----规定匹配阈值，将满足阈值的从result中提取出来
# 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法设置匹配阈值为0.01
threshold = 0.01
loc = np.where(result < threshold)
# 遍历提取出来的位置
for other_loc in zip(*loc[::-1]):
    # 第二次筛选----将位置偏移小于5个像素的结果舍去
    if (temp_loc[0] + 5 < other_loc[0]) or (temp_loc[1] + 5 < other_loc[1]):
        numOfloc = numOfloc + 1
        temp_loc = other_loc
        cv2.rectangle(
            target,
            other_loc,
            (other_loc[0] + twidth, other_loc[1] + theight),
            (0, 0, 225),
            2,
        )
str_numOfloc = str(numOfloc)

# 显示结果,并将匹配值显示在标题栏上
strText = (
    "MatchResult----MatchingValue="
    + strmin_val
    + "----NumberOfPosition="
    + str_numOfloc
)

print("匹配值 :", strmin_val)

cv2.imshow(strText, target)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Single_target_matching.py

# opencv模板匹配----单目标匹配

linewidth = 3

# 读取目标图片
target = cv2.imread("data/matchTemplate/lena_target.jpg")

# 读取模板图片
template = cv2.imread("data/matchTemplate/lena_template.jpg")

# 获得模板图片的高宽尺寸
theight, twidth = template.shape[:2]
# 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
# 归一化处理
cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
# 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# 匹配值转换为字符串
# 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
# 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
strmin_val = str(min_val)

# 绘制矩形边框，将匹配区域标注出来
# min_loc：矩形定点
# (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高

cv2.rectangle(
    target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), RED, linewidth
)

# 显示结果,并将匹配值显示在标题栏上
strText = "MatchResult----MatchingValue=" + strmin_val

print("匹配值 :", strmin_val)

cv2.imshow(strText, target)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


"""
# 使用 cv2.TM_SQDIFF 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

"""
