#!/usr/bin/env python3

import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("\nUDP socket is created...\n")
    except(socket.error):
        print("\nFailed to create UDP socket. \n")
        sys.exit()

    s.close()

if __name__ == "__main__":  
    host = "localhost"
    port = 424242
    size = 65507
    main()