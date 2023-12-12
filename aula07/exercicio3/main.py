#Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings,
#como inverter uma string, contar o número de palavras em uma string e verificar se uma string é um
#palíndromo (lê-se igual de trás para frente). Crie um programa principal que importe o módulo e use
#essas funções com strings fornecidas pelo usuário.

from manipulacao_string import *

texto_usario = str(input("Digite algo: "))

print(InverterString(texto=texto_usario))
print(QuantidadePalavras(texto=texto_usario))
print(VerificaPolimetro(texto=texto_usario))
