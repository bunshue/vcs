"""

共同設定

基本的使用

多元件共同使用


"""

import sys
import tkinter as tk

from tkinter.filedialog import askopenfile #tk之openFileDialog

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

# 設定主視窗之背景色
window.configure(bg = "#7AFEC6")

icon_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/ims.ico'
window.iconbitmap(icon_filename)   # 更改圖示


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button_exit = tk.Button(window, text = "關閉視窗標準版", command = window.destroy)
button_exit.pack()

def show_tk_info():
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    print('取得目前螢幕大小 : ', width, height)

button_info = tk.Button(window, width = 10, height = 2, command = show_tk_info, text = '顯示資訊')
button_info.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# Button測試
tk.Label(text = 'Button測試').pack()
def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")

labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg = "red", textvariable = labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable = btntext, command = clickme)
btntext.set("按我！")
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

x_st = 50
y_st = 150
dx = 120
dy = 80
w = 12
h = 3

def choose():
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)
    msg.set(str)

choice = []

stage_no = [
'第1站 下蓋清潔', '第2站 點膠', '第3站 前2站NG', '第4站 模組接合',
'第5站 間隙檢查', '第6站 UV固化', '第7站 點膠線檢查', '第8站 前4站NG',
'第9站 氣密測試', '第10站 Hi-pot', '第11站 色調', '第12站 前3站NG',
'第13a站 等級判定', '第13b站 資料燒錄', '第14站 前2站NG', '第15站 包裝出料'
]

main_message1 = tk.StringVar()
main_message2 = tk.StringVar()

font_size = 20

# 加入 Label
label_message1 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message1)
label_message1.pack()
label_message1.place(x = 5, y = 0 + 10)
main_message1.set('AAAA')

label_message2 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message2)
label_message2.pack()
label_message2.place(x = 5 + W * 3 / 4, y = 0 + 10)
main_message2.set('BBBB')

msg = tk.StringVar()
label1 = tk.Label(window, text = '選擇顯示站別：')
label1.pack()
label1.place(x = x_st + dx * 0, y = y_st + dy * 2 - 20)
label2 = tk.Label(window, fg = 'red', textvariable = msg)
label2.pack()
label2.place(x = x_st + dx * 0, y = y_st + dy * 2 + 80)

# 加入 Checkbutton
dx2 = dx * 4 / 4   #為了微調距離用
for i in range(0, len(stage_no)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text = stage_no[i], variable = choice[i], command = choose)
    item.pack()
    item.place(x = x_st + dx2 * (i % 6), y = y_st + dy * 2 + int(i / 6) * 25)


# 加入 Text
text1 = tk.Text(window, width = 100, height = 10)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3 + 50)



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def button01Click():
    print('你按了 選取檔案')
    button01_text.set("選取檔案...")
    file = askopenfile(parent = window, mode = 'rb', title = "選取檔案", filetypes = [("選取檔案", "*.*")])
    if file:
        global db_filename
        db_filename = file.name
        message = '選取檔案 : ' + db_filename
        print(message)
        text1.insert('end', message)
        main_message1.set(message)

    button01_text.set("選取檔案")


#開啟資料庫按鈕
#button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '開啟資料庫')
#button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01_text = tk.StringVar()
#button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(window, textvariable = button01_text, width = w, height = h, command = lambda:button01Click())
#button01 = tk.Button(window, command = xxxxxxx, text='選取檔案')
button01_text.set("選取檔案")
button01.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個





window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


"""


button_exit = tk.Button(window, text = "關閉視窗標準版", command = window.destroy)
                                                                   

"""
