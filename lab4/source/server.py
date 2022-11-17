#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
from urllib.parse import urlparse, parse_qs

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
	def do_GET(self):

		print(self.path)
        
		if self.path.startswith('/?'):
			query = urlparse(self.path).query
			query_components = dict(qc.split("=") for qc in query.split("&"))
			self.protocol_version = 'HTTP/1.1'
			self.send_response(200)
			self.send_header("Content-type", "text/html; charset=UTF-8")
			self.end_headers()  
			response = str(query_components['test'])       
			self.wfile.write(response.encode())
							
			return
			tring = unquote(self.path[6:])
			lowercase = sum(1 for c in string if c.islower())
			uppercase = sum(1 for c in string if c.isupper())
			digits = sum(list(map(lambda x:1 if x.isdigit() else 0,set(string))))
			special = len(string)-lowercase-uppercase-digits
			self.protocol_version = 'HTTP/1.1'
			self.send_response(200)
			self.send_header("Content-type", "text/html; charset=UTF-8")
			self.end_headers()  
			response = '{' + f' "lowercase" : {lowercase}, "uppercase" : {uppercase}, "digits" : {digits}, "special" : {special}' + '}'        
			self.wfile.write(response.encode())
		else:
			super().do_GET()
# --- main ---

PORT = 4080

print(f'Starting: c{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
