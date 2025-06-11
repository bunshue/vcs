import time
import datetime
import tkinter as tk


def stopwatch_start():
    global flag_start
    global stopwatch_time_st
    flag_start = True
    stopwatch_time_st = time.time()
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("開始計數時間 :", now)


def stopwatch_stop():
    global flag_start
    global stopwatch_time_st
    flag_start = False
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("\n停止計數時間 :", now)
    stopwatch_time_elapsed = time.time() - stopwatch_time_st
    print("計數時間 :", int(stopwatch_time_elapsed), "秒")


def stopwatch_reset():
    global flag_start
    global stopwatch_time_st
    global counter
    counter = 0


window = tk.Tk()
window.title("Counter")
window.geometry("480x300")
# window.resizable(1,1)

text_font = ("Boulder", 68, "bold")
background = "#f2e750"
foreground = "#363529"
border_width = 25


label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.pack(fill=tk.X, padx=5, pady=5)

button1 = tk.Button(window, text="開始", command=stopwatch_start)
button1.pack(padx=5, pady=5)
button1 = tk.Button(window, text="停止", command=stopwatch_stop)
button1.pack(padx=5, pady=5)
button1 = tk.Button(window, text="歸零", command=stopwatch_reset)
button1.pack(padx=5, pady=5)


flag_start = False
counter = 0  # 儲存數值


# 自訂函式一：顯示標籤(Label)元件
def display(label):
    counter = 0

    # 自訂函式二
    def count():
        global counter
        global flag_start

        if flag_start == False:
            counter = counter
        else:
            counter += 1
            stopwatch_time_elapsed = time.time() - stopwatch_time_st
            counter = round(stopwatch_time_elapsed, 3)
        label.config(text=str(counter))
        label.after(37, count)  # ms

    count()


display(label1)

window.mainloop()
