import random

opção = input("Deseja continuar de onde parou? [S]im / [N]ão:")

if opção == "S":
    fd = open("salvar.db","r")
    dados = fd.close()
    dados = dados.split("|")
    dados = dados[0]
    tries = dados[1]
    fd.close()
else:
    rand = random.randint(1,1000)
    tries = 0

while True:
        user_guess = (input("Qual eh o numero? [S]alvar "))

        fd = open("salvar.db","w")
        fd.write(f"{rand}|{tries}")
        fd.close()
        exit(0)

        user_guess = int(user_guess)

        if user_guess == rand:
                break

        elif user_guess > rand:
                print("Your number is bigger")
                tries += 1
        else:
                print("Your number is lower")
                tries += 1

print ("You win in {0} tries".format(tries))
