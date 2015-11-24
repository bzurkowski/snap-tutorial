#
#   join two files on a common value
#
#   First, read values from a column in the first file. Next, read
#   the second file and and print out lines where a column value
#   matches a value from the first file.
#

import os
import snap
import sys

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print "Usage: %s <file1> <file2> <column1> <column2> <output_filename>" % (sys.argv[0])
        sys.exit(1)

    fname1 = sys.argv[1]
    fname2 = sys.argv[2]
    col1 = int(sys.argv[3]) - 1
    col2 = int(sys.argv[4]) - 1
    output_name = sys.argv[5]


    # read the first file and create the hash table
    f1 = open(fname1)
    h = snap.TStrStrH()

    for line in f1:
        cline = line.split("\n")[0]
        #print str(cline)

        words = cline.split("\t")
        #print len(words), str(words)

        # skip lines with not enough columns
        if len(words) <= col1:
            continue

        key = words[col1]
        h[key] = cline

    f1.close()

    #print len(h)

    # read the second file and print out matching lines
    f2 = open(fname2)
    f = open(output_name, 'w')

    for line in f2:
        cline = line.split("\n")[0]
        #print str(cline)

        words = cline.split("\t")
        #print len(words), str(words)

        # skip lines with not enough columns
        if len(words) <= col2:
            continue

        key = words[col2]
        #print key, cline

        if not h.IsKey(key):
            continue

        line = []
        line.append(cline)
        line.append(h[key])
        f.write("\t".join(line)+"\n")
        #print "\t".join(line)

    f2.close()

