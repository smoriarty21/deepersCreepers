import config
from pygoogle import pygoogle
from py_bing_search import PyBingSearch

def search_bing():
    url_list = []

    # Bing Search
    bing = PyBingSearch(config.get_bing_api_key())
    result_list, next_uri = bing.search('.onion link', limit=5, format='json')

    for result in result_list:
        url_list.append(result.url)

    return url_list

# Fuck googles abuse system
def search_google():
    google = pygoogle('".onion"')
    google.pages = 8
    urls = google.get_urls()
    url_list = []
    master_list = {}
    count = 0

    for url in urls:
        url_list.append(url)

    return url_list