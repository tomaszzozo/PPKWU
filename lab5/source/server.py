#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
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
		
		
# --- main ---

PORT = 4080

print(f'Starting: c{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
