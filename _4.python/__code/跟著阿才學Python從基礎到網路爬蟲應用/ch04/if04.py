score = int(input("請輸入成績："))  #輸入成績再轉成整數並指定給score
if score >=0 and score <= 100:  	#判斷score是否介於0~100之間
   if score >= 60 :	
       show = "Pass"  		#score大於等於60 指定show為 "Pass"
   else :
       show = "不及格"  		#score小於60 指定show為 "不及格" 
else:
    show = "應介於0~100之間"   #score沒有介於0~100之間 ， show指定為 "應介於0~100之間
print("成績", show)
