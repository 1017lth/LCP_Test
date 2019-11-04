import socket

IP = "127.0.0.1"
PORT = 6091
MESSAGE = "HELLO"
MESSAGE = MESSAGE.encode("ascii")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE,(IP,PORT))

