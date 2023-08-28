from tkinter import *
root=Tk() 
#单选
LB1=Listbox(root) 
Label(root,text='单选：选择你的课程').pack()
for item in ['Chinese','English','Math']:
    LB1.insert(END,item)
LB1.pack() 
#多选
LB2=Listbox(root,selectmode=EXTENDED)
Label(root,text='多选：你会几种编程语言').pack()
for item in ['python','C++','C','Java','Php']:
    LB2.insert(END,item)
LB2.insert(1,'JS','Go','R')
LB2.delete(5,6)
LB2.select_set(0,3)
LB2.select_clear(0,1)
print (LB2.size())
print (LB2.get(3))
print(LB2.select_includes(3))
LB2.pack() 
root.mainloop()
