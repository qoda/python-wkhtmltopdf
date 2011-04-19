#!/usr/bin/env python

import optparse
import os
import urlparse

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from main import WKhtmlToPdf

class RequestHandler(BaseHTTPRequestHandler):
    """
    Simple request class to serve json response back to ajax application.
    """
    def handle_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
    def handle_404(self, message):
        self.handle_headers(404)
        self.wfile.write('{"error": "%s"}"' % message)
    
    def handle_200(self, message):
        self.handle_headers(200)
        self.wfile.write('{"success": "%s"}"' % message)
    
    def do_GET(self):
        # get the query string variables
        self.urlparser = urlparse.urlparse(self.path)
        self.query_string = self.urlparser.query
        self.query_dict = urlparse.parse_qs(self.query_string)
        
        # get the url and output_file
        self.url = self.query_dict.get('url', None)
        self.output_file = self.query_dict.get('output_file', None)
        
        if not self.url or not self.output_file:
            self.handle_404("url and output_file params are required")
            return None
        
        wkhtp = WKhtmlToPdf(self.url, self.output_file)
        print wkhtp.render()
        
        # send json response
        self.handle_200("file created successfully")
        
        return None

if __name__ == '__main__':
    
    # parse through the system argumants
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", dest="host", default="localhost", help="server host name")
    parser.add_option("-p", "--port", dest="port", default=8888, help="port to run the api on")
    options, args = parser.parse_args()
    
    # start the server
    server = HTTPServer((options.host, options.port), RequestHandler)
    print 'Starting server (http://%s:%s), use <Ctrl-C> to stop' % (options.host, options.port)
    server.serve_forever()
