from socket import *

with socket(AF_INET, SOCK_STREAM) as soc:
    soc.bind(('127.0.0.1', 65535))
    soc.listen()
    print('Waiting...')
    conn, addr = soc.accept()
    with conn:
        print('Client connected witn IP ', addr)
        data = conn.recv(1435).decode()
        print('Received ', data)
        data = 'All alone'
        conn.sendall(data.encode())
        print('Send ', data)
input()        
