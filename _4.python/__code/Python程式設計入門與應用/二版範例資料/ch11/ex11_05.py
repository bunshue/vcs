# ex11_05.py 利用按鈕控制LED燈
import tkinter
import pyfirmata
from time import sleep
pin=10
port = 'COM7'
board=pyfirmata.Arduino(port)
sleep(5)
top=tkinter.Tk()
top.minsize(300,20)
def onPress():
    board.digital[pin].write(1)
def offPress():
    board.digital[pin].write(0)
onButton=tkinter.Button(top,text="打開LED燈",command=onPress)
offButton=tkinter.Button(top,text="關閉LED燈",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()