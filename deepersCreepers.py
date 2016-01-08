import found_domains
import dns_override
import onion_gen
import urllib2
import time
import sys

VERBOSE = False

def hit_url(url):
    global VERBOSE

    try:
        response = urllib2.urlopen(url)
        html = response.read()

        # Save live url to db
        found_domains.save_domain(url)

        print '{0} Is Live!'.format(url)
    except:
        if VERBOSE:
            print '{0} Is Not Live'.format(url)

def main():
    global VERBOSE

    for arg in sys.argv:
        if arg.lower() == '-v':
            VERBOSE = True
    try:
        found_domains.create_table()
    except:
        if VERBOSE:
            print 'Table Found'
    while True:
        hit_url(onion_gen.generate_url())

if __name__ == '__main__':
    main()