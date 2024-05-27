import tkinter as tk

def fnBmi():
    height = userH.get()	#用get方法取得身高
    weight = userW.get()
    bmi = round(weight / pow(height, 2), 2)
    msg=''
    if bmi < 18.5:
        msg='體重過輕！'
    elif bmi >= 24:
        msg='體重過重！'
    else :
        msg='體重剛好！'    
    tk.messagebox.askokcancel('注意','你的BMI指數為：{} {}'.format(bmi, msg))
    
win = tk.Tk()
win.title('BMI計算')
win.geometry('240x200')
win.configure(bg='white')
lblTitle = tk.Label(win, text='BMI 計算',font=('微軟正黑體', 16),fg='white',bg='blue')
lblTitle.pack(pady=10,fill='x')
tk.Label(win, text='身高(公尺，請輸入浮點數)').pack(pady=5,anchor='w')
userH=tk.DoubleVar()		#宣告userH為浮點數物件
entH = tk.Entry(win,textvariable=userH).pack()  #textvariable參數值為userH
tk.Label(win, text='體重(公斤，請輸入整數)').pack(pady=5,anchor='w')
userW=tk.IntVar()		#宣告userW為整數物件
entW = tk.Entry(win,textvariable=userW).pack()  #textvariable參數值為userW
btnCal = tk.Button(win, text=' 計算 ', command=fnBmi).pack(pady=5)
win.mainloop()