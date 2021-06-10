from socket import *

with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 65535))
    print('Waiting...')
    data, addr = s.recvfrom(1435)
    data = data.decode()
    print('Client connected witn IP ', addr)
    print('Received ', data)
    data = 'All alone'
    s.sendto(data.encode(), addr)
    print('Send ', data)
input()
