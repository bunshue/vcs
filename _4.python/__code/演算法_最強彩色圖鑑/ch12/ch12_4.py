# ch12_4.py
def hanoi(n, src, aux, dst):
    global step
    ''' 河內塔 '''
    if n == 1:                                  # 河內塔終止條件
        step += 1                               # 紀錄步驟
        print('{0:2d} : 移動圓盤 {1} 從 {2} 到 {3}'.format(step, n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        step += 1                               # 紀錄步驟
        print('{0:2d} : 移動圓盤 {1} 從 {2} 到 {3}'.format(step, n, src, dst))
        hanoi(n - 1, aux, src, dst)

step = 0              
n = eval(input('請輸入圓盤數量 : '))
hanoi(n, 'A', 'B', 'C')







      



    
