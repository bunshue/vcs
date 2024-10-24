import sys

print("------------------------------------------------------------")  # 60個
"""
# 貸款試算
loan = 10000  # 貸款金額
year = 1  # 年限
rate = 10  # 年利率%
month_rate = rate / (12 * 100)  # 改成百分比以及月利率

# 計算每月還款金額
molecules = loan * month_rate
denominator = 1 - (1 / (1 + month_rate) ** (year * 12))
monthly_pay = molecules / denominator  # 每月還款金額
total_pay = monthly_pay * year * 12  # 總共還款金額

print("每月還款金額 %d" % int(monthly_pay))
print("總共還款金額 %d" % int(total_pay))

"""


print("------------------------------------------------------------")  # 60個


"""
彰化銀行-貸款試算
https://www.bankchb.com/frontend/SM1-2.jsp?type=2
本息平均攤還
"""

"""
loan = eval(input("請輸入貸款金額："))
year = eval(input("請輸入年限："))
rate = eval(input("請輸入年利率："))
"""
loan = 10000000
year = 20
rate = 0.0185

monthrate = rate / (12 * 100)  # 改成百分比的月利率

# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator  # 每月還款金額
totalPay = monthlyPay * year * 12  # 總共還款金額

print(f"每月還款金額 {int(monthlyPay)}")
print(f"總共還款金額 {int(totalPay)}")

print("------------------------------------------------------------")  # 60個

# Compute Loan

# Enter yearly interest rate
annualInterestRate = eval(input("Enter annual interest rate, e.g., 8.25: "))
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = eval(input("Enter number of years as an integer, e.g., 5: "))

# Enter loan amount
loanAmount = eval(input("Enter loan amount, e.g., 120000.95: "))

# Calculate payment
monthlyPayment = (
    loanAmount
    * monthlyInterestRate
    / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
)
totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) / 100)


print("------------------------------------------------------------")  # 60個


class Loan:
    def __init__(
        self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower=" "
    ):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = (
            self.__loanAmount
            * monthlyInterestRate
            / (1 - (1 / (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        )
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment


# Enter yearly interest rate
# annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))
print("年利率 3%")
annualInterestRate = 3

# Enter number of years
# numberOfYears = eval(input("Enter number of years as an integer: "))
print("貸 20 年")
numberOfYears = 20

# Enter loan amount
# loanAmount = eval(input("Enter loan amount, for example, 120000.95: "))
print("貸款金額 1000 萬")
loanAmount = 10000000

# Enter a borrwer
print("貸款者")
borrower = "Michael"

# Create a Loan object
loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

# Display loan date, monthly payment, and total payment
print("The loan is for", loan.getBorrower())
print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
print("The total payment is", format(loan.getTotalPayment(), ".2f"))

print("------------------------------")  # 60個

"""
參考彰化銀行貸款試算
https://www.bankchb.com/frontend/SM1-2.jsp?type=1

"""

print("本息平均攤還")
print("一段式利率")

# 貸款利率
annualInterestRate = 2.345  # percent

# 貸款年限
numberOfYears = 20  # 年

# 貸款金額
loanAmount = 34560000  # 元

# 貸款人
borrower = "david"

# 計算貸款
loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

print("貸款金額", loanAmount / 10000, "萬元")
print("貸款利率", annualInterestRate, "%")
print("貸款年限", numberOfYears, "年")

print("貸款人", loan.getBorrower())
print("每月應付本息金額", format(loan.getMonthlyPayment(), ".2f"), "元")
print("20年總應付本息金額", format(loan.getTotalPayment(), ".2f"), "元")


"""
直接計算
#貸款利率
annualInterestRate = 2.345  #percent

monthlyInterestRate = annualInterestRate / 1200

#貸款年限
numberOfYears = 20  #年

#貸款金額
loanAmount = 34560000 #元
    
# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / (1
  - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# Display results
print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) /100)
"""


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
