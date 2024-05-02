"""
Grid 測試 grid
"""

import tkinter as tk

def get_data():
    print('取得資料')
    data1 = entry_1_0.get()
    data2 = entry_1_1.get()
    data3 = entry_1_2.get()
    data4 = int(spinbox_3_0.get())
    data5 = entry_3_1.get()
    data6 = float(spinbox_3_2.get())
    print(data1, data2, data3, data4, data5, data6)
    
def set_data():
    print('設定資料')
    

def clear_data():
    print('清除資料')
    entry_1_0.delete(0, tk.END)
    entry_1_1.delete(0, tk.END)
    entry_1_2.delete(0, tk.END)
    spinbox_3_0.delete(0, tk.END)
    spinbox_3_0.insert(0, "1")
    entry_3_1.delete(0, tk.END)
    spinbox_3_2.delete(0, tk.END)
    spinbox_3_2.insert(0, "0.0")

window = tk.Tk()
window.title("grid 測試")

frame = tk.Frame(window)
frame.pack(padx = 20, pady = 10)

print('第 0 row, Label')
label_0_0 = tk.Label(frame, text = "Label 0 0")
label_0_0.grid(row = 0, column = 0)
label_0_1 = tk.Label(frame, text = "Label 0 1")
label_0_1.grid(row = 0, column = 1)
label_0_2 = tk.Label(frame, text = "Label 0 2")
label_0_2.grid(row = 0, column = 2)

print('第 1 row, Entry')
entry_1_0 = tk.Entry(frame)
entry_1_0.grid(row = 1, column = 0)
entry_1_1 = tk.Entry(frame)
entry_1_1.grid(row = 1, column = 1)
entry_1_2 = tk.Entry(frame)
entry_1_2.grid(row = 1, column = 2)

print('第 2 row, Label')
label_2_0 = tk.Label(frame, text = "Label 2 0")
label_2_0.grid(row = 2, column = 0)
label_2_1 = tk.Label(frame, text = "Label 2 1")
label_2_1.grid(row = 2, column = 1)
label_2_2 = tk.Label(frame, text = "Label 2 2")
label_2_2.grid(row = 2, column = 2)

print('第 3 row, Spinbox Entry Spinbox')
spinbox_3_0 = tk.Spinbox(frame, from_ = 1, to = 100)
spinbox_3_0.grid(row = 3, column = 0)

entry_3_1 = tk.Entry(frame)
entry_3_1.grid(row = 3, column = 1)

spinbox_3_2 = tk.Spinbox(frame, from_ = 0.0, to = 500, increment = 0.5)
spinbox_3_2.grid(row = 3, column = 2)

print('第 4 row, Button')
button_4_0 = tk.Button(frame, text = "Button 4 0")
button_4_0.grid(row = 4, column = 0, pady = 5)

button_4_1 = tk.Button(frame, text = "Button 4 1")
button_4_1.grid(row = 4, column = 1, pady = 5)

button_4_2 = tk.Button(frame, text = "Button 4 2")
button_4_2.grid(row = 4, column = 2, pady = 5)

print('第 5 row, Button')
button_5_0 = tk.Button(frame, text = "取得資料", command = get_data)
button_5_0.grid(row = 5, column = 0, pady = 5)

button_5_1 = tk.Button(frame, text = "設定資料", command = set_data)
button_5_1.grid(row = 5, column = 1, pady = 5)

button_5_2 = tk.Button(frame, text = "清除資料", command = clear_data)
button_5_2.grid(row = 5, column = 2, pady = 5)

button_row6 = tk.Button(frame, text = "橫跨的大Button")
button_row6.grid(row = 6, column = 0, columnspan = 3, sticky = "news", padx = 20, pady = 5)
button_row7 = tk.Button(frame, text = "橫跨的大Button")
button_row7.grid(row = 7, column = 0, columnspan = 3, sticky = "news", padx = 20, pady = 5)

window.mainloop()

