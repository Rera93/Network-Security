#!usr/bin/env python3

import socket

def handle(passedconn, conn_number):
    data=b""
    newdata = passedconn.recv(size)
    
    while newdata:
        data += newdata
        newdata = passedconn.recv(size)
        
    if data:
        datastring = data.decode("utf-8")
        filter_out_spam = datastring.replace("spam ", "")
        print(filter_out_spam)
        
    passedconn.close()
    print("Connection " + str(conn_number + 1) + " has terminated.\n")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
    print("Listening on port " + str(port) + "...\n")

    for i in range(0, 3):
        conn, clientaddress = s.accept()
        handle(conn, i)
    s.close()

if __name__ == "__main__":
    host = "localhost"
    port = 42424
    size = 1024
    backlog = 5
    main()

