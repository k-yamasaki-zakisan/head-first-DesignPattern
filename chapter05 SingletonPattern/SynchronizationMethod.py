#pythonは通常同期メソッドのため、マルチスレッドの問題は考慮しなくていい？

class Singleton():
    def __uniqueInstance():
        @abstractmethod
        pass

    def getInstance():
        try:
            uniqueInstance
        except:
            uniqueInstance = Singleton()
    
        return uniqueInstance