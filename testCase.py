from dispather import Dispather
from context import ContextObject
from framework import WeatherData
from interceptor import LoggerInterceptor, WarningInterceptor

class WeatherStation():
    def __init__(self) -> None:
        self.weatherData = WeatherData()
        self.disPatcher = Dispather(ContextObject(self.weatherData))
        self.weatherData.attach(self.disPatcher)
        # self.currentConditionsDisplay = CurrentConditionsDisplay(self.weatherData) #register the display to weatherData
        # self.statisticsDisplay = StatisticsDisplay(self.weatherData)

    def publish(self, temperature, humidity, pressure):
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
    wd.disPatcher.registerInterceptor(LoggerInterceptor())
    wd.disPatcher.registerInterceptor(WarningInterceptor())
    wd.publish(80, 65, 30)
    wd.publish(91, 70, 20)