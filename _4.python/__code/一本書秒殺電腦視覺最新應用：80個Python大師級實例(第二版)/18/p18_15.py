from tkinter import *
#创建容器
tk=Tk()
tk.title("我的GUI界面学习")
#主界面容器
mainfarm=Frame()
mainfarm.pack()

lab1=Label(mainfarm,text="你好，这是Checkbutton操作界面")
lab1.pack()
def button1back_handle():
    print("button1 down")
button2val=IntVar()
button2=Checkbutton(mainfarm,
                    text='BUTTON2',
                    variable=button2val,  #variable为按键的状态值
                    anchor="n",  # 按键文本位置为n
                    bd=5,  # 将borderwidth（边框宽度）设置为5
                    command=button1back_handle,  # 传入回调函数
                    justify="left",  # 按键文本为左对齐
                    cursor="right_ptr",  # 将光标移动至按键时的显示修改为
                    font=("宋体", 15, "bold", "italic"),  # 设置按键的字体、大小、加粗、斜体
                    padx=5, pady=5,  # 指定按键文本或图像距离边框的距离
                    relief=RAISED,  # 指定按键的样式
                    state=ACTIVE,  # 指定按键的状态
                    width=10, height=5,  # 制定按键的宽、高
                    )
button2.pack()
#为了看到按键值使用Lable控件显示下按键的值
Label(mainfarm,textvariable=button2val).pack()
mainloop()
