from Duck import MallardDuck, TestDuck
from Turkey import WildTurkey, TurkeyAdapter

#実行パート
class DuckTestDrive():
    def main():
        duck = MallardDuck()

        turkey = WildTurkey()
        turkeyAdapter = TurkeyAdapter(turkey)

        print("Turkeyの出力-------------------")
        turkey.gobble()
        turkey.fly()

        print("Duckの出力---------------------")
        TestDuck(duck)

        print("TurkeyAdapterの出力------------")
        TestDuck(turkeyAdapter)

DuckTestDrive.main()