# F1750 練習 39

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []
    
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)
    
    def flavors(self):
        return '/'.join(scoop.flavor
                        for scoop in self.scoops)

bowl = Bowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))

print(bowl.flavors())
