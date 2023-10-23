class Wage:
	def __init__(self, fee=200, hour=80):
		self.fee=fee
		self.hour=hour

	def getArea(self):
		return self.fee* self.hour

tom=Wage()
print("透過init()方法預設值的總薪資: ",tom.getArea(),"元")

jane= Wage(250,100)
print("透過init()方法傳入參數的總薪資: ",jane.getArea(),"元")
