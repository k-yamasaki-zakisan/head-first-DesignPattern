from GumballMachine import GumballMachine

#実行パート
class gumballMachineTestDrive():
    def main():
        gumballMachine = GumballMachine(4)

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

        if gumballMachine.count == 0:
            gumballMachine.refill(5)
        

#実行
gumballMachineTestDrive.main()