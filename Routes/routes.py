from typing import List


class RouteBuilder:
    def __init__(self, controller: str, middleware: List[str] = []):
        self.controller = controller
        self.middleware = middleware


def getRoutes():
    return {
            'home': RouteBuilder(controller='testController.home', middleware=['AuthMiddleware']),
            'login': RouteBuilder(controller='testController.login'),
            'logout': RouteBuilder(controller='testController.logout'),
            'timepass': RouteBuilder(controller='testController.timepass')
    }
