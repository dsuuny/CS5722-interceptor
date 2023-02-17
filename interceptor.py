from context import ContextObject

class Interceptor:
    def onRequest(self, contextObject:ContextObject):
        pass


class LoggerInterceptor(Interceptor):
    def onRequest(self, contextObject:ContextObject):
        contextObject.weatherData.getHumidity()
        contextObject.weatherData.getPressure()
        contextObject.weatherData.getPressure()
        # #
        print("LoggerInterceptor: logging the weatehr condition")