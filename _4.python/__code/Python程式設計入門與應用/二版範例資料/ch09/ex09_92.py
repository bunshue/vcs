def checknum():
    pmsg.set("Small")
import tkinter as tk
import random as r
# create gui interface
win = tk.Tk()
win.geometry("400x300")
win.title("Guess Number")
ans=r.randint(0,100)
#print(ans)
#input guess number
pL1 = tk.Label(win, text="Please enter number:")
pL1.pack()
while (True):
    pnum = tk.StringVar()
    pE1 = tk.Entry(win, textvariable=pnum)
    pE1.pack()
    pB1 = tk.Button(win, text="OK", command=checknum)
    pB1.pack()

pmsg = tk.StringVar()
pL2 = tk.Label(win, textvariable=pmsg)
pL2.pack()

#num=121
#while (num!=ans):
#    num=int(input("please enter guess number:"))
#    if (num==ans):
#        break
#    if (num>ans):
#        print("bigger")
#    else:
#        print("smaller")   
#print("you are win")    

win.mainloop()

