from typing import List


class RouteBuilder:
    def __init__(self, controller: str, middleware: List[str] = []):
        self.controller = controller
        self.middleware = middleware


def getRoutes():
    return {
            '': RouteBuilder(controller='UserController.show_login'),
            'home': RouteBuilder(controller='UserController.home', middleware=['AuthMiddleware']),
            'login': RouteBuilder(controller='UserController.login'),
            'logout': RouteBuilder(controller='UserController.logout'),

    }
