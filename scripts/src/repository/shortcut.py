import csv


class Shortcut:
    def __init__(self, _keyword, _path, _existing=False):
        self.keyword = _keyword
        self.path = _path
        self.existing = _existing

    @staticmethod
    def all():
        with open('test.csv', 'rb') as csvfile:
            return csv.reader(csvfile)

    @staticmethod
    def find_by_keyword(__keyword):
        with open('test.csv', 'rb') as csvfile:
            data = csv.reader(csvfile)
            for keyword, path in data:
                if keyword == __keyword:
                    return Shortcut(keyword, path, True)

    def save(self):
        if self.__isExists():
            raise Exception('Keyword already exists')
        elif self.existing:
            raise Exception('Cant rewrite the keyword')
        else:
            with open('test.csv', 'a') as csvfile:
                csvfile.write('{0},{1}\n'.format(self.keyword, self.path))
                return True

    def delete(self):
        pass

    def __isExists(self):
        __result = False
        with open('test.csv', 'rb') as csvfile:
            data = csv.reader(csvfile)
            for obj in data:
                if obj[0] == self.keyword:
                    __result = True
                    return __result
        return __result
