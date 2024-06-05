import tkinter as tk
'''
print("------------------------------------------------------------")  # 60個

def get_entry_data():
    print('你按了 get')
    cc = entry1.get()
    print(cc)
    cc = entry2.get()
    print(cc)
    
window = tk.Tk()
window.title("取得 Entry 資料")

name_data = tk.StringVar()#名字
weight_data = tk.IntVar()#體重

entry1 = tk.Entry(window, foreground = "green", textvariable = name_data)
entry1.pack()

entry2 = tk.Entry(window, foreground = "green", textvariable = weight_data)
entry2.pack()

tk.Button(window, text = "取得上面Entry的資料", command = get_entry_data).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk

def validate():
    print('你按了 Validate')
    cc = entry1.get()
    print(cc)
    
window = tk.Tk()

frame1 = tk.Frame(window)
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

text = tk.Text(frame1, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()

scrollbar.config(command = text.yview)

frame2 = tk.Frame(window)
frame2.pack()

tk.Label(frame2, text = "Enter a filename: ").pack(side = tk.LEFT)

filename = tk.StringVar()
entry1 = tk.Entry(frame2, width = 40, textvariable = filename)
entry1.pack(side = tk.LEFT)

tk.Button(frame2, text = "Validate", command = validate).pack()

window.mainloop()
'''

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('LabelFrame')
window.geometry('400x400')

labelFrame1=tk.LabelFrame(window,text='設定：',relief='raised',borderwidth=2)
labelFrame1.pack(pady=5)

tk.Label(labelFrame1,text='編碼器：').grid(row=0,column=0,pady=3)

spinboxFourcc=tk.Spinbox(labelFrame1,value=('XVID','DIVX','MJPG','I420'),width=10)
spinboxFourcc.grid(row=0,column=1,pady=3,sticky='w')

tk.Label(labelFrame1,text='檔名：').grid(row=2,column=0,pady=3)

entry1 = tk.Entry(labelFrame1, width=20)
entry1.grid(row=2,column=1,pady=3,sticky='w')

tk.Label(labelFrame1,text='AAAAA').grid(row=3,column=0,columnspan=2)

button1=tk.Button(labelFrame1, text='BBBBB')
button1.grid(row=4,column=0,columnspan=1)

button2=tk.Button(labelFrame1, text='CCCCC')
button2.grid(row=4,column=1,columnspan=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

