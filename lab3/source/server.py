#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
	def do_GET(self):

		print(self.path)
        
		if self.path.startswith('/?str='):
			for c in self.path[6:]:
				if c.islower():
					lowercase += 1
				elif c.isupper():
					uppercase += 1
				elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
					digits += 1
				else:
					special += 1
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
