#內建函式format()
salary = int(input('請輸入薪資-> '))
# 依據薪資扣除稅額
if salary >= 28000:
    tax = salary * 0.06
elif salary >= 32000:
    tax = salary * 0.08
else: # < 28000不扣稅
    tax = 0
income = salary - tax #實領薪資
print('薪資：' , format(salary, ' >12d'))
print('扣除額 = ', format(tax, '>12,.2f'))
print('實領薪資：NT$', format(income, '>6,.2f'))
