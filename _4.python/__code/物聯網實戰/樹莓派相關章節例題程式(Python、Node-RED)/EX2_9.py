# Example 2.9
from property import *
tc = House('apartment', 5600000, 'tclin','taichung')
money = Deposit('money', 100000, 'taiwanBank')
stock = Stock('tpower', 5, 20000)
total = [tc, money, stock]
sum_tc = 0
for i in total:
    sum_tc = sum_tc + i.getValue();
print("Total value of properties : {0}".format(sum_tc))
