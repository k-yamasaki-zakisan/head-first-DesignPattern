#抽象パート
class Subject():
    def registerObserver(observer):
        return
    
    def removeObserver(observer):
        return
    
    def notifyObservers():
        return

class Observer():
    def update(temp, humidity, pressure):
        return

class DisplayElement():
    def display():
        return


#具現パート
class WeatharData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure= 0
    
    def registerObserver(self, o):
        self.observers.append(o)
    
    def removeObserver(self, o):
        i = self.observers.index(o)
        if i >= 0:
            self.observers.pop(i)
    
    def notifyObservers(self):
        for i in range(len(self.observers)):
            observer = observers[i]
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, WeatharData):
        self.temperature = WeatharData.temperature
        self.humidity= WeatharData.humidity
        self.weatharData = WeatharData

    def CurrentConditionsDisplay(self, weatharData):
        self.weatharData = weatharData
        self.weatharData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
    
    def display(self):
        print("現在の気象情報：温度"+str(self.temperature)+"度　湿度"+str(self.humidity)+"%")


#天気データ取得パート
class WeatherStation():
    def main():
        weatharData = WeatharData()
        currentDisplay = CurrentConditionsDisplay(weatharData)

        weatharData.setMeasurements(27, 65, 30.4)
        weatharData.setMeasurements(28, 70, 29.2)
        weatharData.setMeasurements(26, 90, 29.2)

#実行パート
WeatherStation.main()


