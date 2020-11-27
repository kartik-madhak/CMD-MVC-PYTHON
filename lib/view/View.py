import string
from definitions import ROOT_DIR


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
            return '\n'.join([self.format(template, **{it: val}, i=i+1) for i, val in zip(range(0, len(value)), value)])
        else:
            return super(SuperFormatter, self).format_field(value, spec)


class View:
    def __init__(self, path: str, objects, extDict={}):
        self.path = path
        self.qualifiedPathName = ROOT_DIR + '\\Views\\' + path + '.txt'
        self.inputs = {}
        self.objects = objects
        with open(self.qualifiedPathName, 'r') as file:
            self.header = extDict
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

    def ObjectMappingLayer(self, objects = None):
        sf = SuperFormatter()
        self.__content = sf.format(self.__content, **objects)

    def langParser(self):
        inputDict = {}
        skipIf = False
        for line in self.__content.split('\n'):

            if ';;if' in line:
                skipIf = True
                split_line = line.lstrip(';;if ').split('and')
                ans = True
                for ll in split_line:
                    tmp = ll.split()
                    if "'" not in tmp[0]:
                        first = inputDict[tmp[0]]
                    else:
                        first = tmp[0].strip("'")

                    if "'" not in tmp[2]:
                        second = inputDict[tmp[2]]
                    else:
                        second = tmp[2].strip("'")

                    if first != second:
                        ans = False
                        break
                if ans:
                    skipIf = False
            elif ';;default' in line:
                skipIf = False

            if skipIf:
                continue

            if ';;inputL' in line:
                pre, trash, post = line.partition(';;inputL')
                print(pre, end='')
                post = post.strip()
                inputDict[post] = ''
                while True:
                    tmp = input()
                    if tmp == 'e':
                        break
                    inputDict[post] += '\n' + tmp
            elif ';;input' in line:
                pre, trash, post = line.partition(';;input')
                print(pre, end='')
                post = post.strip()
                inputDict[post] = input()
            elif ';;redirect' in line:
                tmp = line.lstrip(';;redirect ').strip()
                if "'" in tmp:
                    inputDict['form_redirect'] = tmp.strip("'")
                elif tmp in inputDict:
                    inputDict['form_redirect'] = inputDict[tmp]
                break
            elif ';;push' in line:
                post = line.partition(';;push')[2]
                if '[' in post:
                    try:
                        arr_name = post.split('[')[0].strip()
                        index_name = post.split('[')[1].split(']')[0]
                        var = self.objects[arr_name][int(inputDict[index_name]) - 1]
                        attr = post.split('.')[1]
                        post = getattr(var, attr)
                    except:
                        post = '0'
                if 'ext' not in inputDict:
                    inputDict['ext'] = []
                inputDict['ext'].append(int(post))
            elif ';;exit' == line or ';;exit' in line:
                return -1
            elif ';;refresh' == line or ';;refresh' in line:
                return 1
            else:
                if line != '' and ';;if' not in line and ';;default' not in line:
                    if line == '\\':
                        print()
                    else:
                        print(line)

        self.header['inputs'] = {}

        for i in inputDict:
            if i == 'form_redirect':
                self.header[i] = inputDict[i]
            elif i != 'choice':
                self.header['inputs'][i] = inputDict[i]

        return 0

    def render(self):
        returnVal = self.langParser()
        if returnVal == 1:
            self.render()
        return returnVal

    def parse(self, objects):
        self.ObjectMappingLayer(objects)
        return self.__content
