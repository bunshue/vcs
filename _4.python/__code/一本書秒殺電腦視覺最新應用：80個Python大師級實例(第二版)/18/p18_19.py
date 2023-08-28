import tkinter as tk
window=tk.Tk()              #实例化一个窗口
window.title('Scale组件')   #定义窗口标题
window.geometry('400x600')  #定义窗口大小 
l=tk.Label(window,bg='yellow',width=20,height=2,text='未选择')
l.pack() 
def print_selection(V):
    l.config(text='你已选择'+V) 
s=tk.Scale(window,label='进行选择',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=0.01,command=print_selection)
s.pack() #显示名字,条方向;长度（像素），是否直接显示值，标签的单位长度，保留精度，定义功能
window.mainloop()
