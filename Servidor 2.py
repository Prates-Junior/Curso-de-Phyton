from socket import *
import threading


servidor = socket(AF_INET,SOCK_STREAM)
servidor.bind(("",2222))
servidor.listen(5)


clientes = []

#Msgs dos Clientes
def conexao(cliente):
    while True:
        dados = cliente.recv(2048).decode()
        print(f"Cliente: {dados}")
        # verifica se o cliente quer sair
        if dados == "sair":
            clientes.remove(cliente)
            cliente.close()
            break
        for msg in clientes:
            msg.sendall(dados.encode())

    # Clientes se conectando

while True:
    cliente,endereço = servidor.accept()
    clientes.append(cliente)

    t = threading.Thread(target = conexao,args =(cliente,))
    t.start()
