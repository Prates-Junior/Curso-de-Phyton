from socket import *

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("",1234))
servidor.listen(5)

cliente,endereço = servidor.accept()
print("Bem Vindo {0}",format(endereço))

while True:
       dados = cliente.recv(2048).decode()
       print(f"cliente: {dados}")
       if dados == "sair":
              cliente.close()
              break

       dados = input("Servidor: ")
       cliente.sendall(dados.encode())
       servidor.close()