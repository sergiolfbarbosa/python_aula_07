#FUNÇÃO QUE RECEBE UMA STRING E RETORNA A QUANTIDADE DE CARACTERES DESSA STRING
#FUNÇÃO QUE RECEBE UMA STRING E RETORNA QUANTAS VOGAIS TEM NESSA STRING
#FUNÇÃO QUE RECEBE UMA STRING E RETORNA QUANTAS CONSOANTES TEM NESSA STRING
#FUNÇÃO QUE RECEBE UMA STRING E RETORNA QUANTOS ESPAÇOS VAZIOS TEM NESSA STRING

def contar_caracteres(texto):
    # return len(texto)
    contador = 0
    for letra in texto:
        contador +=1
    return contador


def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra in "aeiouáâãéêíóôõú":
            contador +=1
    return contador

def contar_consoantes(texto):
    contador = 0
    for letra in texto:
        if letra in "bcdfghjklmnpqrstvxywz":
            contador +=1
    return contador


def contar_vazios(texto):
    contador = 0
    for letra in texto:
        if letra == " ":
            contador +=1
    return contador