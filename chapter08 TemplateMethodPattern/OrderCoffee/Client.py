from Coffee  import Coffee, CoffeeWithHook, Tea, TeaWithHook

#実行パート
class BeverageTestDrive():
    def orderCoffee():
        coffee = Coffee()

        print("コーヒを作っています")

        coffee.prepareRecipe()
    
    def orderTea():
        tea = Tea()

        print("コーヒを作っています")

        tea.prepareRecipe()
    
    def orderCoffeeWithHook():
        coffeeWithHook = CoffeeWithHook()

        print("コーヒを作っています")

        coffeeWithHook.prepareRecipe()
    
    def orderTeaWithHook():
        teaWithHook = TeaWithHook()

        print("紅茶を作っています")

        teaWithHook.prepareRecipe()


#実行
#BeverageTestDrive.orderCoffee()
#BeverageTestDrive.orderTea()
#BeverageTestDrive.orderCoffeeWithHook()
BeverageTestDrive.orderTeaWithHook()