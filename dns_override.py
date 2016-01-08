import socks
import socket

# Override create_connection in socks to override the use of default DNS settings for system
# allowing use of tor's internal DNS for the dirty dirty deep web
tor_server = '127.0.0.1'
tor_port = 9050

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, tor_server, tor_port)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection