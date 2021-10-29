from Funcoes import calculadora


while True:

    operador = input("insira um operador(+,-,*,/)")
    if operador == "sair":
        break


    resultado = calculadora(ação= operador)
    print(resultado)














