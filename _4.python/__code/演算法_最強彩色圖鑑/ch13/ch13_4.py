# ch13_4.py
from collections import deque
def banana_dealer(name):
    ''' 回應是不是賣香蕉的經銷商 '''
    if name == 'Banana':
        return True

def search(name):
    ''' 搜尋賣香蕉的朋友 '''
    global not_dealer                       # 儲存已搜尋的名單
    dealer = deque()
    dealer += graph[name]                   # 搜尋串列先儲存Tom的朋友
    while dealer:
        person = dealer.popleft()           # 從左邊取資料
        if banana_dealer(person):           # 如果是True, 表示找到了
            print(person + ' 是香蕉經銷商 ')
            return True                     # search()執行結束
        else:
            not_dealer.append(person)       # 將搜尋過的人儲存至串列
            dealer += graph[person]         # 將不是經銷商的朋友加入搜尋串列
    print('沒有找到經銷商')
    return False
    
not_dealer = []
graph = {}                                  # 建立空字典
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']     # 建立字典graph, key='Tom'的值
graph['Ivan'] = ['Peter']                   # 建立字典graph, key='Ivan'的值
graph['Ira'] = ['Banana']                   # 建立字典graph, key='Ira'的值
graph['Kevin'] = ['Mary']                   # 建立字典graph, key='Mary'的值
graph['Peter'] = []                         # 沒有其他朋友用空集合
graph['Banana'] = []                        # 沒有其他朋友用空集合
graph['Mary'] = []                          # 沒有其他朋友用空集合

search('Tom')
print('列出已搜尋名單 : ', not_dealer)





