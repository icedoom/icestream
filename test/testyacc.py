import sys
sys.path.insert(0, '../')

from icestream.iceyacc import parse

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print "usage: icelex filename"
        sys.exit(1)

    ret = parse(sys.argv[1])
    print "parse done"
    print ret
