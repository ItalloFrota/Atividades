def contador_vogais(lista):
    vogais = 'aeiouAEIOU'
    contador = 0
    for palavra in lista:
        for letras in palavra:
            if letras in vogais:
                contador += 1
    return contador
while True:
    palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
    if palavras:
        break
    else:
        print("A lista de palavras não pode ser vazia. Por favor, tente novamente.")

resultado = contador_vogais(palavras)
print(f"Total de vogais: {resultado}")