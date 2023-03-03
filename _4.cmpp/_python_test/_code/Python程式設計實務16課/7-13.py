# _*_ coding: utf-8 _*_
# 程式 7-13 (Python 3 version )
import os
class_101 = dict() #記錄學生座號及姓名
chi_score = dict() #記錄國文成績
eng_score = dict() #記錄英文成績
mat_score = dict() #記錄數學成績
subjects = ["國文", "英文", "數學"]
scores  = [chi_score, eng_score, mat_score]

def disp_menu():
    os.system("clear")
    print("Class 101班級成績管理系統")
    print("-------------------------")
    print("1. 輸入學生姓名")
    print("2. 輸入國文成績")
    print("3. 輸入英文成績")
    print("4. 輸入數學成績")
    print("5. 顯示成績單")
    print("0. 結束程式")
    print("-------------------------")

def enter_std_data():
    while True:
        no = int(input("座號（0==>停止輸入）："))
        if no <=0 or no >100: break
        name = input("姓名：")
        class_101[no] = name
        print(class_101)

def enter_score(subject_no):
    for no, name in class_101.items():
        scores[subject_no][no] = \
          int(input("{},{}的{}成績:". \
            format(no, name, subjects[subject_no])))
    print(scores[subject_no])
    x = input("按Enter返回主選單")

def disp_score_table():
    for no in class_101.keys():
        print("{:<5}:".format(class_101[no]), end="")
        sum = 0
        for subject_no in range(0,3):
            sum = sum + scores[subject_no][no]
            print("{}:{:>3} ".format(subjects[subject_no], \
              scores[subject_no][no]), end="")
        print("總分:{:>3}, 平均:{:.2f}".format(sum, \
          float(sum)/len(scores)))
    x = input("按Enter返回主選單")


### 主程式從這裡開始

while True:
    disp_menu()
    user_choice = int(input("請輸入您的選擇："))
    if user_choice==1:
        enter_std_data()
    elif user_choice>=2 and user_choice<=4:
        enter_score(user_choice-2)
    elif user_choice==5:
        disp_score_table()
    else:
        break
print("謝謝您的使用，再見！")
