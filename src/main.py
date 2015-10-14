from repository.xml import Shortcut
import posix


class Main(object):
    @staticmethod
    def add_shortcut(keyword, path):
        shortcut = Shortcut(keyword, path)
        shortcut.save()

    @staticmethod
    def goto(keyword):
        shortcut = Shortcut.find_by_keyword(keyword)
        if shortcut:
            posix.chdir(shortcut.path)
        else:
            raise Exception('Keyword not found!')

    @staticmethod
    def delete_shortcut(keyword):
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