num = int(input("digite um número:"))
matriz = []
for i in range(num):
    linha = []
    for j in range(num):
        linha.append(i + j)
    matriz.append(linha)
for linha in matriz:
    print("".join(map(str, linha)))