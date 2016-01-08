import found_domains
import dns_override
import onion_gen
import urllib2
import time
import sys

good = 'http://lpwiqq7bjenhkucm.onion/'
bad = 'http://lpwiqq7bjenhk111.onion/'

def hit_url(url):
    try:
        response = urllib2.urlopen(url)
        html = response.read()

        # Save live url to db
        found_domains.save_domain(url)

        print '{0} Is Live!'.format(url)
    except:
        print '{0} Is Not Live'.format(url)

def main():
    try:
        found_domains.create_table()
    except:
        print 'Table Found'
    while True:
        hit_url(onion_gen.generate_url())

if __name__ == '__main__':
    main()