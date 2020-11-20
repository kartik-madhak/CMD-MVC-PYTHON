from __future__ import annotations

from abc import ABC
from typing import List, Type, TypeVar

from lib.database.QueryBuilder import QueryBuilder

T = TypeVar('T', bound='Model')


class Model(ABC):
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
