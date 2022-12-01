#!/usr/bin/env python3
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi

#print('source code for "http.server":', http.server.__file__)

class web_server(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		
	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        
		# refuse to receive non-json content
		if ctype != 'application/json':
			self.send_response(400)
			self.end_headers()
			return
		length = int(self.headers.getheader('content-length'))
		message = json.loads(self.rfile.read(length))
		self._set_headers()
		self.wfile.write(json.dumps(message))
		
def run(server_class=HTTPServer, handler_class=Server, port=4080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

run()

