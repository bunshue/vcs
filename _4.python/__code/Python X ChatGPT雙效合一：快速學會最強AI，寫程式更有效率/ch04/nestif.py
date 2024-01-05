Score=int(input("輸入學生的分數:")) #輸入學生成績
if Score > 100:     #判斷是否超過 
    print("輸入的分數超過 100.")
else:
    if Score<0: #判斷是否低於0
        print("怎麼會有負的分數??")
    else:
        if Score >= 60: #判斷是否及格
            print("得到 {}分，還不錯唷...".format(Score))
        else:
            print("不太理想喔...，只考了 {} 分".format(Score))
