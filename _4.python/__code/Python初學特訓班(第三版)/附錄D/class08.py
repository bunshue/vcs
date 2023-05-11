class Father():         #定義父類別         
    def say(self):      #定義共用方法 
        print("明天會更好!")
        
class Mother():         #定義父類別  
    def say(self):      #定義共用方法 
        print("包含、尊重!")
        
class Child(Father,Mother): #定義子類別  
    pass
        
child = Child() #建立 child 物件
child.say()     #明天會更好! 