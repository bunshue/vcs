# -*- coding: utf-8 -*-
i = float(input("請輸入PH值："))
if (i < -1 or i > 15):
    print("輸入值異常！！")
else:
    if(i == 7):
        print("中性！！")
    elif (i < 7):
        print("酸性！！")
    else:
        print("鹼性！！")
