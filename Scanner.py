import os
from Funcoes import get_ip,scanner
import threading

meu_ip = (get_ip())
rede = meu_ip[:meu_ip.rfind(".")+1]
clientes = []
threads = []

lock = threading.Lock()

for item in range(1,255):
    teste = rede + str(item)
    t = threading.Thread(target=scanner,args =(teste,clientes,lock,))
    t.start()
    threads.append(t)

for thread in threads:
        thread.join()

print(clientes)


