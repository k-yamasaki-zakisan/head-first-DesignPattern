class WeatearData():
    def __init__(self, temperature, humidity, pressure):
        self.observers = []
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
    
    def registerObserver(self, o):
        self.observers.append(o)
    
    def removeObserver(self, o):
        i = self.observers.index(o)
        if i >= 0:
            self.observers.pop(i)
    
    def notifyObserver(self):
        for i in range(len(self.observers)):
            observer = observers[i]
            observer.update(temperature, humidity, pressure)
    
    def measurementsChanged(self):
        notifyObservers()
    
    def serMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(WeatearData):
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.weatearData = []

    def CurrentConditionsDisplay(self, weatearData):
        self.weatearData = weatearData
        self.weatearData.registerObserver(self)
    
    def update(temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        display()
    
    def display():
        print（"現在の気象情報：温度"+self.temperature）
