import sys

import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('button 1')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button5 = tk.Button(window, text = '指定按鍵大小', width = 20, height = 5)
button5.pack()  #pack無參數, 控件置中

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label = tk.Label(window, text="改變鼠標外形", relief="raised",
            width=28, height = 3,
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# Button測試
tk.Label(text = 'Button測試').pack()
def buttonClick1():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")

labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg = "red", textvariable = labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable = btntext, command = buttonClick1)
btntext.set("按我！")
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick2():
    textvar.set("我已經被按過了！")

textvar = tk.StringVar()
button1 = tk.Button(window, textvariable = textvar, command = buttonClick2)
textvar.set("按鈕")
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick3():
    global count
    count = count + 1
    print("Beep! " + str(count))
    button1.config(text = "Clicked " + str(count))

count = 0;

button1 = tk.Button(window, text = "按鍵數次數, 不指定按鍵大小", command = buttonClick3)
button1.pack(side = tk.LEFT)    #靠左對齊

button2 = tk.Button(window, text = "離開", command = '')
button2.pack(side = tk.RIGHT)   #靠右對齊

#side=tk.RIGHT

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
window.geometry("600x800")
window.title('button 3')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick4():
   print("btn1 pressed.")

btn1 =tk.Button(window,text="press me",command=buttonClick4)
btn1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick5():
   print("btn2 pressed.")

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

img = ImageTk.PhotoImage(Image.open(filename))
btn2 =tk.Button(window,text="press me", image=img ,command=buttonClick5)
btn2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick6():
    print('你按了按鍵')

btn3 = tk.Button(window, text = "Say Hello", command = buttonClick6)
btn3.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, 			
			anchor = tk.E,			# 指定文字對齊模式
			text = 'Button1',			# 指定按鈕上的文字
			width = 40,				# 指定按鈕的寬度，相當於40個字元
			height = 5)				# 指定按鈕的高度，相當於5行字元
button1.pack()							# 將按鈕新增到視窗

button2 = tk.Button(window, 			
			text = 'Button2',	
			bg = 'blue')				# 指定按鈕的背景色
button2.pack()

button3 = tk.Button(window, 			
			text = 'Button3',	
			width = 14,				# 指定按鈕的寬度
			height = 1)				# 指定按鈕的高度
button3.pack()

button4 = tk.Button(window, 			
			text = 'Button4',	
			width = 60,		
			height = 5,		
			state = tk.DISABLED)		# 指定按鈕為禁用狀態
button4.pack()



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title('button 3')

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


