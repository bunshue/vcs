#coding=utf-8
 import tkinter
def handler(event, a, b, c):
    '''事件处理函数'''
    print(event)
    print ("handler", a, b, c) 
def handlerAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds) 
if __name__=='__main__':
    root = tkinter.Tk()
    btn = tkinter.Button(text=u'按钮') 
    # 通过中介函数handlerAdaptor进行事件绑定
    btn.bind("<Button-1>", handlerAdaptor(handler, a=1, b=2, c=3)) 
    btn.pack()
    root.mainloop()
