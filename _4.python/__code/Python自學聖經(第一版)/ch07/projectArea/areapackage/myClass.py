class Rectangle():       #定義父類別  
    def __init__(self, width,height):
        self.width = width    #定義共用屬性   
        self.height = height  #定義共用屬性
    def area(self):           #定義共用方法 
        return self.width * self.height
        
class Triangle(Rectangle): #定義子類別  
    def area2(self):       #定義子類別的共用方法 
        return (self.width * self.height)/2