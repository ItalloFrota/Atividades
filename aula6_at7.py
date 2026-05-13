def numero_linhas(n):
    lista = []
    for i in range(n):
        if len(lista) == n:
            break
        lista.append('_*')
        if len(lista) == n:
            break
        else:
            lista.append('*_')
    return lista
n = int(input("Digite o número de linhas: "))
resultado = numero_linhas(n)
for linha in resultado:    print(linha)