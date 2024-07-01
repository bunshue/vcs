"""
Scrollbar

Text + Scrollbar

Listbox + Scrollbar

"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



""" 準備搬出

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



print("欲搜尋字串")
findstr = "aaaa"
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, filename))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, filename))

print("------------------------------------------------------------")  # 60個




def get_entry1_data():
    cc = entry1.get()
    print(cc)


entry1_data = tk.StringVar()
entry1 = tk.Entry(frame2, width=40, textvariable=entry1_data)
entry1.pack(side=tk.LEFT)

tk.Button(frame2, text="取得entry1資料", command=get_entry1_data).pack()



def getTextData3():
    mesg = text3.get("1.0", "end")
    print("取得Text的資料 :", mesg)



button1 = tk.Button(window, text="取得Text的資料", command=getTextData3)
button1.pack()


def add_text():
    text = "測試字串......."
    # 輸出到界面
    text4.delete(1.0, tk.END)
    text4.insert(1.0, text)

button3 = tk.Button(window, text="蓋過字串", command=add_text)
button3.pack()




"""
