import tkinter as tk
window = tk.Tk()

count = 0

def buttonClick():
    global count
    count = count + 1
    try:
        number = int(entry1.get())  #加了輸入欄位
        if 0 < number < 20:
            print(str(count) + " 使用者按了一下，取得資料:" + str(number))
            result = "第" + str(count) + "次取得數字:" + str(number);
            label2.config(text=result)
        else:
            print(str(count) + " 使用者按了一下，取得數字不合法")
            result = "第" + str(count) + "次取得數字:" + str(number) + "不合法";
            label2.config(text=result)
    except:
        print(str(count) + " 使用者按了一下，取得不是數字")
        result = "第" + str(count) + "次取得不是數字";
        label2.config(text=result)
    entry1.delete(0, tk.END)

label1 = tk.Label(window, text="請輸入<20的正整數")
label2 = tk.Label(window, text="")
entry1 = tk.Entry(window)    #加了輸入欄位
button = tk.Button(window, text="確定", command=buttonClick)
label1.pack()
label2.pack()
entry1.pack()    #加了輸入欄位
button.pack()
window.mainloop()
