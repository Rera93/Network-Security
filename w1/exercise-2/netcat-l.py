#!usr/bin/env python3

import socket
import sys

def handle_data(udp_socket):
    while(1):
        non_decoded_data, client_address = udp_socket.recvfrom(size)
        decoded_data = non_decoded_data.decode("utf-8")
        if decoded_data:
            confirm_with_client = "Message: " + decoded_data + " || SUCCESS ||"
        else:
            confirm_with_client = "Message: " + decoded_data + " || FAILED ||"
        udp_socket.sendto(confirm_with_client.encode("utf-8"), client_address)
        print("[ " + client_address[0] + ", " + str(client_address[1]) + " ] said " + decoded_data + ".\n")
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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

    handle_data(s)
    s.close

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    size = 65507
    main()

