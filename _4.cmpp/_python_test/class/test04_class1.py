print("Class測試")

class fruit:
	color = 'red'
	def taste(self):
		return 'delicious'

class fruit:
	color = 'red'
	def taste(self):
		return 'delicious'

apple = fruit()
apple.color 
apple.taste() 

class staff:
	def salary():
		return "10000元"

yamamoto = staff()
#money = yamamoto.salary()


class staff:
	def salary(self):
		return "10000元"

yamamoto = staff()
yamamoto.salary()


class staff:
	bonus = 30000
	def salary(self):
		salary = 10000 + bonus
		return salary

yamamoto = staff()
yamamoto.salary()


class staff:
	bonus = 30000
	def salary(self):
		salary = 10000 + self.bonus
		return salary

yamamoto = staff()
yamamoto.salary()


class staff:
	def __init__(self, bonus):
		self.bonus = bonus
	def salary(self):
		salary = 10000 + self.bonus
		return salary

yamamoto = staff(50000)
yamamoto.salary()


