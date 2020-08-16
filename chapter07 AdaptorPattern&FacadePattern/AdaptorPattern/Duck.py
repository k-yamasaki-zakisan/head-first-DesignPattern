from abc import ABCMeta, abstractmethod

#通常アヒル
##抽象パート
class Duck(metaclass=ABCMeta):
    @abstractmethod
    def quack():
        pass

    @abstractmethod
    def fly():
        pass

##具象パート
class MallardDuck(Duck):
    def quack(self):
        print("ガーガー")
    
    def fly(self):
        print("飛んでいます")


#コマンドテストクラス
class TestDuck():
    def __init__(self, duck):
        self.__duck = duck
        self.__duck.quack()
        self.__duck.fly()
