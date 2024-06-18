import sys
import tkinter as tk

W = 200
H = 200
w = 28
h = 3

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('button 1')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button5 = tk.Button(window, text = '指定按鍵大小/背景色', width = w, height = h, bg = 'pink')
button5.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

font_size = 20
button1a = tk.Button(window, text = "指定字型大小/字體色/背景色", foreground = "gold", bg = 'red', font = ("標楷體", font_size))
button1a.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

ft2 = ('標楷體', 18)

button1b = tk.Button(window, text = '設定字型', font = ft2, underline=0)
button1b.pack()

button = tk.Button(window, text = "Welcome", underline=0).pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def setup_bg_color():
     #改變背景顏色
     button2a.config(bg = "blue")  

button2a = tk.Button(window, text="改變Button之背景顏色", width = w, height = h, command=setup_bg_color)
button2a.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
#frame0.grid(row = 1, column = 1, sticky = tk.W)
frame0.pack()

# Create images
plusImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/plus.gif")
minusImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/minus.gif")
timesImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/times.gif")
divideImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/divide.gif")

tk.Button(frame0, image = plusImage, command = '').grid(row = 1, column = 1, sticky = tk.W)
tk.Button(frame0, image = minusImage, command = '').grid(row = 1, column = 2)
tk.Button(frame0, image = timesImage, command = '').grid(row = 1, column = 3)
tk.Button(frame0, image = divideImage, command = '').grid(row = 1, column = 4)

# Add buttons to frame2
frame2 = tk.Frame(window) # Create and add a frame to window
#frame2.grid(row = 3, column = 1, pady = 10, sticky = tk.E)
frame2.pack()
tk.Button(frame2, text = "Add", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Subtract", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Multiply", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Divide", command = '').pack(side = tk.LEFT)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(window, bg = '', width = W, height = H)
frame1.pack()

label=tk.Label(frame1,bitmap="hourglass")
label.grid(row = 0, column = 0, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="left",text="我的天空")
label.grid(row = 0, column = 1, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="top",text="我的天空")
label.grid(row = 0, column = 2, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="center",text="我的天空")
label.grid(row = 0, column = 3, padx = 5, pady = 5)

label=tk.Label(frame1, width = 12, height = 3, text="raised",relief="raised")
label.grid(row = 0, column = 4, padx = 5, pady = 5)

label=tk.Label(frame1, width = 12, height = 3, text="raised",relief="raised",bg="lightyellow",padx=5,pady=10)
label.grid(row = 0, column = 5, padx = 5, pady = 5)

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

idx = 0
for Relief in Reliefs:
    tk.Label(frame1,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").grid(row = 1, column = idx, padx = 5, pady = 5)
    idx += 1
    
bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

idx = 0
for bitMap in bitMaps:
    tk.Label(frame1,bitmap=bitMap).grid(row = 2+(idx//6), column = idx % 6, padx = 5, pady = 5)
    idx += 1


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, 			
			anchor = tk.E,			# 指定文字對齊模式
			text = 'Button1',			# 指定按鈕上的文字
			width = 30,				# 指定按鈕的寬度，相當於40個字元
			height = 3)				# 指定按鈕的高度，相當於5行字元
button1.pack()							# 將按鈕新增到視窗

button4 = tk.Button(window, 			
			text = 'Button4',	
			width = 30,		
			height = 3,		
			state = tk.DISABLED)		# 指定按鈕為禁用狀態
button4.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('button 2')

#使用side
button1 = tk.Button(window, text = "按鈕 視窗最右邊", width = 20)
button1.pack(padx = 20, pady = 5, side = "right")
button2 = tk.Button(window, text = "按鈕 視窗最左邊", width = 20)
button2.pack(padx = 20, pady = 5, side = "left")
button3 = tk.Button(window, text = "按鈕 視窗最下邊", width = 20)
button3.pack(padx = 20, pady = 5, side = "bottom")
button4 = tk.Button(window, text = "按鈕 視窗最上邊", width = 20)
button4.pack(padx = 20, pady = 5)

#使用anchor
button1 = tk.Button(window, text = "按鈕 視窗正中央", width = 20)
button1.place(relx = 0.5, rely = 0.5, anchor = "center")
button2 = tk.Button(window, text = "按鈕 視窗左上", width = 20)
button2.place(relx = 0.1, rely = 0.1, anchor = "nw")
button3 = tk.Button(window, text = "按鈕 視窗左下", width = 20)
button3.place(relx = 0.1, rely = 0.8, anchor = "w") #???

#使用pad
button1 = tk.Button(window, text = "這是按鈕一b 有 pad", width = 20)
button1.pack(padx = 20, pady = 5)
button2 = tk.Button(window, text = "這是按鈕二b 有 pad", width = 20)
button2.pack(padx = 20, pady = 5)
button3 = tk.Button(window, text = "這是按鈕三b 有 pad", width = 20)
button3.pack(padx = 20, pady = 5)
button4 = tk.Button(window, text = "這是按鈕四b 有 pad", width = 20)
button4.pack(padx = 20, pady = 5)

#直接pack, 無參數
button1 = tk.Button(window, text = "這是按鈕一c 無 pad", width = 20)
button1.pack()
button2 = tk.Button(window, text = "這是按鈕二c 無 pad", width = 20)
button2.pack()
button3 = tk.Button(window, text = "這是按鈕三c 無 pad", width = 20)
button3.pack()
button4 = tk.Button(window, text = "這是按鈕四c 無 pad", width = 20)
button4.pack()

#使用place
x_st = 600
y_st = 50
dx = 120;
dy = 80;
w = 12
h = 3

button0 = tk.Button(window, text = "用place 0", width = w, height = h, command = '')
button0.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button1 = tk.Button(window, text = "用place 1", width = w, height = h, command = '')
button1.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button2 = tk.Button(window, text = "用place 2", width = w, height = h, command = '')
button2.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button3 = tk.Button(window, text = "用place 3", width = w, height = h, command = '')
button3.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button0.place(x = x_st + dx * 0, y = y_st + dy * 0)
button1.place(x = x_st + dx * 0, y = y_st + dy * 1)
button2.place(x = x_st + dx * 0, y = y_st + dy * 2)
button3.place(x = x_st + dx * 0, y = y_st + dy * 3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x900")
window.title('button 3')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def click_picture_button():
   print("你按了圖片做成的按鈕")

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

img = ImageTk.PhotoImage(Image.open(filename))
picture_button =tk.Button(window,text="圖片按鈕", image=img ,command=click_picture_button)
picture_button.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    button1 = tk.Button(window, text = item, state = item)
    button1.pack()    #以元件加入主視窗

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('連續建立多個button, 使用Button屬性state')
tk.Label(window,text="建立3個button, normal").pack()
for i in range(3):
    button = tk.Button(window, text = 'button'+str(i), state = 'normal')
    button.pack()

tk.Label(window,text="建立3個button, active").pack()
for i in range(3):
    button = tk.Button(window, text = 'button'+str(i), state = 'active')
    button.pack()

tk.Label(window,text="建立3個button, disabled").pack()
for i in range(3):
    button = tk.Button(window, text = 'button'+str(i), state = 'disabled')
    button.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


