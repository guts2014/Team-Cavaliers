#!/usr/bin/env python

import BaseHTTPServer
import sys
import os

data_dir = sys.argv[1]

class Responder(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("/")
        print str(path)
        if path[1] == "here":
            with open(os.path.join(data_dir, path[2]), "w") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("<html><body>%s is here</body></html>" % path[2])

        elif path[1] == "check":
            here = os.listdir(data_dir)
            s = "<html><body>"

            for h in here:
                s += "<p>%s</p>" % h

            s += "</body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(s)

        else:
            print "Invalid request"

server_address = ('', 8080)
httpd = BaseHTTPServer.HTTPServer(server_address, Responder)
httpd.serve_forever()
