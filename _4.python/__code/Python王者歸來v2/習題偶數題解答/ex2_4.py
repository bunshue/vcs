# ex2_4.py
apple = 100
student = 23
day = apple // student
print("蘋果可以吃的天數")
print(day)
print("第幾天產生蘋果不足供應")
print(day+1)
left = apple % student
not_enough = student - left
print("不足數量")
print(not_enough)



