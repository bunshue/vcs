"""circle 模組: 包含 Circle 類別."""
class Circle:
    """Circle 類別"""
    all_circles = []
    pi = 3.14159

    def __init__(self, r=1):
        """以給定的半徑建立圓物件"""
        self.radius = r
        self.__class__.all_circles.append(self)

    def area(self):
        """計算此物件的面積"""
        return self.__class__.pi * self.radius * self.radius
    
    @staticmethod
    def total_area():
       """用來計算 all_circles 這個 list 所有物件總面積的靜態方法"""
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
