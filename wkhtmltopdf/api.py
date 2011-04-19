#!/usr/bin/env python

import optparse
import os
import time
import urlparse

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from main import WKhtmlToPdf

HOST = 'localhost'
PORT = 8888

class RequestHandler(BaseHTTPRequestHandler):
    """
    Simple request class to serve json response back to ajax application.
    """
    def handle_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', host)
        self.end_headers()
        
    def handle_404(self, message):
        self.handle_headers(404)
        self.wfile.write('{"error": "%s"}"' % message)
        self.end_headers()
        
    def handle_500(self, message):
        self.handle_headers(500)
        self.wfile.write('{"error": "%s"}"' % message)
    
    def handle_200(self, message, file_path):
        self.handle_headers(200)
        self.wfile.write('{"success": "%s", "file_path": %s}"' % (message, file_path))
    
    def do_GET(self):
        # get the query string variables
        self.urlparser = urlparse.urlparse(self.path)
        self.query_string = self.urlparser.query
        self.query_dict = urlparse.parse_qs(self.query_string)
        
        # get the url and output_file
        self.url = self.query_dict.get('url', [None, ])[0]
        self.output_file = self.query_dict.get('output_file', [None, ])[0]
        
        if not self.url or not self.output_file:
            self.handle_404("url and output_file params are required")
            return None
        
        wkhtp = WKhtmlToPdf(self.url, self.output_file)
        output_file = wkhtp.render()
        
        # send json response
        if output_file[0]:
            self.handle_200("the file has been saved", output_file[1])
        else:
            self.handle_500("%s - the file could not be created" % output_file[1])
        return None

if __name__ == '__main__':
    
    # parse through the system argumants
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", dest="host", default="localhost", help="server host name")
    parser.add_option("-p", "--port", dest="port", default=8888, help="port to run the api on")
    options, args = parser.parse_args()
    
    # set host and port
    host = options.host
    port = int(options.port)
    
    # handle the server
    server = HTTPServer((host, port), RequestHandler)
    try:
        print time.asctime(), 'Starting server (http://%s:%s), use <Ctrl-C> to stop' % (host, port) 
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print time.asctime(), 'Stopping server (http://%s:%s)' % (host, port)
