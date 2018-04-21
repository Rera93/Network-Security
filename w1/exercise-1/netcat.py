#!/usr/bin/env python3

import socket

s = socket.create_connection(("localhost", 42424))

spamming = ""
for i in range(1, 1000):
    spamming += "spam " + str(i) + "\n"

encodedSpam = spamming.encode("utf-8") 

s.sendall(encodedSpam)
print("Encoded message was sent to listening side")

s.close()