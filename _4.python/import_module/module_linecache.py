import random
import linecache

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/涼州詞.txt"

getLines = linecache.getlines(filename)

print(getLines)

print("取得{}檔案原內容：\n{}".format(filename, getLines))

# 打亂次數
times = 5

for i in range(times):
    random.shuffle(getLines)
    print(getLines)

print("\n隨機抽取：", random.choice(getLines))

print("------------------------------------------------------------")  # 60個
