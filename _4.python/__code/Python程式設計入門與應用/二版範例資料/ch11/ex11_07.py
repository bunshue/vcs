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
onButton=tkinter.Button(top,text="on",command=onPress)
offButton=tkinter.Button(top,text="off",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()