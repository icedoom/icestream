
from icestream.builder import build

if __name__ == '__main__':
    import sys

    #if len(sys.argv) != 2:
     #   print "usage: icelex filename"
     #   sys.exit(1)

    ret = build("test/test.ice")
    print "parse done"
    print dir(ret)
