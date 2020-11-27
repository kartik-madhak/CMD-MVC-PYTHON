from datetime import datetime
from typing import List

from Models.Notification import Notification
from lib.communication import *
from lib.controller import Controller
from lib.view import View


class NotificationController(Controller):
    @staticmethod
    def show(request: Request):
        user = request.user

        notifications: List[Notification] = Notification.query().select().where('is_read', 0).get()

        Notification.query().updateMany({'is_read': 1}).where('is_read', 0).getWithoutTransform()

        view = View('notifications.show', {'user': user, 'notifications': notifications, 'show_option': 1},
                    request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def show_all(request: Request):
        user = request.user

        notifications: List[Notification] = Notification.query().select().get()

        view = View('notifications.show', {'user': user, 'notifications': notifications}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def notifyUser(user: User, msg: str):
        Notification.query().insert([user.id, msg, 0, datetime.today(), datetime.today()])
