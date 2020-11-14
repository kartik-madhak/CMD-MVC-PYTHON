from collections import namedtuple

from lib.communication import *
from lib.view import View
from lib.database import *


class testController(object):
    def __init__(self):
        self.data = 4

    def func(self, request: Request) -> Response:
        request = request.json

        name = request['inputs']['name']
        password = request['inputs']['password']

        config = Config('localhost', 'root', '', 'test')
        conn = Connection(config)
        cursor = conn.getCursor()
        cursor.execute('select * from users where name = %s and password = %s', (name, password))
        user = cursor.fetchone()

        user = namedtuple('Struct', user.keys())(*user.values())

        if not user:
            return Response(ResponseType.error, None)

        view = View('index', {'user': user})
        return Response(ResponseType.valid, view)
