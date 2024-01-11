import linecache, random

fileName = str(input("請輸入欲要取得內容檔名(txt檔)："))
times = int(input("請輸入需要打亂次數："))

if ".txt" not in fileName:
    fileName = fileName + ".txt"

getLines = linecache.getlines(fileName)
print("取得{}檔案原內容：\n{}".format(fileName.replace(".txt", ""), getLines))

for i in range(times):
    random.shuffle(getLines)

print("\n隨機抽取：", random.choice(getLines))
