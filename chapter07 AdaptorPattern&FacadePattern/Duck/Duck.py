from abc import ABCMeta, abstractmethod

#通常アヒル
##抽象パート
class Duck(metaclass=ABCMeta):
    def quack():
        pass

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
        self.duck = duck
        self.duck.quack()
        self.duck.fly()
