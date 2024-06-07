import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個


def computePayment():
    monthlyPayment = getMonthlyPayment(float(loanAmountVar.get()), float(annualInterestRateVar.get()) / 1200, int(numberOfYearsVar.get()))
    monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
    totalPayment = float(monthlyPaymentVar.get()) * 12 * int(numberOfYearsVar.get())
    totalPaymentVar.set(format(totalPayment, '10.2f'))

def getMonthlyPayment(loanAmount, monthlyInterestRate, numberOfYears):
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    return monthlyPayment;

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

print("------------------------------------------------------------")  # 60個

#LoanCalculator

from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        
        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;

LoanCalculator()  # Create GUI 




print("------------------------------------------------------------")  # 60個

def myfun():
    monthrate = interest.get() / (12*100)
    loan = loanmoney.get()
    molecules = loan * monthrate
    denominator = 1-(1/(1+monthrate) ** (years.get() * 12))
    monthpaid = int(molecules / denominator)
    monthpayment.set(monthpaid)
    totalpaid = int(monthpaid * 12 * years.get())
    totalpayment.set(totalpaid)
        
window = tk.Tk()

Interest = tk.Label(window, text="利率")
Years = tk.Label(window, text="貸款年數")
LoanMoney = tk.Label(window, text="貸款金額")
MonthPayment = tk.Label(window, text="每月支付金額")
TotalPayment = tk.Label(window, text="總支付金額")

interest = tk.DoubleVar()
years = tk.IntVar()
loanmoney = tk.IntVar()
monthpayment = tk.IntVar()
totalpayment = tk.IntVar()

interestE = tk.Entry(window, textvariable=interest)
yearsE = tk.Entry(window, textvariable=years)
loanmoneyE = tk.Entry(window, textvariable=loanmoney)
monthpaymentL = tk.Label(window, textvariable=monthpayment, bg='lightyellow')
totalpaymentL = tk.Label(window, textvariable=totalpayment, bg='lightyellow')

Interest.grid(row=0, column=0)
Years.grid(row=1, column=0)
LoanMoney.grid(row=2, column=0)
MonthPayment.grid(row=3, column=0)
TotalPayment.grid(row=4, column=0)

interestE.grid(row=0, column=1, padx=2)
yearsE.grid(row=1, column=1, padx=2)
loanmoneyE.grid(row=2, column=1, padx=2)
monthpaymentL.grid(row=3, column=1, padx=2)
totalpaymentL.grid(row=4, column=1, padx=2)

btnExec = tk.Button(window, text="計算", command=myfun)
btnExec.grid(row=5, column=1, pady=2)

window.mainloop()

print("------------------------------------------------------------")  # 60個

