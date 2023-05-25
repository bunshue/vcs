import tkinter as tk

def buttonClick():
    print("你按了button")

window = tk.Tk()
window.title("範例一")
window.geometry("500x300") #沒有設定寬x高，將依元件調整視窗大小
tk.Button(window, text = "下載資料", command = buttonClick).pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
window.mainloop()


