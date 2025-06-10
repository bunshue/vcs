from areapackage2.Rectangle import Rectangle
        
class Triangle(Rectangle): #定義子類別  
    def area2(self):       #定義子類別的共用方法 
        return (self.width * self.height)/2