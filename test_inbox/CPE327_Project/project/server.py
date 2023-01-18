
import socketserver
import sys
import socket # For gethostbyaddr()

from SimpleHTTPRequestHandler import SimpleHTTPRequestHandler

class HTTPServer(socketserver.TCPServer):

    allow_reuse_address = 1    # Seems to make sense in testing environment

    def server_bind(self):
        """Override server_bind to store the server name."""
        socketserver.TCPServer.server_bind(self)
        host, port = self.server_address[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    daemon_threads = True

def _get_best_family(*address):
    infos = socket.getaddrinfo(
        *address,
        type=socket.SOCK_STREAM,
        flags=socket.AI_PASSIVE,
    )
    family, type, proto, canonname, sockaddr = next(iter(infos))
    return family, sockaddr

if __name__ == '__main__':

    PORT = 8888
    bind=None
    protocol="HTTP/1.0"
    ThreadingHTTPServer.address_family, addr = _get_best_family(bind, PORT)

    with ThreadingHTTPServer(addr, SimpleHTTPRequestHandler) as httpd:
        print ("serving at port :", format(PORT))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)