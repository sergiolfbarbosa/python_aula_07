#Crie um programa que será uma calculadora.
#Nesta calculadora você deverá ter um módulo para as
#operações matemáticas, o arquivo principal deverá
#conter apenas um menu de escolha para o usuário
#(soma, subtração, multiplicação e divisão)

from exercicio2.operacoes import * 

escolha = int(input("digite uma opção>> 1 = SOMA | 2 = SUBTRAÇÃO | 3 = MULTIPLICAÇÃO | 4 = DIVISÃO:   "))

if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
    print("Valor inválido!")
elif escolha == 1:
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    print(somar(numero1,numero2))
elif escolha == 2:
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    print(subtrair(numero1,numero2))
elif escolha == 3:
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    print(multiplicar(numero1,numero2))
elif escolha == 4:
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    print(dividir(numero1,numero2))
