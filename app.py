from src.main import Main
import sys, getopt


def main(argv):
    __keyword, __path = '', ''
    try:
        opts, args = getopt.getopt(argv, 'a:p:', [])
    except getopt.GetoptError:
        raise Exception('Keyword already exists')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            __keyword = arg
        elif opt == '-p':
            __path = arg
    Main.add_shortcut(__keyword, __path)
    print('{0} is added with a pass {1}'.format(__keyword, __path))
if __name__ == '__main__':
    main(sys.argv[1:])


