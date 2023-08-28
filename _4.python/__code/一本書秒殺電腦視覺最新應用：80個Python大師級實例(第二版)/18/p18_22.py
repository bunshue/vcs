import tkinter as tk 
window = tk.Tk()
window.title('窗口菜单')
window.geometry('200x200') 
l = tk.Label(window, text='', bg='blue')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
 
#创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
#定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)
#将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='文件', menu=filemenu)
#在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
#如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)#同样的在`文件`中加入`打开`小菜单
filemenu.add_command(label='保存', command=do_job)#同样的在`文件`中加入`保存`小菜单
filemenu.add_separator()#这里就是一条分割线
#同样的在`文件`中加入`编辑`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='编辑', command=window.quit)
 
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='剪切', command=do_job)
editmenu.add_command(label='复制', command=do_job)
editmenu.add_command(label='粘贴', command=do_job)
#和上面定义菜单一样，不过此处实在`文件`上创建一个空的菜单
submenu = tk.Menu(filemenu)
#给放入的菜单`子菜单`命名为`导入`
filemenu.add_cascade(label='导入', menu=submenu, underline=0)
#这里和上面也一样，在`导入`中加入一个小菜单命令`子菜单1`
submenu.add_command(label="子菜单1", command=do_job)
window.config(menu=menubar) 
window.mainloop()
