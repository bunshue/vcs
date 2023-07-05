count = 0
mmm = 'abcd'

def set_data():
    '''
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + mmm
    print(mesg)
    text1.insert ('end', mesg)
    '''
    global count
    count = count + 1
    message = '  次數' + str(count)
    text1.insert ('end', message)

def clear():
    text1.delete(1.0,'end')
    # 執行 clear 函式時，清空內容

import tkinter as tk

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
text1 = tk.Text(window, width = 80, height = 10)  # 放入多行輸入框
text1.pack()
#text1.place(x = 100, y = 100)

bt_set_data = tk.Button(window, text = 'set data', command = set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window, text = 'clear', command = clear)  # 放入清空按鈕
bt_clear.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

text = tk.Text(window)
text.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text.insert(tk.END, "不需另外安裝即可使用。")
text.pack()
text.config(state=tk.DISABLED)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

label1=tk.Label(window, text="輸入成績：")
#label1.place(x=20, y=20)
label1.pack()
score = tk.StringVar()
entryUrl = tk.Entry(window, textvariable = score)
#entryUrl.place(x=90, y=20)
entryUrl.pack()
btnDown = tk.Button(window, text="計算成績")
#btnDown.place(x=80, y=50)
btnDown.pack()



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()
