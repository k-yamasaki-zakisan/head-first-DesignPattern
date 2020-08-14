#抽象パート
class PizzaStore():
    
    def OrderPizza(type):
        pizza = createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    def createPizza(type): #abstract
        return
