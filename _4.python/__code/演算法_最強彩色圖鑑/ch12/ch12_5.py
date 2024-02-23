# ch12_5.py
def hanoi(n, src, aux, dst):
    ''' 河內塔 '''
    if n == 1:                                  # 河內塔終止條件
        print('移動圓盤 {} 從 {} 到 {}'.format(n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        print('移動圓盤 {} 從 {} 到 {}'.format(n, src, dst))
        hanoi(n - 1, aux, src, dst)
             
n = eval(input('請輸入圓盤數量 : '))
hanoi(n, 'A', 'B', 'C')







      



    
