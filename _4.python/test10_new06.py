import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

f = [x for x in range(1, 10)]

print(f)

print(sys.getsizeof(f))  # 查看對象佔用內存的字節數

print("------------------------------------------------------------")  # 60個

print("設計一個函數產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。\n")

import random


def generate_code(code_len=4):
    """
    生成指定長度的驗證碼

    :param code_len: 驗證碼的長度(默認4個字符)

    :return: 由大小寫英文字母和數字構成的隨機驗證碼
    """
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code(10))

print("------------------------------------------------------------")  # 60個

print("設計一個函數返回給定文件名的後綴名。\n")


def get_suffix(filename, has_dot=False):
    """
    獲取文件名的後綴名

    :param filename: 文件名
    :param has_dot: 返回的後綴名是否需要帶點
    :return: 文件的後綴名
    """
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print(get_suffix(filename))

print("------------------------------------------------------------")  # 60個

print("計算指定的年月日是這一年的第幾天\n")


def is_leap_year(year):
    """
    判斷指定的年份是不是閏年

    :param year: 年份
    :return: 閏年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    計算傳入的日期是這一年的第幾天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第幾天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))

print("------------------------------------------------------------")  # 60個

import numpy as np

print("二維陣列 6 X 4")
a = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(a[3, 1:4])

print("前2列 之 第2欄之後")
print(a[:2, 2:])

print("第2列 之 全部")
print(a[2, :])

print("全部列 之 第3欄, 轉成row")
print(a[:, 3])

print("全部列 之 偶數欄")
print(a[:, ::2])

print("偶數列 之 036欄")
print(a[::2, ::3])

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", a.sum())
print("直行加:", a.sum(axis=0))
print("橫列加:", a.sum(axis=1))

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", a.min(axis=0))
print("每個直行的最小值對應的索引:", a.argmin(axis=0))
print("每個直行的標準差:", a.std(axis=0))

print("全部平均:", a.mean())
print("直行平均:", a.mean(axis=0))
print("橫列平均:", a.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
a = np.arange(10)
print(a)

print("前4項")
print(a[:4])

print("第3項 至 第7項(不含尾)")
print(a[3:7])

print("第5項 至 最後")
print(a[5:])

print("第3至第9項 跳一個")
print(a[3:9:2])

print("第2項開始至最後, 跳一個")
print(a[2::2])

print("從頭至最後, 跳二個")
print(a[::3])

print("------------------------------------------------------------")  # 60個

print("np亂數建立一維陣列 1 ~ 7(不含尾), 300個")
a = np.random.randint(1, 7, 300)
print(a)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
a = np.random.randint(1, 7, (6, 4))
print(a)

for _ in range(10):
    a = np.random.uniform()
    print(a)


print("------------------------------------------------------------")  # 60個

x = np.random.normal(1,4,(3,5))
x = np.random.normal(1,4,(3,5))
y = np.argmax(x,axis=1)
print(x)
print(x.shape)
print(y)
print(y.shape)
                                                                                                                  
print('查詢函數用法')
help(np.max)

print("------------------------------------------------------------")  # 60個

print("使用 numpy函數 對 list做處理")

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))


print("------------------------------------------------------------")  # 60個

print("用numpy建立資料")
a = np.arange(5)
print(a)
a = np.arange(2,5,1)
print(a)
a = np.linspace(2,5,4)
print(a)
a = np.logspace(0,2,5)
print(a)

a = np.empty(5) # 生成5個元素，值爲隨機數的數組（速度快）
print(a)
a = np.zeros(5) # 生成5個值全爲0的數組
print(a)
a = np.ones(5) # 生成5個值全爲1的數組
print(a)
a = np.full(5, 6) # 生成5個值全爲6的數組
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6], dtype=np.int64)
print(a.dtype) 
a = a.astype(np.float32)
print(a.dtype) 
print(a.dtype.type)


print("------------------------------------------------------------")  # 60個

N = 10
y = np.random.randn(N)

print(y)


print("分段函數")

x=np.arange(10)
print(x)

print(np.where(x<5, x, 9-x))


a=np.arange(10)
print(np.select([x<3,x>6], [-1,1], 0))


a=np.arange(10)
print(np.piecewise(x, [x<3,x>6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------------------------------------")  # 60個

print("統計函數")
a=np.arange(10,0,-1)
print(a)
print(a.mean())
print(a.var())
print(a.std())
print(np.average(a, weights=np.arange(0,10,1)))
print(np.median(a))
print(np.percentile(a, 75))


print(a.min())
print(a.max())
print(a.ptp())
print(a.argmin())
print(a.argmax())
print(a.argsort())
a.sort()
print(a)


a=np.random.randint(0,5,10)
print(a) 
print(np.unique(a)) 
print(np.bincount(a)) 
print(np.histogram(a,bins=5))



print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(type(a))

a = np.mat(np.random.random((2,2)))
print(a)
print(np.eye(2))
print(np.diag([2,3]))

a = np.mat([[1.,2.],[3.,4.]])
print(np.dot(a,a))    # 矩陣乘積
print(np.multiply(a,a))    # 矩陣點乘
print(a.T)   # 矩陣轉置
print(a.I)   # 矩陣求逆
print(np.trace(a))    # 求矩陣的跡
print(np.linalg.eig(a))   # 特徵分解


a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))



print("------------------------------------------------------------")  # 60個

