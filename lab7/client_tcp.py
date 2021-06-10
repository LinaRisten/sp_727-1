from socket import *

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 65535))
    s.sendall(b'I am here')
    print('Send', 'I am here')
    data = s.recv(1435)
    print('Received', data.decode())
input()
