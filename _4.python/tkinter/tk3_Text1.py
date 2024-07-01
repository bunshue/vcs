"""

Text 放入多行輸入框


"""

import sys
import time
import tkinter as tk

print("------------------------------------------------------------")  # 60個

count = 0
mmm = "abcd"


def set_data():
    """
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0", "end")
    mesg= mesg + mmm
    print(mesg)
    text1.insert ('end', mesg)
    """
    global count
    count = count + 1
    message = "  次數" + str(count)
    text1.insert("end", message)


def clear():
    text1.delete(1.0, "end")
    # 執行 clear 函式時，清空內容


window = tk.Tk()
window.geometry("600x800")
window.title("Text 1")

text3 = tk.Text(window, width=30, height=5)
text3.pack()

text3.insert(tk.INSERT, "最簡單 W=30, H = 5\n")
text3.insert(tk.INSERT, "故人西辭黃鶴樓，\n")
text3.insert(tk.INSERT, "煙花三月下揚州。\n")
text3.insert(tk.INSERT, "孤帆遠影碧空盡，\n")
text3.insert(tk.END, "唯見長江天際流。\n")

text3.config(state=tk.DISABLED)  # 設定Text內容不可改變

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text7 = tk.Text(window, width=30, height=5, bg="yellow", wrap=tk.WORD)
text7.pack()

sentences = "玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"
text7.insert(tk.END, sentences)

text7.insert(tk.END, "望廬山瀑布\n李白\n")
poem_text = """日照香爐生紫煙，
遙看瀑布挂前川。
飛流直下三千尺，
疑是銀河落九天。"""
text7.insert(tk.END, poem_text)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text7 = tk.Text(window, width=30, height=5)
text7.pack()

text7.insert(tk.INSERT, "功蓋三分國\n")
text7.insert(tk.CURRENT, "名成八陣圖\n")
text7.insert(tk.CURRENT, "江流石不轉\n")
text7.insert(tk.END, "遺恨失吞吳")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text1 = tk.Text(window, width=80, height=6)  # 放入多行輸入框
text1.pack()

bt_set_data = tk.Button(window, text="set data", command=set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window, text="clear", command=clear)  # 放入清空按鈕
bt_clear.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="輸入成績：")
label1.pack()

score = tk.StringVar()
entry1 = tk.Entry(window, textvariable=score)
entry1.pack()

button1 = tk.Button(window, text="計算成績")
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text5 = tk.Text(window, width=50, height=5, padx=15, pady=15)
text5.pack()

text5.insert(1.0, "要加到Text內的文字")
text5.tag_configure("center", justify="center")
text5.tag_add("center", 1.0, "end")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text6 = tk.Text(window, width=30, height=5)
text6.pack()

text6.insert(tk.END, "白髮三千丈，離愁似箇長。\n")  # 插入文字
text6.insert(1.14, "不知明鏡裏，何處得秋霜。")  # 插入文字

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

def selectedText():  # 列印所選的文字
    try:
        selText = text.get(tk.SEL_FIRST, tk.SEL_LAST)
        print("選取文字: ", selText)
        print("selectionstart: ", text.index(tk.SEL_FIRST))
        print("selectionend  : ", text.index(tk.SEL_LAST))
    except TclError:
        print("沒有選取文字")


window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window, text="選取Text的文字", command=selectedText)
button1.pack(pady=3)

text = tk.Text(window, width=30, height=5)
text.pack()

text.insert(tk.END, "白髮三千丈，離愁似箇長。")  # 插入文字

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printIndex():  # 列印索引
    print("INSERT : ", text.index(tk.INSERT))
    print("CURRENT: ", text.index(tk.CURRENT))
    print("END    : ", text.index(tk.END))


window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window, text="Print index", command=printIndex)
button1.pack(pady=3)

text = tk.Text(window, width=30, height=5)
text.pack()

text.insert(tk.END, "白髮三千丈，離愁似箇長。\n")  # 插入文字
text.insert(tk.END, "不知明鏡裏，何處得秋霜。")  # 插入文字

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

text = tk.Text(window, width=30, height=5)
text.pack(fill=tk.BOTH, expand=True)
#text.pack()

text.insert(tk.END, "第1行\n")
text.insert(tk.END, "第2行\n")
text.insert(tk.END, "第3行\n")
text.insert(tk.END, "第4行\n")
text.insert(tk.END, "第5行\n")
text.insert(tk.END, "第6行\n")
text.insert(tk.END, "第7行\n")
text.insert(tk.END, "第8行\n")
text.insert(tk.END, "第9行\n")
text.insert(tk.END, "第10行\n")

print("設定書籤在第5、第8行")
text.mark_set("mark1", "5.0")
text.mark_set("mark2", "8.0")

# 設定標籤
text.tag_add("tag1", "mark1", "mark2")
text.tag_config("tag1", foreground="blue", background="lightyellow")

print(text.get("mark1", "mark2"))

window.mainloop()

print("------------------------------------------------------------")  # 60個


def mySearch():
    text.tag_remove("found", "1.0", tk.END)  # 刪除標籤但是不刪除標籤定義
    start = "1.0"  # 設定搜尋起始位置
    key = entry.get()  # 讀取搜尋關鍵字

    if len(key.strip()) == 0:  # 沒有輸入
        return
    while True:  # while迴圈搜尋
        pos = text.search(key, start, tk.END)  # 執行搜尋
        if pos == "":  # 找不到結束while迴圈
            break
        text.tag_add("found", pos, "%s+%dc" % (pos, len(key)))  # 加入標籤
        start = "%s+%dc" % (pos, len(key))  # 更新搜尋起始位置


window = tk.Tk()
window.geometry("600x400")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

entry = tk.Entry()
entry.grid(row=0, column=0, padx=5, sticky=tk.W + tk.E)

button1 = tk.Button(window, text="搜尋", command=mySearch)
button1.grid(row=0, column=1, padx=5, pady=5)

# 建立Text
text = tk.Text(window, undo=True)
text.grid(
    row=1, column=0, columnspan=2, padx=3, pady=5, sticky=tk.N + tk.S + tk.W + tk.E
)

text.insert(tk.END, "故人西辭黃鶴樓，\n")
text.insert(tk.END, "煙花三月下揚州。\n")
text.insert(tk.END, "孤帆遠影碧空盡，\n")
text.insert(tk.END, "唯見長江天際流。\n")

text.tag_configure("found", background="yellow")  # 定義未來找到的標籤定義

window.mainloop()

print("------------------------------------------------------------")  # 60個


def spellingCheck():
    text.tag_remove("spellErr", "1.0", tk.END)  # 刪除標籤但是不刪除標籤定義
    textwords = text.get("1.0", tk.END).split()  # Text控件的內文
    print("字典內容\n", textwords)  # 列印字典內容

    startChar = "("  # 可能的啟始字元
    endChar = (".", ",", ":", ";", "?", "!", ")")  # 可能的結束字元

    start = "1.0"  # 檢查起始索引位置
    for word in textwords:
        if word[0] in startChar:  # 是否含非字母的啟始字元
            word = word[1:]  # 刪除非字母的啟始字元
        if word[-1] in endChar:  # 是否含非字母的結束字元
            word = word[:-1]  # 刪除非字母的結束字元
        if word not in dicts and word.lower() not in dicts:
            print("error", word)
            pos = text.search(word, start, tk.END)
            text.tag_add("spellErr", pos, "%s+%dc" % (pos, len(word)))
            pos = "%s+%dc" % (pos, len(word))


def clrText():
    text.tag_remove("spellErr", "1.0", tk.END)


window = tk.Tk()
window.geometry("600x400")

# 建立工具列
toolbar = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=1)

chkButton = tk.Button(toolbar, text="拼字檢查", command=spellingCheck)
chkButton.pack(side=tk.LEFT, padx=5, pady=5)

clrButton = tk.Button(toolbar, text="清除", command=clrText)
clrButton.pack(side=tk.LEFT, padx=5, pady=5)

# 建立Text
text = tk.Text(window, undo=True)
text.pack(fill=tk.BOTH, expand=True)

text.insert(tk.END, "故人西辭黃鶴樓，\n")
text.insert(tk.END, "煙花三月下揚州。\n")
text.insert(tk.END, "孤帆遠影碧空盡，\n")
text.insert(tk.END, "唯見長江天際流。\n")

text.tag_configure("spellErr", foreground="red")  # 定義未來找到的標籤定義
with open("image/myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")  # 自訂字典串列

window.mainloop()

print("------------------------------------------------------------")  # 60個

def saveFile():
    textContent = text.get("1.0", tk.END)
    filename = "tmp_write_file.txt"
    with open(filename, "w") as output:
        output.write(textContent)
        window.title(filename)

window = tk.Tk()
window.geometry("600x400")

# 建立Text
text = tk.Text(window, undo=True)
#text.pack(fill=tk.BOTH, expand=True)
text.pack()

text.insert(tk.END, "故人西辭黃鶴樓，\n")
text.insert(tk.END, "煙花三月下揚州。\n")
text.insert(tk.END, "孤帆遠影碧空盡，\n")
text.insert(tk.END, "唯見長江天際流。\n")

button1 = tk.Button(window, text="存檔", command=saveFile)
button1.pack(pady=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("Text + print log")

LOG_LINE_NUM = 0
LOG_LINE_MAX = 10

# 日志動態打印
def write_log():
    global LOG_LINE_NUM
    # 獲取當前時間
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    logmsg_in = str(current_time) + " " + "要記錄的訊息" + "\n"  # 換行
    if LOG_LINE_NUM < LOG_LINE_MAX:
        text4.insert(tk.END, logmsg_in)
        LOG_LINE_NUM = LOG_LINE_NUM + 1
    else:
        text4.delete(1.0, 2.0)
        text4.insert(tk.END, logmsg_in)

# 日誌框
text4 = tk.Text(window, width=50, height=LOG_LINE_MAX)
text4.pack()

button2 = tk.Button(window, text="寫日誌", command=write_log)
button2.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("Text + Scrollbar use window")

xscrollbar = tk.Scrollbar(window, orient=tk.HORIZONTAL)  # x軸scrollbar物件
yscrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)  # y軸scrollbar物件

xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)  # x軸scrollbar包裝顯示
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # y軸scrollbar包裝顯示# 靠右安置與父物件高度相同

text1 = tk.Text(window, width=30, height=10, wrap="none", bg="lightyellow")
text1.pack(fill=tk.BOTH, expand=True)

#text1 = tk.Text(frame1, width=30, height=10, wrap=tk.WORD)
#text1.pack(side=tk.LEFT, fill=tk.Y)  # 靠左安置與父物件高度相同

xscrollbar.config(command=text1.xview)  # x軸scrollbar設定
yscrollbar.config(command=text1.yview)  # y軸scrollbar設定

text1.config(xscrollcommand=xscrollbar.set)  # x軸scrollbar綁定text1
text1.config(yscrollcommand=yscrollbar.set)  # y軸scrollbar綁定text1

text1.insert(tk.END, "李白\n黃鶴樓送孟浩然之廣陵\n")
text = """故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。"""
text1.insert(tk.END, text)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("Text + Scrollbar use frame")

frame1 = tk.Frame(window)
frame1.pack()

xscrollbar = tk.Scrollbar(frame1, orient=tk.HORIZONTAL)  # x軸scrollbar物件
yscrollbar = tk.Scrollbar(frame1, orient=tk.VERTICAL)  # y軸scrollbar物件

xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)  # x軸scrollbar包裝顯示
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # y軸scrollbar包裝顯示# 靠右安置與父物件高度相同

text1 = tk.Text(frame1, width=30, height=10, wrap="none", bg="lightyellow")
text1.pack(fill=tk.BOTH, expand=True)

#text1 = tk.Text(frame1, width=30, height=10, wrap=tk.WORD)
#text1.pack(side=tk.LEFT, fill=tk.Y)  # 靠左安置與父物件高度相同

xscrollbar.config(command=text1.xview)  # x軸scrollbar設定
yscrollbar.config(command=text1.yview)  # y軸scrollbar設定

text1.config(xscrollcommand=xscrollbar.set)  # x軸scrollbar綁定text1
text1.config(yscrollcommand=yscrollbar.set)  # y軸scrollbar綁定text1

text1.insert(tk.END, "李白\n黃鶴樓送孟浩然之廣陵\n")
text = """故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。"""
text1.insert(tk.END, text)

window.mainloop()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
# 產生多行文字框元件
text9 = tk.Text(window,	selectbackground = 'red', selectforeground = 'gray')
text9.pack()
"""


