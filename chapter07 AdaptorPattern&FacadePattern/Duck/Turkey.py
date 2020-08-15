from abc import ABCMeta, abstractmethod
from Duck import Duck

#七面鳥
##抽象パート
class Turkey(metaclass=ABCMeta):
    def gobble():
        pass

    def fly():
        pass

##具象パート
class WildTurkey(Turkey):
    def gobble(self):
        print("ゴロゴロ")
    
    def fly(self):
        print("短い距離を飛んでいます")


##アダプターパート(メソッドの書き換え)
class TurkeyAdapter(Duck):
    #クラスのインスタンス（turkey）で初期化
    def __init__(self, turkey):
        self.__turkey = turkey
    
    def quack(self):
        self.__turkey.gobble()
    
    def fly(self):
        for i in range(5):
            self.__turkey.fly()