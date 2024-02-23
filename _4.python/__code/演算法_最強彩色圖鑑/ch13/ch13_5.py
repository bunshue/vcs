# ch13_5.py
def banana_dealer(name):
    ''' 回應是不是賣香蕉的經銷商 '''
    if name == 'Banana':
        return True

def search(name):
    ''' 搜尋賣香蕉的朋友 '''
    global not_dealer                       # 儲存已搜尋的名單
    dealer = []
    dealer += graph[name]                   # 搜尋串列先儲存Tom的朋友
    while dealer:
        person = dealer.pop(0)              # 從左邊取資料
        if banana_dealer(person):           # 如果是True, 表示找到了
            print(person + ' 是香蕉經銷商 ')
            return True                     # search()執行結束
        else:
            not_dealer.append(person)       # 將搜尋過的人儲存至串列
            dealer += graph[person]         # 將不是經銷商的朋友加入搜尋串列
    print('沒有找到經銷商')
    return False
    
not_dealer = []
graph = {'Tom':['Ivan', 'Ira', 'Kevin'],
         'Ivan':['Peter'],
         'Ira':['Banana'],
         'Kevin':['Mary'],
         'Peter':[],
         'Banana':[],
         'Mary':[]
        }

search('Tom')
print('列出已搜尋名單 : ', not_dealer)





