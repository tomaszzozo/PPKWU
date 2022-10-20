#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!<br>")
        elif self.path == '/?cmd=time':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            now = datetime.datetime.now()
            self.wfile.write(str(now).encode()[11:19])
        else:
            parameters = self.path[2:].split('&')
            if len(parameters) == 2:
		        p1 = parameters[0].split('=')
		        p2 = parameters[1].split('=')
		        parameters = [p1[0], p2[0]]
		        values = [p1[1], p2[1]]
		        if 'cmd' in parameters and 'str' in parameters and values[0] == 'rev':
		        	self.protocol_version = 'HTTP/1.1'
		        	self.send_response(200)
		        	self.send_header("Content-type", "text/html; charset=UTF-8")
		        	self.end_headers()            
		        	self.wfile.write(values[1][::-1].encode())
		        else:
		        	super().do_GET()
            else:
            	super().do_GET()
# --- main ---

PORT = 4080

print(f'Starting: c{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
