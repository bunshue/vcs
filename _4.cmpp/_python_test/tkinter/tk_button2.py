import tkinter as tk

window = tk.Tk()

count =0;

def buttonClick():
    global count
    count = count + 1
    print("Beep! " +str(count))
    button1.config(text="Clicked " + str(count))

def buttonExit():
    window.quit();

button = tk.Button(window, text='PUSH!')    #無動作
button.pack()


button5 = tk.Button(window, text='Very Wide Button', width=50, height = 5).pack()
#button5.pack()

button1 = tk.Button(window, text="Click me!", command=buttonClick)
button1.pack(side=tk.LEFT)

button2 = tk.Button(window, text="Exit", command=buttonExit)
button2.pack(side=tk.LEFT)

#side=tk.RIGHT


'''
btn0 = tk.Button(window, text='btn(0, 0)')
btn1 = tk.Button(window, text='btn(1, 0)')
btn2 = tk.Button(window, text='btn(0, 1)')
btn3 = tk.Button(window, text='btn(1, 1)')

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=1, column=0)
btn3.grid(row=1, column=1)
'''

button1 = tk.Button(window, text='pos(0, 0)', width=10, height = 2)
button2 = tk.Button(window, text='pos(50, 50)', width=10, height = 2)
button3 = tk.Button(window, text='pos(100, 100)', width=10, height = 2)

button1.place(x=0, y=0)
button2.place(x=50, y=50)
button3.place(x=100, y=100)


print("建立toolbar");

def callback():
    print("called the callback!")

# create a toolbar
toolbar = tk.Frame(window)

b = tk.Button(toolbar, text="new", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

b = tk.Button(toolbar, text="open", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)



window.mainloop()

window.destroy()    # 使用quit()離開上面的mainloop
