import string
from definitions import ROOT_DIR
from typing import TypedDict
import json


class SuperFormatter(string.Formatter):
    def __init__(self, default=''):
        self.default = default

    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            return kwds.get(key, self.default.format(key))
        else:
            return string.Formatter.get_value(key, args, kwds)

    def format_field(self, value, spec):
        if spec == 'call':
            return value()
        if spec.startswith('repeat'):
            splitArr = spec.partition(':')
            it = splitArr[0].split()[2]
            template = splitArr[-1]
            return '\n'.join([template.format(**{it: i}) for i in value])
        else:
            return super(SuperFormatter, self).format_field(value, spec)


class View:
    path: str
    qualifiedPathName: str

    def __init__(self, path: str, objects: TypedDict):
        self.path = path
        self.qualifiedPathName = ROOT_DIR + '\\Views\\' + path.replace('/', '.') + '.txt'
        self.inputs = {}
        with open(self.qualifiedPathName, 'r') as file:
            self.header = json.loads(str(next(file)).lstrip("#"))
            self.__content = file.read()
            self.compile()
            self.parse(objects)

    def compile(self):
        openBrackets = 0
        lineCount = 1
        for line in self.__content.split('\n'):
            openBrackets += line.count('{') - line.count('}')
            if ';;Input' in line:
                res = line.partition(';;Input:')[2]
                if res == '':
                    raise Exception('Error compiling view, Input name not given in line at ' + self.qualifiedPathName
                                    + ':' + str(lineCount))
            lineCount += 1
        if openBrackets != 0:
            raise Exception('Error compiling view, Bracket mismatch at ' + self.qualifiedPathName
                            + ':' + str(lineCount))

    def ObjectMappingLayer(self, objects: TypedDict = None):
        sf = SuperFormatter()
        self.__content = sf.format(self.__content, **objects)

    def render(self):
        for line in self.__content.split('\n'):
            if ';;Input:' in line:
                parts = line.partition(';;Input:')
                if parts[0] != ';;Input:':
                    print(parts[0], end='')
                self.inputs[parts[2].strip()] = input()
            elif ';;pause' in line:
                input()
            else:
                print(line)
        self.header['inputs'] = self.inputs

    def parse(self, objects: TypedDict):
        self.ObjectMappingLayer(objects)
        return self.__content
