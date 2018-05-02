#!/usr/bin/env python3

import socket
import struct

def parse_udp(packet):
    header_length = 8
    header = packet[:header_length]
    data = packet[header_length:]

    (source_port, dest_port,
     data_length, checksum) = struct.unpack("!HHHH", header)

    return source_port, dest_port, data_length, checksum, data

def parse_ip(packet):
    header_length_in_bytes = (packet[0] & 0x0F) * 4
    header = packet[:header_length_in_bytes]
    data = packet[header_length_in_bytes:]
    return header_length_in_bytes, header, data

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    while True:
        # client_packet = bytes object representing the data received
        # address = address of the socket sending the data
        client_packet, address = s.recvfrom(size)





if __name__ == "__main__":
    size = 65565
    host = "localhost"
    main()