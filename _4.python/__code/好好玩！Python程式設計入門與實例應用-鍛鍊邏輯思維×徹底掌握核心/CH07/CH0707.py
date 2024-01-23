# 定義函式一
def getFruit(item, name = None):
    
    # 用is運算子判別name是否為None
    if name is None:
        name = [] # 空的List
    #append()方法新增 list 元素
    name.append(item)
    print('水果：', name)

# 定義函式二
def main():
    key = input('y 繼續..，n 結束廻圈..:')
    while key == 'y':
        wd = input('輸入水果名稱：')
        getFruit(wd) #呼叫getFruit()函式
        key = input('y繼續..，n結束廻圈..:')
        
# 呼叫main()函式
main()
