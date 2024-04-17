# Filename: ex02_02.py
chinese = float(input("請輸入國語成績:"))
math = float(input("請輸入數學成績:"))
science = float(input("請輸入自然成績:"))
print("國語成績 %6.2f 數學成績 %6.2f 自然成績 %6.2f 三科總分 %6.2f "%(chinese, math, science, chinese+math+science))