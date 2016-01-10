# Reset DNS Override
import socks
import config
import socket

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(None)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection

from pygoogle import pygoogle
import spyder

def search_google():
    google = pygoogle('".onion"')
    google.pages = 12
    urls = google.get_urls()

    for url in urls:
        print url