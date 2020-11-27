import hashlib
import types
from datetime import datetime
from typing import List

from Controllers import NotificationController
from Models.Notification import Notification
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
        password: str = request.json['inputs']['password']

        passHash = hashlib.sha256(password.encode())
        passHash = passHash.hexdigest()

        users: List[User] = User.query().select().where('name', username).where('passwordHash', passHash).get()
        if not users:
            view = View('', {'error': 'Invalid credentials. Please try again...'}, request.json)
            return Response(ResponseType.error, view)

        user = users[0]
        token = user.hash()

        User_auth.query().insert([user.id, token, datetime.today(), datetime.today()])

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

    @staticmethod
    def register(request: Request):
        username = request.json['inputs']['name']
        email = request.json['inputs']['email']
        password: str = request.json['inputs']['password']
        re_password = request.json['inputs']['re_password']
        role = 1 if request.json['inputs']['role'] == '1' else 2

        if len(password) < 8:
            view = View('', objects={'error': 'Password too short. Please try again...'})
            return Response(ResponseType.error, view)
        if password != re_password:
            view = View('', objects={'error': 'Passwords do not match. Please try again...'})
            return Response(ResponseType.error, view)
        if '@' not in email or '.' not in email:
            view = View('', objects={'error': 'Email format is wrong. Please try again...'})
            return Response(ResponseType.error, view)

        user = User.query().select().where('name', username).getOne()
        if user is not None:
            view = View('', objects={'error': 'Username already taken. Please try again...'})
            return Response(ResponseType.error, view)

        passHash = hashlib.sha256(password.encode())
        passHash = passHash.hexdigest()

        User.query().insert([username, email, '', passHash, role, datetime.today(), datetime.today()])

        user: User = User.query().select().where('name', username).getOne()
        token = user.hash()

        User_auth.query().insert([user.id, token, datetime.today(), datetime.today()])

        NotificationController.notifyUser(user, 'Welcome to freelancerHub, Feel free to look around the site.')

        view = View('home', {'user': user}, {'user_id': user.id, 'authToken': token})
        return Response(ResponseType.valid, view)

    @staticmethod
    def show_edit(request: Request):
        view = View('user.edit', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def edit_description(request: Request):
        loggedUserId: int = request.json['user_id']
        desc = request.json['inputs']['description']

        user: User = User.query().select().where('id', loggedUserId).getOne()

        user.description = desc
        user.save()

        view = View('home', {'user': user}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def edit_password(request: Request):
        loggedUserId: int = request.json['user_id']
        old_password = request.json['inputs']['old_password']
        password = request.json['inputs']['password']
        re_password = request.json['inputs']['re_password']

        user: User = User.query().select().where('id', loggedUserId).getOne()

        if password != re_password:
            view = View('user.edit', {'error': 'passwords do not match'}, request.json)
            return Response(ResponseType.valid, view)

        passHash = hashlib.sha256(old_password.encode())
        passHash = passHash.hexdigest()

        if user.passwordHash != passHash:
            view = View('user.edit', {'error': 'old password is wrong'}, request.json)
            return Response(ResponseType.valid, view)

        passHash = hashlib.sha256(password.encode())
        passHash = passHash.hexdigest()

        user.passwordHash = passHash
        user.save()

        view = View('home', {'user': user}, request.json)
        return Response(ResponseType.valid, view)


