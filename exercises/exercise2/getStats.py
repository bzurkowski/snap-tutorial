import sys
import snap

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: %s <file> <column1> <column2>" % (sys.argv[0])
        sys.exit(1)
