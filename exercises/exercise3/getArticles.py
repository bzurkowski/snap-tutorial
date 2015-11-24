import snap
import csv

def getArticlesLookup(filePath):
    fin = open(filePath)
    tsv = csv.reader(fin, delimiter='\t')

    h = snap.TStrIntH()
    id = 0

    for row in tsv:
        if len(row) < 1:
            continue

        key = row[0]

        if h.IsKey(key):
            continue

        h[row[0]] = id
        id += 1

    fin.close()

    return h
