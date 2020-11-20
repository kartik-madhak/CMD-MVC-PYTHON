from lib.database.Config import Config
from lib.database.Connection import Connection

__connection = None


def getConnection():
    global __connection
    if __connection is None:
        config = Config('localhost', 'root', '', 'mydb')
        __connection = Connection(config)
    return __connection

from lib.database.QueryBuilder import QueryBuilder
