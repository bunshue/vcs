"""
测试OptionMenu(选择项)
用来做多选一，选中的项在顶部显
"""
import tkinter
def show():
    varLabel.set(var.get())
root = tkinter.Tk()
tupleVar = ('python', 'java', 'C', 'C++', 'C#')
var = tkinter.StringVar()
var.set(tupleVar[0])
optionMenu = tkinter.OptionMenu(root, var, *tupleVar)
optionMenu.pack()
varLabel = tkinter.StringVar()
label = tkinter.Label(root, textvariable=varLabel, width=20, height=3, bg='lightblue', fg='red')
label.pack()
button = tkinter.Button(root, text='打印', command=show)
button.pack()
root.mainloop()
