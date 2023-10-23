class Wage:
	def __init__(self, h=80):
		self.__hour=h

	def getHour(self):
		return self.__hour

	def pay(self):
		return hour_fee*self.__hour
hour_fee=200
obj1=Wage(100)
print("每小時基本工資為:",hour_fee,"元")
print("總共工作的小時數:", obj1.__hour)
print("要付給這位工讀生的薪水總額:", obj1.pay(),"元")
