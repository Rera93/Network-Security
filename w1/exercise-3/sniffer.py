#!usr/bin/env python3

import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    while(1):
        print(s.recvfrom(size))

if __name__ == "__main__":
    size = 66565 
    main()
    