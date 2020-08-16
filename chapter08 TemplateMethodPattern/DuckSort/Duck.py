class Duck():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def toString(self):
        return self.name + "の重さは" + str(self.weight)
    
    def compareTo(self, objOtherDuck):
        self.otherDuck = objOtherDuck

        if self.weight < self.otherDuck.weight:
            return -1
        else: #self.weight > self.otherDuck.weight or self.weight == self.otherDuck.weigh
            return 1
