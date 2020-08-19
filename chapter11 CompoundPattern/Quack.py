from abc import ABCMeta, abstractmethod

class Quackable(metaclass=ABCMeta):
    def quack(self):
        pass

class MallarDuck(Quackable):
    def quack(self):
        print("ガーガー")

class RedheadDuck(Quackable):
    def quack(self):
        print("ガーガー")

class DuckCall(Quackable):
    def quack(self):
        print("ガアガア")

class RubberDuck(Quackable):
    def quack(self):
        print("キューキュー")

class Goose(Quackable):
    def hock(self):
        print("ガー")

class GooseAdapter():
    def __init__(self, goose:object):
        self.goose = Goose()
    
    def quack(self):
        self.goose.hock()
    
class QuackCounter(Quackable):
    def __init__(self, duck:object):
        self.__duck = duck
        self.__numberOfQuacks = 0
    
    def quack(self):
        self.__duck.quack()
        self.__numberOfQuacks += 1

    
    def numberOfQuacks(self) -> int:
        return self.__numberOfQuacks
    
class DuckSimulator():

    def main():
        mallarDuck = QuackCounter(MallarDuck())
        redheadDuck = QuackCounter(RedheadDuck())
        duckCall = QuackCounter(DuckCall())
        rubberDuck = QuackCounter(RubberDuck())
        goose = GooseAdapter(Goose())

        print("鴨のシュミレータ")

        mallarDuck.quack()
        redheadDuck.quack()
        duckCall.quack()
        rubberDuck.quack()
        goose.quack()

        print("鴨がないた回数"+str(rubberDuck.numberOfQuacks())+"回")

DuckSimulator.main()

