def comparador(a, b):
    posicao = []
    for i in range(len(a)):
        if a[i] == b[i]:
            posicao.append(f'Posição {i + 1} igual {a[i]}')
        elif a[i] > b[i]:
            posicao.append(f'Posição {i + 1} maior {a[i]}')
        else:
            posicao.append(f'Posição {i + 1} maior {b[i]}')
    return posicao
while True:
    lista1 = input("Digite a primeira lista de palavras separadas por espaço: ").split()
    lista2 = input("Digite a segunda lista de palavras separadas por espaço: ").split()
    for i in lista1:
        if not i.replace('.', '', 1).isdigit():
            print("Por favor, digite apenas números nas listas.")
            break
    for i in lista2:
        if not i.replace('.', '', 1).isdigit():
            print("Por favor, digite apenas números nas listas.")
            break
    if len(lista1) != len(lista2):
        print("As listas devem ter o mesmo número de palavras. Por favor, tente novamente.")
    else:
        lista1 = [float(palavras) for palavras in lista1]
        lista2 = [float(palavras) for palavras in lista2]
        break
resultado = comparador(lista1, lista2)
for item in resultado:    print(item)