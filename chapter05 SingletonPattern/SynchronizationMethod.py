#pythonは通常同期メソッドのため、マルチスレッドの問題は考慮しなくていい？

class Singleton():
    def __uniqueInstance():
        pass

    def getInstance():
        try：
            uniqueInstance
        except:
            uniqueInstance = Singleton()
    
        return uniqueInstance