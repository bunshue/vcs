# ch10_14.py
countries = {'Japan', 'China', 'France'}
print("刪除前的countries集合 ", countries)
country = input("請輸入國家 : ")
if country in countries:    
    countries.remove('Japan')
    print("刪除後的countries集合 ", countries)
else:
    print(f"{country} 不存在")

