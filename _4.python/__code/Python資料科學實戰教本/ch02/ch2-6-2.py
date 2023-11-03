# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    # 方法
    def displayStudent(self):
        print("姓名 = " + self.name)
        print("成績 = " + str(self.__getGrade()))
        
    def __getGrade(self):
        return self.__grade

# 使用類別建立物件
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法
# print("s1.__getGrade() = " + str(s1.__getGrade()))
# 存取資料欄位
print("s1.name = " + s1.name)
# print(s1.__grade)