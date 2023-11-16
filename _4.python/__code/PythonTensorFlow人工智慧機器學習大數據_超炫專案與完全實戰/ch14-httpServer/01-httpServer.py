# -*- coding: UTF-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import sys

if (sys.version_info > (3, 0)):    # python 3.x
    import socketserver as socketserver
    import http.server
    from http.server import SimpleHTTPRequestHandler as RequestHandler
else:                              # python 2.x
    import SocketServer as socketserver
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler as RequestHandler

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

print('Server listening on port %s' % port)

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', port), RequestHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise