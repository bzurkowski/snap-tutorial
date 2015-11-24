import sys
import snap
from getArticles import getArticlesLookup

if __name__ == '__main__':

    if len(sys.argv) < 5:
        print "Usage: %s <articles> <graph> <source> <target>" % (sys.argv[0])
        sys.exit(1)

    articles = getArticlesLookup(sys.argv[1])

    # articles[title] => node_id
    # articles.GetKey(node_id) => title
