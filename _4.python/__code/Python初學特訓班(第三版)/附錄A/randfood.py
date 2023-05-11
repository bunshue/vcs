def getrandom2(n1, n2):  #取得2個不重複的亂數
    while True:
        r1 = random.randint(n1, n2)
        r2 = random.randint(n1, n2)
        if r1 != r2:  #如果兩數不相等就跳出迴圈
            break
    return r1, r2

import os, random
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0  #不顯示警告
doc = word.Documents.Add()
range1 = doc.Range(0,0)  #檔案開頭
range1.Style.Font.Size = "16"  #字體尺寸
title = "明星國小營養午餐菜單"
year1 = "2016年9月"
week = ["一","二","三","四","五"]
teacher = ["歐陽怡","翟定國","陳碧山","陳麗娟","鄭怡衡","林鄧超","朱健政","劉偉明","劉維琪","梁銀燕"]
rice = ["糙米飯","白米飯","拌麵"]
vegetable = ["毛豆白菜","豆芽菜","蛋香時瓜","高麗菜","佛手瓜","酸菜豆包","冬瓜","蘿蔔海結","茄汁洋芋","家常豆腐","鮮菇花椰","豆皮三絲","伍彩雪蓮","干香根絲","茄汁豆腐","香炒花椰","芹香粉絲","紅蘿蔔","洋蔥","青椒"]
meat = ["糖醋排骨","美味大雞腿","椒鹽魚條","香菇肉燥","宮保雞丁","香滷腿排","梅干絞肉","香酥魚丁","條瓜燒雞","時瓜肉絲","海結滷肉","蔥燒雞","柳葉魚","咖哩絞肉","筍香雞","沙茶豬柳","五香棒腿","三杯雞丁","海結豬柳","茄汁雞丁"]
soup = ["蛋香木須湯","味噌海芽湯","綠豆湯","榨菜肉絲湯","薑絲海芽湯","枸杞愛玉湯","冬菜蛋花湯","冬瓜西米露","紫菜蛋花湯","蛋香木須湯"]
date1= 1  #開始日期為1日
weekday = 4  #開始日期為星期四

while weekday < 6 and date1 < 31:  #週一到週五及30日前才製作菜單
    range1.InsertAfter(title + "\n")
    range1.InsertAfter("日期：" + year1 + str(date1) + "日 (星期" + week[weekday-1] + ")\n")
    range1.InsertAfter("製作者：" + teacher[random.randint(0,9)] + "老師\n")
    range1.InsertAfter("今日菜單：\n")
    range1.InsertAfter("一、" + rice[random.randint(0,2)] + "\n")
    rand1, rand2 = getrandom2(0,19)  #取得兩個亂數
    range1.InsertAfter("二、" + vegetable[rand1] + "\n")
    range1.InsertAfter("三、" + vegetable[rand2] + "\n")
    rand1, rand2 = getrandom2(0,19)
    range1.InsertAfter("四、" + meat[rand1] + "\n")
    range1.InsertAfter("五、" + meat[rand2] + "\n")
    range1.InsertAfter("六、" + soup[random.randint(0,9)] + "\n")
    range1.Collapse(constants.wdCollapseEnd)  #移到range尾
    range1.InsertBreak(constants.wdSectionBreakNextPage)  #換頁
    weekday += 1  #星期加1
    date1 += 1  #日期加1
    if weekday == 6:  #如果是星期六
        weekday = 1  #設為星期一
        date1 += 2  #日期加2(星期六及星期日)
    
cpath=os.path.dirname(__file__)
doc.SaveAs(cpath + "\\media\\food.docx")  #存為<food.docx>
#doc.Close()
#word.Quit()