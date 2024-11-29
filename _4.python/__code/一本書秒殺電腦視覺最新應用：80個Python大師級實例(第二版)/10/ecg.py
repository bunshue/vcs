import matplotlib.pyplot as plt
import pywt
import math
import numpy as np

# plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# 获取数据
ecg = pywt.data.ecg()  # 生成心电信号
index = []
data = []
coffs = []

for i in range(len(ecg) - 1):
    X = float(i)
    Y = float(ecg[i])
    index.append(X)
    data.append(Y)
# 创建小波对象并定义参数
w = pywt.Wavelet("db8")  # 选用Daubechies8小波
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
print("maximum level is" + str(maxlev))
threshold = 0  # 阈值过滤

# 分解成小波分量，到选定的层次:
coffs = pywt.wavedec(data, "db8", level=maxlev)  # 将信号进行小波分解
for i in range(1, len(coffs)):
    coffs[i] = pywt.threshold(coffs[i], threshold * max(coeffs[i]))
datarec = pywt.waverec(coffs, "db8")  # 将信号进行小波重构
mintime = 0
maxtime = mintime + len(data)
print(mintime, maxtime)

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("微伏(uV)")
plt.title("原始信号")
plt.subplot(3, 1, 2)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("微伏(uV)")
plt.title("利用小波技术去噪信号")
plt.subplot(3, 1, 3)
plt.plot(index[mintime:maxtime], data[mintime:maxtime] - datarec[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("误差(uV)")
plt.tight_layout()
plt.show()
