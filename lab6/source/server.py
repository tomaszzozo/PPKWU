#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import xmltodict
from dict2xml import dict2xml

#print('source code for "http.server":', http.server.__file__)

class web_server(BaseHTTPRequestHandler):
	def _set_headers(self):
        	self.send_response(HTTPStatus.OK.value)
        	self.send_header('Content-type', 'application/xml')
        	# Allow requests from any origin, so CORS policies don't
        	# prevent local development.
        	self.send_header('Access-Control-Allow-Origin', '*')
        	self.end_headers()
		
	def do_POST(self):
		length = int(self.headers.get('content-length'))
		message = xmltodict.parse(self.rfile.read(length))
		
		result = {}
		if "root" in message:
			message = message["root"]
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
			num1 = int(message["num1"])
			num2 = int(message["num2"])
			result["sum"] = num1+num2
			result["sub"] = num1-num2
			result["mul"] = num1*num2
			result["div"] = num1//num2
			result["mod"] = num1%num2
		
		data = {}
		data["root"] = result
		self._set_headers()
		self.wfile.write(('<?xml version="1.0" encoding="UTF-8" ?>\n' + dict2xml(data)).encode('utf-8'))
		
def run_server():
    server_address = ('', 4080)
    httpd = HTTPServer(server_address, web_server)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()

run_server()

