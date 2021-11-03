import random

opção = input("Deseja continuar de onde parou? [S]im / [N]ão:")

if opção == "S":

    with open("salvar.db","r") as fd:
        dados = fd.read()
        dados = dados.split("|")
        rand= int(dados[0])
        tries = int(dados[1])

else:
    rand = random.randint(1,1000)
    tries = 0

while True:
        user_guess = (input("Qual eh o numero? [S]alvar "))
        if user_guess == "S":
           with open("salvar.db","w") as fd:
            fd.write(f"{rand}|{tries}")
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
