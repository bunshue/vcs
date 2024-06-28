"""
Combobox 下拉式選單

Combobox 下拉選單是 tkinter 的 ttk 加強模組裡的元件

"""

import sys
import tkinter as tk
import tkinter.ttk as ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Combobox 測試")

items = ("鼠", "牛", "虎")
animal_string = tk.StringVar(value=items[0])
combobox1 = ttk.Combobox(window, textvariable=animal_string)
combobox1["values"] = items
# combobox1.configure(values = items)
combobox1.pack()

# events
combobox1.bind(
    "<<ComboboxSelected>>",
    lambda event: label1.config(text=f"你選擇了 : {animal_string.get()}"),
)

label1 = ttk.Label(window, text="a label")
label1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def combobox_select2(event):
    labelVar.set(comboboxVar2.get())


comboboxVar2 = tk.StringVar()
combobox2 = ttk.Combobox(window, textvariable=comboboxVar2)
combobox2["value"] = ("鼠", "牛", "虎")
combobox2.current(0)  # 預設第一個選項
combobox2.bind("<<ComboboxSelected>>", combobox_select2)  # 設定選取選項後執行的程式
combobox2.pack()

labelVar = tk.StringVar()
label2 = tk.Label(window, textvariable=labelVar)
labelVar.set(comboboxVar2.get())
label2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def combobox_select3(event):  # 下拉選單選取選項後執行的程式
    city = comboboxVar3.get()  # 使用者選取的選項
    print(city)
    if city != "請選擇：":  # 選擇縣市
        showdata = city + " 天氣資料：\n"

        labelVar.set(showdata)
    else:
        labelVar.set("請選擇動物")


comboboxVar3 = tk.StringVar()
combobox3 = ttk.Combobox(window, textvariable=comboboxVar3)  # 下拉式選單元件
combobox3["value"] = (
    "請選擇：",
    "鼠",
    "牛",
    "虎",
)  # 設定選項
combobox3.current(0)  # 預設第一個選項
combobox3.bind("<<ComboboxSelected>>", combobox_select3)  # 設定選取選項後執行的程式
combobox3.pack()

labelVar = tk.StringVar()
label3 = tk.Label(window, foreground="red", justify="left", textvariable=labelVar)
labelVar.set("尚未選擇動物")
label3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def combobox_select4(event):
    label_text.set(comboboxVar4.get())


comboboxVar4 = tk.StringVar()
combobox4 = ttk.Combobox(window, textvariable=comboboxVar4)  # 下拉式選單元件
combobox4["value"] = ("鼠", "牛", "虎")
combobox4.current(0)  # 預設第一個選項
combobox4.bind("<<ComboboxSelected>>", combobox_select4)  # 設定選取選項後執行的程式
combobox4.pack()

label_text = tk.StringVar()
label4 = tk.Label(window, textvariable=label_text)
label_text.set(comboboxVar4.get())
label4.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def combobox_select5(event):  # 顯示選項
    labelVar.set(comboboxVar5.get())  # 同步標籤內容


comboboxVar5 = tk.StringVar()
combobox5 = ttk.Combobox(window, textvariable=comboboxVar5)
combobox5["value"] = ("鼠", "牛", "虎")
combobox5.current(0)  # 設定預設選項
combobox5.bind("<<ComboboxSelected>>", combobox_select5)  # 綁定
combobox5.pack()

labelVar = tk.StringVar()
label5 = tk.Label(window, textvariable=labelVar)
labelVar.set(comboboxVar5.get())  # 設定Label的初值
label5.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def combobox_select8():
    print(comboboxVar8.get())
    print(f"{combobox8.current()}:{combobox8.get()}")  # 顯示索引值與內容

comboboxVar8 = tk.StringVar()
comboboxVar8.set("")

# combobox8 = ttk.Combobox(window, width=15, values=["鼠", "牛", "虎"])
# combobox8 = ttk.Combobox(window, textvariable=comboboxVar8, value=("鼠", "牛", "虎")) # same
combobox8 = ttk.Combobox(window, textvariable=comboboxVar8)
combobox8["value"] = ("鼠", "牛", "虎")
combobox8.current(0)  # 預設
#comboboxVar8.set("牛")  # 預設
combobox8.pack()

label8 = tk.Label(window, textvariable=comboboxVar8)  # 建立標籤，內容為變數
label8.pack()

btn = tk.Button(window, text="選擇", command=combobox_select8)
btn.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def combobox_select9(event):
    selected_area = event.widget.get()
    label9.config(text=selected_area)


area = tk.StringVar()
items = ("鼠", "牛", "虎")
combobox9 = ttk.Combobox(window, value=items, textvariable=area)
combobox9.bind("<<ComboboxSelected>>", combobox_select9)
combobox9.current(0)
combobox9.pack()

label9 = tk.Label(window, fg="black", width=18)
label9.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個




window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


