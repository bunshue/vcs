# -*- coding: utf-8 -*-

data = (("張三", 86, 60),("李四", 93, 55),("王五", 72, 66), ("劉六", 89, 84))

print ("編號    姓名      學科    術科    總分")
for idx, dt in enumerate(data):
    print (f"{idx + 1}\t{dt[0]}\t{dt[1]}\t{dt[2]}\t{dt[1] + dt[2]}")
