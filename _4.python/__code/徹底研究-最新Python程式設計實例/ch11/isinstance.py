class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
tiger = Animal()
daniel= Human()
goldfish=Fish()
alice = Mermaid()
print("tiger是屬於Animal類別:",isinstance(tiger,Animal))
print("daniel是屬於Animal類別:",isinstance(daniel,Animal))
print("goldfish是屬於Animal類別:",isinstance(goldfish,Animal))
print("alice是屬於Animal類別:",isinstance(alice,Animal))
print("===============================================")
print("tiger是屬於Human類別:",isinstance(tiger,Human))
print("daniel是屬於Human類別:",isinstance(daniel,Human))
print("goldfish是屬於Human類別:",isinstance(goldfish,Human))
print("alice是屬於Human類別:",isinstance(alice,Human))
print("===============================================")
print("tiger是屬於Fish類別:",isinstance(tiger,Fish))
print("daniel是屬於Fish類別:",isinstance(daniel,Fish))
print("goldfish是屬於Fish類別:",isinstance(goldfish,Fish))
print("alice是屬於Fish類別:",isinstance(alice,Fish))
print("===============================================")
print("tiger是屬於Mermaid類別:",isinstance(tiger,Mermaid))
print("daniel是屬於Mermaid類別:",isinstance(daniel,Mermaid))
print("goldfish是屬於Mermaid類別:",isinstance(goldfish,Mermaid))
print("alice是屬於Mermaid類別:",isinstance(alice,Mermaid))
