"""
tk Toplevel 範例
"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

print('使用 Toplevel(頂級窗口) 開啟新視窗')

mesg = """
Toplevel(頂級窗口)組件類似于 Frame 組件，
但 Toplevel 組件是一個獨立的頂級窗口，
這種窗口通常擁有標題欄、邊框等部件。

Toplevel 組件通常用在顯示額外的窗口、對話框和其他彈出窗口上。
"""

def CreateNewWindow1():  # 建立對話方塊
    tl = tk.Toplevel()
    tl.geometry("300x180")
    tl.title("Toplevel")
    tk.Label(tl, width = 50, height = 5, bg = 'pink', text="Toplevel(頂級窗口)").pack()
    tk.Label(tl, width = 50, height = 5, bg = 'lime', text=mesg).pack()
    
window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window, text="開啟新視窗", command=CreateNewWindow1)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def CreateNewWindow2():  # 建立對話方塊
    tl = tk.Toplevel()  # 建立Toplevel視窗
    tl.geometry("300x180")  # 建立對話方塊大小
    tl.title("開啟新視窗")
    tk.Label(tl, text=mesg).pack(fill=tk.BOTH, expand=True)


button2 = tk.Button(window, text="開啟新視窗", command=CreateNewWindow2)
button2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 開啟新視窗
class MyDialog:  # 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)  # 產生Toplevel元件
        label = tk.Label(self.top, text="請輸入密碼")  # 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)  # 產生文字框元件
        self.entry.pack()
        self.entry.focus()  # 讓文字框獲得焦點
        button = tk.Button(self.top, text="Ok", command=self.Ok)
        button.pack()

    def Ok(self):
        self.input = self.entry.get()  # 取得文字框中內容，儲存為input
        self.top.destroy()  # 銷毀交談視窗

    def get(self):  # 傳回在文字框輸入的內容
        return self.input

def CreateNewWindow2():  # Create按鈕的事件處理函數
    d = MyDialog(window)  # 產生交談視窗
    button3.wait_window(d.top)  # 等待交談視窗結束
    print("你輸入了 :" + d.get())  # 取得交談視窗中輸入值，並輸出


button3 = tk.Button(
    window, text="開啟新視窗取得資料", command=CreateNewWindow2
)  # 設定Create按鈕的事件處理函數
button3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")

def popup():
    popupwindow = tk.Toplevel(window)
    popupwindow.title("新視窗")
    popupwindow.geometry("300x300")
    alert = tk.Label(popupwindow, text="已開啟新視窗")
    button1 = tk.Button(popupwindow, text="離開此視窗", command=popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()

button = tk.Button(window, text="開啟新視窗", command=popup)
button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個

extra_window = None


def button1_click():
    print("你按了子視窗的Button")


class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("extra window")
        self.geometry("300x400")
        tk.Label(self, text="A label").pack()
        tk.Button(self, text="A button", command=button1_click).pack()
        tk.Label(self, text="another label").pack(expand=True)


def create_window():
    global extra_window
    print("開啟子視窗")
    extra_window = Extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('extra window')
    # extra_window.geometry('300x400')
    # tk.Label(extra_window, text = 'A label').pack()
    # tk.Button(extra_window, text = 'A button').pack()
    # tk.Label(extra_window, text = 'another label').pack(expand = True)


def close_window():
    print("關閉子視窗")
    if extra_window != None:
        extra_window.destroy()
        print("已關閉子視窗")
    else:
        print("無子視窗可關閉")


# window
window = tk.Tk()
window.geometry("600x800")
window.title("Multiple windows")

button1 = tk.Button(window, text="開啟子視窗", command=create_window)
button1.pack(expand=True)

button2 = tk.Button(window, text="關閉子視窗", command=close_window)
button2.pack(expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

