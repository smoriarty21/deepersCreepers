import re
import Queue
import requests
import database
import threading
import url_scraper

import dns_override

# Queue for onion urls
url_queue = Queue.Queue()

threads = []

def onion_searcher():
    while not url_queue.empty():
        url = url_queue.get()

        try:
            urls = get_url_source('http://{0}/'.format(url))

            for url in urls:
                print 'url'
                print url
                # Add to DB of lIve URLs
                database.save_domain(url)
                #url_queue.put(url)
                # if database.check_domain_in_db(url):
                #     print 'adding to db'
                #     database.save_domain(url)

                #     url_queue.put(url)
        except:
            print 'No good and shit'

def get_url_source(url):
    try:
        source = requests.get(url).text
        urls = parse_source_for_onions(source)
        return urls
    except:
        print 'Error pulling HTML'

def parse_source_for_onions(source):
    regex = '[a-z2-7]{16}.onion'
    url_list = []

    for match in re.finditer(regex, source):
        url_list.append(source[match.span()[0]:match.span()[1]])

    return url_list

def start_crawl(search_type):
    # Pull Non Onion URLs
    urls = []

    if search_type is 'google':
        urls = url_scraper.search_google()
    elif search_type is 'bing':
        urls = url_scraper.search_bing()

    for url in urls:
        print url
        source = get_url_source(url)

        try:
            for onion in source:
                url_queue.put(onion)
        except:
            print 'Error somewhere and shit'


    t = threading.Thread(target=onion_searcher)
    threads.append(t)
    t.start()
