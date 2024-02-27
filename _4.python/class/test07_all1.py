print("------------------------------------------------------------")  # 60個


# 宣告類別
class Motor:
    def __init__(self):
        # 屬性
        self.name = "CCCCCC"
        self.color = "XXXXXX"

    # 打印物件訊息
    def __repr__(self):
        return f"Motor({self.name, self.color})"

    # 定義方法一：取得名稱和顏色
    def setupCar(self, name, color):
        self.name = name
        self.color = color

    # 定義方法二：輸出名稱和顏色
    def showMessage(self):
        print(f"款式:{self.name:6s},", f"顏色:{self.color:4s}")


# 產生物件
car1 = Motor()  # 物件1
car1.showMessage()  # 呼叫方法
car1.setupCar("Vios", "極光藍")
car1.showMessage()  # 呼叫方法

car2 = Motor()  # 物件2
car2.showMessage()
car2.setupCar("Altiss", "炫魅紅")
car2.showMessage()

print("打印物件訊息, 使用__repr__")
print(car1)
print(car2)

print("------------------------------------------------------------")  # 60個


# 建立類別，產生物件能以不同再別做存取
class Student:
    def message(self, name):  # 方法一
        self.data = name

    def showMessage(self):  # 方法二
        print(self.data)


s1 = Student()  # 第一個物件
s1.message("James McAvoy")  # 呼叫方法時傳入字串
s1.showMessage()
s2 = Student()  # 第二個物件
s2.message(78.566)  # 呼叫方法時傳入浮點數值
s2.showMessage()

print("------------------------------------------------------------")  # 60個


# 宣告類別
class student:
    def score(self, s1, s2, s3):
        return (s1 + s2 + s3) / 3


# 產生物件
vicky = student()
# 呼叫score()方法並傳入引數
average = vicky.score(98, 65, 81)
print(f"Vicky 平均分數：{average:.3f}")


print("------------------------------------------------------------")  # 60個


# 宣告類別
class newClass:
    # __new__()建構物件
    def __new__(Kind, name):
        if name != "":
            print("物件已建構")
            return object.__new__(Kind)
        else:
            print("物件未建構")
            return None

    # __init__()初始化物件
    def __init__(self, name):
        print("物件初始化...")
        print(name)


# 產生物件
x = newClass("")
print()
y = newClass("Second")


print("------------------------------------------------------------")  # 60個


# 產生父類別 或稱 基礎類別
class Father:
    def walking(self):
        print("多走路有益健康!")


# 產生子類別 或稱 衍生類別
class Son(Father):
    pass


# 產生子類別實體 - 即物件
Joe = Son()
Joe.walking()


print("------------------------------------------------------------")  # 60個


# 類和繼承
class Plant():
    def __init__(self, name):
        self.name = name
    def show(self):
        print("plant", self.name)

p = Plant('banana')
p.show()

#plant banana

class Fruit(Plant):
    def show(self):
        print("fruit", self.name)
f = Fruit('banana')
f.show()

#fruit banana


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
