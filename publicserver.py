#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','application/json')
        self.end_headers()
 
        # Send message back to client
        if(self.path == '/'):
          f = open("ethgasAPI.json", "r")
          msg = f.read()
          self.wfile.write(bytes(msg, "utf8"))
        elif(self.path == '/health'):
          f = open("errors.json", "r")
          msg = f.read()
          self.wfile.write(bytes(msg, "utf8"))
        else:
          self.wfile.write(bytes("{'error': 'API doesnot exist'}", "utf8"))
        return
 
def run():
  print('starting server... on http://localhost:8081')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()