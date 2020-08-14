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
    def __init__(self):
        self.description = 'ハウスブレンドコーヒー'
    
    def cost(self):
        return 0.89


class Mocha(CondimentDecorater):
    def __init__(self, coffee):
        self.coffee = coffee

    def getDesctiption(self):
        return self.coffee.getDesctiption() + '+モカ'
    
    def cost(self):
        return 0.2 + self.coffee.cost()


class Soy(CondimentDecorater):
    def __init__(self, coffee):
        self.coffee = coffee

    def getDesctiption(self):
        return self.coffee.getDesctiption() + '+ソイ'
    
    def cost(self):
        return 0.3 + self.coffee.cost()

#注文パート
class StarbuzzCoffee():
    def main():
        beverage = Beverage()
        if beverage.cost() is None:
            print(beverage.getDesctiption(), '$0')
        else:
            print(beverage.getDesctiption(), "$"+str(beverage.cost()))
    
    def orderEspresso():
        beverage2 = Espresso()
        print(beverage2.getDesctiption(), "$"+str(beverage2.cost()))
    
    def orderHouseBlend():
        beverage3 = HouseBlend()
        beverage3 = Mocha(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Soy(beverage3)
        print(beverage3.getDesctiption(), "$"+str(beverage3.cost()))

#実行パート  
StarbuzzCoffee.main()              #不要な飲み物 $0
StarbuzzCoffee.orderEspresso()     #エスプレッソ $1.99
StarbuzzCoffee.orderHouseBlend()   #ハウスブレンドコーヒー+モカ+モカ+ソイ $1.59
