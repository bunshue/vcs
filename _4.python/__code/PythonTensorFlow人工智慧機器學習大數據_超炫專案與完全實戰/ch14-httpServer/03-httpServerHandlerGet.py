# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import time



if (sys.version_info > (3, 0)):    # python 3.x
    import socketserver as socketserver
    import http.server
    from http.server import SimpleHTTPRequestHandler as RequestHandler
    from urllib.parse import urlparse
else:   # python 2.x
    import SocketServer as socketserver
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler as RequestHandler

    from urlparse import urlparse

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        name =b" "
        password =b" "
        if query!="":
           query_components = dict(qc.split("=") for qc in query.split("&"))
           name = query_components["name"]
           password = query_components["password"]
        self.do_HEAD()
        print(self.wfile)
        output = b""
        #output += b"<html><body>Hello name="+b(name) + b" password="+b(password) +b"</body></html>"
        output += b"<html><body>Hello name="
        try:
            output +=name
        except:
            output +=name.encode('utf-8')
        output += b" password="
        try:
            output +=password
        except:
            output +=password.encode('utf-8')
        output += b"</body></html>"
        self.wfile.write(output)
        #self.wfile.close()

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
#httpd = socketserver.TCPServer(('127.0.0.1', port), MyHandler)
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise
