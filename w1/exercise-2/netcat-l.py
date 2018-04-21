#!usr/bin/env python3

import socket
import sys
        
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\nUDP socket is created...\n")
    except(socket.error):
        print("\nFailed to create UDP socket. \n")

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    size = 65507
    main()

