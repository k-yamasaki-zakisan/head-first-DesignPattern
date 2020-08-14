#システムパート
class Beverage():
    def __init__(self):
        self.description = '不要な飲み物'
    
    def getDesctiption(self):
        return self.description
    
    def cost(self):
        return

class CondimentDecorater(Beverage): #abstract
    def getDesctiption():
        return

class Espresso(Beverage):
    def __init__(self):
        self.description = 'エスプレッソ'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def HouseBlend(self):
        self.description = 'ハウスブレンドコーヒー'
    
    def cost():
        return 0.89


class Mocha(CondimentDecorater):
    def Mocha(self):
        self.Beverage = Beverage()

    def getDesctiption():
        return self.Beverage.getDesctiption() + '、モカ'
    
    def cost():
        return 0.2 + self.Beverage.cost()


#注文パート
class StarbuzzCoffee():
    def main():
        beverage = Beverage()
        print(beverage.getDesctiption(), beverage.cost())
    
    def orderEspresso():
        beverage2 = Espresso()
        print(beverage2.getDesctiption(), beverage2.cost())


#実行パート  
#StarbuzzCoffee.main()
StarbuzzCoffee.orderEspresso()