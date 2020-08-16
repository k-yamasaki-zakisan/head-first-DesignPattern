from Duck import Duck

#実行パート
class DuckSortTestDrive():
    def main():
        ducks = [
            Duck("ダッフィー", 8),
            Duck("デゥーイ", 2),
            Duck("ハワード", 7),
            Duck("ルーイ", 2),
            Duck("ドナルド", 10),
            Duck("ヒューイ", 2)
        ]

        print("---------------ソート前---------------")

        for duck in ducks:
            print(duck.toString())
        
        #バブルソート 最悪計算量O(N^2)
        change = True
        while change:
            change = False
            for i in range(1,len(ducks)):
                reself = ducks[i].compareTo(ducks[i-1])
                if reself == -1:
                    change = True
                    tmpOjb = ducks[i-1]
                    ducks[i-1] = ducks[i]
                    ducks[i] = tmpOjb
            if change == False:
                break

        print("---------------ソート後---------------")

        for duck in ducks:
            print(duck.toString())

#実行
DuckSortTestDrive.main()