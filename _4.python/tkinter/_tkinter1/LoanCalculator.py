import tkinter as tk
    
class LoanCalculator:
    def __init__(self):
        window = tk.Tk()
        window.title("Loan Calculator")
        
        tk.Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = tk.W)
        tk.Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = tk.W)
        tk.Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = tk.W)
        tk.Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = tk.W)
        tk.Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = tk.W)
        
        self.annualInterestRateVar = tk.StringVar()
        tk.Entry(window, textvariable = self.annualInterestRateVar, justify = tk.RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = tk.StringVar()
        tk.Entry(window, textvariable = self.numberOfYearsVar, justify = tk.RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = tk.StringVar()
        tk.Entry(window, textvariable = self.loanAmountVar, justify = tk.RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = tk.StringVar()
        lblMonthlyPayment = tk.Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = tk.E)
        self.totalPaymentVar = tk.StringVar()
        lblTotalPayment = tk.Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = tk.E)
        btComputePayment = tk.Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = tk.E)
        
        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()), float(self.annualInterestRateVar.get()) / 1200, int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;

LoanCalculator()
