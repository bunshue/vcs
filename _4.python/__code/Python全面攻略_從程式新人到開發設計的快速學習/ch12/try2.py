n1 = 8
n2 = 0
try:
    d = n1/n2
    print('%d / %d = %d' %(n1, n2, d))
except Exception as e:
    print('錯誤類型 :', end =' ')
    print(e)
finally:
    print('執行 finally: 敘述\n')
