# 5-3-8 SimpleNamespace - 把 dict 鍵變成屬性名稱

from types import SimpleNamespace

car = SimpleNamespace(color='紅', mileage=3812.4, automatic=True)

print(car)
print(car.mileage)

car.windshield = 'broken'
del car.automatic

print(car)