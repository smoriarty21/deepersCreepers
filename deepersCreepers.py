
from utils import spider
from utils import database
from utils import dns_override
from utils import url_scraper
from utils import onion_gen
import urllib2
import time
import sys

VERBOSE = False
BRUTEFORCE = False
SCRAPE = False

# TODO: How high was I for this one? Move this shit
def hit_url(url):
    global VERBOSE

    try:
        response = urllib2.urlopen(url)
        html = response.read()
        print html

        # Save live url to db
        database.save_domain(url)

        print '{0} Is Live!'.format(url)
    except:
        if VERBOSE:
            print '{0} Is Not Live'.format(url)

def main():
    global SCRAPE
    global VERBOSE
    global BRUTEFORCE

    for arg in sys.argv:
        if arg.lower() == '-v':
            VERBOSE = True
        elif arg.lower() == '-b':
            BRUTEFORCE = True
        elif arg.lower() == '-s':
            SCRAPE = True
    try:
        database.initialize()
    except:
        if VERBOSE:
            print 'Table Found'
    if BRUTEFORCE:
        while True:
            hit_url(onion_gen.generate_url())

        # DEBUGGING
        #hit_url('http://sigaintz7qjj3val.onion/')
    elif SCRAPE:
        #url_scraper.search_google()
        spider.start_crawl('bing')



if __name__ == '__main__':
    main()