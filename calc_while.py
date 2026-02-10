print ('Bem Vindo a Primeira Cálculadora!')
while True:

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    escolha = input('Escolha o tipo de operação ')

    if escolha == "0":
        break

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite outro número: '))

    if escolha == '1':
        print(num1 + num2)
    elif escolha == '2':
        print(num1 - num2)
    elif escolha == '3':
        print (num1 * num2)
    elif escolha == '4':
        print (num1 / num2)
    else:
        print ('número incorreto')

