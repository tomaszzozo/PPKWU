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
		
		result = {}
		
		if "str" in message:
			string = message["str"]
			result['lowercase'] = sum(1 for c in string if c.islower())
			result['uppercase'] = sum(1 for c in string if c.isupper())
			result['digits'] = sum(list(map(lambda x:1 if x.isdigit() else 0,set(string))))
			result['special'] = len(string)-lowercase-uppercase-digits
		
		self._set_headers()
		self.wfile.write(json.dumps(result).encode('utf-8'))
		
def run_server():
    server_address = ('', 4080)
    httpd = HTTPServer(server_address, web_server)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()

run_server()

