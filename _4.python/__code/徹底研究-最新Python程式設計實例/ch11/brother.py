class Tom():#父類別
    def __init__(self):
        self.height1=178

class Andy(Tom):#父類別是Tom
    def __init__(self):
        self.height2=180
        super().__init__()

class Michael(Tom):#父類別是Tom
    def __init__(self):
        self.height3=185
        super().__init__()
    def display(self):
        print('父親Tom的身高:', self.height1,'公分')
        print('兄弟Andy的身高:', Andy().height2,'公分')
        print('自己Michael的身高:', m1.height3,'公分')

m1=Michael()
m1.display()
