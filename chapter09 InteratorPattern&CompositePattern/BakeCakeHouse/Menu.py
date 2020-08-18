from abc import ABCMeta, abstractmethod

#抽象
class MenuItem(metaclass=ABCMeta):
    def __inin__(self, name:str, description:str, vegetarian:bool, price:float):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price
    
    @property
    def name(self) ->str:
        return self.__name
    
    @property
    def description(self) ->str:
        return self.__description
    
    @property
    def price(self) ->float:
        return self.__price
    
    @property
    def is_vegetarian(self) ->bool:
        return self.__vegetarian

#具象
class PancakeHouseMenu():
    def __init__(self):
        self.__menuItems = []
    
        self.addItem("K&Bのパンケーキ朝食",
                    "スクランブルエッグとトーストが付いたパンケーキ",
                    True,
                    2.99)
        self.addItem("通常のパンケーキ朝食",
                    "卵焼きとソーセージが付いたパンケーキ",
                    False,
                    2.99)
        self.addItem("ブルーベリーパンケーキ",
                    "新鮮なブルーベリーで作ったパンケーキ",
                    True,
                    3.49)
        self.addItem("ワッフル",
                    "ブルーベリーとイチゴをのせたパンケーキ",
                    True,
                    3.59)
    
    def addItem(self, name:str, description:str, vegetarian:bool, price:float):
        #__menuItem = MenuItem(name, description, vegetarian, price)
        __menuItem = MenuItem()
        self.__menuItems.append(__menuItem)
    
    @property
    def menuItems(self) -> list:
        return self.__menuItems
    
    def createInterator(self):
        return PancakeHouseMenuInterator(self.__menuItems)
    

class DinerMenu():
    def __init__(self):
        self.__maxItems = 6
        self.__menuItems = []

        self.addItem("ベジタリアンBLT",
                    "レタス.トマト.（偽）ベーコンに挟んだ全粒小麦パンサンドイッチ",
                    True,
                    2.99
        )
        self.addItem("BLT",
                    "レタス.トマト.ベーコンに挟んだ全粒小麦パンサンドイッチ",
                    True,
                    2.99
        )
        self.addItem("本日のスープ",
                    "ポテトサラダを添えた本日のスープ",
                    True,
                    3.29
        )
        self.addItem("Hoddog",
                    "サワークラフト、レリッシュ、玉ねぎ、チーズを挟んだホットドック",
                    True,
                    3.29
        )

    def addItem(self, name:str, description:str, vegetarian:bool, price:float):
        #__menuItem = MenuItem(name, description, vegetarian, price)
        __menuItem = MenuItem()
            
        if 6 <= len(self.__menuItems):
            print("メニューがいっぱいです、メニューに追加できません")
        else:
            self.__menuItems.append(__menuItem)
        
    def createInterator(self):
        return DinerMenuInterator(self.__menuItems)
        

#インテレーター（抽象パート）
class Interator(metaclass=ABCMeta):
    def hasNext() -> bool:
        pass
    
    def next():
        pass

class DinerMenuInterator(Interator):
    def __init__(self, items):
        self.__items = items
        self.__menuItem = ""
        self.__position = 0
    
    def next(self):
        self.__menuItem = self.__items[self.__position]
        self.__position += 1
        return self.__menuItem
    
    def hasNext(self) ->bool:
        if len(self.__items) <= self.__position or self.__items[self.__position] == None:
            return False
        else:
            return True


class PancakeHouseMenuInterator(Interator):
    def __init__(self, items):
        self.__items = items
        self.__menuItem = ""
        self.__position = 0
    
    def next(self):
        self.__menuItem = self.__items[self.__position]
        self.__position += 1
        return self.__menuItem
    
    def hasNext(self) ->bool:
        print(self.__items)
        if len(self.__items) <= self.__position or self.__items[self.__position] == None:
            return False
        else:
            return True

    
class Waitress():
    def __init__(self, pancakeHouseMenu, dinerMenu):
        self.__pancakeHouseMenu = pancakeHouseMenu
        self.__dinerMenu = dinerMenu
    
    def printMenu(self):
        pancakeMenu = self.__pancakeHouseMenu.createInterator()
        dinerMenu = self.__dinerMenu.createInterator()
        if self.__pancakeHouseMenu:
            print("メニューーーーーーーーー")
            self.__printMenu(PancakeHouseMenuInterator(pancakeMenu))
        if self.__dinerMenu:
            print("メニューーーーーーーーー")
            self.__printMenu(DinerMenuInterator(dinerMenu))
        
    def __printMenu(self, iterator):
        while iterator.hasNext():
            menuItem = iterator.next()
            print(menuItem.name())
            print(menuItem.price)
            print(menuItem.description())
    

#実行パート
class MenuTestDrive():
    def main():
        pancakeHouseMenu = PancakeHouseMenu()
        dinerMenu = DinerMenu()
        waitress = Waitress(pancakeHouseMenu,dinerMenu)

        waitress.printMenu()


MenuTestDrive.main()




        
        
        
    



    

    
    