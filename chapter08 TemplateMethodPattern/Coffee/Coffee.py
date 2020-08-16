from abc import ABCMeta, abstractmethod

#注文品目
##抽象パート
class CaffeineBeverage(metaclass=ABCMeta):
    def prepareRecipe(self):
        self.brew()
        self.boilWater()
        self.pourInCup()
        if self.customerWantCondiments():
            self.addCondiments()
        self.reselt()

    def brew(self):
        pass

    def addCondiments(self):
        pass

    def boilWater(self):
        print("お湯を沸かします")
    
    def pourInCup(self):
        print("カップに注ぎます")
    
    def reselt(self):
        pass
    
    #フックメソッド（サブクラスでオーバーライド可なメソッド）
    @property
    def customerWantCondiments(self):
        return True

##具象パート
class Coffee(CaffeineBeverage):
    def brew(self):
        print("フィルタでコーヒをドリップします")

    def addCondiments(self):
        print("砂糖とミルクを追加します")
    
    def customerWantCondiments(self):
        pass
    
    def reselt(self):
        print("コーヒをお持ちしました")

class CoffeeWithHook(CaffeineBeverage):
    def __init__(self):
        self.thisCoffee = "コーヒー"

    def brew(self):
        print("フィルタでコーヒをドリップします")

    def addCondiments(self):
        print("砂糖とミルクを追加します")

    def customerWantCondiments(self):
        self.__answer = self.__getUserInput()

        if self.__answer == "y" or self.__answer == "Y":
            self.thisCoffee = "砂糖+ミルク+" + self.thisCoffee
            return True
        else:
            return False
    
    def __getUserInput(self):
        self.__answer = None
        
        print("コーヒーに砂糖とミルクを入れますか？(y/n)")

        #[y/n]を表示して確認や対象指示
        try:
            __ans=input()
        except:
            print("読み取りに失敗しました-------------------")
        
        if __ans == None:
            return "No"
        
        return __ans
    
    def reselt(self):
        print(self.thisCoffee+"をお持ちしました")

class Tea(CaffeineBeverage):
    def brew(self):
        print("紅茶を浸します")
    
    def addCondiments(self):
        print("レモンを追加する")

    def customerWantCondiments(self):
        return True
    
    def reselt(self):
        print("紅茶をお持ちしました")

class TeaWithHook(CaffeineBeverage):
    def __init__(self):
        self.thisTea = "紅茶"

    def brew(self):
        print("紅茶を浸します")

    def addCondiments(self):
        print("レモンを追加する")

    def customerWantCondiments(self):
        self.__answer = self.__getUserInput()

        if self.__answer == "y" or self.__answer == "Y":
            self.thisTea = self.thisTea + "+レモン"
            return True
        else:
            return False
    
    def __getUserInput(self):
        self.__answer = None
        
        print("紅茶にレモンを付けますか？(y/n)")

        #[y/n]を表示して確認や対象指示
        try:
            __ans=input()
        except:
            print("読み取りに失敗しました-------------------")
        
        if __ans == None:
            return "No"
        
        return __ans
    
    def reselt(self):
        print(self.thisTea+"をお持ちしました")

