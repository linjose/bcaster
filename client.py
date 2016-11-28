#!/usr/bin/python
# client.py

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.122.139', 8001))

import time
time.sleep(2)
sock.send('test')
print sock.recv(1024)
sock.close()
