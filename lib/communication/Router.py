from lib.communication import Request
import Controllers
import Middlewares


class Router:
    def __init__(self, d={}):
        self.routes = d

    def sendRequest(self, request: Request):
        routeBuilder = self.routes[request.json['form_redirect']]
        for i in routeBuilder.middleware:
            result = Middlewares.callMiddleware(i, 'handle', request)
            if type(result) == Request:  # If middleware would return success, it will go to next middleware
                request = result
                continue
            else:  # It will return the response to viewHandler
                return result
        className, methodName = routeBuilder.controller.split('.')
        return Controllers.callController(className, methodName, request)
