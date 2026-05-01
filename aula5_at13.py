frase = input('Digite uma frase:')
frase = frase.lower()
frase_vogais = 0
frase_consoantes = 0
frase_espaços = 0
for i in frase:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        frase_vogais += 1
    elif i == ' ':
        frase_espaços += 1
    else:
        frase_consoantes += 1
print('O número de vogais da frase é:', frase_vogais)
print('O número de consoantes da frase é:', frase_consoantes)
print('O número de espaços da frase é:', frase_espaços)