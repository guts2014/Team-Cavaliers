#!/usr/bin/env python

import BaseHTTPServer
import sys
import os

data_dir = sys.argv[1]
classes_dir = os.path.join(data_dir, "classes")

class Responder(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("/")[1:]
        cmd = path[0]
        class_name = path[1]
        if cmd == "create":
            os.makedirs(os.path.join(classes_dir, class_name))

        if cmd == "register":
            person = path[2]
            with open(os.path.join(classes_dir, class_name, person), "w") as _:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("<html><body>%s is here</body></html>" % person)

        elif cmd == "list":
            here = os.listdir(os.path.join(classes_dir)data_dir)
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
