import inspect
import sys

from lib.database.QueryBuilder import QueryBuilder
from lib.model import Model


class Migrate:
    @staticmethod
    def generateTable(cls: Model):
        try:
            Migrate.deleteTable(cls)
        except:
            pass
        QueryBuilder.createTable(cls.__name__ + 's', cls.getVarDict())

    @staticmethod
    def deleteTable(cls):
        QueryBuilder.deleteTable(cls.__name__ + 's')

# Later
# @staticmethod
# def reset():
#     clsmembers = inspect.getmembers(sys.modules['Models'],
#                                     lambda member: print(member.__module__, '<----------------'))
#     print(clsmembers)
#     for i in clsmembers:
#         Migrate.generateTable(i)
