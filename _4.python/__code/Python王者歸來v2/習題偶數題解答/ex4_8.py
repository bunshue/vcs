# ex4_8.py
rates = input("請輸入年利率%為單位：")
years = input("請輸入年數         ：") 
money = 50000 * ( 1 + float(rates) / 100) ** int(years)
print(f"{years} 年後本金和是 {int(money)}")



