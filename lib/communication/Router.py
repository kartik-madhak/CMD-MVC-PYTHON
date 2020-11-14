from lib.communication import Request
import Controllers


class Router:
    def __init__(self, d={}):
        self.routes = d

    def sendRequest(self, routeName: str, request: Request):
        try:
            s = self.routes[routeName]
        except KeyError as e:
            print(e)
            return
        className, methodName = s.split('.')
        return Controllers.callController(className, methodName, request)

    def getRoute(self, name):
        try:
            return self.routes[name]
        except KeyError:
            return None
