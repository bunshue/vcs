# F1750 練習 41

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:
    max_scoops = 3
    
    def __init__(self):
        self.scoops = []
    
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)
    
    def __repr__(self):
        return f'Bowl(scoops={self.scoops}'

class ExtraBowl(Bowl):
    max_scoops = 5
    

bowl = ExtraBowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))
bowl.add_scoop(Scoop('焦糖'), Scoop('抹茶'))

print(bowl)
