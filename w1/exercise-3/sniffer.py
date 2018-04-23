#!usr/bin/env python3

import socket
import struct

def parse_udp(packet):
    header_start = 0
    header_length = 8
    header = packet[header_start:header_start+header_length]

    (source_port, dest_port, data_length, checksum) = struct.unpack("!HHHH", header)

    print("Source Port: {} \n"
          "Destination Port: {}\n"
          "Data Length: {}\n"
          "Checksum: {}\n".format(source_port, dest_port, data_length, checksum))
    
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    while(1):
        parse_udp(s.recvfrom(size))

if __name__ == "__main__":
    size = 66565 
    main()
    