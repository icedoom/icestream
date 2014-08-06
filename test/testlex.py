import sys
sys.path.insert(0, '../')
from icestream.icelex import IceLexer

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print "usage: icelex filename"
        sys.exit(1)

    lexer = IceLexer()
    lexer.input(open(sys.argv[1]).read())

    tok = 1
    while tok:
        tok = lexer.token()
        print tok

