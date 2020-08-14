from abc import ABCMeta, abstractmethod, ABC

#ピザストアパート
##抽象パート
class PizzaStore(metaclass=ABCMeta):
    def OrderPizza(self,type):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    @abstractmethod
    def createPizza(self,type): #abstract
        pass

##具現化パート
class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.pizza = None
        self.ingredientFactory = NYPizzaIngredientFactory()

    def createPizza(self,item):
        if item == "チーズ":
            self.pizza = CheesePizza(self.ingredientFactory)
            self.pizza.setName("ニューヨークスタイルチーズピザ")
        elif itme == "野菜":
            self.pizza = VeggiePizza(self.ingredientFactory)
            self.pizza.setName("ニューヨークスタイル野菜ピザ")
        elif itme == "クラム":
            self.pizza = ClamPizza(self.ingredientFactory)
            self.pizza.setName("ニューヨークスタイルクラムピザ")
        elif item == "ペパロニ":
            self.pizza = PepperoniPizza(self.ingredientFactory)
            self.pizza.setName("ニューヨークスタイルペパロニピザ")
        
        return self.pizza
    

#ピザパート
##抽象パート
class Pizza(metaclass=ABCMeta):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        print("350度で25分間焼く")
    
    def cut(self):
        print("ピザを扇型に切り分ける")

    def box(self):
        print("PizzaStoreの正式な箱にピザをいれる")
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    @abstractmethod
    def toString(self):
        pass

##具現化パート
class CheesePizza(Pizza):
    def __init__(self, PizzaIngredientFactory):
        self.ingredientFactory = PizzaIngredientFactory
    
    def prepare(self):
        print(self.name+"を下処理")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()

class ClamPizza(Pizza, PizzaIngredientFactory):
    def __init__(self):
        self.ingredientFactory = PizzaIngredientFactory
    
    def prepare(self):
        print(self.name+"を下処理")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()


#食材パート
##抽象パート
class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def createDough():
        pass

    @abstractmethod
    def createSauce():
        pass

    @abstractmethod
    def createCheese():
        pass

    @abstractmethod
    def createVeggies():
        pass

    @abstractmethod
    def createPepperoni():
        pass

    @abstractmethod
    def createClam():
        pass

##具現化パート
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough():
        return ThinCrustDough()

    def createSauce():
        return MarinaraSauce()
    
    def createCheese():
        return ReggianoCheese()

    def createVeggies():
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def createPepperoni():
        return SlicedPerpperoni()
    
    def createClam():
        return FreshClams()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough():
        return ThinCrustDough()

    def createSauce():
        return PlumTomatoSauce()
    
    def createCheese():
        return MozzarellaCheese()

    def createVeggies():
        veggies = [BlackOlives(), Spinach(), EggPlant()]
        return veggies
    
    def createPepperoni():
        return SlicedPerpperoni()
    
    def createClam():
        return FrozenClams()


#食材パート
##抽象パート
class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def createDough():
        pass

    @abstractmethod
    def createSauce():
        pass

    @abstractmethod
    def createCheese():
        pass

    @abstractmethod
    def createVeggies():
        pass

    @abstractmethod
    def createPepperoni():
        pass

    @abstractmethod
    def createClam():
        pass

##具現化パート
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()
    
    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPerpperoni()
    
    def createClam(self):
        return FreshClams()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return PlumTomatoSauce()
    
    def createCheese(self):
        return MozzarellaCheese()

    def createVeggies(self):
        veggies = [BlackOlives(), Spinach(), EggPlant()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPerpperoni()
    
    def createClam(self):
        return FrozenClams()


class ThinCrustDough():
    pass

class MarinaraSauce():
    pass

class ReggianoCheese():
    pass


#注文パート2(食材入り)
class PizzaTestDrive2():
    def main():
        nyPizzaStore = NYPizzaStore()
        nyPizzaStore.OrderPizza("チーズ")
        print("美味しいピザを食べました")


#実行パート2(食材入り)
PizzaTestDrive2.main()
