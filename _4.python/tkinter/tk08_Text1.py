import sys
import time
import tkinter as tk

print("------------------------------------------------------------")  # 60個

count = 0
mmm = 'abcd'

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
    message = '  次數' + str(count)
    text1.insert('end', message)

def clear():
    text1.delete(1.0,'end')
    # 執行 clear 函式時，清空內容


# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Text測試"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

#像是richTextBox
text1 = tk.Text(window, width = 80, height = 6)  # 放入多行輸入框
text1.pack()
#text1.place(x = 100, y = 100)

bt_set_data = tk.Button(window, text = 'set data', command = set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window, text = 'clear', command = clear)  # 放入清空按鈕
bt_clear.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

text2 = tk.Text(window, width = 80, height = 6)  # 放入多行輸入框
text2.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text2.insert(tk.INSERT, "雖然功能略為陽春，\n")
text2.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text2.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text2.insert(tk.END, "不需另外安裝即可使用。")
text2.pack()
text2.config(state = tk.DISABLED)   #此行設定Text內容不可改變

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

label1 = tk.Label(window, text = "輸入成績：")
#label1.place(x=20, y=20)
label1.pack()
score = tk.StringVar()
entry1 = tk.Entry(window, textvariable = score)
#entry1.place(x=90, y=20)
entry1.pack()
button1 = tk.Button(window, text = "計算成績")
#button1.place(x=80, y=50)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

frame1 = tk.Frame(window, bg = 'pink') # Hold four labels for displaying cards
frame1.pack()

def getTextData3():
    mesg = text3.get("1.0", "end")
    print('取得Text的資料 :', mesg)
    
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text3 = tk.Text(frame1, width = 80, height = 6, wrap = tk.WORD, yscrollcommand = scrollbar.set)  # 放入多行輸入框
text3.pack()
scrollbar.config(command = text3.yview)

button1 = tk.Button(window, text = "取得Text的資料", command = getTextData3)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



frame1 = tk.Frame(window, bg = 'pink') # Hold four labels for displaying cards
frame1.pack()

LOG_LINE_NUM = 0

#獲取當前時間
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time

#日志動態打印
def write_log():
    global LOG_LINE_NUM
    current_time = get_current_time()
    logmsg_in = str(current_time) +" " + '要記錄的訊息' + "\n"      #換行
    if LOG_LINE_NUM <= 7:
        text4.insert(tk.END, logmsg_in)
        LOG_LINE_NUM = LOG_LINE_NUM + 1
    else:
        text4.delete(1.0,2.0)
        text4.insert(tk.END, logmsg_in)

def add_text():
    string = '測試字串.......'
    #輸出到界面
    text4.delete(1.0, tk.END)
    text4.insert(1.0, string)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
#日誌框
text4 = tk.Text(frame1, width = 80, height = 6, wrap = tk.WORD, yscrollcommand = scrollbar.set)  # 放入多行輸入框
text4.pack()
scrollbar.config(command = text4.yview)

button2 = tk.Button(window, text = '寫日誌', command = write_log)
button2.pack()

button3 = tk.Button(window, text = '蓋過字串', command = add_text)
button3.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

text1 = tk.Text(window, width = 50, height = 6, padx = 15, pady = 15)
text1.insert(1.0, '要加到Text內的文字')
text1.tag_configure("center", justify = "center")
text1.tag_add("center", 1.0, "end")
#text1.grid(column = 1, row = 4)
text1.pack()





separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")
window.title("Text測試")

ptext = tk.Text(window)
ptext.insert(tk.INSERT, "床前明月光\n")
ptext.insert(tk.INSERT, "疑是地上霜\n")
ptext.insert(tk.INSERT, "舉頭望明月\n")
ptext.insert(tk.INSERT, "低頭思故鄉\n")
ptext.pack()
ptext.config(state=tk.DISABLED)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("scrollbar")

window = tk.Tk()
window.title("ScrollBar捲軸")
window.geometry('300x200')

text = tk.Text(window, width = "30", height = "5")
text.grid(row = 0, column = 0)
scrollbar = tk.Scrollbar(command = text.yview, orient = tk.VERTICAL)
scrollbar.grid(row = 0, column = 1, sticky = "ns")
text.configure(yscrollcommand = scrollbar.set)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("text")

sentences="玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"

window = tk.Tk()
window.title("Text多行文字")
window.geometry('300x200')

text = tk.Text(window, width = 30, height = 14, bg = "yellow", wrap=tk.WORD)
text.insert(tk.END,sentences)
text.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
