import exercicios.caracteres as caracteres

texto_usuario = str(input("Digite um texto qualquer: "))

print(caracteres.contar_caracteres(texto=texto_usuario))
print(caracteres.contar_consoantes(texto=texto_usuario))
print(caracteres.contar_vazios(texto=texto_usuario))
print(caracteres.contar_vogais(texto=texto_usuario))