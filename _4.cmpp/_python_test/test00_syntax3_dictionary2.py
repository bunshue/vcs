print('dict使用範例')

class_101 = dict() #記錄學生座號及姓名
chi_score = dict() #記錄國文成績
eng_score = dict() #記錄英文成績
mat_score = dict() #記錄數學成績

subjects = ["國文", "英文", "數學"]
scores  = [chi_score, eng_score, mat_score]

class_101[1] = 'apple'
class_101[2] = 'banana'
class_101[4] = 'cat'
class_101[8] = 'dog'
print(class_101)

subject_no = 0
for no, name in class_101.items():
    scores[subject_no][no] = int(input("{},{}的{}成績:".format(no, name, subjects[subject_no])))
    print(scores[subject_no])

subject_no = 1
for no, name in class_101.items():
    scores[subject_no][no] = int(input("{},{}的{}成績:".format(no, name, subjects[subject_no])))
    print(scores[subject_no])

subject_no = 2
for no, name in class_101.items():
    scores[subject_no][no] = int(input("{},{}的{}成績:".format(no, name, subjects[subject_no])))
    print(scores[subject_no])

for no in class_101.keys():
    print("{:<5}:".format(class_101[no]), end="")
    sum = 0
    for subject_no in range(0,3):
        sum = sum + scores[subject_no][no]
        print("{}:{:>3} ".format(subjects[subject_no], scores[subject_no][no]), end="")
    print("總分:{:>3}, 平均:{:.2f}".format(sum, float(sum)/len(scores)))

