import csv

class Shortcut:
    def __init__(self, _keyword, _path):
        self.keyword = _keyword
        self.path = _path

    @staticmethod
    def all():
        pass

    @staticmethod
    def find_by_keyword(keyword):
        pass

    def save(self):
        if self.__isExists():
            raise 'Keyword already exists'
        else:
            with open('test.csv', 'a') as csvfile:
                csvfile.write('(0),(1)'.format(self.keyword, self.path))
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

