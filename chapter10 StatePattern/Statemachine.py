from abc import ABCMeta, abstractmethod

class GumvallMachine():
    def __init__(self, count:int):
        self.__SoldOut = 0
        self.__NoQuarter = 1
        self.__HasQuarter = 2
        self.__Sold = 3
        self.__state = self.__SoldOut
        self.__count = count
        if 0 < count:
            self.__state = self.__NoQuarter
    
    #@property
    def count(self) ->int:
        return self.__count
    
    def insertQuarter(self):
        if self.__state == self.__HasQuarter:
            print("既に２５セントを投入しています")
        elif self.__state == self.__NoQuarter:
            self.__state = self.__HasQuarter
            print("25セントを投入しました")
        elif self.__state == self.__SoldOut:
            print("25セント投入することは出来ません。このマシンは売り切れです")
        elif self.__state == self.__Sold:
            print("お待ちください、既にガムボールを出しています")
    
    def ejectQuarter(self):
        if self.__state == self.__HasQuarter:
            print("25セントを返却しました")
            self.__state = self.__NoQuarter
        elif self.__state == self.__NoQuarter:
            print("25セントを投入していません")
        elif self.__state == self.__Sold:
            print("既にクランクを回しています")
        elif self.__state == self.__SoldOut:
            print("返金出来ません。まだ２５セントを入れていません")
    
    def turnCrank(self):
        if self.__state == self.__Sold:
            print("2回回しても噛むボールはもう１つ手に入れることは出来ません")
        elif self.__state == self.__NoQuarter:
            print("クランクを回しましたが２５セントを投入していません")
        elif self.__state == self.__SoldOut:
            print("クランクを回しましたがガムボールがありません")
        elif self.__state == self.__HasQuarter:
            print("クランクを回しました.......")
            self.__state = self.__Sold
            self.disponse()
    
    def disponse(self):
        if self.__state == self.__Sold:
            print("ガムボールがスロットから転がり出てきます")
            self.__count -= 1 
            if self.__count == 0:
                print("ガムボールがなくなりました")
                self.__state = self.__SoldOut
            else:
                self.__state = self.__NoQuarter
        elif self.__state == self.__NoQuarter:
            print("まず支払いをする必要があります")
        elif self.__state == self.__SoldOut:
            print("販売するガムボールがありません")
        elif self.__state == self.__HasQuarter:
            print("販売するガムボールはありません")


class GumvallMachineTestDrive():
    def main():
        gumvallMachine = GumvallMachine(5)

        print("------------------------")
        print("残ボール数"+str(gumvallMachine.count()))
        print("------------------------")

        gumvallMachine.insertQuarter()
        gumvallMachine.turnCrank()

        print("------------------------")
        print("残ボール数"+str(gumvallMachine.count()))
        print("------------------------")

        gumvallMachine.insertQuarter()
        gumvallMachine.ejectQuarter()
        gumvallMachine.turnCrank()

        print("------------------------")
        print("残ボール数"+str(gumvallMachine.count()))
        print("------------------------")

        gumvallMachine.insertQuarter()
        gumvallMachine.turnCrank()
        gumvallMachine.insertQuarter()
        gumvallMachine.turnCrank()
        gumvallMachine.ejectQuarter()

        print("------------------------")
        print("残ボール数"+str(gumvallMachine.count()))
        print("------------------------")

        gumvallMachine.insertQuarter()
        gumvallMachine.insertQuarter()
        gumvallMachine.turnCrank()
        gumvallMachine.insertQuarter()
        gumvallMachine.turnCrank()
        gumvallMachine.insertQuarter()

        print("------------------------")
        print("残ボール数"+str(gumvallMachine.count()))
        print("------------------------")

GumvallMachineTestDrive.main()
