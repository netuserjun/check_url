from socket import *
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',8081))
serverSock.listen(1)

clineSock, addr = serverSock.accept()
connectionSock, addr = serverSock.accept()
