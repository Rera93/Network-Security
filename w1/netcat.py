#!/usr/bin/env python3

import socket

s = socket.create_connection(("localhost", 42424))
s.sendall("Shkeputu".encode("utf-8"))
s.close()