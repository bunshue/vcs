from tkinter import *
def main():
    root = Tk()  # 注意Tk的大小写
    photo = PhotoImage(file='house.png')
    the_label = Label(root,
                      text='古典建筑',
                      justify=LEFT,  #字符串进行左对齐
                      image=photo,
                      compound=CENTER,  # 混合模式,文字在图片的正上方显示
                      font=("方正粗黑宋简体", 24),  #字体和大小
                      fg='red'  # 前景颜色，就是字体颜色
                      )

    the_label.pack()  #这句不可少呀
    mainloop()
if __name__ == '__main__':
    main()
