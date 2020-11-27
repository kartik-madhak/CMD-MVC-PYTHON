from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import List, Type, TypeVar

from lib.database.QueryBuilder import QueryBuilder

T = TypeVar('T', bound='Model')


class Model(ABC):
    id: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def getVarDict(cls):
        res = {'id': 'int'}
        for key, value in vars(cls)['__annotations__'].items():
            res[key] = value
        res['created_at'] = 'datetime'
        res['updated_at'] = 'datetime'
        return res

    @classmethod
    def getInstance(cls, objDict={}):
        """
        Converts dictionary to Model instance
        :param objDict:
        :return:
        """
        obj = cls.__new__(cls)
        for key, value in objDict.items():
            obj.__setattr__(key, value)
        return obj

    @classmethod
    def query(cls: Type[T], className: str = None):
        classNames = className if className is not None else cls.__name__ + 's'
        return QueryBuilder(classNames, cls)

    @classmethod
    def transform(cls: Type[T], inputList):
        res: List[Type[T]] = []
        for obj in inputList:
            res.append(cls.getInstance(obj))
        return res

    def save(self):
        args = self.__dict__
        if 'updated_at' in args:
            args['updated_at'] = datetime.today()
        QueryBuilder(self.__class__.__name__ + 's').update(args)

    def delete(self):
        QueryBuilder(self.__class__.__name__ + 's').delete().where('id', self.id).getWithoutTransform()