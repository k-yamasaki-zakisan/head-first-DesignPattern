#pythonは通常同期メソッドのため、マルチメソッドの問題は考慮しなくていい？

class Singleton():
    def __uniqueInstance():
        pass

    def getInstance():
        try：
            uniqueInstance
        except:
            uniqueInstance = Singleton()
    
        return uniqueInstance