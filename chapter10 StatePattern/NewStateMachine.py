from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("25セントを投入しました")
        self.gumballMachine.setState(self.gumballMachine.hasQuarterState)
    
    def ejectQuarter(self):
        print("25セント投入していません")
    
    def turnCrank(self):
        print("クランクを回しましたが25セントを投入していません")

    def dispense(self):
        print("まず支払いをする必要があります")

class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("もう一度25セントを投入してください")
    
    def ejectQuarter(self):
        print("25セント返却しました")
        self.gumballMachine.setState(self.gumballMachine.noQuarterState)
    
    def turnCrank(self):
        print("クランクを回しました..............")
        import random
        random_count = random.randrange(1, 6)
        if random_count == 1 and 0 < self.gumballMachine.count:
            self.gumballMachine.setState(self.gumballMachine.winnerState)
        else:
            self.gumballMachine.setState(self.gumballMachine.soldState)

    def dispense(self):
        print("販売するガムボールがありません")
    
class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("お待ちください。既にガムボールを出しています")
    
    def ejectQuarter(self):
        print("申しわけありません。既にクランクを回しています")
    
    def turnCrank(self):
        print("2回回してもガムボールはもう１つ手に入れることは出来ません")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if 0 < self.gumballMachine.count:
            self.gumballMachine.setState(self.gumballMachine.noQuarterState)
        else:
            print("おっと、ガムボールがなくなりました")
            self.gumballMachine.setState(self.gumballMachine.soldOutState)

class WinnerState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("お待ちください。既にガムボールを出しています")
    
    def ejectQuarter(self):
        print("申しわけありません。既にクランクを回しています")
    
    def turnCrank(self):
        print("2回回してもガムボールはもう１つ手に入れることは出来ません")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.count == 0:
            self.gumballMachine.setState(self.gumballMachine.soldOutState)
        else:
            self.gumballMachine.releaseBall()
            print("当たりです！！２５セントで２つのガムがもらえます！！")
            if 0 < self.gumballMachine.count:
                self.gumballMachine.setState(self.gumballMachine.noQuarterState)
            else :
                print("おっと、ガムボールがなくなりました")
                self.gumballMachine.setState(self.gumballMachine.soldOutState)


class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("販売するガムボールがありません")
    
    def ejectQuarter(self):
        print("返金出来ません。販売するガムボールがありません")
    
    def turnCrank(self):
        print("販売するガムボールがありません")

    def dispense(self):
        print("販売するガムボールがありません")
    

class GumballMachine():
    def __init__(self, numberGumballs:int):
        self.__soldOutState = SoldOutState(self)
        self.__noQuarterState = NoQuarterState(self)
        self.__hasQuarterState = HasQuarterState(self)
        self.__soldState = SoldState(self)
        self.__winnerState = WinnerState(self)
        self.__state = self.__soldState
        self.__count = numberGumballs
        if 0 < self.__count:
            self.__state = self.__noQuarterState
        
    def insertQuarter(self):
        self.__state.insertQuarter()
        
    def ejectQuarter(self):
        self.__state.ejectQuarter()
        
    def turnCrank(self):
        self.__state.turnCrank()

    def dispense(self):
        self.__state.dispense()
        
    def setState(self, state):
        self.__state = state
        
    def releaseBall(self):
        print("ガムボールがスロットから転がり出てきます")
        if self.__count != 0:
            self.__count -= 1
        
    @property
    def soldOutState(self):
        return self.__soldOutState
        
    @property
    def noQuarterState(self):
        return self.__noQuarterState

    @property
    def hasQuarterState(self):
        return self.__hasQuarterState
        
    @property
    def soldState(self):
        return self.__soldState
        
    @property
    def winnerState(self):
        return self.__winnerState
        
    @property
    def count(self):
        return self.__count
        
    @property
    def state(self):
        return self.__state
    

#実行パート
class gumballMachineTestDrive():
    def main():
        gumballMachine = GumballMachine(5)

        print("---------------------------------")
        print("残ボール数："+ str(gumballMachine.count))
        print("---------------------------------")

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.dispense()

        print("---------------------------------")
        print("残ボール数："+ str(gumballMachine.count))
        print("---------------------------------")

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.dispense()

        print("---------------------------------")
        print("残ボール数："+ str(gumballMachine.count))
        print("---------------------------------")

        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.dispense()

        print("---------------------------------")
        print("残ボール数："+ str(gumballMachine.count))
        print("---------------------------------")
        

#実行
gumballMachineTestDrive.main()