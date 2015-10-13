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
        with open('test.csv', 'rb') as csvfile:
            csv.reader(csvfile)


    def delete(self):
        pass