def computePayment():
    monthlyPayment = getMonthlyPayment(float(loanAmountVar.get()), float(annualInterestRateVar.get()) / 1200, int(numberOfYearsVar.get()))
    monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
    totalPayment = float(monthlyPaymentVar.get()) * 12 * int(numberOfYearsVar.get())
    totalPaymentVar.set(format(totalPayment, '10.2f'))

def getMonthlyPayment(loanAmount, monthlyInterestRate, numberOfYears):
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    return monthlyPayment;


import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)
window.title("Loan Calculator")

tk.Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = tk.W)
tk.Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = tk.W)
tk.Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = tk.W)
tk.Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = tk.W)
tk.Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = tk.W)

annualInterestRateVar = tk.StringVar()
tk.Entry(window, textvariable = annualInterestRateVar, justify = tk.RIGHT).grid(row = 1, column = 2)
numberOfYearsVar = tk.StringVar()
tk.Entry(window, textvariable = numberOfYearsVar, justify = tk.RIGHT).grid(row = 2, column = 2)
loanAmountVar = tk.StringVar()
tk.Entry(window, textvariable = loanAmountVar, justify = tk.RIGHT).grid(row = 3, column = 2)

monthlyPaymentVar = tk.StringVar()
lblMonthlyPayment = tk.Label(window, textvariable = monthlyPaymentVar).grid(row = 4, column = 2, sticky = tk.E)
totalPaymentVar = tk.StringVar()
lblTotalPayment = tk.Label(window, textvariable = totalPaymentVar).grid(row = 5, column = 2, sticky = tk.E)
btComputePayment = tk.Button(window, text = "Compute Payment", command = computePayment).grid(row = 6, column = 2, sticky = tk.E)

window.mainloop()
