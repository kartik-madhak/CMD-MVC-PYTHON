from typing import TypedDict

from lib.database import getConnection


class QueryBuilder:
    def __init__(self, dbname):
        self.__queryString = ''
        self.__whereString = ''
        self.__args = []
        self.dbname = dbname

    def setOutputClass(self, cls):
        self.cls = cls

    def select(self, *entities):
        if not entities:
            cols = '*'
        else:
            cols = ','.join(entities)
        self.__queryString += 'Select ' + cols + ' from ' + self.dbname
        return self

    def where(self, col: str, val, op='='):
        if self.__whereString == '':
            self.__whereString += ' where ' + (col + ' ' + op + ' ' + '%s')
        else:
            self.__whereString += (' and ' + col + ' ' + op + ' ' + '%s')
        self.__args.append(val)
        return self

    def orWhere(self, col: str, val, op='='):
        if self.__whereString == '':
            self.__whereString += ' where ' + (col + ' ' + op + ' ' + '%s')
        else:
            self.__whereString += (' or ' + col + ' ' + op + ' ' + '%s')
        self.__args.append(val)
        return self

    def get(self):
        query, args = self.__getQueryString()
        cursor = getConnection().getCursor()
        cursor.execute(query, args)
        return self.cls.transform(cursor.fetchall())

    def __getQueryString(self):
        res = self.__queryString + ' ' + self.__whereString
        args = self.__args
        self.__queryString = ''
        self.__args = []
        self.__whereString = ''
        return res, args

    @staticmethod
    def __convertValueToSQLType(value):
        if value == "<class 'int'>":
            return 'INT'
        elif value == "<class 'float'>":
            return 'FLOAT'
        elif value == "<class 'datetime.datetime'>":
            return 'datetime'
        elif value == "<class 'str'>":
            return 'VARCHAR(400)'

    @staticmethod
    def createTable(name: str, d: TypedDict):
        attrList = []
        for key, value in d.items():
            attrList.append(key + ' ' + QueryBuilder.__convertValueToSQLType(str(value)))
        query = 'create table ' + name + '(' + ','.join(attrList) + ')'
        cursor = getConnection().getCursor()
        cursor.execute(query)

    @staticmethod
    def deleteTable(name: str):
        query = 'drop table ' + name
        cursor = getConnection().getCursor()
        cursor.execute(query)
