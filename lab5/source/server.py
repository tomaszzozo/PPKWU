#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import json

#print('source code for "http.server":', http.server.__file__)

class web_server(BaseHTTPRequestHandler):
	def _set_headers(self):
        	self.send_response(HTTPStatus.OK.value)
        	self.send_header('Content-type', 'application/json')
        	# Allow requests from any origin, so CORS policies don't
        	# prevent local development.
        	self.send_header('Access-Control-Allow-Origin', '*')
        	self.end_headers()
		
	def do_POST(self):
		length = int(self.headers.get('content-length'))
		message = json.loads(self.rfile.read(length))
		self._set_headers()
		self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
		
def run_server():
    server_address = ('', 4080)
    httpd = HTTPServer(server_address, _RequestHandler)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()

run_server()

