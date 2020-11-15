import types

from Models.User import User
from lib.communication import *
from lib.controller import Controller
from lib.view import View
from lib.database import *


class testController(Controller):
    @staticmethod
    def login(request: Request):
        username = request.json['inputs']['username']
        password = request.json['inputs']['password']

        users = User.query().select().where('name', username).where('password', password).get()
        if not users:
            return Response(ResponseType.error, None, 'Invalid credentials. Please try again...')

        view = View('home', {'user': users[0]})
        return Response(ResponseType.valid, view, '')

    @staticmethod
    def logout(request: Request):
        view = View('', {})
        return Response(ResponseType.valid, view, '')

    @staticmethod
    def timepass(request: Request):
        users = User.query().select().get()
        view = View('timepass', {'users': users})
        return Response(ResponseType.valid, view, '')