#!usr/bin/env python3

import socket

host = "localhost"
port = 42424
size = 1024
backlog = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

conn, clientaddress = s.accept()

data = conn.recv(size)

if data:
    datastring = data.decode("utf-8")
    print(datastring)

conn.close()
s.close()

