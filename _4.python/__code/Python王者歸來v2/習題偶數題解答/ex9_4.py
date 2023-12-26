# ex9_4.py
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
for noodle, price in sorted(noodles.items(), key=lambda item:item[1]):
    print(noodle,":",price)

