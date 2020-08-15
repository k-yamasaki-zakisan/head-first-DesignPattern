from Duck import MallardDuck, TestDuck
from Turkey import WildTurkey, TurkeyAdapter

#実行パート
class DuckTestDrive():
    def main():
        duck = MallardDuck()

        turkey = WildTurkey()
        turkeyAdapter = TurkeyAdapter(turkey)

        print("Turkeyの出力-------------------")
        turkey.gobble()             #ゴロゴロ
        turkey.fly()                #短い距離を飛んでいます

        print("Duckの出力---------------------")
        TestDuck(duck)              #ガーガー
                                    #飛んでいます

        print("TurkeyAdapterの出力------------")
        TestDuck(turkeyAdapter)     #ゴロゴロ
                                    #短い距離を飛んでいます
                                    #短い距離を飛んでいます
                                    #短い距離を飛んでいます
                                    #短い距離を飛んでいます
                                    #短い距離を飛んでいます

DuckTestDrive.main()

