import tkinter as tk
window = tk.Tk()

count = 0


def buttonClick():
    global count
    count = count + 1
    button.config(text="按這裡" + str(count))
    stringToCopy = entry1.get()  #加了輸入欄位
    print(str(count) + " 使用者按了一下，取得資料:" + stringToCopy)
    entry2.insert(0, stringToCopy)
    result = "資料" + stringToCopy;
    label2.config(text=result)


label1 = tk.Label(window, text="使用Label")
label2 = tk.Label(window, text="")
entry1 = tk.Entry(window)    #加了輸入欄位
entry2 = tk.Entry(window)    #加了輸入欄位
button = tk.Button(window, text="按這裡", command=buttonClick)
label1.pack()
label2.pack()
entry1.pack()    #加了輸入欄位
entry2.pack()    #加了輸入欄位
button.pack()
window.mainloop()
