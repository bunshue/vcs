#定義整數變數 Score，儲存學生成績
Score=int(input("輸入學生的分數:"))
if Score>=60: #if 條件敘述
     print("得到 %d 分，還不錯唷..." %Score)
else:
     print("不太理想喔...，只考了 %d 分" %Score)
