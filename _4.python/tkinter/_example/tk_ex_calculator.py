import tkinter as tk

print("------------------------------------------------------------")  # 60個


def calculate():  # 執行計算並顯示結果
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))


def show(buttonString):  # 更新顯示區的計算公式
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)


def backspace():  # 刪除前一個字元
    equ.set(str(equ.get()[:-1]))


def clear():  # 清除顯示區,放置0
    equ.set("0")


window = tk.Tk()
window.title("計算器")

equ = tk.StringVar()
equ.set("0")  # 預設是顯示0

# 設計顯示區
label = tk.Label(
    window, width=25, height=2, relief="raised", anchor=tk.SE, textvariable=equ
)
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# 清除顯示區按鈕
clearButton = tk.Button(window, text="C", fg="blue", width=5, command=clear)
clearButton.grid(row=1, column=0)
# 以下是row1的其它按鈕
tk.Button(window, text="DEL", width=5, command=backspace).grid(row=1, column=1)
tk.Button(window, text="%", width=5, command=lambda: show("%")).grid(row=1, column=2)
tk.Button(window, text="/", width=5, command=lambda: show("/")).grid(row=1, column=3)
# 以下是row2的其它按鈕
tk.Button(window, text="7", width=5, command=lambda: show("7")).grid(row=2, column=0)
tk.Button(window, text="8", width=5, command=lambda: show("8")).grid(row=2, column=1)
tk.Button(window, text="9", width=5, command=lambda: show("9")).grid(row=2, column=2)
tk.Button(window, text="*", width=5, command=lambda: show("*")).grid(row=2, column=3)
# 以下是row3的其它按鈕
tk.Button(window, text="4", width=5, command=lambda: show("4")).grid(row=3, column=0)
tk.Button(window, text="5", width=5, command=lambda: show("5")).grid(row=3, column=1)
tk.Button(window, text="6", width=5, command=lambda: show("6")).grid(row=3, column=2)
tk.Button(window, text="-", width=5, command=lambda: show("-")).grid(row=3, column=3)
# 以下是row4的其它按鈕
tk.Button(window, text="1", width=5, command=lambda: show("1")).grid(row=4, column=0)
tk.Button(window, text="2", width=5, command=lambda: show("2")).grid(row=4, column=1)
tk.Button(window, text="3", width=5, command=lambda: show("3")).grid(row=4, column=2)
tk.Button(window, text="+", width=5, command=lambda: show("+")).grid(row=4, column=3)
# 以下是row5的其它按鈕
tk.Button(window, text="0", width=12, command=lambda: show("0")).grid(
    row=5, column=0, columnspan=2
)
tk.Button(window, text=".", width=5, command=lambda: show(".")).grid(row=5, column=2)
tk.Button(window, text="=", width=5, bg="yellow", command=lambda: calculate()).grid(
    row=5, column=3
)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def fnKey(str):
    global exp  # 宣告exp為全域變數
    exp += str  # 運算式為原運算式加新輸入的字串
    lblExp.config(text=exp)  # 重設lblExp的文字為新運算式


def fnCls():
    global exp
    exp = ""  # 運算式設為空字串
    lblExp.config(text=exp)


def fnCal():
    global exp
    exp = str(eval(exp))  # 用eval方法計算運算式並轉型為字串
    lblExp.config(text=exp)


window = tk.Tk()
window.title("簡易計算機")
window.geometry("180x140")

lblExp = tk.Label(window, text="", width=18, relief="raised", bg="yellow")
lblExp.grid(row=0, column=0, columnspan=4)
tk.Button(window, text="7", width=3, command=lambda: fnKey("7")).grid(row=1, column=0)
tk.Button(window, text="8", width=3, command=lambda: fnKey("8")).grid(row=1, column=1)
tk.Button(window, text="9", width=3, command=lambda: fnKey("9")).grid(row=1, column=2)
tk.Button(window, text="/", width=3, command=lambda: fnKey("/")).grid(row=1, column=3)
tk.Button(window, text="4", width=3, command=lambda: fnKey("4")).grid(row=2, column=0)
tk.Button(window, text="5", width=3, command=lambda: fnKey("5")).grid(row=2, column=1)
tk.Button(window, text="6", width=3, command=lambda: fnKey("6")).grid(row=2, column=2)
tk.Button(window, text="*", width=3, command=lambda: fnKey("*")).grid(row=2, column=3)
tk.Button(window, text="1", width=3, command=lambda: fnKey("1")).grid(row=3, column=0)
tk.Button(window, text="2", width=3, command=lambda: fnKey("2")).grid(row=3, column=1)
tk.Button(window, text="3", width=3, command=lambda: fnKey("3")).grid(row=3, column=2)
tk.Button(window, text="-", width=3, command=lambda: fnKey("-")).grid(row=3, column=3)
tk.Button(window, text="0", width=3, command=lambda: fnKey("0")).grid(row=4, column=0)
tk.Button(window, text="C", width=3, command=fnCls).grid(row=4, column=1)
tk.Button(window, text="=", width=3, command=fnCal).grid(row=4, column=2)
tk.Button(window, text="+", width=3, command=lambda: fnKey("+")).grid(row=4, column=3)
exp = ""  # 預設運算式為空字串

window.mainloop()

print("------------------------------------------------------------")  # 60個
