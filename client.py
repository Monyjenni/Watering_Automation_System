#!/usr/bin/python3
import socket

host = socket.gethostname()
port = 5052                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
s.connect(("127.0.0.1", port))
s.sendall(b'Hello')
data = s.recv(1024)
s.close()
print('Received', repr(data))