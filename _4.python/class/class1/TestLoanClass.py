'''
參考彰化銀行貸款試算
https://www.bankchb.com/frontend/SM1-2.jsp?type=1

'''

print('本息平均攤還')
print('一段式利率')

from Loan import Loan

#貸款利率
annualInterestRate = 2.345  #percent

#貸款年限
numberOfYears = 20  #年

#貸款金額
loanAmount = 34560000 #元

#貸款人
borrower = 'david'

#計算貸款
loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

print('貸款金額', loanAmount/10000, '萬元')
print('貸款利率', annualInterestRate, '%')
print('貸款年限', numberOfYears, '年')

print('貸款人', loan.getBorrower())
print('每月應付本息金額', format(loan.getMonthlyPayment(), '.2f'), '元')
print('20年總應付本息金額', format(loan.getTotalPayment(), '.2f'), '元')


'''
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
'''

