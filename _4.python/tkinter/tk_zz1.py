import tkinter as tk

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
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())


choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(window, text="選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(window, text="足球", value="足球", variable=choice, command=choose)
item1.pack()
item2 = tk.Radiobutton(window, text="籃球", value="籃球", variable=choice, command=choose)
item2.pack()
item3 = tk.Radiobutton(window, text="棒球", value="棒球", variable=choice, command=choose)
item3.pack()
lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()
item1.select()
choose()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

label1=tk.Label(window, text="輸入成績：")
#label1.place(x=20, y=20)
label1.pack()
score = tk.StringVar()
entryUrl = tk.Entry(window, textvariable=score)
#entryUrl.place(x=90, y=20)
entryUrl.pack()
btnDown = tk.Button(window, text="計算成績")
#btnDown.place(x=80, y=50)
btnDown.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()




