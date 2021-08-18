#!/usr/bin/python3

import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    root_response = ""
    def do_GET(self):
        if self.path == "/":
            Page = "'{\"response\"}:{\"This is a start page\"}'".encode()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(Page)))
            self.end_headers()
            self.wfile.write(Page)
        elif self.path == '/api':
            response = '''
Welcome to our demo API, here are the details of your request:
Headers: 
  {headers}
Method: {method}
'''.format(headers=self.headers.as_string(), method=self.command).encode()
            print(self.headers)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()