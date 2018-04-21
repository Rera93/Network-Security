#!usr/bin/env python3

import socket
import sys
        
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\nUDP socket is created...\n")
    except(socket.error):
        print("\nFailed to create UDP socket. \n")
        sys.exit()

    try:
        s.bind((host, port))
        print(host + " is bound to UDP socket at port " + str(port) +".\n")
    except(socket.error):
        print("Binding " + host + " at port " + str(port) + " has failed.\n")
        sys.exit()

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    size = 65507
    main()

