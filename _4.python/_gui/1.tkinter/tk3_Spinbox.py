import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Spinbox 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def get_spinbox_data():
    print("你選擇了 :", spinbox3a.get())


spinbox3a = tk.Spinbox(window, values=["AAA", "BBB", "CCC", "DDD"], width=10)
spinbox3a.pack()

button4 = tk.Button(window, text="取得Spinbox資料", command=get_spinbox_data)
button4.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def show_spinbox_selection():
    print("你選擇了 :", spinbox1.get())  # 取得選取資料
    cc = spinbox1.get()  # 取得選取資料
    label1.config(text=cc)


tk.Label(window, text="tk之spinbox").pack()
spinbox1 = tk.Spinbox(
    window, from_=10, to=30, increment=2, command=show_spinbox_selection
)
spinbox1.pack()

label1 = tk.Label(window, fg="red")
label1.pack()


tk.Label(window, text="ttk之spinbox").pack()
spinbox2 = ttk.Spinbox(window, from_=0, to=100, increment=0.1)
spinbox2.pack()

tk.Label(window, text="設定刻度").pack()
# spinbox3 = ttk.Spinbox(window, from_=0, to=10)
spinbox3 = ttk.Spinbox(window, values=(1, 2, 4, 8))
spinbox3.pack()

tk.Label(window, text="設定文字刻度").pack()

names = ("AAA", "BBB", "CCC")  # 以元組儲存數值
spinbox4 = tk.Spinbox(window, values=names, command="", width=20)
spinbox4.pack()

spinbox5 = tk.Spinbox(window, values=(10, 38, 170, 101), command="")
spinbox5.pack()

spinbox6 = tk.Spinbox(window, from_=0, to=10, command="")
spinbox6.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


# Spinbox
spin_int = tk.IntVar(value=12)
spinbox7 = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    command=lambda: print("a你選擇了 :", spin_int.get()),
    textvariable=spin_int,
)

spinbox7.bind("<<Increment>>", lambda event: print("a你選擇了 :", "up"))
spinbox7.bind("<<Decrement>>", lambda event: print("a你選擇了 :", "down"))
# spinbox7['value'] = (1,2,3,4,5)
spinbox7.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased

exercise_letters = ("AAA", "BBB", "CCC", "DDD")
exercise_string = tk.StringVar(value=exercise_letters[0])
spinbox8 = ttk.Spinbox(window, textvariable=exercise_string, values=exercise_letters)
spinbox8.pack()

spinbox8.bind("<<Decrement>>", lambda event: print("b你選擇了 :", exercise_string.get()))

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def spinbox_select():
    selected_month = month.get()
    label2.config(text=selected_month)


default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox9 = tk.Spinbox(
    window,
    from_=1,
    to=12,
    textvariable=month,
    command=spinbox_select,
    font=default_font,
)
spinbox9.pack()

label2 = tk.Label(window, font=default_font, fg="red")
label2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


import random


def fnTest():
    global ans  # 宣告ans為全域變數來記錄答案
    n = int(spnNum.get())  # 取得使用者選擇的位數
    num = [[1, 9], [10, 99], [100, 999]]  # 用二維串列儲存各位數的亂數範圍
    r1 = random.randint(num[n - 1][0], num[n - 1][1])
    r2 = random.randint(num[n - 1][0], num[n - 1][1])
    if r2 > r1:  # 若r2>r1就兩者互換
        r1, r2 = r2, r1
    if spnOpt.get() == "加法":  # 若選擇'加法'
        opt = "+"
        ans = r1 + r2
    else:
        opt = "-"
        ans = r1 - r2
    lblTest.config(text="{} {} {} =".format(r1, opt, r2))
    entAns.focus_set()
    buttonTest.config(state="disable")
    buttonAns.config(state="normal")


def fnAns():
    global ans
    userAns = int(entAns.get())
    if userAns == ans:
        msg.set("太棒了！答案正確！")
    else:
        msg.set("答錯了！答案是：{}".format(ans))
    buttonTest.config(state="normal")
    buttonAns.config(state="disable")


print("加減法測驗")

frmTest = tk.Frame(window, relief="raised", borderwidth=2)
frmTest.pack(side="left", padx=5, pady=3)
lblTest = tk.Label(frmTest, text=" ", font=("微軟正黑體", 20))
lblTest.pack(pady=5)
ans = tk.IntVar()
entAns = tk.Entry(frmTest, textvariable=ans)
entAns.pack(pady=5)
msg = tk.StringVar()
msg.set("設定後按 <出題> 鈕開始測驗")
lblMsg = tk.Label(frmTest, textvariable=msg)
lblMsg.pack(pady=5)
frmSet = tk.Frame(window, relief="raised", borderwidth=2)
frmSet.pack(side="left", padx=5, pady=3)
tk.Label(frmSet, text="運算：").pack(anchor="w")
lstOpt = ["加法", "減法"]
spnOpt = tk.Spinbox(frmSet, values=lstOpt)
spnOpt.pack(anchor="w")
tk.Label(frmSet, text="位數：").pack(anchor="w")
spnNum = tk.Spinbox(frmSet, from_=1, to=3)
spnNum.pack(anchor="w")

buttonTest = tk.Button(frmSet, text="出題", command=fnTest)
buttonTest.pack(side="left", pady=3)

buttonAns = tk.Button(frmSet, text="核對", command=fnAns, state="disable")
buttonAns.pack(side="right", pady=3)

ans = 0

window.mainloop()

print("------------------------------------------------------------")  # 60個


def press():
    print(sb2.get())


window = tk.Tk()
window.title("Spinbox測試")

ttk.Label(window, text="指定from、to、increment").pack()
# 通過指定from_、to、increament選項創建Spinbox
sb1 = tk.Spinbox(window, from_=18, to=50, increment=5)
sb1.pack(fill=tk.X, expand=tk.YES)
ttk.Label(window, text="指定values").pack()
# 通過指定values選項創建Spinbox
sb2 = tk.Spinbox(
    window, values=("Python", "C++", "Java", "PHY"), command=press
)  # 通過command綁定事件處理方法
sb2.pack(fill=tk.X, expand=tk.YES)
ttk.Label(window, text="綁定變量").pack()
intVar = tk.IntVar()
# 通過指定values選項創建Spinbox，并為之綁定變量
sb3 = tk.Spinbox(
    window,
    values=list(range(18, 50, -4)),
    textvariable=intVar,  # 綁定變量
    command=press,
)
sb3.pack(fill=tk.X, expand=tk.YES)
intVar.set(33)  # 通過變量改變Spinbox的值

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
