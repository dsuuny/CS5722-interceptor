from context import ContextObject
from os import remove

class Interceptor:
    def onRequest(self, contextObject:ContextObject):
        pass


class LoggerInterceptor(Interceptor):
    def __init__(self) -> None:
        self.log_path = "log.txt"
        remove(self.log_path)

    def onRequest(self, contextObject:ContextObject):
        
        humidity = contextObject.weatherData.getHumidity()
        tempreture = contextObject.weatherData.getTemp()
        pressure = contextObject.weatherData.getPressure()
   
        print("<<LoggerInterceptor>> logging the weatehr condition")
        with open(self.log_path, "a") as f:
            f.write(f"humidity:{humidity} Tempreture:{tempreture} Pressure:{pressure}\n")


class WarningInterceptor(Interceptor):
    def onRequest(self, contextObject:ContextObject):
        if contextObject.weatherData.getTemp() > 90:
            print(f"<<WarningInterceptor>> Be careful the tempreture is over {contextObject.weatherData.getTemp()}F!!!")

