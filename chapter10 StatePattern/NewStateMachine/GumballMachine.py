from State import NoQuarterState, HasQuarterState, SoldState, WinnerState, SoldOutState

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
        
    def setState(self, state:object):
        self.__state = state
        
    def releaseBall(self):
        print("ガムボールがスロットから転がり出てきます")
        if self.__count != 0:
            self.__count -= 1
    
    def refill(self, count:int):
        self.__count += count
        print("ガムボールは補充されました。新たなカウントは" + str(self.__count))
        self.__state.refill()
        
    @property
    def soldOutState(self) -> object:
        return self.__soldOutState
        
    @property
    def noQuarterState(self) -> object:
        return self.__noQuarterState

    @property
    def hasQuarterState(self)-> object:
        return self.__hasQuarterState
        
    @property
    def soldState(self) -> object:
        return self.__soldState
        
    @property
    def winnerState(self) -> object:
        return self.__winnerState
        
    @property
    def count(self) -> int:
        return self.__count
        
    @property
    def state(self) -> object:
        return self.__state