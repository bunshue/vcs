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

# 像是richTextBox
text1 = tk.Text(window, width=80, height=6)  # 放入多行輸入框
text1.pack()
# text1.place(x = 100, y = 100)

bt_set_data = tk.Button(window, text="set data", command=set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window, text="clear", command=clear)  # 放入清空按鈕
bt_clear.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text2 = tk.Text(window, width=80, height=6)  # 放入多行輸入框
text2.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text2.insert(tk.INSERT, "雖然功能略為陽春，\n")
text2.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text2.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text2.insert(tk.END, "不需另外安裝即可使用。")
text2.pack()
text2.config(state=tk.DISABLED)  # 此行設定Text內容不可改變

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="輸入成績：")
# label1.place(x=20, y=20)
label1.pack()
score = tk.StringVar()
entry1 = tk.Entry(window, textvariable=score)
# entry1.place(x=90, y=20)
entry1.pack()
button1 = tk.Button(window, text="計算成績")
# button1.place(x=80, y=50)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(window, bg="pink")  # Hold four labels for displaying cards
frame1.pack()


def getTextData3():
    mesg = text3.get("1.0", "end")
    print("取得Text的資料 :", mesg)


scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text3 = tk.Text(
    frame1, width=80, height=6, wrap=tk.WORD, yscrollcommand=scrollbar.set
)  # 放入多行輸入框
text3.pack()
scrollbar.config(command=text3.yview)

button1 = tk.Button(window, text="取得Text的資料", command=getTextData3)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(window, bg="pink")  # Hold four labels for displaying cards
frame1.pack()

LOG_LINE_NUM = 0


# 獲取當前時間
def get_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return current_time


# 日志動態打印
def write_log():
    global LOG_LINE_NUM
    current_time = get_current_time()
    logmsg_in = str(current_time) + " " + "要記錄的訊息" + "\n"  # 換行
    if LOG_LINE_NUM <= 7:
        text4.insert(tk.END, logmsg_in)
        LOG_LINE_NUM = LOG_LINE_NUM + 1
    else:
        text4.delete(1.0, 2.0)
        text4.insert(tk.END, logmsg_in)


def add_text():
    string = "測試字串......."
    # 輸出到界面
    text4.delete(1.0, tk.END)
    text4.insert(1.0, string)


scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# 日誌框
text4 = tk.Text(
    frame1, width=80, height=6, wrap=tk.WORD, yscrollcommand=scrollbar.set
)  # 放入多行輸入框
text4.pack()
scrollbar.config(command=text4.yview)

button2 = tk.Button(window, text="寫日誌", command=write_log)
button2.pack()

button3 = tk.Button(window, text="蓋過字串", command=add_text)
button3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text5 = tk.Text(window, width=50, height=5, padx=15, pady=15)
text5.insert(1.0, "要加到Text內的文字")
text5.tag_configure("center", justify="center")
text5.tag_add("center", 1.0, "end")
text5.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Text 2")

text6 = tk.Text(window)
text6.insert(tk.INSERT, "床前明月光\n")
text6.insert(tk.INSERT, "疑是地上霜\n")
text6.insert(tk.INSERT, "舉頭望明月\n")
text6.insert(tk.INSERT, "低頭思故鄉\n")
text6.pack()
text6.config(state=tk.DISABLED)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print("Text多行文字")
sentences = "玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"

text7 = tk.Text(window, width=30, height=14, bg="yellow", wrap=tk.WORD)
text7.insert(tk.END, sentences)
text7.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Text 3")

text8 = tk.Text(window, width=30, height=5)
text8.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text2 = tk.Text(window, width=30, height=5)
text2.pack()
text2.insert(tk.END, "越王勾踐破吳歸，戰士還家盡錦衣。\n")
text2.insert(tk.INSERT, "宮女如花滿春殿，只今唯有鷓鴣飛。")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text3 = tk.Text(window, width=30, height=5)
text3.insert(tk.END, "黃鶴樓送孟浩然之廣陵\n李白\n")
text3.insert(tk.END, "故人西辭黃鶴樓，\n")
text3.insert(tk.END, "煙花三月下揚州。\n")
text3.insert(tk.END, "孤帆遠影碧空盡，\n")
text3.insert(tk.END, "唯見長江天際流。\n")
text3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text4 = tk.Text(window, width=30, height=5)
text4.insert(tk.END, "望廬山瀑布\n李白\n")
str = """日照香爐生紫煙，
遙看瀑布挂前川。
飛流直下三千尺，
疑是銀河落九天。"""
text4.insert(tk.END, str)
text4.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text5 = tk.Text(window, width=30, height=5)
text5.pack()

str = """誰家玉笛暗飛聲，散入春風滿洛城。
此夜曲中聞折柳，何人不起故園情。
"""
text5.insert(tk.END, str)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text6 = tk.Text(window, width=30, height=5)
# text6.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)
text6.pack()

text6.insert(tk.END, "白髮三千丈，離愁似箇長。\n")  # 插入文字
text6.insert(1.14, "不知明鏡裏，何處得秋霜。")  # 插入文字

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

text7.config(state=tk.DISABLED)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個
"""
# 產生多行文字框元件
text9 = tk.Text(window,	selectbackground = 'red', selectforeground = 'gray')
text9.pack()
"""
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

text10 = tk.Text(window, width=30, height=5)
text10.pack()

text10.insert(tk.END, "\n寫在Text中的文字1")
text10.insert(tk.END, "\n寫在Text中的文字2")
text10.insert(tk.END, "\n寫在Text中的文字3")
text10.insert(tk.END, "\n寫在Text中的文字4")

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

# 建立Button
button1 = tk.Button(window, text="選取Text的文字", command=selectedText)
button1.pack(pady=3)

# 建立Text
text = tk.Text(window)
# text.pack(fill=BOTH,expand=True,padx=3,pady=2)
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

# 建立Button
button1 = tk.Button(window, text="Print index", command=printIndex)
button1.pack(pady=3)

# 建立Text
text = tk.Text(window)
# text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)
text.pack()
text.insert(tk.END, "白髮三千丈，離愁似箇長。\n")  # 插入文字
text.insert(tk.END, "不知明鏡裏，何處得秋霜。")  # 插入文字

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

text = tk.Text(window)

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
text.pack(fill=tk.BOTH, expand=True)
print(text.get("mark1", "mark2"))

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("ScrollBar捲軸, Text + Scrollbar 需要用 grid")

window = tk.Tk()
window.title("ScrollBar捲軸")
window.geometry("300x200")

text = tk.Text(window, width="30", height="5")
text.grid(row=0, column=0)

scrollbar = tk.Scrollbar(command=text.yview, orient=tk.VERTICAL)
scrollbar.grid(row=0, column=1, sticky="ns")
text.configure(yscrollcommand=scrollbar.set)

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

text.insert(tk.END, "黃鶴樓送孟浩然之廣陵\n李白\n")
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
text.insert(tk.END, "黃鶴樓送孟浩然之廣陵\n李白\n")
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
text.pack(fill=tk.BOTH, expand=True)

text.insert(tk.END, "黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END, "故人西辭黃鶴樓，\n")
text.insert(tk.END, "煙花三月下揚州。\n")
text.insert(tk.END, "孤帆遠影碧空盡，\n")
text.insert(tk.END, "唯見長江天際流。\n")

button1 = tk.Button(window, text="存檔", command=saveFile)
button1.pack(pady=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def validate():
    print("你按了 Validate")
    cc = entry1.get()
    print(cc)


window = tk.Tk()

frame1 = tk.Frame(window)
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(frame1, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)

frame2 = tk.Frame(window)
frame2.pack()

tk.Label(frame2, text="Enter a filename: ").pack(side=tk.LEFT)

filename = tk.StringVar()
entry1 = tk.Entry(frame2, width=40, textvariable=filename)
entry1.pack(side=tk.LEFT)

tk.Button(frame2, text="Validate", command=validate).pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
