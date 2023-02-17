from interceptor import Interceptor
from framework import Observer, CurrentConditionsDisplay, StatisticsDisplay, WeatherData
from context import ContextObject

class Dispather(WeatherData, Observer):
    def __init__(self, contextObject:ContextObject) -> None:
        self.interceptors:list[Interceptor] = []
        self.observers:list[Observer] = []
        self.registerObservers()
        self.contextObject = contextObject

    def registerInterceptor(self, interceptor:Interceptor):
        self.interceptors.append(interceptor)

    
    def removeInterceptor(self, interceptor:Interceptor):
        self.interceptors.remove(interceptor)

    def update(self, temperature, humidity, pressure):
        self.dispatch(self.contextObject)

    def dispatch(self, contextObject:ContextObject):
        for interceptor in self.interceptors:
            interceptor.onRequest(contextObject)
            # interceptor.onRequest(contextObject)
        self.notify(contextObject)
    
    def notify(self, contextObject:ContextObject):
        for observer in self.observers:
            observer.update(contextObject.weatherData.getTemp(), 
                            contextObject.weatherData.getHumidity(), 
                            contextObject.weatherData.getPressure())

    def registerObservers(self):
        currentConditionsDisplay = CurrentConditionsDisplay(self)
        statisticsDisplay = StatisticsDisplay(self)


