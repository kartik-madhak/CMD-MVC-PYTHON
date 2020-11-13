import string

from definitions import ROOT_DIR
from typing import TypedDict


class SuperFormatter(string.Formatter):
    def format_field(self, value, spec):
        if spec == 'call':
            return value()
        if spec == '':
            template = spec.partition(':')[-1]
            return '\n'.join([template.format(**i) for i in value])
        else:
            return super(SuperFormatter, self).format_field(value, spec)


class View:
    def __init__(self, path: str = ''):
        self.path = path
        with open(ROOT_DIR + '\\Views\\' + path.replace('/', '.') + '.txt', 'r') as file:
            self.__content = file.read()

    def ObjectMappingLayer(self, objects):
        sf = SuperFormatter()
        # noinspection PyArgumentList
        return sf.format(self.__content, **objects)

    def parse(self, objects):
        # noinspection PyTypeChecker
        return self.ObjectMappingLayer(objects)
