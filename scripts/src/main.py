from os import execl
from repository.shortcut import Shortcut
import posix
from subprocess import call

class Main(object):

    @staticmethod
    def execute(param, keyword, path):
        val = param.value
        if val == 'add':
            Main.add(keyword, path)
            return True
        elif val == 'find':
            return Main.find(keyword)
        elif val == 'delete':
            Main.delete(keyword)
            return True

    @staticmethod
    def add(keyword, path):
        shortcut = Shortcut(keyword, path)
        shortcut.save()

    @staticmethod
    def find(keyword):
        shortcut = Shortcut.find_by_keyword(keyword)
        if shortcut:
            return shortcut.path
        else:
            raise Exception('Keyword not found!')

    @staticmethod
    def delete(keyword):
        shortcut = Shortcut.find_by_keyword(keyword)
        if shortcut:
            shortcut.delete()
        else:
            raise Exception('Keyword not found!')

    @staticmethod
    def list():
        shortcuts = Shortcut.all()
        for keyword, path in shortcuts:
            print("Keyword: {0}, Path: {1}".format(keyword, path))
