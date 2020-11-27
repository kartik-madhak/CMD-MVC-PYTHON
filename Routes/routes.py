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
            'user.edit.password': RouteBuilder(controller='UserController.edit_password', middleware=['AuthMiddleware']),

            'post.add_form': RouteBuilder(controller='PostController.show_add_form', middleware=['AuthMiddleware']),
            'post.add': RouteBuilder(controller='PostController.add', middleware=['AuthMiddleware']),
            'post.show': RouteBuilder(controller='PostController.show', middleware=['AuthMiddleware']),
            'post.load': RouteBuilder(controller='PostController.load', middleware=['AuthMiddleware']),
            'post.like': RouteBuilder(controller='PostController.like', middleware=['AuthMiddleware']),

            'post.show_all': RouteBuilder(controller='PostController.show_all', middleware=['AuthMiddleware']),

            'comment.add_form': RouteBuilder(controller='CommentController.add_form', middleware=['AuthMiddleware']),
            'comment.add': RouteBuilder(controller='CommentController.add', middleware=['AuthMiddleware']),
            'comment.view': RouteBuilder(controller='CommentController.view', middleware=['AuthMiddleware']),

            'notifications.show': RouteBuilder(controller='NotificationController.show', middleware=['AuthMiddleware']),
            'notifications.show_all': RouteBuilder(controller='NotificationController.show_all', middleware=['AuthMiddleware']),
    }
