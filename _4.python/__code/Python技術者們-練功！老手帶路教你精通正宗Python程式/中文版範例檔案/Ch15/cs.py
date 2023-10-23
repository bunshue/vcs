"""cs 模組: 物件變數視野與命名空間展示模組."""
mv ="模組變數: mv"

def mf():
    return "模組函式: mf()"

class SC:
    scv = "父類別的類別變數: self.scv"
    __pscv = "父類別的私有類別變數: 無法從外部存取"
    def __init__(self):
        self.siv = "父類別定義的物件變數: self.siv " \
                   "(但必須透過 SC.siv 才能賦值)"
        self.__psiv = "父類別定義的私有物件變數: " \
                       "無法從外部存取"
    def sm(self):
        return "父類別的方法: self.sm()"
    def __spm(self):
        return "父類別的私有方法: 無法從外部存取"

class C(SC):
    cv = "類別變數: self.cv (但必須透過 C.cv才能賦值)"
    __pcv = "私有類別變數: self.__pcv " \
            "(但必須透過 C.__pcv才能賦值)"
    def __init__(self):
        SC.__init__(self)
        self.__piv = "私有物件變數: self.__piv"
    def m2(self):
        return "方法: self.m2()"
    def __pm(self):
        return "私有方法: self.__pm()"

    def m(self, p="參數: p"):
        lv = "區域變數: lv"
        self.iv = "物件變數: self.xi"
        print("直接存取區域、全域、和內建命名空間")
        print("區域命名空間:", list(locals().keys()))
        print(p) 
        print(lv)
        print("全域命名空間:", list(globals().keys()))
        print(mv)  
        print(mf())
        print("透過 'self' 存取物件, 類別, 父類別命名空間")
        print("物件命名空間:",dir(self))
        print(self.iv)        
        print(self.__piv)   
        print(self.siv)       
        print("類別命名空間:",dir(C))
        print(self.cv)      
        print(self.m2())    
        print(self.__pcv) 
        print(self.__pm())
        print("父類別命名空間:",dir(SC))
        print(self.sm())
        print(self.scv) 
