from datetime import datetime
from typing import List

from Models import User
from Models.User_auth import User_auth
from lib.communication import Request, Response, ResponseType, View
from lib.controller import Middleware
from lib.database.QueryBuilder import QueryBuilder


class AuthMiddleware(Middleware):
    def handle(self, request: Request):
        if 'authToken' in request.json and 'user_id' in request.json:
            auth: List[User_auth] = User_auth.query().select().where('user_id', request.json['user_id']). \
                where('token', request.json['authToken']).getWithoutTransform()
            if auth != ():
                return request
            else:
                return Response(
                    responseType=ResponseType.error,
                    view=View('', {'error': 'You need to login first'}, request.json))

        return Response(
            responseType=ResponseType.error,
            view=View('', {'error': 'You must login first'}, request.json))
