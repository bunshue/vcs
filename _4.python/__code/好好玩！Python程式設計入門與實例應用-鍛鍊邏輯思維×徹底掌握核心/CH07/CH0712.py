# 定義函式
def funcData(n1, n2, n3, n4, n5):
    print('基本資料:\n',n1, n2, n3, n4, n5)
    
#呼叫函式，使用*運算子拆解「可迭代物件
data = [1988, 3, 18]
funcData('Mary', 'Birth', *data)
