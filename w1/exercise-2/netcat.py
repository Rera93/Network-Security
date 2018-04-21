#!/usr/bin/env python3

import socket
import sys

def handle_data(udp_socket):
    while(1):
        message_to_send = input("Enter message to send: ")
        encoded_message = message_to_send.encode("utf-8")
        udp_socket.sendto(encoded_message, (host, port))
        non_decoded_server_message, server_address = udp_socket.recvfrom(size)
        decoded_server_message = non_decoded_server_message.decode("utf-8")
        print("Server replied: " + decoded_server_message + "\n")

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("\nUDP socket is created...\n")
    except(socket.error):
        print("\nFailed to create UDP socket. \n")
        sys.exit()

    handle_data(s)
    s.close()

if __name__ == "__main__":  
    host = "localhost"
    port = 424242
    size = 65507
    main()