def InverterString(texto):
    return texto [::-1]

def QuantidadePalavras(texto):
    count = 0
    for i in texto:
        if i == " ":
            count += 1
    return count + 1
    
def VerificaPolimetro(texto):
    texto_invertido = texto [::-1]
    if texto_invertido == texto:
        return f"É polímero {texto_invertido}"
    else:
        return f"Não é polímero, original > {texto} e invertido >{texto_invertido}."
    

