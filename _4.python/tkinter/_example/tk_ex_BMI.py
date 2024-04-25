
def checkp():
    p3.set(p2.get()/(p1.get()*p1.get()/10000))

import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("計算BMI程式")
frame1 = tk.Frame(win)
frame1.pack(padx=20, pady=10)
p1 = tk.IntVar()
p2 = tk.IntVar()
p3 = tk.DoubleVar()
pLabel = tk.Label(frame1, text="請輸入身高(公分)")
pLabel.pack()
pEn1 = tk.Entry(frame1, textvariable=p1)
pEn1.pack()
pLabe2 = tk.Label(frame1, text="請輸入體重(公斤)")
pLabe2.pack()
pEn2 = tk.Entry(frame1, textvariable=p2)
pEn2.pack()
pButton = tk.Button(frame1, text="計算BMI", command=checkp)
pButton.pack()
pLmsg = tk.Label(frame1, textvariable=p3)
pLmsg.pack()
win.mainloop()

