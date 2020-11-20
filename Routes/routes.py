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
            'register': RouteBuilder(controller='UserController.register'),

            'user.edit': RouteBuilder(controller='UserController.show_edit', middleware=['AuthMiddleware']),
            'user.edit.description': RouteBuilder(controller='UserController.edit_description', middleware=['AuthMiddleware']),
            'user.edit.password': RouteBuilder(controller='UserController.edit_password', middleware=['AuthMiddleware'])
    }
