from abc import ABCMeta, abstractmethod
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
class ChicagoSylePizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == "チーズ":
            return ChicagoStyleCheesePizza()
        elif item == "野菜":
            return ChicagoStyleVeggiePizza()
        elif item == "クラム":
            return ChicagoStyleClamPizza()
        elif item == "ペパニロ":
            return ChicagoStylePepperoniPizza()
        else:
            return None

class NYSylePizzaStore(PizzaStore):
    def createPizza(self, item):
        if item == "チーズ":
            return NYStyleCheesePizza()
        elif item == "野菜":
            return NYStyleStyleVeggiePizza()
        elif item == "クラム":
            return NYStyleStyleClamPizza()
        elif item == "ペパニロ":
            return NYStyleStylePepperoniPizza()
        else:
            return None
    
#ピザパート
##抽象パート
class Pizza(metaclass=ABCMeta):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        print(self.name+"を下処理"+self.name)
        print("生地をこねる")
        print("ソースを追加")
        print("トッピングを追加")
        for i in range(len(self.toppings)):
            print(" "+ self.toppings[i])
    
    def bake(self):
        print("350度で25分間焼く")
    
    def cut(self):
        print("ピザを扇型に切り分ける")

    def box(self):
        print("PizzaStoreの正式な箱にピザをいれる")
    
    def getName(self):
        return self.name

##具現化パート
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "ニューヨークスタイルのソース＆チーズピザ"
        self.dough = "薄いクラスト生地"
        self.sauce = "マリナラソース"
        self.toppings = ["粉レッジャーノチーズ"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "シカゴスタイルのソース＆チーズピザ"
        self.dough = "極厚クラスト生地"
        self.sauce = "プラムトマトソース"
        self.toppings = ["刻んだモレラチーズ"]
    
    def cut(self):
        print("刻んだモレラチーズ")
    
##注文パート
class PizzaTestDrive():
    def main():
        nyStore = NYSylePizzaStore()
        chicagoStore = ChicagoSylePizzaStore()

        pizza = nyStore.OrderPizza("チーズ")
        print("イーサンの注文は"+pizza.getName())

        pizza = chicagoStore.OrderPizza("チーズ")
        print("ジョエルは"+pizza.getName())


##実行パート
PizzaTestDrive.main()
