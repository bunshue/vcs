import sys
import collections

print("------------------------------------------------------------")  # 60個

print("查找出現次數最多的元素")

list1 = [10, 30, 10, 50, 40, 20, 30, 20, 40, 20, 10, 50, 10]
freqDict = collections.Counter(list1)
print(freqDict)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查找出現次數最多的元素")

words = ["foo", "bar", "pop", "foo", "bar", "foo"]

word_counts = collections.Counter(words)

print(type(word_counts))
print(word_counts)

for item, counter in word_counts.items():
    print(item, "出現", counter, "次")

print("出現最多次的項目:", word_counts.most_common(1))  # 最多出現的前N名

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查找出現次數最多的元素")

words = [
    "look",
    "into",
    "my",
    "eyes",
    "look",
    "into",
    "my",
    "eyes",
    "don't",
    "look",
    "eyes",
    "look",
    "into",
    "my",
    "eyes",
]

word_counts = collections.Counter(words)

# 出现频率最高的3个单词
cc = word_counts.most_common(3)  # 最多出現的前N名
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from collections import Counter

cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4]

cc = Counter(cyl).items()
print(cc)

labels, values = zip(*Counter(cyl).items())

print(values)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 排序字典

d = collections.OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import nt

_ntuple_diskusage = collections.namedtuple("usage", "total used free")


def disk_usage(path):
    total, free = nt._getdiskusage(path)
    used = total - free
    return _ntuple_diskusage(total, used, free)


foldername = "D:/_git/vcs/"
du = disk_usage(foldername)
print(du)
print("容量 :", du.total, "個位元組\t", du.total // 1024 // 1024 // 1024, "GB")
print("已使用空間 :", du.used, "個位元組\t", du.used // 1024 // 1024 // 1024, "GB")
print("可用空間 :", du.free, "個位元組\t", du.free // 1024 // 1024 // 1024, "GB")

foldername = "D:/"
du = disk_usage(foldername)
print(du)
print("容量 :", du.total, "個位元組\t", du.total // 1024 // 1024 // 1024, "GB")
print("已使用空間 :", du.used, "個位元組\t", du.used // 1024 // 1024 // 1024, "GB")
print("可用空間 :", du.free, "個位元組\t", du.free // 1024 // 1024 // 1024, "GB")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 算體重總和
# collections.Counter - 多重集合 (計數器)

inventory = collections.Counter()

loot = {"寶劍": 1, "麵包": 3}
inventory.update(loot)

print(inventory)

more_loot = {"寶劍", "金幣"}
inventory.update(more_loot)

print(inventory)

yet_more_loot = ["麵包", "麵包", "藥草"]
inventory.update(yet_more_loot)

print(inventory)

print("鍵種類 =", len(inventory))

print("值總和 =", sum(inventory.values()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("defaultdict 容器")

words = ["foo", "bar", "pop", "foo", "bar", "foo"]

d = collections.defaultdict(int)

for item in words:
    d[item] += 1

print(d)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

prices = [
    ["apple", 50],
    ["banana", 120],
    ["grape", 500],
    ["apple", 70],
    ["banana", 150],
    ["banana", 700],
]

fruits = collections.defaultdict(list)

for name, price in prices:
    fruits[name].append(price)

for name, prices in fruits.items():
    print(name, prices)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
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


print("統計一串英文字串個字母出現的頻率")

from collections import defaultdict

text = "this is a lion-mouse"

frequency = defaultdict(int)
for symbol in text:
    frequency[symbol] += 1
print(frequency)

heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
print(heap)

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



