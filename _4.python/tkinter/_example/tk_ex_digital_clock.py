import time
import tkinter as tk

text_font = ("Boulder", 68, "bold")
background = "#f2e750"
foreground = "#363529"
border_width = 25

print("------------------------------------------------------------")  # 60個
"""
def digital_clock(): 
   show_time = time.strftime("%H:%M:%S")
   label1.config(text=show_time) 
   label1.after(200, digital_clock)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("420x150")
window.resizable(1,1)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

digital_clock()

window.mainloop()

print("------------------------------------------------------------")  # 60個

def digital_clock():
   global program_start_time
   show_time = time.time() - program_start_time
   label1.config(text=show_time) 
   label1.after(37, digital_clock)

window = tk.Tk()
window.title("Counter")
window.geometry("1000x150")
window.resizable(1,1)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

program_start_time = time.time()

digital_clock()

window.mainloop()

print("------------------------------------------------------------")  # 60個

num = 0
def fnAdd():
    global num		#宣告為全域變數
    num += 1		#num加1
    label2['text']=str(num)	#重設標籤文字
    if (num>0):		#若num大於0，就設歸零鈕可以使用
        button2['state']='normal'
    
def fnClear():
    global num
    num = 0
    label2['text']=str(num)
    button2['state']='disabled'  #設歸零鈕不能使用
 
window=tk.Tk()
window.geometry("600x400")
window.title('計數器')
window.configure(bg='white')

label1=tk.Label(window, text = '計數器',font=('標楷體', 16),fg='white',bg='blue')
label2=tk.Label(window, text = '0',font=('微軟正黑體', 36))

button1=tk.Button(window, text = '加 1',pady=5,padx=10,command=fnAdd)
button2=tk.Button(window, text = '歸零',pady=5,padx=10,command=fnClear,state='disabled')

label1.pack(pady=10,fill='x')
label2.pack(pady=20,fill='x')

button1.pack(pady=5, side='left',fill='x', expand=True)
button2.pack(pady=5, side='left',fill='x', expand=True)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def digital_clock():
    show_mesg = ""
    if time.time() > endTime:
        show_mesg = "時間到"
    else:
        minutesLeft = int(endTime - time.time()) // 60
        secondsLeft = int(endTime - time.time()) % 60
        show_mesg = "剩餘時間: {} 分 {} 秒".format(minutesLeft, secondsLeft)
    label1.config(text=show_mesg)
    label1.after(200, digital_clock)


window = tk.Tk()
window.title("Digital Clock")
window.geometry("900x150")
window.resizable(1, 1)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

TIME_TO_SOLVE = 300  # 秒
startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

digital_clock()

window.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
