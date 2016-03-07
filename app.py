import sys
import getopt

from src.main import Main


def main(argv):
    __keyword, __path = '', ''
    try:
        opts, args = getopt.getopt(argv, 'a:p:', ['list'])
    except getopt.GetoptError:
        raise Exception('Something went wrong')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            __keyword = arg
        elif opt == '-p':
            __path = arg
        elif opt == '--list':
            Main.list()
    if '-a' in sys.argv[1:]:
        Main.add_shortcut(__keyword, __path)
        print('{0} is added with a pass {1}'.format(__keyword, __path))


def execute(__keyword):
    Main.goto(__keyword)


if __name__ == '__main__':
    args_len = len(sys.argv)
    if args_len == 2 and '--list' not in sys.argv:
        execute(sys.argv[1])
    else:
        main(sys.argv[1:])
