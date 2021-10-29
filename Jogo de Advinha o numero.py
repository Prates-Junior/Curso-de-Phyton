import random
rand = random.randint(1,1000)

num = 0

while True:
    num = int(input("Digite um numero de 1 a 1000"))
    if num == rand:
        break
    elif num > rand:
        print("Parabéns, seu numero eh maior")
        num += 1
    else:
        print("seu numero eh menor")
        num += 1
print("você venceu em {0)".format(num))

import random

arquivo = open("log.txt", "r")
dado_lido = arquivo.read()
if dado_lido:
    numero = int(dado_lido)
    print(numero + 1)
    arquivo.close()



arquivo = open("log.txt", "w")
numero_pesquisado = random.randrange(1,100)
arquivo.write(str(numero_pesquisado))
arquivo.close()