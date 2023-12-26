# ch12_34.py
class Geometric():
    def __init__(self):
        self.color = "Green"
class Circle(Geometric):
    def __init__(self,radius):
        super().__init__()
        self.PI = 3.14159
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)
    def getColor(self):
        return color

A = Circle(5)
print("圓形的顏色 : ", A.color)
print("圓形的半徑 : ", A.getRadius())
print("圓形的直徑 : ", A.getDiameter())
print("圓形的圓周 : ", A.getPerimeter())
print("圓形的面積 : ", A.getArea())
A.setRadius(10)
print("圓形的直徑 : ", A.getDiameter())





                       

    












        
        
