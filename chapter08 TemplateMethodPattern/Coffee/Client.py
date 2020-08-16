from Coffee  import Coffee, CoffeeWithHook, Tea, TeaWithHook

#実行パート
class BeverageTestDrive():
    def main():
        coffee = Coffee()

        print("コーヒを作っています")

        coffee.prepareRecipe()
    
    def main2():
        tea = Tea()

        print("コーヒを作っています")

        tea.prepareRecipe()
    
    def main3():
        coffeeWithHook = CoffeeWithHook()

        print("コーヒを作っています")

        coffeeWithHook.prepareRecipe()
    
    def main4():
        teaWithHook = TeaWithHook()

        print("紅茶を作っています")

        teaWithHook.prepareRecipe()


#実行
#BeverageTestDrive.main()
#BeverageTestDrive.main2()
#BeverageTestDrive.main3()
BeverageTestDrive.main4()