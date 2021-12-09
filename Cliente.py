from socket import *

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect(("127.0.0.1", 1234))

while True:
    dados = input("Cliente:")
    cliente.sendall(dados.encode())
    if dados == "sair":
        cliente.close()
        break

        dados = cliente.recv(2048).decode()
        print(f"Servidor: {dados}")





print (dados)
