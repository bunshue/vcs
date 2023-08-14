# 定義Student類別
class Student:
    count = 0
    # 建構子
    def __init__(self, name):
        self.name = name
        Student.count += 1
    # 方法
    def getCount(self):
        return Student.count

    def getName(self):
        return self.name

# 使用類別建立物件
s1 = Student("陳會安")
print(s1.getCount(), s1.getName())
s2 = Student("陳允傑")
print(s2.getCount(), s2.getName())
s3 = Student("江小魚")
print(s3.getCount(), s3.getName())
print("學生數: ", Student.count)
