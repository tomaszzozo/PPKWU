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
			num1 = int(query_components["num1"])
			num2 = int(query_components["num2"])
			response = '{' + f'"sum" : {num1+num2}, "sub" : {num1-num2}, "mul" : {num1*num2}, "div" : {num1//num2}, "mod" : {num1%num2}' + '}'    
			self.wfile.write(response.encode())
		else:
			super().do_GET()
# --- main ---

PORT = 4080

print(f'Starting: c{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
