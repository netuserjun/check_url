
m socket import *
from select import *

HOST = ''
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)
print('bind')

serverSocket.listen(100)
print('listen')

clientSocekt, addr_info = serverSocket.accept()
print('accept')
print('--client information--')
print(clientSocekt)

while True:
    data = clientSocekt.recv(65535)
    print('recieve data : ',data.decode())
    msg = data.decode()
    if msg == 'exit':
        break;

clientSocekt.close()
serverSocket.close()
print('close')
