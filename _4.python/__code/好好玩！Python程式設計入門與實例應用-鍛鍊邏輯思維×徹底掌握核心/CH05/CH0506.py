# if/elif敘述，依據輸入月分顯示天數

month = int(input('請輸入1~12月分-> '))

# 第一層 if/else敘述判斷輸入數值是否在1~12之間，邏輯運算子and須前後條件皆符合才會回傳True
if month >=1 and month <= 12:
    
    #第二層if/elif 多重條件
    if month == 4 or month == 6 or month == 9 \
           or month == 11:
        print(month, '月有30天！')
    elif month == 2:
        print(month, '月有28或29天！')
    else:
        print(month, '月有31天！')

else:
    print('月分在1~12之間...')
