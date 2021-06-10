from socket import *

with socket(AF_INET, SOCK_DGRAM) as s:
    data = b'I am here'
    s.sendto(data, ('127.0.0.1', 65535))
    print('Send', 'I am here')
    data, _ = s.recvfrom(1435)
    print('Received', data.decode())
input()
