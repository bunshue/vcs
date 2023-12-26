# ch12_36.py
# 定義 Vehicle 類別來表示車輛
class Vehicle:
    # 初始化方法，設置車輛的製造商、型號和生產年份
    def __init__(self, make, model, year):
        self.make = make                    # 車輛的製造商
        self.model = model                  # 車輛的型號
        self.year = year                    # 車輛的生產年份

    # 方法回傳車輛的基本資料
    def get_info(self):
        # 回傳格式化的車輛資料字串
        return f'{self.year} {self.make} {self.model}'

# 使用 Vehicle 類別來建立車輛物件並獲取車輛資料
car = Vehicle('Lexus', 'ES 300h', 2025)     # 建立一個 Vehicle 對象
info = car.get_info()                       # get_info方法獲取車輛資料
print(info)                                 # 輸出：'2025 ES 300h'



