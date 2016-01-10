import socks
import config
import socket

# Override create_connection in socks to override the use of default DNS settings for system
# allowing use of tor's internal DNS for the dirty dirty deep web
tor_server = str(config.get_tor_ip())
tor_port = int(config.get_tor_port())

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, tor_server, tor_port)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection