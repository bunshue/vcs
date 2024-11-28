# Homework 2-9
import property as P
tc = P.House('apartment', 5600000, 'tclin','taichung')
money = P.Deposit('money', 100000, 'taiwanBank')
stock = P.Stock('tpowerStock', 5, 20000)
total = [tc, money, stock]
sum = 0
for i in total:
    sum = sum + i.getValue();
print("Total value of properties : {0}".format(sum))
