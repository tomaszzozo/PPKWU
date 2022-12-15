#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import xmltodict
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
		message = xmltodict.parse(self.rfile.read(length))
		
		result = {}
		if "root" in message:
			message = xmltodict.parse(["root"])
		if "str" in message:
			string = message["str"]
			lowercase = sum(1 for c in string if c.islower())
			uppercase = sum(1 for c in string if c.isupper())
			digits = sum(list(map(lambda x:1 if x.isdigit() else 0,set(string))))
			special = len(string)-lowercase-uppercase-digits
			result["lowercase"] = lowercase
			result["uppercase"] = uppercase
			result["digits"] = digits
			result["special"] = special
		if "num1" in message and "num2" in message:
			num1 = message["num1"]
			num2 = message["num2"]
			result["sum"] = num1+num2
			result["sub"] = num1-num2
			result["mul"] = num1*num2
			result["div"] = num1//num2
			result["mod"] = num1%num2
		
		self._set_headers()
		self.wfile.write(json.dumps(result).encode('utf-8'))
		
def run_server():
    server_address = ('', 4080)
    httpd = HTTPServer(server_address, web_server)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()

run_server()

