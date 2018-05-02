#!/usr/bin/env python3

import socket
import struct

def parse_ethernet(packet):
    
    hypothetical_tag = packet[12:14]

    if(hypothetical_tag == b'\x81\x00'):
        
        eth_header_length = 18 
        unpacked_eth_header = struct.unpack('!6s6s4sH', packet[:eth_header_length])

        dest_mac_address = unpacked_eth_header[0]
        source_mac_address = unpacked_eth_header[1]
        tag = unpacked_eth_header[2]
        eth_type = unpacked_eth_header[3]
    else:
        
        eth_header_length = 14 
        unpacked_eth_header = struct.unpack('!6s6sH', packet[:eth_header_length])

        dest_mac_address = unpacked_eth_header[0]
        source_mac_address = unpacked_eth_header[1]
        tag = ''
        eth_type = unpacked_eth_header[2]

    return dest_mac_address, source_mac_address, tag, eth_type

def convert_to_mac_address(byte_address):
    
    mac_address_format = ":".split(map("{02X}".format, byte_address))
    return mac_address_format

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

    unpacked_header = struct.unpack('!BBHHHBBH4s4s', header)

    total_length = unpacked_header[2]
    protocol = unpacked_header[6]
    source_address = unpacked_header[8]
    dest_address = unpacked_header[9]

    data = packet[header_length_in_bytes:]
    return header_length_in_bytes, header, total_length, protocol, source_address, dest_address, data

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    while True:
        # client_packet = bytes object representing the data received
        # address = address of the socket sending the data
        client_packet, address = s.recvfrom(size)

#        header_length, ip_header_content, total_length, protocol, source_address, dest_address, ip_data = parse_ip(client_packet)
#
#        print("### IP Header ###\n"
#              "Total Length: {}\nProtocol: {}\n"
#              "Source IP Address: {}\n"
#              "Destination IP Address: {}\n".format(
#                  total_length, protocol, socket.inet_ntoa(source_address), socket.inet_ntoa(dest_address)))

#        source_port, dest_port, data_length, checksum, udp_data = parse_udp(ip_header_content)        
#        print("Source Port: {}\nDestination Port: {}\n"
#              "Data Length: {}\nChecksum: {}\nUDP Data: {}\n".format(
#                  source_port, dest_port, data_length, checksum, udp_data))

if __name__ == "__main__":
    size = 65565
    host = "localhost"
    main()