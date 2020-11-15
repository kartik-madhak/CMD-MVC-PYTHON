from lib.communication import Request, Response, ResponseType, View
from lib.controller import Middleware


class AuthMiddleware(Middleware):
    def handle(self, request: Request):
        return Response(ResponseType.error, View('', {}), 'You must login first')
