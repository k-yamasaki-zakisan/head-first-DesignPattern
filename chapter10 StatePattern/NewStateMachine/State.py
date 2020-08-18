from abc import ABCMeta, abstractmethod

#抽象パート
class State(metaclass=ABCMeta):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

    def refill(self):
        pass


#具象パート
class NoQuarterState(State):
    def __init__(self, gumballMachine:object):
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
    def __init__(self, gumballMachine:object):
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
    def __init__(self, gumballMachine:object):
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
    def __init__(self, gumballMachine:object):
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
    def __init__(self, gumballMachine:object):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("販売するガムボールがありません")
    
    def ejectQuarter(self):
        print("返金出来ません。販売するガムボールがありません")
    
    def turnCrank(self):
        print("販売するガムボールがありません")

    def dispense(self):
        print("販売するガムボールがありません")
    
    def refill(self):
        self.gumballMachine.setState(self.gumballMachine.noQuarterState)
