num = int(input("Digite um número:"))
print("=" * 60) 
for i in range(num):
    print("*" * num)
print("=" * 60) 
matriz = []
for i in range(num):
    lista = []
    for j in range(num):
        lista.append('*')
    matriz.append(lista)
for lista in matriz:
    print("".join(lista))