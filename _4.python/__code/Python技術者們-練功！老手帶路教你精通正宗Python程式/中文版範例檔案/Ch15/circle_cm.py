"""circle_cm 模組: 包含 Circle 類別."""
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

    @classmethod
    def total_area(cls):  
        """用來計算所有物件總面積的類別方法"""
        total = 0
        for c in cls.all_circles:  
                    #3
            total = total + c.area()
        return total
