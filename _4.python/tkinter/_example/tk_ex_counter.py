import time
import datetime
import tkinter as tk

window = tk.Tk() 
window.title("Counter")
window.geometry("420x250")
window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

record_time_st = time.time()
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("開始錄影時間 :", now)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label1.grid(row=0, column=1)
button1 = tk.Button(window, text = '離開', command = window.destroy)
button1.grid(row=1, column=1)

counter = 0 #儲存數值

# 自訂函式一：顯示標籤(Label)元件
def display(label):
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      label.config(text = str(counter))
      label.after(100, count) #ms
   count()
   
display(label1)

window.mainloop()

print(counter // 10)

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("\n停止時間 :", now)
record_time_elapsed = time.time() - record_time_st
print("錄影時間 :", int(record_time_elapsed), "秒")
