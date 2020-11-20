from typing import TypedDict

from lib.database import getConnection


class QueryBuilder:
    def __init__(self, dbname, cls=None):
        self.cls = cls
        self.__queryString = ''
        self.__whereString = ''
        self.__args = []
        self.dbname = dbname

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

    def getWithoutTransform(self):
        query, args = self.__getQueryString()
        cursor = getConnection().getCursor()
        cursor.execute(query, args)
        res = cursor.fetchall()
        return res

    def get(self):
        return self.cls.transform(self.getWithoutTransform())

    def getOne(self):
        try:
            return self.get()[0]
        except IndexError:
            return None

    def insert(self, args=[]):
        # args.insert(0, 'NULL')
        self.__queryString = 'insert into ' + self.dbname + ' values(NULL,' + ','.join(['%s' for i in args]) + ');'
        self.__args = args
        return self.getWithoutTransform()

    def delete(self):
        self.__queryString = 'delete from ' + self.dbname
        return self

    def update(self, args={}):
        self.__queryString = 'update ' + self.dbname + ' set ' + ','.join([str(key) + '=%s' for key in args]) + 'where id=%s'
        self.__args = list(args.values())
        self.__args.append(args['id'])
        return self.getWithoutTransform()

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
            return 'DATETIME'
        elif value == "<class 'str'>":
            return 'VARCHAR(400)'
        else:
            return 'TEXT'

    @staticmethod
    def createTable(name: str, d: TypedDict):
        attrList = []
        for key, value in d.items():
            if key == 'id':
                attrList.append('id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')
            else:
                attrList.append(key + ' ' + QueryBuilder.__convertValueToSQLType(str(value)))
        query = 'create table ' + name + '(' + ','.join(attrList) + ')'
        cursor = getConnection().getCursor()
        cursor.execute(query)

    @staticmethod
    def deleteTable(name: str):
        query = 'drop table ' + name
        cursor = getConnection().getCursor()
        cursor.execute(query)
