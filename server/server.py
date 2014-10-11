#!/usr/bin/env python
#
# to list all classes:
#    /classes
#
# to create a class:
#    /create/<classname>
#
# to list all the students registered for a class:
#    /list/<classname>
#
# to register for a class:
#    /register/<classname>/<person>
#
# to clear a class list:
#    /clear/<classname>

import argparse
import BaseHTTPServer
import sys
import os
import os.path


def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)

parser = argparse.ArgumentParser(description="Run the Here I Am server")
parser.add_argument("dataDir")
main_args = parser.parse_args()

data_dir = main_args.dataDir

mkdir_p(data_dir)
classes_dir = os.path.join(data_dir, "classes")
mkdir_p(classes_dir)


class Responder(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("/")[1:]

        if path:
            cmd = path[0]
            args = path[1:]

            if cmd == "classes":
                self.list_classes()
            elif cmd == "create":
                self.create_class(args)
            elif cmd == "list":
                self.list_class_members(args)
            elif cmd == "register":
                self.register_for_class(args)
            # elif cmd == "clear":
            #     self.clear_class(args)
            else:
                self.report_error()
        else:
            self.report_error()

    def list_classes(self):
        self.send_list(map(lambda c: "<a href=\"/list/%s\">%s</a>" % (c, c), os.listdir(classes_dir)), "All classes")

    def create_class(self, args):
        if len(args) >= 1:
            class_name = args[0]
            mkdir_p(os.path.join(classes_dir, class_name))
            self.report_success("Created class '%s'" % class_name)
        else:
            self.report_error()

    def list_class_members(self, args):
        if len(args) >= 1:
            class_name = args[0]
            self.send_list(os.listdir(os.path.join(classes_dir, class_name)),
                           "Present in %s" % class_name,
                           "<p><a href=\"clear/%s\">Clear class</a></p>" % class_name)
        else:
            self.report_error()

    def register_for_class(self, args):
        if len(args) >= 2:
            class_name = args[0]
            person = args[1]
            with open(os.path.join(classes_dir, class_name, person), "w") as _:
                self.report_success("%s is here" % person)
        else:
            self.report_error()

    # def clear_class(self, args):
    #     if len(args) >= 2:
    #         class_name = args[0]
    #         # delete all names under class
    #     else:
    #         self.report_error()

    def send_list(self, l, title, footer=""):
        s = "<html><head><title>%s</title></head><body><h1>%s</h1><ul>" % (title, title)

        for item in l:
            s += "<li>%s</li>" % item

        s += "</ul>%s</body></html>" % footer
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(s)

    def report_success(self, s):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Success</title></head><body>%s</body></html>" % s)

    def report_error(self):
        msg = "Invalid request: %s" % self.path
        print msg
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Invalid request</title></head><body><p>%s</p></body></html>" % msg)


server_address = ('', 80)
httpd = BaseHTTPServer.HTTPServer(server_address, Responder)
httpd.serve_forever()
