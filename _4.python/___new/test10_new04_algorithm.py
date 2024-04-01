"""
演算法_最強彩色圖鑑_Python程式實作_王者歸來(第二版)


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個
'''
btree = [0] * 16
print(type(btree))
print(btree)

print("------------------------------------------------------------")  # 60個


def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length - 1):
        print("第 %d 次外圈排序" % (i + 1))
        for j in range(length - 1 - i):
            if nLst[j] > nLst[j + 1]:
                nLst[j], nLst[j + 1] = nLst[j + 1], nLst[j]
            print("第 %d 次內圈排序 : " % (j + 1), nLst)
    return nLst


data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))


print("------------------------------------------------------------")  # 60個

def merge(left, right):
    #兩數列合併
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output


def merge_sort(nLst):
    #合併排序
    if len(nLst) <= 1:  # 剩下一個或0個元素直接返回
        return nLst
    mid = len(nLst) // 2  # 取中間索引
    # 切割(divide)數列
    left = nLst[:mid]  # 取左半段
    right = nLst[mid:]  # 取右半段
    # 處理左序列和右邊序列
    left = merge_sort(left)  # 左邊排序
    right = merge_sort(right)  # 右邊排序
    # 遞迴執行合併
    return merge(left, right)  # 傳回合併


data = [6, 1, 5, 7, 3, 9, 4]
print("原始串列 : ", data)
print("排序結果 : ", merge_sort(data))


print("------------------------------------------------------------")  # 60個

cars = ["honda", "bmw", "toyota", "ford"]
print("目前串列內容 = ", cars)
print("使用sort( )由小排到大")
cars.sort()
print("排序串列結果 = ", cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ", nums)
print("使用sort( )由小排到大")
nums.sort()
print("排序串列結果 = ", nums)

print("------------------------------------------------------------")  # 60個

cars = ["honda", "bmw", "toyota", "ford"]
print("目前串列內容 = ", cars)
print("使用sort( )由大排到小")
cars.sort(reverse=True)
print("排序串列結果 = ", cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ", nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)
print("排序串列結果 = ", nums)

print("------------------------------------------------------------")  # 60個

def cocktail_sort(nLst):
    #雞尾酒排序
    n = len(nLst)
    is_sorted = True
    start = 0  # 前端索引
    end = n - 1  # 末端索引
    while is_sorted:
        is_sorted = False  # 重置是否排序完成
        for i in range(start, end):  # 往右比較
            if nLst[i] > nLst[i + 1]:
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i]
                is_sorted = True
        print("往後排序過程 : ", nLst)
        if not is_sorted:  # 如果沒有交換就結束
            break

        end = end - 1  # 末端索引左移一個索引
        for i in range(end - 1, start - 1, -1):  # 往左比較
            if nLst[i] > nLst[i + 1]:
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i]
                is_sorted = True
        start = start + 1  # 前端索引右移一個索引
        print("往前排序過程 : ", nLst)
    return nLst


data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", cocktail_sort(data))

print("------------------------------------------------------------")  # 60個


def selection_sort(nLst):
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
        print("第 %d 次迴圈排序" % (i + 1), nLst)
    return nLst


data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", selection_sort(data))

print("------------------------------------------------------------")  # 60個

def selection_sort(nLst):
    #選擇排序
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


cars = ["honda", "bmw", "toyota", "ford"]
print("目前串列內容 = ", cars)
print("使用selection_sort( )由小排到大")
selection_sort(cars)
print("排序串列結果 = ", cars)


print("------------------------------------------------------------")  # 60個


def selection_sort(nLst):
    #選擇排序
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][2] < nLst[j][2]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


music = [
    ("李宗盛", "山丘", 24740000),
    ("趙傳", "我是一隻小小鳥", 8310000),
    ("五佰", "挪威的森林", 34130000),
    ("林憶蓮", "聽說愛情回來過", 12710000),
]

print("YouTube點播排行")
selection_sort(music)
for i in range(len(music)):
    print("{}:{}{} -- 點播次數 {}".format(i + 1, music[i][0], music[i][1], music[i][2]))

print("------------------------------------------------------------")  # 60個


def insertion_sort(nLst):
    #插入排序
    n = len(nLst)
    if n == 1:  # 只有1筆資料
        print("第 %d 次迴圈排序" % n, nLst)
        return nLst
    print("第 1 次迴圈排序", nLst)
    for i in range(1, n):  # 迴圈
        for j in range(i, 0, -1):
            if nLst[j] < nLst[j - 1]:
                nLst[j], nLst[j - 1] = nLst[j - 1], nLst[j]
            else:
                break
        print("第 %d 次迴圈排序" % (i + 1), nLst)
    return nLst


data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", insertion_sort(data))

print("------------------------------------------------------------")  # 60個


def sequential_search(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:  # 找到了
            return i  # 傳回索引值
    return -1  # 找不到傳回-1


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]

print("請輸入搜尋值 : ")
# key = eval(input("請輸入搜尋值 : "))
key = 5
index = sequential_search(data)
if index != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (index, (index + 1)))
else:
    print("查無此搜尋號碼")

print("------------------------------------------------------------")  # 60個


def binary_search(nLst):
    print("列印搜尋串列 : ", nLst)
    low = 0  # 串列的最小索引
    high = len(nLst) - 1  # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0  # 搜尋次數
    while True:
        times += 1
        if key == nLst[middle]:  # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1  # 下一次往右邊搜尋
        else:
            high = middle - 1  # 下依次往左邊搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:  # 所有元素比較結束
            rtn = -1
            break
    return rtn, times


data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sorted_data = sorted(data)  # 排序串列
# key = int(input("請輸入搜尋值 : "))
key = 62
index, times = binary_search(sorted_data)
if index != -1:
    print("在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")

print("------------------------------------------------------------")  # 60個

product_list = {}  # 產品列表的字典
product_list["Refrigerator"] = 8000
product_list["Television"] = 12000
product_list["Printer"] = 8000
print("列印產品資料")
print(product_list)
print("列印 Refrigerator : ", product_list["Refrigerator"])
print("列印 Television   : ", product_list["Television"])
print("列印 Printer      : ", product_list["Printer"])

print("------------------------------------------------------------")  # 60個

phone_book = {}  # 通訊簿的字典
phone_book["Trump"] = "0912111111"
phone_book["Lisa"] = "0922222222"
phone_book["Mike"] = "0932333333"
# name = input('請輸入名字 : ')
name = "Trump"
if name in phone_book:
    print("{} 的電話號碼是 {}".format(name, phone_book[name]))
else:
    print("{} 不在通訊簿內 ".format(name))

print("------------------------------------------------------------")  # 60個


def check_name(name):
    if voted[name]:
        print("你已經投過票了")
    else:
        print("歡迎投票")
        voted[name] = True


voted = {"Trump": None, "Lisa": None, "Mike": None}

# name = input('請輸入名字 : ')

name = "Trump"
if name in voted:
    check_name(name)
else:
    print("你不是選民")

print("------------------------------------------------------------")  # 60個

from pprint import pprint

maze = [  # 迷宮地圖
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
]
directions = [  # 使用串列設計走迷宮方向
    lambda x, y: (x - 1, y),  # 往上走
    lambda x, y: (x + 1, y),  # 往下走
    lambda x, y: (x, y - 1),  # 往左走
    lambda x, y: (x, y + 1),  # 往右走
]


def maze_solve(x, y, goal_x, goal_y):
    #解迷宮程式 x, y是迷宮入口, goal_x, goal_y是迷宮出口
    maze[x][y] = 2
    stack = []  # 建立路徑堆疊
    stack.append((x, y))  # 將路徑push入堆疊
    print("迷宮開始")
    while len(stack) > 0:
        cur = stack[-1]  # 目前位置
        if cur[0] == goal_x and cur[1] == goal_y:
            print("抵達出口")
            return True  # 抵達出口返回True
        for dir in directions:  # 依上, 下, 左, 右優先次序走此迷宮
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:  # 如果是通道可以走
                stack.append(next)
                maze[next[0]][next[1]] = 2  # 用2標記走過的路
                break
        else:  # 如果進入死路, 則回溯
            maze[cur[0]][cur[1]] = 3  # 標記死路
            stack.pop()  # 回溯
    else:
        print("沒有路徑")
        return False


maze_solve(1, 1, 4, 4)
pprint(maze)  # 跳行顯示元素

print("------------------------------------------------------------")  # 60個


from pprint import pprint

maze = [  # 迷宮地圖
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
directions = [  # 使用串列設計走迷宮方向
    lambda x, y: (x - 1, y),  # 往上走
    lambda x, y: (x + 1, y),  # 往下走
    lambda x, y: (x, y - 1),  # 往左走
    lambda x, y: (x, y + 1),  # 往右走
]


def maze_solve(x, y, goal_x, goal_y):
    #解迷宮程式 x, y是迷宮入口, goal_x, goal_y是迷宮出口
    maze[x][y] = 2
    stack = []  # 建立路徑堆疊
    stack.append((x, y))  # 將路徑push入堆疊
    print("迷宮開始")
    while len(stack) > 0:
        cur = stack[-1]  # 目前位置
        if cur[0] == goal_x and cur[1] == goal_y:
            print("抵達出口")
            return True  # 抵達出口返回True
        for dir in directions:  # 依上, 下, 左, 右優先次序走此迷宮
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:  # 如果是通道可以走
                stack.append(next)
                maze[next[0]][next[1]] = 2  # 用2標記走過的路
                break
        else:  # 如果進入死路, 則回溯
            maze[cur[0]][cur[1]] = 3  # 標記死路
            stack.pop()  # 回溯
    else:
        print("沒有路徑")
        return False


maze_solve(1, 1, 8, 2)
pprint(maze)  # 跳行顯示元素

print("------------------------------------------------------------")  # 60個


def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])


data = [6, 1, 5]
print("mysum = ", mysum(data))


print("------------------------------------------------------------")  # 60個

def fib(i):
    #計算 Fibonacci number
    if i == 0:  # 定義 0
        return 0
    elif i == 1:  # 定義 1
        return 1
    else:  # 執行遞迴計算
        return fib(i - 1) + fib(i - 2)

print("Fibonacci number : 10")

n = 10
for i in range(n + 1):
    print("n = {},   Fib({}) = {}".format(i, i, fib(i)))

print("------------------------------------------------------------")  # 60個

def hanoi(n, src, aux, dst):
    global step
    # 河內塔
    if n == 1:  # 河內塔終止條件
        step += 1  # 紀錄步驟
        print("{0:2d} : 移動圓盤 {1} 從 {2} 到 {3}".format(step, n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        step += 1  # 紀錄步驟
        print("{0:2d} : 移動圓盤 {1} 從 {2} 到 {3}".format(step, n, src, dst))
        hanoi(n - 1, aux, src, dst)


step = 0
print("河內塔 圓盤數量 = 7")
n = 7
hanoi(n, "A", "B", "C")


print("------------------------------------------------------------")  # 60個

def hanoi(n, src, aux, dst):
    # 河內塔
    if n == 1:  # 河內塔終止條件
        print("移動圓盤 {} 從 {} 到 {}".format(n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        print("移動圓盤 {} 從 {} 到 {}".format(n, src, dst))
        hanoi(n - 1, aux, src, dst)


print("河內塔 圓盤數量 = 7")
n = 7
hanoi(n, "A", "B", "C")

print("------------------------------------------------------------")  # 60個

def is_OK(row, col):
    # 檢查是否可以放在此row, col位置
    for i in range(1, row + 1):  # 迴圈往前檢查是否衝突
        if (
            queens[row - i] == col  # 檢查欄
            or queens[row - i] == col - i  # 檢查左上角斜線
            or queens[row - i] == col + i
        ):  # 檢查右上角斜線
            return False  # 傳回有衝突, 不可使用
    return True  # 傳回可以使用


def location(row):
    # 搜尋特定row的col欄位
    start = queens[row] + 1  # 也許是回溯,所以start不一定是0
    for col in range(start, SIZE):
        if is_OK(row, col):
            return col  # 暫時可以在(row,col)放置皇后
    return -1  # 沒有適合位置所以回傳 -1


def solve():
    # 從特定row列開始找尋皇后的位置
    row = 0
    while row >= 0 and row <= 7:
        col = location(row)
        if col < 0:  # 如果回傳是 -1, 必須回溯前一列
            queens[row] = -1
            row -= 1  # 設定row少1, 可以回溯前一列
        else:
            queens[row] = col  # 第row列皇后位置是col
            row += 1  # 往下一列
    if row == -1:
        return False  # 沒有解答
    else:
        return True  # 找到解答


SIZE = 8  # 棋盤大小
queens = [-1] * SIZE  # 預設皇后位置
solve()  # 解此題目
for i in range(SIZE):  # 繪製結果圖
    for j in range(SIZE):
        if queens[i] == j:
            print("Q", end="")
        else:
            print("1", end="")
    print()


print("------------------------------------------------------------")  # 60個

class Queens:
    def __init__(self):
        self.queens = size * [-1]  # 預設皇后位置
        self.solve(0)  # 從row = 0 開始搜尋
        for i in range(size):  # 繪製結果圖
            for j in range(size):
                if self.queens[i] == j:
                    print("Q", end="")
                else:
                    print("1", end="")
            print()

    def is_OK(self, row, col):
        # 檢查是否可以放在此row, col位置
        for i in range(1, row + 1):  # 迴圈往前檢查是否衝突
            if (
                self.queens[row - i] == col  # 檢查欄
                or self.queens[row - i] == col - i  # 檢查左上角斜線
                or self.queens[row - i] == col + i
            ):  # 檢查右上角斜線
                return False  # 傳回有衝突, 不可使用
        return True  # 傳回可以使用

    def solve(self, row):
        # 從第 row 列開始找尋皇后的位置
        if row == size:  # 終止搜尋條件
            return True
        for col in range(size):
            self.queens[row] = col  # 安置(row, col)
            if self.is_OK(row, col) and self.solve(row + 1):
                return True  # 找到並返回
        return False  # 表示此row沒有解答


size = 8  # 棋盤大小
Queens()

print("------------------------------------------------------------")  # 60個

from collections import deque

graph = {}  # 建立空字典
graph["Tom"] = ["Ivan", "Ira", "Kevin"]  # 建立字典graph, key='Tom'的值
people = deque()  # 建立queue
people += graph["Tom"]  # 將graph字典Tom鍵的值加入people
print("列出people資料類型 : ", type(people))
print("列出搜尋名單       : ", people)
for name in range(len(people)):
    print(people.popleft())


print("------------------------------------------------------------")  # 60個

def dfs(graph, node, path=[]):
    # 深度優先搜尋法
    path += [node]  # 路徑
    for n in graph[node]:  # 將相鄰節點放入佇列
        if n not in path:
            path = dfs(graph, n, path)
    return path


graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G", "H"],
    "E": ["B"],
    "F": ["C", "I", "J"],
    "G": ["D"],
    "H": ["D"],
    "I": ["F"],
    "J": ["F"],
}
print(dfs(graph, "A"))


print("------------------------------------------------------------")  # 60個

from collections import deque

graph = {}  # 建立空字典
graph["Tom"] = ["Ivan", "Ira", "Kevin"]  # 建立字典graph, key='Tom'的值
people = deque()  # 建立queue
people += graph["Tom"]  # 將graph字典Tom鍵的值加入people
print("列出people資料類型 : ", type(people))
print("列出搜尋名單       : ", people)
for name in range(len(people)):
    print(people.pop())


print("------------------------------------------------------------")  # 60個

from collections import deque

people = deque()  # 建立queue
people.append("Ivan")  # 右邊加入
people.append("Ira")  # 右邊加入
print("列出名單 : ", people)
people.appendleft("Unistar")  # 右邊加入
print("列出名單 : ", people)
people.appendleft("Ice Rain")  # 右邊加入
print("列出名單 : ", people)

print("------------------------------------------------------------")  # 60個

from collections import deque


def banana_dealer(name):
    # 回應是不是賣香蕉的經銷商
    if name == "Banana":
        return True


def search(name):
    # 搜尋賣香蕉的朋友
    global not_dealer  # 儲存已搜尋的名單
    dealer = deque()
    dealer += graph[name]  # 搜尋串列先儲存Tom的朋友
    while dealer:
        person = dealer.popleft()  # 從左邊取資料
        if banana_dealer(person):  # 如果是True, 表示找到了
            print(person + " 是香蕉經銷商 ")
            return True  # search()執行結束
        else:
            not_dealer.append(person)  # 將搜尋過的人儲存至串列
            dealer += graph[person]  # 將不是經銷商的朋友加入搜尋串列
    print("沒有找到經銷商")
    return False


not_dealer = []
graph = {}  # 建立空字典
graph["Tom"] = ["Ivan", "Ira", "Kevin"]  # 建立字典graph, key='Tom'的值
graph["Ivan"] = ["Peter"]  # 建立字典graph, key='Ivan'的值
graph["Ira"] = ["Banana"]  # 建立字典graph, key='Ira'的值
graph["Kevin"] = ["Mary"]  # 建立字典graph, key='Mary'的值
graph["Peter"] = []  # 沒有其他朋友用空集合
graph["Banana"] = []  # 沒有其他朋友用空集合
graph["Mary"] = []  # 沒有其他朋友用空集合

search("Tom")
print("列出已搜尋名單 : ", not_dealer)

print("------------------------------------------------------------")  # 60個

def banana_dealer(name):
    # 回應是不是賣香蕉的經銷商
    if name == "Banana":
        return True


def search(name):
    # 搜尋賣香蕉的朋友
    global not_dealer  # 儲存已搜尋的名單
    dealer = []
    dealer += graph[name]  # 搜尋串列先儲存Tom的朋友
    while dealer:
        person = dealer.pop(0)  # 從左邊取資料
        if banana_dealer(person):  # 如果是True, 表示找到了
            print(person + " 是香蕉經銷商 ")
            return True  # search()執行結束
        else:
            not_dealer.append(person)  # 將搜尋過的人儲存至串列
            dealer += graph[person]  # 將不是經銷商的朋友加入搜尋串列
    print("沒有找到經銷商")
    return False


not_dealer = []
graph = {
    "Tom": ["Ivan", "Ira", "Kevin"],
    "Ivan": ["Peter"],
    "Ira": ["Banana"],
    "Kevin": ["Mary"],
    "Peter": [],
    "Banana": [],
    "Mary": [],
}

search("Tom")
print("列出已搜尋名單 : ", not_dealer)


print("------------------------------------------------------------")  # 60個

def bfs(graph, start):
    # 寬度優先搜尋法
    visited = []  # 拜訪過的頂點
    queue = [start]  # 模擬佇列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        visited.append(node)  # 加入已拜訪行列
        neighbors = graph[node]  # 取得已拜訪節點的相鄰節點
        for n in neighbors:  # 將相鄰節點放入佇列
            queue.append(n)
    return visited


graph = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F"],
    "D": ["G", "H"],
    "E": [],
    "F": ["I", "J"],
    "G": [],
    "H": [],
    "I": [],
    "J": [],
}
print(bfs(graph, "A"))


print("------------------------------------------------------------")  # 60個


def bfs(graph, start):
    # 寬度優先搜尋法
    visited = []  # 拜訪過的頂點
    queue = [start]  # 模擬佇列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        if node not in visited:
            visited.append(node)  # 加入已拜訪行列
            neighbors = graph[node]  # 取得已拜訪節點的相鄰節點
            for n in neighbors:  # 將相鄰節點放入佇列
                queue.append(n)
    return visited


graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G", "H"],
    "E": ["B"],
    "F": ["C", "I", "J"],
    "G": ["D"],
    "H": ["D"],
    "I": ["F"],
    "J": ["F"],
}
print(bfs(graph, "A"))


print("------------------------------------------------------------")  # 60個

def is_exit(node):
    # 回應是否出口
    if node == "K":
        return True


def bfs(graph, start):
    # 寬度優先搜尋法
    global visited  # 拜訪過的頂點
    queue = [start]  # 模擬佇列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        if is_exit(node):  # 如果是True, 表示找到了
            print(node + " 是迷宮出口 ")
            return visited  # bfs()執行結束
        if node not in visited:
            visited.append(node)  # 加入已拜訪行列
            neighbors = graph[node]  # 取得已拜訪節點的相鄰節點
            for n in neighbors:  # 將相鄰節點放入佇列
                queue.append(n)
    return visited


graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["C"],
    "E": ["C", "H"],
    "F": ["G"],
    "G": ["F", "H"],
    "H": ["E", "G", "I"],
    "I": ["H", "K"],
    "J": ["G"],
    "K": ["I"],
}
visited = []
print(bfs(graph, "A"))


print("------------------------------------------------------------")  # 60個

def dfs(graph, start, goal):
    # 深度優先搜尋法
    path = []  # 拜訪過的節點
    stack = [start]  # 模擬堆疊
    while stack:
        node = stack.pop()  # pop堆疊
        path.append(node)  # 加入已拜訪行列
        if node == goal:  # 如果找到了
            print("找到了")
            return path
        for n in graph[node]:  # 將相鄰節點放入佇列
            stack.append(n)
    return "找不到"


graph = {
    "A": ["D", "C", "B"],
    "B": ["E"],
    "C": ["F"],
    "D": ["H", "G"],
    "E": [],
    "F": ["J", "I"],
    "G": [],
    "H": [],
    "I": [],
    "J": [],
}
print(dfs(graph, "A", "G"))

print("------------------------------------------------------------")  # 60個

def dijkstra(graph, start):
    visited = []
    index = start
    nodes = dict((i, INF) for i in graph)  # 設定節點為最大值
    nodes[start] = 0  # 設定起點為start

    while len(visited) < len(graph):  # 有幾個節點就執行幾次
        visited.append(index)
        for i in graph[index]:
            new_cost = nodes[index] + graph[index][i]  # 新路徑距離
            if new_cost < nodes[i]:  # 新路徑如果比較短
                nodes[i] = new_cost  # 採用新路徑

        next = INF
        for n in nodes:  # 從串列中找出下一個節點
            if n in visited:  # 如果已拜訪回到for選下一個
                continue
            if nodes[n] < next:  # 找出新的最小權重節點
                next = nodes[n]
                index = n
    return nodes


INF = 9999
graph = {
    "A": {"A": 0, "B": 2, "C": 4},
    "B": {"B": 0, "C": 7, "E": 6},
    "C": {"C": 0, "D": 6, "E": 2},
    "D": {"D": 0, "E": 8, "G": 4},
    "E": {"E": 0, "G": 2},
    "G": {"G": 0},
}
rtn = dijkstra(graph, "A")
print(rtn)


print("------------------------------------------------------------")  # 60個

def get_edges(graph):
    # 建立邊線資訊
    n1 = []  # 線段的節點1
    n2 = []  # 線段的節點2
    weight = []  # 定義線段權重串列
    for i in graph:  # 為每一個線段建立兩端的節點串列
        for j in graph[i]:
            if graph[i][j] != 0:
                weight.append(graph[i][j])
                n1.append(i)
                n2.append(j)
    return n1, n2, weight


def bellman_ford(graph, start):
    n1, n2, weight = get_edges(graph)
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0
    for times in range(len(graph) - 1):  # 執行迴圈len(graph)-1次
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]  # 新的路徑花費
            if new_cost < nodes[n2[i]]:  # 新路徑如果比較短
                nodes[n2[i]] = new_cost  # 採用新路徑
                cycle = 1
        if cycle == 0:  # 如果沒有更改結束for迴圈
            break
    flag = 0
    # 下一個迴圈是檢查是否存在負權重的迴圈
    for i in range(len(nodes)):  # 對每條邊線在執行一次鬆弛操作
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:  # 如果有變化表示有負權重的迴圈
        return "圖形含負權重的迴圈"
    return nodes


INF = 999
graph = {
    "A": {"A": 0, "B": 2, "C": 4},
    "B": {"B": 0, "C": 7, "E": 6},
    "C": {"C": 0, "D": 6, "E": 2},
    "D": {"D": 0, "E": 8, "G": 4},
    "E": {"E": 0, "G": 2},
    "G": {"G": 0},
}

rtn = bellman_ford(graph, "A")
print(rtn)

print("------------------------------------------------------------")  # 60個

def get_edges(graph):
    # 建立邊線資訊
    n1 = []  # 線段的節點1
    n2 = []  # 線段的節點2
    weight = []  # 定義線段權重串列
    for i in graph:  # 為每一個線段建立兩端的節點串列
        for j in graph[i]:
            if graph[i][j] != 0:
                weight.append(graph[i][j])
                n1.append(i)
                n2.append(j)
    return n1, n2, weight


def bellman_ford(graph, start):
    n1, n2, weight = get_edges(graph)
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0
    for times in range(len(graph) - 1):  # 執行迴圈len(graph)-1次
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]  # 新的路徑花費
            if new_cost < nodes[n2[i]]:  # 新路徑如果比較短
                nodes[n2[i]] = new_cost  # 採用新路徑
                cycle = 1
        if cycle == 0:  # 如果沒有更改結束for迴圈
            break
    flag = 0
    # 下一個迴圈是檢查是否存在負權重的迴圈
    for i in range(len(nodes)):  # 對每條邊線在執行一次鬆弛操作
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:  # 如果有變化表示有負權重的迴圈
        return "圖形含負權重的迴圈"
    return nodes


INF = 999
graph = {
    "A": {"A": 0, "B": -1, "C": 4},
    "B": {"B": 0, "C": 3, "D": 2, "E": 2},
    "C": {"C": 0},
    "D": {"D": 0, "B": 1, "C": 5, "G": 4},
    "E": {"E": 0, "D": -3, "E": 2},
    "G": {"G": 0},
}

rtn = bellman_ford(graph, "A")
print(rtn)


print("------------------------------------------------------------")  # 60個

def get_edges(graph):
    # 建立邊線資訊
    n1 = []  # 線段的節點1
    n2 = []  # 線段的節點2
    weight = []  # 定義線段權重串列
    for i in graph:  # 為每一個線段建立兩端的節點串列
        for j in graph[i]:
            if graph[i][j] != 0:
                weight.append(graph[i][j])
                n1.append(i)
                n2.append(j)
    return n1, n2, weight


def bellman_ford(graph, start):
    n1, n2, weight = get_edges(graph)
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0
    for times in range(len(graph) - 1):  # 執行迴圈len(graph)-1次
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]  # 新的路徑花費
            if new_cost < nodes[n2[i]]:  # 新路徑如果比較短
                nodes[n2[i]] = new_cost  # 採用新路徑
                cycle = 1
        if cycle == 0:  # 如果沒有更改結束for迴圈
            break
    flag = 0
    # 下一個迴圈是檢查是否存在負權重的迴圈
    for i in range(len(nodes)):  # 對每條邊線在執行一次鬆弛操作
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:  # 如果有變化表示有負權重的迴圈
        return "圖形含負權重的迴圈"
    return nodes


INF = 999
graph = {
    "A": {"A": 0, "B": -1, "C": 4},
    "B": {"B": 0, "C": 3, "D": 2, "E": 2},
    "C": {"C": 0},
    "D": {"D": 0, "B": -4, "C": 5, "G": 4},
    "E": {"E": 0, "D": -3, "E": 2},
    "G": {"G": 0},
}

rtn = bellman_ford(graph, "A")
print(rtn)

print("------------------------------------------------------------")  # 60個

def greedy(course):
    # 課程的貪婪演算法
    length = len(course)  # 課程數量
    course_list = []  # 儲存結果
    course_list.append(course[0])  # 第一節課
    course_end_time = course_list[0][1][1]  # 第一節課下課時間
    for i in range(1, length):  # 貪婪選課
        if course[i][1][0] >= course_end_time:  # 上課時間晚於或等於
            course_list.append(course[i])  # 加入貪婪選課
            course_end_time = course[i][1][1]  # 新的下課時間
    return course_list


course = {
    "化學": (12, 13),  # 定義課程時間
    "英文": (9, 11),
    "數學": (8, 10),
    "計概": (10, 12),
    "物理": (11, 13),
}

cs = sorted(course.items(), key=lambda item: item[1][1])  # 課程時間排序
print("所有課程依下課時間排序如下")
print("課程", "   開始時間 ", " 下課時間")
for i in range(len(cs)):
    print("{0}{1:7d}:00{2:8d}:00".format(cs[i][0], cs[i][1][0], cs[i][1][1]))

s = greedy(cs)  # 呼叫貪婪選課
print("貪婪排課時間如下")
print("課程", "   開始時間 ", " 下課時間")
for i in range(len(s)):
    print("{0}{1:7d}:00{2:8d}:00".format(s[i][0], s[i][1][0], s[i][1][1]))


print("------------------------------------------------------------")  # 60個

def greedy(things):
    # 商品貪婪演算法
    length = len(things)  # 商品數量
    things_list = []  # 儲存結果
    things_list.append(things[length - 1])  # 第一個商品
    weights = things[length - 1][1][1]
    for i in range(length - 1, -1, -1):  # 貪婪選商品
        if things[i][1][1] + weights <= max_weight:  # 所選商品可放入背包
            things_list.append(things[i])  # 加入貪婪背包
            weights += things[i][1][1]  # 新的背包重量
    return things_list


things = {
    "iWatch手錶": (15000, 0.1),  # 定義商品
    "Asus  筆電": (35000, 0.7),
    "iPhone手機": (38000, 0.3),
    "Acer  筆電": (40000, 0.8),
    "Go Pro攝影": (12000, 0.1),
}

max_weight = 1
th = sorted(things.items(), key=lambda item: item[1][0])  # 商品依價值排序
print("所有商品依價值排序如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(th)):
    print("{0:8s}{1:10d}{2:10.2f}".format(th[i][0], th[i][1][0], th[i][1][1]))

t = greedy(th)  # 呼叫貪婪選商品
print("貪婪選擇商品如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(t)):
    print("{0:8s}{1:10d}{2:10.2f}".format(t[i][0], t[i][1][0], t[i][1][1]))

print("------------------------------------------------------------")  # 60個


def greedy(radios, cities):
    # 貪婪演算法
    greedy_radios = set()  # 最終電台的選擇
    while cities:  # 還有城市沒有覆蓋迴圈繼續
        greedy_choose = None  # 最初化選擇
        city_cover = set()  # 暫存
        for radio, area in radios.items():  # 檢查每一個電台
            cover = cities & area  # 選擇可以覆蓋城市
            if len(cover) > len(city_cover):  # 如果可以覆蓋更多則取代
                greedy_choose = radio  # 目前所選電台
                city_cover = cover
        cities -= city_cover  # 將被覆蓋城市從集合刪除
        greedy_radios.add(greedy_choose)  # 將所選電台加入
    return greedy_radios  # 傳回電台


cities = set(["台北", "基隆", "桃園", "新竹", "台中", "嘉義", "台南", "高雄"])  # 期待廣播覆蓋區域

radios = {}
radios["電台 1"] = set(["新竹", "台中", "嘉義"])
radios["電台 2"] = set(["基隆", "新竹", "台北"])
radios["電台 3"] = set(["桃園", "台中", "台南"])
radios["電台 4"] = set(["台中", "嘉義"])
radios["電台 5"] = set(["台南", "高雄"])

print(greedy(radios, cities))  # 電台, 城市

print("------------------------------------------------------------")  # 60個

def greedy(graph, cities, start):
    # 貪婪演算法計算業務員旅行
    visited = []  # 儲存已拜訪城市
    visited.append(start)  # 儲存起點城市
    start_i = cities.index(start)  # 獲得起點城市的索引
    distance = 0  # 旅行距離
    for outer in range(len(cities) - 1):  # 尋找最近城市
        graph[start_i][start_i] = INF  # 將自己城市距離設為極大值
        min_dist = min(graph[start_i])  # 找出最短路徑
        distance += min_dist  # 更新總路程距離
        end_i = graph[start_i].index(min_dist)  # 最短距離城市的索引
        visited.append(cities[end_i])  # 將最短距離城市列入已拜訪
        for inner in range(len(graph)):  # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = INF
            graph[inner][start_i] = INF
        start_i = end_i  # 將下一個城市改為新的起點
    return distance, visited

print('貪婪演算法計算業務員旅行1, 從新竹出發')

INF = 9999  # 距離極大值
cities = ["新竹", "竹南", "竹北", "關西", "竹東"]
graph = [
    [0, 12, 10, 28, 16],
    [12, 0, 20, 35, 19],
    [10, 20, 0, 21, 11],
    [28, 35, 21, 0, 12],
    [16, 19, 11, 12, 0],
]
dist, visited = greedy(graph, cities, "新竹")
print("拜訪順序 : ", visited)
print("拜訪距離 : ", dist)

print('貪婪演算法計算業務員旅行1, 從關西出發')

INF = 9999  # 距離極大值
cities = ["新竹", "竹南", "竹北", "關西", "竹東"]
graph = [
    [0, 12, 10, 28, 16],
    [12, 0, 20, 35, 19],
    [10, 20, 0, 21, 11],
    [28, 35, 21, 0, 12],
    [16, 19, 11, 12, 0],
]
dist, visited = greedy(graph, cities, "關西")
print("拜訪順序 : ", visited)
print("拜訪距離 : ", dist)

print("------------------------------------------------------------")  # 60個


def subset_generator(data):
    # 子集合生成函數, data須是可迭代物件
    final_subset = [[]]  # 空集合也算是子集合
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset


data = ["a", "b", "c"]
subset = subset_generator(data)
for s in subset:
    print(s)

print("------------------------------------------------------------")  # 60個

def subset_generator(data):
    final_subset = [[]]  # 空集合也算是子集合
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset


data = ["電視", "音響", "筆電"]
value = [40000, 50000, 20000]
weight = [3, 4, 1]
bags = subset_generator(data)
max_value = 0  # 商品總值
for bag in bags:  # 處理組合商品
    if bag:  # 如果不是空集合
        w_sum = 0  # 組合商品總重量
        v_sum = 0  # 組合商品總價值
        for b in bag:  # 拆解商品
            i = data.index(b)  # 了解商品在data的索引
            w_sum += weight[i]  # 加總商品數量
            v_sum += value[i]  # 加總商品價值
            if w_sum <= 4:  # 如果商品總重量小於4公斤
                if v_sum > max_value:  # 如果總價值大於目前最大價值
                    max_value = v_sum  # 更新最大價值
                    product = bag  # 紀錄商品

print("商品組合 = {},\n商品價值 = {}".format(product, max_value))

print("------------------------------------------------------------")  # 60個

def knapsack(W, wt, val):
    # 動態規劃演算法
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格row
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                table[r][c] = max(
                    val[r - 1] + table[r - 1][c - wt[r - 1]], table[r - 1][c]
                )
            else:
                table[r][c] = table[r - 1][c]
    return table[n][W]


value = [20000, 50000, 40000, 25000]  # 商品價值
weight = [1, 4, 3, 1]  # 商品重量
bag_weight = 4  # 背包可容重量
print("商品價值 : ", knapsack(bag_weight, weight, value))


print("------------------------------------------------------------")  # 60個

def traveling(W, wt, val):
    # 動態規劃演算法
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格row
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                table[r][c] = max(
                    val[r - 1] + table[r - 1][c - wt[r - 1]], table[r - 1][c]
                )
            else:
                table[r][c] = table[r - 1][c]
    return table[n][W]


value = [7, 6, 9, 9, 8]  # 旅遊點評分數
weight = [1, 1, 2, 4, 1]  # 單項景點所需天數
travel_weight = 4  # 總旅遊天數
print("旅遊點評總分 = ", traveling(travel_weight, weight, value))

print("------------------------------------------------------------")  # 60個

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

print("摩斯密碼 請輸入大寫英文字")
wd = "TAIWAN"
for c in wd:
    print(morse_code[c])

print("------------------------------------------------------------")  # 60個

abc = "abcdefghijklmnopqrstuvwxyz"
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

#msgTest = input("請輸入原始字串 : ")
print("請輸入原始字串 : ")
msgTest = "america"

cipher = []
for i in msgTest:  # 執行每個字元加密
    v = encry_dict[i]  # 加密
    cipher.append(v)  # 加密結果
ciphertext = "".join(cipher)  # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)


print("------------------------------------------------------------")  # 60個

import string

def encrypt(text, encryDict):  # 加密文件
    cipher = []
    for i in text:  # 執行每個字元加密
        v = encryDict[i]  # 加密
        cipher.append(v)  # 加密結果
    return "".join(cipher)  # 將串列轉成字串


abc = string.printable[:-5]  # 取消不可列印字元
subText = abc[-3:] + abc[:-3]  # 加密字串
encry_dict = dict(zip(subText, abc))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

msg = "If the implementation is easy to explain, it may be a good idea."
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

'''
print("------------------------------------------------------------")  # 60個

import math

film = [5, 7, 8, 10, 2]  # 玩命關頭特徵值
film_titles = [  # 比較影片片名
    "復仇者聯盟",
    "決戰中途島",
    "冰雪奇緣",
    "雙子殺手",
]
film_features = [  # 比較影片特徵值
    [2, 8, 8, 5, 6],
    [5, 6, 9, 2, 5],
    [8, 2, 0, 0, 10],
    [5, 8, 8, 8, 3],
]

dist = []  # 儲存影片相似度值
for f in film_features:
    distances = 0
    for i in range(len(f)):
        distances += (film[i] - f[i]) ** 2
    dist.append(math.sqrt(distances))

min = min(dist)  # 求最小值
min_index = dist.index(min)  # 最小值的索引

print("與玩命關頭最相似的電影 : ", film_titles[min_index])
print("相似度值 : ", dist[min_index])
for i in range(len(dist)):
    print("影片 : %s, 相似度 : %6.2f" % (film_titles[i], dist[i]))

print("------------------------------------------------------------")  # 60個

import math

""" fail
def knn(record, target, k):
    # 計算k組近鄰值, 以list回傳數量和距離
    distances = []  # 儲存紀錄與目標的距離
    record_number = []  # 儲存紀錄的烤香腸數量

    for r in record:  # 計算過往紀錄與目標的距離
        tmp = 0
        for i in range(len(target) - 1):
            tmp += (target[i] - r[i]) ** 2
        dist = math.sqrt(tmp)
        distances.append(dist)  # 儲存距離
        record_number.append(r[len(target) - 1])  # 儲存烤香腸數量

    knn_number = []  # 儲存k組烤香腸數量
    knn_distances = []  # 儲存k組距離值
    for i in range(k):  # k代表取k組近鄰值
        min_value = min(distances)  # 計算最小值
        min_index = distances.index(min_value)  # 計算最小值索引
        # 將香腸數量分別儲存至knn_number串列
        knn_number.append(record_number.pop(min_index))
        # 將距離分別儲存至knn_distances
        knn_distances.append(distances.pop(min_index))
    return knn_number, knn_distances


def regression(knn_num):
    # 計算迴歸值
    return int(sum(knn_num) / len(knn_num))


target = [1, 5, 2, "value"]  # value是需計算的值
# 過往紀錄
record = [
    [0, 3, 3, 100],
    [2, 4, 3, 250],
    [2, 5, 6, 350],
    [1, 4, 2, 180],
    [2, 3, 1, 170],
    [1, 5, 4, 300],
    [0, 1, 1, 50],
    [2, 4, 3, 275],
    [2, 2, 4, 230],
    [1, 3, 5, 165],
    [1, 5, 5, 320],
    [2, 5, 1, 210],
]

k = 5  # 設定k組最相鄰的值
k_nn = knn(record, target, k)
print("需準備 %d 條烤香腸" % regression(k_nn[0]))
for i in range(k):
    print("k組近鄰的距離 %6.4f, 銷售數量 %d" % (k_nn[1][i], k_nn[0][i]))
"""
print("------------------------------------------------------------")  # 60個

def isPrime(num):
    # 測試num是否質數
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print("請輸入大於1的整數做質數測試 = 12347")

num = 12347
if isPrime(num):
    print("%d是質數" % num)
else:
    print("%d不是質數" % num)


print("------------------------------------------------------------")  # 60個

def rob(nums):
    prev = cur = 0
    for money in nums:
        prev, cur = cur, max(prev + money, cur)
    return cur


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))

print("------------------------------------------------------------")  # 60個

""" fail
def minCost(costs):
    red, blue, green = 0, 0, 0
    for r, b, g in costs:
        red, blue, green = r + min(blue, green), b + min(red, green), g + min(red, blue)
    return min(red, blue, green)


print(minCost([[17, 2, 14], [15, 16, 5], [14, 3, 18]]))
"""

print("------------------------------------------------------------")  # 60個

def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:  # 1根籬笆的刷法
        return k
    same = k  # 2根相同顏色刷法
    diff = k * (k - 1)  # 2根不相同顏色刷法
    for i in range(3, n + 1):  # 3根籬笆以上的刷法
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff  # 回傳總計


print(numWays(1, 2))
print(numWays(2, 2))
print(numWays(3, 2))
print(numWays(4, 2))

print("------------------------------------------------------------")  # 60個

from collections import deque


def palindrome(word):
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True


print("x      是回文 : ", palindrome("x"))
print("abccba 是回文 : ", palindrome("abccba"))
print("radar  是回文 : ", palindrome("radar"))
print("python 是回文 : ", palindrome("python"))


print("------------------------------------------------------------")  # 60個

chicken = 0
while True:
    rabbit = 35 - chicken  # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:  # 腳的總數
        print("雞有 {} 隻, 兔有 {} 隻".format(chicken, rabbit))
        break
    chicken += 1


print("------------------------------------------------------------")  # 60個

h = eval(input("請輸入頭的數量 : "))
f = eval(input("請輸入腳的數量 : "))
chicken = f / 2 - h
rabbit = 2 * h - f / 2
print("雞有 {} 隻, 兔有 {} 隻".format(int(chicken), int(rabbit)))


print("------------------------------------------------------------")  # 60個

def gold(W, wt, val):
    # 動態規劃演算法
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格row
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                table[r][c] = max(
                    val[r - 1] + table[r - 1][c - wt[r - 1]], table[r - 1][c]
                )
            else:
                table[r][c] = table[r - 1][c]
    return table[n][W]


value = [10, 16, 20, 22, 25]  # 金礦產值
weight = [3, 4, 3, 5, 5]  # 單項金礦所需人力
gold_weight = 10  # 總人力
print("最大產值 = {} 公斤".format(gold(gold_weight, weight, value)))


print("------------------------------------------------------------")  # 60個

def climbStairs(n):
    prev, cur = 1, 1
    for i in range(1, n):
        prev, cur = cur, prev + cur
    return cur


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))


print("------------------------------------------------------------")  # 60個


def factorial(n):
    # 計算n的階乘, n 必須是正整數
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 20
times = 0.0000000001 * factorial(n)
print("排列組合需要 %d 秒" % times)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


def sequentialSearch(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:  # 找到了
            return i  # 傳回索引值
    return -1  # 找不到傳回-1


nameLst = []
while True:
    name = input("請輸入姓名(Q或q代表輸入結束) : ")
    if name == "Q" or name == "q":
        break
    nameLst.append(name)

key = input("請輸入搜尋姓名 : ")
rtn = sequentialSearch(nameLst)
if rtn != -1:
    print("在索引 %d 位置找到了 %s 共找了 %d 次" % (rtn, key, (rtn + 1)))
else:
    print("查無此搜尋姓名")


print("------------------------------------------------------------")  # 60個

from pprint import pprint

maze = [  # 迷宮地圖
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
directions = [  # 使用串列設計走迷宮方向
    lambda x, y: (x - 1, y),  # 往上走
    lambda x, y: (x + 1, y),  # 往下走
    lambda x, y: (x, y - 1),  # 往左走
    lambda x, y: (x, y + 1),  # 往右走
]


def maze_solve(x, y, goal_x, goal_y):
    # 解迷宮程式 x, y是迷宮入口, goal_x, goal_y是迷宮出口
    maze[x][y] = 2
    stack = []  # 建立路徑堆疊
    stack.append((x, y))  # 將路徑push入堆疊
    print("迷宮開始")
    while len(stack) > 0:
        cur = stack[-1]  # 目前位置
        if cur[0] == goal_x and cur[1] == goal_y:
            print("抵達出口")
            return True  # 抵達出口返回True
        for dir in directions:  # 依上, 下, 左, 右優先次序走此迷宮
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:  # 如果是通道可以走
                stack.append(next)
                maze[next[0]][next[1]] = 2  # 用2標記走過的路
                break
        else:  # 如果進入死路, 則回溯
            maze[cur[0]][cur[1]] = 3  # 標記死路
            stack.pop()  # 回溯
    else:
        print("沒有路徑")
        return False


print("迷宮圖形如下 : ")
pprint(maze)
entry_x, entry_y = eval(input("請輸入迷宮入口 x, y : "))
exit_x, exit_y = eval(input("請輸入迷宮出口 x, y : "))
maze_solve(entry_x, entry_y, exit_x, exit_y)
pprint(maze)  # 跳行顯示元素


print("------------------------------------------------------------")  # 60個

def mymax(nLst):
    if len(nLst) == 2:
        return nLst[0] if nLst[0] > nLst[1] else nLst[1]
    tmp_max = mymax(nLst[1:])
    return nLst[0] if nLst[0] > tmp_max else tmp_max


data = [1, 5, 9, 2, 8, 100, 81]
print("data         = ", data)
print("data的最大值 = ", mymax(data))


print("------------------------------------------------------------")  # 60個


def dfs(graph, start, goal):
    # 深度優先搜尋法
    path = []  # 拜訪過的節點
    stack = [start]  # 模擬堆疊
    while stack:
        node = stack.pop()  # pop堆疊
        if node in path:
            continue
        path.append(node)  # 加入已拜訪行列
        if node == goal:  # 如果找到了
            print("找到了")
            return path
        for n in graph[node]:  # 將相鄰節點放入佇列
            stack.append(n)
    return "找不到"


graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G", "H"],
    "E": ["B"],
    "F": ["C", "I", "J"],
    "G": ["D"],
    "H": ["D"],
    "I": ["F"],
    "J": ["F"],
}
print(dfs(graph, "F", "G"))

print("------------------------------------------------------------")  # 60個

def dijkstra(graph, start):
    visited = []
    index = start
    nodes = dict((k, INF) for k in graph)  # 設定節點為最大值
    nodes[start] = 0  # 設定起點為start

    while len(visited) < len(graph):  # 有幾個節點就執行幾次
        visited.append(index)
        for i in graph[index]:
            new_cost = nodes[index] + graph[index][i]  # 新路徑距離
            if new_cost < nodes[i]:  # 新路徑如果比較短
                nodes[i] = new_cost  # 採用新路徑

        next = INF
        for n in nodes:  # 從串列中找出下一個節點
            if n in visited:  # 如果已拜訪回到for選下一個
                continue
            if nodes[n] < next:  # 找出新的最小權重節點
                next = nodes[n]
                index = n
    return nodes


INF = 9999
graph = {
    "A": {"A": 0, "B": 2, "C": 4},
    "B": {"B": 0, "A": 2, "C": 7, "E": 6},
    "C": {"C": 0, "A": 4, "D": 6, "E": 2},
    "D": {"D": 0, "C": 6, "E": 8, "G": 4},
    "E": {"E": 0, "B": 6, "C": 2, "D": 8, "G": 2},
    "G": {"G": 0, "D": 4, "E": 2},
}
node = input("請輸入起點 : ")
rtn = dijkstra(graph, node)
print(rtn)

print("------------------------------------------------------------")  # 60個

def greedy(things):
    # 商品貪婪演算法
    length = len(things)  # 商品數量
    things_list = []  # 儲存結果
    things_list.append(things[length - 1])  # 第一個商品
    weights = things[length - 1][1][1]
    for i in range(length - 1, -1, -1):  # 貪婪選商品
        if things[i][1][1] + weights <= max_weight:  # 所選商品可放入背包
            things_list.append(things[i])  # 加入貪婪背包
            weights += things[i][1][1]  # 新的背包重量
    return things_list


things = {
    "iWatch手錶": (15000, 0.1),  # 定義商品
    "Asus  筆電": (35000, 0.7),
    "iPhone手機": (38000, 0.3),
    "Acer  筆電": (40000, 0.8),
    "Go Pro攝影": (12000, 0.1),
    "Google眼鏡": (20000, 0.12),
    "Garmin手錶": (10000, 0.1),
}

max_weight = 1
th = sorted(things.items(), key=lambda item: item[1][0])  # 商品依價值排序
print("所有商品依價值排序如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(th)):
    print("{0:8s}{1:10d}{2:10.2f}".format(th[i][0], th[i][1][0], th[i][1][1]))

t = greedy(th)  # 呼叫貪婪選商品
print("貪婪選擇商品如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(t)):
    print("{0:8s}{1:10d}{2:10.2f}".format(t[i][0], t[i][1][0], t[i][1][1]))

print("------------------------------------------------------------")  # 60個

def greedy(graph, cities, start):
    # 貪婪演算法計算業務員旅行
    visited = []  # 儲存已拜訪城市
    visited.append(start)  # 儲存起點城市
    start_i = cities.index(start)  # 獲得起點城市的索引
    distance = 0  # 旅行距離
    for outer in range(len(cities) - 1):  # 尋找最近城市
        graph[start_i][start_i] = INF  # 將自己城市距離設為極大值
        min_dist = min(graph[start_i])  # 找出最短路徑
        distance += min_dist  # 更新總路程距離
        end_i = graph[start_i].index(min_dist)  # 最短距離城市的索引
        visited.append(cities[end_i])  # 將最短距離城市列入已拜訪
        for inner in range(len(graph)):  # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = INF
            graph[inner][start_i] = INF
        start_i = end_i  # 將下一個城市改為新的起點
    return distance, visited


INF = 9999  # 距離極大值
cities = ["新竹", "竹南", "竹北", "關西", "竹東"]
graph = [
    [0, 12, 10, 28, 16],
    [12, 0, 20, 35, 19],
    [10, 20, 0, 21, 11],
    [28, 35, 21, 0, 12],
    [16, 19, 11, 12, 0],
]
start = input("請輸入開始城市起點 : ")
dist, visited = greedy(graph, cities, start)
print("拜訪順序 : ", visited)
print("拜訪距離 : ", dist)

print("------------------------------------------------------------")  # 60個

def fruits_bag(W, wt, val):
    # 動態規劃演算法
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    items = [[[] for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格row
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                cur = val[r - 1] + table[r - 1][c - wt[r - 1]]
                cur_items = []
                cur_items.append(item[r - 1])
                if items[r - 1][c - wt[r - 1]]:
                    cur_items += items[r - 1][c - wt[r - 1]]
                pre = table[r - 1][c]
                pre_items = items[r - 1][c]
                if cur > pre:
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r - 1][c]
                items[r][c] = items[r - 1][c]
    return items, table[n][W]


item = ["釋迦", "西瓜", "玉荷包", "蘋果", "蓮霧", "番茄"]
value = [800, 200, 600, 700, 400, 100]  # 商品價值
weight = [5, 3, 2, 2, 3, 1]  # 商品重量
bag_weight = 5  # 背包可容重量
items, total_value = fruits_bag(bag_weight, weight, value)
print("最高價值 : ", total_value)
print("商品組合 : ", items[len(item)][bag_weight])

print("------------------------------------------------------------")  # 60個

def traveling(W, wt, val):
    # 動態規劃演算法
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    items = [[[] for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格
    for r in range(n + 1):  # 填入表格row
        for c in range(W + 1):  # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r - 1] <= c:
                cur = val[r - 1] + table[r - 1][c - wt[r - 1]]
                cur_items = []
                cur_items.append(item[r - 1])
                if items[r - 1][c - wt[r - 1]]:
                    cur_items += items[r - 1][c - wt[r - 1]]
                pre = table[r - 1][c]
                pre_items = items[r - 1][c]
                if cur > pre:
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r - 1][c]
                items[r][c] = items[r - 1][c]
    return items, table[n][W]


item = ["頤和園", "天壇", "故宮", "萬里長城", "圓明園"]
value = [7, 6, 9, 9, 8]  # 旅遊點評分數
weight = [1, 1, 2, 4, 1]  # 單項景點所需天數
travel_weight = 4  # 總旅遊天數
items, total_value = traveling(travel_weight, weight, value)
print("旅遊點評總分 : ", total_value)
print("旅遊景點組合 : ", items[len(item)][travel_weight])

print("------------------------------------------------------------")  # 60個

abc = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

msgTest = input("請輸入原始字串 : ")

cipher = []
for i in msgTest:  # 執行每個字元加密
    v = encry_dict[i]  # 加密
    cipher.append(v)  # 加密結果
ciphertext = "".join(cipher)  # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)


print("------------------------------------------------------------")  # 60個

from collections import deque


def palindrome(word):
    return word == word[::-1]


wd = input("請輸入字串 : ")
print("{} 是回文 : {}".format(wd, palindrome(wd)))

print("------------------------------------------------------------")  # 60個

def cr(head, foot):
    chicken = 0
    while True:
        rabbit = head - chicken  # 頭的總數
        if 2 * chicken + 4 * rabbit == foot:  # 腳的總數
            break
        chicken += 1
        if chicken > head:
            return "input", "error!", False
    return chicken, rabbit, True


h = eval(input("請輸入頭的數量 : "))
f = eval(input("請輸入腳的數量 : "))
chicken, rabbit, flag = cr(h, f)
if flag:
    print("雞有 {} 隻, 兔有 {} 隻".format(chicken, rabbit))
else:
    print(chicken, rabbit)

print("------------------------------------------------------------")  # 60個

from array import *

x = array("l", [1, 11, 22, 33, 44, 55])
print("陣列內容如下: ")
for data in x:
    print(data)
index = eval(input("請輸入欲刪除的索引 : "))
if index > 5 and index < 0:
    print("輸入錯誤")
else:
    x.pop(index)
    for data in x:
        print(data)

print("------------------------------------------------------------")  # 60個

class Node:
    # 節點

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list:
    # 鏈結串列

    def __init__(self):
        self.head = None  # 鏈結串列第 1 個節點

    def print_list(self):
        # 列印鏈結串列
        ptr = self.head  # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def search(self, val):
        ptr = self.head
        count = 0
        while ptr:
            if ptr.data == val:
                count += 1
            ptr = ptr.next
        return count


link = Linked_list()
link.head = Node(5)
n2 = Node(15)  # 節點 2
n3 = Node(5)  # 節點 3
link.head.next = n2  # 節點 1 指向節點 2
n2.next = n3  # 節點 2 指向節點 3
print("所建的鏈結串列")
link.print_list()  # 列印鏈結串列 link
print("分別列出數值5, 15, 20的出現次數")
print("5  出現 %d 次" % link.search(5))
print("15 出現 %d 次" % link.search(15))
print("20 出現 %d 次" % link.search(20))

print("------------------------------------------------------------")  # 60個

from queue import Queue

food = ["漢堡", "薯條", "可樂"]
q = Queue()
for f in food:
    q.put(f)
    print("成功插入 %s 至佇列" % f)

print("佇列輸出")
while not q.empty():
    print(q.get())

print("------------------------------------------------------------")  # 60個

class Stack:
    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def isEmpty(self):
        return self.my_stack == []

    def cls(self):
        del self.my_stack[:]


stack = Stack()
fruits = ["Grape", "Mango", "Apple"]
for fruit in fruits:
    stack.my_push(fruit)
    print("將 %s 水果堆入堆疊" % fruit)
print("堆疊有 %d 種水果" % stack.size())
stack.cls()
while not stack.isEmpty():
    print(stack.my_pop())
print("程式結束")

print("------------------------------------------------------------")  # 60個


class Node:
    def __init__(self, data=None):
        # 建立二元樹的節點
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # 建立二元樹
        if self.data:  # 如果根節點存在
            if data < self.data:  # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)  # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)  # 建立新節點存放資料
            else:  # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:  # 如果根節點不存在
            self.data = data  # 建立根節點

    def postorder(self):
        # 後序列印
        if self.left:  # 如果左子節點存在
            self.left.postorder()  # 遞迴呼叫下一層
        if self.right:  # 如果右子節點存在
            self.right.postorder()  # 遞迴呼叫下一層
        print(self.data)  # 列印

    def depth(self):
        current_depth = 0
        if self.left:
            current_depth = max(current_depth, self.left.depth())
        if self.right:
            current_depth = max(current_depth, self.right.depth())
        return current_depth + 1


num = 0
tree = Node()  # 建立二元樹物件
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]  # 建立二元樹數據
for d in datas:
    tree.insert(d)  # 分別插入數據
print("所建的二元樹後序列印如下 : ")
tree.postorder()  # 後序列印
print("二元樹的深度 = ", tree.depth())

print("------------------------------------------------------------")  # 60個


class Heaptree:
    def __init__(self):
        self.heap = []  # 堆積樹串列
        self.size = 0  # 堆積樹串列元素個數

    def data_down(self, i):
        # 如果節點值大於子節點值則資料與較小的子節點值對調
        while (i * 2 + 2) <= self.size:  # 如果有子節點則繼續
            mi = self.get_min_index(i)  # 取得較小值得子節點
            if self.heap[i] > self.heap[mi]:  # 如果目前節點大於子節點
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]
            i = mi

    def get_min_index(self, i):
        # 傳回較小值的子節點索引
        if i * 2 + 2 >= self.size:  # 只有一個左子節點
            return i * 2 + 1  # 傳回左子節點索引
        else:
            if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:  # 如果左子節點小於右子節點
                return i * 2 + 1  # True傳回左子節點索引
            else:
                return i * 2 + 2  # False傳回右子節點索引

    def build_heap(self, mylist):
        # 建立堆積樹
        i = (len(mylist) // 2) - 1  # 從有子節點的節點開始處理
        self.size = len(mylist)  # 得到串列元素個數
        self.heap = mylist  # 初步建立堆積樹串列
        while i >= 0:  # 從下層往上處理
            self.data_down(i)
            i = i - 1

    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret


h = [10, 21, 5, 9, 13, 28, 3]
print("執行前普通串列   = ", h)
obj = Heaptree()
obj.build_heap(h)  # 建立堆積樹串列
print("執行後堆積樹串列 = ", obj.heap)
min = obj.get_min()
print("所獲得的最小值   = ", min)
print("執行後堆積樹串列 = ", obj.heap)

print("------------------------------------------------------------")  # 60個


def check_name(name):
    if voted.get(name):
        print("你已經投過票了")
    else:
        print("歡迎投票")
        voted[name] = True


voted = {}  # 建立選民名單

name = input("請輸入名字 : ")
check_name(name)

print("------------------------------------------------------------")  # 60個


def selection_sort(nLst):
    # 選擇排序
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][1] < nLst[j][1]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


program = [
    ("Python", 98789),
    ("C", 56532),
    ("C#", 88721),
    ("Java", 90397),
    ("C++", 63122),
    ("PHP", 58000),
]

print("程式語言使用率排行")
selection_sort(program)
for i in range(len(program)):
    print("{0}:{1:7s} -- 使用次數 {2}".format(i + 1, program[i][0], program[i][1]))

print("------------------------------------------------------------")  # 60個



def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length - 1):
        print("第 %d 次外圈排序" % (i + 1))
        for j in range(length - 1 - i):
            if nLst[j] < nLst[j + 1]:
                nLst[j], nLst[j + 1] = nLst[j + 1], nLst[j]
            print("第 %d 次內圈排序 : " % (j + 1), nLst)
    return nLst


data = []
while True:
    val = input("請輸入數值(Q或q代表輸入結束) : ")
    if val == "Q" or val == "q":
        break
    data.append(int(val))
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

