# ch9_21_4.py
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item:item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")



