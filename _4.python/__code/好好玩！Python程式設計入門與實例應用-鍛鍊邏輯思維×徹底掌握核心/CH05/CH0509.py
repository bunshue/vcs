# 使用 %運算子格式化字串
blackTea = 45
name = input('請輸入你的名字：')
qty = int(input('輸入購買杯數：'))

print('Hi! %10s' % name)
if qty >= 10:
    total = qty * blackTea * 0.9
    print('飲料 NT$ %4.2f' % total)
else:
    total = qty * blackTea
    print("飲料 NT$ %4d" % total)
