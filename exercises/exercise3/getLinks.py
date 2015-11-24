import os
import snap
import sys
import csv
from getArticles import getArticlesLookup

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print "Usage: %s <articles> <links> <output>" % (sys.argv[0])
        sys.exit(1)

    articles = getArticlesLookup(sys.argv[1])

    # for k in articles:
    #     print k, articles[k]

    # map links to article ids

    fin = open(sys.argv[2])
    out = open(sys.argv[3], 'w')

    tsv = csv.reader(fin, delimiter='\t')

    for row in tsv:
        if len(row) < 2:
            continue

        id1 = articles[row[0]]
        id2 = articles[row[1]]

        if not id1 and id2:
            continue

        edge = [str(id1), str(id2)]

        out.write('\t'.join(edge) + '\n')

    out.close()
