# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import time

from sys import version as python_version
from cgi import parse_header, parse_multipart

if (sys.version_info > (3, 0)):    # python 3.x
    import socketserver as socketserver
    import http.server
    from http.server import SimpleHTTPRequestHandler as RequestHandler
    #from urllib.parse import urlparse
    from urllib.parse import parse_qs
    #from http.server import BaseHTTPRequestHandler


else:   # python 2.x
    import SocketServer as socketserver
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler as RequestHandler
    #from urlparse import urlparse
    from urlparse import parse_qs

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        varLen = int(self.headers['Content-Length'])
        name =b" "
        password =b" "
        if varLen>0:
           query_components = parse_qs(self.rfile.read(varLen), keep_blank_values=1)
           print(query_components)
           name = query_components[b"name"][0]
           password = query_components[b"password"][0]
        self.do_HEAD()
        print(self.wfile)
        output = b""
        output += b"<html><body>Hello name="
        output +=name
        output += b" password="
        output +=password
        output += b"</body></html>"
        self.wfile.write(output)
        #self.wfile.close()

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)

try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise
