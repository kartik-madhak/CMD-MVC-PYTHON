import types
from datetime import datetime
from typing import List

from Models.User import User
from Models.User_auth import User_auth
from lib.communication import *
from lib.controller import Controller
from lib.database import QueryBuilder
from lib.view import View
from lib.database import *


class UserController(Controller):

    @staticmethod
    def show_login(request: Request):
        view = View('', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def login(request: Request):
        username = request.json['inputs']['name']
        password = request.json['inputs']['password']

        users: List[User] = User.query().select().where('name', username).where('password', password).get()
        if not users:
            view = View('', {'error': 'Invalid credentials. Please try again...'}, request.json)
            return Response(ResponseType.error, view)

        user = users[0]
        token = hash(user)

        User_auth.query().insert([user.id, token, datetime.today()])

        view = View('home', {'user': users[0]}, {'user_id': user.id, 'authToken': token})
        return Response(ResponseType.valid, view)

    @staticmethod
    def home(request: Request):
        loggedUserId: int = request.json['user_id']
        user: User = User.query().select().where('id', loggedUserId).getOne()

        view = View('home', {'user': user}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def logout(request: Request):
        loggedUserId: int = request.json['user_id']

        User_auth.query().delete().where('user_id', loggedUserId).get()

        view = View('', {})
        return Response(ResponseType.valid, view)
