class SetMeasurements:
    def setMeasurement():
        pass

class Observer:
    def update():
        pass

class DisplayElement:
    def display():
        pass

class Subject:
    def attach(observer:Observer):
        pass

    def detach(observer:Observer):
        pass

    def notify(self):
        pass

class GetMeasurements:
    def getTemp(self):
        pass

    def getHumidity(self):
        pass

    def getPressure(self):
        pass

class WeatherData(SetMeasurements, Subject, GetMeasurements):
    def __init__(self) -> None:
        self.observers:list[Observer] = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def attach(self, observer:Observer):
        self.observers.append(observer)

    def detach(self, observer:Observer):
        self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def setMeasurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        # self.notify()
    
    def getTemp(self):
        return self.temperature
    
    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData:WeatherData) -> None:
        self.weatherData = weatherData
        self.weatherData.attach(self)
        self.temperature = None
        self.humidity = None
  
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
  
    def display(self):
        print(f"current condition: {self.temperature}F degrees and {self.humidity}% humidity")

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData:WeatherData) -> None:
        self.weatherData = weatherData
        self.weatherData.attach(self)
        self.maxTemp = 0
        self.minTemp= 200
        self.tempSum = 0
        self.numReadings = 0
  
    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.numReadings += 1
        
        if temperature > self.maxTemp:
            self.maxTemp = temperature
        
        if temperature < self.minTemp:
            self.minTemp = temperature
        self.display()
  
    def display(self):
        print(f"Avg/Max/Min temperature : {self.tempSum/self.numReadings}/{self.maxTemp}/{self.minTemp}")

class WeatherStation():
    def __init__(self) -> None:
        self.weatherData = WeatherData()
        self.currentConditionsDisplay = CurrentConditionsDisplay(self.weatherData) #register the display to weatherData
        self.statisticsDisplay = StatisticsDisplay(self.weatherData)

    def public(self, temperature, humidity, pressure):
        self.weatherData.setMeasurement(temperature, humidity, pressure)


""" 
step1: observer pattern
step2: identify interception point   
    I think it is the 
        PreMarshalOutRequest: 
step3: specify the context object
step4: specify the interceptors
step5: specify the dispatchers 
step6: implement callback mechanisms in concrete Framework
step7: implement concrete interceptors
"""
if __name__ == "__main__":
    wd = WeatherStation()
    wd.public(80, 65, 30)
    wd.public(82, 70, 20)