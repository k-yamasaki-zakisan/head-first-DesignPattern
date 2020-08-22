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

    
class QuackCountInjecter(Quackable):
    def __init__(self, duck:object):
        self.__duck = duck
        self.__quackCounter = QuackCounter()
    
    def quack(self):
        self.__duck.quack()
        self.__quackCounter.addCounter()

    
    def numberOfQuacks(self) -> int:
        return self.__quackCounter.numberOfQuacks()

class Flock(Quackable):
    def __init__(self):
        self.__quakers = []
    
    def add(self, quacker:object):
        self.__quakers.append(quacker)
    
    def quack(self):
        iterator = self.__quakers
        for ite in iterator:
            ite.quack()
        

class QuackCounter():
    __quackCount = 0
    def addCounter(self):
        self.__quackCount += 1
    
    def numberOfQuacks(self) -> int:
        return self.__quackCount

#ファクトリ
##抽象パート
class abstractDuckFactory(metaclass=ABCMeta):
    def createMallarDuck(self):
        pass

    def createRedheadDuck(self):
        pass

    def createDuckCall(self):
        pass

    def createRubberDuck(self):
        pass

##具象パート
class DuckFactory(abstractDuckFactory):
    def createMallarDuck(self) -> object:
        return MallarDuck()
    
    def createRedheadDuck(self) -> object:
        return RedheadDuck()
    
    def createDuckCall(self) -> object:
        return DuckCall()
    
    def createRubberDuck(self) -> object:
        return RubberDuck()

class CountingDuckFactory(abstractDuckFactory):
    def createMallarDuck() -> object:
        return QuackCountInjecter(MallarDuck())
    
    def createRedheadDuck() -> object:
        return QuackCountInjecter(RedheadDuck())
    
    def createDuckCall() -> object:
        return QuackCountInjecter(DuckCall())
    
    def createRubberDuck() -> object:
        return QuackCountInjecter(RubberDuck())


    
class DuckSimulator():

    def mainTest():
        quackCounter = QuackCounter()
        mallarDuck = QuackCountInjecter(MallarDuck())
        redheadDuck = QuackCountInjecter(RedheadDuck())
        duckCall = QuackCountInjecter(DuckCall())
        rubberDuck = QuackCountInjecter(RubberDuck())
        goose = GooseAdapter(Goose())

        print("鴨のシュミレータ")

        mallarDuck.quack()
        redheadDuck.quack()
        duckCall.quack()
        rubberDuck.quack()
        goose.quack()

        print("鴨がないた回数"+str(quackCounter.numberOfQuacks())+"回")

    def flockTest():
        mallarDuck = CountingDuckFactory.createMallarDuck()
        redheadDuck = CountingDuckFactory.createRedheadDuck()
        duckCall = CountingDuckFactory.createDuckCall()
        rubberDuck = CountingDuckFactory.createRubberDuck()
        goose = GooseAdapter(Goose())

        print('鴨シュミュレーター')

        flockDucks = Flock()

        flockDucks.add(mallarDuck)
        flockDucks.add(redheadDuck)
        flockDucks.add(duckCall)
        flockDucks.add(rubberDuck)

        flockMallarDucks = Flock()

        mallarDuck1 = CountingDuckFactory.createMallarDuck()
        mallarDuck2 = CountingDuckFactory.createMallarDuck()
        mallarDuck3 = CountingDuckFactory.createMallarDuck()
        mallarDuck4 = CountingDuckFactory.createMallarDuck()

        flockMallarDucks.add(mallarDuck1)
        flockMallarDucks.add(mallarDuck2)
        flockMallarDucks.add(mallarDuck3)
        flockMallarDucks.add(mallarDuck4)

        flockDucks.add(flockMallarDucks)

        print("鳩の群れシュミレーション")
        flockDucks.quack()

        print("マガモの群れシュミレーター")
        flockMallarDucks.quack()
        

    def simulate(self, duck:object):
        self.duck.quack()



#DuckSimulator.mainTest()
DuckSimulator.flockTest()
