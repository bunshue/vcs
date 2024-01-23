# 定義函式
def person(name, salary, s2, s3):
    print(name)
    # format()函式分設欄寬為10, 6 並加千位符號
    print(f'扣除額：{(s2 + s3):11,}')
    salary =  salary - s2 - s3    
    print(f'實領金額 NT$ {salary:6,}')
        
income = [28800, 605, 405]
#呼叫函式 -- number串列物件，可迭代
person('Tomas', *income)
